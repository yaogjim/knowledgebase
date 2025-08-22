---
title: "Agentic Workflows"
source: "https://cobusgreyling.medium.com/agentic-workflows-034d2df458d3"
author:
  - "[[Cobus Greyling]]"
published: 2025-08-22
created: 2025-08-22
description: "I used an AI research API to analyse emerging trends and identify those on the rise versus in decline. Agentic Workflows bridge the gap between traditional RPA — which is often brittle, inflexible…"
tags:
  - "Cobus Greyling"
---
[Sitemap](https://cobusgreyling.medium.com/sitemap/sitemap.xml)

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*5_sEIENHpBfmNC-SDFM_qg.png)

## 一个笔记本、函数调用、智能工作流与检索增强生成

我使用了一个人工智能研究应用程序编程接口来分析新兴趋势，并识别哪些趋势正在上升，哪些正在下降。

令人惊讶的是，对 ***人工智能代理*** 的兴趣正在减弱，而有两个领域正在兴起：

1. 先进的研究和推理能力，以及
2. **Agentic Workflows.**

**智能代理工作流** 弥合了传统机器人流程自动化（RPA）与成熟的人工智能智能体之间的差距。传统 RPA 往往脆弱、缺乏灵活性且严格预先设定，而人工智能智能体的自主程度可能让人感觉难以承受。

**智能工作流** 实现了一种理想的平衡：

- 它们为应用程序提供了一个基础模板，在定义的边界内实现自主性
- 以及传统机器人流程自动化（RPA）严重缺乏的适应性和自主性。

当然，在我能够以最简单的形式实现它之前，所有这些对我来说都还只是理论上的。

所以，我发现了这个很棒的 **LangChain** 笔记本，它用简单易懂的方式展示了几个 URL 是如何在 Chroma 中被索引的……以及 RAG 查找是如何被配置为一个函数调用的。

这种设置允许大语言模型（LLM）通过决定是否调用检索增强生成（RAG）函数，在 **智能体工作流** 中引入一层自主性。

你可以轻松设想扩展此过程，以纳入代理工作流程可用的多个工具和功能。

就个人而言，我认为函数调用没有得到应有的重视或未被充分理解……但它确实是一种在保持一定程度可控性的同时增强适应能力的有效方法。

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*v2peI59ykoc_n8mVL7KNDg.png)

This is the pattern or workflow of the notebook shared in this article. It is based on LangChain’s LangGraph and provides a template for the Agentic Workflow, without introducing rigidity or brittleness.

## Agentic Workflow

代码中的 LangGraph 部分是代理工作流的一个明显示例。

我将逐步剖析这一点，包括使其具有\*\*智能体特性\*\*的因素，以及结构化的\*\*流程\*\*如何促成这种分类。

## 什么是代理工作流？

人工智能中的 **智能体工作流** 是指一个动态的、迭代的过程，其中一个或多个人工智能智能体（通常由大语言模型驱动）做出自主决策，如推理、规划和行动（调用工具或确定路径）。

> 与僵化的线性管道不同，工作流允许基于智能体的输出实现灵活性、循环和条件分支。

它们通常涉及编排框架来管理状态、持久性和多步骤交互，从而实现更具协作性和可优化的人工智能行为。

> 智能代理工作流提供了一种平衡的自主性水平——比传统的机器人流程自动化（RPA）更具适应性，但比完全的人工智能智能体受到的约束更少，后者在没有明确边界的情况下可能表现出过度的独立性。

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*pYl9EqaEt2dig8_tP1l3ig.png)

## LangGraph 如何融入智能工作流

LangGraph 专门设计为一个有状态的编排框架，用于构建和部署此类工作流，尤其是那些涉及人工智能代理的工作流。

它将流程表示为图形，其中节点（ *一个 LLM 智能体或工具执行* ）和边（ *条件路由* ）定义了流程。

这种基于图的结构支持诸如持久性、流处理和调试等功能，使其非常适合智能体应用程序。

LangGraph 通常用于创建多智能体或单智能体设置，其中 LLM 可以充当“路由器”来动态决定下一步操作。

## 为什么这段特定的代码是一个示例

## The Flow Aspect

这段代码使用 **LangGraph** 来定义一个有向图，该图具有表示智能体（LLM 调用）和工具（检索器执行）的节点，并通过边连接。

条件边创建一个分支流，如果大语言模型（LLM）输出工具调用，它会路由到工具节点；否则，它就结束。

这种结构化流程将简单的大语言模型（LLM）调用转变为工作流，它不仅是顺序执行的，而且具有适应性和状态性（跨步骤跟踪消息）。

## The Agentic Element

这里的 LLM 充当一个代理，它通过函数调用（工具调用）来 ***决定*** 路径。

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*AxqUPSkdXP9oYer2PqAp9g.png)

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*HbEQ8Xd8VpdutR_eUhIIEQ.png)

## Data Store

该笔记本使用向量存储（具体来说是 Chroma）来存储文档嵌入以供检索。

例如，来自相关 LangGraph RAG 教程和示例的代码片段显示：

```c
vectorstore = Chroma.from_documents(
    documents=doc_splits,
    embedding=OpenAIEmbeddings(),
)
```

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*At0VYdgmCoUExm59hkUnnQ.png)

## 作为路由器的函数调用

这段代码有效地说明了大语言模型（LLM）在函数调用（ *工具调用* ）中的作用，它是 LangGraph 工作流程中的一个决策点或 *路由* 机制。

## 通过函数调用进行路由的关键示例

## LLM as Router

大语言模型（LLM）与工具绑定。在 *调用模型函数* 时，它会处理输入消息并决定是否要：

- 直接回复（不使用工具，流程结束）。
- 通过函数调用调用工具（在其响应中输出 tool\_calls，路由到“tools”节点）。

这个决策隐含在模型的输出中……如果响应包含工具调用（一个工具调用列表），则图会相应地进行路由；否则，它就结束。

因此，此设置展示了一个带有 RAG 的智能工作流程，其中模型根据需求进行动态路由（ *如果信息缺失则检索，否则进行响应* ），与静态管道相比，增强了灵活性。

## Working Notebook

```c
# Install required packages
!pip install -U --quiet langchain-community tiktoken langchain-openai langchainhub chromadb langchain langgraph langchain-text-splitters

import getpass
import os

# Set OpenAI API key
if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = getpass.getpass("OPENAI_API_KEY:")

# Optional: Set LangSmith for tracing (comment out if not needed)
# if "LANGCHAIN_API_KEY" not in os.environ:
#     os.environ["LANGCHAIN_API_KEY"] = getpass.getpass("LANGCHAIN_API_KEY:")
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_PROJECT"] = "Agentic RAG"

# Load documents and create vectorstore
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

urls = [
    "https://lilianweng.github.io/posts/2023-06-23-agent/",
    "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
    "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
]

docs = [WebBaseLoader(url).load() for url in urls]
docs_list = [item for sublist in docs for item in sublist]

text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=100, chunk_overlap=50
)
doc_splits = text_splitter.split_documents(docs_list)

vectorstore = Chroma.from_documents(
    documents=doc_splits,
    collection_name="rag-chroma",
    embedding=OpenAIEmbeddings(),
)
retriever = vectorstore.as_retriever()

# Create retriever tool
from langchain.tools.retriever import create_retriever_tool

retriever_tool = create_retriever_tool(
    retriever,
    "retrieve_blog_posts",
    "Search and return information about Lilian Weng blog posts on LLM agents, prompt engineering, and adversarial attacks on LLMs.",
)

tools = [retriever_tool]

# Agent state
from typing import Sequence
from typing_extensions import Annotated, TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]

# Call model (highlight: this is where the agent decides to use the tool or not via function calling)
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Use a more reliable model to avoid the error
llm = ChatOpenAI(model="gpt-4o-mini", streaming=True)

# Bind tools
llm = llm.bind_tools(tools)

# Define a system prompt to guide the agent
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that answers questions using the provided tools when necessary. Think step-by-step."),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

def call_model(state: AgentState):
    # Invoke the chain with the messages
    chain = prompt | llm
    response = chain.invoke({"messages": state["messages"]})
    
    # Print the LLM's decision on tool use
    if response.tool_calls:
        tool_names = [tool_call['name'] for tool_call in response.tool_calls]
        print(f"LLM decided to use tool(s): {', '.join(tool_names)}")
    else:
        print("LLM decided not to use any tool.")
    
    # The agent appends the response to the messages
    return {"messages": [response]}

# Tool execution
from langgraph.prebuilt import ToolNode

tool_node = ToolNode(tools)

# Define the graph
from langgraph.graph import END, StateGraph, START
from langgraph.prebuilt import tools_condition

workflow = StateGraph(AgentState)

workflow.add_node("agent", call_model)
workflow.add_node("tools", tool_node)

workflow.add_edge(START, "agent")

# Highlight: Tool selection portion - the conditional edge decides if tool is needed based on the agent's response
# If the agent message has tool_calls, it goes to "tools", else to END
workflow.add_conditional_edges(
    "agent",
    tools_condition,
    {"tools": "tools", END: END},
)

workflow.add_edge("tools", "agent")

graph = workflow.compile()

# Print out the graph
from IPython.display import Image, display

display(Image(graph.get_graph().draw_mermaid_png()))

# Example run to illustrate
import pprint

inputs = {
    "messages": [
        HumanMessage(
            content="What are the types of agent memory based on Lilian Weng's blog post?"
        )
    ]
}
for output in graph.stream(inputs):
    for key, value in output.items():
        pprint.pprint(f"Output from node '{key}':")
        pprint.pprint("---")
        pprint.pprint(value, indent=2, width=80, depth=None)
    pprint.pprint("\n---\n")
```

打印出的图表：

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*v2peI59ykoc_n8mVL7KNDg.png)

This is the pattern or workflow of the notebook shared in this article. It is based on LangChain’s LangGraph and provides a template for the Agentic Workflow, without introducing rigidity or brittleness.

## Output

## 步骤 1：LLM 对工具使用的决策

大语言模型决定使用工具：检索博客文章

**节点“代理”的输出**

```c
{
  'messages': [
    AIMessage(
      content='',
      additional_kwargs={
        'tool_calls': [
          {
            'index': 0,
            'id': 'call_Vw9cswL1anFHbjKpbC9gPB1N',
            'function': {
              'arguments': '{"query":"agent memory types"}',
              'name': 'retrieve_blog_posts'
            },
            'type': 'function'
          }
        ]
      },
      response_metadata={
        'finish_reason': 'tool_calls',
        'model_name': 'gpt-4o-mini-2024-07-18',
        'system_fingerprint': 'fp_560af6e559',
        'service_tier': 'default'
      },
      id='run--26f85d0e-5f70-4df5-a46a-231775f6c08d-0',
      tool_calls=[
        {
          'name': 'retrieve_blog_posts',
          'args': {'query': 'agent memory types'},
          'id': 'call_Vw9cswL1anFHbjKpbC9gPB1N',
          'type': 'tool_call'
        }
      ]
    )
  ]
}
```

**节点“工具”的输出**

```c
{
  'messages': [
    ToolMessage(
      content='Memory stream: is a long-term memory module (external database) that records a comprehensive list of agents’ experience in natural language.\n\nEach element is an observation, an event directly provided by the agent.\n- Inter-agent communication can trigger new natural language statements.\n\n\nRetrieval model: surfaces the context to inform the agent’s behavior, according to relevance, recency and importance.\n\nThe design of generative agents combines LLM with memory, planning and reflection mechanisms to enable agents to behave conditioned on past experience, as well as to interact with other agents.\n\nCategorization of human memory.\n\nWe can roughly consider the following mappings:\n\nSensory memory as learning embedding representations for raw inputs, including text, image or other modalities;\nShort-term memory as in-context learning. It is short and finite, as it is restricted by the finite context window length of Transformer.\nLong-term memory as the external vector store that the agent can attend to at query time, accessible via fast retrieval.\n\nTable of Contents\n\n\n\nAgent System Overview\n\nComponent One: Planning\n\nTask Decomposition\n\nSelf-Reflection\n\n\nComponent Two: Memory\n\nTypes of Memory\n\nMaximum Inner Product Search (MIPS)\n\n\nComponent Three: Tool Use\n\nCase Studies\n\nScientific Discovery Agent\n\nGenerative Agents Simulation\n\nProof-of-Concept Examples\n\n\nChallenges\n\nCitation\n\nReferences',
      name='retrieve_blog_posts',
      id='1f7c3034-8de4-4031-9429-35d2941edba9',
      tool_call_id='call_Vw9cswL1anFHbjKpbC9gPB1N'
    )
  ]
}
```

## 步骤 2：LLM 对工具使用的决策

大语言模型决定不使用任何工具。

**节点“代理”的输出**

```c
{
  'messages': [
    AIMessage(
      content="According to Lilian Weng's blog post, the types of agent memory can be categorized as follows:\n\n1. **Memory Stream**: \n - This serves as a long-term memory module (external database) that records a comprehensive list of the agent's experiences in natural language. Each entry represents an observation or event directly provided by the agent. Inter-agent communication can trigger new natural language statements.\n\n2. **Retrieval Model**: \n - This model surfaces the context that informs the agent's behavior based on relevance, recency, and importance. It helps agents behave conditioned on past experiences and interact with other agents.\n\n3. **Categorization of Human Memory**: \n - This can be roughly mapped as:\n - **Sensory Memory**: Involves learning embedding representations for raw inputs, such as text and images.\n - **Short-term Memory**: Represents in-context learning; it is short and finite due to the limitations of the Transformer’s context window length.\n - **Long-term Memory**: Comprises an external vector store that the agent can access via fast retrieval at query times.\n\nThese memory types facilitate various functionalities and behaviors in agent systems.",
      additional_kwargs={},
      response_metadata={
        'finish_reason': 'stop',
        'model_name': 'gpt-4o-mini-2024-07-18',
        'system_fingerprint': 'fp_560af6e559',
        'service_tier': 'default'
      },
      id='run--143b529d-6abb-409d-bda7-3c6e1eaef1a9-0'
    )
  ]
}
```
![](https://miro.medium.com/v2/resize:fit:640/format:webp/0*1_3GXs4jXpAV3Up2.png)

[***首席传道官***](https://www.linkedin.com/in/cobusgreyling/) ***@*** [*科雷人工智能公司*](https://blog.kore.ai/cobus-greyling/the-shifting-vocabulary-of-ai//?utm_medium=OrganicSocial&utm_source=Medium&utm_campaign=CobusPostFeed&utm_term=Medium22112024) *| 我热衷于探索人工智能与语言的交叉领域。语言模型、人工智能智能体、智能应用程序、开发框架以及塑造未来的数据驱动工具。*
