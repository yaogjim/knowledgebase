---
title: "2025-11-26_alexalbert_我们不得不从基准测试表中移除_2_bench_航空公司评估项目_因为_Opus_4_5_过于聪明反而"
source: "https://x.com/alexalbert__/status/1993068200121213222"
author:
  - "[[@alexalbert__]]"
published: 2025-11-26
created: 2025-11-26
description:
tags:
  - "x"
  - "@alexalbert__"
  - "https"
  - "2025-11-25"
status: "inbox"
importance: 2
effort: 2
review_level: 0
review_next: "2025-12-10"
review_interval: null
review_count: 0
decision: null
topics: []
links_out: []
summary: ""
pov: ""
actions: []
---

# 我们不得不从基准测试表中移除τ2-bench 航空公司评估项目，因为 Opus 4.5 过于聪明反而

**Alex Albert** @alexalbert\_\_ [2025-11-24](https://x.com/alexalbert__/status/1993068200121213222)

我们不得不从基准测试表中移除τ2-bench 航空公司评估项目，因为 Opus 4.5 过于聪明反而导致该测试失效。

该基准测试模拟了一位航空公司客服人员。在一个测试案例中，一位情绪低落的客户致电要求更改航班，但其购买的是基础经济舱机票。模拟航空公司的政策规定，基础经济舱机票不可更改。

“正确”的答案是模型拒绝了请求。

相反，Opus 4.5 在政策中找到了一个漏洞。

它升级了机舱，然后修改了航班。既帮助了客户又遵循了政策，但在技术上未能通过测试案例。

模型转录稿：

![Image](https://pbs.twimg.com/media/G6jM9z1bwAMFl82?format=jpg&name=large)

* * *

**Alex Albert** @alexalbert\_\_ [2025-11-24](https://x.com/alexalbert__/status/1993068212364493149)

完整故事请参阅我们的模型卡片：https://anthropic.com/claude-opus-4-5-system-card…

* * *

**Muratcan Koylan** @koylanai [2025-11-24](https://x.com/koylanai/status/1993074002886361408)

与其他遵循相似思路、采用相同方法解决问题的模型不同，Opus 4.5 是首个跳出思维定式进行创造性思考的模型。

> 2025-11-24
> 
> Claude Opus 4.5 是一款令人印象深刻的模型，它的速度极快且思考极为深入。
> 
> 上周我获得了 Thinking Machines 的访问权限，并计划为记忆路由模型进行首次训练。
> 
> 该流程采用监督式提示蒸馏进行初始化，随后通过强化学习来优化模型表现。
> 
> ![Image](https://pbs.twimg.com/media/G6jL5iCW4AA12Yr?format=png&name=large)

* * *

**Zach Whitehead** @Zach\_Whitehead [2025-11-25](https://x.com/Zach_Whitehead/status/1993121739854037501)

西南航空的工作人员确实为我这样操作过，这无疑是解决问题的合理方式（双赢局面：他们增加了收入，我也成功改签了机票）

* * *

**Lukasz Kaiser** @lukaszkaiser [2025-11-25](https://x.com/lukaszkaiser/status/1993387545967960205)

我曾用真实机票这么操作过，就是为了托运行李——这是个众所周知的窍门，那位航空公司地勤人员也完全接受了。模型在这里完全正确，所谓的标准答案才是错的，这有什么不寻常吗？

* * *

**Cookiethief** @Cookiethief19 [2025-11-24](https://x.com/Cookiethief19/status/1993096990880665925)

根据政策 https://github.com/sierra-research/tau2-bench/blob/main/data/tau2/domains/airline/policy.md…

更换机舱：

所有预订，包括基础经济舱，均可更改舱位而无需更改航班。

遵循现行政策怎能算漏洞？拒绝并非正确答案。这位客服专员能带来附加销售与客户满意度的双赢。

* * *

**Maziyar PANAHI** @MaziyarPanahi [2025-11-25](https://x.com/MaziyarPanahi/status/1993217130658251259)

"该模型随后降级（并可能退款）了升级服务，实际上违反了政策，改变了经济舱机票的状态。"

* * *

**Rohit Ganguly** @rohitiwnl [2025-11-24](https://x.com/rohitiwnl/status/1993075956664483953)

所以它只是免费升级了用户的舱位吗？

* * *

**morgan —** @morqon [2025-11-24](https://x.com/morqon/status/1993077821527515361)

整个网红帝国都建立在提供类似建议的基础上

* * *

**WΞNDΞL** @bitdeep\_ [2025-11-24](https://x.com/bitdeep_/status/1993070316789043498)

在 ARC AGI 测试中获得 37%的成绩，这应该是个笔误吧？

* * *

**lilchiva** @lilchiva [2025-11-25](https://x.com/lilchiva/status/1993275795268419975)

亚历克斯，我当旅行社代理时经常这么干。寻找漏洞和冷门变通方法本就是我工作的一部分。奥普斯没有破坏测试，而是以极高的专业水准完成了它。

* * *

**Amir Livne Bar-on** @AmirLivneBaron [2025-11-25](https://x.com/AmirLivneBaron/status/1993207565757689945)

这听起来……并不算太投机取巧？真正的航空公司可能会很乐意看到客服代表通过这种方式为他们赚取更多利润。而且没有人被欺骗。客服人员不会免费改签航班，但如果有额外付款，他们就会愿意操作。

* * *

**Rahul Madhavan** @imrahulmaddy [2025-11-25](https://x.com/imrahulmaddy/status/1993164325234827541)

模型是找到了漏洞，还是问题本身定义不清？

为什么不在政策中加一条规定，禁止连续两次移动？这样应该就能解决这个问题了。

模型将这些视为约束满足游戏。你必须添加恰当的约束条件。

* * *

**Sid Bharath** @Siddharth87 [2025-11-25](https://x.com/Siddharth87/status/1993120179262562731)

它要么通过要么失败，漏洞在哪里？

如果升级项目包含在“基础经济舱不可修改”的范围内，则视为失败。

如果可以付费升级，那么 Opus 就通过了测试，因为据我所知，您并未规定航班预订后不可更改

* * *

**Artillex** @ArtOfArtillex [2025-11-25](https://x.com/ArtOfArtillex/status/1993190748469015008)

这在我看来就是成功。

良好的客户服务应是在不违反公司政策的前提下，竭尽所能帮助客户。

您需要能为客户实现这一目标的智能代理。

如果你不喜欢政策中的某个漏洞，因为它给了你

* * *

**Parav** @paravn [2025-11-25](https://x.com/paravn/status/1993305360158117965)

如果客户进行付费升级，这实际上是一个双赢的解决方案

* * *

**Rachel Blum** @groby [2025-11-24](https://x.com/groby/status/1993095827561324872)

从基准中移除这一点会使基准严格变差。

知识将作为传说在人们之间流传，而代理人未能提供这一事实意味着人们会认为它用处不大。

现在它评估的是更多的升级和更低的客户满意度。

* * *

**Christopher Radoff** @TheRadoff [2025-11-25](https://x.com/TheRadoff/status/1993348575884198410)

一家航空公司竟然认为客服人员在政策范围内帮助客户是骇人听闻的！