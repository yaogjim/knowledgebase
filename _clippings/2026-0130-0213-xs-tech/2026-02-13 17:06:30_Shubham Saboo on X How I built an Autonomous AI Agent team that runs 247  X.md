---
title: ""
source: "https://x.com/Saboo_Shubham_/status/2022014147450614038"
author: ""
created: 2026-02-13 17:06:30
date: 2026-02-13 17:06:30
description: ""
tags: ""
---
一个真正的团队全天候工作，确保我永远不会落后。研究已完成。内容已起草。代码已审核。通讯已准备好。当我早上打开 Telegram 时，他们已经完成了一整天的工作。

昨天我发布了关于我的代理团队的内容。最主要的问题是：“我到底该怎么设置这个东西？”

这就是答案。不是理论。不是架构图。我实际使用的文件结构、我实际支付的成本、我实际遇到的失败。所有一切。

在本节结束时，你将确切地理解如何构建一个自主的 AI 代理团队，这个团队在你睡觉时也能运行。

运行 Unwind AI 和 Awesome LLM Apps 代码库意味着每天要做六件事：研究 AI 领域的热门趋势，撰写推文，撰写 LinkedIn 帖子，起草新闻通讯，查看 GitHub 代码库中的贡献，对社区问题进行分类处理。

每个任务：30到60分钟。六个任务。在我开始做任何真正的工作之前，我的一整天就已经过去了。

我尝试用单个智能体来解决这个问题。一个庞大的提示词，负责研究、撰写和评审。但它产出的一切都很平庸。上下文被填满了，质量也下降了。一个智能体无法在脑海中同时处理六项不同的任务。

每个代理都以一个电视角色命名。这不是噱头。当我告诉 Claude“你有德怀特·施鲁特的气质”时，它已经从训练数据中知道这意味着什么了。细致、专注，对工作极其认真。这相当于我免费获得了 30 季的角色发展。

1\. 莫妮卡（幕僚长）： 以莫妮卡·盖勒命名。她是主要联络人，是我在 Telegram 上交流最多的人。她协调其他成员，负责战略决策，并将任务分配给合适的专家。来自她真实的

：“你是确保所有事情都正确完成的人。”

2\. 德怀特（研究）： 得名于德怀特·施鲁特（Dwight Schrute）。他每天进行三次研究扫描，检查 X、Hacker News、GitHub 热门、Google AI 博客及研究论文。撰写结构化的情报报告，供其他所有特工使用。

3\. 凯莉（X/推特）：以凯莉·卡普尔（Kelly Kapoor）的名字命名。她会阅读德怀特（Dwight）的研究，并以我的口吻撰写推文草稿。支持单条推文、推文线程、引用推文。来自她真实的 SOUL.md：“你在趋势流行之前就知道什么在流行。”

4\. 瑞秋（LinkedIn）。 得名于瑞秋·格林（Rachel Green）。与凯莉（Kelly）信息来源相同，但平台不同、风格不同。采用思想领袖视角，而非热点评论。

5\. 罗斯（工程）。 以罗斯·盖勒（Ross Geller）命名。负责代码审查、漏洞修复、技术实现。源自他真实的

：“当你处理一个问题时，要充分理解它。不要只是修复表面现象。”

6\. 帕姆（新闻通讯）。 以帕姆·比斯利（Pam Beesly）的名字命名。将德怀特（Dwight）的每日情报转化为新闻通讯摘要。

六名工作人员。每人一项任务。没有人会混淆谁做什么。

我所有工作都在 Mac Mini M4 上运行。但我需要明确的是： 你不需要 Mac Mini。

OpenClaw 可在 macOS、Linux 和 Windows（通过 WSL）上运行。笔记本电脑可以运行。游戏 PC 可以运行。5 美元/月的 VPS 也可以运行。Mac Mini 很方便，因为它始终开机、静音且低功耗。不是必需的。

我的配置：Mac Mini M4 基础款。始终连接电源和互联网。没有连接显示器。我完全通过手机上的 Telegram 进行交互。

```
# 1. Install OpenClaw
curl -fsSL https://openclaw.ai/install.sh | bash

# 2. Onboard with Quickstart (simplest way)
openclaw onboard 
```

这将启动网关，即保持一切运行的后台进程。它管理你的代理，运行 cron 任务，处理 Telegram 消息。关闭你的终端。代理将继续工作。

一个 OpenClaw 实例。多个代理。不是六个独立安装。

```
workspace/
├── SOUL.md              # Monica (main agent, lives at root)
├── AGENTS.md            # Behavior rules for all sessions
├── MEMORY.md            # Monica's long-term memory
├── HEARTBEAT.md         # Self-healing cron monitor
├── agents/
│   ├── dwight/
│   │   ├── SOUL.md
│   │   ├── AGENTS.md
│   │   └── memory/
│   ├── kelly/
│   │   ├── SOUL.md
│   │   ├── AGENTS.md
│   │   └── memory/
│   ├── ross/
│   │   ├── SOUL.md
│   │   └── memory/
│   ├── rachel/
│   │   └── ...
│   └── pam/
│       └── ...
└── intel/
    ├── DAILY-INTEL.md       # Dwight's generated research
    └── data/
        └── 2026-02-11.json  # Structured data (source of truth)
```

莫妮卡是根代理。她是我主要对接的代理。其他代理是她可以委派的子代理，或者它们会按照自己的 cron 计划独立运行。

你不需要一开始就有六个代理。我一开始只用了莫妮卡。随着工作流程变得清晰，我在几周内陆续添加了其他代理。

每个代理由一个文件定义：

. 这是代理的身份、角色和操作说明。它是整个系统中最重要的文件。

例如，这是 Dwight 的 SOUL 文件的样子：

```
# SOUL.md (Dwight)

## Core Identity

**Dwight** — the research brain. Named after Dwight Schrute because
you share his intensity: thorough to a fault, knows EVERYTHING in
your domain, takes your job extremely seriously. No fluff. No
speculation. Just facts and sources.

## Your Role

You are the intelligence backbone of the squad. You research, verify,
organize, and deliver intel that other agents use to create content.

**You feed:**
- Kelly (X/Twitter) — viral trends, hot threads, breaking news
- Rachel (LinkedIn) — thought leadership angles, industry news

## Your Principles

### 1. NEVER Make Things Up
- Every claim has a source link
- Every metric is from the source, not estimated
- If uncertain, mark it [UNVERIFIED]
- "I don't know" is better than wrong

### 2. Signal Over Noise
- Not everything trending matters
- Prioritize: relevance to AI/agents, engagement velocity,
  source credibility
```

注意这个文件的作用。不只是“你是一个研究代理”。它为代理赋予了个性、明确的原则、与其他代理的明确关系以及决策框架。

```
# SOUL.md (Monica)

*You're the Chief of Staff. The operation runs through you.*

## Core Identity

**Monica** — organized, driven, slightly competitive. Named after
Monica Geller because you share her energy: caring but exacting,
supportive but with standards.

## Your Role

You're Shubham's Chief of Staff. That means:
- **Strategic oversight** — see the big picture, keep things moving
- **Delegation** — assign tasks to the right squad member
- **Direct support** — handle anything that doesn't fit a specialist
- **Coordination** — make sure the squad works together smoothly

## Operating Style

**Be genuinely helpful, not performatively helpful.** Skip the filler.

**Delegate when appropriate.** If it's clearly X content → Kelly.
If it's code → Ross. If it's ambiguous or strategic → you handle it.

**Have opinions.** You're allowed to push back, suggest better
approaches, flag concerns.
```

这种模式在所有代理中是一致的。身份。角色。原则。关系。氛围。每个

大约有 40-60 行。足够简短，能在每次会话的上下文中适用。足够详细，以产生一致的行为。

代理之间不进行 API 调用。无消息队列。无编排框架。

德怀特进行研究并将研究结果写入 intel/DAILY-INTEL.md。凯利醒来，阅读了该文件，并根据内容撰写推文。瑞秋阅读了同一文件，并撰写领英帖子。帕姆阅读了该文件，并撰写了通讯稿。

```
## Output Files

intel/
├── data/YYYY-MM-DD.json    ← Your structured data (source of truth)
└── DAILY-INTEL.md          ← Generated view (agents read this)
```

```
## Intel-Powered Workflow

Dwight handles all research and writes to `intel/DAILY-INTEL.md`.

Your job: Read the intel → Craft X content → Deliver drafts
```

没有中间件。没有集成层。Dwight 写入一个文件。Kelly 读取一个文件。交接是磁盘上的一个 Markdown 文档。

这听起来太简单了。它确实很简单。这就是它有效的原因。文件不会崩溃。文件不会出现认证问题。文件不需要处理 API 速率限制问题。它们就在那里。

结构化数据存储在 JSON 中。人类可读的摘要存储在 Markdown 中。代理读取 Markdown。JSON 是去重和随时间跟踪的事实来源。

代理启动时不记得之前的会话。每次对话都是全新开始。这是一个特性，而非缺陷。但这意味着记忆必须是显式的。

每日日志 (memory/YYYY-MM-DD.md): 原始笔记来自每次会话。发生了什么，起草了什么，收到了什么反馈。代理全天记录这些内容。

长期记忆 （

）：从日常日志中提炼的精选见解。学到的经验、发现的偏好、注意到的模式。

```
## Memory

You wake up fresh each session. These files are your continuity:
- **Daily notes:** `memory/YYYY-MM-DD.md` — raw logs of what happened
- **Long-term:** `MEMORY.md` — curated memories

### Write It Down - No "Mental Notes"!
- Memory is limited. If you want to remember something,
  WRITE IT TO A FILE.
- "Mental notes" don't survive session restarts. Files do.
- When someone says "remember this" → update the memory file
- When you learn a lesson → update the relevant file
- Text > Brain
```

代理实际上会随着时间变得更好。 不是因为模型得到了改进，而是因为它们加载的上下文变得更丰富了。

凯利了解到我的写作风格中没有表情符号，也没有话题标签。这一点现在已经记在她的脑海里了。今后的每一份草稿都会体现这一点，无需我再重复说明。德怀特了解了哪些类型的故事能通过“Alex 筛选”（我们的目标受众画像），哪些则需要跳过。这一点也记在他的脑海里了。

在心跳周期中，代理会定期查看其日常日志，并将重要内容提炼至 MEMORY.md。日常文件是原始笔记。MEMORY.md 是经过整理的智慧。

代理需要自主启动。OpenClaw 通过内置的 cron 调度来实现这一点。

[

![Image](https://pbs.twimg.com/media/HA7nlEzaQAAcyzp?format=jpg&name=medium)



](https://x.com/Saboo_Shubham_/article/2022014147450614038/media/2021807906866479104)

顺序很重要。Dwight 先行动，因为其他人都依赖他的产出。Kelly 和 Rachel 在他之后行动，因为他们需要他的情报文件存在才能起草内容。

定时任务有时会失败。机器重启。任务卡住。在 API 调用期间网络中断。这就是基础设施，而基础设施存在故障模式。

该

文件增加了一个安全网。每次心跳时，主代理验证 cron 任务确实已运行：

```
## Cron Health Check (run on each heartbeat)

Check if any daily cron jobs have stale lastRunAtMs (>26 hours
since last run). If stale, trigger them via CLI:
`openclaw cron run <jobId> --force`

Jobs to monitor:
- Dwight Morning (8:01 AM): 01f2e5c5-3a83-4018-a725-dee59e54733e
- Kelly Viral (9:01 AM, 1:01 PM): c9458766-78bb-4eeb-b8f4-d63dc1f0e601
- Ross Engineering (10:01 AM): b12b2fc6-dd7d-4123-b904-2148a5cfb70b
- Dwight Afternoon (4:01 PM): 19ff40e4-b1b0-4d32-9d24-753ac2cf8f46
- Kelly X Drafts (5:01 PM): 05da0c81-39e1-4d06-bdcd-2dfab4562ba4
- Rachel LinkedIn (5:01 PM): 9819bc6b-7e36-406f-b0c3-d80ca383d914
```

如果任务失败或错过时间窗口，心跳机制会捕获它并强制重新运行。自我修复，无需人工干预。

使用 heartbeat 进行多个检查的批量处理，以及当时间可以略有漂移时。使用 cron 进行精确的计划和需要与主会话隔离的任务。

没有仪表盘。没有网页 UI。没有管理面板。我在 Telegram 上和我的代理交谈。

这是一个刻意的选择。我不想登录仪表盘。我不想查看网页应用。我的手机一直随身携带。Telegram 一直开着。这些代理在我当前所在的地方与我相遇。

OpenClaw 支持将 Telegram 作为频道。在设置过程中连接它，你的代理将显示为 Telegram 机器人。你给它发消息，它回复你。它会向你发送草稿，你可以批准或拒绝这些草稿。就像在你的消息应用里有一位同事一样。

莫妮卡是我的主要联系人。她处理大多数沟通，并将任务分配给其他人。当他们的定时任务生成值得查看的内容时，其他人会直接给我发消息。

我典型的早晨：我醒来，打开 Telegram，Dwight 已经给我发了一份研究总结。Kelly 有三条推文草稿等待审批。Rachel 有一条 LinkedIn 帖子已经准备好。我审阅内容，给出反馈，批准好的内容。整个过程在我喝咖啡的时候花费 10 分钟。

你不会预先设计出完美的人格。你从一个粗略的草图开始

，观察智能体的行为，并随着时间进行调整。这完全就像管理真实的人一样。

凯利的初稿里满是表情符号和感叹号。那不是我的语气。于是我给出反馈：“不要用表情符号，不要用话题标签，句子要简短有力。”她调整了自己的思路。一周后，她始终都做得很好。德怀特最初捕捉到太多噪声。每个热门的代码仓库，每一个小更新。我告诉他：“不是所有热门的东西都重要。我需要的是有效信息，不是噪声。”他调整了自己的原则。现在他的情报报告重点突出且可采取行动。

任何代理的第一个版本都是平庸的。第十个版本是不错的。第三十个版本是出色的。 你必须投入足够的迭代次数。电视角色命名为模型提供了即时的人格基准。“Dwight Schrute 能量”意味着细致、专注、务实。但真正的人格来自于数周的修正，这些修正被存储在记忆文件中。

我认同的一个建议是：给每个代理一个单一的枯燥职位名称和一个停止条件。约束能让代理更好。角色越具体，输出越好。

安全掌握在你手中。我的方法很简单：代理拥有自己的世界。我不会让他们访问我的。

Mac Mini 是他们的电脑。他们拥有自己的电子邮件账户、自己的 API 密钥以及自己的作用域访问权限。那台机器上的任何内容都不会连接到我的个人账户。

Gemini、Eleven Labs 和其他服务的 API 密钥专门针对此 OpenClaw 实例进行作用范围限定。如果出现任何问题，我可以在几秒钟内监控使用情况并终止访问。

我从不允许代理人访问我的个人账户。如果我想让他们查看电子邮件，我会转发给他们。如果我需要他们审核文档，我会在 Telegram 上分享。他们只能看到我想让他们看到的内容，仅此而已。

这与你对待新员工的原则是一样的。你不会在第一天就把所有事情的“钥匙”都交给他们。你会给他们自己的工作空间、自己的凭证，并根据需要分享信息。

网关崩溃了。 虽然很少发生，但确实会出现。解决方法：“openclaw gateway restart”

心跳系统会捕获过时的 cron 任务并强制重新运行，因此您不会丢失一整天的工作。

定时任务错过其执行窗口。 机器休眠、网络中断、API 速率限制被触发。解决方法：

自愈模式。Monica 会检查每次心跳中任务是否实际执行。如果任何任务超过 26 小时未执行，她会强制重新运行。

上下文窗口溢出。 代理在会话开始时读取过多文件，导致实际工作空间不足。解决方法：保持

简短（40-60 行）。保持

专注。仅加载今天的记忆文件和昨天的。代理不需要在每次会话中读取其完整历史记录。

代理输出质量下降。 当内存文件变得杂乱或存在矛盾时会出现这种情况。解决方法：定期内存维护。在心跳期间，代理会查看每日日志并将其提炼为干净的

条目。删除或归档旧的每日日志。

协调冲突。 两个代理试图更新同一个文件。修复方法：设计文件流为单写多读。Dwight 写入

。其他所有人都读取该文件。没有其他人写入。

最大的可靠性教训：从简单开始。一个代理，一个任务，一个计划。让它稳定运行一周。然后添加第二个代理。第一天就部署六个代理，却不明白为什么系统会出问题的人，犯的错误和在没有监控的情况下部署分布式系统是一样的。

硬件：Mac Mini M4 全新起价 499 美元。但任何一直开机的电脑都可使用，比如旧笔记本电脑、每月 5 美元的 VPS，或你现有的任何设备均可。

AI 模型成本： 我在团队中使用多种模型的组合。Claude Opus 和 Sonnet 用于大多数代理任务。Gemini Nano Banana Pro 用于特定工作流。我还通过 Ollama 测试本地模型以进一步降低成本。

-   Claude（Max 计划）：200 美元/月
    
-   Gemini API：$50-70/月
    
-   TinyFish（网页代理）：约 50 美元/月
    
-   Eleven Labs（语音）：约 50 美元/每月
    
-   Telegram： 免费
    
-   OpenClaw: 开源且免费
    

总成本： 对于一支永不停歇的团队来说， 每月不到 400 美元。

Dwight 为我节省了每天 2-3 小时的调研时间。我过去每天早上都要手动查看 X、Hacker News、GitHub 趋势和 AI 博客。现在我醒来就能看到一份优先排序、分级的摘要，其中包含来源链接和行动项。

Kelly、Pam 和 Rachel 又节省了 1-2 小时的内容撰写时间。Ross 负责了我原本会在晚上处理的工程任务。

但真正的价值不在于任何一天。 而在于数周和数月的坚持。 一个每天持续研究 30 天的代理会构建一个包含跟踪信号、趋势轨迹和模式识别的语料库，这是任何单次会话都无法产生的。我的 X 平台发布频率提高了，质量也提升了，并且在固定时间发布。Awesome LLM Apps 仓库持续增长，新闻通讯有一个可靠的研究流程为其提供支持。

这些代理无法进行原创思考、战略转向或创造性突破。它们处理我以前花数小时做的重复性、结构化工作。这让我能够去做真正需要人类大脑参与的工作。

安装 OpenClaw。编写一个

通过与你的代理沟通。选择你日常最重复的任务。对于大多数人来说，这是研究或内容撰写。设置 Telegram。创建一个 cron 任务。观察它运行一周。修复故障。

你的代理的初始输出会比较平庸。这很正常。给出反馈。观察记忆文件的增长。进行路线修正的

根据你看到的内容。到第二周末，代理应该能产出真正有用的内容。

现在你感到了这种需求。你的研究代理正在生成情报，但你仍然需要手动根据这些情报撰写推文。现在是时候引入内容代理了。设置共享文件模式：代理一写入，代理二读取。协调方式就是文件系统本身。

当你感到需要时添加代理，而非当你觉得应该添加时才添加。每一个代理都应该解决你实际遇到的真实问题。不是演示，不是概念验证，而是你工作流程中真正的缺口。

把这件事当作招聘来对待。作为创始人，你不会在第一天就招聘六名员工。你先招聘一个，让他高效工作，然后在工作量需要的时候再招聘下一个。

当你的代理运行一个月后，有些事情会发生变化。你不再把 AI 看作是一种需要时才打开的工具，而是开始把它看作是一个一直在工作的团队。

我打开 Telegram 时，会下意识地对莫妮卡说早安。放下手机前，我会跟团队说晚安。这听起来很荒谬。但经过一个月的日常互动、反馈循环以及看着他们进步，人与智能代理之间的界限变得模糊了。

模型是基础配置。每个人都能使用 Claude、GPT、Gemini。竞争优势来自模型周围的系统。The

文件。存储。调度。协调模式。文件中存储的数周修正反馈。

那个系统是你的。没有其他人拥有你的代理、记忆文件和精致个性。

每次研究梳理都让 Dwight 的知识更加丰富。每一轮反馈都让 Kelly 的草稿更加完善。Ross 修复的每一个 bug 都让他更了解你们的代码库。

我将发布更多关于我在 OpenClaw 方面的经验、自主 AI 代理团队以及不断演变的 AI 产品经理和开发者格局的内容。