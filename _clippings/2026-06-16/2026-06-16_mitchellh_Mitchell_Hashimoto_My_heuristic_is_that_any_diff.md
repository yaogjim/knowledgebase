---
title: "2026-06-16_mitchellh_Mitchell_Hashimoto_My_heuristic_is_that_any_diff_a"
source: "https://x.com/mitchellh/status/2066645959539556852"
author:
  - "[[@mitchellh]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "x"
  - "@mitchellh"
  - "💬"
  - "hashimoto**"
---

# Mitchell Hashimoto: My heuristic is that any diff an agent generates over ~1500 lines is too big and…

**Mitchell Hashimoto**

我的启发式是，任何代理生成的超过 1001 到 1500 行的 diff 都太大，这表明问题需要分解。这是我现在进行功能开发时的一般模式：

尝试在松散指导下实现整个功能。我将此称为“画猫头鹰”提示，参考那个梗。预期会得到垃圾，你会得到垃圾。

2\. 如果 diff 小于 1500 行，审查并正常迭代。如果 diff 大于 1500 行，提示代理将问题分解为原子级、增量式、可审查的任务。同时，你自己也要这样做。

3\. 代理往往会将这些任务设置得过于具体，只针对他们解决的那种形式。你需要将其调整为合适的通用形式。照做即可。

4\. 启动新代理处理那些增量任务（尽可能并行化）。应用相同的规则。

5\. 在某个特定时刻，重复“画猫头鹰”的提示。在某个时候，你将低于你的审查能力阈值。

这一过程始终产出高质量、可维护、可审查的代码块，这些代码块能够很好地交接，既可以直接合并，也可以进行人工优化。

而且，在最新前沿模型处于高思维水平的情况下，这些模型的速度都足够慢，通常你可以同时运行多个，而你正在积极查看其他任务或处理自己的任务时。

HITL（human-in-the-loop）代理仍然非常重要，特别是在功能开发工作中。功能在用户界面（UI）、应用程序编程接口（API）等方面触及了人机交互的边界。而全新的内容可能会在架构中引入病态问题，这些问题会违反预期的不变量（这些不变量本应在规范或测试中体现，但我们并不完美！）

我了解到很多前沿的智能体论述都围绕着“循环”以及智能体持续驱动智能体展开。我也做了一些相关工作（稍后会对此进行报告）。不过，在日常需要实际完成任务的工作中，这是我目前最有收获的模式。

* * *

### 热门回复

**@iDenfy** ♥ 607 · 💬 22

Stop overpaying for denied KYC verifications while onboarding customers to your dApps, crypto wallets, exchanges, RWA tokenization platforms or NFT marketplaces

**@Mitchell Hashimoto** ♥ 18 · 💬 2

只有当你能够完美地度量代码的行为时，这一点才成立。我们做不到。代理目前也无法生成完美的覆盖率。这会引入你本想避免但未能明确说明的病态情况。审查是解决这个问题的唯一方法。

**@Valigator** ♥ 6 · 💬 3

Introducing Holdfast: a non-custodial Solana stake manager for Chrome.

Every operation in the stake program. Activate, split, merge, deactivate, withdraw, transfer authority. Ledger, Keystone, and Trezor hardware wallet support.

Private beta open now →

**@Mitchell Hashimoto** ♥ 9 · 💬 0

随意且适合我，适应你自己的代码库

**@HSVSphere** ♥ 8 · 💬 0

在允许你通过类型/可验证的代码片段表达更多内容的语言中效果更佳。你定义函数类型、粗略的枚举，而 LLMs 填补空白。这尤其适合从规范重新实现，因为需要做什么已经为你确定好了，你只需要