---
title: "马天翼关于拉尔夫循环（Ralph Loop)的讨论"
source: "https://x.com/fkysly/status/2008862457591419364"
author:
  - "[[@fkysly]]"
date: "2026-01-08T11:18:01+08:00"
created: 2026-01-08
description:
tags:
  - "@fkysly # AI编程 #ClaudeCode #拉尔夫循环 #AI开发"
---
**马天翼** @fkysly [2026-01-07](https://x.com/fkysly/status/2008862457591419364/history)

最近又一个概念火了，叫拉尔夫循环（Ralph Loop）。

简单来说，就是你告诉 Agent 一个任务，比如：帮我生成一张图；Agent 开始执行，执行了很多轮之后，可能 Agent 就停下了，轮次上限到了；那有了这个拉尔夫循环的情况下，当 Agent 决定 "我完成了" 要退出时，拉尔夫会拦截这个退出，然后把同样的 prompt 再喂一遍。这个时候，Agent 之前的上下文还在（有的是持久化到了文件里，有的实现是复用上下文）、但是之前做的代码修改已经改掉了，Agent 会从上次停下来的地方继续干活。

这个有点像实习生觉得自己做完了就停了，然后老板甩着鞭子继续要求实习生干活，一直干到老板满意为止，这个形象很绝。

本质上，也是通过多轮迭代想要解决 LLM 上下文不够导致 Agent 不能很好完成长任务的问题。

目前流传最广的是说，有个老哥靠这个“鞭打”Agent，跑了一个 3 个月的循环，直接干出了一个完整的编程语言。

Claude Code 目前也支持了这个拉尔夫循环的插件：

---

**耳朵** @RookieRicardoR [2026-01-07](https://x.com/RookieRicardoR/status/2008877792059126152)

上下文不够一定不是这样做的，一定是子 SubAgent 去执行，具体见

> 2026-01-07
> 
> 强大的 Agent 至少应该包含什么？Orchestrator-Workers 任务委派、Evaluator-Optimizer 评估优化、Pipeline 管道、Circuit Breaker 断路器、State Machine状态机。
> 
> 最近 OpenCode 很令人好评的一点就是：能够同时驱动三家模型进行代码设计和编写，每家模型各有所长，充分发挥长处。 x.com/RookieRicardoR…
> 
> ![Image](https://pbs.twimg.com/media/G-AD6VVbcAAiasu?format=jpg&name=large)

---

**马天翼** @fkysly [2026-01-07](https://x.com/fkysly/status/2008890342146457604)

学习了。你意思是通过 一个监督的 subagent 去让其他 subagent 自我循环，直到产出达标对吧。

---

**marovole** @marovole [2026-01-07](https://x.com/marovole/status/2008876270537601430)

尝试用了一下，没掌握要领。可以讲下具体怎么能跑的久吗

---

**马天翼** @fkysly [2026-01-07](https://x.com/fkysly/status/2008889365003710690)

我也还没来得及尝试呢

---

**懒羊羊** @0Xweaksheep [2026-01-07](https://x.com/0Xweaksheep/status/2008888376695627943)

循环造屎吗

---

**comaple zhang** @comaple123 [2026-01-07](https://x.com/comaple123/status/2008905677939573121)

如果人类对 AI coding 产生了依赖那将是可怕的事情。

---

**程序员Left** @coder\_left [2026-01-07](https://x.com/coder_left/status/2008911155830689977)

听说/ralph-loop Plugin和planning-with-files skills更配哟  
听说拉尔夫循环插件和基于文件的规划技能更配哦

---

**Astra** @Astra448167 [2026-01-07](https://x.com/Astra448167/status/2008941949022355957)

这得花多少钱，太有钱了

---

**LonelyInvestorX** @webb\_dever [2026-01-07](https://x.com/webb_dever/status/2008902541451661692)

这个有点意思，不知道是怎么解决上下文爆炸。即使通过外部记忆，到最后也会影响性能和丢失早期细节

---

**GillianR** @GillianR2026 [2026-01-07](https://x.com/GillianR2026/status/2008908295864823850)

@crosg2026 非常有概念贩子的感觉

---

**Phoenix** @snipermaxxx [2026-01-07](https://x.com/snipermaxxx/status/2008945218675196244)

账单直接流泪了。

---

**KC** @ScarletKc\_ [2026-01-07](https://x.com/ScarletKc_/status/2008965746043523386)

买哪只股 推荐

---

**vewin** @lawgpts [2026-01-07](https://x.com/lawgpts/status/2009035378297024868)

token不够烧的。五小时120次都没有把？

---

**zorurume** @YehYungChien [2026-01-07](https://x.com/YehYungChien/status/2008966986722890118)

可以自製

---

**Alex\_tu** @York\_0831 [2026-01-07](https://x.com/York_0831/status/2009037374052028794)

纯靠AI自己判断自己的原生产物没有意义，比如写代码，你得让他跑端到端测试，模拟复杂场景才行

---

**lc liu** @llc7218 [2026-01-07](https://x.com/llc7218/status/2008951698555801762)

Claud 官方都出插件了

---

**Mr.Candy.AI** @ruiapp [2026-01-07](https://x.com/ruiapp/status/2008912196206498154)

英雄所见略同，我下午刚推荐了这个 claude code 插件