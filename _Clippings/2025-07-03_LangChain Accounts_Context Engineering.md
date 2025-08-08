---
title: "Context Engineering"
source: "https://blog.langchain.com/context-engineering-for-agents/"
author:
  - "[[LangChain Accounts]]"
published: 2025-07-02
created: 2025-07-03
description: "TL;DRAgents need context to perform tasks. Context engineering is the art and science of filling the context window with just the right information at each step of an agent’s trajectory. In this post, we break down some common strategies — write, select, compress, and isolate — for context engineering"
tags:
  - "clippings"
---
### TL;DR

智能体执行任务需要上下文。上下文工程是一门艺术与科学，即在智能体运行轨迹的每一步，用恰到好处的信息填充上下文窗口。在本文中，我们通过回顾各种流行的智能体和论文，剖析上下文工程的一些常见策略—— **编写、选择、压缩和隔离** 。然后我们将解释 LangGraph 是如何设计来支持这些策略的！

**此外，点击此处查看我们关于情境工程的视频** [**此处**](https://youtu.be/4GiqzUHD5AA?ref=blog.langchain.com) **。**

![](https://blog.langchain.com/content/images/2025/07/image.png)

上下文工程的一般类别

### 上下文工程

正如安德烈·卡帕西所说，大语言模型（LLMs）就像是一种新型操作系统。大语言模型（LLM）就如同中央处理器（CPU），其上下文窗口就像随机存取存储器（RAM），充当模型的工作内存。就像随机存取存储器一样，大语言模型上下文窗口处理各种上下文来源的能力有限。而且，正如操作系统会筛选适合中央处理器随机存取存储器的内容一样，我们可以认为“上下文工程”也起着类似的作用。卡帕西对此总结得很好：

> *\[上下文工程是\]“……一门微妙的艺术与科学，即为下一步操作在上下文窗口中填入恰到好处的信息。”*

![](https://blog.langchain.com/content/images/2025/07/image-1.png)

LLM 应用中常用的上下文类型

在构建 LLM 应用程序时，我们需要管理哪些类型的上下文？上下文工程就像一把伞，适用于几种不同类型的上下文：

- **说明** – 提示、记忆、少样本示例、工具描述等
- **知识** – 事实、记忆等
- **工具** – 来自工具调用的反馈

### 智能体的情境工程

今年，随着大语言模型（LLMs）在推理和工具调用方面表现得越来越好，人们对智能体（agents）的兴趣急剧增长。智能体（Agents）交错进行大语言模型（LLM）调用和工具调用，通常用于处理长时间运行的任务（long-running tasks）。智能体（Agents）交错进行大语言模型（LLM）调用和工具调用，并利用工具反馈来决定下一步行动。

![](https://blog.langchain.com/content/images/2025/07/image-2.png)

智能体交错进行大语言模型（LLM）调用和工具调用，利用工具反馈来决定下一步行动

然而，长时间运行的任务以及来自工具调用的累积反馈意味着智能体通常会使用大量的标记。这可能会导致许多问题：它可能会 [超出上下文窗口的大小](https://cognition.ai/blog/kevin-32b?ref=blog.langchain.com) ，使成本/延迟大幅增加，或者降低智能体的性能。德鲁·布罗伊尼格 [很好地概述了](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html?ref=blog.langchain.com) 较长上下文可能导致性能问题的一些具体方式，包括：

- [上下文中毒：当一个幻觉进入上下文时](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html?ref=blog.langchain.com#context-poisoning)
- [上下文干扰：当上下文使训练不堪重负时](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html?ref=blog.langchain.com#context-distraction)
- [上下文混淆：当多余的上下文影响响应时](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html?ref=blog.langchain.com#context-confusion)
- [上下文冲突：当上下文的各部分不一致时](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html?ref=blog.langchain.com#context-clash)
![](https://blog.langchain.com/content/images/2025/07/image-3.png)

来自工具调用的上下文会在多个智能体轮次中累积

考虑到这一点，《认知》强调了情境工程的重要性：

> *“情境工程”……实际上是构建人工智能代理的工程师的首要工作。*

[Anthropic](https://www.anthropic.com/engineering/built-multi-agent-research-system?ref=blog.langchain.com) 也明确阐述了这一点：

> *智能体常常会进行持续数百轮的对话，这就需要精心的上下文管理策略。*

那么，如今人们是如何应对这一挑战的呢？我们将智能体上下文工程的常见策略归为四类—— **编写、选择、压缩和隔离** ，并通过回顾一些流行的智能体产品和论文，给出每一类的示例。然后我们将解释 LangGraph 是如何设计来支持这些策略的！

![](https://blog.langchain.com/content/images/2025/07/image-4.png)

上下文工程的一般类别

### 编写上下文

*编写上下文意味着将其保存在上下文窗口之外，以帮助智能体执行任务。*

**临时记录区**

当人类解决任务时，我们会做笔记并记住事情，以便用于未来相关的任务。智能体也正在获得这些能力！通过“ [暂存区](https://www.anthropic.com/engineering/claude-think-tool?ref=blog.langchain.com) ”做笔记是智能体执行任务时持久保存信息的一种方法。其理念是在上下文窗口之外保存信息，以便智能体能够获取。 [Anthropic 的多智能体研究员](https://www.anthropic.com/engineering/built-multi-agent-research-system?ref=blog.langchain.com) 给出了一个清晰的例子：

> *首席研究员首先思考研究方法，并将其计划保存到内存中以保留上下文，因为如果上下文窗口超过200,000个标记，它将被截断，保留计划很重要。*

暂存区可以通过几种不同的方式来实现。它们可以是一个简单地 [写入文件的工具调用](https://www.anthropic.com/engineering/claude-think-tool?ref=blog.langchain.com) 。它们也可以是运行时 [状态对象](https://langchain-ai.github.io/langgraph/concepts/low_level/?ref=blog.langchain.com#state) 中的一个字段，该字段在会话期间持续存在。在任何一种情况下，暂存区都能让智能体保存有用信息以帮助它们完成任务。

**记忆**

暂存区帮助智能体在给定会话（或 [线程](https://langchain-ai.github.io/langgraph/concepts/persistence/?ref=blog.langchain.com#threads) ）内解决任务，但有时智能体需要在 *多个* 会话中记住一些事情才能受益！ [反思智能体](https://arxiv.org/abs/2303.11366?ref=blog.langchain.com) 引入了在每个智能体回合后进行反思并重用这些自我生成的记忆的想法。 [生成式智能体](https://ar5iv.labs.arxiv.org/html/2304.03442?ref=blog.langchain.com) 创建了定期从过去智能体反馈集合中合成的记忆。

![](https://blog.langchain.com/content/images/2025/07/image-5.png)

LLM 可用于更新或创建记忆

这些概念已融入到诸如 ChatGPT、Cursor 和 Windsurf 等热门产品中，这些产品都具备根据用户与代理的交互自动生成可跨会话持久保存的长期记忆的机制。

### 选择上下文

*选择上下文意味着将其拉入上下文窗口，以帮助智能体执行任务。*

**便签本**

从暂存区中选择上下文的机制取决于暂存区的实现方式。如果它是一个 [工具](https://www.anthropic.com/engineering/claude-think-tool?ref=blog.langchain.com) ，那么智能体可以通过进行工具调用来简单地读取它。如果它是智能体运行时状态的一部分，那么开发者可以选择在每一步向智能体暴露状态的哪些部分。这为在后续轮次中将暂存区上下文暴露给 LLM 提供了细粒度的控制级别。

**记忆**

如果智能体有保存记忆的能力，那么它们还需要具备选择与正在执行的任务相关记忆的能力。这样做有几个原因。智能体可能会选择少量示例（ [情景](https://langchain-ai.github.io/langgraph/concepts/memory/?ref=blog.langchain.com#memory-types) [记忆](https://arxiv.org/pdf/2309.02427?ref=blog.langchain.com) ）作为期望行为的示例、指令（ [程序](https://langchain-ai.github.io/langgraph/concepts/memory/?ref=blog.langchain.com#memory-types) [记忆](https://arxiv.org/pdf/2309.02427?ref=blog.langchain.com) ）来引导行为，或者选择事实（ [语义](https://langchain-ai.github.io/langgraph/concepts/memory/?ref=blog.langchain.com#memory-types) [记忆](https://arxiv.org/pdf/2309.02427?ref=blog.langchain.com) ）以获取与任务相关的上下文。

![](https://blog.langchain.com/content/images/2025/07/image-6.png)

几个可以应用摘要的地方

一个挑战是确保选择相关的记忆。一些流行的智能体只是简单地使用一组有限的文件，这些文件总是被纳入上下文。例如，许多代码智能体使用特定的文件来保存指令（“程序性”记忆），或者在某些情况下保存示例（“情景性”记忆）。Claude Code 使用 [`CLAUDE.md`](http://claude.md/?ref=blog.langchain.com) 。 [Cursor](https://docs.cursor.com/context/rules?ref=blog.langchain.com) 和 [Windsurf](https://windsurf.com/editor/directory?ref=blog.langchain.com) 使用规则文件。

但是，如果一个智能体要存储大量的事实和/或关系（例如语义记忆），那么选择就会更加困难。ChatGPT 就是一个很好的例子，它是一款热门产品，能够存储并从大量特定用户的记忆中进行选择。

用于内存索引的嵌入和/或知识图谱通常用于辅助选择。不过，内存选择仍然具有挑战性。在人工智能工程师世界博览会上，西蒙·威利森分享了一个选择出错的例子：ChatGPT 从记忆中获取了他的位置，并意外地将其注入到请求的图像中。这种意外或不期望的内存检索会让一些用户觉得上下文缠绕器“不再属于他们”！

**Tools**

智能体使用工具，但如果提供的工具过多，它们可能会不堪重负。这通常是因为工具描述存在重叠，导致模型在选择使用哪个工具时产生困惑。一种方法是将 RAG（检索增强生成）应用于工具描述，以便只为任务获取最相关的工具。一些近期的论文表明，这能将工具选择的准确率提高三倍。

**知识**

[检索增强生成（RAG）](https://github.com/langchain-ai/rag-from-scratch?ref=blog.langchain.com) 是一个丰富的主题，并且它 [可能是上下文工程的核心挑战](https://x.com/_mohansolo/status/1899630246862966837?ref=blog.langchain.com) 。代码智能体是大规模生产中 RAG 的一些最佳示例。来自 Windsurf 的瓦伦很好地捕捉到了其中的一些挑战：

> *索引代码≠上下文检索……\[我们正在进行索引和嵌入搜索……\[通过\]抽象语法树（AST）解析代码并沿着语义有意义的边界进行分块……随着代码库规模的增长，嵌入搜索作为一种检索启发式方法变得不可靠……我们必须依靠诸如 grep/文件搜索、基于知识图谱的检索等多种技术的组合，以及……一个重新排序步骤，在该步骤中\[上下文\]按相关性顺序进行排序。*

### 压缩上下文

*压缩上下文涉及仅保留执行任务所需的标记。*

**上下文摘要**

智能体交互可能会持续 [数百轮](https://www.anthropic.com/engineering/built-multi-agent-research-system?ref=blog.langchain.com) ，并使用大量令牌的工具调用。总结是应对这些挑战的一种常见方法。如果你使用过 Claude Code，就会看到它在实际运行。当你超过上下文窗口的 95%后，Claude Code 会运行“ [自动压缩](https://docs.anthropic.com/en/docs/claude-code/costs?ref=blog.langchain.com) ”，它会总结用户与智能体交互的完整轨迹。这种跨 [智能体轨迹](https://langchain-ai.github.io/langgraph/concepts/memory/?ref=blog.langchain.com#manage-short-term-memory) 的压缩类型可以使用各种策略，如 [递归](https://arxiv.org/pdf/2308.15022?ref=blog.langchain.com#:~:text=the%20retrieved%20utterances%20capture%20the,based%203) 或 [分层](https://alignment.anthropic.com/2025/summarization-for-monitoring/?ref=blog.langchain.com#:~:text=We%20addressed%20these%20issues%20by,of%20our%20computer%20use%20capability) 总结。

![](https://blog.langchain.com/content/images/2025/07/image-7.png)

几个可以应用摘要的地方

在智能体设计的特定点添加总结也可能很有用。例如，它可用于对某些工具调用进行后处理（例如，占用大量令牌的搜索工具）。再举一个例子，“认知”在智能体与智能体的边界处提到了总结，以在知识交接期间减少令牌数量。如果需要捕捉特定事件或决策，总结可能会是一项挑战。“认知”为此使用了一个经过微调的模型，这凸显了这一步骤可能需要做多少工作。

**上下文修剪**

虽然总结通常使用语言模型（LLM）来提炼最相关的上下文片段，但修剪通常可以过滤上下文，或者用德鲁·布罗伊尼格的话来说，“修剪”上下文。这可以使用硬编码的启发式方法，比如从列表中删除旧消息。德鲁还提到了普罗旺斯，这是一个经过训练的用于问答的上下文修剪器。

### 隔离上下文

*隔离上下文涉及将其拆分，以帮助智能体执行任务。*

**多智能体**

隔离上下文最流行的方法之一是将其分散到子智能体中。OpenAI 的 [Swarm](https://github.com/openai/swarm?ref=blog.langchain.com) 库的一个动机是 [关注点分离](https://openai.github.io/openai-agents-python/ref/agent/?ref=blog.langchain.com) ，即一组智能体可以处理特定的子任务。每个智能体都有一组特定的工具、指令以及它自己的上下文窗口。

![](https://blog.langchain.com/content/images/2025/07/image-8.png)

跨多个智能体拆分上下文

Anthropic 的多智能体研究人员为此提供了一个例证：许多具有孤立上下文的智能体表现优于单智能体，很大程度上是因为每个子智能体的上下文窗口可以分配给更狭窄的子任务。正如该博客所说：

> *\[子代理与它们自己的上下文窗口并行运行，同时探索问题的不同方面。\]*

当然，多智能体面临的挑战包括令牌使用（例如，据 Anthropic 报告，比聊天多使用高达 15 倍的令牌）、需要精心进行提示工程以规划子智能体的工作，以及子智能体的协调。

**使用环境进行上下文隔离**

HuggingFace 的深度研究员展示了另一个有趣的上下文隔离示例。大多数智能体使用工具调用 API，这些 API 返回可传递给工具（例如搜索 API）以获取工具反馈（例如搜索结果）的 JSON 对象（工具参数）。HuggingFace 使用一种代码智能体，其输出包含所需的工具调用。然后代码在沙盒中运行。工具调用中选定的上下文（例如返回值）随后会传递回 LLM。

![](https://blog.langchain.com/content/images/2025/07/image-9.png)

沙盒可以将上下文与大语言模型（LLM）隔离开来。

这使得上下文能够在环境中与大语言模型（LLM）隔离开来。Hugging Face 指出，这是一种特别好的隔离大型对象的方法：

> *\[代码代理允许\]更好地处理状态……需要存储此图像/音频/其他内容以供以后使用？没问题，只需将其作为变量* [*赋值到你的状态中，然后你就可以\[在以后使用它\]*](https://deepwiki.com/search/i-am-wondering-if-state-that-i_0e153539-282a-437c-b2b0-d2d68e51b873?ref=blog.langchain.com) *。*

**State**

值得指出的是，智能体的运行时 [状态对象](https://langchain-ai.github.io/langgraph/concepts/low_level/?ref=blog.langchain.com#state) 也是隔离上下文的好方法。这与沙盒化具有相同的作用。状态对象可以设计为具有一个 [模式](https://langchain-ai.github.io/langgraph/concepts/low_level/?ref=blog.langchain.com#schema) ，该模式具有可写入上下文的字段。模式的一个字段（例如， `messages` ）可以在智能体的每一轮中暴露给 LLM，但模式可以隔离其他字段中的信息以供更有选择性地使用。

### 使用 LangSmith / LangGraph 进行上下文工程

那么，你如何应用这些想法呢？在开始之前，有两个基础要素会很有帮助。首先，确保你有一种方法来查看数据并跟踪整个智能体的令牌使用情况。这有助于了解在何处最适合进行上下文工程。LangSmith 非常适合智能体追踪/可观测性，并提供了一种很好的方法来做到这一点。其次，确保你有一种简单的方法来测试上下文工程是会损害还是提高智能体性能。LangSmith 支持智能体评估，以测试任何上下文工程工作的影响。

**编写上下文**

LangGraph 在设计时兼具线程作用域（ [短期](https://langchain-ai.github.io/langgraph/concepts/memory/?ref=blog.langchain.com#short-term-memory) ）和 [长期记忆](https://langchain-ai.github.io/langgraph/concepts/memory/?ref=blog.langchain.com#long-term-memory) 。短期记忆使用 [检查点](https://langchain-ai.github.io/langgraph/concepts/persistence/?ref=blog.langchain.com) 来在智能体的所有步骤中持久保存 [智能体状态](https://langchain-ai.github.io/langgraph/concepts/low_level/?ref=blog.langchain.com#state) 。这作为一个“便签本”非常有用，使你能够向状态写入信息并在智能体轨迹的任何步骤中获取它。

LangGraph 的长期记忆功能使您能够在与智能体的多个会话中持久保存上下文 *（跨多个会话）* 。它非常灵活，允许您保存少量的 [文件](https://langchain-ai.github.io/langgraph/concepts/memory/?ref=blog.langchain.com#profile) （例如，用户配置文件或规则）或更大的 [记忆集合](https://langchain-ai.github.io/langgraph/concepts/memory/?ref=blog.langchain.com#collection) 。此外， [LangMem](https://langchain-ai.github.io/langmem/?ref=blog.langchain.com) 提供了一系列有用的抽象概念，以帮助进行 LangGraph 的内存管理。

**选择上下文**

在 LangGraph 智能体的每个节点（步骤）中，你可以获取状态。这使你能够在智能体的每个步骤中对呈现给 LLM 的上下文进行细粒度控制。

此外，LangGraph 的长期记忆在每个节点中都可访问，并支持各种类型的检索（例如，获取文件以及基于嵌入的内存集合检索）。有关长期记忆的概述，请参阅我们的深度学习.ai 课程。有关应用于特定智能体的内存的入门内容，请参阅我们的环境智能体课程。这展示了如何在一个可以管理你的电子邮件并从你的反馈中学习的长期运行的智能体中使用 LangGraph 内存。

![](https://blog.langchain.com/content/images/2025/07/image-10.png)

具有用户反馈和长期记忆功能的电子邮件代理

对于工具选择， [LangGraph Bigtool](https://github.com/langchain-ai/langgraph-bigtool?ref=blog.langchain.com) 库是对工具描述应用语义搜索的好方法。在处理大量工具时，这有助于为任务选择最相关的工具。最后，我们有几个 [教程和视频](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/?ref=blog.langchain.com) 展示了如何将各种类型的 RAG 与 LangGraph 一起使用。

**压缩上下文**

由于 LangGraph 是一个低级编排框架，你将代理布置为一组节点，定义每个节点内的逻辑，并定义一个在它们之间传递的状态对象。这种控制提供了几种压缩上下文的方法。

一种常见的方法是使用消息列表作为你的智能体状态，并定期使用一些内置实用工具对其进行总结或修剪。不过，你也可以通过几种不同的方式添加逻辑来对工具调用或智能体的工作阶段进行后处理。你可以在特定点添加总结节点，也可以在工具调用节点添加总结逻辑，以便压缩特定工具调用的输出。

**隔离上下文**

LangGraph 是围绕一个 [状态](https://langchain-ai.github.io/langgraph/concepts/low_level/?ref=blog.langchain.com#state) 对象设计的，它允许你指定一个状态模式，并在每个智能体步骤中访问状态。例如，你可以将工具调用的上下文存储在状态的某些字段中，在需要该上下文之前将它们与 LLM 隔离。除了状态，LangGraph 还支持使用沙盒进行上下文隔离。有关使用 [E2B 沙盒](https://e2b.dev/?ref=blog.langchain.com) 进行工具调用的 LangGraph 智能体示例，请参阅此 [仓库](https://github.com/jacoblee93/mini-chat-langchain?tab=readme-ov-file&ref=blog.langchain.com) 。有关使用 Pyodide 进行沙盒化（其中状态可以持久化）的示例，请参阅此 [视频](https://www.youtube.com/watch?v=FBnER2sxt0w&ref=blog.langchain.com) 。LangGraph 还对构建多智能体架构提供了很多支持，例如 [监督器](https://github.com/langchain-ai/langgraph-supervisor-py?ref=blog.langchain.com) 和 [群体](https://github.com/langchain-ai/langgraph-swarm-py?ref=blog.langchain.com) 库。有关使用 LangGraph 的多智能体的更多详细信息，你可以 [查看](https://www.youtube.com/watch?v=4nZl32FwU-o&ref=blog.langchain.com) [这些](https://www.youtube.com/watch?v=JeyDrn1dSUQ&ref=blog.langchain.com) [视频](https://www.youtube.com/watch?v=B_0TNuYi56w&ref=blog.langchain.com) 。

### 结论

上下文工程正在成为智能体构建者应努力掌握的一门技艺。在此，我们介绍了当今许多流行智能体中常见的一些模式：

- *编写上下文——将其保存在上下文窗口之外，以帮助智能体执行任务。*
- *选择上下文——将其拉入上下文窗口以帮助代理执行任务。*
- *压缩上下文——仅保留执行任务所需的标记。*
- *隔离上下文——将其拆分以帮助智能体执行任务。*

LangGraph 使实现它们中的每一个都变得容易，而 LangSmith 提供了一种简单的方法来测试你的智能体并跟踪上下文使用情况。LangGraph 和 LangSmith 共同形成了一个良性反馈循环，用于识别应用上下文工程的最佳机会、实施它、测试它并不断重复。