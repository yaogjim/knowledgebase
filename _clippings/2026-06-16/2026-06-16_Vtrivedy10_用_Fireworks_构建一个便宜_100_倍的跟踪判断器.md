---
title: "2026-06-16_Vtrivedy10_用_Fireworks_构建一个便宜_100_倍的跟踪判断器"
source: "https://x.com/Vtrivedy10/status/2066571435871551655"
author:
  - "[[@Vtrivedy10]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "#traces"
  - "x"
  - "@Vtrivedy10"
  - "https"
---

# 用 Fireworks 构建一个便宜 100 倍的跟踪判断器

**Viv**

# 用 Fireworks 构建一个便宜 100 倍的跟踪判断器

A

[@LangChain](https://x.com/@LangChain) Labs x

[@FireworksAI\_HQ](https://x.com/@FireworksAI_HQ)

study on fine-tuning open models to efficiently mine signals across large-scale trace data.

[@Vtrivedy10](https://x.com/@Vtrivedy10)

[@jakebroekhuizen](https://x.com/@jakebroekhuizen)

[@hwchase17](https://x.com/@hwchase17)

[@chahvivi](https://x.com/@chahvivi)

太长不看

- LangSmith 每天在生产追踪中处理数十亿个 token。我们的核心挑战之一是在这些追踪中高效地挖掘信号。
- 我们与 Fireworks 合作，构建了一个高效的 Trace Judge。我们微调了一个 Qwen 模型，以在每条生产轨迹上检测“Perceived Error”。它达到或超过了前沿模型的性能，且运行成本便宜 100 倍。
- If you want to be an earlier tester of this “perceived error” model, please sign up
 
 [here](https://airtable.com/appWdRBlSecNOgErA/pagAEfUlHu4F35opm/form).
 

Agents now

[produce a majority of the world’s data](https://www.cnet.com/tech/services-and-software/its-official-agentic-bots-surf-the-web-more-than-real-people-do/) and power many applications we use today. As more agents move into production,

[traces](https://docs.langchain.com/langsmith/observability-concepts#traces)

will become more important as one of the richest sources of data to understand how agentic systems behave with real users.

研究问题： 如何在保持前沿性能的同时，以经济高效的方式从每一条轨迹中挖掘重要信号 ？

To answer this question, we partnered with

[Fireworks](https://app.fireworks.ai/account/home) to fine-tune a Qwen judge model to detect “Perceived Error” from user interactions.

什么是感知错误：

> Perceived error is when the user thinks the assistant made a mistake or produced something that needed correction. Perceived Error is not judging objective correctness or user happiness. For example, an agent could give a correct answer but the user is frustrated by the information (not the agent).

我们通常推动团队构建特定于应用的评估器，因为判断跟踪的逻辑通常需要具备该应用的上下文。然而，我们认为“感知错误”是一种可通用的评估器的示例。我们相信它将寻找的信号在所有应用中都是通用的。

“感知误差”的普适性是一个关键问题。我们之后进行的一些实验专门旨在测试该指标的普适性。

我们从跟踪信号（如用户修正、对代理操作的拒绝、重复请求以及助手对错误的确认）中推断感知到的错误。然后，感知错误评估器会用以下格式的信息丰富跟踪内容：

```text
{"perceived_error": true, "reason": "The user corrects the meeting date the assistant used."}
```

## 我们如何创建了一个数据集

应用于任务的代理的质量仅取决于训练它们的数据。我们从我们在生产环境中使用的两个内部追踪数据集中获取数据：

[聊天 LangChain](https://github.com/langchain-ai/chat-langchain)

文档问答代理，用于回答关于 LangChain 库和产品的问题。用户可能会提出概念性问题、调试问题，或寻求构建相关帮助。这些交流通常具有技术性，并且涉及大量细节。

[Fleet](https://www.langchain.com/langsmith/fleet):

一个无代码工具，用于创建能够执行撰写文档和进行研究等真实工作的代理。用户可以使用 Fleet 完成各种任务，他们可以调用许多不同的工具或技能。

我们从每个跟踪数据集中选取了一部分跟踪数据作为训练集和验证集。在从跟踪数据池中进行筛选时，我们选择了多轮对话跟踪数据，因为判断“感知错误”需要人类对 AI 结果做出回应（例如，纠正助手或重复请求）。

使用多个数据集的部分动机是为了测试“感知误差”的通用性。在一个数据集上训练来检测感知误差的模型能否迁移到第二个数据集？

## 数据准备

在准备用于训练和预测的数据时，我们选择只包含人类和 AI 消息，忽略所有工具调用。我们这样做是因为我们假设，对于我们所寻找的信号，人类和 AI 消息是主要的信息来源。这是我们未来打算尝试的一个手段。

我们还原样包含了所有消息，没有删减长内容。这是我们未来打算尝试的另一个手段。

## 标签

为了生成标签，我们采用了模型辅助标注与人工审核相结合的方式，为每条轨迹创建简短的 JSON 标签和标注依据。具体来说，我们首先让模型小组评判一条轨迹。如果它们一致同意，我们就将该结果作为真实标签。如果它们存在分歧，我们就收集所有模型的标签和标注依据，提交给另一组模型，让其判断谁的标注正确。如果另一组模型达成一致，我们就以该结果作为真实标签。如果它们仍存在分歧，我们就由人工进行标注。在整个数据集上，chat-langchain 和 Fleet 的轨迹中，被标记为错误的比例分别为 24%和 18%。

## 微调设置

在对其他模型进行了一些小规模实验之后，我们选择 Qwen-3.5-35B 作为训练的基础模型。更小的模型错误率很高，并且不足以对我们的多轮对话轨迹进行推理。使用 Qwen-3.5-35B，我们拥有了一个强大且成本较低的开源模型，并且有通过微调达到前沿性能的空间。

我们仅使用 chat-langchain 数据集的数据进行训练。仅使用单一数据集的数据进行训练的原因是为了让我们能够测试该模型是否能迁移到完全不同的领域。

[在 Fireworks 上使用 LoRA 进行管理式 SFT 训练](https://docs.fireworks.ai/fine-tuning/supervised-fine-tuning)

## 实验与结果

我们围绕三个问题组织了实验：

1.  微调是否能将基线评判质量提升至前沿模型的性能水平？
2.  经过训练的判断者是否能跨数据集迁移？
3.  部署微调模型是否具有成本效益？

微调开源模型可以超越或媲美前沿模型

![Image](https://pbs.twimg.com/media/HK3rCm2XAAAR-Aw?format=png&name=large)

我们发现，经过良好提示词优化的基础 Qwen 模型是感知错误分类任务中一个表现强劲的开箱即用模型，但在分类准确率上落后于前沿模型。在两个数据集上，运行 LoRA SFT 任务都能将基础模型提升至接近或超过前沿模型的性能水平。

除了与前沿模型进行基准测试外，我们还与更小、更便宜的模型进行了比较。运行高吞吐量、低成本推理任务的常见策略是使用最小的封闭前沿模型，例如 Haiku。但我们始终发现，强大的开源模型开箱即用的表现优于 Haiku，同时运行成本也低得多。

经过微调的判断器对未见过的数据具有良好的迁移能力

![Image](https://pbs.twimg.com/media/HK3rIH_WIAAK7UP?format=png&name=large)

初步结果显示，Fleet 对所有模型而言都是一个更具挑战性的数据集。在 chat-langchain 上进行微调后，我们测试了该模型在未进行任何针对 Fleet 的特定训练的情况下，对 Fleet 数据的迁移效果如何。在 chat-langchain 数据上训练的模型在 Fleet 数据上的表现优于所有前沿模型。

We then experimented with training a model specifically on Fleet data. This resulted in a small improvement over our chat-langchain SFT’d model.

This is an important result because:

1.  It shows that our perceived error model is able to transfer to other domains and still maintain performance at frontier levels (in this case, slightly above).
2.  For builders who want to push the performance on perceived error (or other fine-tuned judges) on their own datasets even further, they have the option to fine-tune on application specific traces for some further performance gain.

## Fine-tuned models are much cheaper to run

![Image](https://pbs.twimg.com/media/HK3rMw0XgAAYzuc?format=png&name=large)

Fine-tuned models match frontier accuracy and are much cheaper to run at scale - 10-100x depending on trace volume and model choice. As trace volumes grow, the cost savings from a fine-tuned model continue to grow. And on performance, the fine-tuned Qwen model outperforms all model sizes Haiku, Sonnet, and Opus (and gpt-5.5).

## Future research on trace understanding

Solving Continual Learning will involve tackling large-scale data mining problems around trace understanding. In general, we’re excited to push forward recipes around building specialized, cost-effective models to better understand traces.

[Open models have crossed an intelligence threshold](https://www.langchain.com/blog/open-models-have-crossed-a-threshold) and are now strong out-of-the-box cost-effective classifiers for many tasks. With easy to use training & inference infrastructure from Fireworks, we’re able to push open models towards frontier performance while being orders of magnitude cheaper to run.

Future research directions include helping teams design good training objectives & rubrics to build their own evaluator models for their agent traces. The more we understand our agent traces, the better informed we can be when making changes to improve agents.

## Try our perceived error model

We will be rolling out our fine-tuned perceived error model to a select number of customers over the next few weeks before a broader rollout in a month or two. If you are interested in testing this perceived error judge and providing feedback, please sign up

[here](https://airtable.com/appWdRBlSecNOgErA/pagAEfUlHu4F35opm/form).

Also posted on the LangChain

[blog](https://www.langchain.com/blog/building-a-100x-cheaper-trace-judge-with-fireworks).