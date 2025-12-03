---
title: "Agent Frameworks, Runtimes, and Harnesses- oh my!"
source: "https://blog.langchain.com/agent-frameworks-runtimes-and-harnesses-oh-my/"
author:
  - "[[LangChain Accounts]]"
published: 2025-11-11
created: 2025-11-11
description: "There are few different open source packages we maintain: LangChain and LangGraph being the biggest ones, but DeepAgents being an increasingly popular one. I’ve started using different terms to describe them: LangChain is an agent framework, LangGraph is an agent runtime, DeepAgents is an agent harness. Other folks are"
tags:
  - "LangChain Accounts"
status: "inbox"
importance: 2
effort: 2
review_level: 0
review_next: "2025-12-10"
review_interval: null
review_count: 0
decision: null
topics: []
links_out: []
summary: ""
pov: ""
actions: []
---
我们维护着几个不同的开源软件包： [LangChain](https://docs.langchain.com/oss/python/langchain/quickstart?ref=blog.langchain.com&ajs_aid=52fc5c7a-ee15-4113-91a9-edd21e24400b) 和 [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview?ref=blog.langchain.com&ajs_aid=52fc5c7a-ee15-4113-91a9-edd21e24400b) 是其中规模最大的，而 [DeepAgents](https://docs.langchain.com/oss/python/deepagents/overview?ref=blog.langchain.com&ajs_aid=52fc5c7a-ee15-4113-91a9-edd21e24400b) 正日益受到欢迎。我开始用不同的术语来描述它们：LangChain 是智能体框架，LangGraph 是智能体运行时，DeepAgents 则是 [智能体治理工具](https://www.vtrivedy.com/posts/claude-code-sdk-haas-harness-as-a-service?ref=blog.langchain.com) 。其他人也在使用这些术语——但我认为框架、运行时和治理工具之间尚无明确定义。本文将尝试厘清这些概念。我必须承认这些定义仍存在模糊与重叠之处，因此非常欢迎各位提出反馈意见！

![](https://blog.langchain.com/content/images/size/w600/2025/10/Screenshot-2025-10-25-at-9.08.30---AM.png)

## 代理框架（LangChain）

市面上大多数辅助构建 LLM 应用的包，我将其归类为智能体框架。它们提供的核心价值在于抽象层，这些抽象代表着对世界的思维模型。理想的抽象层应当能降低入门门槛，同时为应用开发提供标准化方式，便于开发者快速上手并在不同项目间切换。对抽象层的批评在于，若设计不当反而会掩盖内部运作机制，无法满足高级用例所需的灵活性。

我们将 [LangChain](https://docs.langchain.com/oss/python/langchain/overview?ref=blog.langchain.com&ajs_aid=52fc5c7a-ee15-4113-91a9-edd21e24400b) 视为智能体框架。在 1.0 版本开发过程中，我们投入大量时间构思抽象层——包括结构化内容块、智能体循环机制、以及为标准智能体循环提升灵活性的中间件。其他符合智能体框架定义的示例包括 Vercel 的 AI SDK、CrewAI、OpenAI Agents SDK、Google ADK、LlamaIndex 等众多方案。

## 代理运行时（LangGraph）

当需要在生产环境中运行智能体时，你会需要某种智能体运行时。这种运行时应当提供更多基础设施层面的考量。首先想到的是 [持久化执行](https://docs.langchain.com/oss/python/langgraph/durable-execution?ref=blog.langchain.com&ajs_aid=52fc5c7a-ee15-4113-91a9-edd21e24400b) ，但我认为还应包含对流式处理的支持、 [人工介入支持](https://docs.langchain.com/oss/python/langgraph/interrupts?ref=blog.langchain.com&ajs_aid=52fc5c7a-ee15-4113-91a9-edd21e24400b) 、线程级持久化以及 [跨线程持久化](https://docs.langchain.com/oss/python/langgraph/add-memory?ref=blog.langchain.com&ajs_aid=52fc5c7a-ee15-4113-91a9-edd21e24400b) 等考量因素。

在构建 [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview?ref=blog.langchain.com&ajs_aid=52fc5c7a-ee15-4113-91a9-edd21e24400b) 时，我们便希望从头打造一个生产就绪的智能体运行时环境。您可 [在此](https://blog.langchain.com/building-langgraph/) 进一步了解我们开发 LangGraph 的思考过程。我们认为与此最接近的其他项目包括 Temporal、Inngest 等持久化执行引擎。

代理运行时通常比代理框架更为底层，能够为代理框架提供支持。例如，LangChain 1.0 便是构建在 LangGraph 之上，以利用其提供的代理运行时能力。

## 智能体框架（DeepAgents）

[DeepAgents](https://docs.langchain.com/oss/python/deepagents/overview?ref=blog.langchain.com&ajs_aid=52fc5c7a-ee15-4113-91a9-edd21e24400b) 是我们正在开发的最新项目。它比智能体框架更高级——构建在 LangChain 之上。它内置了默认提示词、规范化的工具调用处理机制、规划工具，支持文件系统访问等功能。这不仅是框架，更是开箱即用的完整解决方案。

我们用来描述 DeepAgents 的另一种方式是“通用版 Claude Code”。平心而论，Claude Code 本身也在尝试成为智能体运行框架——他们发布的 Claude Agent SDK 就是朝这个方向迈出的一步。除了 Claude Agent SDK，我认为目前市面上并没有太多通用的智能体运行框架。不过也有人认为，从某种角度来说，所有编程命令行工具都可以算作智能体运行框架，并且可能具备通用性。

## 何时使用每一种

我们来总结一下差异，并讨论各自适用的场景：

![](https://blog.langchain.com/content/images/size/w600/2025/10/Screenshot-2025-10-25-at-9.05.40---AM.png)

必须承认，这些概念之间的界限确实模糊。例如，LangGraph 或许最恰当的定位是兼具运行时和框架的双重属性。而"智能体治理框架"这个术语（ [并非我的首创](https://www.vtrivedy.com/posts/claude-code-sdk-haas-harness-as-a-service?ref=blog.langchain.com) ）也是近期才逐渐被广泛使用。我认为目前对这些概念尚未形成特别明确的定义。

在早期领域开发的部分乐趣，在于构建用于描述事物的心智模型。我们知道 LangChain 不同于 LangGraph，而 DeepAgents 又与这两者都不同。将它们分别描述为框架、运行时和测试平台是一种有益的区分——但一如既往，我们期待您的反馈！