---
title: "2026-02-25_Muratcan_Koylan_Muratcan_Koylan_The_File_System_Is_the_New_D"
source: "https://x.com/koylanai/status/2025286163641118915"
author:
  - "[[@Muratcan Koylan]]"
published: 2026-02-25
created: 2026-02-25
description:
tags:
  - "x"
  - "@Muratcan Koylan"
  - "https"
  - "twimg"
---

# Muratcan Koylan # The File System Is the New D

**Muratcan Koylan**

# The File System Is the New Database: How I Built a Personal OS for AI Agents 文件系统是新的数据库：我是如何为人工智能代理构建个人操作系统的

Every AI conversation starts the same way. You explain who you are. You explain what you're working on. You paste in your style guide. You re-describe your goals. You give the same context you gave yesterday, and the day before, and the day before that. Then, 40 minutes in, the model forgets your voice and starts writing like a press release.

每次与人工智能的对话都以同样的方式开始。你先介绍自己，说明你在做什么，粘贴你的风格指南，再次描述你的目标，提供和昨天、前天、大前天一样的背景信息。然后，40分钟后，模型就忘了你的意思，开始像写新闻稿一样撰写内容。

I got tired of this. So I built a system to fix it.

我厌倦了这种情况，所以我开发了一套系统来解决这个问题。

I call it Personal Brain OS. It's a file-based personal operating system that lives inside a Git repository. Clone it, open it in Cursor or Claude Code, and the AI assistant has everything: my voice, my brand, my goals, my contacts, my content pipeline, my research, my failures. No database, no API keys, no build step. Just 80+ files in markdown, YAML, and JSONL that both humans and language models read natively.

我称之为“个人大脑操作系统”。它是一个基于文件的个人操作系统，运行在 Git 代码库中。克隆它，用 Cursor 或 Claude Code 打开，AI 助手就能获取一切：我的声音、我的品牌、我的目标、我的联系人、我的内容创作流程、我的研究、我的失败。无需数据库、无需 API 密钥、无需构建步骤。只有 80 多个 Markdown、YAML 和 JSONL 文件，人类和语言模型都能直接读取。

[

![](https://pbs.twimg.com/profile_images/2017468785473548288/43nF1d1X_x96.jpg)

](/koylanai)

Muratcan Koylan

![](https://pbs.twimg.com/profile_images/1984530242783039488/x9LWpM4z_bigger.jpg)

@koylanai

·

[Dec 30, 2025](/koylanai/status/2005827257458131321)

Context Engineering Skills 10x'd my project creation. I rebuilt my digital brain system with Claude Code using the Context Plugin, so it is now a Personal OS. It provides a complete folder-based architecture for managing: - Personal Brand - Voice, positioning, values - Content

Context Engineering Skills 使我的项目创建速度提升了 10 倍。 我使用 Claude Code 和 Context 插件重建了我的数字大脑系统，所以它现在是一个个人操作系统。 它提供了一个完整的基于文件夹的管理架构： 个人品牌——声音、定位、价值观 - 内容

Show more

[

![Image](https://pbs.twimg.com/media/G9YcHGnW8AABl6q?format=jpg&name=medium)


](/koylanai/status/2005827257458131321/photo/1)

Quote

引用

![](https://pbs.twimg.com/profile_images/2017468785473548288/43nF1d1X_normal.jpg)

Muratcan Koylan

![](https://pbs.twimg.com/profile_images/1984530242783039488/x9LWpM4z_bigger.jpg)

@koylanai

·

Oct 6, 2025

![Embedded video](https://pbs.twimg.com/amplify_video_thumb/1975080002589691904/img/PKiTlWQ7nUuStWAD?format=jpg&name=360x360)

7:31

How I built an AI agent system that automatically maintains my digital brain based on the content I engage with? My personal context engineering architecture with Claude Sonnet 4.5, Groq Compound, Browser Use, all in Cursor ![👇](https://abs-0.twimg.com/emoji/v2/svg/1f447.svg)

我是如何构建一个人工智能代理系统，根据我接触的内容自动维护我的数字大脑的？ 我的个人上下文工程架构，使用 Claude Sonnet 4.5、Groq Compound、浏览器使用，全部在 Cursor ![👇](https://abs-0.twimg.com/emoji/v2/svg/1f447.svg) 中

20

64

616

[

68K


](/koylanai/status/2005827257458131321/analytics)

I'm sharing the full architecture, the design decisions, and the mistakes so you can build your own version. Not a copy of mine; yours. The specific modules, the file schemas, the skill definitions will look different for your work. But the patterns transfer. The principles for structuring information for AI agents are universal. Take what fits, ignore what doesn't, and ship something that makes your AI actually useful instead of generically helpful.

我分享完整的架构、设计决策和错误，以便您可以构建自己的版本。不是复制我的版本，而是您自己的版本。具体的模块、文件模式和技能定义会因您的工作而异，但模式是通用的。构建人工智能代理信息结构的原则是通用的。取其精华，去其糟粕，最终交付真正有用的人工智能，而不是泛泛而谈的辅助工具。

Here's how I built it, why the architecture decisions matter, and what I learned the hard way.

以下是我构建它的过程，为什么架构决策很重要，以及我从惨痛经历中学到的东西。

## 

1) THE CORE PROBLEM: CONTEXT, NOT PROMPTS

1）核心问题：语境，而非提示

Most people think the bottleneck with AI assistants is prompting. Write a better prompt, get a better answer. That's true for single interactions and production agent prompts. It falls apart when you want an AI to operate as you across dozens of tasks over weeks and months.

大多数人认为人工智能助手的瓶颈在于提示。编写更好的提示，就能得到更好的答案。这对于单次交互和生产环境中的助手提示来说确实如此。但当你想让人工智能在数周甚至数月的时间里，像你一样完成数十项任务时，这种方法就行不通了。

The Attention Budget: Language models have a finite context window, and not all of it is created equal. This means dumping everything you know into a system prompt isn't just wasteful, it actively degrades performance. Every token you add competes for the model's attention.

注意力预算： 语言模型的上下文窗口是有限的，而且并非所有信息都同等重要。这意味着把所有已知信息都一股脑地倾倒到系统提示符中不仅浪费资源，还会降低性能。你添加的每个词元都会争夺模型的注意力。

[

![Image](https://pbs.twimg.com/media/HBsn1YtWAAAhgKc?format=jpg&name=medium)


](/koylanai/article/2025286163641118915/media/2025256255552356352)

Our brains work similarly. When someone briefs you for 15 minutes before a meeting, you remember the first thing they said and the last thing they said. The middle blurs. Language models have the same U-shaped attention curve, except theirs is mathematically measurable. Token position affects recall probability. The newer models are getting better at this, but still, you are distracting the model from focusing on what matters most. Knowing this changes how you design information architecture for AI systems.

我们的大脑运作方式也类似。如果有人在会议前 15 分钟向你简要介绍情况，你会记住他们说的第一句话和最后一句话，中间的内容则会变得模糊。语言模型也具有类似的 U 型注意力曲线，只不过它们的注意力曲线是可以用数学方法测量的。词元位置会影响回忆概率。虽然新模型在这方面有所改进，但你仍然会分散模型的注意力，使其无法专注于最重要的信息。了解这一点会改变你为人工智能系统设计信息架构的方式。

[

![](https://pbs.twimg.com/profile_images/2017468785473548288/43nF1d1X_x96.jpg)

](/koylanai)

Muratcan Koylan

![](https://pbs.twimg.com/profile_images/1984530242783039488/x9LWpM4z_bigger.jpg)

@koylanai

·

[Dec 12, 2025](/koylanai/status/1999192104850133146)

AI Agent Personas should simulate the structure of human reasoning. I’ve been arguing that you cannot "invent" a digital expert agent using just prompt engineering. You have to extract the expert via deep interviewing. A new NeurIPS paper, "Simulating Society Requires

AI 代理角色应该模拟人类的推理结构。 我一直认为，仅仅依靠提示工程是无法“发明”出一个数字专家代理的。你必须通过深度访谈来提取专家信息。 一篇新的 NeurIPS 论文，题为“模拟社会需要……”

Show more

[

![Image](https://pbs.twimg.com/media/G76HOSwXgAAZaJB?format=jpg&name=medium)


](/koylanai/status/1999192104850133146/photo/1)

Quote

引用

![](https://pbs.twimg.com/profile_images/2017468785473548288/43nF1d1X_normal.jpg)

Muratcan Koylan

![](https://pbs.twimg.com/profile_images/1984530242783039488/x9LWpM4z_bigger.jpg)

@koylanai

·

Dec 10, 2025

[

![Image](https://pbs.twimg.com/media/G7wtzSvX0AAYKCf?format=jpg&name=240x240)


](/koylanai/status/1998530190847390025/photo/1)

You should NOT use LLMs to generate synthetic human-like profiles. I just read the NeurIPS paper "LLM Generated Persona is a Promise with a Catch" and it confirms a suspicion we’ve held for a long time: You cannot "invent" a realistic human being using just statistics and an

你不应该使用 LLM 来生成合成的类人模型。 我刚读了 NeurIPS 的论文《LLM 生成的人物形象是一个有缺陷的承诺》，它证实了我们长期以来的一个怀疑：你无法仅凭统计数据和……就“创造”出一个真实的人。

23

73

405

[

53K


](/koylanai/status/1999192104850133146/analytics)

Instead of writing one massive system prompt, I split Personal OS into 11 isolated modules. When I ask the AI to write a blog post, it loads my voice guide and brand files. When I ask it to prepare for a meeting, it loads my contact database and interaction history. The model never sees network data during a content task, and never sees content templates during a meeting prep task.

我没有编写一个庞大的系统提示符，而是将个人操作系统拆分成 11 个独立的模块。当我让 AI 撰写博客文章时，它会加载我的语音指南和品牌文件。当我让它准备会议时，它会加载我的联系人数据库和互动记录。在内容创作任务中，模型不会接触到任何网络数据；在会议准备任务中，模型也不会接触到任何内容模板。

[

![](https://pbs.twimg.com/profile_images/2017468785473548288/43nF1d1X_x96.jpg)

](/koylanai)

Muratcan Koylan

![](https://pbs.twimg.com/profile_images/1984530242783039488/x9LWpM4z_bigger.jpg)

@koylanai

·

[Dec 10, 2025](/koylanai/status/1998530190847390025)

You should NOT use LLMs to generate synthetic human-like profiles. I just read the NeurIPS paper "LLM Generated Persona is a Promise with a Catch" and it confirms a suspicion we’ve held for a long time: You cannot "invent" a realistic human being using just statistics and an

你不应该使用 LLM 来生成合成的类人模型。 我刚读了 NeurIPS 的论文《LLM 生成的人物形象是一个有缺陷的承诺》，它证实了我们长期以来的一个怀疑：你无法仅凭统计数据和……就“创造”出一个真实的人。

Show more

[

![Image](https://pbs.twimg.com/media/G7wtzSvX0AAYKCf?format=jpg&name=medium)


](/koylanai/status/1998530190847390025/photo/1)

58

91

540

[

90K


](/koylanai/status/1998530190847390025/analytics)

Progressive Disclosure: This is the architectural pattern that makes the whole system work. Instead of loading all 80+ files at once, the system uses three levels. Level 1 is a lightweight routing file that's always loaded. It tells the AI which module is relevant. Level 2 is module-specific instructions that load only when that module is needed. Level 3 is the actual data JSONL logs, YAML configs, research documents, loaded only when the task requires them.

渐进式披露： 这是整个系统运行的基础架构模式。系统并非一次性加载 80 多个文件，而是采用三层加载方式。 第一层是一个轻量级的路由文件，始终加载，用于告知 AI 哪个模块是相关的。 第二层是模块特定的指令 ，仅在需要时加载。 第三层是实际数据，包括 JSONL 日志、YAML 配置和研究文档，仅在任务需要时加载。

This mirrors how experts operate. The three levels create a funnel: broad routing, then module context, then specific data. At each step, the model has exactly what it needs and nothing more.

这与专家的工作方式如出一辙。这三个层级构成了一个漏斗：首先是宏观路径，然后是模块上下文，最后是具体数据。在每个步骤中，模型都只拥有它需要的，不多也不少。

[

![Image](https://pbs.twimg.com/media/HBsoQRQXQAEVWn1?format=jpg&name=medium)


](/koylanai/article/2025286163641118915/media/2025256717408223233)

My routing file is \`

[SKILL.md](//SKILL.md)

\` that tells the agent "this is a content task, load the brand module" or "this is a network task, load the contacts." The module instruction files (\`

[CONTENT.md](//CONTENT.md)

\`, \`

[OPERATIONS.md](//OPERATIONS.md)

\`, \`

[NETWORK.md](//NETWORK.md)

\`) are 40-100 lines each, with file inventories, workflow sequences, and an \`<instructions>\` block with behavioural rules for that domain. Data files load last, only when needed. The AI reads contacts line by line from JSONL rather than parsing the entire file. Three levels, with a maximum of two hops to any piece of information.

我的路由文件是 \`

[技能.md](//SKILL.md)

\` 告诉代理“这是一个内容任务，加载品牌模块”或“这是一个网络任务，加载联系人”。模块指令文件（\`

[内容.md](//CONTENT.md)

\`, \`

[操作.md](//OPERATIONS.md)

\`, \`

[网络.md](//NETWORK.md)

\`)\` 每个文件包含 40-100 行，包含文件清单、工作流程序列以及一个包含该领域行为规则的 \`<instructions>\` 块。数据文件最后加载，仅在需要时加载。AI 逐行读取 JSONL 中的联系人信息，而不是解析整个文件。信息流分为三层，最多需要两跳才能获取任何信息。

[

![](https://pbs.twimg.com/profile_images/2017468785473548288/43nF1d1X_x96.jpg)

](/koylanai)

Muratcan Koylan

![](https://pbs.twimg.com/profile_images/1984530242783039488/x9LWpM4z_bigger.jpg)

@koylanai

·

[Dec 7, 2025](/koylanai/status/1997444237890081104)

Most people treat AI like Google: ask a question, get an answer. But what if AI could think \*like/with you?\* I reverse-engineer "Theory of Mind" to test if the model can form a "theory of my mind". Using AI as a mirror to understand myself by giving it personal context and

大多数人对待人工智能的方式就像对待谷歌：问问题，得到答案。但如果人工智能能够像你一样思考，或者与你一起思考呢？ 我对“心智理论”进行逆向工程，以检验该模型是否能够形成“我的心智理论”。 利用人工智能作为一面镜子，通过赋予它个人背景信息来了解我自己。

Show more

![](https://pbs.twimg.com/amplify_video_thumb/1997438305894371329/img/Tn9XiH9Nui8tMyr7.jpg)

Quote

引用

![](https://pbs.twimg.com/profile_images/1998536249003380736/ew_SXOsl_normal.png)

Carlos E. Perez

@IntuitMachine

·

Dec 6, 2025

[

![Image](https://pbs.twimg.com/media/G7c8F_pWYAA5o2b?format=png&name=240x240)


](/IntuitMachine/status/1997131059805163542/photo/1)

You know how some people seem to have a magic touch with LLMs? They get incredible, nuanced results while everyone else gets generic junk. The common wisdom is that this is a technical skill. A list of secret hacks, keywords, and formulas you have to learn. But a new paper

你知道有些人似乎对法学硕士（LLM）有种神奇的魔力吗？他们能获得令人难以置信、细致入微的成果，而其他人得到的却是千篇一律的垃圾。 人们普遍认为这是一项技术技能。你需要学习一系列秘而不宣的技巧、关键词和公式。 但一篇新论文

3

14

125

[

23K


](/koylanai/status/1997444237890081104/analytics)

The Agent Instruction Hierarchy: I built three layers of instructions that scope how the AI behaves at different levels. At the repository level, \`

[CLAUDE.md](//CLAUDE.md)

\` is the onboarding document -- every AI tool reads it first and gets the full map of the project. At the brain level, \`

[AGENT.md](//AGENT.md)

\` contains seven core rules and a decision table that maps common requests to exact action sequences. At the module level, each directory has its own instruction file with domain-specific behavioral constraints.

智能体指令层级： 我构建了三层指令，分别控制人工智能在不同层级的行为方式。在存储库层级，\`

[CLAUDE.md](//CLAUDE.md)

这是入职文档——每个人工智能工具都会首先读取它，并获取项目的完整地图。在大脑层面，

[代理.md](//AGENT.md)

包含七条核心规则和一个决策表，该决策表将常见请求映射到精确的操作序列。在模块级别，每个目录都有自己的指令文件，其中包含特定领域的行为约束。

[

![Image](https://pbs.twimg.com/media/HBsxNHyXYAATt1r?format=jpg&name=medium)


](/koylanai/article/2025286163641118915/media/2025266558931525632)

This solves the "conflicting instructions" problem that plagues large AI projects. When everything lives in one system prompt, rules contradict each other. A content creation instruction might conflict with a networking instruction. By scoping rules to their domain, you eliminate conflicts and give the agent clear, non-overlapping guidance. The hierarchy also means you can update one module's rules without risking regression in another module's behavior.

这解决了困扰大型人工智能项目的“指令冲突”问题。当所有指令都集中在一个系统提示中时，规则之间就会相互矛盾。例如，内容创建指令可能与网络建设指令冲突。通过将规则限定在其各自的领域内，可以消除冲突，并为智能体提供清晰且互不重叠的指导。这种层级结构还意味着，您可以更新一个模块的规则，而不会导致其他模块的行为出现倒退。

[

![Image](https://pbs.twimg.com/media/HBspOASW0AA-E6d?format=jpg&name=medium)


](/koylanai/article/2025286163641118915/media/2025257778005069824)

My \`

[AGENT.md](//AGENT.md)

\` is a decision table. The AI reads "User says 'send email to Z'" and immediately sees:

我的

[代理.md](//AGENT.md)

\` 是一个决策表。人工智能读取到“用户说‘向 Z 发送电子邮件’”，并立即看到：

1.  Step 1, look up contact in HubSpot.
 
 第一步，在 HubSpot 中查找联系人。
 
2.  Step 2, verify email address.
 
 第二步，验证电子邮件地址。
 
3.  Step 3, send via Gmail.
 
 第三步，通过 Gmail 发送。
 

Module-level files like \`

[OPERATIONS.md](//OPERATIONS.md)

\` define priority levels (P0: do today, P1: this week, P2: this month, P3: backlog) so the agent triages tasks consistently. The agent follows the same priority system I use because the system is codified, not implied.

模块级文件，例如\`

[操作.md](//OPERATIONS.md)

定义优先级级别（P0：今天完成，P1：本周完成，P2：本月完成，P3：待办事项），以便代理能够一致地对任务进行分类。代​​理遵循我使用的相同优先级系统，因为该系统是明确规定的，而不是隐含的。

## 

2) THE FILE SYSTEM AS MEMORY

2）文件系统即内存

One of the most counterintuitive decisions I made: no database. No vector store. No retrieval system except Cursor or Claude Code's features. Just files on disk, versioned with Git.

我做出的最反直觉的决定之一：没有数据库，没有向量存储，除了 Cursor 或 Claude Code 的功能之外，没有其他检索系统。只有磁盘上的文件，用 Git 进行版本控制。

[

![Image](https://pbs.twimg.com/media/HBsqFxuW8AAdrU-?format=jpg&name=medium)


](/koylanai/article/2025286163641118915/media/2025258736168660992)

Format-Function Mapping: Every file format in the system was chosen for a specific reason related to how AI agents process information. JSONL for logs because it's append-only by design, stream-friendly (the agent reads line by line without parsing the entire file), and every line is self-contained valid JSON. YAML for configuration because it handles hierarchical data cleanly, supports comments, and is readable by both humans and machines without the noise of JSON brackets. Markdown for narrative because LLMs read it natively, it renders everywhere, and it produces clean diffs in Git.

格式-功能映射： 系统中每种文件格式的选择都基于特定原因，这些原因与人工智能代理处理信息的方式相关。日志使用 JSONL，因为它设计为仅追加式，对流式处理友好（代理逐行读取，无需解析整个文件），并且每一行都是独立的有效 JSON。配置使用 YAML，因为它能清晰地处理层级数据，支持注释，并且对人和机器都易于阅读，避免了 JSON 括号带来的冗余。叙述性内容使用 Markdown，因为 LLM 可以原生读取它，它可以在任何地方渲染，并且在 Git 中生成清晰的差异。

[

![](https://pbs.twimg.com/profile_images/2017468785473548288/43nF1d1X_x96.jpg)

](/koylanai)

Muratcan Koylan

![](https://pbs.twimg.com/profile_images/1984530242783039488/x9LWpM4z_bigger.jpg)

@koylanai

·

[Feb 16](/koylanai/status/2023405681080938932)

The problem is how memory gets into the context window and what happens when compaction wipes it. OpenClaw loads MEMORY\[.\]md plus the last two days of daily logs at session start. Static injection. Everything gets stuffed into the context window upfront. When the window fills

问题在于内存如何进入上下文窗口，以及压缩操作清除内存时会发生什么。 OpenClaw 在会话开始时加载 MEMORY\[.\]md 文件以及最近两天的每日日志。静态注入。所有内容都会预先加载到上下文窗口中。当窗口填满时

Show more

[

![Image](https://pbs.twimg.com/media/HBSDv5aW8AAZaVZ?format=png&name=medium)


](/koylanai/status/2023405681080938932/photo/1)

Quote

引用

![](https://pbs.twimg.com/profile_images/1996831016720486400/vycHz0uG_normal.jpg)

@levelsio

@levelsio

·

Feb 16

How did you guys fix persistent memory with OpenClaw? My bot keeps forgetting stuff, I already have qmd installed

你们是怎么解决 OpenClaw 持久内存问题的？我的机器人总是忘记一些东西，我已经安装了 qmd。

34

58

664

[

86K


](/koylanai/status/2023405681080938932/analytics)

JSONL's append-only nature prevents a category of bugs where an agent accidentally overwrites historical data. I've seen this happen with JSON files agent writes the whole file, loses three months of contact history. With JSONL, the agent can only add lines. Deletion is done by marking entries as \`"status": "archived"\`, which preserves the full history for pattern analysis. YAML's comment support means I can annotate my goals file with context the agent reads but that doesn't pollute the data structure. And Markdown's universal rendering means my voice guide looks the same in Cursor, on GitHub, and in any browser.

JSONL 的追加特性避免了一类错误，即代理程序意外覆盖历史数据。我曾见过这种情况发生在 JSON 文件上：代理程序写入整个文件，导致三个月的联系人历史记录丢失。而使用 JSONL，代理程序只能添加行。删除操作通过将条目标记为 \`"status": "archived"\` 来实现，这样可以保留完整的历史记录以进行模式分析。YAML 的注释支持意味着我可以为目标文件添加代理程序可以读取的上下文注释，而不会污染数据结构。Markdown 的通用渲染功能意味着我的语音指南在 Cursor、GitHub 和任何浏览器中看起来都一样。

[

![](https://pbs.twimg.com/profile_images/2017468785473548288/43nF1d1X_x96.jpg)

](/koylanai)

Muratcan Koylan

![](https://pbs.twimg.com/profile_images/1984530242783039488/x9LWpM4z_bigger.jpg)

@koylanai

·

[Dec 5, 2025](/koylanai/status/1996905189656211931)

OpenAI wants markdown structure. Anthropic prefers XML tags. Google emphasizes few-shot examples. So I built a simple agent system that reads the official prompting docs and applies them to the given prompt. Each optimizer runs a ReAct loop: - list\_provider\_docs → discover

OpenAI 倾向于使用 Markdown 结构。Anthropic 更喜欢 XML 标签。Google 则强调少量示例。 所以我构建了一个简单的代理系统，它可以读取官方提示文档并将其应用于给定的提示。 每个优化器都运行一个 ReAct 循环： - list\_provider\_docs → 发现

Show more

![](https://pbs.twimg.com/amplify_video_thumb/1996899836021395456/img/tgLJMRKbjUv_MHUq.jpg)

22

50

671

[

63K


](/koylanai/status/1996905189656211931/analytics)

My system uses 11 JSONL files (posts, contacts, interactions, bookmarks, ideas, metrics, experiences, decisions, failures, engagement, meetings), 6 YAML files (goals, values, learning, circles, rhythms, heuristics), and 50+ Markdown files (voice guides, research, templates, drafts, todos). Every JSONL file starts with a schema line: \`{"\_schema": "contact", "\_version": "1.0", "\_description": "..."}\`. The agent always knows the structure before reading the data.

我的系统使用 11 个 JSONL 文件 （帖子、联系人、互动、书签、想法、指标、体验、决策、失败、参与度、会议）、 6 个 YAML 文件 （目标、价值观、学习、圈子、节奏、启发式方法） 和 50 多个 Markdown 文件 （语音指南、研究、模板、草稿、待办事项）。 每个 JSONL 文件都以一个 schema 行开头：\`{"\_schema": "联系人", "\_version": "1.0", "\_description": "..."}\`。代理在读取数据之前始终知道文件结构。

[

![](https://pbs.twimg.com/profile_images/2017468785473548288/43nF1d1X_x96.jpg)

](/koylanai)

Muratcan Koylan

![](https://pbs.twimg.com/profile_images/1984530242783039488/x9LWpM4z_bigger.jpg)

@koylanai

·

[Dec 5, 2025](/koylanai/status/1996757974610559171)

Your best people can't document their expertise because they don't know what they know until they're asked. We built an interviewer that achieves peer status, so experts reveal the judgment patterns they'd only share with a colleague. I wrote a blog about how we architected the

你最优秀的人才无法证明自己的专业知识，因为在被问及时，他们并不知道自己掌握了哪些知识。 我们开发了一款能够达到同行地位的面试官，因此专家们会展现出他们只会与同事分享的判断模式。 我写了一篇博客，讲述了我们如何构建……

Show more

[

![Image](https://pbs.twimg.com/media/G7XmZw0XsAAoB0S?format=jpg&name=small)


](/koylanai/status/1996757974610559171/photo/1)

[

![Image](https://pbs.twimg.com/media/G7XoDGtW8AAr-U0?format=jpg&name=small)


](/koylanai/status/1996757974610559171/photo/2)

Quote

引用

![Square profile picture](https://pbs.twimg.com/profile_images/1798110641414443008/XP8gyBaY_normal.jpg)

Anthropic

@AnthropicAI

·

Dec 5, 2025

We’re launching Anthropic Interviewer, a new tool to help us understand people’s perspectives on AI. It’s now available at http://claude.ai/interviewer for a week-long pilot.

我们即将推出“人格访谈者”，这是一款帮助我们了解人们对人工智能的看法的新工具。 现在可以在 http://claude.ai/interviewer 上进行为期一周的试用。

37

127

1.5K

[

249K


](/koylanai/status/1996757974610559171/analytics)

Episodic Memory: Most "second brain" systems store facts. Mine stores judgment as well. The \`memory/\` module contains three append-only logs: \`experiences.jsonl\` (key moments with emotional weight scores from 1-10), \`decisions.jsonl\` (key decisions with reasoning, alternatives considered, and outcomes tracked), and \`failures.jsonl\` (what went wrong, root cause, and prevention steps).

情景记忆： 大多数“第二大脑”系统存储事实。我的系统也存储判断。\`memory/\` 模块包含三个仅追加的日志：\`experiences.jsonl\` （关键时刻，带有 1-10 的情感权重评分） 、\`decisions.jsonl\` （关键决策，包含推理过程、考虑的替代方案和跟踪的结果） 和\`failures.jsonl\` （出了什么问题、根本原因和预防措施）。

[

![Image](https://pbs.twimg.com/media/HBsq81mXsAEoTyy?format=jpg&name=medium)


](/koylanai/article/2025286163641118915/media/2025259682101702657)

There's a difference between an AI that has your files and an AI that has your judgment. Facts tell the agent what happened. Episodic memory tells the agent what mattered, what I'd do differently, and how I think about tradeoffs. When the agent encounters a decision similar to one I've logged, it can reference my past reasoning instead of generating generic advice. The failures log is the most valuable, it encodes pattern recognition that took real pain to acquire.

拥有你过往记录的 AI 和拥有你判断的 AI 之间是有区别的。事实告诉智能体发生了什么，而情景记忆则告诉智能体什么才是最重要的，我会如何改进，以及我是如何权衡利弊的。当智能体遇到与我记录过的决策类似的情况时，它可以参考我过去的推理过程，而不是生成通用建议。失败日志是最有价值的，它记录了我苦心钻研才获得的模式识别能力。

> When I was deciding whether to accept Antler Canada's $250K investment or join
> 
> [Sully.ai](//Sully.ai)
> 
> as Context Engineer, the decision log captured both options, the reasoning for each, and the outcome. If a similar career tradeoff comes up, the agent doesn't give me generic career advice. It references how I actually think about these decisions: "Learning > Impact > Revenue > Growth" is my priority order, and "Can I touch everything? Will I learn at the edge of my capability? Do I respect the founders?" is my company-joining framework.
> 
> 当我决定是否接受 Antler Canada 的 25 万美元投资或加入时
> 
> [Sully.ai](//Sully.ai)
> 
> 作为情境工程师，决策日志记录了所有选项、每个选项背后的原因以及最终结果。如果遇到类似的职业选择，系统不会给我千篇一律的职业建议，而是会参考我实际的思考方式：“学习、影响力、收入和增长”是我的优先级顺序，而“我能否接触到所有方面？我能否在自身能力的极限范围内学习？我是否尊重创始人？”则是我选择加入公司的框架。

Cross-Module References: The system uses a flat-file relational model. No database, but structured enough for agents to join data across files. \`contact\_id\` in \`interactions.jsonl\` points to entries in \`contacts.jsonl\`. \`pillar\` in \`ideas.jsonl\` maps to content pillars defined in \`identity/brand.md\`. Bookmarks feed content ideas. Post metrics feed weekly reviews. The modules are isolated for loading, but connected for reasoning.

跨模块引用： 该系统采用平面文件关系模型。虽然没有数据库，但结构足够清晰，代理可以跨文件连接数据。\`interactions.jsonl\` 中的 \`contact\_id\` 指向 \`contacts.jsonl\` 中的条目。\`ideas.jsonl\` 中的 \`pillar\` 映射到 \`identity/brand.md\` 中定义的内容支柱。书签提供内容创意。帖子指标用于每周评论。各模块在加载时相互独立，但在推理过程中相互关联。

Isolation without connection is just a pile of folders. The cross-references let the agent traverse the knowledge graph when needed. "Prepare for my meeting with Sarah" triggers a lookup chain: find Sarah in contacts, pull her interactions, check pending todos involving her, compile a brief. The agent follows the references across modules without loading the entire system.

孤立无援的局面就像一堆文件夹。交叉引用让智能体能够在需要时遍历知识图谱。“准备与 Sarah 的会面”会触发一个查找链：在联系人中查找 Sarah，提取她的互动记录，检查与她相关的待办事项，并整理一份简报。智能体无需加载整个系统，即可跨模块跟踪这些引用。

My pre-meeting workflow chains three files: \`contacts.jsonl\` (who they are), \`interactions.jsonl\` (filtered by contact\_id for history), and \`

[todos.md](//todos.md)

\` (any pending items). The agent produces a one-page brief with relationship context, last conversation summary, and open follow-ups. No manual assembly. The data structure makes the workflow possible.

我的会前工作流程包含三个文件：\`contacts.jsonl\`（联系人信息）、\`interactions.jsonl\`（按 contact\_id 筛选以记录互动历史）和\`

[todos.md](//todos.md)

（任何待办事项）。代理会生成一份包含关系背景、上次对话摘要和待办事项的单页简报。无需手动整理。数据结构使工作流程成为可能。

## 

3) THE SKILL SYSTEM: TEACHING AI HOW TO DO YOUR WORK

3）技能系统：教人工智能如何完成你的工作

Files store knowledge. Skills encode process. I built Agent Skills following the Anthropic Agent Skills standard, structured instructions that tell the AI how to perform specific tasks with quality gates baked in.

文件存储知识，技能编码流程。我遵循人机交互代理技能标准构建了代理技能，该标准包含结构化的指令，告诉人工智能如何执行特定任务，并内置了质量控制机制。

[

![](https://pbs.twimg.com/profile_images/2017468785473548288/43nF1d1X_x96.jpg)

](/koylanai)

Muratcan Koylan

![](https://pbs.twimg.com/profile_images/1984530242783039488/x9LWpM4z_bigger.jpg)

@koylanai

·

[Dec 28, 2025](/koylanai/status/2005082048973905938)

Most "agentic" failures happen because the model lacks specific domain knowledge. Here I'm showing how loading a Skills Plugin solves that for dataset generation. I turned a research paper (shows fine-tuning dataset creation from books) into a Skill and just gave a book link

大多数“代理”故障都是由于模型缺乏特定领域知识造成的。 这里我展示了如何通过加载技能插件来解决数据集生成的问题。我将一篇研究论文（展示了如何从书籍中优化数据集的创建）转换成了一个技能，并提供了一个书籍链接。

Show more

![](https://pbs.twimg.com/amplify_video_thumb/2005080230134771712/img/sL0lQi7olj8DXhO3.jpg)

Quote

引用

![](https://pbs.twimg.com/profile_images/2017468785473548288/43nF1d1X_normal.jpg)

Muratcan Koylan

![](https://pbs.twimg.com/profile_images/1984530242783039488/x9LWpM4z_bigger.jpg)

@koylanai

·

Dec 27, 2025

[

![Image](https://pbs.twimg.com/media/G9LBIxNXgAAQk-P?format=jpg&name=360x360)


](/koylanai/status/2004877190911950881/photo/1)

I wanted to try this, so I trained Qwen3-8B-Base on Gertrude Stein's "Three Lives" (1909) with Thinking Machines. The model now writes in Stein's repetitive, rhythmic voice and gets Human Written label from AI Detection tools like Pangram. https://muratcankoylan.com/projects/gertrude-stein-style-training/… This became

我想尝试一下，所以我用 Thinking Machines 对 Qwen3-8B-Base 进行了训练，训练内容是 Gertrude Stein 的《三生》（1909 年）。 该模型现在以斯坦因重复、有节奏的声音写作，并从 Pangram 等 AI 检测工具获得“人类书写”标签。 https://muratcankoylan.com/projects/gertrude-stein-style-training/ …​ 这变成了

25

78

576

[

103K


](/koylanai/status/2005082048973905938/analytics)

Auto-Loading vs. Manual Invocation: Two types of skills solve two different problems. Reference skills (\`voice-guide\`, \`writing-anti-patterns\`) set \`user-invocable: false\` in their YAML frontmatter. The agent reads the description field and injects them automatically whenever the task involves writing. I never invoke them, they activate silently, every time. Task skills (\`/write-blog\`, \`/topic-research\`, \`/content-workflow\`) set \`disable-model-invocation: true\`. The agent can't trigger them on its own. I type the slash command, and the skill becomes the agent's complete instruction set for that task.

自动加载与手动调用： 两种类型的技能解决两种不同的问题。参考技能（例如 \`voice-guide\`、\`writing-anti-patterns\`）在其 YAML 前置元数据中设置了 \`user-invocable: false\`。当任务涉及写作时，智能体会读取描述字段并自动注入这些技能。我无需手动调用它们，它们每次都会静默激活。任务技能（例如 \`/write-blog\`、\`/topic-research\`、\`/content-workflow\`）设置了 \`disable-model-invocation: true\`。智能体无法自行触发这些技能。我需要输入斜杠命令，该技能才会成为智能体执行该任务的完整指令集。

[

![](https://pbs.twimg.com/profile_images/2017468785473548288/43nF1d1X_x96.jpg)

](/koylanai)

Muratcan Koylan

![](https://pbs.twimg.com/profile_images/1984530242783039488/x9LWpM4z_bigger.jpg)

@koylanai

·

[Jan 29](/koylanai/status/2016684758588154239)

Progressive disclosure is not reliable because LLMs are inherently lazy. "In 56% of eval cases, the skill was never invoked. The agent had access to the documentation but didn't use it." Vercel ran evals on Next.js 16 APIs that aren't in model training data to test whether

渐进式披露不可靠，因为法学硕士生天生懒惰。 “在56%的评估案例中，这项技能从未被运用。评估人员可以查阅相关文档，但却没有使用。” Vercel 对 Next.js 的 16 个 API 进行了评估，这些 API 不在模型训练数据中，以测试它们是否

Show more

Quote

引用

![Square profile picture](https://pbs.twimg.com/profile_images/1767351110228918272/3Pndc5OT_normal.png)

Vercel

@vercel

·

Jan 29

We're experimenting with ways to keep AI agents in sync with the exact framework versions in your projects. Skills, 𝙲𝙻𝙰𝚄𝙳𝙴.𝚖𝚍, and more. But one approach scored 100% on our Next.js evals: https://vercel.com/blog/agents-md\-outperforms-skills-in-our-agent-evals…

我们正在尝试各种方法，使 AI 代理与您项目中的框架版本保持同步。技能、CLAWE.m 等。 但有一种方法在我们的 Next.js 评估中获得了 100% 的分数： https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals …​

63

120

1.1K

[

196K


](/koylanai/status/2016684758588154239/analytics)

Auto-loading solves the consistency problem. I don't have to remember to say "use my voice" every time I ask for a draft. The system remembers for me. Manual invocation solves the precision problem. A research task has different quality gates than a blog post. Keeping them separate prevents the agent from conflating two different workflows. The YAML frontmatter is the mechanism, and a few metadata fields control the entire loading behaviour.

自动加载解决了一致性问题。我无需每次请求草稿时都记住“使用语音”，系统会自动记住。手动调用解决了精确性问题。研究任务和博客文章的质量门槛不同。将它们分开可以防止代理混淆两种不同的工作流程。YAML 前置元数据是实现这一机制的关键，一些元数据字段控制着整个加载行为。

[

![Image](https://pbs.twimg.com/media/HBsrS_2W8AAyLgY?format=jpg&name=medium)


](/koylanai/article/2025286163641118915/media/2025260062810238976)

When I type \`/write-blog context engineering for marketing teams\`, five things happen automatically: the voice guide loads (how I write), the anti-patterns load (what I never write), the blog template loads (7-section structure with word count targets), the persona folder is checked for audience profiles, and the research folder is checked for existing topic research. One slash command triggers a full context assembly. The skill file itself says "Read \`brand/tone-of-voice.md\`", it references the source module, never duplicates the content. Single source of truth.

当我输入 \`/write-blog context engineering for marketing teams\` 时，五件事会自动发生：加载语音指南（我的写作方式）、加载反模式（我从不写的内容）、加载博客模板（包含七个部分的结构和字数目标）、检查用户画像文件夹中的受众群体信息，以及检查研究文件夹中是否存在已有的主题研究。一个斜杠命令即可触发完整的上下文构建。技能文件本身会显示“读取 \`brand/tone-of-voice.md\`”，它引用了源模块，并且从不重复内容。确保单一数据源的真实性。

[

![](https://pbs.twimg.com/profile_images/2017468785473548288/43nF1d1X_x96.jpg)

](/koylanai)

Muratcan Koylan

![](https://pbs.twimg.com/profile_images/1984530242783039488/x9LWpM4z_bigger.jpg)

@koylanai

·

[Jan 7](/koylanai/status/2008824728824451098)

I just built Ralph Wiggum Copywriter; learns your voice, critiques its own work, rewrites until it's actually good. Self-critique loop hits different.

我刚刚开发了 Ralph Wiggum 文案撰写工具；它能学习你的写作风格，评价自己的作品，并不断修改直到达到理想状态。 自我批评的恶性循环带来的冲击是不同的。

[

![Image](https://pbs.twimg.com/media/G-DEzNFXkAALZ_Y?format=jpg&name=medium)


](/koylanai/status/2008824728824451098/photo/1)

57

102

1.6K

[

98K


](/koylanai/status/2008824728824451098/analytics)

The Voice System: My voice is encoded as structured data and ngl with some vibes. The voice profile rates five attributes on a 1-10 scale: Formal/Casual (6), Serious/Playful (4), Technical/Simple (7), Reserved/Expressive (6), Humble/Confident (7). The anti-patterns file contains 50+ banned words across three tiers, banned openings, structural traps (forced rule of three, copula avoidance, excessive hedging), and a hard limit of one em-dash per paragraph.

语音系统： 我的声音被编码为结构化数据，并带有一些个人风格。语音档案以 1-10 分制评估五个属性：正式/随意 (6)、严肃/轻松 (4)、技术性/简洁 (7)、内敛/富有表现力 (6)、谦逊/自信 (7)。反模式文件包含 50 多个禁用词，分为三个层级，此外还包括禁用的开头语、结构陷阱（强制三词规则、避免使用系词、过度使用缓和语），以及每段最多只能使用一个破折号的限制。

[

![Image](https://pbs.twimg.com/media/HBsr1oBXwAAn6h5?format=jpg&name=medium)


](/koylanai/article/2025286163641118915/media/2025260657709400064)

Most people describe their voice with adjectives: "professional but approachable." That's useless for an AI. A 7 on the Technical/Simple scale tells the model exactly where to land. The banned word list is even more powerful; it's easier to define what you're NOT than what you are. The agent checks every draft against the anti-patterns list and rewrites anything that triggers it. The result is content that sounds like me because the guardrails prevent it from sounding like AI.

大多数人会用形容词来描述自己的声音：“专业但平易近人”。这对人工智能来说毫无用处。技术/简洁程度评分为 7 分，就能让模型准确把握声音的定位。禁用词列表的作用更加强大；定义你“不是什么”比定义你“是什么”要容易得多。智能体会将每一份草稿与反模式列表进行比对，并重写任何触发列表的内容。最终生成的内容听起来像我本人，因为这些限制条件防止了它听起来像人工智能生成的。

Every content template includes voice checkpoints every 500 words: "Am I leading with insight? Am I being specific with numbers? Would I actually post this?" The blog template has a 4-pass editing process built in: structure edit (does the hook grab?), voice edit (banned words scan, sentence rhythm check), evidence edit (claims sourced?), and a read-aloud test. The quality gates are part of the skill, not something I add after the fact.

每个内容模板都包含每500字的语音检查点：“我的开头是否切中要害？我的数据是否具体？我真的会发布这篇文章吗？”博客模板内置了四道编辑工序：结构编辑（开头是否引人入胜？）、语音编辑（检查禁用词汇、句子节奏）、证据编辑（论点是否有来源？）以及朗读测试。这些质量把关是写作技巧的一部分，而不是事后添加的。

[

![](https://pbs.twimg.com/profile_images/2017468785473548288/43nF1d1X_x96.jpg)

](/koylanai)

Muratcan Koylan

![](https://pbs.twimg.com/profile_images/1984530242783039488/x9LWpM4z_bigger.jpg)

@koylanai

·

[Oct 6, 2025](/koylanai/status/1975090268316827983)

How I built an AI agent system that automatically maintains my digital brain based on the content I engage with? My personal context engineering architecture with Claude Sonnet 4.5, Groq Compound, Browser Use, all in Cursor ![👇](https://abs-0.twimg.com/emoji/v2/svg/1f447.svg)

我是如何构建一个人工智能代理系统，根据我接触的内容自动维护我的数字大脑的？ 我的个人上下文工程架构，使用 Claude Sonnet 4.5、Groq Compound、浏览器使用，全部在 Cursor ![👇](https://abs-0.twimg.com/emoji/v2/svg/1f447.svg) 中

![](https://pbs.twimg.com/amplify_video_thumb/1975080002589691904/img/PKiTlWQ7nUuStWAD.jpg)

8

11

134

[

76K


](/koylanai/status/1975090268316827983/analytics)

Templates as Structured Scaffolds: Five content templates define the structure for different content types. The long-form blog template has seven sections (Hook, Core Concept, Framework, Practical Application, Failure Modes, Getting Started, Closing) with word count targets per section totaling 2,000-3,500 words. The thread template defines an 11-post structure with a hook, deep-dive, results, and CTA. The research template has four phases: landscape mapping, technical deep-dive, evidence collection, and gap analysis.

模板作为结构化框架： 五个内容模板定义了不同内容类型的结构。长篇博客模板包含七个部分（引子、核心概念、框架、实际应用、故障模式、入门指南、结尾），每个部分的字数目标为 2,000-3,500 字。系列文章模板定义了一个包含 11 篇文章的结构，每个文章都包含引子、深度分析、结果和行动号召。研究模板包含四个阶段：现状分析、技术深度分析、证据收集和差距分析。

Templates not only constrain creativity but also constrain chaos. Without structure, the agent produces amorphous blobs of text. With structure, it produces content that has rhythm, progression, and payoff. Each template also includes a quality checklist so the agent can self-evaluate before presenting the draft.

模板不仅能限制创造力，还能抑制混乱。没有结构，创作者只能写出杂乱无章的文字；有了结构，就能创作出节奏分明、条理清晰、引人入胜的内容。每个模板还包含一份质量检查清单，方便创作者在提交草稿前进行自我评估 。

The research template outputs to \`knowledge/research/\[topic\].md\` with a structured format: Executive Summary, Landscape Map, Core Concepts, Evidence Bank (with statistics, quotes, case studies, and papers each cited with source and date), Failure Modes, Content Opportunities, and a Sources List graded HIGH/MEDIUM/LOW on reliability. That research document then feeds into the blog template's outline stage. The output of one skill becomes the input of the next. The pipeline builds on itself.

研究模板以结构化格式输出到 \`knowledge/research/\[topic\].md\` 文件，内容包括：执行摘要、概览图、核心概念、证据库（包含统计数据、引文、案例研究和论文，每项均注明来源和日期）、失效模式、内容机会以及可靠性评级为高/中/低的参考文献列表。该研究文档随后会导入博客模板的大纲阶段。一项技能的输出成为下一项技能的输入。整个流程环环相扣。

## 

4) THE OPERATING SYSTEM: HOW I ACTUALLY USE THIS DAILY

4）操作系统：我日常是如何实际使用它的

Architecture is nothing without execution. Here's how the system runs in practice.

没有执行，建筑设计就毫无意义。 以下是该系统在实际运行中的运作方式。

The Content Pipeline: Seven stages: Idea, Research, Outline, Draft, Edit, Publish, Promote.

内容制作流程： 七个阶段：构思、研究、大纲、草稿、编辑、发布、推广。

- Ideas are captured to \`ideas.jsonl\` with a scoring system, each idea rated 1-5 on alignment with positioning, unique insight, audience need, timeliness, and effort-versus-impact. Proceed if total score hits 15 or higher.
 
 所有想法都会被记录到 \`ideas.jsonl\` 文件中，并采用评分系统进行评估。每个想法都会根据其与定位的契合度、独特见解、受众需求、时效性以及投入产出比进行 1-5 分的评分。总分达到 15 分或以上即可继续推进。
 
- Research outputs to the knowledge module.
 
 研究成果提交至知识模块。
 
- Drafts go through four editing passes.
 
 草稿要经过四轮修改。
 
- Published content gets logged to \`posts.jsonl\` with platform, URL, and engagement metrics.
 
 发布的内容会记录到 \`posts.jsonl\` 文件中，包括平台、URL 和互动指标。
 
- Promotion uses the thread template to create an X announcement and a LinkedIn adaptation.
 
 推广活动使用主题模板创建 X 公告和 LinkedIn 版本。
 

[

![Image](https://pbs.twimg.com/media/HBswXU_WsAAsCfg?format=jpg&name=medium)


](/koylanai/article/2025286163641118915/media/2025265634762731520)

I batch content creation on Sundays: 3-4 hours, target output of 3-4 posts drafted and outlined. The content calendar maps each day to a platform and content type.

我会在周日集中进行内容创作：3-4小时，目标是完成3-4篇博文的草稿和大纲。内容日历会将每天的内容对应到一个平台和一种内容类型。

The Personal CRM: Contacts organized into four circles with different maintenance cadences: inner (weekly), active (bi-weekly), network (monthly), dormant (quarterly reactivation). Each contact record has \`can\_help\_with\` and \`you\_can\_help\_with\` fields that enable the introduction matching system. cross-referencing these fields surfaces mutually valuable intros. Interactions are logged with sentiment tracking (positive, neutral, needs\_attention) so relationship health is visible at a glance.

个人客户关系管理系统： 联系人分为四个层级，维护频率各不相同：核心联系人（每周）、活跃联系人（每两周）、人脉圈联系人（每月）和休眠联系人（每季度重新激活）。每个联系人记录都包含 \`can\_help\_with\` 和 \`you\_can\_help\_with\` 字段，用于实现介绍匹配系统。通过交叉引用这些字段，系统会发现对双方都有价值的人脉资源。互动记录会进行情感追踪（正面、中性、需要关注），因此关系健康状况一目了然。

[

![Image](https://pbs.twimg.com/media/HBsyXzAWwAAW89B?format=jpg&name=medium)


](/koylanai/article/2025286163641118915/media/2025267841843249152)

Most people keep contacts in their head and let relationships decay through neglect. The \`stale\_contacts\` script cross-references contacts (who they are), interactions (when we last talked), and circles (how often we should talk) to surface outreach needs. A 30-second scan each week shows me which relationships need attention.

大多数人只是把联系人信息记在脑子里，任由关系因疏于维护而逐渐淡漠。\`stale\_contacts\` 脚本会交叉比对联系人（他们是谁）、互动记录（上次联系的时间）和社交圈（多久联系一次），从而发现哪些关系需要维系。每周只需 30 秒，我就能知道哪些关系需要关注。

Specialized groups in \`circles.yaml\`founders, investors, ai\_builders, creators, mentors, mentees, each have explicit relationship development strategies. For AI builders: share useful content, collaborate on open source, provide tool feedback, amplify their work. For mentors: bring specific questions, update on progress from previous advice, look for ways to add value back. These are operational instructions the agent follows when I ask "Who should I reach out to this week?"

\`circles.yaml\` 中的专业群体包括创始人、投资者、人工智能开发者、创作者、导师和学员，每个群体都有明确的关系发展策略。对于人工智能开发者：分享有用的内容、合作开发开源项目、提供工具反馈、推广他们的工作。对于导师：提出具体问题、汇报之前指导的进展情况、寻找回馈价值的方式。这些是当我询问“本周我应该联系谁？”时，系统会遵循的操作指南。

Automation Chains: Five scripts handle recurring workflows. They chain together for compound operations. The Sunday weekly review runs three scripts in sequence: \`metrics\_snapshot.py\` updates the numbers, \`stale\_contacts.py\` flags relationships, \`weekly\_review.py\` generates a summary document with completed-versus-planned, metrics trends, and next week's priorities. The content ideation chain reads recent bookmarks, checks undeveloped ideas, generates fresh suggestions, and cross-references with the content calendar to find scheduling gaps. These aren't cron jobs -- the agent runs them when I ask for a review, or I trigger them with \`npm run weekly-review\`.

自动化链： 五个脚本处理重复性工作流程。它们串联起来执行复合操作。每周日的周回顾会按顺序运行三个脚本：\`metrics\_snapshot.py\` 更新数据，\`stale\_contacts.py\` 标记关系，\`weekly\_review.py\` 生成一份包含已完成与计划对比、指标趋势以及下周优先级的总结文档。内容创意链会读取最近的书签，检查未开发的想法，生成新的建议，并与内容日历交叉引用以查找日程安排上的空档。这些不是定时任务——代理会在我请求回顾时运行它们，或者我可以使用 \`npm run weekly-review\` 命令触发它们。

[

![](https://pbs.twimg.com/profile_images/2017468785473548288/43nF1d1X_x96.jpg)

](/koylanai)

Muratcan Koylan

![](https://pbs.twimg.com/profile_images/1984530242783039488/x9LWpM4z_bigger.jpg)

@koylanai

·

[Feb 4](/koylanai/status/2018865011356053927)

This is how I consume X and LinkedIn. Cursor is my cockpit. MCPs connect everything: Zapier for actions, alphaXiv for papers, Browser Use for scraping posts, ElevenLabs for audio. All managed through custom Skills in my Digital Brain OS repo. Just saw an Anthropic announcement.

这就是我使用 X 和 LinkedIn 的方式。 Cursor 是我的驾驶舱。MCP 连接一切：Zapier 用于操作，alphaXiv 用于论文，浏览器用于抓取帖子，ElevenLabs 用于音频。所有这些都通过我 Digital Brain OS 代码库中的自定义技能进行管理。 刚刚看到人类学的公告。

Show more

![](https://pbs.twimg.com/amplify_video_thumb/2018862272915939328/img/c9nJe9_-WEOiECxp.jpg)

14

13

113

[

10K


](/koylanai/status/2018865011356053927/analytics)

Scripts that output to stdout in agent-readable format close the loop between data and action. The weekly review script doesn't just tell me what happened -- it references my goals and identifies which key results are on track, which are behind, and what to prioritize next week. The scripts read from the same files the agent reads during normal operation, so there's no data duplication or synchronization problem.

以代理可读格式输出到标准输出的脚本实现了数据与行动之间的闭环。每周回顾脚本不仅告诉我发生了什么，还会参考我的目标，指出哪些关键结果进展顺利，哪些落后，以及下周的优先事项。这些脚本读取的文件与代理在正常运行期间读取的文件相同，因此不存在数据重复或同步问题。

[

![Image](https://pbs.twimg.com/media/HBswupNXYAAJwVy?format=jpg&name=medium)


](/koylanai/article/2025286163641118915/media/2025266035327197184)

After running the weekly review, the agent has everything it needs to update \`

[todos.md](//todos.md)

\` for next week, adjust \`goals.yaml\` progress numbers, and suggest content topics that align with underperforming key results. The review isn't a report -- it's the starting point for next week's planning. The automation creates a feedback loop: goals drive content, content drives metrics, metrics drive reviews, reviews drive goals.

完成每周审查后，代理程序就拥有了更新所需的一切信息。

[todos.md](//todos.md)

下周，调整 \`goals.yaml\` 文件中的进度指标，并针对表现欠佳的关键指标提出相应的内容主题建议。此次评估并非报告，而是下周计划的起点。自动化流程构建了一个反馈循环：目标驱动内容，内容驱动指标，指标驱动评估，评估驱动目标。

## 

5) WHAT I GOT WRONG AND WHAT I'D DO DIFFERENTLY

5）我的错误之处以及我会如何改进

- I over-engineered the schema first pass. My initial JSONL schemas had 15+ fields per entry. Most were empty. Agents struggle with sparse data -- they try to fill in fields or comment on the absence. I cut schemas to 8-10 essential fields and added optional fields only when I actually had data for them. Simpler schemas, better agent behavior.
 
 我第一次设计模式时设计得过于复杂。 最初的 JSONL 模式每个条目有 15 个以上的字段，其中大部分都是空的。代理程序处理稀疏数据很吃力——它们会尝试填充字段或对缺失的字段进行注释。我把模式精简到 8-10 个必要字段，只有在有实际数据时才添加可选字段。更简洁的模式，代理程序的行为也更好。
 
- The voice guide was too long at first. Version one of \`
 
 [tone-of-voice.md](//tone-of-voice.md)
 
 \` was 1,200 lines. The agent would start strong, then drift by paragraph four as the voice instructions fell into the lost-in-middle zone. I restructured it to front-load the most distinctive patterns (signature phrases, banned words, opening patterns) in the first 100 lines, with extended examples further down. The critical rules need to be at the top, not the middle.
 
 语音提示一开始太长了。 第一版
 
 [语气.md](//tone-of-voice.md)
 
 原文有 1200 行。代理人的开头气势如虹，但到了第四段，语音指令就显得冗长乏味，中间部分也显得模糊不清。我重新调整了结构，将最鲜明的模式（标志性短语、禁用词、开场白）放在前 100 行，并在后面提供更详细的示例。关键规则应该放在开头，而不是中间。
 
- Module boundaries matter more than you think. I initially had identity and brand in one module. The agent would load my entire bio when it only needed my banned words list. Splitting them into two modules cut token usage for voice-only tasks by 40%. Every module boundary is a loading decision. Get them wrong and you load too much or too little.
 
 模块边界比你想象的更重要。 我最初把身份和品牌放在一个模块里。结果，系统加载了我的整个个人简介，而实际上只需要我的禁用词列表。把它们拆分成两个模块后，语音任务的令牌使用量减少了 40%。每个模块边界都代表着一个加载决策。设置错误会导致加载过多或过少。
 
- Append-only is non-negotiable. I lost three months of post engagement data early on because an agent rewrote \`posts.jsonl\` instead of appending to it. JSONL's append-only pattern isn't just a convention -- it's a safety mechanism. The agent can add data. It cannot destroy data. This is the most important architectural decision in the system.
 
 仅追加模式是不可妥协的。 我早期丢失了三个月的帖子互动数据，因为一个代理程序重写了 \`posts.jsonl\` 文件，而不是追加数据。JSONL 的仅追加模式不仅仅是一种约定，更是一种安全机制。代理程序可以添加数据，但不能删除数据。这是系统中最重要的架构决策。
 

## 

6) THE RESULTS AND THE PRINCIPLE BEHIND THEM

6）结果及其背后的原理

The real result is simpler than any metric. I open Cursor or Claude Code, start a conversation, and the AI already knows who I am, how I write, what I'm working on, and what I care about. It writes in my voice because my voice is encoded as structured data. It follows my priorities because my goals are in a YAML file it reads before suggesting what to work on. It manages my relationships because my contacts and interactions are in files it can query.

实际结果比任何指标都简单。我打开 Cursor 或 Claude Code，开始对话，人工智能就已经知道我是谁、我的写作风格、我正在做什么以及我关心什么。它能用我的声音写作，因为我的声音被编码成了结构化数据。它能遵循我的优先级，因为我的目标记录在一个 YAML 文件中，它会在提出工作建议前读取该文件。它能管理我的人际关系，因为我的联系人和互动记录在它可以查询的文件中。

The principle behind all of it: this is context engineering, not prompt engineering. Prompt engineering asks "how do I phrase this question better?" Context engineering asks "what information does this AI need to make the right decision, and how do I structure that information so the model actually uses it?"

这一切背后的原则是：这是情境工程，而不是提示工程。提示工程问的是“我该如何更好地表述这个问题？”而情境工程问的是“人工智能需要哪些信息才能做出正确的决策，以及我该如何组织这些信息才能让模型真正利用它们？”

The shift is from optimizing individual interactions to designing information architecture. It's the difference between writing a good email and building a good filing system. One helps you once. The other helps you every time.

这种转变是从优化个体交互转向设计信息架构。这就好比写一封好邮件和构建一个好的文件系统之间的区别。前者只能帮到你一次，后者则每次都能帮到你。

[

![](https://pbs.twimg.com/profile_images/2017468785473548288/43nF1d1X_x96.jpg)

](/koylanai)

Muratcan Koylan

![](https://pbs.twimg.com/profile_images/1984530242783039488/x9LWpM4z_bigger.jpg)

@koylanai

·

[Nov 9, 2025](/koylanai/status/1987254288393916571)

Kimi K2 is a great writer, but it's hard to explain your taste to LLMs. So, I built an AI interviewer that extracts your literary DNA. 12-question interview → structured profile → reusable prompt. Open sourcing shortly.

Kimi K2 是一位很棒的作家，但是很难向法学硕士解释你的品味。 于是，我开发了一款人工智能面试官，它可以提取你的文学基因。 12 道题面试 → 结构化个人资料 → 可重复使用的提示。 即将开源。

[

![Image](https://pbs.twimg.com/media/G5QkwRlWIAAnUmD?format=png&name=medium)


](/koylanai/status/1987254288393916571/photo/1)

45

75

1.1K

[

75K


](/koylanai/status/1987254288393916571/analytics)

The entire system fits in a Git repository. Clone it to any machine, point any AI tool at it, and the operating system is running. Zero dependencies. Full portability. And because it's Git, every change is versioned, every decision is traceable, and nothing is ever truly lost.

整个系统都装在一个 Git 代码库里。把它克隆到任何机器上，用任何 AI 工具连接，操作系统就能运行。零依赖，完全可移植。而且因为是 Git，每次更改都有版本控制，每个决策都可追溯，数据永远不会真正丢失。

Muratcan Koylan is Context Engineer at

[Sully.ai](//Sully.ai)

, where he designs context engineering systems for healthcare AI. His on-source work on context engineering (8,000+ GitHub stars) is cited in academic research alongside Anthropic. Previously AI Agent Systems Manager at 99Ravens AI, building multi-agent systems handling 10,000+ weekly interactions.

Muratcan Koylan 是 Context Engineer

[Sully.ai](//Sully.ai)

他目前从事医疗保健人工智能的上下文工程系统设计工作。他在上下文工程方面的源代码（GitHub 上获得 8000 多个 star）与 Anthropic 一起被学术研究引用。此前，他曾担任 99Ravens AI 的人工智能代理系统经理，负责构建每周处理超过 10000 次交互的多代理系统。

Framework: \[Agent Skills for Context Engineering\](

[https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering)

)

框架：\[用于上下文工程的代理技能\](

[https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering)

）

[

![](https://pbs.twimg.com/profile_images/2017468785473548288/43nF1d1X_x96.jpg)

](/koylanai)

Muratcan Koylan

![](https://pbs.twimg.com/profile_images/1984530242783039488/x9LWpM4z_bigger.jpg)

@koylanai

·

[](/koylanai/status/2002797649842331919)