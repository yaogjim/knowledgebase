---
title: "2026-01-06_brucexu_eth_Amazing_使用_LangGraph_和之前版本_去年使用_Claude_Code_sonne"
source: "https://x.com/brucexu_eth/status/2007582420133130312"
author:
  - "[[@brucexu_eth]]"
published: 2026-01-06
created: 2026-01-06
description:
tags:
  - "x"
  - "@brucexu_eth"
  - "https"
  - "2026-01-04"
---

# Amazing! 使用 LangGraph 和之前版本（去年使用 Claude Code sonne

**brucexu.eth** @brucexu\_eth [2026-01-03](https://x.com/brucexu_eth/status/2007582420133130312)

Amazing! 使用 LangGraph 和之前版本（去年使用 Claude Code sonnet 4.1 写了三个月）的经验再加上更强悍的 Codex，即便算上 bun 踩坑，也只花了 12 个小时就完成了新版 @VibemanAI MVP！一月份一定发布不能再等了。这效率周末和业余时间开发都完全足够了。

这核心 API 的设计太美妙了，自己之前第一代写了很多屎一样代码，对比确实差了很多。回顾一下我感觉有几个学到的经验：

1\. 先有业务场景和需求，才会有后面的探索、尝试和迭代。如果不做这个，我根本也完全不会接触 DAG、图等。所以学习编程的好方法肯定不是啃书或者系统性的刷视频，而是找到自己感兴趣的项目做中学。经过 AI 的评估，我的实现已经接近 40-50% 了，再重构一到两次估计能做个山寨版的。不过现在可以省事直接用了。

2\. 多调研。基于之前的经验，我主要了解和选择 state machine，所以原本打算使用 xstate 来重构第二版。但是后来我用三大模型一起分析和推荐技术架构，发现 LangGraph 频繁被提到，所以研究了一下发现这就是我需要的。所以高级程序员在新时代可能会遇到的一个问题就是路径依赖。要时刻保持开放，这次我也尝试了 Bun，虽然踩了一些坑但是也学到了新东西。构建性能飞升。

3\. 底层和复杂度很高的框架或者计算机问题，需要从学术层面入手和应用。LangGraph 的设计参考了 Google 的 Pregel 算法，主要参考两篇论文：Pregel: a system for large-scale graph processing（SIGMOD 2010, Malewicz et al.）——提出 Pregel 的图计算模型：每轮迭代顶点收消息、更新状态、发消息；A Bridging Model for Parallel Computation（CACM 1990, Leslie G. Valiant）——BSP 模型的经典论文：把并行计算抽象成一轮轮同步的计算 + 通信 + barrier。

当我在苦思夜想怎么设计这个 workflow 的时候，不断抽象我感觉条件、逻辑、存储、重试和 audit，情况好多好复杂，已经超出了我的脑容量。实际上可能论文或者过去的学术研究早已经有答案了。这一点也非常适合借助 AI 来寻找和研究，找到答案。学习了🫡

立个 flag，一月份绝对发布 @VibemanAI，要实现的目标就是帮你从 10x 程序员变成 100x。感兴趣可以找我报名内测。

![Image](https://pbs.twimg.com/media/G9xdkWzbMAAZS_-?format=jpg&name=large)

* * *

**非典型程序员** @null12022202 [2026-01-04](https://x.com/null12022202/status/2007633076525150277)

看见这段代码就忍不住想把它再重构一下，哈哈

* * *

**Burneek** @Burneek

⚡️ HALO Sauna - your at-home spa for deeper sleep, improved well-being, and total relaxation. Get a free Cold Plunge today only.

1-Year Warranty.

Free 2-Day Shipping.

100-Day Money-Back Guarantee.

⚡️ HALO Sauna - 你在家的水疗，助你深度睡眠、改善健康并彻底放松。今日仅限免费体验冷水浴！

1年保修

免费2天送达

100天退款保证

* * *

**C.mathresearcher** @hubo1989 [2026-01-04](https://x.com/hubo1989/status/2007669841604592065)

怎么报名？

* * *

**Lulu ⟠** @FryCookVC [2026-01-04](https://x.com/FryCookVC/status/2007630930543104029)

excitedly watching 🔥🔥💪

兴奋地看着 🔥 🔥 💪

* * *

**Nekoneko Studio** @0x2218\_Nekoneko [2026-01-04](https://x.com/0x2218_Nekoneko/status/2007721956653846763)

必须报名

* * *

**Kuncle** @\_Kuncle [2026-01-04](https://x.com/_Kuncle/status/2007626893793898629)

内

* * *

**sandra** @sandraaasol [2026-01-03](https://x.com/sandraaasol/status/2007582684810490045)

how do you plan to measure the real impact of this vpm tech on developer productivity across teams

你打算如何衡量这项 VPM 技术对各团队开发者生产力的实际影响？