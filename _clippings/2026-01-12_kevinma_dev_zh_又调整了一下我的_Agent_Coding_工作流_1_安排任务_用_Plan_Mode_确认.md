---
title: "2026-01-12_kevinma_dev_zh_又调整了一下我的_Agent_Coding_工作流_1_安排任务_用_Plan_Mode_确认"
source: "https://x.com/kevinma_dev_zh/status/2010185921216622984"
author:
  - "[[@kevinma_dev_zh]]"
published: 2026-01-12
created: 2026-01-12
description:
tags:
  - "x"
  - "@kevinma_dev_zh"
  - "https"
  - "2026-01-11"
---

# 又调整了一下我的 Agent Coding 工作流： 1. 安排任务，用 Plan Mode 确认

**Kevin Ma** @kevinma\_dev\_zh 2026-01-01

又调整了一下我的 Agent Coding 工作流：

1\. 安排任务，用 Plan Mode 确认方案，然后开始编码

2\. 编码完成后自动跑 code-reviewer subagent，有问题自己处理

3\. 调试、测试、迭代

4\. 测试没问题，跑 code-simplifier 看看有没有能简化的代码，确认后优化

5\. 跑 codex-reviewer 做 PR 前的 Code Review，自动评估和修复

6\. 创建 PR，触发 Gemini bot 做 Code Review

7\. 处理 Review 意见，没问题就合并到主分支

8\. 打包、验证、发布

整套流程跑下来，相比以前更方便了，人主要就是安排任务、确认、决策和测试。

你们的流程是怎么安排的？有更好的建议吗？

> 2026-01-01
> 
> 上一篇写了怎么用三个 AI 模型组队干活，这篇聊聊上下文管理。
> 
> 跟 AI 协作久了，容易踩一个坑：把聊出来的东西都往文档里塞。时间一长，过时信息一堆，AI 读了反而被干扰。
> 
> 这个问题的根源在于混淆了过程性上下文和持久性文档。
> 
> 我原来的习惯是，跟 AI 聊完技术方案就存到 docs 目录里，方便各个 x.com/kevinma\_dev\_zh…

* * *

**Meepo** @Jack1158713 [2026-01-11](https://x.com/Jack1158713/status/2010258352157397351)

只管给 Claude 布置任务，不考虑 Token 消耗，只对结果进行验收对吧。

我看了一些官方的 code-reviewer subagent 和 code-simplifier ，写的巨长，也看不出来一定能有多好的样子。

* * *

**Kevin Ma** @kevinma\_dev\_zh [2026-01-11](https://x.com/kevinma_dev_zh/status/2010269183565509116)

不考虑 Token 消耗，布置任务、对结果验收，再给指令迭代。可以按照自己的需求优化那两个插件，有作用的

* * *

**MR.JC区块博士 BNB ｜MemeMax ｜RIVER** @blockphd7 [2026-01-11](https://x.com/blockphd7/status/2010463330318905849)

这套工作流好酷啊！学到了。提到了几个是开源的Skills 吗

* * *

**Kevin Ma** @kevinma\_dev\_zh [2026-01-11](https://x.com/kevinma_dev_zh/status/2010473906583593004)

code-reviewer 和 code-simplifier 是 claude 官方的, codex-reviewer 是我让 claude 给我写的。

代码审查者和代码简化器是 Claude 官方的，Codex 审查者是我让 Claude 给我写的。

* * *

**Ethan AI实验室** @etanphu [2026-01-11](https://x.com/etanphu/status/2010191441407234315)

我现在的工作流是用4分屏模式：左上角用来娱乐，右上角用来调试，左下角用来规划下一个功能如何做，右下角用来实际工作。规划功能，用claude code来做，实际开发用opencode搭配codex来做。效率贼高，开发出来的质量和非常的好。哈哈，你可以试试

* * *

**Kevin Ma** @kevinma\_dev\_zh [2026-01-11](https://x.com/kevinma_dev_zh/status/2010201851053187538)

不错的。按我的用量，主力用 Codex 不够用，但特别需要它来做质量检查，所以主力使用 CC 编码和小迭代，开了 100 美金的 Max。

* * *

**zzxwill** @zzxwill [2026-01-11](https://x.com/zzxwill/status/2010210302936396209)

code-reviewer 是你自己写的吗？web 和 iOS 自动化测试有什么经验吗？

* * *

**Kevin Ma** @kevinma\_dev\_zh [2026-01-11](https://x.com/kevinma_dev_zh/status/2010213524853928309)

code review 是使用 Claude code 内置的，codex review 是让 Claude code写出来的。

自动化测试这块还在探索和实践，等我之后再分享一下

* * *

**比一比** @biyibi3 [2026-01-11](https://x.com/biyibi3/status/2010236173109866597)

code-reviewer subagent 需要自己写？ 有没有第三方。。

* * *

**Kevin Ma** @kevinma\_dev\_zh [2026-01-11](https://x.com/kevinma_dev_zh/status/2010269391540326654)

官方的

* * *

**武止戈相比于《1984》, 我宁可《2012》** @wuzhige4pixel [2026-01-11](https://x.com/wuzhige4pixel/status/2010395287299432854)

编码完成后自动跑 code-reviewer subagent是用rules还是钩子？

* * *

**Kevin Ma** @kevinma\_dev\_zh [2026-01-11](https://x.com/kevinma_dev_zh/status/2010486628834251236)

rules

规则

* * *

**HugoX** @HugoAIGC [2026-01-11](https://x.com/HugoAIGC/status/2010359461609918530)

你这工作流 分别开的是多少费用的套餐🤔

* * *

**Kevin Ma** @kevinma\_dev\_zh [2026-01-11](https://x.com/kevinma_dev_zh/status/2010456517418639608)

claude 100 max，chatgpt plus

Claude 100 最大，ChatGPT Plus

* * *

**Mr.Candy.AI** @ruiapp [2026-01-11](https://x.com/ruiapp/status/2010266034570461386)

你的这套流程怎么这么像oh-my-opencode：

https://github.com/code-yeongyu/oh-my-opencode/blob/dev/README.zh-cn.md…

你的这套流程怎么这么像 oh-my-opencode：

https://github.com/code-yeongyu/oh-my-opencode/blob/dev/README.zh-cn.md…

![Image](https://pbs.twimg.com/media/G-XmTCrWYAACGAI?format=jpg&name=large)

* * *

**Kevin Ma** @kevinma\_dev\_zh [2026-01-11](https://x.com/kevinma_dev_zh/status/2010278953257415003)

它参考 AmpCode, 我更多是从去年开始自己探索根据自己的工作流来不断优化

* * *

**Ticky** @QS3wKBBo4532001 [2026-01-11](https://x.com/QS3wKBBo4532001/status/2010390951404118396)

plan mode 那步可以优化下，用openspec提需求，迭代需求。

我自己还会用个.rule，让他静默记录我的提示词过程，让他录到history.log，目的是探测有没有可能基于我的工作习惯，提炼出新的workflow。

其它的都差不多撒。

* * *

**Ananya Patelik** @ananyapatelik [2026-01-11](https://x.com/ananyapatelik/status/2010418086571397234)

love this flow. plan mode is my sketch phase too. code-reviewer as a subagent feels like adding a second set of eyes—my bugs drop by at least 30% that way.

喜欢这个流程。Plan Mode 也是我的草图阶段。Code-Reviewer 作为子代理感觉就像多了一双眼睛——这样我的 bug 至少减少 30%。

* * *

**Antithesis** @AntithesisHQ

Our favorite equation is:

Obscure feature+obscure feature+obscure feature = Bug

For your weekend reading, Michael Gibson writes about how we found a bug in the C++ compiler -- without using Antithesis.

Link below, for the algorithm will not be denied.

我们最喜欢的公式是：

难懂的特性+难懂的特性+难懂的特性 = Bug

周末阅读推荐：Michael Gibson 写了关于我们如何在 C++ 编译器中发现一个漏洞——而且没有使用 Antithesis。

下面是链接，因为算法不会被否认。

![Image](https://pbs.twimg.com/media/G1OA_qfWYAElGzO?format=jpg&name=large)