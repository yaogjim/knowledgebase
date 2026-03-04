---
title: "2026-03-03_Shubham_Saboo_Shubham_Saboo_如何设置能够随着时间推移不断改进的_OpenClaw_代理"
source: "https://x.com/Saboo_Shubham_/status/2027463195150131572"
author:
  - "[[@Shubham Saboo]]"
published: 2026-03-03
created: 2026-03-03
description:
tags:
  - "x"
  - "@Shubham Saboo"
  - "md"
---

# Shubham Saboo # 如何设置能够随着时间推移不断改进的 OpenClaw 代理（

**Shubham Saboo**

# 如何设置能够随着时间推移不断改进的 OpenClaw 代理（40 天后我的配置）

我的经纪人每天都在进步，我做的就是和他们交流。

不调整提示音。不更换模型。不重建架构。

就跟他们聊聊，给他们反馈，然后看着他们写下来。

40天前，我的内容代理撰写的推文充斥着表情符号和话题标签。我的研究代理则把真正有价值的信息淹没在了无意义的信息中。我花在修改这些推文上的时间，比我自己完成这些任务所需的时间还要多。

今天，凯莉用我的声音写稿。德怀特每天早上交出 7 篇稿件，篇篇精彩。八位经纪人 24 小时不间断工作。我打开 Telegram，审阅稿件，喝着咖啡。

第 1 天和第 40 天的模型相同。区别在于，第 40 天会生成一堆 Markdown 文件，这些文件每周都会变得更加丰富。

这就是堆栈。

## 堆栈

整个操作系统由三层组成：

- 第一层：身份：这个代理是谁（SOUL.md、IDENTITY.md、USER.md）
- 第二层：操作： 这个代理是如何工作的（ 代理商.md， 心跳.md（角色特定指南）
- 第 3 层：知识： 该智能体学到了什么（ 内存.md（每日日志，共享上下文/）

就是这样。没有编排框架，没有消息队列，没有数据库，只有磁盘上的 Markdown 文件。文件系统就是集成层。

## 第一层：身份

灵魂.md（代理人是谁）

它定义了代理是谁、代理做什么以及代理如何行动。

以下是我的研究代理人德怀特的节选版本：

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

这是个电视角色梗。 每个特工的名字都取自一个电视角色。当我跟克劳德说“你浑身散发着德怀特·施鲁特的气息”时，它已经从训练数据中明白了这意味着什么：认真负责、专注投入、对工作极其认真。这相当于免费获得了 30 季电视剧的角色发展经验。

控制在 60 行以内。 灵魂.md 每次会话都会加载。如果加载时间过长，就会占用本应用于实际工作的上下文信息。身份、角色、原则、人际关系、氛围，这些就足够了。

以下是一个入门模板：

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

先从一位代理人开始。选择你每天最重复的任务。写个草图。初稿可能不太好。接下来的一个月里，你要根据实际情况修改十遍。

身份信息.md（快速参考卡）

灵魂.md 是完整的人格。 身份信息.md 这就是名片。姓名、职位、个人风格、一句简短介绍。

```markdown
# IDENTITY.md

- **Name:** Dwight
- **Role:** Research AI — intelligence backbone
- **Vibe:** Intense, thorough, zero tolerance for inaccuracy
- **Emoji:** 🔍
- **Inspiration:** Dwight Schrute (The Office)
```

文件虽小，但对于管理 8 位客服人员来说，却能显著提升工作效率。这是客服人员在 Telegram 上向您发送消息时显示的内容。

用户.md（该经纪人为谁工作）

每个经纪人都需要知道自己在帮助谁。 用户.md 包含您的偏好、背景以及影响代理行为方式的上下文。

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

只需写一遍，每个经纪人都会读。

个人细节比你想象的更重要。时区不同意味着经纪人不会在凌晨三点安排工作。饮食偏好不同意味着帕姆在撰写团队聚餐的简报时，不会建议去牛排馆。这些细节累积起来，影响最终结果。

## 第二层：操作

代理商.md（行为规则）

灵魂.md 就是代理人。 代理商.md 这就是它的运行方式。会话启动例程、文件读取顺序、内存管理、安全规则。

这是根级别代理商.md 每个代理人都会继承以下内容：

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

然后每个代理人都会添加自己的代理人。凯利的代理商.md 她将这一点与她的具体工作流程相结合：

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

代理程序在会话之间没有记忆。一切都从头开始。如果更正没有写入文件，那么在下一个会话中它将不存在。 代理商.md 这样就明确地让代理人把所有事情都写下来。

专业档案是特工们磨练技艺的地方。 凯利不仅拥有…… 代理商.md 她还有六个额外的文件，详细定义了她如何创作内容：写作风格指南、文章格式参考、真实案例、每日任务。

德怀特制定了目标受众画像和研究方案。随着角色定位的不断完善，每位代理人的档案也会随之增长。从……开始代理商.md。

只有当您发现某种模式需要反复纠正时，才需要添加专业文件。

心跳.md（用于自我疗愈）

代理团队是基础设施。基础设施会出故障。

莫妮卡的心跳.md：

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

莫妮卡会在每次心跳时运行这个程序。她会检查两件事：浏览器是否处于活动状态，以及定时任务是否实际运行。

它们之间是有关联的。如果浏览器崩溃，德怀特就无法进行调查。如果德怀特错过了一次调查，凯莉和瑞秋就只能根据过时的情报撰写内容。如果定时任务悄无声息地停止运行，表面上整个系统看起来一切正常，但实际上却什么都没发生。

最后那件事正是我在第三周遇到的情况。调度器出了 bug。任务在队列里不断前进，但却从未执行。我好几个小时都没注意到。

之后，我构建了心跳机制，以便在一个地方同时捕获这两种故障模式。此后，它已经多次成功捕获故障。

第一天不需要这个功能。等第一次失败后再构建它。你会确切地知道需要监控什么，因为你已经体会到哪些环节出了问题。

## 第三层：知识

有效的内存系统是基于文件的三层系统。

第一层级： 内存.md（精心设计的长期记忆）

不是原始日志，也不是所有发生过的事情，而是真正重要的东西。

来自莫妮卡的内存.md：

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

请注意“惨痛教训”部分。莫妮卡误删了一个项目文件夹。现在，这个错误永远铭刻在她的长期记忆中。她以后绝不会再犯同样的错误。一次纠正，一次存储，就能防止在以后的每次会话中再次发生同样的错误。

来自凯利内存.md：

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

凯莉在修改后亲自撰写了“错误”部分。她会记录自己的错误，以免重蹈覆辙。单单这一部分就比任何工程指南都更有价值。

安全提示。 内存.md 仅在直接会话中加载，不会在群聊等共享环境中加载。请勿将敏感偏好设置放在所有位置都会加载的文件中。

不要写内存.md 从第一天开始。 它根据反馈不断成长。提供反馈 → 代理将其记录在每日内存中 → 提炼重要信息内存.md→ 每次会话都会加载 → 无需再次进行更正。

第二层：memory/YYYY-MM-DD.md（每日会话日志）

原始笔记。今天发生了什么。草拟了什么。收到了哪些反馈。

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

每日日志是原始素材。 内存.md 是精制产品。两者都需要。

维护规则。 每日日志积累速度很快。如果不进行清理，代理的上下文信息就会膨胀。Kelly 的日志数量达到了 161,000 个标记。输出质量直线下降。我不得不将她的日志压缩到 40,000 个。现在我每两周审查并归档一次旧的每日日志。

只需加载今天的日志和昨天的日志。代理程序不需要每次会话都加载完整的历史记录。

第三层级：整理好的记忆文件夹

从根本上讲，我按人来组织记忆：

```markdown
memory/
├── shubham/ # Private notes, work projects, ideas
├── shared/ # Joint context (Awesome llm apps, Unwind AI, travel)
└── 2026-02-27.md # Daily operational logs
```

随着组织规模的扩大，可以按人员或项目进行整理。

共享上下文（跨智能体知识层）

这是最新添加的功能，也是改变一切的功能。这是一个所有代理在会话开始时都会读取的文件夹。

```markdown
shared-context/
├── THESIS.md — what I believe right now
├── FEEDBACK-LOG.md  — corrections that apply across agents
└── SIGNALS.md — articles and trends I'm tracking
```

论文.md 这就是我目前的世界观。它包含了我关心的事情、我已经写过的东西，以及仍然存在的空白。德怀特会阅读它来确定研究的优先顺序。凯莉会阅读它来了解我的想法。瑞恩会阅读它来提出文章选题。所有参与者都遵循同一个真理来源。

反馈日志.md 这是跨代理纠错层。当我告诉 Kelly “不要用破折号”时，这条反馈同样适用于 Rachel、Ryan 和 Pam。我不用分别纠正四个代理的错误，只需写一次，所有代理都会看到。

## 代理人如何协调

代理之间不进行 API 调用。没有消息队列。只有文件。

德怀特撰写研究报告，发布在 intel/DAILY-INTEL.md 网站上。凯莉会阅读。瑞秋会阅读。帕姆也会阅读。协调工作就通过文件系统完成。

一个代理写入数据，其他代理读取数据。交接的文件是磁盘上的 Markdown 文件。

单写规则。 永远不要让两个代理同时写入同一个文件。每个共享文件都应该设计成一个写入器和多个读取器。这样可以避免所有协调冲突，否则你就得费力调试了。

调度机制确保了这一点。 德怀特在早上 8 点和下午 4 点运行。凯莉和瑞秋在下午 5 点运行。德怀特先运行，因为所有人都依赖他的输出。如果顺序错误，下游代理就会读取过期或空的文件。

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

## 为什么这种方法有效

文件并非一成不变，它们会不断演变。

凯利灵魂.md 第一天只是个粗略的草稿。到了第 40 天，草稿里已经有了具体的语音示例、她自己编写的被否决的模式列表，以及一个列出所有她已经讲过的主题的“永不再提”部分。

德怀特第一天的原则是“找到热门话题”。到了第十天，原则变成了“如果亚历克斯今天不能用它做点什么，那就跳过它”。（亚历克斯是我们的目标读者，也就是我们为其创作内容的开发者。）到了第二十天，他又增加了验证步骤：检查仓库创建日期、检查 Show HN 时间戳、追溯 X 个发现的原始出处。

共享上下文层直到第 20 天才出现。我当时对多个代理重复进行相同的修正。然后我构建了论文.md 和反馈日志.md 突然间，一个修正就生效了。这一个改动比任何即时优化都节省了我更多的时间。

模型在第一天和第四十天都是一样的。它不会因为你使用时间更长而变得更智能。但它周围的文件会变得更丰富、更精准，更符合你的具体需求。这种积累的上下文信息就是护城河。没有人能用同样的模型复制它。

你每天到岗并与经纪人交谈才能赢得这份工作。

## 如何开始

不要在一个周末内完成所有这些工作。我就是这么做的。

今天。 安装 OpenClaw。编写一个灵魂.md， 一身份信息.md， 一用户.md 选择你每天重复性最高的任务。设置一个定时任务。让它运行。

三天后， 你的客服人员的工作表现会比较平庸。这时你需要开始提供具体的反馈。确保反馈内容被记录下来，而不仅仅是聊天记录。

一周后创建代理商.md 定义会话启动例程。添加内存管理规则。

两周后开始内存.md 回顾你的每日记录。哪些需要反复纠正的地方？把它们整理成永久记录。这时你就会感受到复利效应的开始。

三周后， 添加第二个代理。设置基于文件的协调机制：第一个代理写入共享文件，第二个代理读取该文件。随着模式的出现，添加特定角色的指导规则。

差不多在同一时间， 构建共享上下文层。在你到达这里之前，你就会感受到这种拉力。对多个代理重复相同的修正就是信号。 论文.md 符合你目前的想法。 反馈日志.md 用于跨代理纠正。

4 周后。 添加心跳.md 第一次失败之后，你就会确切地知道该监控哪些方面，因为你已经体会到哪里出了问题。

你只需要和你的代理人沟通，剩下的事情就交给文件来处理。

* * *

如果你还没读过第一篇文章，我强烈建议你现在就去读一下。

> 我是如何构建一个全天候运行的自主人工智能代理团队的六个人工智能代理在我睡觉时操控着我的生活。 这不是演示，也不是周末项目。 一个真正的团队全天候工作，确保我永远不会落后。研究完成。内容撰写完成。代码审查完成。新闻稿……
> 
> — Shubham Saboo
> 
> [https://x.com/Saboo\_Shubham\_/status/2022014147450614038](https://x.com/Saboo_Shubham_/status/2022014147450614038)

我将发布更多关于 OpenClaw、自主 AI 代理团队以及 AI 项目经理和开发人员不断变化的环境的文章。

跟我来 @Saboo\_Shubham\_ 敬请期待。