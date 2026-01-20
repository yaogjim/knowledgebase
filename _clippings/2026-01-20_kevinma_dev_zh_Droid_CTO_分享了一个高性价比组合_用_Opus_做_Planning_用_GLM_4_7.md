---
title: "2026-01-20_kevinma_dev_zh_Droid_CTO_分享了一个高性价比组合_用_Opus_做_Planning_用_GLM_4_7"
source: "https://x.com/kevinma_dev_zh/status/2013201702799753725"
author:
  - "[[@kevinma_dev_zh]]"
published: 2026-01-20
created: 2026-01-20
description:
tags:
  - "x"
  - "@kevinma_dev_zh"
  - "2026-01-19"
  - "https"
---

# Droid CTO 分享了一个高性价比组合：用 Opus 做 Planning，用 GLM 4.7

**Kevin Ma** @kevinma\_dev\_zh 2026-01-19

Droid CTO 分享了一个高性价比组合：用 Opus 做 Planning，用 GLM 4.7 或 GPT-5.2-Codex 做执行。

Opus 聪明但贵，用它来编码性价比不高，但很适合做 Planning。

Codex 模型强，写的代码可靠性好，任务执行也稳。

Thinking 可以默认选择 High。

这样成本砍掉一大截，效果还很好。

> 2026-01-19
> 
> 目前最具成本效益的组合是设置 Opus 作为你的规划模型，以及 GLM 4.7 或 GPT-5.2-Codex 作为你的执行模型。这能给你带来与 Opus 基本相同的性能，却只需消耗少量的 token。

* * *

**吕立青\_JimmyLv 2𐃏26** @Jimmy\_JingLv [2026-01-19](https://x.com/Jimmy_JingLv/status/2013259845781110872)

哈哈哈，我给GLM写的文章就是这个组合 https://zhuanlan.zhihu.com/p/1974833071040796223…

* * *

**danielw** @dddanielwang [2026-01-19](https://x.com/dddanielwang/status/2013212111292322123)

我也转了这个贴，决定入手copilot试试水

* * *

**Kevin Ma** @kevinma\_dev\_zh [2026-01-19](https://x.com/kevinma_dev_zh/status/2013217300607029551)

嗯，推荐试试 droid ，好用的

* * *

**Vincent** @win1688888888 [2026-01-19](https://x.com/win1688888888/status/2013233953046438159)

当执行遇到 Block 时，流程是回滚给 Opus 重新 Planning，还是允许 Codex 局部 Patch？ 如果没有在这个节点做 Loop Control，你可能会发现便宜的 Codex 跑了一堆无用的 Token，最后还得请回 Opus 擦屁股。

* * *

**Kevin Ma** @kevinma\_dev\_zh [2026-01-19](https://x.com/kevinma_dev_zh/status/2013237027303793038)

不会, codex 模型写的代码比 opus 好，我过去一般都是 opus 写代码, codex 做 review 和修 bug，现在主力使用 codex 写代码了，效果很好。

* * *

**Crazyox** @crazyox [2026-01-19](https://x.com/crazyox/status/2013238679985078385)

这个组合确实省钱又好用

* * *

**Himanshu Kumar** @codewithimanshu [2026-01-19](https://x.com/codewithimanshu/status/2013327706193305883)

@kevinma\_dev\_zh, 使用 Opus 进行规划并使用 Codex 执行是针对复杂任务的明智且经济高效的方法。

* * *

**周尔复** @cholf5 [2026-01-19](https://x.com/cholf5/status/2013283747215323268)

其实全程都用 Codex 就好了，没觉得 Plan Mode 有什么特别的。我都是跟 Codex 说：「先聊方案，不写代码」，这不就是 Plan Mode 吗？也可以挖得很深。Anthropic 搞出来多少概念了？ Plan Mode、MCP、Skills、Cowork，都可以报菜名了，一会一个新概念，累不累？如果不是一天写300万行代码，大可不必。

* * *

**程序员鱼皮** @yupi996 [2026-01-19](https://x.com/yupi996/status/2013257685806846263)

我是用 Gemini（DeepSearch）做初始调研（全面深入） + Claude Opus 做方案设计（聪明可靠） + Sonnet 生成代码（上下文长）

* * *

**shafa ba** @shafajia [2026-01-19](https://x.com/shafajia/status/2013291174799225208)

既然都用codex写代码的话还要什么opus做规划，它自己规划自己写就行了，gpt 5.x将思考强度开到高以上速度很慢有点忍不了才会用claude或其它的..但是确实感觉它的静态代码分析能力确实是独一档，思考半小时改了3行代码然后看了下还真能解决疑难bug..

* * *

**Jerell** @cwfox67 [2026-01-19](https://x.com/cwfox67/status/2013223950893846989)

我是使用 opus 4.5 做 planning, 用 grok-code-fast-1 做執行, 還不錯 速度挺快.

* * *

**赖叔 | LaiShu.ai** @hiheimu [2026-01-19](https://x.com/hiheimu/status/2013255445796765867)

用啥工具同时支持这几个

好像反重力不支持codex5.2

* * *

**Charlie** @Lei1247559 [2026-01-19](https://x.com/Lei1247559/status/2013237405201858683)

不错，这个路径值得收藏

* * *

**Echo** @SuperGGBo [2026-01-19](https://x.com/SuperGGBo/status/2013270970660761909)

我的习惯刚好是反的，gpt 做拆解 claude 干活

* * *

**tony** @Tony\_luyajun [2026-01-19](https://x.com/Tony_luyajun/status/2013226341160935657)

@threadreaderapp 展开

* * *

**ZPASSER** @Justinhk1208 [2026-01-19](https://x.com/Justinhk1208/status/2013244150456766890)

反代出谷歌反重力的多个模型为API使用，直接使用免费的pro的额度，相当于不要钱使用多个模型

> 2026-01-19
> 
> ![Article cover image](https://pbs.twimg.com/media/G_B5nrDXwAAWDst?format=jpg&name=large)