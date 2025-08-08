---
title: "Which agent framework should you use? I tried 7. The winners will surprise you 🤯"
source: "https://makingaiagents.substack.com/p/which-agent-framework-should-you"
author:
  - "[[Julian Harris]]"
published: 2025-06-19
created: 2025-07-01
description: "I rewrote my \"tech writer\" agent in 7 frameworks: Agno, Autogen, Google ADK, Atomic Agents, DSPy, Langgraph, and Pydantic AI. You'll NEVER guess the winners."
tags:
  - "clippings"
---
### 我用 7 种框架重写了我的“技术写作”智能体：Agno、Autogen、谷歌 ADK、Atomic Agents、DSPy、Langgraph 和 Pydantic AI。你绝对猜不到胜出者是谁。

*新功能： [试用我的实验性聊天机器人](https://reports.makingaiagents.com/) ，你可以在其中阅读本文， **浏览代理源代码，** 并提问：*

![](https://substackcdn.com/image/fetch/$s_!s7uu!)

[https://reports.makingaiagents.com](https://reports.makingaiagents.com/) 是一个实验性聊天机器人，可让您就该报告进行对话。

所以你想制作一个智能体。

**那么代理框架到底有多有用呢？**

在《制作人工智能代理》的上一期中，我编写了一个没有框架的技术写作代理。

这个“无框架”智能体展示了智能体可以有多简单，但仍然具有几年前还只存在于科幻作品中的相当神奇的特性。

为了回答关于框架的问题，我在一系列不同的框架中实现了完全相同的技术文档撰写代理，并在此分享我的见解。

## 但首先，有多少种智能体创建框架呢？

据最新统计，我已确定大约：

- 133个智能体制作解决方案
- 其中46个是开源的
- 其中 32 个是用 Python 编写的
- 其中 15 个是 Python 包（其余的在专用服务器上运行）

到目前为止，我已经用七种不同的框架重写了技术写作代理：

- 代理开发者工具包（谷歌）
- Agno
- 原子智能体
- 自动生成（微软）
- DSPy
- 朗格图
- Pydantic 人工智能

## 你为什么选择技术写作代理进行评估？

技术撰写代理 **回答有关 GitHub 仓库的简单英语问题** 。

你给它一个简短的内容，它就会生成一份报告。

它解决了如何在无需创建不同工具的情况下回答广泛问题的难题。例如

- 架构师： **给我一份代码库的概述**
- 新手入门： **给我一份新手入门指南**
- 发布工程： **部署此代码涉及哪些方面？**

这些问题都可以由同一个智能体回答： **在过去，这些问题需要编写非常不同且复杂的脚本** ，或者花费大量人工查看时间。

所以技术写作代理是一个非常简单且非常有用的绝佳组合。

## 我学到了什么？

对于像我这样的技术文案撰写者这样的简单智能体来说，智能体框架很有用，但并非必不可少。

在诸如交互式聊天或多智能体支持等更复杂的场景中，它们的强大功能可能会发挥作用，我将在未来的《制作人工智能智能体》系列文章中对此进行探讨。

为了解释我的选择，让我回顾一下智能体的基本组成部分。

## 智能体的构建模块

![](https://makingaiagents.substack.com/p/%7B%22src%22:%22https://substack-post-media.s3.amazonaws.com/public/images/654d42ad-7d87-45e2-bbc4-1edca9d752b9_1024x1536.png%22,%22srcNoWatermark%22:null,%22fullscreen%22:null,%22imageSize%22:null,%22height%22:1536,%22width%22:1024,%22resizeWidth%22:416,%22bytes%22:3362686,%22alt%22:null,%22title%22:null,%22type%22:%22image/png%22,%22href%22:null,%22belowTheFold%22:true,%22topImage%22:false,%22internalRedirect%22:%22https://makingaiagents.substack.com/i/166298130?img=https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F654d42ad-7d87-45e2-bbc4-1edca9d752b9_1024x1536.png%22,%22isProcessing%22:false,%22align%22:null,%22offset%22:false})

智能体的3个基本构建模块，湿婆木雕版本

智能体有三个基本组成部分：

- 语言模型
- 它调用的工具
- Memory

因此，一个优秀的智能体框架能轻松搞定以下三件事：

- **语言模型** ：合适的语言模型取决于具体用例：它们并非一劳永逸。 **切换模型有多容易？**
- **工具** ：理想情况下，我只需将智能体指向我的 Python 函数即可。 **我能否毫无麻烦地使用日常的 Python 函数？**
- **内存** ：除非不可避免，否则我无需担心智能体如何记住其行动。 **我是否必须为智能体如何管理其内存而烦恼？**

当智能体能很好地回答这三个问题时，它们编写代码时也需要更少的代码量。

为此，在我最初选择的 7 个中，表现突出的智能体制作工具是 **DSPy** 和 **Agno** ，两者都非常紧凑且灵活。

## 我最终选定了什么？

最终给每个智能体都增添了一点复杂性的一条规则是一条严格的规则： **“尽可能使用通用函数和常量”。**

看，我有这样一个想法，通过设置一些标准的东西来对这些框架更公平：

- 标准提示
- 标准工具

结果这是一件喜忧参半的事：

- 输入和输出格式确实略有不同，所以有时智能体需要进行比通常所需更多一点的包装
- 然而，它确实确保了启用.gitignore 的分层文件搜索的复杂功能能够一致地工作，并且提示信息（大多）是相同的。

此外，我在执行方面进行了标准化：它们都使用 uv，这是 Python 包管理方面的新热门工具。Uv 是正确的选择：它速度极快，并且很容易创建隔离的代理环境以避免任何潜在冲突。

## 我是如何对它们进行排名的？

所有框架都有其优缺点。

虽然我用一个非常简单的用例测试了这些框架，但这足以让我了解它们各自的设计理念。

一端是“尽可能简洁”，另一端是“尽可能类型安全”。（我个人的观点是，“尽可能简洁”更符合 Python 的习惯用法。）

![](https://makingaiagents.substack.com/p/%7B%22src%22:%22https://substack-post-media.s3.amazonaws.com/public/images/ecca8452-cc01-48a7-993e-7462b3ae94d5_928x1392.png%22,%22srcNoWatermark%22:null,%22fullscreen%22:null,%22imageSize%22:null,%22height%22:1392,%22width%22:928,%22resizeWidth%22:502,%22bytes%22:120251,%22alt%22:null,%22title%22:null,%22type%22:%22image/png%22,%22href%22:null,%22belowTheFold%22:true,%22topImage%22:false,%22internalRedirect%22:%22https://makingaiagents.substack.com/i/166298130?img=https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fecca8452-cc01-48a7-993e-7462b3ae94d5_928x1392.png%22,%22isProcessing%22:false,%22align%22:null,%22offset%22:false})

我将我评估的七个分成了四大类：

- 超低摩擦
- 低摩擦
- 完全可以接受
- 更高的摩擦

有很糟糕的吗？它们大多都没什么问题，只是我发现 Atomic Agents 那种类型安全的冗长是我不想再经历的。

那么，对于我的用例来说，这些框架的价值体现在哪里呢？

### 超低摩擦

- DSPy 2.6.17：超级简洁。
- Agno 1.5.10：紧凑；甚至可以更紧凑

### 低摩擦

- Autogen 0.6.1：硬编码的 LLM 支持

### 完全可以接受

- 谷歌 ADK 0.1.0：谷歌的偏见对其造成损害
- LangGraph 0.4.8：复杂工具定义
- Pydantic-AI 0.2.16b：复杂工具定义

### 更高的摩擦

- 原子智能体：针对我的用例而言设计过度

## 谷歌智能体开发者工具包

[浏览我实验性聊天机器人的源代码](https://reports.makingaiagents.com/) 。

这个框架大约有115行代码，是一个易于使用的简洁框架：

- 它体积小巧，并且可以选择具备服务器功能，以便使用可视化工具将代理作为服务器运行。
- 作为一个更大的可视化/服务器解决方案的一部分：虽然它可以在没有服务器的情况下独立运行，但默认情况下显然是打算作为服务器运行的。它也是对微软的 Autogen 的回应，提供了一个非常强大的基于网络的工作室工具。我预计在未来几个季度会在这方面开展大量工作，可能会进一步与谷歌开发生态系统中的其他工具集成（比如 [aistudio.google.com](http://aistudio.google.com/) 、 [jules.google](https://jules.google/) 以及其他各种工具）。
- 另请注意，该智能体代码中有大约 10 行是我认为对于理解 ADK 所呈现的新概念有必要添加的注释。

缺点很轻微：

- 烦人之处在于：它没有访问语言模型的标准方式，对于 Gemini 是一种方式，而对其他所有模型又是另一种方式，所以才有了我的“stupid\_hack\_to\_get\_model()”函数。对我来说，这只是徒增不必要的麻烦。
- 它稍微复杂一些，因为它需要会话的概念来保存内存。这与许多其他完全封装会话概念的智能体形成对比。我尊重这种抽象，但就我的用例而言，除了将它们传递回更多 ADK API 之外，实际上没有必要使用这些概念，因此考虑一种不需要会话或用户 ID 的更高级别产品可能是有价值的。

## Agno

[浏览我实验性聊天机器人的源代码](https://reports.makingaiagents.com/)

Agno 只有 72 行代码，是我目前编写的技术写作代理中最紧凑、最简洁的实现。

如果有一种通用的方式，能够使用许多框架和工具所支持的新兴格式来实例化语言模型，将供应商和模型 ID 用斜杠或冒号分隔，例如“openai:gpt-4.1-mini”或“anthropic/claude-sonnet-4.0”（就像 LangChain、LiteLLM 和 OpenRouter 等所支持的那样），那么它还可以变得更加紧凑。

就目前而言，Agno 要求针对每个供应商使用特定的类，由于我的代码以字符串作为输入，所以我有一个 ModelFactory 包装器来直接进行这种操作。

为什么阿格诺要这么做？我认为这里对语言模型的使用方式存在误解。

它们绝对不是一种一劳永逸的解决方案：人工智能工程的日常工作是针对特定用例评估一系列模型，所以从不同供应商那里获取一组不同的模型是完全正常的。我很少会完全坚定地使用某一种特定的语言模型——即使在实际操作中，我可能也想…… （原文最后不完整）

## 原子智能体

[浏览我实验性聊天机器人的源代码](https://reports.makingaiagents.com/)

这是目前为止使用起来最麻烦的框架，代码量约为224行，具有讽刺意味的是，它最大的卖点之一却是“极其轻量级”。

它严重依赖于 Instructor 和 Pydantic 这两个非常值得尊敬的框架，以帮助实现类型安全和数据完整性，为此我尊重它们的方法。

然而，在编写智能体时，这绝对是最麻烦的方法，例如，对于单个工具规范需要使用单独的类。

老实说，到了某个程度，这真的开始让人感觉它正从 Python 惯用法转向更重量级的东西，比如 Java。

另一个大麻烦是它将提示拆分成不同的方面，这感觉像是繁琐的工作，因为最终它只是将所有内容重新拼接成一段文本。如果你想要强类型的输入和输出，可以看看 DSPy，它在这方面做得非常优雅和简洁。

## Autogen

[浏览我实验性聊天机器人的源代码](https://reports.makingaiagents.com/)

这个实现有124行代码，处于中等水平。

Autogen 实际上是最早的一批智能体框架之一，它还有一个非常全面的 Autogen Studio，我在之前的一期中简要介绍过。

其大语言模型（LLM）的实现完全依赖于支持 OpenAI API 协议的供应商（几乎所有供应商都支持），但存在一个不幸的限制，即只能使用它特别列出的一个子集。

依赖 OpenAI 的 API 是完全合理的做法，我也很希望看到它更加开放，以便更灵活地支持其他模型和供应商。

最后，它的工具支持也相当轻量级；我只需要给工具添加异步包装器，其他方面它们就能正常工作。

## DSPy

[浏览我实验性聊天机器人的源代码](https://reports.makingaiagents.com/)

我将 DSPy 排在我的排名前列，考虑到它本身并非首要的专用代理框架，这相当了不起。

它与众不同之处在于，与其他的不同，它并非“只是一个 LLM 包装器”。

它有一种全新的指定提示的方法，之后，利用操作数据，可以使用非常复杂的优化技术对其进行优化。

这个解决方案只有99行代码，非常简洁，原因如下：

- 它可以直接将任何 Python 函数用作工具
- 它使用 LiteLLM 进行大语言模型（LLM）实例化，因此它直接接受“<供应商>/<模型ID>”组合
- 与 Atomic Agents 一样，它在底层使用 Pydantic 进行类型化输入和输出，但也能做到极其简洁。
- 它内置了一个 ReAct 智能体

唯一的难点在于我认为这近乎“文档字符串滥用”：DSPy 将文档字符串用作提示的功能来源。

这看起来可能不错，但实际上，a) 文档字符串不是代码的功能部分，实际上应该 *仅* 用于记录行为，并且 b) 因此，使用外部变量作为提示有点像一种变通方法。

为此，该文件的25行内容是我通用工具中定义的提示的重复。另一种实现方式可以这样做：

`class.__doc__ = <TECH_WRITER_SYSTEM_PROMPT>`

… 但这很不正规，如果你把它看作一个普通的 DSPy 程序，你可能会奇怪它为什么没有提示。

## 朗格图

[浏览我实验性聊天机器人的源代码](https://reports.makingaiagents.com/)

这个框架大约有155行代码，对于技术文档撰写的用例来说，它也是一个不错的框架，能让事情保持简单，原因如下：

- 它内置了一个 ReAct 智能体
- 它支持供应商/型号配置字符串

不过工具的使用门槛可以更低。

老实说，我的 Python 水平还不足以理解为什么这是个问题，但与大多数其他框架不同的是，Langgraph 工具在工具运行的上下文方面有额外的复杂性。

这相当于一个相当轻量级的包装器，用于传递正在扫描的目录。

我真的试图弄明白为什么 Langgraph 不能像其他框架那样直接解决这个问题，而是维持原样。

也许一位合适的 Python 从业者或 Langgraph 专家可以改进这一点。

## Pydantic 人工智能

[浏览我实验性聊天机器人的源代码](https://reports.makingaiagents.com/)

Pydantic AI 来自令人惊叹的类型安全/对象关系映射库 Pydantic 的创建者。

我尝试用 Pydantic AI 编写技术文档，最终代码量略多，约有 123 行。

这不是最轻量级框架之一的唯一原因是它定义工具的特定方式：

- Python 方法需要 `@<agent_name>.tool ` 注解
- 另外，它还需要一个 RunContext 参数来传递正在分析的代码目录。

再说一次，对于 Langgraph，我对 Python 的作用域规则了解得还不够，以至于不明白为什么在其他框架不需要额外包装器的情况下它却需要，但是这会带来稍高的使用难度和认知负担，因为你必须理解什么是 RunContext 以及为什么需要它。

## 其他 Python 智能体制作框架

未来我希望能介绍一下目前我找到的其余 8 个 Python 包代理制作工具：

- [Ag2](https://ag2.ai/)
- [代理栈](https://github.com/AgentOps-AI/AgentStack)
- [蜜蜂人工智能](https://github.com/i-am-bee/beeai-framework) （国际商业机器公司）
- [骆驼人工智能](https://github.com/camel-ai/camel)
- [CrewAI](https://crewai.com/)
- [格利普泰普](https://github.com/griptape-ai/griptape)
- [语义内核](https://github.com/microsoft/semantic-kernel) （微软，多语言）
- [轻量级智能体](https://github.com/huggingface/smolagents) （HuggingFace）

## 其他 Python 智能体制造商

此外，还有大约 15 个其他的开源 Python 解决方案，据我所知，它们仅作为独立服务器提供。我也会在某个时候对这些进行评估，但许多方案不容易编写脚本，评估起来会复杂得多：

- [Agent-S](https://github.com/simular-ai/Agent-S)
- [智能体世界](https://github.com/OpenBMB/AgentVerse)
- [Archon](https://github.com/coleam00/Archon)
- [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT)
- [鹿流](https://github.com/bytedance/deer-flow) （字节跳动）
- [dify](https://dify.ai/)
- [julep](https://julep.ai/)
- [Letta](https://github.com/cpacker/MemGPT)
- [parlant](https://github.com/emcie-co/parlant)
- [pippin](https://github.com/pippinlovesyou/pippin)
- [potpie](https://github.com/potpie-ai/potpie)
- [pyspur](https://github.com/PySpur-Dev/pyspur) （多语言）
- [rowboat](https://github.com/rowboatlabs/rowboat)
- [suna](https://github.com/kortix-ai/suna)
- [超级通用人工智能](https://github.com/TransformerOptimus/SuperAGI)
- [零号智能体](https://github.com/frdel/agent-zero)

## TypeScript 智能体开发者

在 Python 之外，第二大开源智能体制作语言是 TypeScript。

- [BaseAI](https://github.com/LangbaseInc/BaseAI)
- [Flowise](https://github.com/FlowiseAI/Flowise)
- [Motia](https://github.com/MotiaDev/motia)
- [N8n](https://github.com/n8n-io/n8n)
- [开放式](https://github.com/Aident-AI/open-cuak)

## 其他语言

有适用于 PHP、Ruby、Go 和 Rust 的代理框架。我会适时探索这些框架。