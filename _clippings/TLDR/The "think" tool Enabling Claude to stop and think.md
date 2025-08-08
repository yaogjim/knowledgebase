---
title: "The \"think\" tool: Enabling Claude to stop and think"
source: "https://www.anthropic.com/engineering/claude-think-tool"
author:
  - "[[@AnthropicAI]]"
published:
created: 2025-03-26
description: "A blog post for developers, describing a new method for complex tool-use situations"
tags:
  - "clippings"
---
随着我们不断提升 Claude 解决复杂问题的能力，我们发现了一种特别有效的方法：一种“思考”工具，它在复杂任务中为结构化思考创造了专门的空间。

这种简单却强大的技术——正如我们将在下文解释的，它与 Claude 新的“扩展思维”能力不同——已经使 Claude 在智能体工具使用能力方面有了显著提升。这包括遵循策略、做出一致决策以及处理多步骤问题，所有这些都只需极少的实施成本。

在这篇文章中，我们将探讨如何在不同应用程序上实现“思考”工具，并根据经过验证的基准测试结果为开发者提供实用指导。

### 什么是“思考”工具？

借助“思考”工具，我们赋予 Claude 一种能力，即在得出最终答案的过程中，增加一个额外的思考步骤，并为其设置专门的空间。

虽然它听起来与扩展思维相似，但却是一个不同的概念。扩展思维是指 Claude 在开始生成回复之前所做的事情。通过扩展思维，Claude 在采取行动之前会深入思考并反复完善其计划。“思考”工具是让 Claude 在开始生成回复后，添加一个步骤来停下来思考它是否拥有继续前进所需的所有信息。这在执行长链工具调用或与用户进行长时间多步骤对话时特别有用。

这使得“思考”工具更适用于这样的情况：Claude 无法仅根据用户查询获得制定响应所需的所有信息，并且需要处理外部信息（例如工具调用结果中的信息）。Claude 使用“思考”工具进行的推理不如通过扩展思考获得的推理全面，并且更侧重于模型发现的新信息。

我们建议在诸如非顺序工具调用或直接遵循指令等较简单的工具使用场景中使用扩展思维。扩展思维对于编码、数学和物理等用例也很有用，在这些用例中，你不需要 Claude 调用工具。当 Claude 需要调用复杂工具、在长串工具调用中仔细分析工具输出、在有详细指南的政策繁重环境中导航或做出每一步都基于前一步且错误代价高昂的顺序决策时，“思考”工具更适用。

这是一个使用来自τ-Bench 的标准工具规范格式的示例实现：

```
{
  "name": "think",
  "description": "Use the tool to think about something. It will not obtain new information or change the database, but just append the thought to the log. Use it when complex reasoning or some cache memory is needed.",
  "input_schema": {
    "type": "object",
    "properties": {
      "thought": {
        "type": "string",
        "description": "A thought to think about."
      }
    },
    "required": ["thought"]
  }
}
```

### τ基准测试的性能

我们使用τ-bench（tau-bench）对“思考”工具进行了评估，τ-bench 是一个全面的基准测试，旨在测试模型在实际客户服务场景中使用工具的能力，其中“思考”工具是评估标准环境的一部分。

τ基准测试评估 Claude 的以下能力：

- 与模拟用户进行逼真的对话导航
- 始终如一地遵循复杂的客户服务代理政策指南
- 使用各种工具来访问和操作环境数据库

τ-bench 中使用的主要评估指标是 pass^k，它衡量的是给定任务的所有 k 个独立任务试验均成功的概率，是在所有任务上的平均值。与其他 LLM 评估中常见的 pass@k 指标（衡量 k 次试验中是否至少有一次成功）不同，pass^k 评估的是一致性和可靠性——这对于客户服务应用程序来说是至关重要的品质，因为在这类应用中严格遵守政策是必不可少的。

#### 性能分析

我们的评估比较了几种不同的配置：

1. 基线（无“思考”工具，无扩展思考模式）
2. 仅扩展思维模式
3. 仅“思考”工具
4. 具有优化提示（适用于航空领域）的“思考”工具

结果显示，当 Claude 3.7 在基准测试的“航空”和“零售”客户服务领域有效使用“思考”工具时，有显著改进：

- 航空领域：经过优化提示的“思考”工具在 pass^1 指标上达到了 0.570，而基线仅为 0.370，相对提高了 54%；
- 零售领域：仅“思考”工具的得分就达到了 0.812，而基线的得分为 0.783。

![A line graph showing the performance of Claude 3.7 Sonnet on the "airline" domain of the Tau-Bench eval](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fff91e5c84be59ae71306bcc60adba9affed86484-2200x1300.jpg&w=3840&q=75)

Claude 3.7 在四种不同配置下，在 Tau-Bench 评估的“航空公司”领域的十四行诗性能。

Claude 3.7 在 Tau-Bench 评估的“航空公司”领域的表现

| 配置 | *k* =1 | *k* =2 | *k* =3 | *k* =4 | *k* =5 |
| --- | --- | --- | --- | --- | --- |
| “思考”+提示 | 0.584 | 0.444 | 0.384 | 0.356 | 0.340 |
| "Think" | 0.404 | 0.254 | 0.186 | 0.140 | 0.100 |
| 扩展思维 | 0.412 | 0.290 | 0.232 | 0.192 | 0.160 |
| 基线 | 0.332 | 0.206 | 0.148 | 0.116 | 0.100 |

四种不同配置的评估结果。分数为比例。

在航空领域，通过将“思考”工具与优化后的提示相结合，实现了最佳性能。该提示给出了在分析客户请求时应使用的推理方法类型的示例。以下是优化提示的一个示例：

```
## Using the think tool

Before taking any action or responding to the user after receiving tool results, use the think tool as a scratchpad to:
- List the specific rules that apply to the current request
- Check if all required information is collected
- Verify that the planned action complies with all policies
- Iterate over tool results for correctness 

Here are some examples of what to iterate over inside the think tool:
<think_tool_example_1>
User wants to cancel flight ABC123
- Need to verify: user ID, reservation ID, reason
- Check cancellation rules:
  * Is it within 24h of booking?
  * If not, check ticket class and insurance
- Verify no segments flown or are in the past
- Plan: collect missing info, verify rules, get confirmation
</think_tool_example_1>

<think_tool_example_2>
User wants to book 3 tickets to NYC with 2 checked bags each
- Need user ID to check:
  * Membership tier for baggage allowance
  * Which payments methods exist in profile
- Baggage calculation:
  * Economy class × 3 passengers
  * If regular member: 1 free bag each → 3 extra bags = $150
  * If silver member: 2 free bags each → 0 extra bags = $0
  * If gold member: 3 free bags each → 0 extra bags = $0
- Payment rules to verify:
  * Max 1 travel certificate, 1 credit card, 3 gift cards
  * All payment methods must be in profile
  * Travel certificate remainder goes to waste
- Plan:
1. Get user ID
2. Verify membership level for bag fees
3. Check which payment methods in profile and if their combination is allowed
4. Calculate total: ticket price + any bag fees
5. Get explicit confirmation for booking
</think_tool_example_2>
```

特别有趣的是不同方法之间的比较。使用经过优化提示的“思考”工具，在扩展思考模式下取得了显著更好的结果（扩展思考模式的表现与未提示的“思考”工具相似）。单独使用“思考”工具（无提示）比基线提高了性能，但仍不及优化后的方法。

“思考”工具与优化后的提示相结合，其性能大幅领先，这可能是由于基准测试中航空公司政策部分的高度复杂性，在这部分内容中，模型从获得如何“思考”的示例中受益最大。

在零售领域，我们还测试了各种配置，以了解每种方法的具体影响

![Line graph showing the performance of Claude 3.7 Sonnet on the "retail" domain of the Tau-Bench eval](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F5819616b4cc109d30f1a7d47ec8a32a6b839637b-7638x4513.jpg&w=3840&q=75)

Claude 3.7 十四行诗在三种不同配置下在 Tau-Bench 评估的“零售”领域的性能。

Claude 3.7 在 Tau-Bench 评估的“零售”领域的表现

| 配置 | *k* =1 | *k* =2 | *k* =3 | *k* =4 | *k* =5 |
| --- | --- | --- | --- | --- | --- |
| “思考”+无提示 | 0.812 | 0.735 | 0.685 | 0.650 | 0.626 |
| 扩展思维 | 0.770 | 0.681 | 0.623 | 0.581 | 0.548 |
| 基线 | 0.783 | 0.695 | 0.643 | 0.607 | 0.583 |

三种不同配置下的评估结果。分数为比例。

“思考”工具即使在没有额外提示的情况下也取得了 0.812 的最高通过率^1。与航空领域相比，零售政策明显更容易理解，而且 Claude 仅通过有一个思考空间而无需进一步指导就能有所改进。

#### τ基准分析的关键见解

我们的详细分析揭示了几种模式，这些模式可以帮助您有效地实施“思考”工具：

1. 在困难领域中，提示起着至关重要的作用。仅仅提供“思考”工具可能会在一定程度上提高性能，但将其与优化后的提示相结合，对于困难领域能产生显著更好的结果。然而，较简单的领域可能只需能够使用“思考”就会受益。
2. 跨试验提高了一致性。使用“思考”带来的改进在 pass^k 中一直保持到 k = 5，这表明该工具帮助 Claude 更有效地处理边缘情况和异常场景。

### 在 SWE-Bench 上的性能

在评估 Claude 3.7 Sonnet 时，我们的 SWE-bench 设置中添加了一个类似的“思考”工具，这有助于实现 0.623 的当前最优分数。下面给出了经过调整的“思考”工具定义：

```
{
  "name": "think",
  "description": "Use the tool to think about something. It will not obtain new information or make any changes to the repository, but just log the thought. Use it when complex reasoning or brainstorming is needed. For example, if you explore the repo and discover the source of a bug, call this tool to brainstorm several unique ways of fixing the bug, and assess which change(s) are likely to be simplest and most effective. Alternatively, if you receive some test results, call this tool to brainstorm ways to fix the failing tests.",
  "input_schema": {
    "type": "object",
    "properties": {
      "thought": {
        "type": "string",
        "description": "Your thoughts."
      }
    },
    "required": ["thought"]
  }
}
```

我们的实验（使用“思考”工具的 30 个样本，未使用的 144 个样本）表明，包含此工具的单独效果平均将性能提高了 1.6%（韦尔奇 t 检验：t(38.89) = 6.71，p <.001，d = 1.47）。

### 何时使用“思考”工具

基于这些评估结果，我们已经确定了 Claude 从“思考”工具中获益最多的特定场景：

1. 工具输出分析。当 Claude 在采取行动之前需要仔细处理先前工具调用的输出，并且可能需要在其方法中回溯时；
2. 政策密集的环境。当 Claude 需要遵循详细的指导方针并核实合规情况时；以及
3. 顺序决策。当每个行动都建立在先前行动的基础上且错误代价高昂时（常见于多步领域）。

## 实施最佳实践

要充分利用 Claude 的“思考”工具，我们根据τ-bench 实验推荐以下实施方法。

#### 1\. 使用特定领域示例进行策略性提示

最有效的方法是提供关于何时以及如何使用“思考”工具的明确说明，例如用于τ-bench 航空公司领域的工具。提供针对您特定用例的示例可显著提高模型使用“思考”工具的效率：

- 推理过程中预期的详细程度；
- 如何将复杂的指令分解为可操作的步骤；
- 用于处理常见场景的决策树；以及
- 如何检查是否已收集所有必要信息。

#### 2\. 将复杂的引导信息置于系统提示中

我们发现，当它们冗长和/或复杂时，在系统提示中包含有关“思考”工具的说明比将它们放在工具描述本身中更有效。这种方法提供了更广泛的上下文，并有助于模型更好地将思考过程整合到其整体行为中。

### 何时不使用“思考”工具

鉴于“思考”工具可以带来显著改进，但它并不适用于所有工具使用用例，而且确实会以增加提示长度和输出令牌为代价。具体而言，我们发现“思考”工具在以下用例中没有提供任何改进：

1. 非顺序工具调用。如果 Claude 只需要进行单个工具调用或多个并行调用就能完成一项任务，那么添加“思考”环节不太可能带来任何改进。
2. 简单的指令遵循。当 Claude 需要遵守的约束条件不多，并且其默认行为已经足够好时，额外的“思考”不太可能带来收益。

### 入门指南

“思考”工具是对你的 Claude 实现的一个直接补充，只需几步就能带来有意义的改进：

1. 使用智能体工具使用场景进行测试。从具有挑战性的用例开始——即 Claude 目前在长期工具调用链中的策略合规性或复杂推理方面存在困难的用例。
2. 添加工具定义。实现一个针对您的领域定制的“思考”工具。它需要最少的代码，但能实现更结构化的推理。还要考虑在系统提示中包含有关何时以及如何使用该工具的说明，并附上与您的领域相关的示例。
3. 监控并优化。观察 Claude 在实际中如何使用该工具，并调整你的提示词以鼓励更有效的思维模式。

最棒的是，添加这个工具在性能结果方面的负面影响极小。除非 Claude 决定使用它，否则它不会改变外部行为，也不会干扰你现有的工具或工作流程。

### 结论

我们的研究表明，“思考”工具可以显著提高 Claude 3.7 十四行诗在需要遵循策略和在长链工具调用中进行推理的复杂任务上的性能 1。“思考”并非适用于所有情况的万能解决方案，但它为正确的用例带来了巨大好处，且所有这些都只需极低的实现复杂度。

我们期待看到你将如何使用“思考”工具与 Claude 构建更强大、可靠和透明的人工智能系统。

1\. 虽然我们的τ基准测试结果侧重于使用“思考”工具对 Claude 3.7 十四行诗进行改进，但我们的实验表明，Claude 3.5 十四行诗（新版）在与 3.7 十四行诗相同的配置下也能够实现性能提升，这表明这种改进也适用于其他 Claude 模型。