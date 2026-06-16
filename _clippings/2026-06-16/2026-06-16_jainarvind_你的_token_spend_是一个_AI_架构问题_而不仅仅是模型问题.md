---
title: "2026-06-16_jainarvind_你的_token_spend_是一个_AI_架构问题_而不仅仅是模型问题"
source: "https://x.com/jainarvind/status/2062294414714945764"
author:
  - "[[@jainarvind]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "x"
  - "@jainarvind"
  - "ai"
  - "work"
---

# 你的 token spend 是一个 AI 架构问题，而不仅仅是模型问题

**Arvind Jain**

# 你的 token spend 是一个 AI 架构问题，而不仅仅是模型问题

企业 AI 代币支出正快速增长，特别是随着技术从简单的聊天助手转向编码代理、AI 协作者和长期运行的工作流。这些系统每个任务完成的工作量大得多，但消耗的代币也多得多。这对企业来说产生了一个新的运营约束：不是 AI 是否有用，而是它能否产生足够的有用成果来证明成本合理。

The spending signals are now hard to ignore.

[Deloitte’s 2025 Tech Value Survey](https://www.deloitte.com/us/en/insights/topics/digital-transformation/ai-tech-investment-roi.html) found that more than half of respondents allocate between 21% and 50% of their digital initiative budgets to AI, with an average of 36%.

[Ramp](https://ramp.com/ai-cost-monitoring)

recently reported a 4x year-over-year increase in monthly AI spend. And

[Fortune](https://fortune.com/2026/05/26/uber-coo-ai-spending-tokens-claude-code/)

reported that Uber burned through its entire 2026 AI coding tools budget in four months.

在我与领导者的太多对话中，代币消耗增长迅速，而商业价值却没有以相同的速度增长。

这就是为什么我认为企业需要一个比原始 token 使用量更好的衡量指标。正确的问题不是系统消耗了多少 token，而是系统每消耗一个 token 产生了什么有用的成果。换句话说：token yield。

思考 AI 经济学时，更有用的方式是考虑 token 使用，因为 token 使用很少仅由模型单独驱动。它由模型周围的整个系统决定：上下文如何检索、工具如何被暴露、任务如何分解、模型如何路由，以及先前执行如何被复用。如果该架构低效，即使输出质量没有下降，token 消耗也会增加。

词元不仅仅是提示词中的单词

简短的用户指令可能会触发非常大的 token 账单。

以这样的提示为例：“分析这些账户的流失风险并创建后续任务。”用户可见的提示内容很小，但实际的 token 负载通常包括系统指令、工具架构、检索到的文档、中间推理过程、执行轨迹以及记忆内容。在许多企业系统中，大多数 token 根本不是由用户输入的，而是由任务周围的支撑框架生成的。

这就是架构开始发挥作用的地方。如果系统检索过多上下文、调用过多工具、重复已完成的工作，或通过昂贵的前沿模型处理常规工作，token 消耗会增加，但质量并未相应提升。这种浪费并非源于某个单独的提示词，而是源于系统的设计。

这就是为什么代币收益率从根本上说是一个架构问题。

四个决定代币效率的架构杠杆

上下文质量

大多数企业级 AI 失败始于上下文。

模型不知道哪些上下文是重要的。它们会处理你提供的所有内容。而且随着上下文的增长，处理这些上下文的成本也会增加。如果检索过程存在噪声，模型会将其处理预算浪费在不相关或冲突的信息上进行推理，而不是根据正确的信号采取行动。

答案不是往提示词里塞更多数据，而是要更好地检索。

[benchmark](https://www.glean.com/blog/cowork-mcp-eval)

[@glean](https://x.com/@glean)

That is the hidden tax of poor context architecture.

A well-designed context layer does the opposite. It gives the model the right information earlier, in a more usable form, so the system can spend tokens on solving the problem rather than assembling the problem.

2\. Model routing

Not every step in an agentic workflow requires frontier reasoning.

A large share of enterprise AI work is operational: search, retrieval planning, tool selection, validation, and execution management. Those steps matter, but they do not always require the most expensive model in the stack.

This is why multi-model architectures are important. The goal is not to use smaller models everywhere. It is to use the right level of intelligence for the job.

That distinction becomes more important as usage scales. If every step is routed through a frontier model by default, the enterprise is effectively paying frontier prices for routine work.

Right-sizing model usage is one of the most direct ways to improve token yield: preserve frontier reasoning where it creates differentiated value, and use specialized models where the work is narrower and more repeatable.

3\. Continual learning

Enterprise AI systems should not solve the same class of problem from scratch every time.

Every execution produces signal about how similar work should be done next time: which tools were useful, which retrieval path worked, which steps were unnecessary, and which outputs actually helped a user complete the job. Humans already work this way. When someone does useful work or writes something worth reusing, we document it so we do not have to recreate it from scratch every time. Enterprise AI systems should work the same way. Over time, that accumulated trace data should help the system avoid redundant exploration and get better at resolving similar work.

If it doesn’t, the system keeps paying the same exploratory cost again and again.

This is often an underappreciated part of AI economics. A system that learns from prior execution can reduce redundant reasoning, skip failed paths, and converge faster on the right workflow. The result is not just higher quality. It is lower cost on repeated work.

The best enterprise AI systems will compound in this way. Each completed task should improve the economics of the next related one.

4\. Harness design

As agents take on longer-running, multi-step work, the harness becomes a major determinant of both quality and cost.

A naive harness keeps expanding the active context window. It carries more instructions, more tools, more state, and more intermediate outputs forward at every step. Cost grows as the workflow grows. Reliability usually degrades too.

A better harness treats context as something to manage, not something to accumulate.

That means scoping tools to the current step, distributing work across specialized agents when appropriate, externalizing intermediate state instead of keeping everything in active memory, and giving each model only the working set it needs. The goal is not only to support more complex tasks. It is to support them without collapsing under context bloat.

The real AI moat is execution efficiency.

* * *

### 热门回复

**@Mahesh Lambe** ♥ 1 · 💬 0

2023 年 1 月，我构建了

http://

Tokenomy.ai 为自己。

那时，这个问题感觉很个人化，几乎有点书呆子气：

我想了解我使用了多少 token，我的 AI 实验花费了多少，以及在发送之前我是否能做出更好的模型选择

**@Sam Z Liu** ♥ 0 · 💬 0

问题在于，这其中多大程度上取决于实施 AI 的公司来解决，而不是模型公司。例如，更好的 KV 缓存可能就能在基础设施层面解决这个问题。

**@Raj Koneru** ♥ 0 · 💬 0

架构和解决方案设计是目前最被低估的话题。这是实现规模化并积累价值的最佳途径。