---
title: "2026-01-16_itunpredictable_近年来_模型的最佳改进之一就是整合了网络搜索功能_这里再稍微讲讲它在技术层面是怎么运作的_第一步是"
source: "https://x.com/itunpredictable/status/2011855115838505111"
author:
  - "[[@itunpredictable]]"
published: 2026-01-16
created: 2026-01-16
description:
tags:
  - "x"
  - "@itunpredictable"
  - "https"
  - "ai"
---

# 近年来，模型的最佳改进之一就是整合了网络搜索功能。这里再稍微讲讲它在技术层面是怎么运作的。 第一步是

**sisyphus bar and grill** @itunpredictable [2026-01-15](https://x.com/itunpredictable/status/2011855115838505111)

近年来，模型的最佳改进之一就是整合了网络搜索功能。这里再稍微讲讲它在技术层面是怎么运作的。

第一步是模型要判断自己是否真的需要或想要进行搜索。除了那些明显需要实时信息的提示之外，它如何判断用户提示的答案是否已存在于其权重中，或者反而需要基于某些外部数据进行锚定？

嗯，一个不错的方法是训练模型（或子模型）来完成这个任务。我们并不确切知道 OpenAI 是如何训练的，但很可能这是训练后期的一个步骤，该步骤会结合使用 SFT、RLHF 或在强化学习环境中进行训练，以确定何时进行网络搜索是合适的。

一旦模型决定要进行搜索，就会发起工具调用，这通常通过一系列特殊标记（比如<|call|>）来实现。过去几年实验室在模型训练方面做的很大一部分工作，就是让工具调用足够可靠。

这些搜索结果到底是从哪里来的？大多数主要的搜索引擎提供商——谷歌、必应（即将弃用）、DuckDuckGo——都有用于程序化搜索的 SERP API。这些就是 OpenAI 等公司用来获取结果的工具……但这并不意味着这些结果就很好。

今天的 SERP APIs 与 AI 搜索实际上非常不匹配，因为它们是为消费者（我们）设计的，而我们的消费模式和 AI 完全不同。

不过在模型调用 SERP API 之前，它需要把你的对话内容转换成网络搜索能理解的形式。你问 ChatGPT 在法国南部旅行期间应该住哪家酒店，它需要把这个问题转化为关键词。

最后，一旦模型得到想要的结果，就需要返回并引用这些结果。它这样做的方式是通过为每个网络搜索会话维护一种临时索引。

AI 网络搜索工作原理中一个非常有趣的部分是 web search agent loop，这是一种实验室用来让他们的模型成为更好搜索者的代理循环。解决这个问题的一种方法是通过构建一个代理，你可以给它植入一个指令，比如：“用户正在计划一次法国南部的旅行，他们似乎不太清楚自己想做什么，这里有一些关于他们的细节。”

这个代理只能使用一个工具（网络搜索），并且它可以反复调用这个工具，直到对结果满意，这些结果会被返回给顶层模型（ChatGPT）。

网页搜索的一个酷点是你可以轻松并行化。所以为了加快这个过程，你可以让网页搜索代理递归地创建其他网页搜索代理，所有这些代理同时执行某种简单的搜索任务。顶层代理会汇总所有这些结果，然后决定：这样够好了吗？还是我需要调用更多搜索代理……以及我要告诉它们什么？

总的来说，这就是 AI 网络搜索的工作方式，但情况在快速演变（事实证明用户仍然需要搜索）。

![Image](https://pbs.twimg.com/media/G-uLc25bQAECcrN?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G-uLeKCbQAY3FrI?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G-uLfLvbQAA_tIW?format=jpg&name=large)

* * *

**sisyphus bar and grill** @itunpredictable [2026-01-15](https://x.com/itunpredictable/status/2011855268397924866)

完整帖子的链接：

* * *

**Jeff Huber** @jeffreyhuber [2026-01-15](https://x.com/jeffreyhuber/status/2011937570129838432)

后排听不见，再大声点！

* * *

**sisyphus bar and grill** @itunpredictable [2026-01-16](https://x.com/itunpredictable/status/2011969065812664387)

AI 搜索很难