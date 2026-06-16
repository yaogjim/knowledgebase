---
title: "2026-06-16_unknown_代码智能体操作系统三层设计"
source: "omnisun://digest/1773993083081"
author:
  - "[[@RLanceMartin]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "#prompt"
  - "#1"
  - "@RLanceMartin"
  - "claude"
---

# 代码智能体操作系统三层设计

# 构建 Claude Code 的经验：提示词缓存就是一切

https://x.com/trq212/status/2024574133011673516

**Thariq**

# 构建 Claude Code 的经验：提示词缓存就是一切

工程领域中常有人说“缓存主宰我周围的一切”，同样的规则也适用于代理。

长期运行的智能代理产品（如 Claude Code）的实现得益于提示词缓存，这使得我们能够重用之前往返中的计算，并显著降低延迟和成本。

什么是提示词缓存，它是如何工作的，以及技术上如何实现？

[阅读更多@RLanceMartin 关于提示词缓存以及我们新的自动缓存功能发布的文章](https://x.com/RLanceMartin/status/2024573404888911886)

在 Claude Code，我们围绕提示词缓存构建整个系统。高提示词缓存命中率可降低成本，并帮助我们为订阅计划设置更宽松的速率限制，因此我们会监控提示词缓存命中率，若其过低则宣布 SEV。

这些是（往往不直观的）我们在大规模优化提示词缓存过程中获得的经验教训。

## 设置用于缓存的提示

![Image](https://pbs.twimg.com/media/HBipHa1boAAXD_A?format=jpg&name=large)

提示缓存通过前缀匹配实现——API 会缓存从请求开始到每个 cache\_control 断点为止的所有内容。这意味着你放置内容的顺序极为重要，你希望尽可能多的请求共享一个前缀。

完成此操作的最佳方式是先处理静态内容，最后处理动态内容。对于 Claude Code，这表现为：

1.  静态系统提示词 & 工具（全局缓存）
2.  Claude.MD（在项目中缓存）
3.  会话上下文 （在会话中缓存）
4.  对话消息

这样我们最大化了共享缓存命中的会话数量。

但这可能会出人意料地脆弱！我们之前破坏这种顺序的原因包括：在静态系统提示中放入详细的时间戳、非确定性地打乱工具顺序定义、更新工具的参数（例如 AgentTool 可以调用的代理）等。

## 使用消息接收更新

有时，你输入提示中的信息可能会过时，例如当你有时间或者用户修改了文件时。更新提示可能会很诱人，但这会导致缓存未命中，并且可能最终对用户来说成本很高。

考虑一下下次是否可以通过消息传递这些信息。在 Claude Code 中，我们会在下一次用户消息或工具结果中添加 <system-reminder> 标签，包含模型的更新信息（例如现在是星期三），这有助于保留缓存。

## 不要在会话中途更改模型

提示缓存是模型独有的，这可能会使提示缓存的计算相当难以理解。

如果你已经与 Opus 进行了 10 万个 token 的对话，并且想要提出一个比较容易回答的问题，实际上切换到 Haiku 会比让 Opus 回答更昂贵，因为我们需要为 Haiku 重建提示词缓存。

如果需要切换模型，最好的方法是使用子代理，其中 Opus 会准备一条“交接”消息给另一个需要执行该任务的模型。我们经常在使用 Haiku 的 Claude Code 中的探索代理中这样做。

## 切勿在会话期间添加或移除工具

在对话过程中更改工具集是人们破坏提示词缓存的最常见方式之一。这似乎很直观——你应该只给模型你认为它现在需要的工具。但由于工具是缓存前缀的一部分，添加或移除工具会使整个对话的缓存失效。

规划模式 — 围绕缓存设计

计划模式是围绕缓存限制设计功能的一个很好的例子。直观的方法应该是：当用户进入计划模式时，替换掉工具集，只保留只读工具。但这会破坏缓存。

相反，我们始终保留所有工具在请求中，并将 EnterPlanMode 和 ExitPlanMode 本身用作工具。当用户开启计划模式时，代理会收到一条系统消息，说明它处于计划模式以及指令内容——探索代码库，不要编辑文件，计划完成后调用 ExitPlanMode。工具定义永远不会改变。

这有一个额外的好处：因为 EnterPlanMode 是模型可以自我调用的工具，当它检测到难题时，能够自主进入规划模式，不会造成任何缓存中断。

工具搜索 — 推迟而非移除

同样的原则适用于我们的工具搜索功能。Claude Code 可以加载数十个 MCP 工具，在每个请求中包含所有这些工具的成本会很高。但在对话过程中移除它们会破坏缓存。

我们的解决方案：defer\_loading。而不是移除工具，我们发送轻量级存根——仅包含工具名称，并附带 defer\_loading: true——，模型可以通过 ToolSearch 工具在需要时"发现"这些存根。完整的工具架构仅在模型选择它们时才会被加载。

幸运的是，您可以使用

[tool search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool) 工具通过我们的 API 来简化这一过程。

## 分支上下文 — 压缩

![Image](https://pbs.twimg.com/media/HBitEdRbUAMVSnM?format=jpg&name=large)

压缩是当你耗尽上下文窗口时发生的情况。我们总结到目前为止的对话，并基于该总结继续一个新的会话。

令人惊讶的是，压缩在提示缓存方面存在许多边缘情况，这些情况可能不直观。

特别是，当我们进行压缩时，需要将整个对话发送给模型以生成摘要。如果这是一个带有不同系统提示且没有工具的单独 API 调用（即简单实现的情况），主对话中的缓存前缀会完全不匹配。你需要为所有这些输入 token 支付全额费用，这会大幅增加用户的成本。

解决方案 — 缓存安全分叉

当我们执行压缩时，我们使用的是完全相同的系统提示、用户上下文、系统上下文以及工具定义，与父对话完全相同。我们在开头添加父对话的消息，然后在末尾追加压缩提示作为新的用户消息。

从 API 的角度来看，这个请求看起来与父请求的上一次请求几乎相同——相同的前缀、相同的工具、相同的历史，因此重用了缓存的前缀。唯一的新标记是压缩提示本身。

不过这确实意味着我们需要预留一个“compaction buffer”，以便我们在上下文窗口中有足够的空间来包含紧凑消息和摘要输出 token。

压缩很棘手，但幸运的是，你不需要自己学习这些知识——基于我们从 Claude Code 获得的经验，我们构建了

[压缩](https://platform.claude.com/docs/en/build-with-claude/compaction#prompt-caching)直接集成到 API 中，以便你能在自己的应用中应用这些模式。

## 经验教训

1.  提示缓存是一种前缀匹配。前缀中的任何位置发生的更改都会使之后的所有内容失效。围绕这个约束设计整个系统。正确处理顺序，大部分缓存工作都会自动有效。
2.  使用消息而非修改系统提示。你可能会想要编辑系统提示来完成诸如进入计划模式、更改日期等操作，但实际上，在对话过程中将这些内容插入消息中会更好。
3.  不要在对话过程中更换工具或模型。 使用工具来建模状态转换（如计划模式），而不是更换工具集。延迟工具加载而非移除工具。
4.  监控你的缓存命中率，就像监控运行时间一样。 我们会对缓存中断发出警报，并将它们视为事件。几个百分点的缓存未命中率可能会显著影响成本和延迟。
5.  分叉操作需要共享父进程的前缀。 如果需要运行辅助计算（压缩、汇总、技能执行），请使用相同的缓存安全参数，以便在父进程的前缀上命中缓存。

Claude Code 从一开始就以提示词缓存为核心构建，如果你正在构建代理，你也应该这样做。

* * *

### 热门回复

**@Kati Holland** ♥ 24.4K · 💬 139

《Chlorine》MV 的幕后花絮，我在其中以美人鱼的形象完成从少女到女人的转变（！）

**@Mitch Harris** ♥ 86 · 💬 3

为什么缓存不是王道？

**@mert** ♥ 45 · 💬 16

Claude Code 经常忘记你在 Claude MD 中指定的内容，该如何解决？

**@Thariq** ♥ 27 · 💬 2

是的，当然！你可能只需要把 Claude 指向这篇文章 :)

**@Thariq** ♥ 15 · 💬 3

不，缓存应该直接就能用！

* * *

# 构建 Claude 代码的经验：像智能体一样观察

https://x.com/trq212/status/2027463795355095314

**Thariq**

# 构建 Claude 代码的经验：像智能体一样观察

构建 agent 框架最困难的部分之一是构造其动作空间。

Claude acts through Tool Calling, but there are a number of ways tools can be constructed in the Claude API with primitives like bash, skills and recently code execution (read more about programmatic tool calling on the Claude API in

[@RLanceMartin's new article](https://x.com/RLanceMartin/status/2027450018513490419)).

考虑到所有这些选项，你如何设计你的代理的工具？你只需要一个工具，比如代码执行或 Bash 吗？如果你有 50 个工具，每个工具对应代理可能遇到的一个用例，那会怎样？

为了设身处地想象自己是这个模型，我喜欢想象自己被给予一道数学难题。为了解决它，你会需要什么工具？这取决于你自己的技能！

最基础的选择是使用纸张，但你会受到手动计算的限制。计算器会更好，但你需要知道如何操作更高级的功能。最快且最强大的选择是使用计算机，但你必须知道如何用它来编写和执行代码。

这是一个设计智能体的有用框架。你希望给它一些根据自身能力定制的工具。但你如何知道这些能力是什么呢？你需要关注、查看它的输出并进行实验。你学会像智能体一样思考。

以下是我们在开发 Claude Code 时关注 Claude 所学到的一些经验教训。

# 改进信息提取与 AskUserQuestion 工具

![Image](https://pbs.twimg.com/media/HCLxg2JbsAA3Ag_?format=jpg&name=large)

开发 AskUserQuestion 工具时，我们的目标是提升 Claude 提问的能力（通常称为引导式提问）。

虽然 Claude 可以直接用纯文本提问，但我们发现回答这些问题似乎花费了过多不必要的时间。我们该如何降低这种沟通摩擦，提高用户与 Claude 之间的沟通带宽？

## 尝试 #1 - 编辑 ExitPlanTool

我们首先尝试的是在 ExitPlanTool 中添加一个参数，以便与计划一同包含一组问题数组。这是最容易实现的，但这让 Claude 感到困惑，因为我们同时请求了一个计划和一组关于该计划的问题。如果用户的回答与计划中所述的内容冲突怎么办？Claude 是否需要调用 ExitPlanTool 两次？我们需要另一种方法。

(you can read more about why we made an ExitPlanTool in

[our post on prompt caching](https://x.com/trq212/status/2024574133011673516))

## 尝试 #2 - 更改输出格式

接下来我们尝试修改 Claude 的输出指令，以提供一种略有修改的 Markdown 格式，使其能够用来提问。例如，我们可以要求它输出一个项目符号形式的问题列表，其中备选答案用方括号括起。然后我们可以解析并格式化该问题，作为用户界面呈现给用户。

尽管这是我们能做的最通用的改动，Claude 甚至似乎能够胜任输出这个内容，但这无法保证。Claude 会添加额外的句子、省略选项，或者完全使用不同的格式。

## 尝试 #3 - AskUserQuestion 工具

![Image](https://pbs.twimg.com/media/HCL0gcObkAA4tKt?format=jpg&name=large)

最后，我们决定创建一个 Claude 随时可以调用的工具，但特别在规划模式下会被提示这样做。当工具被触发时，我们会显示一个模态框来显示问题，并阻止代理的循环直到用户回答。

这个工具让我们能够提示 Claude 生成结构化输出，并且帮助我们确保 Claude 为用户提供了多种选择。它还为用户提供了实现该功能的方法，例如在 Agent SDK 中调用它，或者在技能中引用它。

最重要的是，Claude 似乎喜欢调用这个工具，我们发现它的输出结果效果很好。即使是设计最精良的工具，如果 Claude 不理解如何调用它，也无法正常工作。

这是 Claude Code 中提示方式的最终形式吗？我们不确定。如你在下一个示例中所见，适用于一个模型的方法可能并不适用于另一个模型。

# 更新功能 - 任务 & 待办事项

![Image](https://pbs.twimg.com/media/HCLxrfXbEAUXwRV?format=jpg&name=large)

当我们首次推出 Claude Code 时，我们意识到该模型需要一个待办事项列表来保持其按计划推进。待办事项可以在开始时记录，并在模型执行工作时标记为已完成。为实现这一点，我们为 Claude 配备了 TodoWrite 工具，该工具可以编写或更新待办事项并向用户展示。

但即便如此，我们经常看到 Claude 忘记它该做什么。为了适应，我们每 5 轮插入一次系统提醒，这些提醒会提醒 Claude 它的目标。

随着模型的改进，它们不仅不再需要被提醒待办事项列表，反而会觉得它有局限性。收到待办事项列表的提醒让 Claude 觉得它必须严格遵循这个列表，而不是修改它。我们还看到 Opus 4.5 在使用子代理方面也有了很大进步，但子代理如何在共享的待办事项列表上进行协调呢？

Seeing this, we replaced TodoWrite with the Task Tool (

[read more on Tasks here](https://x.com/trq212/status/2014480496013803643)). Whereas Todos were about keeping the model on track, Tasks were more about helping agents communicate with each other. Tasks could include dependencies, share updates across subagents and the model could alter and delete them.

随着模型能力的提升，你们的模型曾经需要的工具现在可能会限制它们。重要的是要不断重新审视关于需要哪些工具的先前假设。这也是为什么坚持使用一小部分具有相当相似能力特征的模型来支持是有用的。

# 设计搜索界面

对于 Claude 来说，特别重要的一组工具是可以用来构建其自身上下文的搜索工具。

当 Claude 首次推出时，我们使用 RAG 向量数据库为 Claude 查找上下文。虽然 RAG 功能强大且速度快，但它需要索引和设置，并且在多种不同环境中可能会很脆弱。更重要的是，Claude 被给予了这个上下文，而不是自己查找上下文。

但是如果 Claude 能在网上搜索，为什么不能搜索你的代码库呢？通过给 Claude 一个 Grep 工具，我们可以让它搜索文件并自行构建上下文。

这是我们观察到的一种模式：随着 Claude 变得更聪明，如果它得到合适的工具，它在构建上下文方面会变得越来越擅长。

当我们引入代理技能时，我们将渐进式披露的理念正式化，这使代理能够通过探索逐步发现相关上下文。

Claude 可以读取技能文件，而这些文件又可以引用模型递归读取的其他文件。事实上，技能的一个常见用途是为 Claude 添加更多搜索能力，比如给它提供如何使用 API 或查询数据库的指令。

在过去的一年中，Claude 从不太能够构建自己的上下文，转变为能够在几层文件中进行嵌套搜索，以找到所需的精确上下文。

渐进式展示现在是我们常用的一种无需添加工具即可添加新功能的技术。

# 渐进式披露 - Claude 代码指南代理

Claude Code 目前拥有大约 20 个工具，并且我们不断地问自己是否需要所有这些工具。添加新工具的门槛很高，因为这会给模型多一个需要考虑的选项。

例如，我们注意到 Claude 对如何使用 Claude Code 了解不足。如果你问它如何添加一个 MCP 或者斜杠命令是什么，它将无法回复。

我们本可以将所有这些信息都放在系统提示中，但考虑到用户很少询问这些内容，这会增加上下文衰减并干扰 Claude Code 的主要工作：编写代码。

相反，我们尝试了一种渐进式展示的方式。我们给 Claude 提供了一个文档链接，它可以加载该链接以搜索更多信息。这种方法有效，但我们发现，Claude 为了找到正确答案，会加载大量结果到上下文中，而实际上你只需要答案本身。

因此，我们构建了 Claude Code Guide 子代理，当你询问关于它自己的问题时，Claude 会被提示调用这个子代理。这个子代理有关于如何有效搜索文档以及返回什么内容的详细指令。

虽然这并非完美，但当你询问 Claude 如何进行自我设置时，它仍然可能会困惑，不过它已经比以前好多了！我们能够在不添加新工具的情况下，向 Claude 的操作空间中添加内容。

## 一门艺术，而非一门科学

如果你期望得到一套关于如何构建你的工具的严格规则，很遗憾，本指南并非如此。为你的模型设计工具既是一门科学，也是一门艺术。这在很大程度上取决于你使用的模型、智能体的目标以及它所处的环境。

多做实验，审视你的输出，尝试新事物。像代理一样观察。

* * *

### 热门回复

**@Canary Mission** ♥ 1.8K · 💬 303

EXCLUSIVELY EXPOSED:

“We proclaim our support for the Islamic republic! Shame, shame USA!”

“We condemn the assassination of martyr Ali Khamenei! Martyrdom is our highest honor!”

NJ resident and computer science student at Suffolk Community College, Taha Hasnain, wants to make

**@The YIVO Institute** ♥ 232 · 💬 11

YIVO Program Assistant August Kahn discusses a Yiddish Esperanto textbook.

**@Andrey** ♥ 92 · 💬 1

兄弟，你每次都出好东西，这些内容太有见地了！

**@toki** ♥ 79 · 💬 4

谢谢你的这个。刚刚把这篇文章粘贴到 Claude Code 里，现在我有了/agent-design 技能。

**@Thariq** ♥ 52 · 💬 1

啊，谢谢兄弟，我很高兴听到

* * *

# 构建 Claude 代码的经验：我们如何运用技能

https://x.com/trq212/status/2033949937936085378

**Thariq**

# 构建 Claude 代码的经验：我们如何运用技能

技能已成为 Claude Code 中最常用的扩展点之一。它们灵活、易于制作且易于分发。

但这种灵活性也使得难以确定什么最有效。值得培养什么样的技能？打造一个好技能的秘诀是什么？什么时候与他人分享这些技能？

我们在 Anthropic 公司广泛使用 Claude Code 中的技能，其中数百个技能正处于活跃使用状态。这些是我们学到的关于如何利用技能加速开发的经验教训。

## 什么是技能？

If you’re new to skills, I’d recommend

[reading our docs](https://code.claude.com/docs/en/skills) or watching our newest course on

[new Skilljar on Agent Skills](https://anthropic.skilljar.com/introduction-to-agent-skills)

, this post will assume you already have some familiarity with skills.

我们常听到关于技能的一个常见误解是，它们“只是 Markdown 文件”，但技能最有趣的部分在于，它们不仅仅是文本文件。它们是文件夹，可以包含脚本、资源、数据等，代理可以发现、探索和操作这些内容。

In Claude Code, skills also have a

[wide variety of configuration options](https://code.claude.com/docs/en/skills#frontmatter-reference) including registering dynamic hooks.

我们发现，Claude Code 中一些最有趣的技能会创造性地使用这些配置选项和文件夹结构。

# 技能类型

在整理完我们所有的技能后，我们注意到它们聚集到了几个常见的类别中。最优秀的技能能清晰地归入某一类；而那些较难归类的技能则横跨多个类别。这不是一份权威清单，但它是一种很好的思考方式，能帮助你判断你的组织是否缺少某些技能。

![Image](https://pbs.twimg.com/media/HDlvMmubEAIzF-N?format=jpg&name=large)

## 库和 API 参考

解释如何正确使用库、CLI 或 SDK 的技能。这些可以是针对内部库或 Claude Code 有时难以处理的通用库。这些技能通常包括一个参考代码片段文件夹，以及一份 Claude 在编写脚本时应避免的注意事项列表。

示例：

- billing-lib — 你内部的账单库：边缘情况、潜在陷阱等等。
- internal-platform-cli — 内部 CLI 包装器的每个子命令及其使用场景示例
- 前端设计——让 Claude 在你的设计系统中表现更好

## 2\. 产品验证

描述如何测试或验证代码是否正常工作的技能。这些技能通常与 playwright、tmux 等外部工具配合使用，以进行验证。

验证技能对于确保 Claude 的输出正确非常有用。让工程师花一周时间来使你的验证技能变得出色是值得的。

考虑诸如让 Claude 录制其输出的视频以便你能确切看到它测试了什么，或者在每个步骤中对状态执行程序化断言等技术。这些通常通过在技能中包含各种脚本来实现。

示例：

- signup-flow-driver — 在无头浏览器中执行注册→邮箱验证→新用户引导流程，带有用于在每个步骤中断言状态的钩子
- checkout-verifier — 使用 Stripe 测试卡驱动结账界面，验证发票实际处于正确状态
- tmux-cli-driver — 用于需要 TTY 的交互式命令行界面测试

## 3\. 数据获取与分析

与你的数据和监控栈相关的技能。这些技能可能包括用于带凭证获取数据的库、特定的仪表盘 ID 等，以及关于常见工作流或获取数据方法的说明。

示例：

- 漏斗查询 — 我需要参与哪些事件才能看到注册→激活→付费的流程，加上实际包含规范用户 ID 的表
- 队列对比 — 比较两个队列的留存率或转化率，标记具有统计显著性的差异，关联到细分定义
- Grafana — 数据源 UID、集群名称、问题 → 仪表盘查找表

## 4\. 业务流程与团队自动化

能够将重复工作流程自动转化为单个命令的技能。这些技能通常是相当简单的指令，但可能对其他技能或 MCPs 有更复杂的依赖关系。对于这些技能，将之前的结果保存到日志文件中可以帮助模型保持一致性，并反思工作流程的先前执行情况。

示例：

- standup-post — 聚合你的工单跟踪器、GitHub 活动和之前的 Slack → 格式化的站会，仅增量
- create-<ticket-system>-ticket — 强制验证模式（有效的枚举值、必填字段）以及创建后工作流（通知审核人、在 Slack 中关联）
- 每周总结 — 合并 PR + 关闭工单 + 部署 → 格式化总结帖子

## 5\. 代码脚手架与模板

生成特定功能框架样板的技能。你可以将这些技能与可组合的脚本结合使用。当你的脚手架有仅靠代码无法完全覆盖的自然语言需求时，这些技能尤其有用。

示例：

- new-<框架>-工作流 — 利用你的注释搭建新的服务/工作流/处理程序
- new-migration — 你的迁移文件模板加上常见陷阱
- create-app — 新的内部应用，其身份验证、日志记录和部署配置已预先配置

## 6\. 代码质量与评审

组织内部确保代码质量并帮助进行代码审查的技能。这些技能可能包括确定性脚本或工具，以实现最大的健壮性。您可能希望将这些技能作为钩子的一部分或在 GitHub Action 中自动运行。

- 对抗性审查——生成一个全新视角子代理进行批评，实施修复，迭代直到发现的问题降级为吹毛求疵的细节
- 代码风格 — 强制执行代码风格，尤其是 Claude 默认情况下做得不好的风格。
- 测试实践 — 关于如何编写测试及测试什么的说明。

## 7\. CI/CD & 部署

帮助你在代码库内部获取、推送和部署代码的技能。这些技能可能会引用其他技能来收集数据。

示例：

- babysit-pr — 监控 PR → 重试不稳定的 CI → 解决合并冲突 → 启用自动合并
- 部署-<服务> → 构建 → 冒烟测试 → 逐步流量发布并进行错误率比较 → 回归时自动回滚
- cherry-pick-prod — 隔离的工作树 → cherry-pick → 冲突解决 → 带模板的拉取请求

## 8\. 操作手册

能够处理一个症状（例如 Slack 讨论线程、告警或错误签名），进行多工具调查并生成结构化报告的技能。

示例：

- <service>-debugging — 映射症状 → 工具 → 查询模式 用于您的高流量服务
- oncall-runner — 获取告警 → 检查常见问题 → 格式化发现结果
- 日志关联器——给定请求 ID，从所有可能涉及该请求的系统中拉取匹配的日志

## 9\. 基础设施运维

执行日常维护和操作流程的技能——其中一些涉及破坏性操作，这些操作得益于防护措施。这些技能让工程师更容易在关键操作中遵循最佳实践。

示例：

- <资源>-orphans — 查找孤儿 Pod/卷 → 发送到 Slack → 浸泡期 → 用户确认 → 级联清理
- 依赖管理 — 您的组织的依赖审批流程
- 成本调查 — '为什么我们的存储/流出费用突然激增' 针对特定的存储桶和查询模式

# 技能提升小贴士

![Image](https://pbs.twimg.com/media/HDoKg58bEAAL1bw?format=jpg&name=large)

一旦你决定了要掌握的技能，该如何撰写它？这些是我们发现的一些最佳实践、技巧和窍门。

We also recently released

[Skill Creator](https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills) to make it easier to create skills in Claude Code.

## 不要说显而易见的话

Claude Code 对你的代码库非常了解，Claude 也对编程非常了解，包括许多默认观点。如果你要展示一项主要关于知识的技能，尽量聚焦于能让 Claude 跳出常规思维方式的信息。

The

[frontend design skill](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md) is a great example — it was built by one of the engineers at Anthropic by iterating with customers on improving Claude’s design taste, avoiding classic patterns like the Inter font and purple gradients.

## 构建一个注意事项部分

![Image](https://pbs.twimg.com/media/HDlwEG1bEAUdmcV?format=jpg&name=large)

任何技能中最重要的内容是易错点部分。这些部分应该基于 Claude 在使用你的技能时遇到的常见失败点来构建。理想情况下，你应该随着时间更新你的技能以涵盖这些易错点。

## 使用文件系统和渐进式展示

![Image](https://pbs.twimg.com/media/HDlwhSjbEAIJSc9?format=jpg&name=large)

就像我们之前说的，技能是一个文件夹，而不仅仅是一个 Markdown 文件。你应该将整个文件系统视为一种上下文工程和渐进式披露的形式。告诉 Claude 你技能中的文件有哪些，它会在适当的时候读取这些文件。

渐进式披露最简单的形式是指向其他 Markdown 文件供 Claude 使用。例如，你可以将详细的函数签名和使用示例拆分为 references/api.md。

另一个例子：如果你的最终输出是一个 markdown 文件，你可能会在 assets/中包含一个用于它的模板文件，供复制和使用。

你可以创建包含参考资料、脚本、示例等的文件夹，这些文件夹能帮助 Claude 更高效地工作。

## 避免强行推动 Claude

Claude 通常会尽量遵循你的指令，但由于技能具有很强的可重复使用性，你需要注意在指令中不要过于具体。给 Claude 提供它需要的信息，同时要给予它适应具体情况的灵活性。例如：

![Image](https://pbs.twimg.com/media/HDlwurvbEAM5ZNu?format=jpg&name=large)

## 仔细考虑设置

![Image](https://pbs.twimg.com/media/HDlw1mYbEAY-Bul?format=jpg&name=large)

某些技能可能需要根据用户提供的上下文进行设置。例如，如果你正在开发一个将你的每日站会内容发布到 Slack 的技能，你可能希望 Claude 询问应该发布到哪个 Slack 频道。

一个好的做法是将此设置信息存储在 skill 目录下的 config.json 文件中，如上面的示例所示。如果配置未设置，代理可以向用户询问信息。

如果你希望代理呈现结构化的选择题，你可以指示 Claude 使用 AskUserQuestion 工具。

## 描述字段用于模型

当 Claude Code 启动会话时，它会构建一个包含每个可用技能及其描述的列表。Claude 会扫描这个列表以判断“是否有适用于该请求的技能”。这意味着描述字段不是摘要——而是描述何时触发此 PR。

![Image](https://pbs.twimg.com/media/HDlw5ULbEAQOqtJ?format=jpg&name=large)

## 内存与数据存储

![Image](https://pbs.twimg.com/media/HDoImh1bEAU-mMI?format=jpg&name=large)

一些技能可以通过在其中存储数据来包含一种记忆形式。你可以将数据存储在任何东西中，从像仅追加文本日志文件或 JSON 文件这样简单的存储方式，到像 SQLite 数据库这样复杂的存储方式。

例如，一个 standup-post 技能可能会维护一个 standups.log 文件，记录它所写的每一篇帖子，这意味着下次运行时，Claude 会读取自己的历史记录，并能判断自昨天以来有哪些内容发生了变化。

Data stored in the skill directory may be deleted when you upgrade the skill, so you should store this in a stable folder, as of today we provide \`${CLAUDE\_PLUGIN\_DATA}\` as a stable folder per plugin to store data in.

## 保存脚本 & 生成代码

你能给 Claude 的最强大工具之一就是代码。给 Claude 提供脚本和库，能让 Claude 在每个回合专注于组合工作，决定下一步做什么，而不是重复编写模板代码。

例如，在你的数据科学技能中，你可能拥有一个用于从事件源获取数据的函数库。为了让 Claude 进行复杂分析，你可以给它一组辅助函数，像这样：

![Image](https://pbs.twimg.com/media/HDlxbtkbkAAOse7?format=jpg&name=large)

然后 Claude 可以实时生成脚本来组合此功能，以对诸如“周二发生了什么？”这样的提示进行更高级的分析

![Image](https://pbs.twimg.com/media/HDlxfEIb0AA2E7l?format=jpg&name=large)

## 按需钩子

技能可以包含仅在调用该技能时激活，并持续到会话结束的钩子。对于那些不想一直运行但有时又非常有用的更具倾向性的钩子，可以使用这种方式。

例如：

- /careful — blocks rm -rf, DROP TABLE, force-push, kubectl delete via PreToolUse matcher on Bash. You only want this when you know you're touching prod — having it always on would drive you insane
- /freeze — blocks any Edit/Write that's not in a specific directory. Useful
- 调试时："我想要添加日志，但我总是不小心地‘修复’无关的"

# 分配技能

技能的最大好处之一是你可以与团队中的其他成员分享它们。

有两种方式你可能会与他人分享技能：

- 检查你的技能到你的仓库中（位于 ./.claude/skills 下）
- make a plugin and have a Claude Code Plugin marketplace where users can upload and install plugins (read more on the
 
 [documentation](https://code.claude.com/docs/en/plugin-marketplaces) here)
 

对于仅使用相对较少代码仓库的小型团队而言，将技能检入代码仓库的方式效果良好。但每一项被检入的技能都会为模型的上下文增加一些内容。随着团队规模的扩大，内部插件市场允许你分发技能，并让团队自主决定安装哪些技能。

## 管理市场

你如何决定哪些技能进入技能市场？人们如何提交这些技能？

我们没有一个集中的团队来做决策；相反，我们尝试自然地发现最有用的技能。如果你有一项希望人们尝试的技能，你可以将其上传到 GitHub 的沙箱文件夹，然后在 Slack 或其他论坛中引导人们查看它。

一旦某个技能获得发展势头（这由技能所有者决定），他们就可以提交 PR 以将其发布到市场。

A note of warning, it can be quite easy to create bad or redundant skills, so making sure you have some method of curation before release is important.

## Composing Skills

You may want to have skills that depend on each other. For example, you may have a file upload skill that uploads a file, and a CSV generation skill that makes a CSV and uploads it. This sort of dependency management is not natively built into marketplaces or skills yet, but you can just reference other skills by name, and the model will invoke them if they are installed.

## Measuring Skills

To understand how a skill is doing, we use a PreToolUse hook that lets us log skill usage within the company (

[example code here](https://gist.github.com/ThariqS/24defad423d701746e23dc19aace4de5)). This means we can find skills that are popular or are undertriggering compared to our expectations.

# Conclusion

Skills are incredibly powerful, flexible tools for agents, but it’s still early and we’re all figuring out how to use them best.

Think of this more as a grab bag of useful tips that we’ve seen work than a definitive guide. The best way to understand skills is to get started, experiment, and see what works for you. Most of ours began as a few lines and a single gotcha, and got better because people kept adding to them as Claude hit new edge cases.

I hope this was helpful, let me know if you have any questions.