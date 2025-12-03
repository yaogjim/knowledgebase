---
title: "2025-11-28_yan5xu_anthropic_真的是一环扣一环_有理论有实践_在发_skills_的时候_针对工具膨胀浪费_t"
source: "https://x.com/yan5xu/status/1993511875989098512"
author:
  - "[[@yan5xu]]"
published: 2025-11-28
created: 2025-11-28
description:
tags:
  - "x"
  - "@yan5xu"
  - "2025-11-26"
  - "https"
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

# anthropic 真的是一环扣一环 有理论有实践 在发 skills 的时候，针对工具膨胀浪费 t

**yan5xu** @yan5xu [2025-11-26](https://x.com/yan5xu/status/1993511875989098512)

anthropic 真的是一环扣一环 有理论有实践

在发 skills 的时候，针对工具膨胀浪费 token 提出了， Prompt 分层加载/复用，用代码执行&串联api/mcp（manus 把这个叫做上下文卸载）两个方法

前天发 opus 的同时，把这两个方法固定到了推理 API 层面，Tool Search Tool，解决工具的发现&懒加载，Programmatic Tool Calling 实现代码执行工具。 感觉以后anthropic api协议😂大有替代 openai 的可能

* * *

**yan5xu** @yan5xu [2025-11-26](https://x.com/yan5xu/status/1993511894225912019)

* * *

**yetone** @yetone [2025-11-26](https://x.com/yetone/status/1993545212476768704)

哈哈，不需要这么神话 Anthropic，其实 Anthropic 只是把大家这些年来的免费分享的最佳实践重新总结了一下用自己的话说出来，比如 search\_tools 和 Programmatic Tools Calling 很久之前就有了：

* * *

**yan5xu** @yan5xu [2025-11-26](https://x.com/yan5xu/status/1993551008484708758)

确实是，不过也变相把社区的最佳实践推广出去，毕竟他们足够 voice louder

* * *

**xincmm** @xincmm [2025-11-26](https://x.com/xincmm/status/1993526562134884712)

隐约觉得，目前似乎只有 Opus 4.5 有能力驱动这个架构。目前只有它足够的元认知能力，知道自己不知道什么，知道什么时候该搜索，知道如何把任务分解成可编程的步骤，这种能力是其他模型现阶段不具备的。

* * *

**Leo Xiang** @leeoxiang [2025-11-26](https://x.com/leeoxiang/status/1993642866212774339)

兼容多家大模型的成本越来越高了

* * *

**kangkang** @pengwk2 [2025-11-26](https://x.com/pengwk2/status/1993516313839648844)

昨天看到这个 Programmatic Tool Calling 惊呆了，一开始以为是在模型侧的容器里运行自己的工具代码，结果是在模型侧做编排工具，厉害了

* * *

**SWH | (168, 168)** @swh16888 [2025-11-26](https://x.com/swh16888/status/1993665810448159074)

請教一下 我看到有人說現在搞agent, 用Claude code SDK 開始省事很多。JS版本跟Python 版本有差別嗎？

* * *

**Gu3ss.eth** @StaccNotGuilty [2025-11-26](https://x.com/StaccNotGuilty/status/1993593989937996207)

从来没有觉得openai能和claude竞争.