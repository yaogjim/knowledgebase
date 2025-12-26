---
title: "Give an Engineer a Problem and He Will LangGraph the Solution"
source: "https://medium.com/@juan8arias/give-an-engineer-a-problem-and-he-will-langgraph-the-solution-2f330775b841"
author:
  - "[[Juan Felipe Arias Aguirre]]"
date: "2025-12-09T17:47:50+08:00"
created: 2025-12-09
description: "Give an Engineer a Problem and He Will LangGraph the Solution How I used a sledgehammer to crack a nut, and learned to love the graph along the way. It started with a simple, personal problem: I …"
tags:
  - "Juan Felipe Arias Aguirre"
---
[Sitemap](https://medium.com/sitemap/sitemap.xml)

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*4EAZiNHss8YYLoW657k1YA.gif)

> 我如何用大锤砸开坚果，并在此过程中爱上了图表。

一切始于一个简单的个人需求：我想追踪自己的能源消耗情况。

我有个电表，还有个手机。我想给电表拍张照片，发到某个地方，然后它就能被神奇地自动记录。另外容我辩解一句：没错，我既没有智能电表，也无法接入供电公司的平台。

“明智”的工程解决方案本该很简单：接收图片 → 光学字符识别 → 存入数据库。搞定。

但既然我们身处人工智能时代，我自然选择了 **火力全开** 的方案——决定构建一个功能完备的 AI 助手来处理这项任务。

然而，在构建过程中，我意识到关于使用 LLMs 进行开发的一个关键点： **并非所有场景都适合采用智能体模式。**

如果给 LLM *过多* 自由，它可能会产生幻觉、分心，甚至无法可靠完成简单任务。你绝不会想让一个"创意十足"的智能体去解析关键仪表读数——你需要的是精准执行的机器人。

这个项目， **能源伙伴** ，便是最终成果。它展示了采用 [LangGraph](https://github.com/langchain-ai/langgraph) 的 **混合架构** 方案，融合了以下要素：

1. **确定性逻辑** ：适用于那些 *必须* 每次都按相同方式执行的操作（如消息解析、路由选择）。
2. **智能体智能** ：适用于需要灵活性的场景（例如回答“我的使用情况与上个月相比如何？”这类问题）。

这是一个“简单而美好的项目”，证明了鱼与熊掌可以兼得：既有代码的可靠性，又具备智能体的灵活性。

## 架构：双流叙事

该应用采用图结构而非单一整体代理。这使得我们能够根据逻辑定义"固定动作"，同时只在真正需要的地方保留"大脑"。

## 1\. 主图（核心框架）

当消息从 WhatsApp（通过 Twilio）传来时，它并不会直接发送给 LLM，而是会经过一个结构化的处理流程：

1. **解析器** ：首先，我们需要确认实际接收到的内容类型。是图像还是文本？
2. **路由** ：根据输入决定执行路径。
- *图像？* -> 发送至 **分类器** 与 **提取器** （专项聚焦任务）。
- *文本？* -> 发送给 **查询代理** （即“大脑”）。

3. **数据记录员** ：若成功提取数据，我们会将其存入 BigQuery。

4. **应答器** ：最后，我们整理出得体的回复。

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*lscVtfXoj3bSQUE4JTLZBw.png)

## 2\. 聚焦：配备工具的智能体

这就是“超强能力”的体现。当你提出一个问题时（例如 *“根据我最近 10 次读数，预估我每月的欧元消费是多少？”* ）， **查询代理** 就会接管处理。

这不仅仅是一个聊天机器人。它是一个 **ReAct 智能体** ，配备了与真实世界交互的专用工具。它能查询数据库、实时查看电价（仍需寻找可靠的 API 接口，目前采用备用响应方案😅），甚至还能动态生成 Python 图表。

## 代码深度探索：构建图结构

让我们来看看如何利用 LangGraph 实际实现这种混合方法。

## 1\. The State

首先，我们定义 `AgentState` 。这是在我们图的所有节点之间传递的共享内存。它是一个类型化字典，可以轻松准确地知道在任何时间点有哪些数据可用。

```c
class AgentState(TypedDict):
    message_sid: str
    sender: str
    message_body: str
    media_url: Optional[str]
    has_image: bool
    is_query: bool
    # ... other fields
```

## 2\. 工作流定义

这是应用的核心。在 `src/workflow.py` 文件中，我们定义了图结构。请注意我们如何为流程的每个步骤添加节点。

```c
# src/workflow.py
def create_workflow() -> StateGraph:
    # Initialize StateGraph with AgentState schema
    workflow = StateGraph(AgentState)
    # Add all sub-agent nodes
    workflow.add_node("parse_message", parse_message)
    workflow.add_node("classify_image", classify_image)
    workflow.add_node("extract_reading", extract_reading)
    workflow.add_node("write_to_bigquery", write_to_bigquery)
    workflow.add_node("query_handler", handle_query)
    workflow.add_node("generate_response", generate_response)
    # Set entry point
    workflow.set_entry_point("parse_message")
    # ...
```

## 3\. 路由逻辑（"魔法粘合剂"）

混合图最重要的部分是 **条件边** ，它决定了我们何时扮演"机器人"角色，何时切换至"大脑"模式。

我们不再询问 LLM“下一步该做什么”，而是使用简单的 Python 函数。这种方法更快、更经济，且百分之百可靠。

```c
# src/workflow.py
def should_classify_image(state: AgentState) -> Literal["classify_image", "query_handler", "responder"]:
    """Routes based on message content type."""
    has_image = state.get("has_image", False)
    is_query = state.get("is_query", False)
    if has_image:
        return "classify_image"
    elif is_query:
        return "query_handler"
    return "responder"
# Add the conditional edge to the graph
workflow.add_conditional_edges(
    "parse_message",
    should_classify_image,
    {
        "classify_image": "classify_image",
        "query_handler": "query_handler",
        "responder": "generate_response"
    }
)
```

## 4\. “大脑”侧：配备工具的智能体

当路由器判定这是一个文本查询时，我们会将其发送至 `查询代理 ` 。这是一个标准的 ReAct 智能体，但由于我们已经过滤掉了"干扰项"（如图像处理任务），它能够完全专注于解答用户的问题。

我们赋予它特定的工具：

1. `query_readings` ：用于从 BigQuery 获取数据。
2. `get_electricity_price` ：用于获取实时电价。
3. `generate_plot` ：用于数据可视化。
```c
# src/nodes/agents/query_agent.py
def create_query_agent():
    llm = get_chat_model()
    tools = [
        query_readings,
        get_electricity_price,
        generate_plot
    ]
    # System prompt enforces rules like "DIRECTLY execute tools"
    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=SYSTEM_PROMPT,
    )
    return agent
```

`SYSTEM_PROMPT` 固然重要，但真正的力量源自我们提供的工具。

## 5\. 记忆（短期）：情境为王

LangGraph 最酷的功能之一就是它能轻松处理对话历史。我无需构建复杂的数据库架构来存储聊天记录，只需使用 **检查点** 就能实现。

```c
# src/workflow.py
from langgraph.checkpoint.memory import InMemorySaver
# ... inside create_workflow
checkpointer = InMemorySaver()
compiled_workflow = workflow.compile(checkpointer=checkpointer)
```

当我们调用工作流时，只需传入一个 `thread_id` （这里用的是用户手机号）。LangGraph 会在每个步骤后自动保存状态。

```c
# src/workflow.py
final_state = workflow.invoke(
    initial_state, 
    config={"configurable": {"thread_id": user_phone}}
)
```

这意味着当我问“刚才那个读数是什么来着？”时，智能体能准确理解我们讨论的内容。它自带“短期记忆”功能——当然，仅限于服务器运行期间。

## 未来规划：打造更强大的功能

这个版本很棒，但我已经在规划下一次升级了。

虽然当前检查点处理的是即时对话，但我想要 **长期记忆** 。我希望智能体能记住我通常在周日查看电表，或者去年七月我的电费突然飙升。想象一个智能体不仅能回应你当前的问题，还能从你数月甚至数年的习惯中学习——这才是理想中的形态。

## 结论：两全其美

通过使用 LangGraph，我们不仅构建了一个聊天机器人，更打造了一个可靠系统。

- **可靠性：** 我们在关键路径（读取仪表）上使用确定性代码。如果我发送一张图片，它 *必定* 会被处理。LLM 无法“决定”忽略它。
- **灵活性：** 我们采用智能体处理开放式路径（问题）。我可以直接询问“上周我花了多少钱？”，它就能自动解析出答案。

所以，如果你正在构建一个 AI 应用，不妨问问自己： **这真的需要成为一个智能体吗？**

如果答案介于“是”与“否”之间，那么图结构或许正是你所需。不必畏惧编写硬编码逻辑——你的智能体（以及用户）终将为此受益。

*完整代码请查看* [*GitHub*](https://github.com/juanfe88/energy_buddy) *。*