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
  - "https"
  - "2025-11-18"
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

**Starlink** @Starlink

Starlink Mini offers fast, reliable internet on the go—great for traveling, camping, exploring, boating, RVing, and more.

Stay connected without dead zones or slow speeds.

Order online in under 2 minutes.

星链迷你版提供快速可靠的移动网络，非常适合旅行、露营、探险、划船、房车出行等多种场景。

保持连接，无死角，不卡顿。

两分钟内完成在线下单。

* * *

**TSLA99T** @Tsla99T [2025-11-18](https://x.com/Tsla99T/status/1990893516579320063)

“但是并没有解决多少问题”：大错特错

这是他早在2017年提出的概念

对于我们2018-2020年的FSD研发上产生了深远的影响

* * *

**宝玉** @dotey [2025-11-18](https://x.com/dotey/status/1990894003479322767)

是我孤陋寡闻了

* * *

**LukeWang** @xxaccp [2025-11-18](https://x.com/xxaccp/status/1990655899669836226)

软件工程中一个需求的可验证性如何实现，TDD测试驱动吗

* * *

**宝玉** @dotey [2025-11-18](https://x.com/dotey/status/1990660267642949836)

这就说到点子上了，实际上 TDD 只能验证模块，而 Software 2.0 理想中的验证是直接验证产品

* * *

**𝙩𝙮≃𝙛{𝕩}^A𝕀²·ℙarad𝕚g𝕞** @TaNGSoFT [2025-11-18](https://x.com/TaNGSoFT/status/1990613793865609341)

所以AK才天然和宝玉老师耦合啊

看来商单对10万fo以上的大V老师免疫

* * *

**素人极客-Amateur Geek** @changli71829684 [2025-11-18](https://x.com/changli71829684/status/1990615285825733002)

能把具象的现象，抽象为概念，并且十分容易能让人接受和秒懂，这个能力太刺激了。

世界上有三种人非常有魅力。

1）概念提炼者：他们能把零散发生的事情压缩成一两个清晰的概念，让人立刻抓住问题的本质。

* * *

**Xinchun Qian** @ZhiyiQian [2025-11-18](https://x.com/ZhiyiQian/status/1990787125474963700)

他不算是“发明新的概念”吧，我感觉他往往更像是把大家都遇到的新状态/新问题/新场景，用一个基本贴切的概念总结了一下（并且经常也能直指这个新状态/新问题/新场景的核心）。这对后续大家的交流和讨论还是有帮助的。

* * *

**阿兹特克小羊驼** @AztecaAlpaca [2025-11-18](https://x.com/AztecaAlpaca/status/1990615752827961658)

看到AK又发推了，宝玉老师的心情⬇️⬇️⬇️

![Image](https://pbs.twimg.com/media/G6AWXbCbMAQWtsY?format=png&name=large)

* * *

**Ro** @ro

Struggling with ED? Ro Sparks get you harder, faster, if prescribed.

Compounded, not FDA approved. See safety info link on image.

为勃起障碍而困扰？若经医生处方，罗火花能让您更快、更坚挺。

复合配方，未经食品药品监督管理局批准。请参阅图片上的安全信息链接。

* * *

**MetaGPT** @MetaGPT\_ [2025-11-18](https://x.com/MetaGPT_/status/1990739233254916369)

Frameworks evolve, but good ones stick around.

框架会不断演变，但优秀的框架总能经久不衰。

* * *

**Runkun Miao** @\_rain\_miao\_ [2025-11-19](https://x.com/_rain_miao_/status/1990970802154713186)

可能是因为andrej也没有一个解决方案。整个行业都是长期处在从1.0到2.0的状态。有些场景跑得快一点，有些场景跑得慢

* * *

**waroy** @0xWaroy [2025-11-18](https://x.com/0xWaroy/status/1990659353817591946)

好的概念阐述，可以让人少走好多弯路。

做对的事，比做很多事重要得多了。

* * *

**Kateiso U** @KateisoCao [2025-11-19](https://x.com/KateisoCao/status/1990993419586408884)

从语言学角度看，无论新概念是否解决问题，都有重大意义的。

例如，如无“股票”概念，那我们会称其为“反映实际价值，用于交易的一种…”，此为一因。计算机中各概念同理。

另外，开创新概念，就有了定义这个词的权利，益于个人影响力。当我们想到“AI自己来编程”我们就会想到Vibe Coding，就会想到AK

* * *

**X** @ohyourgod\_x [2025-11-18](https://x.com/ohyourgod_x/status/1990632784340426865)

Software 2.0还好😂，已经不算新了是他很久之前就开始说。我印象中几乎和vibe coding同一时期的产物。他又拿出回来提一下。

* * *

**你的伊芙琳** @lover\_reze [2025-11-18](https://x.com/lover_reze/status/1990614035931476246)

大佬喜欢秀 thought leadership，只给方向、落不落地另说，让路人粉不明觉厉