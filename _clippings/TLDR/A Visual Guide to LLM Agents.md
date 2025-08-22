---
title: "A Visual Guide to LLM Agents"
source: "https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-llm-agents"
author:
  - "[[Maarten Grootendorst]]"
published: 2024-02-19
created: 2025-03-26
description: "Explore the main components of what makes LLM Agents special."
tags:
  - "clippings"
---
### 探索单智能体和多智能体的主要组件Exploring the main components of Single- and Multi-Agents

LLM 智能体正变得越来越普遍，似乎正在取代我们所熟悉的“常规”对话。LLM 这些令人惊叹的能力并非轻易就能创造出来，需要许多组件协同工作。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc3177e12-432e-4e41-814f-6febf7a35f68_1360x972.png)

在这篇文章中有 60 多个自定义视觉效果，你将探索LLM智能体领域、它们的主要组件，并探讨多智能体框架。

## 什么是LLM代理？

要了解什么是LLM智能体，让我们首先探索一下LLM的基本能力。传统上，LLM所做的不过是下一个标记预测。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F495cca88-574b-4ace-b785-d6d6746e8f81_1500x504.png)

通过连续采样许多标记，我们可以模拟对话并使用LLM来对我们的查询给出更详尽的回答。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6cc95dc7-b956-425c-a548-3f1f9f3f4fd1_1500x260.png)

然而，当我们继续“对话”时，任何给定的LLM都会展现出其主要缺点之一。它不记得对话！

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F969ff525-cab0-419e-9d83-3d85c1acfbe9_1716x544.png)

还有许多其他任务是LLMs经常做不好的，包括像乘法和除法这样的基本数学运算：

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fff414a39-4acb-4762-b902-433e5c8aadf1_1592x464.png)

这是否意味着LLMs很糟糕？绝对不是！LLMs无需具备所有能力，因为我们可以通过外部工具、内存和检索系统来弥补它们的劣势。

通过外部系统，可以增强LLM的功能。Anthropic 将此称为“增强版LLM”。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4d245ca0-e18a-4b40-91d6-9d7247f2b83f_1332x584.png)

例如，当面对一道数学题时，LLM可能会决定使用合适的工具（计算器）。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F56ec0862-cffb-45cc-a8d3-aa0581719d2d_1592x464.png)

那么这个“增强版LLM”就是一个智能体吗？不，也许有点像……

让我们从智能体的定义开始：1

智能体是指任何可以被视为通过传感器感知其环境并通过执行器对该环境采取行动的事物。  
  
— 拉塞尔与诺维格，《人工智能：一种现代方法》（2016 年）

智能体与它们的环境进行交互，并且通常由几个重要组件组成：

- 环境 —— 智能体与之交互的世界
- 传感器 — 用于观测环境
- 执行器 — 用于与环境交互的工具
- 执行器 —— 决定如何从观察结果转化为行动的 “大脑” 或规则

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5f575b4a-783e-4ca5-be3f-c9ef7086b0da_1180x608.png)

此框架用于与各种环境进行交互的各类智能体，例如与物理环境交互的机器人或与软件交互的人工智能智能体。

我们可以稍微推广一下这个框架，使其更适合“增强版LLM”。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe5cdee7c-ac55-4185-95fb-d88cc6395bf0_1180x608.png)

使用“增强型”LLM，智能体可以通过文本输入观察环境（因为LLMs通常是文本模型），并通过使用工具（如搜索网络）执行某些操作。

为了选择要采取的行动，LLM智能体有一个至关重要的组成部分：它的规划能力。为此，LLMs需要能够通过思维链等方法进行“推理”和“思考”。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7cc4d8b1-bb2b-45f1-a17e-a53357d3d999_1228x1004.png)

有关推理的更多信息，请查看《推理视觉指南》LLMs

使用这种推理行为，LLM智能体将规划出需要采取的必要行动。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8bebdfdf-74f8-4a3b-a54f-b7d643e97f63_1156x588.png)

这种规划行为使智能体能够理解当前情况（LLM）、规划下一步行动（规划）、采取行动（工具）并跟踪已采取的行动（记忆）。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcece7ade-43c2-497a-8e78-e61cfcf467ac_1032x720.png)

根据系统的不同，你可以使用具有不同自主程度的LLM代理。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F98d5ce2c-e9ba-4f67-bc11-e62983f890a1_1736x1140.png)

根据询问的对象不同，一个系统由LLM决定其行为方式的程度越高，就越具有“自主性”。

在下文中，我们将通过LLM智能体的三个主要组件：内存、工具和规划，介绍各种自主行为的方法。

## Memory

LLMs 是健忘的系统，或者更准确地说，在与它们交互时根本不会进行任何记忆。

例如，当你向一个LLM提问，然后接着问另一个问题时，它不会记住前一个问题。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7c6d3e7a-5cc0-440e-a3d6-3ddee9cd73f0_1032x568.png)

我们通常将此称为短期记忆，也称为工作记忆，它作为（近乎）即时上下文的缓冲区。这包括LLM智能体最近采取的行动。

但是，LLM 代理还需要跟踪可能多达数十个步骤，而不仅仅是最近的操作。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd93050da-f962-426c-87bc-9742b896e008_1320x888.png)

这被称为长期记忆，因为理论上LLM智能体可能需要记住几十甚至几百步。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F81dfc42c-2cbd-4a1d-9430-4ac2518d4490_936x696.png)

让我们探索一些赋予这些模型记忆的技巧。

## 短期记忆

启用短期记忆最直接的方法是使用模型的上下文窗口，它本质上是一个LLM能够处理的标记数量。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3512b33d-3987-41b9-8ab5-4db78718d6e1_1032x460.png)

上下文窗口往往至少有 8192 个词元，有时可以扩展到数十万词元！

大上下文窗口可用于跟踪完整的对话历史记录，作为输入提示的一部分。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F66e6afca-afc6-4a3f-a4b0-4d11e050c558_1204x616.png)

只要对话历史记录在LLM的上下文窗口范围内，这种方法就有效，并且是模仿记忆的一种好方法。然而，我们并不是真正记住对话，而是基本上“告诉”LLM那段对话是什么。

对于上下文窗口较小的模型，或者当对话历史较长时，我们可以改用另一个LLM来总结到目前为止发生的对话。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F11f97b1d-737b-4843-b8a3-4ad1ac24b173_1320x812.png)

通过持续总结对话，我们可以保持此对话的规模较小。它将减少标记数量，同时仅跟踪最重要的信息。

## 长期记忆

LLM智能体中的长期记忆包括该智能体过去的动作空间，这些动作空间需要在较长时间内保留。

一种实现长期记忆的常见技术是将所有以前的交互、动作和对话存储在外部向量数据库中。

要构建这样一个数据库，首先要将对话嵌入到能够捕捉其含义的数字表示形式中。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8420e846-ec02-4101-a0c1-ad9ba1d4a4d7_1028x660.png)

构建数据库后，我们可以嵌入任何给定的提示，并通过将提示嵌入与数据库嵌入进行比较，在向量数据库中找到最相关的信息。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F47304195-33bd-4637-b18e-ad7c57c8aa2c_1028x756.png)

这种方法通常被称为检索增强生成（RAG）。

长期记忆还可能涉及保留来自不同会话的信息。例如，你可能希望一个LLM代理记住它在之前会话中所做的任何研究。

不同类型的信息也可以与要存储的不同类型的记忆相关联。在心理学中，有许多类型的记忆需要区分，但《语言智能体的认知架构》这篇论文将其中四种与LLM智能体联系起来。2

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa56c3d15-e512-4bf3-9815-d42cc01ccfa1_1204x416.png)

这种区分有助于构建能动框架。语义记忆（关于世界的事实）可能存储在与工作记忆（当前和近期情况）不同的数据库中。

## Tools

工具允许给定的LLM与外部环境（如数据库）进行交互，或使用外部应用程序（如运行的自定义代码）。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9dfac69b-7b8a-4eee-ad04-8a06ea3be617_1272x176.png)

工具通常有两种用例：获取数据以检索最新信息，以及采取行动，如安排会议或订购食物。

要实际使用一个工具，LLM必须生成符合给定工具 API 的文本。我们倾向于期望能格式化为 JSON 的字符串，以便能轻松地输入到代码解释器中。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F87b42a6f-87a8-4057-8975-969293f73bb2_1460x420.png)

请注意，这不仅限于 JSON，我们还可以在代码本身中调用该工具！

你还可以生成 LLM 可以使用的自定义函数，比如一个基本的乘法函数。这通常被称为函数调用。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8152f4a2-34d4-40ee-8445-25b4eed4b179_1460x364.png)

一些LLMs如果得到正确且广泛的提示，就可以使用任何工具。使用工具是大多数当前LLMs都能够做到的事情。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F20f31f7e-cce9-4c5f-bf94-f46eb635f700_1460x304.png)

一种更稳定的访问工具的方法是通过微调LLM（稍后会详细介绍！）。

如果代理框架是固定的，工具可以按照给定的顺序使用……

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F36192526-b953-4f5a-a2fa-9bde40a827ef_1624x648.png)

…或者LLM可以自主选择使用哪种工具以及何时使用。LLM智能体，就像上面的图片一样，本质上是LLM调用的序列（但具有对动作/工具等的自主选择）。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F36870bf2-e0e5-42d7-bcdc-45b1a1ab7c15_1520x556.png)

换句话说，中间步骤的输出会反馈到LLM中以继续处理。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb5d354e0-d89b-417f-9df7-ffe40985852d_1460x568.png)

## 工具变形器

工具使用是一种强大的技术，可用于增强LLMs的能力并弥补其缺点。因此，在过去几年中，关于工具使用和学习的研究工作迅速涌现。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0f533a89-9af8-482c-aac6-f1806801b725_1284x820.png)

《基于大语言模型的工具学习综述》论文的注释和裁剪图片。随着对工具使用的关注度不断提高，（智能体）LLMs有望变得更加强大。

这项研究的大部分内容不仅涉及提示LLMs使用工具，还专门针对工具使用对它们进行训练。

最早这样做的技术之一叫做 Toolformer，这是一个经过训练以决定调用哪些 API 以及如何调用的模型。3

它通过使用 `  [  ` 和 ` ]` 标记来指示调用工具的开始和结束来做到这一点。当给出一个提示，例如“5 乘以 3 等于多少？”时，它开始生成标记，直到到达 `  [  ` 标记。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4f2fe527-6e4c-45b6-bfcf-ff34c4672c01_1592x208.png)

之后，它会生成令牌，直到到达 `  →  ` 令牌，该令牌表示 LLM 停止生成令牌。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F43bbc573-bebc-4057-82f8-6718be598770_1592x312.png)

然后，该工具将被调用，其输出将被添加到目前为止生成的标记中。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4d88be14-0d49-433c-a2c6-ab0e96b041c0_1592x348.png)

`] ` 符号表示 LLM 现在可以在必要时继续生成。

Toolformer 通过精心生成一个包含许多模型可以训练的工具使用情况的数据集来创建这种行为。对于每个工具，手动创建一个少样本提示，并用于采样使用这些工具的输出。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F20cdf6b6-47d7-4ffd-bc51-b1cb38500bbe_1460x1068.png)

输出根据工具使用的正确性、输出以及损失减少情况进行过滤。所得数据集用于训练一个LLM以遵循这种工具使用格式。

自 Toolformer 发布以来，出现了许多令人兴奋的技术，如可以使用数千个工具的LLMs（ToolLLM 4）或可以轻松检索最相关工具的LLMs（Gorilla 5）。

无论哪种方式，大多数当前的LLMs（2025 年初）都已被训练为通过 JSON 生成轻松调用工具（如我们之前所见）。

## 模型上下文协议（MCP）

工具是智能体框架的重要组成部分，它允许LLMs与外界进行交互并扩展其能力。然而，当你有许多不同的 API 时，启用工具使用会变得很麻烦，因为任何工具都需要：

- 手动跟踪并输入到LLM
- 手动描述（包括其预期的 JSON 模式）
- 每当其 API 发生变化时手动更新

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4392e0ed-f13e-4f6c-9b26-7804498a94ae_1624x828.png)

为了让工具在任何给定的智能体框架中更易于实现，Anthropic 开发了模型上下文协议（MCP）。6 MCP 为天气应用程序和 GitHub 等服务的 API 访问进行了标准化。

它由三个组件组成：

- MCP 主机 — LLM 管理连接的应用程序（如光标）
- MCP 客户端 —— 与 MCP 服务器保持一对一连接
- MCP 服务器 — 为 LLMs 提供上下文、工具和功能

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F24c1c103-b26f-4fb2-8089-6a5b0696a99f_1624x764.png)

例如，假设你希望某个给定的LLM应用程序总结来自你的仓库的 5 个最新提交。

MCP 主机（与客户端一起）首先会调用 MCP 服务器询问有哪些可用工具。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2ecb19e6-53fd-414e-a729-dab86c43b189_1624x780.png)

LLM接收信息并可能选择使用工具。它通过主机向 MCP 服务器发送请求，然后接收结果，包括所使用的工具。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7bf83696-db99-437a-bd3e-7c638f6445b6_1624x616.png)

最后，LLM接收结果并可以解析出给用户的答案。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F29c46b51-7d88-403e-8e47-2eb82e1bb6a7_1624x616.png)

此框架通过连接到任何LLM应用程序都可以使用的 MCP 服务器，使创建工具变得更加容易。因此，当你创建一个与 Github 交互的 MCP 服务器时，任何支持 MCP 的LLM应用程序都可以使用它。

## 规划

工具的使用使一个LLM能够增强其能力。它们通常通过类似 JSON 的请求来调用。

但是在一个智能体系统中，LLM 是如何决定使用哪一种工具以及何时使用呢？

这就是规划发挥作用的地方。LLM 智能体中的规划涉及将给定任务分解为可操作的步骤。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F39a6b7eb-0700-4cde-bbe3-59b6d99baee8_1460x540.png)

此计划允许模型反复思考过去的行为，并在必要时更新当前计划。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe521c2fc-6aee-435f-833f-8247b12d1e5d_1460x224.png)

我喜欢计划圆满达成的时刻！

要在LLM代理中启用规划功能，让我们首先看看这项技术的基础，即推理。

## 推理

规划可操作的步骤需要复杂的推理行为。因此，LLM必须能够在规划任务的下一步之前展示这种行为。

“推理”LLMs是指那些倾向于在回答问题之前“思考”的人。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8cdd114b-427f-454f-9e85-ee5d241d266f_1668x1060.png)

我使用“推理”和“思考”这两个术语时有点宽泛，因为我们可以争论这是类似人类的思考，还是仅仅将答案分解为结构化步骤。

这种推理行为大致可以通过两种选择来实现：微调LLM或进行特定的提示工程。

通过提示工程，我们可以创建LLM应遵循的推理过程示例。提供示例（也称为少样本提示 7）是引导LLM行为的好方法。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa05700ec-3ef5-4071-80b3-f97093196928_1480x748.png)

这种提供思维过程示例的方法称为思维链，它能够实现更复杂的推理行为。8

通过简单地说明“让我们一步一步地思考”，也可以在没有任何示例（零样本提示）的情况下启用思维链。9

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F028e3be4-f1f5-451a-b441-20fcae781aac_1648x280.png)

在训练一个LLM时，我们既可以给它提供足够数量的包含类似思维示例的数据集，也可以让LLM自行发现其思维过程。

一个很好的例子是 DeepSeek-R1，其中奖励被用来指导思维过程的使用。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5a85a363-4c76-4b73-8532-ffe863948882_1628x972.png)

有关“推理LLMs”的更多信息，请参阅我的可视化指南。

## 推理与行动

在LLMs中启用推理行为很棒，但这不一定使其能够规划可操作的步骤。

到目前为止，我们所关注的技术要么展示推理行为，要么通过工具与环境进行交互。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5e3d90c2-c007-4fef-a8df-176d68ae5fd6_1844x652.png)

例如，思维链纯粹专注于推理。

最早将这两个过程结合起来的技术之一称为 ReAct（推理与行动）。10

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fca0a3091-bcf9-4da6-9a28-242d82f12acf_1844x652.png)

ReAct 通过精心的提示工程来做到这一点。ReAct 提示描述了三个步骤：

- 思考 - 关于当前情况的一个推理步骤
- 操作 - 要执行的一组操作（例如，工具）
- 观察 - 关于行动结果的推理步骤

提示本身就相当直接明了。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F95450e98-4045-4fb6-b866-5aed129e5a7c_1404x824.png)

LLM 使用此提示（可用作系统提示）来引导其行为，使其以思考、行动和观察的循环方式工作。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F77b17db6-da65-4afb-a775-e6a939f1ea58_1900x1168.png)

它会持续这种行为，直到某个动作指定返回结果。通过遍历想法和观察结果，LLM 可以规划动作、观察其输出并相应地进行调整。

因此，与具有预定义和固定步骤的智能体相比，此框架使LLMs能够展现出更多自主能动行为。

## 反射

没有人，即使是使用 ReAct 的LLMs，也无法完美地完成每一项任务。只要你能反思这个过程，失败就是这个过程的一部分。

此过程在 ReAct 中缺失，这就是 Reflexion 发挥作用的地方。Reflexion 是一种使用语言强化来帮助智能体从先前失败中学习的技术。11

该方法假设有三个LLM角色：

- 智能体 —— 根据状态观察选择并执行动作。我们可以使用思维链或反应式行动等方法。
- 评估器 —— 对执行者产生的输出进行评分。
- 自我反思 —— 反思行动者采取的行动以及评估者生成的分数。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb22cf4df-37b1-4359-8417-084a77248232_1176x588.png)

内存模块用于跟踪行动（短期）和自我反思（长期），帮助智能体从错误中学习并确定改进的行动。

一种类似且精妙的技术被称为自我优化（SELF-REFINE），其中对输出进行优化和生成反馈的操作会不断重复。12

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F36c8b4af-5ca1-46e9-a5b6-e5ff94c8e32a_1484x580.png)

相同的LLM负责生成初始输出、优化输出和反馈。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6b713a88-5805-4e5b-984c-f377d2d59386_1736x652.png)

《自我优化：通过自我反馈进行迭代优化》论文的注释图。

有趣的是，这种自我反思行为，即 Reflexion 和 SELF-REFINE，与强化学习非常相似，在强化学习中，奖励是根据输出质量给出的。

## 多智能体协作

我们所探讨的单一智能体存在几个问题：工具过多可能会使选择变得复杂，上下文会变得过于复杂，并且任务可能需要专业化。

相反，我们可以关注多智能体，即多个智能体（每个智能体都可以使用工具、内存和规划）相互之间以及与它们的环境进行交互的框架：

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb028b7eb-eeec-492c-816b-1c0837be2b40_1228x716.png)

这些多智能体系统通常由专门的智能体组成，每个智能体都配备有自己的工具集，并由一个监督者进行监督。监督者管理智能体之间的通信，并可以向专门的智能体分配特定任务。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa15cb88d-c059-41dc-b658-f643ad076588_1228x504.png)

每个智能体可能有不同类型的可用工具，但也可能有不同的记忆系统。

在实践中，有几十种多智能体架构，其核心有两个组件：

- 智能体初始化 —— 单个（专门的）智能体是如何创建的？
- 代理编排 —— 所有代理如何进行协调？

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F17b03793-5c78-45d0-b79a-52901c288201_1228x652.png)

让我们探索各种有趣的多智能体框架，并重点介绍这些组件是如何实现的。

## 人类行为的交互式拟像

可以说，最具影响力且坦率地讲非常酷的多智能体论文之一是《生成式智能体：人类行为的交互式模拟》。13

在本文中，他们创建了模拟可信人类行为的计算软件代理，他们将其称为生成式代理。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd427f53c-35b9-4253-aa2a-8cd566e8b129_1156x252.png)

每个生成式智能体所具有的特征使其表现出独特的行为方式，并有助于创造出更有趣、更具动态性的行为。

每个智能体都由三个模块（记忆、规划和反思）初始化，这与我们之前在 ReAct 和 Reflexion 中看到的核心组件非常相似。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8a42fc17-5d98-40f4-a350-a2d4fe2f8890_1324x732.png)

内存模块是此框架中最重要的组件之一。它存储规划和反思行为，以及迄今为止的所有事件。

对于任何给定的下一步或问题，会检索记忆并根据其近期性、重要性和相关性进行评分。得分最高的记忆会与智能体共享。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe0746e39-a6d5-4a5c-9336-cae884f250d7_1496x1356.png)

《生成式智能体：人类行为的交互式模拟》论文的注释图

它们共同使得智能体能够自由地进行其行为并相互交互。因此，由于它们没有特定的工作目标，所以几乎没有智能体编排。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fffdf51e4-c348-46a5-94ed-3c3d091da550_2536x1052.png)

交互式演示中的带注释图像.

这篇论文中有太多令人惊叹的信息片段，但我想重点介绍一下他们的评估指标。14

他们的评估将智能体行为的可信度作为主要指标，由人类评估者对其进行打分。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F98b3af2a-bd4b-4d30-a83b-c9300c8df2ce_1076x716.png)

《生成式智能体：人类行为的交互式模拟》论文的注释图

它展示了观察、规划和反思在这些生成式智能体的表现中结合起来是多么重要。如前所述，没有反思行为，规划是不完整的。

## 模块化框架

无论你选择何种框架来创建多智能体系统，它们通常都由几个要素组成，包括其配置文件、对环境的感知、记忆、规划以及可用动作。15 16

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F16d08b46-3c57-434e-aa73-7a1e516305c7_1232x656.png)

用于实现这些组件的流行框架有 AutoGen 17、MetaGPT 18 和 CAMEL 19。然而，每个框架在处理每个智能体之间的通信方式上略有不同。

例如，使用 CAMEL 时，用户首先创建问题并定义人工智能用户和人工智能助手角色。人工智能用户角色代表人类用户，并将指导整个过程。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faa8b7a80-9b4e-402b-a0da-b6ae21e8464a_1232x236.png)

之后，人工智能用户和人工智能助手将通过相互交互来合作解决该查询。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6bcc2339-cf84-4099-915b-ccd1c7417ff9_1232x648.png)

这种角色扮演方法能够实现智能体之间的协作通信。

自动生成（AutoGen）和元 GPT（MetaGPT）有不同的通信方式，但归根结底都是这种协作性的通信本质。智能体有机会相互参与和交流，以更新它们当前的状态、目标和下一步行动。

在过去一年，尤其是过去几周，这些框架的增长呈爆发式。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fddc3ddb2-40f6-4e4a-b463-92bf902cda54_1044x700.png)

随着这些框架不断成熟和发展，2025 年将是真正令人兴奋的一年！

## 结论

这就是我们的LLM特工之旅的结束！希望这篇文章能让大家更好地了解LLM特工是如何构建的。

要查看与LLMs相关的更多可视化内容并支持本时事通讯，请查看我写的关于大语言模型的书！

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa0b260f5-da52-4186-bc06-fd22077b2737_590x768.jpeg)

本书官方网站。你可以在亚马逊上订购这本书。所有代码已上传到 GitHub.

1. 拉塞尔，S. J.，& 诺维格，P.（2016 年）。《人工智能：一种现代方法》。培生教育出版集团。
2. 萨默斯、西奥多等人。《语言智能体的认知架构》。《机器学习研究汇刊》（2023 年）
3. Schick, Timo, et al. "Toolformer: Language models can teach themselves to use tools." *Advances in Neural Information Processing Systems* 36 (2023): 68539-68551.  
	施克，蒂莫，等人。《Toolformer：语言模型可以自学使用工具》。《神经信息处理系统进展》36（2023）：68539 - 68551。
4. 秦宇佳等人。“Toolllm：助力大语言模型掌握 16000 多个现实世界的应用程序编程接口。”arXiv 预印本 arXiv:2307.16789（2023 年）。
5. 帕蒂尔，希希尔·G.，等人。《大猩猩：与大量应用程序编程接口相连的大语言模型》。《神经信息处理系统进展》37（2024）：126544 - 126565。
6. "推出模型上下文协议。" 安托 ropic 公司，www.anthropic.com/news/model-context-protocol。访问时间：2025 年 3 月 13 日。
7. 曼恩、本等人。《语言模型是少样本学习者》。arXiv 预印本 arXiv:2005.14165 1（2020 年）：3。
8. 魏，贾森等人。《思维链提示在大语言模型中引发推理》。《神经信息处理系统进展》35（2022）：24824 - 24837。
9. Kojima, Takeshi, et al. "Large language models are zero-shot reasoners." *Advances in neural information processing systems* 35 (2022): 22199-22213.  
	小岛秀夫等人。《大语言模型是零样本推理器》。《神经信息处理系统进展》35（2022）：22199 - 22213。
10. Yao, Shunyu, Zhao, Jeffrey, Yu, Dian, Du, Nan, Shafran, Izhak, Narasimhan, Karthik, and Cao, Yuan. *ReAct: Synergizing Reasoning and Acting in Language Models*. Retrieved from https://par.nsf.gov/biblio/10451467. *International Conference on Learning Representations (ICLR)*.  
	姚舜禹、赵杰弗里、余典、杜楠、伊扎克·沙夫兰、卡尔蒂克·纳拉西姆汉和曹原。ReAct：语言模型中推理与行动的协同。取自 https://par.nsf.gov/biblio/10451467。国际学习表征会议（ICLR）。
11. Shinn, Noah, et al. "Reflexion: Language agents with verbal reinforcement learning." *Advances in Neural Information Processing Systems* 36 (2023): 8634-8652.  
	辛恩，诺亚等人。《反思：基于言语强化学习的语言智能体》。《神经信息处理系统进展》36（2023）：8634 - 8652。
12. Madaan, Aman, et al. "Self-refine: Iterative refinement with self-feedback." *Advances in Neural Information Processing Systems* 36 (2023): 46534-46594.  
	马丹、阿曼等人。《自我精炼：基于自我反馈的迭代精炼》。《神经信息处理系统进展》36 卷（2023 年）：46534 - 46594 页。
13. Park, Joon Sung, et al. "Generative agents: Interactive simulacra of human behavior." *Proceedings of the 36th annual acm symposium on user interface software and technology*. 2023.  
	朴俊成等人。《生成式智能体：人类行为的交互式模拟》。第 36 届美国计算机协会用户界面软件与技术年度研讨会会议录。2023 年。
14. To see a cool interactive playground of the Generative Agents, follow this link: [https://reverie.herokuapp.com/arXiv\_Demo/](https://reverie.herokuapp.com/arXiv_Demo/)  
	要查看生成式智能体的酷炫交互式演示，请点击此链接：https://reverie.herokuapp.com/arXiv\_Demo/
15. Wang, Lei, et al. "A survey on large language model based autonomous agents." *Frontiers of Computer Science* 18.6 (2024): 186345.  
	王雷等人。“基于大语言模型的自主智能体综述”。《计算机科学前沿》18.6（2024）：186345。
16. Xi, Zhiheng, et al. "The rise and potential of large language model based agents: A survey." *Science China Information Sciences* 68.2 (2025): 121101.  
	习近平、智恒等。《基于大语言模型的智能体的兴起与潜力：一项综述》。《中国科学：信息科学》68 卷第 2 期（2025 年）：121101。
17. Wu, Qingyun, et al. "Autogen: Enabling next-gen llm applications via multi-agent conversation." *arXiv preprint arXiv:2308.08155* (2023).  
	吴青云等人。“Autogen：通过多智能体对话实现下一代llm应用程序。”arXiv 预印本 arXiv:2308.08155（2023 年）。
18. Hong, Sirui, et al. "Metagpt: Meta programming for multi-agent collaborative framework." *arXiv preprint arXiv:2308.00352* 3.4 (2023): 6.  
	洪思睿等人。“Metagpt：用于多智能体协作框架的元编程。”arXiv 预印本 arXiv:2308.00352 3.4（2023 年）：6。
19. Li, Guohao, et al. "Camel: Communicative agents for" mind" exploration of large language model society." *Advances in Neural Information Processing Systems* 36 (2023): 51991-52008.  
	李，国豪等人。《骆驼：用于大语言模型社会“思维”探索的交流智能体》。《神经信息处理系统进展》36（2023）：51991 - 52008。