---
title: "Langchain Open Deep Research Internals: A Step-by-Step Architecture Guide"
source: "https://www.bolshchikov.com/p/open-deep-research-internals-a-step"
author:
  - "[[Sergey Bolshchikov]]"
date: "2025-12-09T17:47:43+08:00"
created: 2025-12-09
description: "A detailed walkthrough of Langchain Open Deep Research's architecture, showing how state evolves, agents coordinate, and design patterns combine at each execution step."
tags:
  - "Sergey Bolshchikov"
---
### 《Langchain Open Deep Research 架构详解》：逐步展示各执行阶段的状态演变、智能体协作机制以及设计模式的融合应用。

这篇博文与众不同，它深入剖析了 Open Deep Research 的内部运作机制，揭示了其如何通过特定设计模式成为顶尖开源深度研究智能体的核心奥秘。

这篇帖子与其他资源有何不同？

1. LangChain 的 GitHub 仓库和博客文章仅提供了关于工作原理的高层次解释。
2. LangSmith 和 LangGraph Studio 并未完全公开所有细节——难以捕捉每一步的状态以及图的动态调用过程。因此，在执行过程的每个步骤中都难以把握全局情况。
3. 要深入理解这一过程，必须扎实掌握反思代理机制、工具使用设计模式以及基础递归原理。

本文篇幅较长，请做好阅读准备。我们将首先明确开放深度研究的整体设计框架，随后解析实现过程中几个关键的设计模式。最后，我们将通过一个实例逐步深入剖析，观察开放深度研究图谱及其状态在每一步的演进过程。

## 设计理念

我猜你已经读过官方 LangChain 博客中关于 Open Deep Research 构建方式的介绍。不过为了确保大家理解一致，我们还是快速浏览一下整体架构。

![Open Deep Research High Level Architecture](https://substackcdn.com/image/fetch/$s_!XMDf!,w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcab9689f-4ed4-49c6-aeb0-bdd195bb3a26_2776x596.png)

开放式深度研究架构 \[4\]

智能体在概念上包含三个主要部分：范围界定、研究探索和最终报告。任何您想要构建的设计变体，很可能都会包含这三个组成部分。

范围界定阶段的目标是为研究阶段构建输入。在开放深度研究中，这包括一个用户澄清循环——LLM 判断是否需要向用户寻求澄清——然后生成简报。

若您自行设计代理程序，此处可进行用户提示优化或运用其他技术以提升用户输入质量。

简报生成后，便进入研究阶段。这是核心工作展开的环节，后续我们会详细探讨，但简而言之，它包含两个阶段：监督者与研究子智能体。监督者基于简报内容并通过反思，按需生成多个研究子智能体，每个子智能体负责特定的子任务。各子智能体（子图）接收专属主题后展开研究，并将摘要反馈给监督者。当监督者反思研究结果并判定已收集足够数据时，所有信息将移交至记者环节。

记者将收集到的所有信息进行整合，生成最终结果。若结果体量过大，可在此处生成文件成品（如 Claude 的操作方式）替代纯文本输出。

## Prior Knowledge

要真正理解 Open Deep Research 的运作机制，我们需要单独剖析其中贯穿使用的几种模式。它采用的并非如今已成为标准的经典 ReACT 模式。

### Reflection Pattern

![AI Agent Reflection Design Pattern](https://substackcdn.com/image/fetch/$s_!3Nns!,w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2d9d46d-6256-43b4-b156-25d1c9e17b1f_2813x1605.png)

反射设计模式

反思模式使智能体能够评估自身输出，并利用反馈迭代优化回答。该模式中，大语言模型首先生成初始响应，随后扮演自我批判者评估输出质量。基于这种自我审视，智能体会生成改进版本，循环此过程直至达到质量标准或满足终止条件。这种自我修正循环让智能体得以摆脱纯粹反应式思维定式，转向更审慎、更有条理的问题解决路径。

### Tool Use Pattern

![AI Agent Tool Use Design Pattern](https://substackcdn.com/image/fetch/$s_!yjQe!,w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc0d91040-73b4-468a-ba4f-9be465db8106_3083x1605.png)

工具使用设计模式

工具调用模式是理解 Open Deep Research 架构的核心基础。虽然它看起来与标准工具调用类似，但关键差异使其能够实现更复杂的智能体行为。

#### 标准工具调用（ReACT）

在经典的 ReACT 架构中，工具调用是直截了当的：

```markup
@tool
def search_web(query: str) -> str:
    “”“Search the web for information.”“”
    return tavily_search(query)

# LangGraph automatically:
# 1. Detects the tool call in LLM response
# 2. Executes the function
# 3. Adds result to message history
# 4. Continues to next LLM call
```

这对于简单工具来说效果很好，但在处理复杂操作时存在局限性。

#### 手动工具使用模式

Open Deep Research 采用了一种不同的方法—— **人工工具编排** 。以下是其缘由与实现方式：

**Why is this needed?**

1. **复杂操作** ：当某个“工具”实际在生成完整子图（如研究子智能体）时，您需要更精细的控制
2. **内存管理** ：工具返回的结果可能非常庞大（例如完整的研究报告）。将所有内容都添加到消息历史中会导致上下文窗口过度膨胀
3. **自定义路由逻辑** ：根据业务逻辑可能需要以不同方式处理工具执行
4. **并行执行** ：同时启动多个子代理需要手动协调

**How it works:**

1. **定义工具模式但不实现具体功能：**
```markup
class ConductResearch(BaseModel):
    “”“Tool definition for spawning a research sub-agent.”“”
    topic: str = Field(description=”The research topic to investigate”)
    
# Note: This is just a schema - no actual function implementation
```
1. **将模式绑定到 LLM：**
```markup
llm_with_tools = llm.bind_tools([ConductResearch, ThinkTool, ResearchComplete])
```
1. **LLM 返回结构化工具调用：** 当 LLM 决定“使用”某个工具时，它会返回：
```markup
AIMessage(
    content=”I’ll research this topic now”,
    tool_calls=[
        {
            “name”: “ConductResearch”,
            “args”: {”topic”: “machine learning frameworks”},
            “id”: “call_abc123”
        }
    ]
)
```
1. **你手动处理工具执行：**
```markup
# Check if LLM wants to call a tool
if message.tool_calls:
    for tool_call in message.tool_calls:
        if tool_call[”name”] == “ConductResearch”:
            # Spawn a research sub-agent (a whole subgraph!)
            result = await research_subgraph.ainvoke({
                “research_topic”: tool_call[”args”][”topic”]
            })
            
            # Return a compact confirmation, not the full result
            return ToolMessage(
                content=f”Research completed on {tool_call[’args’][’topic’]}”,
                tool_call_id=tool_call[”id”]
            )
```

**开放式深度研究的关键优势：**

- **子图调用** ：监督者可将完整的研究子智能体作为“工具”进行生成
- **上下文效率优化** ：不再将长达万词的研究报告存入消息历史，而是返回简洁的"研究已完成"提示信息
- **灵活路由** ：您可将不同的工具调用路由至不同的子图或处理器
- **并行协调** ：同时启动多个研究子代理，每个代理拥有独立的上下文环境

**权衡之处：** 你失去了自动化工具执行的能力，但获得了对执行时机、方式和内容的精细控制。这种控制在像开放深度研究这样复杂的多智能体架构中至关重要，因为这里的“工具”实际上是具有独立状态管理的完整推理子图。

## 深入浅出逐步指南

既然我们已经掌握了必要的知识，并对 Open Deep Research 的设计理念有了高层次的理解，现在该是深入探究的时候了。

最佳描述方式是通过逐步演示一个实例，观察深度研究智能体的整体图谱和状态在每一步如何变化。

每一步都配有相应的图像，展示该步骤下的图谱状态以及 LangGraph 状态对象（绿色高亮部分）。

### 第一步：用户提问

![](https://substackcdn.com/image/fetch/$s_!6vWd!,w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faed0f871-2e72-42ff-9498-717fc6583d0f_2165x1736.png)

第一步：用户提出问题

一切始于用户提问。LLM 通过结构化输出判断是否需要向用户寻求澄清。若需要，则返回相应的布尔值及后续问题发送给用户。此阶段的状态很简单：仅包含消息数组。

### 第二步：用户回应澄清性问题

![](https://substackcdn.com/image/fetch/$s_!jNeU!,w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2d52bd31-cfb0-4a86-903e-c2d01c7f0256_2195x1900.png)

第二步：用户回答澄清问题

当用户回复时，深度开放研究会对消息数组再次调用 LLM。它可能会再次要求澄清，或返回包含以下内容的结构化输出：

```markup
{
  need_verification: false,
  verification: “Thank you…”
}
```

其中 `need_verification` 表示我们是否应继续联系简报撰写人。

```markup
response = await clarification_model.ainvoke([HumanMessage(content=prompt_content)])
if response.need_clarification:
    # End with clarifying question for user
    return Command(
        goto=END,
        update={”messages”: [AIMessage(content=response.question)]}
    )
else:
    # Proceed to research with verification message
    return Command(
        goto=”write_research_brief”,
        update={”messages”: [AIMessage(content=response.verification)]}
    )
```

### 第三步：生成简报并提交给主管

![](https://substackcdn.com/image/fetch/$s_!1pha!,w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6ac00173-d342-4642-94c2-47a2fd2b9d5a_2429x2714.png)

第三步：智能体生成简报

现在我们调用 LLM 生成研究简报，这次使用不同的提示语。返回的结果将存入状态中。

我们还会为监督子图准备初始状态，该状态存储在内部的 `supervisor_messages` 中，并以系统提示和刚刚生成的摘要作为起始内容。

### 第四步：主管反思任务简报

![](https://substackcdn.com/image/fetch/$s_!2oqg!,w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2917c1f5-794e-4be0-81bc-ac927cc44e61_5419x3067.png)

第四步：主管对收到的简报进行反思

现在进入复杂环节。监督者拥有独立的系统提示词和三个工具定义： `think_tool` 、 `conduct_research` 与 `research_complete` 。需要特别指出我们之前描述的模式——这些仅是定义而非实际实现。监督者节点监听 LLM 调用，并自行执行工具调用。

首先调用 `think_tool` （反思模式）来理解应该执行什么操作，结果存储在 `supervisor_messages` 中。监督器还会检查已进行的调用次数（ `research_iterations` ），如果超过预设最大值则停止执行；否则研究可能会无限期持续下去。

### 第五步：监督者启动研究

![](https://substackcdn.com/image/fetch/$s_!XOTP!,w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd1e90284-af6c-4beb-8041-83377b1ceaa3_5861x3502.png)

第五步：主管启动调研

当首次反思被记录时，监督器会调用 LLM，LLM 将返回一个带有主题的 `conduct_research` 工具调用。它可能会返回多个 `conduct_research` 工具；在这种情况下，监督器将并行生成多个子代理，每个代理负责一个特定主题。

### 第六步：启动研究子代理

![](https://substackcdn.com/image/fetch/$s_!zD66!,w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feb0733f2-72aa-48ac-bc15-8e6bb5737448_5052x4712.png)

第六步：监督代理启动研究子代理

研究子代理是一个基于 `conduct_research` 工具中 LLM 响应动态调用的子图，因此在 LangGraph Studio 中不可见。它包含三个核心节点： `researcher` 、 `research_tools` 和 `compress_research` 。研究工具可配置，通常包含与监督工具逻辑相同的 `think_tool` 、搜索功能、MCP 服务器以及 `research_complete` 工具。作为子图，它拥有独立的状态，包含从监督者接收的消息和 `research_topic` 。与监督者类似，每个工具调用都会在状态中被追踪，并受最大迭代次数限制。

### 第七步：研究代理启动搜索

![](https://substackcdn.com/image/fetch/$s_!9k_8!,w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc301688f-517a-4227-9d10-07495bacd542_5724x4712.png)

第七步：研究代理启动搜索

这一步操作简明直接。研究节点使用系统提示词和从监督者处获取的研究主题，向大语言模型发起调用。随后它会收到一个指向 `web_search` 的工具调用指令，其中包含需要执行的一系列查询请求。

### 步骤八：研究代理执行多重搜索

![](https://substackcdn.com/image/fetch/$s_!RVX0!,w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdbd145aa-9b8f-45ae-8bff-92c8ef224cf8_6204x4715.png)

第八步：研究代理执行搜索

Open Deep Research 采用 Tavily 搜索并并行发起多个搜索，每个查询对应研究员节点接收到的请求。考虑到搜索结果可能体量庞大，在搜索工具返回结果前会先进行摘要处理，随后将摘要存储至状态中的 `researchers_messages` 字段。

### 第九步：研究成果反思

![](https://substackcdn.com/image/fetch/$s_!4F7V!,w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F027ca5b0-62a5-45e9-8a49-2883ee34bbe6_5732x4712.png)

第九步：研究代理对搜索结果进行反思

与研究主管类似，研究节点会调用 `think_tool` 来反思接收到的搜索结果，并决定这些结果是否足够，或者是否需要继续搜索。

### 步骤10：研究完成

![](https://substackcdn.com/image/fetch/$s_!1v7R!,w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F04fc00a3-af98-41b2-b98b-54cf677a342a_5717x4712.png)

步骤10：研究智能体完成调研

若 `think_tool` 的执行结果显示研究已获取充分信息，研究节点将调用 `research_complete` 工具并跳转至 `compress_research` 节点。由于搜索结果可能体量庞大，此时需对结果进行压缩处理，最终将精简后的内容返回给监督模块。

### 步骤11：重新评估研究计划

![](https://substackcdn.com/image/fetch/$s_!Vh_6!,w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2f31a757-5d97-41e9-b368-f76561c8caea_5859x3055.png)

步骤11：监督代理对研究成果进行反思

当收到研究子代理的结果时，就像完成了一次工具调用。我们将结果存入状态，并向 LLM 明确 `conduct_research` 已完成。监督器根据其系统提示调用 `think_tool` 来理解下一步该做什么。

### 步骤12：研究完成

![](https://substackcdn.com/image/fetch/$s_!5Bsv!,w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3d5b22cd-9ae3-4e87-b1a0-1ae2f1cb4a02_5859x3441.png)

步骤12：智能体完成整体研究

此时，反思表明监督者已为用户所请求的研究收集到足够信息， `research_complete` 工具被调用来完成此子图的执行。

### 步骤13：生成最终报告

![](https://substackcdn.com/image/fetch/$s_!GrPd!,w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8fff8b36-2080-451e-b499-e5084157f9d0_5150x2076.png)

步骤13：智能体生成最终报告

当所有子图完成时，当前状态包含消息历史、 `supervisor_messages` 、任务简报和研究成果。最后一步是调用 LLM 生成最终报告并返回给用户。

## References

1. [https://www.philschmid.de/agentic-pattern#reflection-pattern](https://www.philschmid.de/agentic-pattern#reflection-pattern)
2. [https://www.philschmid.de/agentic-pattern#tool-use-pattern](https://www.philschmid.de/agentic-pattern#tool-use-pattern)
3. [https://blog.langchain.com/reflection-agents/](https://blog.langchain.com/reflection-agents/)
4. [https://github.com/langchain-ai/open\_deep\_research](https://github.com/langchain-ai/open_deep_research)
5. [https://blog.langchain.com/open-deep-research/](https://blog.langchain.com/open-deep-research/)