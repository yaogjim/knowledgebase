---
title: "Context Engineering for Agents"
source: "https://rlancemartin.github.io/2025/06/23/context_engineering/"
author:
published: 2025-07-11
created: 2025-06-26
description: "Patterns for managing the context needed for agents to perform their tasks."
tags:
  - "clippings"
---
[兰斯·马丁](https://x.com/RLanceMartin)

### 上下文工程

正如安德烈·卡帕西所说，大语言模型（LLMs）就像是一种新型操作系统。大语言模型（LLM）就如同中央处理器（CPU），其上下文窗口就像随机存取存储器（RAM），代表着模型的“工作内存”。

上下文以多种方式进入大语言模型（LLM），包括提示（例如用户指令）、检索（例如文档）和工具调用（例如应用程序编程接口）。

就像随机存取存储器（RAM）一样，大语言模型（LLM）的上下文窗口用于处理这些各种上下文来源的“通信带宽”有限。

正如操作系统管理哪些内容适合装入 CPU 的随机存取存储器一样，我们可以思考“上下文工程”，即将执行任务所需的信息填入上下文窗口的艺术与科学。

![](https://rlancemartin.github.io/assets/context_types.png)

### 上下文工程的兴起

上下文工程是一门涵盖几个不同重点领域的综合性学科：

- **教学上下文** – 提示（参见： [提示工程](https://www.promptingguide.ai/) ）、记忆、少样本示例
- **知识上下文** – 用于扩展模型世界知识的检索或记忆（参见： [基于检索增强生成](https://github.com/langchain-ai/rag-from-scratch) ）
- **操作上下文** – 通过工具从环境中流入的上下文

随着大语言模型（LLMs）在工具调用方面表现得越来越好，智能体现在变得可行了。智能体将大语言模型（LLM）调用与工具调用交织起来以处理长期运行的任务，并引发了对所有三种类型上下文进行工程设计的需求。

![](https://rlancemartin.github.io/assets/agent_flow.png)

[认知](https://cognition.ai/blog/dont-build-multi-agents) 指出了在构建智能体时上下文工程的重要性：

> *“上下文工程”……实际上是构建人工智能智能体的工程师的首要工作。*

[Anthropic](https://www.anthropic.com/engineering/built-multi-agent-research-system) 也明确阐述了这一点：

> *智能体常常会进行持续数百轮的对话，这就需要精心的上下文管理策略。*

本文旨在剖析一些用于智能体上下文工程的常见策略—— **压缩** 、 **持久化** 和 **隔离** 。

### 智能体的上下文工程

智能体上下文会填充来自工具调用的反馈，这些反馈可能会 [超出上下文窗口的大小](https://cognition.ai/blog/kevin-32b) ，并使成本/延迟大幅增加。

![](https://rlancemartin.github.io/assets/tool_context.png)

我多次吃过这方面的苦头。我构建的一个深度研究智能体的版本使用了大量令牌的搜索 API 工具调用，每次运行会产生超过 50 万个令牌，花费几美元！

长上下文也可能会降低智能体的性能。谷歌和珀西·梁的团队已经描述了不同类型的“上下文退化综合征”，因为长上下文会限制大语言模型（LLMs）回忆事实或遵循指令的能力。

有很多方法可以解决这个问题，我将其归纳为三类并在下面进行描述：压缩上下文、持久化上下文和隔离上下文。

![](https://rlancemartin.github.io/assets/context_eng_overview.png)

### 压缩上下文

压缩上下文涉及在每一轮中只保留价值最高的标记。

**上下文摘要**

智能体交互可能会持续 [数百轮](https://www.anthropic.com/engineering/built-multi-agent-research-system) ，并且可能会有大量令牌的工具调用。上下文总结是管理这一情况的一种常见方法。

如果你使用过 Claude Code，你就会看到它在实际运行中的情况。当你超过上下文窗口的 95%时，Claude Code 会运行“ [自动压缩](https://docs.anthropic.com/en/docs/claude-code/costs) ”。

摘要可用于不同的地方，例如使用递归或分层摘要等方法处理完整的智能体轨迹。

![](https://rlancemartin.github.io/assets/context_curation.png)

总结工具调用反馈（例如，一个占用大量令牌的搜索工具）或特定步骤（例如，Anthropic 的多智能体研究人员对已完成的工作阶段进行总结）也是很常见的。

[认知](https://cognition.ai/blog/dont-build-multi-agents#a-theory-of-building-long-running-agents) 指出，如果需要从智能体轨迹中提取特定事件或决策，那么总结可能会很棘手。他们在 Devin 中为此使用了一个微调模型，这凸显了在完善这一步骤时可能需要付出多少努力。

### 持久化上下文

持久化上下文涉及系统随时间存储、保存和检索上下文。

**存储上下文**

文件是存储上下文的一种简单方式。许多流行的智能体都采用了这种方式：Claude Code 使用 [`CLAUDE.md`](http://claude.md/) 。 [Cursor](https://docs.cursor.com/context/rules) 和 [Windsurf](https://windsurf.com/editor/directory) 使用规则文件，并且一些插件（例如， [Cursor Memory Bank](https://forum.cursor.com/t/managing-chat-context-in-cursor-ide-for-large-repositories-what-s-working-for-you/76391/2) ）/ [MCP 服务器](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) 管理内存文件集合。

一些智能体需要存储难以用几个文件轻松捕获的信息。例如，我们可能想要存储大量的事实和/或关系。出现了一些工具来支持这一点，并展示一些常见模式。

[莱塔](https://docs.letta.com/concepts/memgpt) 、 [内存 0](https://mem0.ai/research) 以及 [语言图](https://langchain-ai.github.io/langgraph/concepts/memory/#long-term-memory) / [内存](https://langchain-ai.github.io/langmem/) 存储嵌入式文档。 [泽普](https://arxiv.org/html/2501.13956v1#:~:text=In%20Zep%2C%20memory%20is%20powered,subgraph%2C%20and%20a%20community%20subgraph) 和 [尼奥 4J](https://neo4j.com/blog/developer/graphiti-knowledge-graph-memory/#:~:text=changes%20since%20updates%20can%20trigger,and%20holistic%20memory%20for%20agentic) 使用知识图谱对事实或关系进行连续/时态索引。

**保存上下文**

Claude 代码委托用户创建/更新记忆（例如， `#` 快捷键）。但在很多情况下，我们希望智能体能够自主创建/更新记忆。

《反思》一文介绍了在每个智能体回合后进行反思并重新利用这些自我生成提示的想法。《生成式智能体》通过综合过去反馈集合来创建记忆摘要。

这些概念已融入到诸如 ChatGPT、Cursor 和 Windsurf 等热门产品中，这些产品都具备基于用户与智能体的交互自动生成记忆的机制。

![](https://rlancemartin.github.io/assets/email_agent.png)

记忆创建也可以在智能体的轨迹中的特定点进行。我喜欢的一种模式是：根据用户反馈更新记忆。

例如，对工具调用进行人工参与的审查是增强对智能体信心的好方法。但如果将此与记忆更新相结合，那么随着时间的推移，智能体可以从你的反馈中学习。我的 [电子邮件助手](https://github.com/langchain-ai/agents-from-scratch) 就是通过基于文件的记忆来做到这一点的。

**检索上下文**

最简单的方法就是将所有记忆都拉入智能体的上下文窗口。例如，Claude Code 在每个会话开始时，只是将所有 [`CLAUDE.md`](http://claude.md/) 文件读入上下文。在我的 [电子邮件助手](https://github.com/langchain-ai/agents-from-scratch) 中，我总是加载一组提供电子邮件分类和回复指令的记忆到上下文中。

但是，如果记忆集合很大，那么获取选定记忆的机制就很重要。存储将有助于确定方法（例如，基于嵌入的搜索或图检索）。

[在实践中，这是一个很深奥的话题](https://x.com/_mohansolo/status/1899630246862966837) 。检索可能很棘手。例如， [生成式智能体](https://ar5iv.labs.arxiv.org/html/2304.03442) 根据相似性、近期性和重要性对记忆进行评分。 [西蒙·威利森分享了](https://simonwillison.net/2025/Jun/6/six-months-in-llms/) 一个记忆检索出错的例子。GPT-4o 根据他的记忆在图像中注入了位置信息，而这并非他所期望的。糟糕的记忆检索会让用户感觉上下文窗口“不属于他们”！

### 隔离上下文

隔离上下文涉及到在不同智能体或环境之间对其进行划分的方法。

**上下文模式**

通常， [消息](https://python.langchain.com/docs/concepts/messages/) 用于构建智能体上下文。工具反馈会附加到消息列表中。然后，在每个智能体轮次，完整的列表会被传递给大语言模型（LLM）。

问题在于，列表可能会因包含大量令牌的工具调用而变得臃肿。通过 [模式](https://langchain-ai.github.io/langgraph/concepts/low_level/#schema) （例如 [Pydantic](https://docs.pydantic.dev/latest/concepts/models/) 模型）定义的结构化运行时状态通常可能更有效。

然后，你可以更好地控制在每个智能体轮次中语言模型（LLM）能看到的内容。例如，在一个深度研究智能体的版本中，我的模式同时包含 `  消息  ` 和 [`  部分  `](https://github.com/langchain-ai/open_deep_research/blob/e5a5160a398a3699857d00d8569cb7fd0ac48a4f/src/open_deep_research/multi_agent.py#L428) 。 `  消息  ` 在每个轮次被传递给语言模型（LLM），但我将占用大量令牌的部分隔离在 `  部分  ` 中，并选择性地获取它们。

**多智能体**

一种流行的方法是在子智能体之间划分上下文。OpenAI 的 [Swarm](https://github.com/openai/swarm) 库的一个动机是“ [关注点分离](https://openai.github.io/openai-agents-python/ref/agent/) ”，即一组智能体可以处理子任务，并且每个智能体都有自己的指令和上下文窗口。

![](https://rlancemartin.github.io/assets/multi_agent.png)

Anthropic 的多智能体研究人员对此给出了明确的例证：具有孤立上下文的多智能体比单智能体的表现高出 90.2%，这在很大程度上归因于令牌使用情况。正如该博客中所说：

> *\[子智能体运行时\] 与它们自己的上下文窗口并行，同时探索问题的不同方面。*

多智能体存在的问题包括令牌使用（例如，比聊天多15倍的令牌）、子智能体规划需要精心的提示和上下文，以及子智能体协调。基于这些原因，认知学反对使用多智能体。

我也遇到过这种情况：我的深度研究智能体的一个迭代版本让一组智能体撰写报告的各个部分。有时最终报告显得脱节，因为这些智能体在撰写过程中没有相互交流。

解决这个问题的一种方法是确保任务是可并行化的。一个微妙之处在于，Anthropic 的深度研究多智能体系统将并行化应用于研究。这比写作更容易，写作需要报告各部分之间紧密衔接，以实现流畅的整体行文。

**通过环境实现上下文隔离**

HuggingFace 的深度研究员是上下文隔离的另一个很好的例子。大多数智能体使用工具调用 API，这些 API 返回可以传递给工具（例如搜索 API）以获取工具反馈（例如搜索结果）的 JSON 对象（参数）。

![](https://rlancemartin.github.io/assets/isolation.png)

HuggingFace 使用一个 [代码智能体](https://huggingface.co/papers/2402.01030) ，它输出用于执行工具的代码。代码在一个 [沙盒](https://e2b.dev/) 中运行，并且从代码执行中选择的工具反馈会被传回给 LLM。

> *\[代码智能体支持\] 对状态进行更好的处理…… 需要存储此图像/音频/其他内容以供后续使用？没问题，只需将其作为变量赋值到你的状态中，然后你 \[稍后即可使用它\]。*

沙盒存储执行期间生成的对象（例如图像），将它们与 LLM 上下文窗口隔离开来，但代理稍后仍可以使用变量引用这些对象。

### Lessons

构建智能体的一般原则仍处于起步阶段。模型变化迅速，《惨痛教训》告诫我们要避免进行随着大语言模型（LLMs）的改进而变得无关紧要的上下文工程。

例如， [持续学习](https://www.dwarkesh.com/p/timelines-june-2025) 可能会让 [大语言模型（LLMs）](https://www.wired.com/story/this-ai-model-never-stops-learning/?utm_source=chatgpt.com) 从反馈中学习，从而减少对外部记忆的一些需求。考虑到这一点以及上述模式，以下是一些大致按照使用它们所需的工作量排序的一般经验教训。

- **首先进行监测：** 始终 [查看你的数据](https://hamel.dev/blog/posts/evals/) 。在构建智能体时，确保你有一种跟踪令牌的方法。这使我能够捕捉到各种令牌使用过量的情况，并隔离出占用大量令牌的工具调用。这为任何上下文工程工作奠定了基础。
- **思考你的智能体状态：** Anthropic 提出了“ [像你的智能体一样思考](https://www.youtube.com/watch?v=D7_ipDqhtwk) ”的理念。一种实现方法是思考你的智能体在运行时需要收集和使用的信息。定义良好的状态模式是在智能体运行过程中更好地控制向 LLM 暴露内容的简便方法。我在构建的几乎每个智能体中都使用了这一方法，而不是仅仅将所有上下文保存到消息列表中。\[Anthropic\]在他们的研究中也提到了这一点，他们保存研究计划以供将来使用。
- **在工具边界进行压缩：** 如有需要，工具边界是添加压缩的自然位置。例如，可以使用简单提示的小型 LLM 对大量令牌工具调用的输出进行总结。这使您能够在源处快速限制失控的上下文增长，而无需在整个智能体轨迹上进行压缩。
- **从简单的记忆开始** ：记忆是使智能体个性化的有力方式。然而，要做好并不容易。我 [经常使用](https://github.com/langchain-ai/agents-from-scratch) 简单的基于文件的记忆，它会跟踪我想要保存并随时间改进的一小部分智能体偏好。每次我的智能体运行时，我都会将这些偏好加载到上下文中。基于人工参与的反馈，我使用大语言模型（LLM）来更新这些偏好（见 [此处](https://github.com/langchain-ai/agents-from-scratch) ）。这是一种使用记忆的简单而有效的方法，但显然如果需要，记忆的复杂性可以显著增加。
- **考虑用于易于并行化任务的多智能体** ：智能体间通信仍处于早期阶段，协调多智能体团队很困难。但这并不意味着你应该放弃多智能体的想法。相反，在问题可以轻松并行化且子智能体之间不需要严格紧密协调的情况下考虑多智能体，如 [Anthropic 的多智能体研究人员](https://www.anthropic.com/engineering/built-multi-agent-research-system) 案例所示。