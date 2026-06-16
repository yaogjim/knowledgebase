---
title: "2026-06-16_github_com_marciopuga_cog_Cognitive_architecture_for_Claude_C"
source: "https://github.com/marciopuga/cog"
author:
  - "[[@anthropic]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "github"
  - "@anthropic"
  - "claude"
  - "https"
---

# marciopuga/cog: Cognitive architecture for Claude Code — persistent memory, self-reflection, and foresight

[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/) [Open in codespace](/codespaces/new/marciopuga/cog?resume=1)

| Name | Name | 
Last commit message

 | 

Last commit date

 |
| --- | --- | --- | --- |
| 

and

[docs: clarify that the architecture evolves, not the model](/marciopuga/cog/commit/65e5043c6fcc58924648960d0e54240380acbbd4)

[65e5043](/marciopuga/cog/commit/65e5043c6fcc58924648960d0e54240380acbbd4) ·

[8 Commits](/marciopuga/cog/commits/main/)

 |
| 

[.claude](/marciopuga/cog/tree/main/.claude ".claude")

 | 

[.claude](/marciopuga/cog/tree/main/.claude ".claude")

 | 

[feat(pipeline): add Unix toolbox orientation to pipeline skills](/marciopuga/cog/commit/d5e9e4333d917713283d528c698b89d8d798729b "feat(pipeline): add Unix toolbox orientation to pipeline skills
- Add Orientation sections to housekeeping, reflect, evolve with shell
commands (find -mtime, grep -c, git diff, wc -c) for efficient scoping
- Update CLAUDE.md memory retrieval to use domain-scoped L0 grep
Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>")

 |  |
| 

[memory](/marciopuga/cog/tree/main/memory "memory")

 | 

[memory](/marciopuga/cog/tree/main/memory "memory")

 | 

[feat: scalable entities & patterns architecture](/marciopuga/cog/commit/d47510b0f66cef9ad8427ce13f535719adba9051 "feat: scalable entities & patterns architecture
- Entity format: 3-line compact registry (### Name / key facts / status+links)
Heavy entries promoted to thread files. Cross-domain pointers for shared entities.
- Pattern satellites: core patterns.md cap reduced from 110→70 lines (5.5KB).
Domain-specific patterns go in satellite files loaded only by owning skill.
- Reflect: pattern routing rules, entity format enforcement (step 3b)
- Housekeeping: entity registry enforcement (step 5b), glacier inactive entities
- Evolve: scorecard metrics for pattern distribution + entity compression ratio
- README: updated entity example to 3-line format
Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>")

 |  |
| 

[.gitignore](/marciopuga/cog/blob/main/.gitignore ".gitignore")

 | 

[.gitignore](/marciopuga/cog/blob/main/.gitignore ".gitignore")

 | 

[feat: initial cog release — cognitive architecture for Claude Code](/marciopuga/cog/commit/1dd881975b77419c68fbcb06039bca97a5b892b0 "feat: initial cog release — cognitive architecture for Claude Code
Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>")

 |  |
| 

[CLAUDE.md](/marciopuga/cog/blob/main/CLAUDE.md "CLAUDE.md")

 | 

[CLAUDE.md](/marciopuga/cog/blob/main/CLAUDE.md "CLAUDE.md")

 | 

[feat(pipeline): add Unix toolbox orientation to pipeline skills](/marciopuga/cog/commit/d5e9e4333d917713283d528c698b89d8d798729b "feat(pipeline): add Unix toolbox orientation to pipeline skills
- Add Orientation sections to housekeeping, reflect, evolve with shell
commands (find -mtime, grep -c, git diff, wc -c) for efficient scoping
- Update CLAUDE.md memory retrieval to use domain-scoped L0 grep
Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>")

 |  |
| 

[LICENSE](/marciopuga/cog/blob/main/LICENSE "LICENSE")

 | 

[LICENSE](/marciopuga/cog/blob/main/LICENSE "LICENSE")

 | 

[feat: initial cog release — cognitive architecture for Claude Code](/marciopuga/cog/commit/1dd881975b77419c68fbcb06039bca97a5b892b0 "feat: initial cog release — cognitive architecture for Claude Code
Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>")

 |  |
| 

[README.md](/marciopuga/cog/blob/main/README.md "README.md")

 | 

[README.md](/marciopuga/cog/blob/main/README.md "README.md")

 | 

[docs: clarify that the architecture evolves, not the model](/marciopuga/cog/commit/65e5043c6fcc58924648960d0e54240380acbbd4 "docs: clarify that the architecture evolves, not the model
Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>")

 |  |
|  |

## Cog

一个基于纯文本的 Claude Code 认知架构——设计简洁，因此模型可以使用其已熟悉的相同 Unix 工具（ `grep` 、 `find` 、 `git diff` ）对自身记忆进行推理。

**[文档](https://lab.puga.com.br/cog)** | **[为什么文本](https://lab.puga.com.br/cog/#/why-text)** | **[致谢与灵感](https://lab.puga.com.br/cog/#/credits)**

Cog 是一组约定——而非代码——这些约定教会 Claude Code 如何构建和维护自己的记忆。你以纯文本形式定义规则。Claude 搭建结构并遵循这些规则。文件系统是接口。

没有服务器，没有运行时，没有应用代码。 `CLAUDE.md` 包含了这些规范——如何分层管理内存、何时进行精简、如何路由查询、何时进行归档。技能文件 (`.claude/commands/*.md`) 向 Claude 传授了特定的工作流程：自我反思、预见、维护和自我进化。Claude 读取这些指令并遵循它们，以在跨会话中组织、维护和扩展一个持久化知识库。

一切都是刻意设计的纯文本 [by design](https://lab.puga.com.br/cog/#/why-text) 。并非妥协——因为正是纯文本使其能够正常工作。记忆文件只是 Markdown 格式，这意味着 Claude 可以使用 `grep` 查找模式、使用 `find` 找出变更内容、使用 `wc` 检查文件大小，以及使用 `git diff` 查看最后一次流水线运行触及的内容。正是这些让 Linux 强大的 Unix 工具，使得 Cog 的记忆系统具备可观察性和可维护性。

Cog 是一个学习工具——一个观察记忆架构在具备明确规范和自我观察能力时如何演变的实验。你设定规则，Claude 搭建结构，而流程技能会随着时间优化这些规范。模型本身不会演变——它遵循它找到的任何规则。变化的是规则本身。每个决策都可追踪。每个规则都可编辑。每次变更都记录在 git 日志中。

## Quick Start

Requires [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview).

```
git clone https://github.com/marciopuga/cog
cd cog
```

在 Claude Code 中打开项目，然后：

```
/setup
```

Cog 会询问你的生活和工作——公司、副业项目、你想要追踪的内容。基于这次对话，它会生成所有内容：领域清单、记忆目录、技能文件和路由表。

That's it. Start talking.

### Permissions

Cog 随附 `.claude/settings.json` 文件，该文件预先批准了它所需的工具——文件读取、写入、编辑、搜索以及 Git 操作。当你首次打开项目时，Claude Code 会要求你接受这些项目级别的权限。只需确认一次，之后就不会再被打断了。

如果您希望手动检查所有内容，请删除 `.claude/settings.json` ，Claude Code 将对每个操作单独进行提示。

`CLAUDE.md` 定义了以下约定。Claude 在每次会话开始时读取这些约定，并遵循它们来决定存储事实的位置、何时进行压缩、如何路由查询以及何时进行归档。 `memory/` 目录是随着时间遵循这些规则而形成的状态。

### Three-Tier Memory

```
memory/
├── hot-memory.md ← Always loaded. <50 lines. What matters right now.
├── personal/ ← Warm. Loaded when relevant.
│ ├── hot-memory.md
│ ├── observations.md ← Append-only event log
│ ├── action-items.md ← Tasks with due dates
│ ├── entities.md ← People, places, things
│ └── ...
├── work/acme/ ← Your work domain (created by /setup)
│ └── ...
└── glacier/ ← Cold. Archived, indexed, retrieved on demand.
 └── index.md
```

- **热门** ：每次对话都会加载。当前状态、优先事项。
- **热加载** : 当技能激活时加载的领域特定文件。
- **Glacier** ：YAML 前置元数据的归档文件。通过 `glacier/index.md` 搜索。

这是随着时间逐步积累的内容。这些内容都不是预先填充的——而是源于你的对话。

**`memory/hot-memory.md`** — 30,000 英尺视角:

```
# Hot Memory
<!-- L0: Current priorities, active situations, system notes -->

## Identity
- Software engineer at Acme Corp, 2 kids, based in Melbourne
- Side project: open-source CLI tools

## Watch
- Performance review cycle opens next week — prep doc started [[work/acme/action-items]]
- Kid's speech therapy showing progress — 3 new words this month [[personal/health]]

## System
- /reflect found 3 observation clusters ready to promote to patterns
```

**`memory/personal/observations.md`** — 原始事件，只追加：

**`memory/work/acme/entities.md`** — 简洁的 3 行注册表:

```
### Sarah Chen (Engineering Manager)
- Direct report to VP Eng | Joined Jan 2025 | Runs platform team | Prefers async over meetings
- status: active | last: 2026-03-10
```

重量级条目会被提升到线程文件中——实体 stub 仅链接到： `→ [[work/acme/sarah-chen]]`

### Progressive Condensation

Two processes:

**浓缩：** 观察 → 模式 → 热记忆。每一层都比下一层更小且更可操作。

**归档：** 旧观测 → 冰川。已索引，可检索，不常用。

没有东西被删除——它会移动到正确的位置。

当一个主题在观察中反复出现时，Cog 会将其转化为一个 **线程** ——一个优化了读取的综合文件，该文件将分散的片段整合成连贯的叙述。

每一条线程都有相同的脊柱：

- **当前状态** — 此刻真实的情况（可自由改写）
- **时间线** ——带日期的条目，仅追加，完整细节被保留
- **洞察** — 模式、经验、这次有何不同

当一个主题在 2 周以上的时间里出现在 3 次以上的观察中，或者当你说“raise X”或“thread X”时，会生成一个线程。线程会不断变长——这正是其意义所在。细节（纹理）就是价值。一个文件永久存在，从不被压缩。

片段（观察）永远不会移动。线程通过维基链接引用它们。

See the full [线程框架文档](https://lab.puga.com.br/cog/#/memory) for details.

每个记忆文件都有一个单行摘要： `<!-- L0: what's in this file -->` 。这是三级检索协议的第一层级：

- **L0** — 单行摘要。决定是否打开文件。
- **L1** — 节标题扫描。标识长文件中需要读取的部分。
- **L2** — 完整文件读取。当需要完整上下文时使用。

先扫描 L0s，确认相关性，长文件使用 L1，只读取必要内容。

每个事实都存在于一个规范文件中。 `entities.md` 存储人物信息， `action-items.md` 存储任务信息。 `hot-memory.md` 存储指针——而非任何事实的权威版本。其他文件通过 `[[wiki-links]]` 进行引用，而非复制内容。

### Wiki-Links

文件通过 `[[domain/filename]]` 链接相互引用。链接索引由 `/housekeeping` 自动生成，以便你能够发现哪些内容相互关联。

### Domain Registry

领域是你生活中的区域——个人、工作、副业项目。每个领域都有自己的记忆目录和斜杠命令。

```
/setup → conversational → domains.yml → directories + skills + routing
```

| Type | Purpose | Examples |
| --- | --- | --- |
| `personal` | Personal life | Always created |
| `work` | Day job | `/acme`, `/google` |
| `side-project` | Ventures, hobbies | `/myapp`, `/substack` |
| `system` | Cog internals | Auto-created (`cog-meta`) |

## Skills

Built-in skills in `.claude/commands/`:

| Skill | What it does |
| --- | --- |
| `/setup` | Conversational domain setup |
| `/personal` | 家庭、健康、日历、日常 |
| `/reflect` | 挖掘对话内容，提取模式，浓缩 |
| `/evolve` | 审计内存架构，提出规则变更 |
| `/foresight` | Cross-domain strategic nudge |
| `/scenario` | 带有时间线叠加层的决策模拟 |
| `/housekeeping` | 归档、修剪、链接审计、冰川索引 |
| `/history` | 深度搜索记忆文件 |
| `/explainer` | 写作与解释（Atkins + Montaigne 方法） |
| `/humanizer` | Remove AI patterns from text |

领域技能（ `/work` 、 `/sideproject` 等）由 `/setup` 自动生成。

## Pipeline

Cog 包含能够随时间维护内存健康的管道技能。手动运行它们：

```
/housekeeping # Archive stale data, prune hot-memory, rebuild indexes
/reflect # Mine recent work, condense patterns, detect threads
/evolve # Audit architecture, check rule effectiveness
/foresight # Cross-domain scan, surface one strategic nudge
```

Or automate with scheduling:

**Claude Code** 具备内置的任务调度功能 — 使用 `/loop` 或 cron 定期运行流水线技能：

```
# Example: nightly housekeeping + reflect via cron
0 23 * * * cd /path/to/cog && claude -p "$(cat .claude/commands/housekeeping.md)"
0 0  * * * cd /path/to/cog && claude -p "$(cat .claude/commands/reflect.md)"
```

**[Cowork](https://claude.com/product/cowork)** 会话也可以执行流水线技能。在 Cowork 中打开 Cog，要求它执行 `/housekeeping` 或 `/reflect` — 它拥有完全的文件访问权限，并且可以作为更长的自主会话的一部分维护记忆。

该管道是可选的。Cog 在没有它的情况下也能工作——但定期运行它可以保持内存清洁，并揭示你会错过的见解。

## Architecture

Cog 的架构完全存在于指令中—— `CLAUDE.md` 用于规范，`.claude/commands/*.md` 用于工作流。不存在应用代码。这些指令定义了内存的结构、查询的路由方式以及系统如何自我维护。Claude 读取这些文件并根据它们执行操作。 `memory/` 目录只是累积的状态。

这使得 Cog 与界面无关。它适用于：

- **[Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview)** (终端) — 原生。只需打开项目。
- **[协作](https://claude.com/product/cowork)** — Claude 桌面版的代理模式。指向 `memory/` 并继承所有内容。非常适合大量文档生成和长期自主工作流。
- **任何由 Claude 驱动的工具** 能够读取 `CLAUDE.md` 并且具有文件访问权限。

内存系统在任何地方都是相同的——带有约定的 Markdown 文件。界面只是决定了如何加载上下文。

## Connecting Tools

当通过 MCP（模型上下文协议）连接到外部工具时，Cog 会变得显著更强大。在 Claude Code 或 Cowork 中，您可以连接如下服务：

- **Google Calendar** — 日程意识、会议准备、时间块划分
- **Gmail** — 电子邮件撰写、收件箱分类处理、跟进追踪
- **Slack** — 团队上下文、消息撰写、频道监控
- **GitHub** — PR 评审, 问题跟踪, 代码库认知
- **Linear/Jira** — 项目跟踪，冲刺上下文
- **Notion/Obsidian** — 扩展知识库，笔记同步

当工具连接时，Cog 的技能可以自动使用它们。 `/foresight` 在显示提示之前会检查你的日历。 `/reflect` 可以引用 Slack 线程。 `/personal` 可以撰写电子邮件。记忆层为这些工具提供了它们单独拥有时所不具备的东西：持续存在且累积的上下文。

**在 Cowork 中连接工具** ，添加 MCP 服务器到您的 Cowork 设置中。每个工具以一组函数的形式呈现，Cog 可以在进行其记忆操作的同时调用这些函数——无需修改代码。

持久内存 + 连接工具的结合，让 Cog 从笔记系统转变为认知层。没有行动的记忆只是日记。有工具支持的记忆则是智能体。

## Credits

Cog 是来自研究、开源系统和知识管理传统的理念综合。

**研究** : [RLM](https://arxiv.org/abs/2512.24601) （递归内存层次结构）| [A-MEM](https://arxiv.org/abs/2502.12110) （双向反向链接）| [OpenViking](https://github.com/volcengine/OpenViking) （L0/L1/L2 分层上下文加载）

**系统** ： [Zep/Graphiti](https://github.com/getzep/graphiti) （时间有效性）| [Mem0](https://github.com/mem0ai/mem0) （矛盾检测）| [Claude Memory](https://docs.anthropic.com/en/docs/claude-code/memory) （基于文件的架构验证）

**传统** : [卡片盒笔记法](https://en.wikipedia.org/wiki/Zettelkasten) (主题框架) | [SSOT](https://en.wikipedia.org/wiki/Single_source_of_truth) (规范事实存储)

**平台** : [Claude 代码](https://docs.anthropic.com/en/docs/claude-code/overview) (Anthropic)

查看 [完整 credits 页面](https://lab.puga.com.br/cog/#/credits) ，了解每个想法如何塑造了 Cog 的设计。

## Citation

如果 Cog 影响了你的工作——无论你是分叉它、调整这些模式，还是参考其架构——提及它都大有裨益：

```
Cog: Cognitive Architecture for Claude Code
https://github.com/marciopuga/cog
Marcio Puga, 2026
```

BibTeX for academic use:

```
@software{puga2026cog,
  author = {Puga, Marcio},
  title = {Cog: Cognitive Architecture for Claude Code},
  year = {2026},
  url = {https://github.com/marciopuga/cog},
  note = {Persistent memory, self-reflection, and foresight for AI agents}
}
```

## License

MIT

## Releases

No releases published

## Packages

No packages published