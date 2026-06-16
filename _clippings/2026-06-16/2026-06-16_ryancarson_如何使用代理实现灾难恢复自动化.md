---
title: "2026-06-16_ryancarson_如何使用代理实现灾难恢复自动化"
source: "https://x.com/ryancarson/status/2064751272834593135"
author:
  - "[[@ryancarson]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "x"
  - "@ryancarson"
  - "restore"
  - "maintenance"
---

# 如何使用代理实现灾难恢复自动化

**Ryan Carson**

# 如何使用代理实现灾难恢复自动化

你是早期采用者，你的代理已经交付了你所有功能、漏洞修复和重构的100%。给自己点个赞吧。

现在是时候升级到 <span id=2> 自动化代理驱动灾难恢复 。

(作弊码：只需将你的代理指向这篇帖子并说“实施这个”。)

数据库恢复是你整个系统中最可怕的按钮。它具有破坏性，使用场景罕见，而当你真正需要它的时候，你会在凌晨2点惊慌失措，拼命回想哪个备份才是正确的。

这正是那种高风险、低频率的流程，应该被记录为一个操作手册，供你的代理执行——而且，关键是，一个你已经在实际条件下测试过，在你需要它之前。

这篇文章介绍了我们如何设置以下内容：两种独立的备份策略（时间点恢复和异地转储）、我们的代理遵循的单一操作手册、我们如何触发它、如何验证它，以及我们如何在不丢失数据的情况下对生产环境进行实时破坏性测试。

[@DevinAI](https://x.com/@DevinAI)

在整个过程中，有两个标准术语值得牢记，因为这是有经验的操作人员思考这个问题的方式

- RPO (Recovery Point Objective): how much data you can afford to lose, measured in time. A daily backup implies an RPO of up to ~24h; continuous PITR gets you to seconds.
- RTO (Recovery Time Objective): how long recovery is allowed to take.

另一个试金石是经典的 3-2-1 规则：至少 3 份数据，存储在 2 种不同的介质/系统上，其中 1 份存放在异地。以下所有内容实际上只是 3-2-1 规则的具体、由代理操作的实施方式，并且有明确的 RPO/RTO 目标。

## 为什么是两个备份而不是一个

备份的黄金法则：

A backup you haven't restored is just a hope.

单一的备份策略是单点故障。我们使用两个，因为它们以不同的方式失效，并且覆盖不同的灾难：

1\. 时间点恢复（PITR）——您的快速“撤销”

Most modern managed Postgres providers (we use

[@neondatabase](https://x.com/@neondatabase) - it integrates really easy with

[@vercel](https://x.com/@vercel)

; Supabase, RDS, Cloud SQL, and others have equivalents) keep a continuous change history and let you roll the database back to any moment within a retention window (ours is 7 days).

- Best for: "We just ran a bad migration / a bad delete / a buggy deploy 20 minutes ago." You roll back to the timestamp just before the damage. (Excellent RPO — seconds.)
- Granularity: to the second.
- 速度（RTO）： 由服务提供商决定——不要假设“即时”。 在 Neon 中，恢复是一种写时复制分支操作，几乎是即时的。在 RDS / Cloud SQL 中，PITR 通过基础快照+WAL 重放提供一个全新的实例从基础快照+WAL 重放开始，可能需要数十分钟到数小时，之后进行切换。了解您的服务提供商的恢复机制，并在演练期间安排时间，以便您的 RTO 是一个可测量的数值，而非猜测。
- 杀手级功能：它是可逆的。当你进行恢复时，提供方会将恢复前的状态作为一个独立的分支/快照保留下来。如果你的恢复操作有误，你可以撤销这个撤销操作。
- The catch: it lives inside the same provider account as your live database. If that account is compromised, deleted, or the provider has a catastrophic failure, your PITR history can go with it.

2\. 异地备份 — 您的“大楼失火”级别的备份

This is a backup written to object storage in a different vendor (we use AWS S3; GCS, Cloudflare R2, Backblaze B2 all work). A cron job runs it on a schedule (daily, in our case).

我们使用简单的 pg\_dump，并且诚实地说明什么时候这是合适的工具：

- Logical dumps (pg\_dump) are great for small-to-mid databases — say up to tens of GB. They're simple, portable across Postgres versions, and trivial to inspect. But they don't scale well: dumps and (single-threaded) restores get painfully slow as the DB grows, and a nightly dump gives you a coarse RPO (up to ~24h).
- For larger or higher-RPO systems, graduate to physical backups + continuous WAL archiving to object storage — tools like pgBackRest, WAL-G, or Barman. These give you off-site point-in-time recovery (not just a nightly snapshot), parallel/faster restores, and far better RPO. If your DB is big or your RPO target is tight, treat nightly pg\_dump as a starter and plan the upgrade.

无论机制如何：

- Best for: the provider account itself is gone, corrupted, or locked. Or you need a backup older than the PITR window. Or compliance wants an immutable, exportable copy.
- 粒度 (RPO): 无论你的备份/归档频率如何（每日转储 = 潜在损失最多~24 小时；WAL 归档 = 秒级）
- Speed (RTO): slower than PITR — you download and replay. For a logical dump, restore time grows with DB size.
- The killer feature: it's off-site and vendor-independent. Totally separate blast radius from your primary DB.
- 关键问题：逻辑转储是粗粒度的，并且只有在你最后一次运行时才是最新的。

同时拥有两者的意义在于：PITR 是你日常的、细粒度的、快速回滚工具。异地备份则是应对最坏情况的保障。在实际事件中，你通常会同时使用它们——而这正是我们演练过的场景（更多内容见下文）。

## 步骤1：设置两个备份

You need these to exist before you write the playbook. An agent can help you build all of this.

时间点恢复

- 确认您的服务提供商支持 PITR 并检查保留窗口（例如，7 天）。如果预算允许，请延长该窗口时长——更长的窗口意味着您可以从更多灾难中恢复。
- 验证恢复操作保留先前状态 (Neon 会通过自动分支操作实现这一点)。可恢复性是确保在线测试安全的关键。

异地转储

- 一个定时任务（GitHub Actions cron、Vercel cron、Lambda——任何合适的方式），该任务运行 pg\_dump，对其进行 gzip 压缩，然后上传到一个不同供应商的存储桶中。（在大规模场景下，可将其替换为 pgBackRest/WAL-G 等 WAL 归档工具，这些工具会写入同一个存储桶。）
- 一个带有版本控制和合理生命周期/保留策略的存储桶。如果你需要防勒索软件、防篡改的副本，请考虑对象锁定 / 不可变。
- A read-only, least-privilege credential scoped to only that backup bucket, that the agent can use to list and download dumps. Don't hand your agent your root keys.
- 额外提示：启用手动触发器（例如 workflow\_dispatch），以便您可以在几分钟内生成按需转储，而不是等待夜间运行。

> 💡 提示：了解你的实际转储时间，而不是 cron 表达式。我们的计划时间是 UTC 03:00，但由于 CI 队列时间的关系，实际执行时间大约在 UTC 04:30。这个细节在你考虑“我们会丢失多少数据”时很重要。

## 步骤 2: 编写操作手册

In Devin, a playbook is a first-class, reusable procedure you author once and then attach to any session. You create it in the Devin web app (Settings → Playbooks), give it a name and a trigger macro (ours is !database\_restore), and write the body as a plain-language, step-by-step runbook. From then on, anyone on the team can start a Devin session, attach that playbook (or type the macro), and Devin loads those instructions and executes them itself — calling the database/provider APIs, running psql, toggling maintenance mode, and reporting back. You're not writing code that Devin calls; you're writing the checklist Devin follows.

如果您使用的是没有操作手册概念的其他代理，那么在提示词中引用的、您代码仓库中结构良好的 RESTORE.md 文件的内容，将帮助您完成大部分工作。

The key insight: the playbook is the runbook. You're writing the checklist a careful human would follow, precisely enough that the agent can execute it without improvising on the dangerous parts.

我们的有两种模式：

- VALIDATION mode (default, non-destructive): restore into a throwaway branch, check the data looks right, throw it away. This is what you run on a schedule to keep yourself honest. It touches nothing real.
- DISASTER mode (destructive, requires explicit authorization): the real thing, against the live database.

一个好的恢复操作手册按顺序说明：

1.  Triage first. Confirm it's actually a data problem and establish the exact restore timestamp ("restore to just before 09:15 UTC").
2.  将应用程序置于维护模式，在操作数据库之前，这样应用程序写入和定时任务会停止，并且在恢复过程中不会出现数据损坏。（见步骤 4 — 使这一步即时完成，并注意其实际限制：中间件停止前门写入，并非所有可能的写入操作。）
3.  选择路径：PITR 窗口内的损坏且服务提供商正常 → PITR。服务提供商账户被入侵，或您需要旧版本/异地副本 → S3 dump。
4.  Snapshot the current state first, even though it's broken — name it something obvious like main-before-restore-<timestamp>. This is your "undo the undo" safety net.
5.  Execute the restore (the specific provider API calls or psql commands).
6.  Verify (Step 5 below) — while still in maintenance mode.
7.  Only if verification passes, lift maintenance mode.
8.  Report: what was restored, to when, the safety branch name, total downtime, and before/after row counts.

需要整合到操作手册中的事项，以确保代理不会自毁

- Hard gates: "If verification fails, leave maintenance mode ON and stop. Do not lift maintenance on a bad restore."
- 无中断中止预检：检查凭证并确保转储可下载/有效，在启用维护之前。如果 S3 不可访问，你会在关闭网站之前发现这一点。
- 永远不要删除安全分支，作为运行的一部分。清理是一个单独的、需人工批准的决定。
- Require explicit authorization for DISASTER mode.

剧本 vs. 技能 — 有什么区别？

The rule of thumb: if you want the agent to decide on its own when to apply some knowledge, make it a skill. If you want a human to deliberately pull a lever, make it a playbook.

A destructive database restore is the textbook case for a playbook, not a skill. You never want an agent to auto-decide it's time to overwrite production — that's a lever a human pulls on purpose, with authorization, which is exactly what a manually-attached playbook gives you. (Skills are perfect for the non-destructive habits around it — e.g. a repo skill that says "here's how to run a scheduled validation restore into a throwaway branch.")

## 步骤 3：触发代理

我们有两种触发它的方式，针对两种不同的情况

A real incident (you, manually): open a Devin session, attach the playbook or type its macro (!database\_restore), and tell it what happened: "We had a bad delete around 09:15 UTC, restore production to 09:10." Devin loads the playbook and walks the steps, pausing where the playbook says to pause.

A supervised drill (Devin spawns a child Devin): for our live test, we had a main Devin session spin up a separate child Devin session dedicated to running the playbook, and watched it work in real time. Devin can launch and monitor child sessions, which makes this clean:

- 子节点在其自己的机器上端到端执行该过程。
- 父端监控进度，不进行干预，并向您传递里程碑事件（“维护开启”、“恢复完成”、“已验证”、“维护关闭”）。
- 你会得到一份清晰且可审计的、确切记录所做内容的记录。

## 步骤 4: 使维护模式立即生效

This is the unsung hero of a safe restore. You cannot do a clean restore while writers are hitting the database. You need a switch that, in seconds:

- 将所有流量路由到维护页面
- stops application-driven writes,
- 并暂停 cron/后台作业。

准确说明“维护模式”实际上冻结了什么。应用层中间件仅阻止通过应用前端入口的写入操作。它不会自动停止：后台工作器和队列消费者、命中其他入口点的入站 webhook、已在运行中的计划任务，或任何直接连接到数据库的内容。

Your maintenance switch has to also gate those paths (we freeze cron and reject writes in the API/server-action layer), and you should accept that a small number of in-flight writes can still land in the instant the flag flips. The only true write freeze is at the database itself — e.g. revoking write privileges, flipping the DB to read-only, or terminating all other connections. For a short restore window, app-layer gating plus paused cron is usually enough; just don't tell yourself it's a hard guarantee.

需要避免的错误：将维护操作设置为需要环境变量才能通过重新部署来切换。在发生故障时，等待3–5分钟进行部署以切换维护状态简直是煎熬，并且会扩大数据丢失窗口。

We made it instant and deploy-free using a low-latency edge config store (we use Vercel Edge Config; a Redis key or any fast KV store works) read on every request in middleware:

- 中间件在每个请求上检查的维护模式标志会将所有内容重定向到/maintenance。
- 标志在~1–3 秒内通过 API 调用切换 — 无需重新部署。
- 故障开放（一种刻意的可用性权衡）： 如果配置读取错误，默认提供流量而不是显示维护状态， 这样配置存储的小故障就不会导致整个网站瘫痪。 这种权衡的含义是，故障期间的配置中断不会自动阻止写入——如果您更希望确保阻止写入， 则应选择故障关闭。 有意选择故障模式。
- 额外提示：将维护页面的标题/消息/预计恢复时间存储在同一配置中，以便您可以实时更新文案（例如“美国东部时间10:30前恢复”）而无需部署代码。

我们为此给代理程序提供了一个小型命令行界面（CLI），用于维护模式（on|off|status），因此剧本步骤只需一条命令。

## 步骤 5：检查它是否真的能正常工作（不影响生产环境）

Build verification into a routine you run constantly, not just during incidents:

- Scheduled VALIDATION restores. Have the agent restore the latest off-site dump into a throwaway branch on a schedule, run sanity checks, and report. If the dump is corrupt or the restore mechanics broke, you learn it on a Tuesday afternoon — not during a fire.
- 有实际意义的完整性检查。关键表（用户表、核心域表）的行数统计，确认所有模式都存在，并检查最新时间戳，以确认高写入表中的数据新鲜度。
- 凭证检查。确认代理的备份凭证以预期的最小权限身份进行身份验证并且能够列出/读取存储桶。(更多原因见下文。)

> ⚠️ The kind of bug drilling catches. Drills routinely surface problems that look fine on paper: a stale or mis-scoped credential, a backup identity that's lost read access to the bucket, an expired key, an IAM policy that quietly drifted. These are invisible until someone actually exercises the path — and they tend to bite hardest in a fresh, cold-start emergency session that doesn't have your laptop's cached state. Running the drill flushes them out with zero production impact, so you fix the credential/policy centrally and re-run before it matters. The backups you never test are the ones that betray you.

## 步骤 6：进行真实的、实际的破坏性测试

First, the standard practice, stated plainly: the normal, safe way to test restores is non-destructively, into a separate branch / clone / staging instance (Step 5). You should be doing that on a schedule, and for most teams that's sufficient — it proves the dump is good and the restore mechanics work without ever risking production. If you're not comfortable touching prod, don't; a restored-clone drill is a perfectly respectable answer.

That said, a clone drill doesn't exercise the production-specific glue: your maintenance switch, your real DNS/edge routing, your actual credentials in a cold session, and the muscle memory of doing it for real. So — as an advanced, optional, heavily-gated exercise — we also ran the full thing against production once. This section is about how to do that without it being reckless. It is not a substitute for routine clone-based validation; it's a deliberate, one-time confidence check on top of it. 话虽如此，克隆演练并不锻炼生产特定的核心连接：你的维护开关、真实的 DNS/边缘路由、冷会话中的实际凭证，以及真实操作时的肌肉记忆。因此——作为一项高级、可选、受严格管控的演练——我们也曾针对生产环境完整运行过一次。本节介绍如何在不鲁莽的情况下做到那操作而不鲁莽行事。它不是常规基于克隆的验证的替代品；而是在其基础上进行的一种刻意的、一次性的信心检查。

The trick that makes it safe: freeze writes first, so both restore targets converge on the same moment. If you enable maintenance mode at time T0, (almost) nothing is written after T0. So restoring "to T0" loses essentially nothing — the only data at risk is whatever was in flight the instant the flag flipped (see the in-flight-writes caveat in Step 4). And because PITR is reversible (preserved branch) and the off-site copy is untouched, every step has an undo.

We went further and practiced a realistic two-path chain in a single maintenance window, because in a real incident you might genuinely need both:

1.  Enable maintenance mode. Record T0. Capture baseline row counts.
2.  Snapshot current production to a safety branch.
3.  Restore from the off-site S3 dump (this rolls production back to the dump's timestamp — the off-site fallback path).
4.  验证 S3 恢复已完成：架构完整，数量正常。
5.  通过 PITR 恢复丢失的时间 — 向前滚动生产到 T0，恢复转储和冻结之间的所有内容。（S3 状态首先保存在其自己的分支中。）
6.  验证与基准进行对比。我们检查了关键表的行数、模式存在情况以及最新时间戳。值得说明的一个警告：行数匹配是必要的，但不充分 — 行数相等并不证明内容相等。为了真正有信心，还需比较一些内容敏感的内容：关键表的校验和/哈希值（例如，在确定性排序下的 md5(array\_agg(...))）、一些抽样检查的行，或者 pg\_dump --schema-only 的差异。行数是快速的第一道关卡；校验和才是证明。
7.  Lift maintenance mode. Smoke-test: homepage 200, login redirect works.
8.  Report a three-state table: BASELINE → POST-S3 → POST-RECOVERY.

这证明了：异地转储可以正确恢复，并且之后你可以从 PITR 恢复——也就是当你必须回退到异地副本并随后追回最近数据时需要执行的确切步骤。

我们的实际结果：整个链路在一个约8分钟的维护窗口内运行，准确恢复到基准计数，通过保留的分支全程完全可逆。(我们验证了计数和时间戳；对于生产级别的签署，我们会按照上述说明添加表校验和。)

实时测试安全检查清单:

- 你必须 <span id=2> 显式授权才能对生产进行破坏性运行。
- Maintenance mode is instant and verified working before you start.
- Pre-flight checks (creds + dump integrity) run before any outage, with a clean abort path.
- Every destructive step preserves the prior state in a named branch.
- Hard gate: if any verification fails, maintenance stays ON and the agent stops.
- You run during a low-traffic window.
- You captured baseline counts to compare against.
- 安全分支的清理是一个独立的、审慎的、经人工批准的后续步骤。

## 关于凭证和最小权限的说明

给你的代理一个凭证，能够恰好完成剧本所需的操作，不多也不少：

- Backup reads: a read-only key scoped to only the backup bucket. It should be able to list and download dumps — not delete them, not touch other buckets.
- Restore operations: the provider API key needs restore/branch permissions, but you can still keep it off destructive account-level actions.
- Store these as shared secrets at the org/team level so a fresh agent session inherits the correct ones automatically — then verify a clean, cold session actually picks them up. Stale or mis-scoped secrets are one of the most common things a drill exposes, so treat "a brand-new session can authenticate as the expected least-privilege identity" as an explicit test, not an assumption.

## 核心要点

Disaster recovery is the perfect thing to delegate to an agent, if you do the prep:

1.  Two backups, different blast radii — point-in-time (fast, fine-grained, reversible, same provider) and off-site dump (coarse, slow, vendor-independent).
2.  A playbook that encodes the careful-human procedure: triage → maintenance mode → snapshot → restore → verify → (only then) lift maintenance → report — with hard safety gates.
3.  Instant, deploy-free maintenance mode so freezing writes takes seconds, not a redeploy.
4.  持续非破坏性验证，加上至少一个真实现场演练以证明端到端路径——以及排查出类似失效凭证形状的意外情况，在它们造成影响之前。

你第一次执行生产恢复操作时，不应该是你首次运行生产恢复操作的时候。

Write the playbook, hand it to your agent, and drill it — so when something breaks for real, recovery is a calm, eight-minute, well-rehearsed procedure instead of a panic.