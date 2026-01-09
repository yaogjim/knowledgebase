---
title: "LangChain on X: "Evaluating Deep Agents: Our Learnings" / X"
source: "https://x.com/LangChain/status/2006589207196930109"
author: ""
created: 2026-01-06 19:18:37
date: 2026-01-06 19:18:37
description: ""
tags: ""
---
过去一个月里，在 LangChain，我们发布了四个基于 Deep Agents 框架的应用：

-   DeepAgents CLI: 一个编码代理
    
-   LangSmith 助手：应用内的助手，帮助在 LangSmith 中处理各种事情
    
-   个人邮箱助手：一个通过与每个用户的互动学习的邮箱助手
    
-   : 一个无代码代理构建平台，由 Meta 深度代理驱动
    

构建和发布这些代理意味着为每个代理添加评估，我们在这个过程中学到了很多！在这篇文章中，我们将深入探讨以下用于评估深度代理的模式。

1.  深度代理需要为每个数据点定制测试逻辑 — 每个测试用例都有其自身的成功标准。
    
2.  运行单步深度代理非常适合在特定场景中验证决策（而且还能节省 token！）
    
3.  完整的代理轮次非常适合测试关于代理“最终状态”的断言。
    
4.  多智能体轮次模拟真实的用户交互，但需要被引导到正轨上。
    
5.  环境配置很重要 — 深度智能体需要干净、可重现的测试环境
    

-   单步：限制核心代理循环仅运行一次迭代，确定代理将采取的下一步行动。
    
-   完整轮次：在单一输入上完整运行代理，该输入可能包含多次工具调用迭代。
    
-   多轮：多次完整运行代理。通常用于模拟代理与用户之间的“多轮”对话，即多次来回交互。
    

[

![Image](https://pbs.twimg.com/media/G9jRmh_aMAYOs1F?format=jpg&name=medium)



](https://x.com/LangChain/article/2006589207196930109/media/2006584093883117574)

-   轨迹：代理调用的工具序列，以及代理生成的具体工具参数。
    
-   最终响应: 来自代理到用户的最终返回的响应。
    
-   其他状态：代理在运行时生成的其他值（例如文件、其他工件）
    

[

![Image](https://pbs.twimg.com/media/G9jRqxNbkAAIcEU?format=jpg&name=medium)



](https://x.com/LangChain/article/2006589207196930109/media/2006584166687936512)

3) 在数据集上运行你的应用程序以生成输出，并使用你的评估器对这些输出进行评分

每个数据点都被同等对待——经过相同的应用逻辑处理，由同一个评估器评分。

[

![Image](https://pbs.twimg.com/media/G9jRwb9a0AA4cGx?format=jpg&name=medium)



](https://x.com/LangChain/article/2006589207196930109/media/2006584264062849024)

Deep Agents 打破了这一假设。你会想要测试的不只是最终消息。“成功标准”可能对每个数据点也更具体，并且可能涉及针对代理的轨迹和状态的具体断言。

[

![Image](https://pbs.twimg.com/media/G9jR0SBaMAITpvl?format=jpg&name=medium)



](https://x.com/LangChain/article/2006589207196930109/media/2006584330114707458)

我们有一个能够记住用户偏好的日历日程深度代理。用户会让他们的代理记住“永远不要在上午9点前安排会议”。我们希望确认，日历日程代理会更新其在文件系统中的自身记忆，以记住这个信息。

1) 代理调用了 edit\_file 方法，针对 文件路径

3) The memories.md 文件实际上包含了关于不安排早会的信息。你可以：

-   使用正则表达式查找“9am”的提及
    
-   或者使用 LLM 作为评判者，根据具体的成功标准，对文件更新进行更全面的分析
    

LangSmith 的 Pytest 和 Vitest 集成支持这种定制化测试。你可以针对每个测试用例，对代理的轨迹、最终消息和状态进行不同的断言。

```
# Mark as a LangSmith test case
@pytest.mark.langsmith
def test_remember_no_early_meetings() -> None:
    user_input = "I don't want any meetings scheduled before 9 AM ET"
    # We can log the input to the agent to LangSmith
    t.log_inputs({"question": user_input})
    
    response = run_agent(user_input)
    # We can log the output of the agent to LangSmith
    t.log_outputs({"outputs": response})
    
    agent_tool_calls = get_agent_tool_calls(response)
    
    # We assert that the agent called the edit_file tool to update its memories
    assert any([tc["name"] == "edit_file" and tc["args"]["path"] == "memories.md" for tc in agent_tool_calls])
    
        # We log feedback from an llm-as-judge that the final message confirmed the memory update
        communicated_to_user = llm_as_judge_A(response)
    t.log_feedback(key="communicated_to_user", score=communicated_to_user)
    
    # We log feedback from an llm-as-judge that the memories file now contains the right info
    memory_updated = llm_as_judge_B(response)
    t.log_feedback(key="memory_updated", score=memory_updated)
```

想要使用 Pytest 的一般代码片段，可查看 ：

这个 LangSmith 集成会自动将所有测试用例记录到实验中，这样你就可以查看失败测试用例的执行轨迹（以调试哪里出错了）并随时间跟踪结果。

[

![Image](https://pbs.twimg.com/media/G9jR5QlbcAAhzIe?format=jpg&name=medium)



](https://x.com/LangChain/article/2006589207196930109/media/2006584415628259328)

在为 Deep Agents 进行评估时，大约一半的测试用例看起来是单步评估，即 LLM 在特定一系列输入消息之后立即决定做什么？

这在验证代理在特定场景下调用了正确的工具和参数时尤其有用。常见的测试用例包括：

-   它用对工具来查找会议时间了吗？
    
-   它检查了正确的目录内容吗？
    
-   它更新记忆了吗？
    

回归通常发生在单独的决策点，而非整个执行序列中。如果使用 LangGraph，其流式能力允许你在单次工具调用后中断代理以检查输出——这样你就能尽早发现问题，而无需完整的代理序列带来的额外开销。

在下面的代码片段中，我们在 tools 节点之前手动设置了一个断点，使我们能够轻松地单步运行代理。然后我们可以检查并对单步执行后的状态进行断言。

```
@pytest.mark.langsmith
def test_single_step() -> None:
    state_before_tool_execution = await agent.ainvoke(
        inputs,
        # interrupt_before specifies nodes to stop before
        # interrupting before the tool node allows us to inspect the tool call args
        interrupt_before=["tools"]
    )
    # We can see the message history of the agent, including the latest tool call
    print(state_before_tool_execution["messages"])
```

[

![Image](https://pbs.twimg.com/media/G9jR9rLaMAAB6Z7?format=jpg&name=medium)



](https://x.com/LangChain/article/2006589207196930109/media/2006584491486359552)

把单步评估看作你的“单元测试”，确保代理在特定场景下采取预期的行动。同时，完整的代理轮次也很有价值——它们向你展示代理执行的端到端行动的完整图景。

1) 轨迹：评估完整轨迹的一种非常常见的方法是确保在操作过程中的某个时刻调用了特定工具，但具体何时调用并不重要。在我们的日历调度器示例中，调度器可能需要多次调用工具来找到一个适合所有参与者的合适时间段。

[

![Image](https://pbs.twimg.com/media/G9jSFIIbMAAJcBx?format=jpg&name=medium)



](https://x.com/LangChain/article/2006589207196930109/media/2006584619517554688)

2) 最终回答: 在某些情况下，最终输出的质量比代理采取的具体路径更重要。我们发现这一点在更开放性的任务（如编码和研究）中是正确的。

[

![Image](https://pbs.twimg.com/media/G9jSHXJa8AAEy9h?format=jpg&name=medium)



](https://x.com/LangChain/article/2006589207196930109/media/2006584657908002816)

3) 其他状态： 评估其他状态与评估代理的最终响应非常相似。有些代理会生成产物而非以聊天格式响应用户。通过检查 LangGraph 中代理的状态，检查和测试这些产物变得很容易。

1.  对于编码代理 → 阅读然后测试该代理编写的文件。
    
2.  针对研究代理 → 确认代理找到了正确的链接或来源。
    

完整的代理交互过程能让你全面了解代理的执行情况。LangSmith 让你可以轻松地将完整的代理交互过程以轨迹形式查看，在这些轨迹中你可以查看延迟和 token 使用等高级指标，同时还能分析具体步骤，深入到每个模型调用或工具调用。

[

![Image](https://pbs.twimg.com/media/G9jSLYraMAEQ6sc?format=jpg&name=medium)



](https://x.com/LangChain/article/2006589207196930109/media/2006584727038472193)

某些场景需要在多轮对话中测试代理，这些对话包含多个连续的用户输入。挑战在于，如果天真地硬编码输入序列，而代理偏离了预期路径，后续的硬编码用户输入可能就没有意义了。

我们通过在 Pytest 和 Vitest 测试中添加条件逻辑来解决这个问题。例如，我们会：

-   执行第一轮，然后检查代理输出。若输出符合预期，就执行下一轮。
    
-   如果这不在预期之中，就提前让测试失败。（这之所以可行，是因为我们能够在每一步后灵活地添加检查。）
    

这种方法让我们能够进行多轮评估，而无需为每个可能的代理分支建模。如果我们想单独测试第二轮或第三轮，只需从那个环节开始，用合适的初始状态设置一个测试即可。

深度智能体是有状态的，旨在处理复杂、长期运行的任务——通常需要更复杂的环境来进行评估。

与更简单的 LLM 评估不同，这类评估的环境通常仅限于几个无状态工具，而 Deep Agents 每次评估运行都需要一个全新、干净的环境，以确保结果可重现。

编码代理清晰地说明这一点。Harbor 为在专用 Docker 容器或沙箱中运行的 TerminalBench 提供评估环境。对于 DeepAgents CLI，我们采用更轻量的方法：为每个测试用例创建一个临时目录并在其中运行代理。

更重要的一点：深度智能体评估需要每次测试时重置的环境——否则你的评估会变得不稳定且难以复现。

LangSmith Assist 需要连接到真实的 LangSmith API。针对实际服务运行评估可能会很慢且成本很高。相反，将 HTTP 请求记录到文件系统中，并在测试执行期间重放这些请求。对于 Python， 效果很好；对于 JS，我们通过 Hono 应用代理 fetch 请求，这样可行。

模拟或重放 API 请求能让 Deep Agent 的评估更快、更易于调试，尤其是当代理严重依赖外部系统状态时。

上述技术是我们在为深度智能体驱动的应用编写自己的测试套件时看到的常见模式。你可能只需要上述模式中的一部分来满足你的特定应用需求——因此，你的评估框架具备灵活性非常重要。如果你正在构建深度智能体并开始进行评估，不妨看看 ！