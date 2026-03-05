---
title: "2026-03-05_adil_eth_adil_eth_我如何将_AI_研究转化为真正会重新查阅的笔记_OpenClaw"
source: "https://x.com/AdilMouja/status/2025266443613319546"
author:
  - "[[@adil.eth]]"
published: 2026-03-05
created: 2026-03-05
description:
tags:
  - "x"
  - "@adil.eth"
  - "ai"
  - "obsidian"
---

# 我如何将 AI 研究转化为真正会重新查阅的笔记（OpenClaw + Obsidian）

一个全天候的研究代理，能将结构化、可操作的笔记直接存入我的知识库——以及为什么这些文件比工具更重要。

每周我都有同样的经历。我向 AI 询问我正在研究的内容，得到一个真正有用的答案，然后想我应该把这个保存下来，但没有做。三周后我又得从头开始，因为对话被淹没在历史记录中，与我所知道的其他一切都脱节了。

这就是 AI 研究的一个不为人知的真相：它擅长产生洞见，却不善于保存这些洞见。即便你确实保存了这次对话——把它复制粘贴到 Notion 中、添加到书签——它可能已经过时了。AI 领域的变化速度之快，以至于六个月前的最佳实践往往已经不再适用了。

你需要的不只是保存研究的方法，而是要让它保持活力的方法。

# 哲学优先

Obsidian 首席执行官 Steph Ango（@kepano）写了一篇题为 File over app 以一种看似简单的论点：你用来创作的应用最终会消亡、转型或把你拒之门外。本地存储、归你所有的纯文本文件则有机会永久存在。

> 应用程序转瞬即逝，但你的文件有机会永存。

将此应用于 AI 输出时，其含义令人不安。你在 ChatGPT 中生成的每一个见解都存在于 ChatGPT 的基础设施中。Claude 的每一次研究会话仅在 Anthropic 维护该历史记录时存在。当工具发生变化时——而这是必然的——你积累的研究成果也会随之消失。

如果每一份 AI 研究成果都能被自动保存为你可控的本地知识库中的纯文本.md 文件会怎样？这正是这个技术栈所提供的。

# 三个工具

- OpenClaw 是一个拥有 215K GitHub 星标的开源个人 AI 助手——有史以来增长最快的开源项目。它运行在服务器上（我使用 AWS EC2 实例），并可连接到 Telegram、WhatsApp 或任何你喜欢工作的地方。可以把它想象成操作中的永不离线的大脑：它接收你的消息，决定调用哪些工具，并在你处理日常事务时编排工作流程。
- The last30days (@slashlast30days) skill is a Claude Code skill by @mvanhorn (2,900+ GitHub stars) that does something specific and genuinely useful: given any topic, it searches Reddit, X, YouTube, and the broader web for the freshest signal from the past thirty days, then synthesizes the findings into a structured, actionable report. When you ask OpenClaw to research a topic using last30days, it knows to open Claude Code, run it with the last30days skill loaded, and hand you back a clean synthesis — not a raw dump of links, but a structured breakdown of what's trending, which tools matter, and what you should pay attention to. The skill itself just produces output; where that output goes is up to you. I've configured OpenClaw with a standing instruction: whenever I say "save to Obsidian," it takes the results and writes them as a .文件放入专门的 openclaw-notes 文件夹中，文件名使用时间戳和描述性标题命名——例如 20260220-obsidian-openclaw-agentic-pkm-research.md。这种命名规范很重要：它使笔记可以按日期排序、按主题进行 grep 搜索，并且能被链中的任何其他工具立即读取。这种技能存在的原因恰恰反映了当前的一个现实：AI 领域发展速度极快，六个月前的最佳实践和工具往往已经过时。你不需要一个静态的知识库——你需要持续的、新鲜的信号。
- @obsdmdObsidian (@obsdmd): 是所有这些研究成果的归宿。如果你还没用过它，这里有个简要介绍：Obsidian 是一款本地优先的笔记应用，它将所有内容以纯 Markdown 文件的形式存储在你的设备上。它凭借生产力和个人知识管理（PKM）爱好者群体赢得了声誉——这些人重视知识组织，希望完全掌控自己的笔记。但它现在正经历第二次复兴，因为事实证明，使其受到生产力爱好者喜爱的相同特质——纯文本、本地文件、无云锁定——也使其成为 AI 生成内容的理想归宿。你的 AI 生成的每条笔记都可以与你自己的思考并存，通过 \`\[\[wikilinks\]\]\` 与其他笔记建立链接，并能被工作流中的任何其他 AI 工具读取。Obsidian 与其说是一个笔记应用，不如说是一个知识库：一个持久、可查询、不断增长的关于你所知道的一切的记录。

# 工作流

我全天候在 AWS EC2 实例上运行 OpenClaw，以 Telegram 为界面——始终运行、始终可用，无需让本地机器保持开机状态。典型的研究会话从我的手机开始。我给助手发消息——我叫它 Mouja：

研究 Obsidian + OpenClaw + 代理型 PKM 工作流

这就是全部输入了。我把手机收起来了。OpenClaw 拿起它，运行 /last30days 异步地，我不再去想它了。该技能梳理了该主题过去三十天的信号，过滤了噪声，并将综合结果交给 AI。返回的不是大脑倾倒——而是一份结构化笔记：什么在流行及其原因、带有 GitHub 链接的关键工具、新兴模式，以及与我的项目相关的具体行动项。

当我准备保存时，只需说：“保存到 Obsidian。”OpenClaw 会获取输出内容，将其保存为.md 文件到我的 openclaw-notes 文件夹，文件名包含时间戳和描述性内容，提交到版本库，并推送到 GitHub。当我在 Mac 上打开 Obsidian 时，笔记已经在那里了，有名称、日期，并且可以直接用于链接。

同步设置很简单，但值得解释一下。GitHub 位于中间，作为事实来源：EC2 实例和我的 Mac 都从同一个私有仓库进行推送和拉取操作，因此无论哪台机器先写入笔记，另一台都会自动获取。无需手动管理文件，也不会有冲突。从 Mac 到我的手机，我使用 Obsidian Sync — 这是整个方案中唯一需要付费的部分，但它能无缝处理移动设备同步，无需额外配置。

```asciidoc
EC2 (OpenClaw + Claude Code)
 ▲│
 pull ││ push
 │▼
 GitHub repo (private)
 ▲│
 push ││ pull
 │▼
 Mac (Obsidian)
 │
  Obsidian Sync
 │
 iPhone (Obsidian)
```

纯文本。我所有。可搜索。可链接。永远。

# 为什么这会加剧

大多数 AI 工作流程都是一次性交易。你得到一个答案，对话结束，并且输出与你所知道的其他内容无关。

这个在结构上有所不同。每次研究会话都会向你的知识库中存入一条新的、独立的笔记。并且由于 .md 是现代 AI 工具的原生语言——它是 Claude Code、OpenClaw 以及几乎所有智能代理都能原生读写的格式——这些笔记不会只是放在那里等待人类阅读。它们会成为其他工作流程的输入。

让 OpenClaw 研究一个主题并将其保存到你的知识库，然后让 Claude Code 读取该文件并生成着陆页原型、功能规格说明书或竞品分析。研究成果直接流入构建过程。无需复制粘贴，无需切换上下文——只需一个工具生成、另一个工具读取的文件。

Obsidian \[\[wikilink\]\] 系统会随着时间进一步拓展这一能力：笔记可以链接到之前的研究、项目片段和想法线索，因此知识库会逐渐构建出你的知识拓扑图——哪些主题相互关联，哪里存在知识空白，哪些想法是稳定的，哪些正在被积极地颠覆。

六个月后，你将拥有一张可搜索、相互关联的图谱，涵盖你曾经研究过的所有内容。AI 是工具。这个知识库是资产。

# 关于工具变更的说明

驱动此流程的人工智能模型将会改变。今天是 Claude。明天可能会是来自完全不同实验室的更好模型。OpenClaw 本身在其创建者加入 OpenAI 之后，最近已转变为开源基金会。

那些都不影响金库。

过去 30 天创建的.md 文件将在五十年后，在尚未存在的硬件上仍然可读，因为纯文本是人类有史以来最持久的格式。而现在，在 2026 年，它恰好也是每个严肃的 AI 工具都倾向于使用的格式。这并非偶然——这就是为什么整个技术栈都趋向于 Markdown。工具会改变。知识库会不断增长。

这是对这个工作流程本质最深刻的诠释：一个将转瞬即逝的 AI 生成洞察转化为持久、专属、复利式累积的知识的系统。

# 全栈

- github.com/openclaw/openclawOpenClaw → github.com/openclaw/openclaw — 215K ⭐, AWS EC2, Telegram 界面
- @slashlast30days skill by @mvanhorn → 2,900+ ⭐
- Obsidian (@obsdmd) → obsidian.md — 本地优先的 Markdown 知识库，个人使用免费
- GitHub → 同步 EC2 ↔ Mac 通过 git push/pull
- Obsidian Sync → 同步 Mac ↔ 手机

你的研究工作流程是什么样的？尤其想知道是否有人通过定时监控列表或自动化每日简报进一步推进了这一流程。