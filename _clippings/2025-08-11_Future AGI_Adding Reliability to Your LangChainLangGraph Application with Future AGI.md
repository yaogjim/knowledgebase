---
title: "Adding Reliability to Your LangChain/LangGraph Application with Future AGI"
source: "https://docs.futureagi.com/cookbook/cookbook13/Adding-Reliability-to-Your-LangChain-LangGraph-Application-with-Future%20AGI"
author:
  - "[[Future AGI]]"
published: 2025-08-11
created: 2025-08-11
description:
tags:
  - "Future AGI {{\"extract tags  with # in Chinese\"}}"
---
了解如何通过集成 Future AGI 的可观测性框架来提高你的 LangChain/LangGraph 应用程序的可靠性

## Introduction

LLM 应用程序通常依赖于检索数据、调用工具并响应用户查询的智能体。这有时可能会导致不可预测的行为。确保此类应用程序在生产环境中的每个响应都是完整、有依据且可靠的，已变得至关重要。 随着这些应用程序的复杂性不断增加，仅仅返回一个答案已经不够了。开发人员需要了解每个响应是如何生成的、使用了哪些工具、检索了哪些数据以及如何做出决策。这种透明度对于调试、监控以及随着时间的推移提高此类应用程序的可靠性至关重要。 本教程展示了如何通过使用 Future AGI 的检测 SDK 将评估和可观测性纳入到你的 LangChain 或 LangGraph 应用程序中，从而为你的 LLM 应用程序增加可靠性。

## Methodology

在本教程中，我们专注于构建和评估一个工具增强的语言模型（LLM）智能体，该智能体能够如图 1 所示，利用其内部知识和实时网络搜索来回答用户查询。目标不仅仅是生成回复，还要基于相关指标系统地监控和评估回复的质量。![Fig 1: Framework for evaluating LangChain chatbot using Future AGI](https://mintlify.s3.us-west-1.amazonaws.com/futureagi/cookbook/cookbook13/images/fig1.png)

Fig 1: Framework for evaluating LangChain chatbot using Future AGI

要实现这一点，我们将使用 LangGraph 构建一个对话代理，它将 OpenAI 的模型与作为工具的 [谷歌搜索 API](https://python.langchain.com/docs/integrations/tools/google_search/) 相结合。该代理接收用户查询，然后决定是可以直接回答，还是需要进行网络搜索以获取最新信息。当需要该工具时，它会进行实时谷歌搜索，并将结果用于其回复中。 为了监控智能体在每一步的行为，我们将使用 Future AGI 的 `traceAI-langchain` Python 包，它会记录模型推理、工具使用和响应的详细跟踪信息。然后，会针对诸如完整性、有根据性、幻觉以及工具的正确使用等质量方面对这些跟踪信息进行评估。完整性确保答案能充分解决用户的查询，有根据性验证响应是否基于检索到的证据，幻觉检测标记无根据或编造的内容，工具使用评估检查智能体是否正确调用外部工具并正确整合结果。这些指标共同帮助开发者构建不仅智能，而且可靠、可解释且适合生产的智能体。

## 安装所需的包

```
pip install fi-instrumentation

pip install traceAI-langchain

pip install openai

pip install langgraph

pip install langchain

pip install langchain-openai

pip install langchain-core

pip install langchain-community

pip install langchain-google-community

pip install google-api-python-client
```

## 导入所需的包

## 设置环境

- 点击 [此处](https://python.langchain.com/docs/integrations/tools/google_search/) 了解如何获取你的 `GOOGLE_API_KEY` 和 `GOOGLE_CSE_ID`
- 点击 [此处](https://platform.openai.com/account/api-keys) 以访问你的 `OPENAI_API_KEY`
- 点击 [此处](https://app.futureagi.com/dashboard/keys) 以获取您的 `FI_API_KEY` 和 `FI_SECRET_KEY`

```
os.environ["GOOGLE_CSE_ID"] = "google_cse_id"

os.environ["GOOGLE_API_KEY"] = "google_api_key"

os.environ["OPENAI_API_KEY"] = "openai_api_key"

os.environ["FI_API_KEY"] = "fi_api_key"

os.environ["FI_SECRET_KEY"] = "fi_secret_key"

os.environ["FI_BASE_URL"] = "https://api.futureagi.com"
```

## 为 LangGraph 项目添加监测工具

这是为你的 LLM 应用程序添加追踪的过程。追踪有助于你监控关键指标，如成本、延迟和评估结果。 在一个跨度表示执行流程中的单个操作（记录输入输出数据、执行时间和错误）的情况下，一个追踪将多个跨度连接起来以表示请求的完整执行流程。 对此类项目进行监测需要三个步骤：
1. **设置评估标签：** 为了评估跟踪记录，我们将使用 Future AGI 提供的适当评估模板。由于我们正在处理基于工具的聊天机器人代理，我们将根据以下这些指标来评估代理的行为：
	- **完整性：** 评估回复是否完整地回答了输入的查询。
	- **有根有据性：** 评估回复是否牢固地基于所提供的输入上下文。
	- **大语言模型函数调用：** 评估输出是否正确识别工具调用的需求以及是否准确包含该工具。
	- **检测幻觉：** 评估模型是否编造了事实或添加了输入中不存在的信息。
	虽然这些是我们在本教程中决定使用的指标，但 Future AGI 支持 50 多种预构建的评估模板，具体取决于不同的用例，比如如果你想评估模型的回答在给定上下文中的符合程度，就可以使用上下文符合度模板；如果你想衡量检索到的文档的有用性，就可以使用上下文检索质量模板等等。如果现有的模板不符合你的用例，你也可以创建自定义评估。 根据你应用程序的要求，还可以纳入其他指标，如实性准确性、块归属或文体质量，以提供更全面的评估。 **`eval_tags`** 列表包含多个 **`EvalTag`** 实例。每个 **`EvalTag`** 代表一个在运行时要应用的特定评估配置，封装了评估过程所需的所有参数。
	- **`类型 ` ：** 指定评估标签的类别。在本烹饪书中，使用的是 **`EvalTagType.OBSERVATION_SPAN`** 。
	- **`value`** ：定义评估标签所涉及的操作类型。
		- **`EvalSpanKind.AGENT`** 表示评估目标是涉及智能体的操作。
		- **`EvalSpanKind.TOOL`** ：用于涉及工具的操作。
	- **`eval_name`** ：要执行的评估的名称。
	- **`config`** ：用于为评估提供特定配置的字典。空字典表示将使用默认配置参数。
	- **`mapping`** ：此字典将评估所需的输入映射到操作的特定属性。
	- **`custom_eval_name`** ：特定评估实例的用户定义名称。
	> 点击 [**此处**](https://docs.futureagi.com/future-agi/products/prototype/evals) 了解有关 Future AGI 提供的评估的更多信息
2. 设置追踪提供程序：追踪提供程序是 traceAI 生态系统的一部分，traceAI 是一个开源软件包，可实现对人工智能应用程序和框架的追踪。它与 OpenTelemetry 协同工作，以监控跨不同模型、框架和供应商的代码执行情况。要配置一个 `trace_provider` ，我们需要将以下参数传递给 `register` 函数：
	- **`project_type`** ：指定项目类型。在这里，使用 **`ProjectType.EXPERIMENT`** ，因为评估设置更倾向于对聊天机器人的发现和评估进行实验。
	- **`项目名称 `** ：项目的用户定义名称。
	- \*\* ` 项目版本名称：` \*\*用于跟踪不同实验运行的项目版本名称。
	- **`eval_tags`** ：一个评估标签列表，用于定义要应用的特定评估。
3. **设置 LangChain 监测器：** 这样做是为了与 LangChain 框架集成，以收集遥测数据。在 **`LangChainInstrumentor`** 实例上调用 **`instrument`** 方法。此方法负责使用提供的 **`tracer_provider`** 来设置 LangChain 框架的监测。

## 创建 LangGraph 应用程序

我们首先使用\`GoogleSearchAPIWrapper\`设置一个\*\*谷歌搜索工具\*\*。该工具充当外部数据源，代理在需要当前信息时可以调用它。然后，我们将\`ChatOpenAI\`与\`gpt-4o-mini\`模型一起使用，并将其绑定到搜索工具。 在 LangGraph 中，智能体逻辑中的每一步都表示为图中的一个 **节点** 。每个节点处理一项特定任务，应用程序根据对话的当前状态从一个节点移动到另一个节点。在我们的聊天机器人中，我们定义了三个主要节点：
- **智能体节点：** 这是主要的推理步骤。它接收当前对话历史，可选择包含过去的工具结果，并生成回复或触发工具调用。
- **工具节点：** 如果智能体请求使用工具，此节点将执行谷歌搜索，并将结果附加到对话上下文中。它还会记录中间交互过程。
- **最终节点：** 如果不再需要其他工具，此节点将完成答案并返回给用户。
然后，一个 `路由器` 函数会检查智能体是否请求了某个工具。如果请求了，流程会转移到工具节点。如果没有，智能体则直接进入最终节点以生成响应。这使得智能体能够根据查询动态地做出决策。 然后，我们使用 `StateGraph` 将所有节点组合成一个完整的图。随着对话的进行，这个图会跟踪消息历史和工具结果。最后，我们通过在一些示例查询上运行聊天机器人来对其进行测试。

```
# Google Search Tool

search = GoogleSearchAPIWrapper()

google_tool = Tool(

    name="google_search",

    description="Use this to search Google for current events or factual knowledge.",

    func=search.run

)

# LLM bound to tool

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0).bind_tools([google_tool])

# LangGraph State

State = Annotated[dict, MessagesState]

# Node 1: Agent node

def agent_node(state: State) -> State:

    messages = state["messages"]

    steps = state.get("intermediate_steps", [])

    tool_msgs = format_to_openai_tool_messages(steps)

    response = llm.invoke(messages + tool_msgs)

    return {

        "messages": messages + [response],

        "intermediate_steps": steps

    }

# Node 2: Tool handler

def tool_node(state: MessagesState) -> MessagesState:

    messages = state["messages"]

    tool_call = messages[-1].tool_calls[0]

    tool_name = tool_call["name"]

    args = tool_call.get("args") or json.loads(tool_call.get("arguments", "{}"))

    result = google_tool.invoke(args)

    tool_msg = ToolMessage(tool_call_id=tool_call["id"], content=str(result))

    return {

        "messages": messages + [tool_msg],

        "intermediate_steps": state.get("intermediate_steps", []) + [(messages[-1], tool_msg)]

    }

# Node 3: Final responder

def final_node(state: State) -> State:

    response = llm.invoke(state["messages"])

    return {"messages": state["messages"] + [response]}

# Router

def router(state: State) -> str:

    msg = state["messages"][-1]

    if getattr(msg, "tool_calls", None):

        return "tool"

    return "final"

# Graph assembly

graph = StateGraph(MessagesState)

graph.add_node("agent", agent_node)

graph.add_node("tool", tool_node)

graph.add_node("final", final_node)

graph.set_entry_point("agent")

graph.add_conditional_edges("agent", router, {

    "tool": "tool",

    "final": "final"

})

graph.add_edge("tool", "agent")

graph.add_edge("final", END)

memory = MemorySaver()

app = graph.compile(checkpointer=memory)

example_queries = [

    "Who won the 2024 Nobel Prize in Physics?",

    "Who won Game of the Year at The Game Awards 2024?",

    "When was GPT-4o released by OpenAI?"

]

# Run the agent with multiple queries

for i, query in enumerate(example_queries):

    print(f"\n\nQUERY {i+1}: {query}\n")

    config = {"configurable": {"thread_id": f"multi-tool-agent-{i}"}}

    input_messages = [HumanMessage(content=query)]

    output = app.invoke({"messages": input_messages}, config)

    output["messages"][-1].pretty_print()

    print("\n" + "--"*50)
```

图 2 将 LangGraph 执行层次结构显示为一棵树，它以树的形式呈现，展示了完整的调用栈。它从 **智能体** 节点开始，该节点使用 GPT-4o-mini 模型（ `ChatOpenAI` ）来解释用户的查询。模型决定使用 **工具节点** ，该节点使用 LangChain 的包装器执行谷歌搜索（ `google_search` ）。获取结果后，控制权再次返回给 **智能体节点** 以解释工具响应。最后，系统到达 **最终节点** ，该节点生成输出。底部面板显示了跨度级别所使用评估的结果。![Fig 2: Future AGI dashboard for visualising traces and evals](https://mintlify.s3.us-west-1.amazonaws.com/futureagi/cookbook/cookbook13/images/fig2.png)

Fig 2: Future AGI dashboard for visualising traces and evals

图3展示了所有跨度的汇总视图，包括平均延迟、令牌使用情况和成本，以及评估分数。这些分数能让人快速了解智能体行为的质量。在这个例子中，智能体在工具调用、幻觉和有根据性方面的通过率达到了100%，这表明工具使用正确、事实准确且上下文基础扎实。然而，完整性分数仅为50%，这表明一些回答没有完全解决用户的问题。![Fig 3: Aggregated scores of evals](https://mintlify.s3.us-west-1.amazonaws.com/futureagi/cookbook/cookbook13/images/fig3.png)

Fig 3: Aggregated scores of evals

## Conclusion

在本教程中，我们展示了如何通过将 OpenAI 的模型与谷歌搜索 API 相结合，构建一个基于 LangGraph 的值得信赖且可靠的对话代理。为确保透明度和可靠性，我们集成了 Future AGI 的评估和追踪框架。这使我们能够自动捕获详细的执行跟踪信息并评估代理的行为。

## 准备好让你的 LangChain 应用程序具备可靠性了吗？

使用 Future AGI 的可观测性框架，自信地开始评估您的 LangChain/LangGraph 应用程序。Future AGI 提供您构建可靠、可解释且可投入生产的应用程序所需的工具。 立即点击 [**此处**](https://futureagi.com/contact-us) 与我们预约演示！
