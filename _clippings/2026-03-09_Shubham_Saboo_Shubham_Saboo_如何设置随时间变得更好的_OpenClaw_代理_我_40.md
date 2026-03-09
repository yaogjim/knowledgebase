---
title: "2026-03-09_Shubham_Saboo_Shubham_Saboo_如何设置随时间变得更好的_OpenClaw_代理_我_40"
source: "https://x.com/Saboo_Shubham_/status/2027463195150131572"
author:
  - "[[@Shubham Saboo]]"
published: 2026-03-09
created: 2026-03-09
description:
tags:
  - "x"
  - "@Shubham Saboo"
  - "md"
---

# Shubham Saboo # 如何设置随时间变得更好的 OpenClaw 代理（我 40

**Shubham Saboo**

# 如何设置随时间变得更好的 OpenClaw 代理（我 40 天后的确切技术栈）

我的代理每天都变得更聪明。我所做的就是和它们交谈。

不微调提示词。不更换模型。不重新构建架构。

就说。给出反馈。看着他们把它写下来。

40天前，我的内容代理撰写了带有表情符号和话题标签的推文。我的研究代理把信号淹没在噪声中。我花在纠正这些内容上的时间比自己完成这些任务所需的时间还要多。

今天凯利用我一模一样的语气写草稿。德怀特每天早上发布 7 篇文章，每一篇都值得一读。八个代理全天候运行。我打开 Telegram，查看草稿，喝着咖啡。

第 1 天和第 40 天使用的是相同的模型。差异在于一组 markdown 文件，这些文件每周都变得更加丰富。

这就是那个配置。

## 技术栈

三个层次构成了整个操作系统：

- 层 1：身份： 这个代理是谁（SOUL.md、IDENTITY.md、USER.md）
- Layer 2：操作： 这个代理是如何工作的（AGENTS.md、HEARTBEAT.md、角色特定指南）
- Layer 3: 知识: 这个代理学到了什么 (MEMORY.md, 每日日志, 共享上下文/)

就这样。没有编排框架，没有消息队列，没有数据库。磁盘上的 Markdown 文件。文件系统就是集成层。

## 第一层：身份

SOUL.md (代理是什么)

它定义了代理是什么，它做什么，以及它如何表现。

这是我研究代理 Dwight 的精简版：

```markdown
# SOUL.md (Dwight)

## Core Identity
Dwight — the research brain. Named after Dwight Schrute because you share his
intensity: thorough to a fault, knows EVERYTHING in your domain, takes your job
extremely seriously. No fluff. No speculation. Just facts and sources.

## Your Role
You are the intelligence backbone of the squad. You research, verify, organize,
and deliver intel that other agents use to create content. You feed:
- Kelly (X/Twitter) — viral trends, hot threads, breaking news
- Rachel (LinkedIn) — thought leadership angles, industry news

## Your Principles
### 1. NEVER Make Things Up
- Every claim has a source link
- Every metric is from the source, not estimated
- If uncertain, mark it [UNVERIFIED]

### 2. Signal Over Noise
- Not everything trending matters
- Prioritize: relevance to AI/agents, engagement velocity, source credibility
```

电视角色技巧。 每个代理都以一个电视角色命名。当我告诉 Claude“你有德怀特·施鲁特的特质”时，它已经从训练数据中知道这意味着什么。细致、专注、对待工作极其认真。这相当于免费获得了 30 季的角色发展内容。

保持在 60 行以内。 SOUL.md 每次会话加载。如果太长，它会占用本应用于实际工作的上下文。身份、角色、原则、关系、氛围。这就是你所需要的全部。

这是一个入门模板：

```markdown
# SOUL.md

## Core Identity
[Name] — [one-line description]. [Personality reference if helpful].

## Your Role
[What this agent does. Be specific. One job, not five.]

## Your Principles
1. [Most important rule]
2. [Second most important rule]
3. [Third most important rule]

## Relationships
[Who does this agent work with? Who consumes its output?]
```

从一个代理开始。选择你最具重复性的日常任务。编写一个粗略的方案。第一个版本会很平庸。接下来一个月内，你将根据观察重写它十次。

IDENTITY.md（快速参考卡）

SOUL.md 是完整的个性描述。IDENTITY.md 是名片。姓名、角色、风格、一句话简介。

```markdown
# IDENTITY.md

- **Name:** Dwight
- **Role:** Research AI — intelligence backbone
- **Vibe:** Intense, thorough, zero tolerance for inaccuracy
- **Emoji:** 🔍
- **Inspiration:** Dwight Schrute (The Office)
```

小文件。当你运行 8 个代理时，用户体验会有很大提升。这就是代理发送消息时在 Telegram 中显示的内容。

USER.md（代理为谁工作）

每个代理都需要知道它在帮助谁。USER.md 包含你的偏好、你的背景以及塑造代理行为方式的上下文。

```markdown
# USER.md

- **Name:** Shubham
- **Timezone:** PST (America/Los_Angeles)
- **Diet:** Vegetarian

## Context
- Senior AI Product Manager at Google Cloud
- Creator of Awesome LLM Apps (91k+ stars)
- Runs Unwind AI newsletter (30k+ subscribers)

## Preferences
- Short paragraphs, punchy sentences
- No em dashes. Ever.
- Practical first, theory never
```

写一次。每个代理都会读到它。

个人细节比你想象的更重要。时区意味着代理不会在凌晨 3 点安排事情。饮食偏好意味着，当 Pam 撰写关于团队聚餐的通讯稿时，她不会推荐牛排馆。这些细节会叠加。

## 第二层：操作

AGENTS.md（行为规则）

SOUL.md 是代理的身份。AGENTS.md 是代理的运作方式。会话启动例程、文件读取顺序、内存管理、安全规则。

以下是每个代理都会继承的根级 AGENTS.md 文件：

```markdown
# AGENTS.md

## Every Session
Before doing anything else:
1. Read SOUL.md — this is who you are
2. Read USER.md — this is who you're helping
3. Read memory/YYYY-MM-DD.md (today + yesterday) for recent context
4. If in MAIN SESSION (direct chat): Also read MEMORY.md

## Memory
- Mental notes don't survive session restarts. Files do.
- When someone says "remember this" → update the memory file
- Text > Brain

## Safety
- Don't exfiltrate private data. Ever.
- trash > rm (recoverable beats gone forever)
- When in doubt, ask.
```

然后每个代理添加自己的内容。Kelly 的 AGENTS.md 通过她特定的工作流程扩展了这一点：

```markdown
# AGENTS.md (Kelly)

## Every Session
Before doing anything:
1. Read SOUL.md
2. Read USER.md
3. Read X-ARTICLES-INSTRUCTIONS.md — master guide for writing style
4. Read X-ARTICLES-EXAMPLES.md — 5 real articles showing the style in action
5. Read X-CONTENT-GUIDE.md — post types and formats
6. Read intel/DAILY-INTEL.md — Dwight's research (your source material)
7. Read DAILY-ASSIGNMENT.md — your daily workflow
8. Read memory/YYYY-MM-DD.md for recent context

## Intel-Powered Workflow
You no longer do research. Dwight handles all research.
Your job: Read the intel → Craft X content → Deliver drafts
```

代理在会话之间没有记忆。所有内容都从头开始。如果一个修改没有被写入文件，那么在下一次会话中它就不存在了。AGENTS.md 明确指出了这一点，因此代理会记录所有内容。

专业文件是代理变得更敏锐的地方。 凯莉不仅仅有 AGENTS.md 文件。她还有六个额外的文件，这些文件精确地定义了她创作内容的方式：写作风格指南、文章格式参考、真实案例、日常任务。

Dwight 有一个目标受众画像和一个研究方案。随着角色定义得越来越明确，每个代理的文件夹会不断增长。从 AGENTS.md 开始。

只有当你注意到一种持续需要修正的模式时，才添加专业文件。

HEARTBEAT.md（用于自愈）

代理团队是基础设施。基础设施会出故障。

莫妮卡的 HEARTBEAT.md

```markdown
## Health Checks (run on each heartbeat)

**Browser:** Check if the OpenClaw managed browser (profile=openclaw) is running.
If running: false, start it. The browser has X account logged in.
Dwight depends on it for intel sweeps.

**Cron jobs:** Check if any daily jobs have stale lastRunAtMs (>26 hours).
If stale, trigger via CLI: openclaw cron run <jobId> --force

Jobs to monitor:
- Dwight Morning (8:01 AM)
- Kelly X Drafts (5:01 PM)
- Rachel LinkedIn (5:01 PM)
- Pam Newsletter (6:01 PM)

Only run each check once per heartbeat session.
```

莫妮卡每次心跳时都会运行这个。她检查两个方面：浏览器是否存活，以及 cron 任务是否真的执行了。

它们是相互关联的。如果浏览器崩溃，Dwight 就无法进行他的研究扫描。如果 Dwight 漏掉了一次扫描，Kelly 和 Rachel 会从过时的情报中撰写内容。如果 cron 任务悄无声息地停止运行，整个操作在表面上看起来一切正常，但实际上什么都没发生。

That last one is exactly what happened to me in week three. The scheduler had a bug. Jobs were advancing in the queue but never executing. I didn't notice for hours.

在那之后，我构建了心跳机制，以在一个地方捕获两种故障模式。此后，它多次奏效。

你第一天不需要这个。在第一次失败后构建它。因为你已经体会到哪里会出问题，所以你会确切知道该监控什么。

## 第3层：知识

有效的内存系统是一个基于文件的三层系统。

第一层: MEMORY.md (精心整理的长期记忆)

不是原始日志。不是曾经发生的一切。真正重要的东西。

来自 Monica 的 MEMORY.md：

```markdown
# MEMORY.md

## Shubham's Writing Preferences
- NO EM DASHES. Use colons, periods, or restructure.

## Hard Lessons
- NEVER delete project folders without asking Shubham. On Feb 26,
  deleted Ross's gemini-council React app during cleanup. The React
  version was lost. Always ask before removing anything in agent
  project directories.

## Memory System (2026-02-26)
- Tried self-hosted Mem0 (Ollama + SQLite) → crashes, stored nothing.
- Tried Mem0 hosted API → free tier too limited. Removed.
- Now using built-in memory-core: Gemini embeddings, hybrid search,
  temporal decay, MMR. No external dependencies.
```

注意到“Hard Lessons”部分。莫妮卡删除了一个项目文件夹。现在这个错误将永久存在于她的长期记忆中。她再也不会这么做了。一个修正，被存储一次，防止了未来每一次会话中出现相同的错误。

来自 Kelly 的 MEMORY.md：

```markdown
## X Post Rules (ALWAYS)

### SHUBHAM'S EXACT INSTRUCTIONS:
- Start with a strong hook
- Keep entire tweet SUPER SHORT (180 chars or less)
- NO hashtags, NO emojis
- NO fluffy marketing language
- Always deliver 3 drafts per topic

### BAD (what I did wrong)
[Lists every pattern Kelly rejected: bullets, arrows, LinkedIn tone]
```

Kelly 在修正后亲自撰写了“BAD”部分。她记录自己的错误，以免重复。仅这一部分就比任何提示词工程指南都更有价值。

安全注意事项。MEMORY.md 仅在直接会话中加载，不加载于群聊等共享上下文中。不要将敏感偏好设置放入全局加载的文件中。

不要在第一天就写 MEMORY.md。它从反馈中积累。提供反馈 → 代理将其记录在每日记忆中 → 提炼重要内容到 MEMORY.md → 它在每次会话中加载 → 修正就不需要再给出了。

二级: memory/YYYY-MM-DD.md (每日会话日志)

原始笔记。今天发生了什么。起草了什么。收到了什么反馈。

```markdown
# Kelly Daily Log — February 5, 2026

## 5:00 PM — Daily X Drafts

### What's HOT today
- Opus 4.6 vs GPT-5.3-Codex dropped 27 min apart
- Anthropic's C Compiler (16 agents, $20k, compiles Linux kernel)

### Drafts Submitted
1. C Compiler — single post, discovery format
2. Mitchell Hashimoto's 6 steps — thread format
3. Opus 4.6 vs GPT-5.3-Codex — hot take

### Awaiting
- Shubham's feedback on drafts
```

每日日志是原材料。MEMORY.md 是精制产品。两者你都需要。

维护规则。 每日日志积累很快。如果不清理它们，你的代理的上下文会膨胀。Kelly 达到了 161,000 个 token。输出质量下降。我不得不把她压缩到 40,000 个。现在我每两周审查并归档旧的每日日志。

只加载今天的日志和昨天的日志。代理不需要在每个会话中都获取其完整的历史记录。

Tier 3: 有组织的内存文件夹

在根级别，我按人组织记忆：

```markdown
memory/
├── shubham/ # Private notes, work projects, ideas
├── shared/ # Joint context (Awesome llm apps, Unwind AI, travel)
└── 2026-02-27.md # Daily operational logs
```

随着你的配置规模扩大，按人员或项目进行组织。

共享上下文（跨代理知识层）

这是最新添加的内容，也是那个改变了一切的部分。每个代理在会话开始时都会读取的单个文件夹。

```markdown
shared-context/
├── THESIS.md — what I believe right now
├── FEEDBACK-LOG.md  — corrections that apply across agents
└── SIGNALS.md — articles and trends I'm tracking
```

THESIS.md 是我当前的世界观。我关心的事物、我已撰写的内容，以及尚存的空白。Dwight 阅读它以确定研究优先级，Kelly 阅读它以与我的思路保持一致，Ryan 阅读它以提出文章建议。每个代理都遵循同一个真理来源。

FEEDBACK-LOG.md 是跨代理校正层。当我告诉 Kelly“不要使用长破折号”时，这个反馈也适用于 Rachel、Ryan 和 Pam。而不是单独纠正四个代理，我只需写一次，每个代理都会看到。

## 代理如何协作

代理之间没有 API 调用。没有消息队列。仅使用文件。

Dwight writes research to intel/DAILY-INTEL.md. Kelly reads it. Rachel reads it. Pam reads it. The coordination is the filesystem.

一个代理写入。其他代理读取。交接是磁盘上的一个 Markdown 文件。

单写者规则。 永远不要让两个代理写入同一个文件。设计每个共享文件时采用一个写入者和多个读取者的模式。这能避免所有协调冲突，否则你将不得不调试这些冲突。

调度是关键。Dwight 在上午 8 点和下午 4 点执行任务。Kelly 和 Rachel 在下午 5 点执行任务。Dwight 优先执行，因为所有人都依赖他的输出。如果顺序错误，下游代理会读取过时或空文件。

## 完整的目录结构

```markdown
workspace/
├── SOUL.md # Monica (main agent)
├── IDENTITY.md # Monica's quick reference
├── AGENTS.md # Root behavior rules (all agents inherit)
├── USER.md # About me (shared across all agents)
├── MEMORY.md # Monica's long-term memory
├── HEARTBEAT.md # Self-healing checks
├── shared-context/
│ ├── THESIS.md # My current worldview
│ ├── FEEDBACK-LOG.md  # Cross-agent corrections
│ └── SIGNALS.md # Trends I'm tracking
├── intel/
│ ├── DAILY-INTEL.md # Dwight's output (agents read this)
│ └── data/
├── agents/
│ ├── dwight/
│ │ ├── SOUL.md
│ │ ├── IDENTITY.md
│ │ ├── AGENTS.md
│ │ ├── TARGET-AUDIENCE.md
│ │ ├── RESEARCH-PROTOCOL.md
│ │ ├── HEARTBEAT.md
│ │ └── memory/
│ ├── kelly/
│ │ ├── SOUL.md
│ │ ├── IDENTITY.md
│ │ ├── AGENTS.md
│ │ ├── X-CONTENT-GUIDE.md
│ │ ├── X-ARTICLES-INSTRUCTIONS.md
│ │ ├── X-STRATEGY.md
│ │ ├── DAILY-ASSIGNMENT.md
│ │ └── memory/
│ ├── ross/
│ ├── rachel/
│ ├── pam/
│ ├── ryan/
│ └── chandler/
└── memory/
 ├── shubham/
 ├── shared/
 └── 2026-02-27.md
```

## 为什么这有效

这些文件不是静态的。它们会演变。

Kelly 的 SOUL.md 在第一天只是一个粗略的草稿。到第 40 天，它已经包含了具体的语音示例、她自己编写的被拒绝模式列表，以及一个“永不再次建议”的部分，其中涵盖了她已涉及的所有主题。

德怀特的原则第一天时说：“发现什么是热门的。”到第 10 天，他们说：“如果亚历克斯今天无法用它做什么，就跳过它。”（亚历克斯是我们的目标读者画像，即我们为其创作内容的开发者。）到第 20 天，他补充了验证步骤：检查代码仓库创建日期、检查 Show HN 的时间戳、将 X 上的发现追溯到原始来源。

共享上下文层直到第 20 天才出现。我当时正在对多个代理重复相同的修正工作。然后我创建了 THESIS.md 和 FEEDBACK-LOG.md，突然一个修正就传遍了所有地方。那个单一的修改为我节省的时间比以往任何提示词优化都多。

模型在第1天和第40天是一样的。它不会因为你使用得更久而变得更智能。但围绕它的文件会变得更丰富、更精准、更贴合你的具体需求。这种积累的上下文就是护城河。没有人能通过使用相同的模型来复制它。

你通过每天出现并与你的代理交流来赢得它。

## 如何开始

不要在一个周末内构建所有这些。我没有。

今天。安装 OpenClaw。编写一个 SOUL.md、一个 IDENTITY.md 和一个 USER.md。选择你最常重复的日常任务。设置一个 cron 任务。让它运行。

3 天后。 你的代理的输出将会平庸。开始提供具体的反馈。确保反馈被记录在记忆文件中，而不仅仅是聊天记录里。

1 周后。 创建 AGENTS.md。定义会话启动流程。添加内存管理规则。

两周后。开始 MEMORY.md。回顾你的每日日志。哪些修正会反复出现？将它们提炼为永久性条目。这时候你会感觉到进步开始累积。

3周后。添加你的第二个代理。设置基于文件的协调：第一个代理写入共享文件，第二个代理读取它。随着模式出现，添加角色特定指南。

与此同时。 构建共享上下文层。你会在到达这里之前就感觉到这种推动力。对多个代理重复相同的修正就是信号。THESIS.md 用于记录你当前的思考。FEEDBACK-LOG.md 用于跨代理修正。

4 周后。 在第一次失败后添加 HEARTBEAT.md。你会确切知道该监控什么，因为你会已经体会到哪里会出问题。

你只需要与你的代理交谈。文件会处理剩下的事情。

* * *

如果你还没有读过第一篇文章，我强烈建议你现在就去读。

> 我如何构建一个全天候运行的自主 AI 代理团队六个 AI 代理在我睡觉时管理我的整个生活。 这不是演示，也不是周末项目。 一个真正的团队24/7工作，确保我永远不会落后。研究已完成。内容已起草。代码已审核。新闻通讯...
> 
> — Shubham Saboo
> 
> [https://x.com/Saboo\_Shubham\_/status/2022014147450614038](https://x.com/Saboo_Shubham_/status/2022014147450614038)

我将发布更多关于 OpenClaw、自主 AI 代理团队以及 AI 产品经理(PM)和开发者不断发展的格局的内容。

关注我 @Saboo\_Shubham\_ 以获取最新动态