---
title: "2025-11-19_dotey_一方面我不喜欢_Andrej_Karpathy_总是发明新的概念_一方面又不得不承认他确实很多想法是"
source: "https://x.com/dotey/status/1990612409900273746"
author:
  - "[[@dotey]]"
published: 2025-11-19
created: 2025-11-19
description:
tags:
  - "x"
  - "@dotey"
  - "ai"
  - "https"
---

# 一方面我不喜欢 Andrej Karpathy 总是发明新的概念，一方面又不得不承认他确实很多想法是

**宝玉** @dotey 2025-11-16

一方面我不喜欢 Andrej Karpathy 总是发明新的概念，一方面又不得不承认他确实很多想法是很有价值的。

比如这里对 Software 1.0/2.0 的定义就挺好的：

1). 软件1.0时代，容易自动化的是你能明确告诉计算机怎么做的事情。

2). 软件2.0时代，容易自动化的是你能自动验证结果好坏的事情。

那这里的自动化都什么意思呢？

1\. 软件1.0：靠指定规则（Specify Rule）自动化

过去的几十年，我们用的所有传统软件（比如Excel、Word、会计系统），都是“软件1.0”。

它的核心逻辑是“指定”（Specify）。

你必须像个事无巨细的监工，把每一个规则都用代码写得清清楚楚。比如做个会计软件，你必须告诉它：

“如果A栏的数字大于B栏，那么C栏就显示红色。”“月末，把所有D栏的数字加起来，放到Z栏。”

软件1.0擅长什么？ 自动化那些规则固定、逻辑清晰的任务。

软件1.0解决的是什么问题呢？ 是人类的“机械性重复劳动”。比如打字员、记账员、算账员。只要一个任务的全部流程能被清晰描述出来，软件1.0就能接管它。

2\. 软件2.0：靠指定目标（Specify Objective）自动化

现在，AI 来了，升级到了软件2.0。

它的逻辑完全变了。我们不再是指定规则，而是设定目标。

我们不再像监工一样告诉AI每一步怎么做，而是像个教练，只告诉它验收的标准是什么。

比如训练AI下棋。我们不告诉它“当对方出这一招，你就必须走那一步”。我们只给它一个目标：“想办法赢棋”。

然后，AI 就开始自己搜索那个能赢棋的步骤。它通过海量的自我对弈（也就是梯度下降）来寻找最佳策略。

这就是 AK 的核心观点：软件1.0是我们手动写程序，软件2.0是AI自动搜索生成程序。

3\. 软件 1.0 时代看“可指定性”（Specifiability），2.0 时代看“可验证性”（Verifiability）。

如果说软件 1.0 自动化任务的标准是我们能不能指定清晰的规则，比如说你要写个自动抓取的爬虫，只要指定清晰饿抓取规则和解析规则就可以了。

那么软件 2.0 自动化任务的标准则是结果是不是能自动被验证。

“可验证性”就是AI能不能在一个任务上进行高效的“刻意练习”。

AK 给出了“可验证”的三个关键条件：

1). 可重置 (Resettable)

AI必须能够无限次地重新开始尝试。比如下棋，这局输了，没关系，棋盘一清，马上开下一局。

2). 高效率 (Efficient)

AI的练习速度必须远超人类。它可以在一小时内“看”完人类一辈子都看不完的视频，一天内下几百万盘棋。

3). 可奖励 (Rewardable)

这是最关键的一点。必须有一个自动化的、即时的、没有争议的奖惩机制。

自动化至关重要。如果AI每次做完一件事，都需要一个人类专家来看半天，然后给个模棱两可的评价（比如“嗯，这个创意还行”），那AI就没法高效学习。

像在编程、数学领域就很容易符合上面的三个条件，但是像写作这种非标准化的就很难验证。

但对于软件来说，稍微复杂一点的软件系统，其实很难达到可验证的标准。

比如说我在实现 UI 时，会尝试把 UI 设计稿扔给 AI，然后给 AI 一个截图工具，让它反复截图对比设计稿，然后找出差异优化，但是以目前的 AI 能力，还不足以修复这些差异，所以无论你运行多久，也不会真的得到一个理想的结果。

这可能就是我不太喜欢 AK 发明的这些新概念的原因，总是提出一个个概念，但是并没有解决多少问题。

> 2025-11-16
> 
> Sharing an interesting recent conversation on AI's impact on the economy.
> 
> AI has been compared to various historical precedents: electricity, industrial revolution, etc., I think the strongest analogy is that of AI as a new computing paradigm (Software 2.0) because both are
> 
> 分享一段近期关于人工智能对经济影响的精彩对话。
> 
> 人工智能常被比作历史上的诸多先例：电力、工业革命等。但我认为最贴切的类比，是将人工智能视为一种新的计算范式（软件2.0），因为二者都

* * *

**宝玉** @dotey [2025-11-18](https://x.com/dotey/status/1990614486957322609)

这配图画的挺好的👍

https://x.com/zhengyaojiang/status/1990218960617492784…

> 2025-11-17
> 
> Love this framing！
> 
> This is exactly what we’re building at Weco:
> 
> \- you write an eval script (your verifier)
> 
> \- Weco iterates on the code to optimize it against that eval
> 
> Software 1.0: write the process
> 
> Software 2.0: write the evaluation x.com/karpathy/statu…
> 
> 这个角度太棒了！
> 
> 这正是我们在 Weco 构建的目标：
> 
> \- 你编写一个评估脚本（你的验证器）
> 
> \- Weco 对代码进行迭代，以根据该评估进行优化
> 
> 软件 1.0：编写流程
> 
> 软件 2.0：编写评估 x.com/karpathy/statu…
> 
> ![Image](https://pbs.twimg.com/media/G6AVO43XUAAB2wy?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G56tmABWQAEmAxp?format=jpg&name=large)

* * *

**TSLA99T** @Tsla99T [2025-11-18](https://x.com/Tsla99T/status/1990893516579320063)

“但是并没有解决多少问题”：大错特错

这是他早在2017年提出的概念

对于我们2018-2020年的FSD研发上产生了深远的影响