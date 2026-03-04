---
title: "2026-03-03_OpenHands_OpenHands_对于编码代理来说_技能_是自动化重复性工作流程的好方法_但我们如何才能"
source: "https://x.com/OpenHandsDev/status/2028575626190279130"
author:
  - "[[@OpenHands]]"
published: 2026-03-03
created: 2026-03-03
description:
tags:
  - "#LLMs"
  - "#AI"
  - "x"
  - "@OpenHands"
---

# OpenHands 对于编码代理来说，“技能”是自动化重复性工作流程的好方法，但我们如何才能

**OpenHands**

对于编码代理来说，“技能”是自动化重复性工作流程的好方法，但我们如何才能知道它们是否能大规模发挥作用呢？ 我们深入探讨了如何记录、监控和提高代理人的技能，并举了一个构建定制化公关审核技能的真实案例。

![图片](https://pbs.twimg.com/media/HCbyx_uWAAA79qr?format=png&name=large)

* * *

### 热门回复

**@Haitham Bou Ammar** ♥ 321 · 💬 3

太棒了！扩散 #LLMs 终于开始整合了！ 干得好！ #AI #MachineLearning

**@Joël Niklaus** ♥ 125 · 💬 3

我们刚刚发布了 100BT 规模的预混合、预洗牌预训练数据集。 @asankhaya 我们测试了 50 多种不同的混合策略，规模达 10 亿。最终胜出的是什么？是 50% 的 finePDFs + 30% 的 DCLM + 20% 的 FineWeb-Edu 的静态混合方案。无需复杂的课程体系。 我们将规模扩大到 100BT，

**@OpenHands** ♥ 5 · 💬 1

为了简化我们的 PR 审核流程，我们开发了一个开源的 PR 审核插件，该插件可在 GitHub CI 中运行： https:// github.com/OpenHands/exte nsions/tree/main/plugins/pr-review … 但我们需要一种方法来知道它是否真的有帮助——而不仅仅是产生噪音。

**@OpenHands** ♥ 3 · 💬 1

步骤 1：记录所有数据。我们对智能体轨迹进行插桩以保存它们（通过 @lmnrai ）每个代理的操作都会被记录下来——它做了什么，它在哪里遇到了困难，哪些方法奏效了。

**@OpenHands** ♥ 3 · 💬 1

步骤 2：根据人类行为进行评估。每次 PR 合并后，我们都会检查：开发人员是否真正采纳了智能体的建议？ 准确率 = 已反映的建议 / 已提出的建议 这可以真实反映代理的质量，并且可以应用于其他用户案例！