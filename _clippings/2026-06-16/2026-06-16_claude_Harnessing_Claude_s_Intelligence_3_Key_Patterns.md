---
title: "2026-06-16_claude_com_Harnessing_Claude_s_Intelligence_3_Key_Patterns_fo"
source: "https://claude.com/blog/harnessing-claudes-intelligence"
author:
  - "[[@claude.com]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "#additional"
  - "claude"
  - "@claude.com"
  - "https"
---

# Harnessing Claude's Intelligence | 3 Key Patterns for Building Apps | Claude

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d225588ad176f7c4aafd_abc884c723daea810d2e986455358281a2f94102-1000x1000.svg)

- Date
 
 April 2, 2026
 
- Reading time
 
 5
 
 min
 
- Share
 
 [Copy link](#)
 
 https://claude.com/blog/harnessing-claudes-intelligence
 

Anthropic 的联合创始人之一 Chris Olah [表示](https://www.darioamodei.com/post/the-urgency-of-interpretability) ，像 Claude 这样的生成式 AI 系统与其说是被构建，不如说是被培育成长。研究人员设定条件以引导其发展，但由此产生的确切结构或能力并不总是可预测的。

This creates a challenge for building with Claude: [代理利用编码假设](https://www.anthropic.com/engineering/harness-design-long-running-apps) about what Claude can’t do on its own, but those assumptions grow stale as Claude gets more capable. Even lessons shared in articles like this deserve frequent revisiting.

在本文中，我们分享了团队在构建应用程序时应采用的三种模式，这些应用程序需要跟上 Claude 不断发展的智能，同时平衡延迟和成本：使用它已知的内容、询问你可以停止做什么，以及谨慎地与代理工具设定边界。

### 1\. Use what Claude knows

我们建议使用 Claude 熟悉的工具来构建应用程序。

2024 年底，Claude 3.5 Sonnet 在 SWE-bench Verified 上达到了 49%的分数——随后达到了 [最先进水平](https://www.anthropic.com/engineering/swe-bench-sonnet) ——仅使用了一个 [bash 工具](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool) 和一个 [文本编辑器工具](https://platform.claude.com/docs/en/agents-and-tools/tool-use/text-editor-tool) 来查看、创建和编辑文件。Claude Code 基于这些相同的工具。 [Bash](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool) 并非为构建智能体而设计，但它是 Claude *知道* 如何使用的工具，并且随着时间的推移使用得越来越好。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69cd8747994e07042a959518_image2.png)

SWE-bench Verified 基准上的分数在 Claude 各模型版本中凸显了其演进。

我们看到 Claude 将这些通用工具组合成可解决不同问题的模式。例如， [Agent 技能](https://agentskills.io/home) 、 [程序化工具调用](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling) 和 [记忆工具](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool) 都是由 bash 和文本编辑器工具构建而成的。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69cd8835161641fba4aa1def_image4.png)

程序化工具调用、技能和记忆是我们的 bash 和文本编辑器工具的组成部分。

### 2\. 问“我可以停止做什么？”

[Agent 利用编码假设](https://www.anthropic.com/engineering/harness-design-long-running-apps) about what Claude can’t do on its own. As Claude gets more capable, those assumptions should be tested.

**让 Claude 编排自身的行动**

一个常见的假设是，每个工具结果都应该通过 Claude 的 [上下文窗口](https://platform.claude.com/docs/en/build-with-claude/context-windows) 回流，以指导后续操作。按 token 处理工具结果可能会很慢、成本很高且没有必要，如果工具结果只需要传递给下一个工具，或者 Claude 只关心输出的一小部分。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69cd889c76e6e17dbe4ff4b9_image7.png)

Claude 调用工具，这些工具在一个环境中执行。

考虑读取一个大型表格来分析单个列：整个表格都会进入上下文，而 Claude 需要为每一行它不需要的内容支付 token 成本。在工具设计中，可以使用 [硬编码过滤器](https://platform.claude.com/docs/en/about-claude/models/migration-guide#additional-recommended-changes) 来解决这个问题。但这并没有解决一个事实，即 agent 框架正在做出一个 *编排决策* ，而 Claude 更适合做出这个决策。

给 Claude 提供一个 [代码执行](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool) 工具（例如 [bash 工具](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool) 或 [特定语言的 REPL](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool) ）可以解决这个问题：它允许 Claude 编写代码来表达工具调用以及它们之间的逻辑。与由框架决定每个工具调用结果都作为 token 处理不同，Claude 会决定哪些结果要传递、过滤或管道到下一次调用，而不触碰上下文窗口。只有代码执行的输出才会进入 Claude 的上下文窗口。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69cd891f5b4d2dea57b008d1_image6.png)

Claude 能够编写表达工具调用及其之间逻辑的代码。

编排决策从框架转移到模型。由于代码是 Claude 编排操作的通用方式，强大的编码模型也是强大的 *通用* 代理。Claude 采用这种模式在 [非编码评估](https://claude.com/blog/improved-web-search-with-dynamic-filtering) 中表现出色：在 BrowseComp（一个测试代理网页浏览能力的 [基准测试](https://arxiv.org/abs/2504.12516) ）上，Opus 4.6 能够过滤自身工具输出，准确率从 45.3%提升至 61.6%。

**让 Claude 管理它自己的上下文**

任务特定的上下文引导 Claude 使用 bash 和文本编辑器工具等通用工具。一个常见的假设是， [系统提示](https://platform.claude.com/docs/en/release-notes/system-prompts) 应该通过任务特定的指令手工编写。问题在于，预先在提示中加载指令无法在多个任务中扩展：每添加一个 token 都会消耗 [Claude 的注意力预算](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) ，并且预先在上下文中加载很少使用的指令是一种浪费。

赋予 Claude 访问 [技能](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) 的能力可以解决这一问题：每个技能的 YAML frontmatter 是预先加载到上下文窗口的简短描述，提供技能内容的概述。如果任务需要，Claude 可以通过调用读取文件工具逐步披露完整技能内容。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69cd895f7f04456cccf7b7e0_image3.png)

Claude 能够运用技能逐步揭示与任务相关的上下文。

尽管能力让 Claude 能够自由构建自己的上下文窗口， [上下文编辑](https://platform.claude.com/docs/en/build-with-claude/context-editing) 则与之相反，提供了一种选择性地移除变得陈旧或无关的上下文的方法，例如旧的工具结果或思维障碍。

借助 [子代理](https://code.claude.com/docs/en/sub-agents) ，Claude 在判断何时分叉到新的上下文窗口以隔离特定任务的工作方面表现得越来越好。 [借助 Opus 4.6](https://www-cdn.anthropic.com/0dd865075ad3132672ee0ab40b05a53f14cf5288.pdf) ，生成子代理的能力在 BrowseComp 上的表现相比最佳的单一代理运行提升了 2.8%。

**让 Claude 保持它自己的上下文**

长期运行的代理可能会超出单个 [上下文窗口](https://platform.claude.com/docs/en/build-with-claude/context-windows) 的限制。普遍假设是，记忆系统应依赖模型周围的检索基础设施。我们的大部分工作都专注于为 Claude 提供简单的方式，使其能够 *自主选择* 需要持久化的内容。

[上下文压缩](https://platform.claude.com/docs/en/build-with-claude/compaction) 让 Claude 能够总结其过去的上下文，以在长期任务中保持连续性。经过几个版本的迭代，Claude 在选择需要记住的内容方面变得更好了。 [在 BrowseComp 上](https://www-cdn.anthropic.com/14e4fb01875d2a69f646fa5e574dea2b1c0ff7b5.pdf) ，例如，作为一种智能体搜索任务，Sonnet 4.5 在无论我们给予的压缩预算是多少的情况下，都保持在 43%不变。然而，Opus 4.5 提升至 68%，而 Opus 4.6 在相同的设置下达到了 84%。

一个 [记忆文件夹](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool) 是另一种方法，允许 Claude 将上下文写入文件，并在需要时读取这些文件。我们已经看到 Claude 将此用于代理式搜索。在 BrowseComp-Plus 上，为 Sonnet 4.5 提供一个记忆文件夹 [将准确率从 60.4%提升至 67.2%](https://www-cdn.anthropic.com/bf10f64990cfda0ba858290be7b8cc6317685f47.pdf) 。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69cd89bfccdc7c50beb40e0d_image5.png)

Claude 可以将上下文持久化到记忆文件夹。

[长视野游戏](https://www.youtube.com/watch?v=CXhYDOvgpuU) ，例如宝可梦，就是 Claude 改进的记忆文件夹使用能力的体现。Sonnet 3.5 将记忆视为记录，仅记录非玩家角色（NPC）的对话内容，而非重要信息。在经历 14,000 步后，它生成了 31 个文件——其中包括两个关于毛毛虫宝可梦的近乎重复的文件——并且仍停留在第二个城镇：

```json
caterpie_weedle_info:
- Caterpie and Weedle are both caterpillar Pokémon.
- Caterpie is a caterpillar Pokémon that does not have poison.
- Weedle is a caterpillar Pokémon that does have poison.
- This information is crucial for future encounters and battles.
- If our Pokémon get poisoned, we should seek healing at a Pokémon
  Center as soon as possible.
```

后续模型撰写了战术笔记。Opus 4.6 在相同的步数下，包含 10 个按目录组织的文件、三个健身徽章，以及一个从自身失败中提炼出的经验文件：

```json
/gameplay/learnings.md:
- Bellsprout Sleep+Wrap combo: KO FAST with BITE before Sleep
  Powder lands. Don't let it set up!
- Gen 1 Bag Limit: 20 items max. Toss unneeded TMs before dungeons.
- Spin tile mazes: Different entry y-positions lead to DIFFERENT
  destinations. Try ALL entries and chain through multiple pockets.
- B1F y=16 wall CONFIRMED SOLID at ALL x=9-28 (step 14557)
```

### 3\. Set boundaries carefully

代理工具为 Claude 提供结构，以确保用户体验(UX)、成本或安全性。

**设计上下文以最大化缓存命中**

The [Messages API](https://platform.claude.com/docs/en/build-with-claude/working-with-messages) is 无状态的。Claude 无法查看之前轮次的对话历史。这意味着，代理框架需要在每一轮次中，将新的上下文连同所有过去的操作、工具描述和指令一起打包给 Claude。

提示词可以基于设置的 [断点](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) 进行缓存。换句话说，Claude API 将上下文写入到断点处的缓存中，并检查该上下文是否与任何先前的缓存条目匹配。

由于缓存 token [仅为基础输入 token 成本的 10%](https://platform.claude.com/docs/en/about-claude/pricing) ，以下是一些在 agent harness 中帮助最大化缓存命中的原则：

| Principle | Description |
| --- | --- |
| Static first, dynamic last | 安排请求，使稳定内容（系统提示、工具）优先。 |
| Messages for updates | 在消息中添加一个 `<system-reminder>` 而不是编辑提示词。 |
| Don't change models | 避免在会话期间切换模型。缓存是模型特定的；切换模型会破坏缓存。如果需要更便宜的模型，可以使用子代理。 |
| Carefully manage tools | 工具位于缓存前缀中。添加或移除一个工具会使缓存前缀失效。为了进行动态发现，请使用 **工具搜索** ，该方法在添加内容时不会破坏缓存。 |
| Update breakpoints | 对于多轮应用（例如：代理），将断点移动到最新消息以保持缓存最新。使用 **自动缓存** 来实现这一点。 |

**将声明式工具用于用户体验、可观测性或安全边界**

Claude 不一定了解应用程序的安全边界或用户体验界面。Claude 发出工具调用，这些调用由工具管理框架处理。bash 工具为 Claude 提供了执行操作的广泛编程能力，但它只向工具管理框架提供一个命令字符串——每个操作的结构都相同。将操作提升到专用工具，可为工具管理框架提供一个特定于操作的钩子，该钩子带有类型化参数，工具管理框架可以对其进行拦截、控制、渲染或审计。

需要安全边界的操作自然是专用工具的候选对象。可撤销性通常是一个很好的标准，而像外部 API 调用这类难以撤销的操作则可以通过用户确认来进行控制。开发像 `edit` 这样的工具时，可以包含一个陈旧性检查，以确保 Claude 不会覆盖自上次读取以来已更改的文件。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69cd8ebecb4a73207c8b2ffc_image1.png)

专用工具可用于基于安全、UX 或可观测性考虑的操作。

当需要向用户展示某个操作时，工具也很有用。例如，它们可以被渲染为模态框，以向用户清晰展示一个问题、给用户提供多个选项，或者阻塞代理循环直到用户提供反馈。

最后，工具对可观测性很有用。当操作是类型化工具时，测试框架会获取可结构化的参数，以便进行记录、跟踪和重放。

决定将操作推广到工具中，这一决策应持续重新评估。例如，Claude Code 的 [auto-mode](https://www.anthropic.com/engineering/claude-code-auto-mode) （发布时处于研究模式）为 bash 工具提供了安全边界：它让第二个 Claude 读取命令字符串并判断是否安全。这种模式可以 *限制* 对专用工具的需求，并且仅应在用户信任整体方向的任务中使用。专用工具对于某些高风险操作仍然可以获得其地位。

### Looking forward

Claude 的智能前沿一直在变化。对于 Claude 不能做什么的假设，需要随着其能力的每一步变化重新测试。

我们看到这种模式反复出现。在 [我们为长期任务构建的代理](https://www.anthropic.com/engineering/harness-design-long-running-apps) 中，Sonnet 4.5 会在感觉到上下文限制即将到来时过早完成。我们添加了重置功能以清除上下文窗口，以解决这种“上下文焦虑”。使用 Opus 4.5 后，这种行为消失了。我们构建的用于补偿的上下文重置功能在代理框架中变得多余。

移除这些冗余部分很重要 [因为它会成为瓶颈](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) Claude 的性能。随着时间的推移，我们应用程序中的结构或边界应该根据问题 *我可以停止做什么？ 进行优化。*

*要使用此处讨论的所有工具和模式，* [*我们的 claude-api 技能*](https://github.com/anthropics/skills/tree/main/skills/claude-api) *。*

### Acknowledgements

由克劳德平台团队的技术人员兰斯·马丁（Lance Martin）撰写。特别感谢 Thariq Shihipar、Barry Zhang、Mike Lambert、David Hershey 和李达亮（Daliang Li）就所涉及的主题提供的有益讨论。感谢 Lydia Hallie、Lexi Ross、Katelyn Lesse、Andy Schumeister、Rebecca Hiscott、Jake Eaton、Pedram Navid 和 Molly Vorwerck 提供的编辑审阅和反馈。

产品更新、使用指南、社区亮点以及更多内容。每月发送到您的收件箱。