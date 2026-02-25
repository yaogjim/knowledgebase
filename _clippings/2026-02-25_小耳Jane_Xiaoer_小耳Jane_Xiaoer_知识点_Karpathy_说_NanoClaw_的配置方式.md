---
title: "2026-02-25_小耳Jane_Xiaoer_小耳Jane_Xiaoer_知识点_Karpathy_说_NanoClaw_的配置方式"
source: "https://x.com/xiaoerzhan/status/2026179786008048111"
author:
  - "[[@小耳Jane｜Xiaoer]]"
published: 2026-02-25
created: 2026-02-25
description:
tags:
  - "x"
  - "@小耳Jane｜Xiaoer"
  - "https"
  - "twimg"
---

# 小耳Jane｜Xiaoer 知识点： Karpathy 说 NanoClaw 的配置方式

**小耳Jane｜Xiaoer**

知识点： Karpathy 说 NanoClaw 的配置方式 "slightly blew my mind"。 我去研究了一下，发现确实是个新思路。 先说问题： OpenClaw 有 40 万行代码。 你想加个 Telegram？改配置文件。 想换个数据库？改配置文件。 想加个新功能？改配置文件。 配置文件越来越长，if-else 越来越多，最后没人看得懂。 NanoClaw 的做法完全不同—— 它的核心只有大约 2000 行代码。 没有配置文件。 所有定制都通过 Skills 完成： 你想接入 Telegram。 输入 /add-telegram。 AI 读取这份 Skill 文档，然后自己去： → 安装 Telegraf 依赖 → 在源码里加上 Telegram 消息处理 → 帮你配好 Bot Token → 测试连通 创始人 Gavriel Cohen 在采访里说了一句很关键的话： "如果一个软件加了一堆你不需要的功能，那它对你来说就变差了——更大、更不安全、而且你用不到。" 所以 NanoClaw 的理念是：核心极简，需要什么功能，让 AI 在编译时加进去。 每个人部署出来的 NanoClaw 都不一样——只包含你真正用到的代码。 还有一个细节： 整个 NanoClaw 的源码只有大约 35000 tokens。 Claude 的上下文窗口是 200K tokens。 也就是说，AI 可以一次性读完整个项目的所有代码，完全理解，然后一次性写出新功能。 OpenClaw 的 40 万行？AI 根本塞不进上下文。 这就是为什么 Karpathy 说 NanoClaw "fits into both my head and that of AI agents"——人能看懂，AI 也能看懂。 Cohen 还提了几个 AI 时代写代码的新原则： ① DRY（不重复代码）可能过时了——因为 AI 改共享函数时不考虑下游影响，重复代码反而更安全 ② 严格的文件行数限制可能过时了——AI 花更多时间重构而不是写功能 ③ 代码不需要"经得起时间考验"——6 个月后更好的模型会帮你重写 如果你对 Claw 生态感兴趣但不敢碰 OpenClaw，从这个开始就对了。

![图片](https://pbs.twimg.com/media/HBz7mataoAAALPU?format=jpg&name=large)

> **@xiaoerzhan**
> 
> Karpathy 刚花了一个周末研究 Claw 生态，结论是： OpenClaw 概念牛逼，但 40 万行 vibe code + 正在被大规模攻击 = 安全雷区。 他推荐了一批更小、更安全的替代品，我帮你整理好了： ![🦞](https://abs-0.twimg.com/emoji/v2/svg/1f99e.svg) NanoClaw — ~4000 行代码，容器隔离，他重点推荐 ![🦀](https://abs-0.twimg.com/emoji/v2/svg/1f980.svg) ZeroClaw — Rust 写的，<5MB 内存，$10 硬件能跑 ![🐹](https://abs-0.twimg.com/emoji/v2/svg/1f439.svg)

![👂](https://abs-0.twimg.com/emoji/v2/svg/1f442.svg)![🦞](https://abs-0.twimg.com/emoji/v2/svg/1f99e.svg)![🦀](https://abs-0.twimg.com/emoji/v2/svg/1f980.svg)![🐹](https://abs-0.twimg.com/emoji/v2/svg/1f439.svg)![引用图片](https://pbs.twimg.com/media/HBz7mataoAAALPU?format=jpg&name=large)

* * *

### 热门回复

**@Marven11** ♥ 3 · 💬 1

什么叫根据skill修改源码，这个世界真的疯了

**@NerdC** ♥ 2 · 💬 1

nanoclaw其实是claude code的wrapper，今天claude code的remote control出来之后就没必要用它了。 更详细龙虾变种集合请看： https:// openclawindex.pages.dev

**@es05** ♥ 0 · 💬 1

It's a massive economic mismatch: using expensive inference to solve a cheap if-else config. It’s like using a laser-guided missile to swat a fly—then charging the user a "Token Tax" for the gamble. Why pay to play "code roulette"?

**@TenSteps** ♥ 0 · 💬 1

这个理念超棒的！等你vibe了一堆定制功能后，上游发了个安全补丁…………

**@Crazyox** ♥ 0 · 💬 1

配置文件地狱真的太痛苦了