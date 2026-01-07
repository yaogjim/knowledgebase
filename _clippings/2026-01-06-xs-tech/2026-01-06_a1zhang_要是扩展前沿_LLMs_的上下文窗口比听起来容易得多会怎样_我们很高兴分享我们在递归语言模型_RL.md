---
title: "2026-01-06_a1zhang_要是扩展前沿_LLMs_的上下文窗口比听起来容易得多会怎样_我们很高兴分享我们在递归语言模型_RL"
source: "https://x.com/a1zhang/status/1978469116542337259"
author:
  - "[[@a1zhang]]"
published: 2026-01-06
created: 2026-01-06
description:
tags:
  - "x"
  - "@a1zhang"
  - "https"
  - "2025-10-15"
---

# 要是扩展前沿 LLMs 的上下文窗口比听起来容易得多会怎样？ 我们很高兴分享我们在递归语言模型（RL

**Alex L Zhang** @a1zhang [2025-10-15](https://x.com/a1zhang/status/1978469116542337259)

要是扩展前沿 LLMs 的上下文窗口比听起来容易得多会怎样？

我们很高兴分享我们在递归语言模型（RLMs）方面的研究成果。这是一种新的推理策略，LLMs 可以分解并递归地与看似无界长度的输入提示词进行交互，作为一个 REPL 环境。

在 OOLONG 基准测试中，搭载 GPT-5-mini 的 RLMs 在 132k token 序列上的表现优于 GPT-5，提升超过 110%（超过两倍！），且平均查询成本更低。

在 BrowseComp-Plus 基准测试中，配备 GPT-5 的递归语言模型（RLMs）可接收 1000 万+ token 作为“prompt”，回答高度组合性查询无性能退化，效果甚至优于显式索引/检索。

我们在下面附上我们的博客文章、（仍处于非常早期阶段！）实验和讨论。

![Image](https://pbs.twimg.com/media/G3TuAPxWYAATrbO?format=jpg&name=large)

* * *

**Alex L Zhang** @a1zhang [2025-10-15](https://x.com/a1zhang/status/1978469119797162157)

递归语言模型和底层语言模型一样通用。事实上，从用户的角度来看，它们看起来和普通的模型调用没什么不同，但它们可以在内部生成（递归的）语言模型调用，以进行中间计算。

当 RLM 被查询时，它允许“根”LM 将上下文作为其环境的一部分进行探索或处理。它使用递归(R)LM 来委托并扩展对任意结构或长度上下文的处理。

![Image](https://pbs.twimg.com/media/G3TuJwDWkAAb5Ic?format=png&name=large)

* * *

**Alex L Zhang** @a1zhang [2025-10-15](https://x.com/a1zhang/status/1978469122666086905)

我们将其实现为一个类似 Jupyter 的 REPL 环境：

核心思想是将用户的提示放入 Python 变量中，并给 LLM 一个 REPL 循环，让它可以尝试理解提示，而无需直接读取整个内容。

“根”语言模型通过编写代码并查看每个单元格的输出与环境交互，并且可以在这个 REPL 环境中递归调用 LM 以导航其上下文。

这比任何“分块”策略都要通用得多。我们认为你应该让 LLM 自己决定如何最好地摸索、分解并递归处理长提示词。

![Image](https://pbs.twimg.com/media/G3TuOYOXQAA3m39?format=jpg&name=large)

* * *

**Alex L Zhang** @a1zhang [2025-10-15](https://x.com/a1zhang/status/1978469126415806961)

RLMs 旨在解决上下文衰减，即那种奇怪的现象——当你使用很长的 Claude Code 或 Cursor 实例时，它无法妥善处理你的长对话历史。

OOLONG 是一个新的、有挑战性的长上下文基准测试，模型需在极其密集的上下文中回答查询。我们选取了一个特别困难的分割，其中 GPT-5 在 132-263k token 的上下文中得分约 33%。

与此同时，使用 GPT-5-mini 的 RLM 表现优于 GPT-5，且每次查询成本更低，在 132k 的情况下提升超过 114%（即超过一倍！），在 263k 的情况下提升 49%！

![Image](https://pbs.twimg.com/media/G3TuS8xXgAA1wwK?format=jpg&name=large)

* * *

**Alex L Zhang** @a1zhang [2025-10-15](https://x.com/a1zhang/status/1978469129225912398)

RLMs 也被设计来处理近乎无限的上下文，无需额外的支撑结构。

BrowseComp-Plus (BC+) 是一项 DeepResearch 基准测试，在该测试中，模型需要回答多跳组合式问题，而这些问题需要检索多个离线文档。

对于这些初步结果，我们选取了 BC+中的一小部分查询，将作为上下文直接输入的文档数量从 10 扩大到 1000（约 10 万至 1000 万 token），发现使用 GPT-5 的递归语言模型（RLMs）在这些规模下仍能保持性能、无性能退化，甚至优于 ReAct+检索循环！

![Image](https://pbs.twimg.com/media/G3TuXkuWQAASWku?format=jpg&name=large)

* * *

**Alex L Zhang** @a1zhang [2025-10-15](https://x.com/a1zhang/status/1978469131407290859)

博客文章：https://alexzhang13.github.io/blog/2025/rlm/

博客文章中可以找到 RLMs 表现出的几个有趣行为的例子。我们编写了一个可视化工具，以便让这些例子更清晰，并突出这些模型可以采用的不同策略。

乌龙：

https://openreview.net/forum?id=lrDr6dmXOX…

BCP: https://arxiv.org/abs/2508.06600

我想感谢我出色的导师 @lateinteraction，还有在做这个项目时我在 Slack 上狂发消息骚扰的 @noahziems，以及我实验室的其他成员 @jacobli99 @dianetc\_ 感谢他们在这个项目中的支持和讨论！

* * *

**Omar Khattab** @lateinteraction [2025-10-15](https://x.com/lateinteraction/status/1978514927955427385)

如果你在找链接却像 @omouamoua，好吧，这是你的捷径：

> 2025-10-15
> 
> 博客文章：https://alexzhang13.github.io/blog/2025/rlm/
> 
> 博客文章中可以找到 RLMs 产生的一些有趣行为的例子。我们开发了一个可视化工具，以便让这些例子更清晰，并突出展示这些模型可以采用的不同策略。
> 
> 乌龙茶

* * *

**AIxBlock** @AIxBlock [2025-10-15](https://x.com/AIxBlock/status/1978506649166848340)

所以基本上… LLMs 学会“循环思考”。

* * *

**Alex L Zhang** @a1zhang [2025-10-15](https://x.com/a1zhang/status/1978508543654297793)

是的！虽然可以说它“循环思考”的机制在这里是独特的 :)

* * *

**Mike Taylor** @hammer\_mt [2025-10-15](https://x.com/hammer_mt/status/1978563912577474977)

延迟是多少？这在生产环境的聊天机器人中是否可行，还是说它需要用于批量任务？