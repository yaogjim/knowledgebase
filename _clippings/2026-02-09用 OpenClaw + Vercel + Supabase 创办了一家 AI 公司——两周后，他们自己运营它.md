---
title: 2026-02-09用 OpenClaw + Vercel + Supabase 创办了一家 AI 公司——两周后，他们自己运营它
source: https://x.com/Voxyz_ai/status/2019914775061270747
author:
  - ""
created: 2026-02-09 11:54:16
date: 2026-02-09 11:54:16
description: ""
tags:
---
> 6 个 AI 代理，1 台 VPS，1 个 Supabase 数据库——从“代理能够对话”到“代理自主运行网站”花了我两周时间。本文正好涵盖了中间缺失的部分、如何解决这些问题，以及一个你可以带回家使用的架构。

如果你最近一直在使用 AI 代理，很可能你已经配置好了 OpenClaw。

它解决了一个大问题：让 Claude 使用工具、浏览网页、操作文件和运行定时任务。你可以给代理分配 cron 任务——每日推文、每小时情报扫描、定期研究报告。

My project is called VoxYZ Agent World — 6 AI agents autonomously operating a website from inside a pixel-art office. The tech stack is simple: 

-   OpenClaw (on VPS): The agents' "brain" — runs roundtable discussions, cron jobs, deep research 
    
-   Next.js + Vercel: Website frontend + API layer 
    
-   Supabase: Single source of truth for all state (proposals, missions, events, memories) 
    

六个角色，每个角色有一项职责：Minion 做决策，Sage 分析策略，Scout 收集情报，Quill 撰写内容，Xalt 管理社交媒体，Observer 进行质量检查。

OpenClaw 的定时任务让它们每天“上班”。Roundtable 让它们讨论、投票并达成共识。

代理生成的所有内容——草稿推文、分析报告、内容作品——都停留在 OpenClaw 的输出层。没有任何东西将其转化为实际执行，执行完成后也没有任何东西告诉系统“完成”。

Between "agents can produce output" and "agents can run things end-to-end," there's a full execute → feedback → re-trigger loop missing. That's what this article is about. 

让我们首先定义“闭环”，以便我们不会构建错误的东西。

Agent 提议一个想法（提案） ↓ 自动审批检查（自动审批） ↓ 创建任务 + 步骤 (任务 + 步骤) ↓ 工作器认领并执行（Worker） ↓ 触发事件 (Event) ↓ 触发新的反应 (触发器 / 反应) ↓ 返回第一步

听起来很简单？实际上，我遇到了三个陷阱——每一个都让系统“看起来在运行，但实际上原地打转”。

[

![Image](https://pbs.twimg.com/media/HAgr06LXcAANBuA?format=jpg&name=medium)



](https://x.com/Voxyz_ai/article/2019914775061270747/media/2019912620845789184)

我的 VPS 上有 OpenClaw 工作器在认领并执行任务。与此同时，Vercel 有一个心跳 cron 任务在运行 mission-worker，也试图认领相同的任务。

双方查询同一个表，抢占同一个步骤，独立执行。没有协调，纯粹的竞态条件。偶尔某个步骤会被双方标记为冲突状态。

Fix: Cut one. VPS is the sole executor. Vercel only runs the lightweight control plane (evaluate triggers, process reaction queue, clean up stuck tasks). 

改动很小——从心跳路由中移除 runMissionWorker 调用：

// 心跳现在只做4件事 常量 触发结果 = 等待 评估触发器(sb, 4\_000); const 反应结果 = await 处理反应队列(sb, 3\_000); const 学习结果 = await 提升洞察(sb); const 过期结果 = await 恢复过期步骤(sb);

额外收获：节省了 Vercel Pro 的费用。Heartbeat 不再需要 Vercel 的 cron 了——只需在 VPS 上使用一行 crontab 即可完成任务。

\*/5 \* \* \* \* curl -s -H "授权: Bearer $KEY"

[

![Image](https://pbs.twimg.com/media/HAgsp9-WYAAMenS?format=jpg&name=medium)



](https://x.com/Voxyz_ai/article/2019914775061270747/media/2019913532398002176)

我编写了4个触发器：当推文病毒式传播时自动分析，当任务失败时自动诊断，当内容发布时自动审核，当洞察成熟时自动推广。

在测试过程中我注意到：触发器正确检测到条件并创建了一个提案。但该提案一直停留在待处理状态——从未成为任务，也从未生成可执行步骤。

The reason: triggers were directly inserting into the ops\_mission\_proposals table, but the normal approval flow is: insert proposal → evaluate auto-approve → if approved, create mission + steps. Triggers skipped the last two steps. 

Fix: Extract a shared function createProposalAndMaybeAutoApprove. Every path that creates a proposal — API, triggers, reactions — must call this one function. 

// proposal-service.ts — 所有提案创建的单一入口点 导出 async function createProposalAndMaybeAutoApprove( sb: SupabaseClient, ProposalServiceInput, // 包含来源：'api' | 'trigger' | 'reaction' ): Promise<提案服务结果> { // 1. 检查每日限额 // 2. 检查 Cap Gates（下文解释） // 3. 插入提案 // 4. 触发事件 // 5. 评估自动审批 // 6. 如果已批准 → 创建任务 + 步骤 // 7. 返回结果 }

// 触发器-评估器.ts if (结果.已触发 && 结果.提案) { await createProposalAndMaybeAutoApprove(sb, { 结果.提案, 触发器 }); }

一个功能统管一切。任何未来的检查逻辑（速率限制、阻止列表、新限制）—— 只需修改一个文件。

[

![Image](https://pbs.twimg.com/media/HAgsGLDXUAAhPDB?format=jpg&name=medium)



](https://x.com/Voxyz_ai/article/2019914775061270747/media/2019912917433405440)

最隐蔽的漏洞——表面上一切看起来都正常，日志中没有错误，但数据库中的待处理步骤却越来越多，堆积起来。

原因：推文配额已满，但提案仍在被审批，生成任务、生成排队步骤。VPS 工作节点发现配额已满，直接跳过——未认领、未标记为失败。第二天，又一批任务到达。

Fix: Cap Gates — reject at the proposal entry point. Don't let it generate queued steps in the first place. 

// proposal-service.ts 中的门系统 常量 步骤类型门: Record<字符串, 步骤类型门> = { write\_content: checkWriteContentGate, // 检查每日内容上限 post\_tweet: checkPostTweetGate, // 检查推文配额 部署: checkDeployGate, // 检查部署策略 };

Each step kind has its own gate. Tweet quota full? Proposal gets rejected immediately, reason clearly stated, warning event emitted. No queued step = no buildup. 

异步函数 checkPostTweetGate(sb: SupabaseClient) { const autopost = await getOpsPolicyJson(sb, 'x\_autopost', {}); if (autopost.enabled === false) return { ok: false, reason: 'x\_autopost 已禁用' }; const 配额 = await 获取运维策略 JSON(sb, 'x\_daily\_quota', {}); const limit = Number(quota.limit ?? 10); const { count } = await sb .from('ops\_tweet\_drafts') .select('id', { count: 'exact', head: true }) .eq('状态', '已发布') .gte('posted\_at', 今天开始的 UTC ISO 时间()); if ((count ?? 0) >= limit) return { ok: false, reason: \`每日推文配额已用尽 (${count}/${limit})\` }; 返回 { ok: true }; }

Key principle: Reject at the gate, don't pile up in the queue. Rejected proposals get recorded (for auditing), not silently dropped. 

[

![Image](https://pbs.twimg.com/media/HAgr_tsXUAAUEqO?format=jpg&name=medium)



](https://x.com/Voxyz_ai/article/2019914775061270747/media/2019912806473093120)

在修复了三个陷阱之后，循环正常工作。但是这个系统只是一个“无错误的流水线”，而不是一个“反应迅速的团队”。

4个内置规则——每个检测到一个条件并返回一个提案模板：

推文互动率 > 5%：Growth 分析其走红原因（2 小时） 任务失败：Sage 诊断根本原因（1 小时） 新内容发布：Observer 审核质量（2 小时） Insight 获得多个点赞：自动推广至永久存储（4 小时）

Triggers only detect — they don't touch the database directly, they hand proposal templates to the proposal service. All cap gates and auto-approve logic apply automatically. 

冷却时间很重要。没有它的话，一条病毒式推文每心跳周期（每5分钟）就会触发一次分析。

{ "模式": \[ { "source": "推特替代版", "tags": \["推文","已发布"\], "target": "增长", {"类型": "分析", "概率": 0.3, "冷却时间": 120}, {"source": "\*", "tags": \["mission:failed"\], "target": "大脑",} {"类型": "诊断", "概率": 1.0, "冷却时间": 60} \] }

Xalt 发布一条推文 → 30%的概率 Growth 将分析其表现。任何任务失败 → 100%的概率 Sage 将进行诊断。

概率不是缺陷，而是特性。100% 确定性 = 机器人。添加随机性 = 感觉更像一个真实的团队，其中“有时候有人回应，有时候没人回应”。

虚拟专用服务器重启、网络小故障、API 超时——步骤陷入运行状态，而实际上没有人处理它们。

// 30 分钟无进展 → 标记为失败 → 检查是否应完成任务 const 过期阈值\_毫秒 = 30 \* 60 \* 1000; const { data: stale } = await sb .from('ops\_mission\_steps') .select('id, mission\_id') .eq('status', 'running') .lt('reserved\_at', staleThreshold); for (const 步骤 of stale) { await sb.从('ops\_mission\_steps').更新({ 状态: '失败', last\_error: 'Stale: 30 分钟内无进展' }).eq('id', ); await 可能完成任务如果已完成(sb, 步骤.任务 ID); }

maybeFinalizeMissionIfDone checks all steps in the mission — any failed means the whole mission fails, all completed means success. No more "one step succeeded so the whole mission gets marked as success." 

-   OpenClaw (VPS): Think + Execute (brain + hands) 
    
-   Vercel: Approve + Monitor (control plane) 
    
-   Supabase: All state (shared cortex) 
    

[

![Image](https://pbs.twimg.com/media/HAgrUcPWMAA4VL2?format=jpg&name=medium)



](https://x.com/Voxyz_ai/article/2019914775061270747/media/2019912063053606912)

如果你使用 OpenClaw + Vercel + Supabase，以下是一个最小可行闭环清单：

任务提案：存储提案（待处理/已接受/已拒绝） 任务：存储任务（已批准/运行中/已成功/已失败） 任务步骤：存储执行步骤（已入队/运行中/已成功/已失败） 代理事件：存储事件流（所有代理操作） 策略：存储策略（auto\_approve、x\_daily\_quota 等，以 JSON 格式） 触发规则：存储触发规则 代理反应：存储反应队列 操作运行：存储执行日志

Put proposal creation + cap gates + auto-approve + mission creation in one function. All sources (API, triggers, reactions) call it. This is the hub of the entire loop. 

不要硬编码限制。每个行为开关都存在于 ops\_policy 表中：

// auto\_approve: 哪些步骤类型允许自动通过 { "enabled": "已启用", "allowed\_step\_kinds": \["草稿推文","爬取","分析","撰写内容"\] } // x\_daily\_quota: 每日推文上限 { "限制": 8 } // worker\_policy: Vercel 是否执行步骤（设置为 false = 仅 VPS） { "启用": false }

4\. 心跳（一个 API 路由 + 一行 Crontab）

Vercel 上的 /api/ops/heartbeat 路由。VPS 上的一个 cron 任务，每 5 分钟调用一次该路由。该 cron 任务执行以下操作：触发评估、反应队列处理、洞察推广、过期任务清理。

Each step kind maps to a worker. After completing a step, the worker calls maybeFinalizeMissionIfDone to check whether the entire mission should be finalized. Never mark a mission as succeeded just because one step finished. 

阶段 时间 完成内容 基础设施 前期准备 OpenClaw VPS + Vercel + Supabase（已设置） 提案 + 审批 3 天 提案 API + 自动审批 + 策略表 执行引擎 2 天 mission-worker + 8 个步骤执行器 触发器 + 反应 2 天 4 种触发器类型 + 反应矩阵 循环统一 1 天 提案服务 + 上限门 + 修复三个问题 影响系统 + 可视化 2 天 Affect 重写 + 空闲行为 + 像素办公集成 种子 + 上线 半天 迁移 + 种子策略 + 定时任务

Excluding pre-existing infrastructure, the core closed loop (propose → execute → feedback → re-trigger) takes about one week to wire up. 

这 6 个代理现在可以自主运行

每天。我仍在每天优化系统——调整策略、扩展触发规则、改进代理间的协作方式。

它远非完美——代理间协作仍然很基础，而“自由意志”主要是通过基于概率的非确定性来模拟的。但这个系统确实能正常运行，真正不需要有人盯着它。

下一篇文章，我将介绍智能体如何相互“争论”和“说服”——圆桌投票和 Sage 的记忆整合如何将 6 个独立的 Claude 实例转变为某种类似团队认知的存在。

如果你正在使用 OpenClaw 构建智能体系统，我很乐意交流心得。当你作为一名独立开发者在做这件事时，每一次交流都能帮你避免另一个陷阱。

[

![Image](https://pbs.twimg.com/media/HAgsRA7XgAE_oLo?format=jpg&name=medium)



](https://x.com/Voxyz_ai/article/2019914775061270747/media/2019913103694069761)