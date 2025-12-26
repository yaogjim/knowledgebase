---
title: "2025-11-28_yan5xu_这有一块有一个反范式_如果你用户体量足够大的时候_system_Prompt_全局前缀一致_因为缓存"
source: "https://x.com/yan5xu/status/1993893340618883262"
author:
  - "[[@yan5xu]]"
published: 2025-11-28
created: 2025-11-28
description:
tags:
  - "x"
  - "@yan5xu"
  - "https"
  - "2025-11-27"
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

# 这有一块有一个反范式。如果你用户体量足够大的时候。system Prompt 全局前缀一致，因为缓存

**yan5xu** @yan5xu 2025-11-26

这有一块有一个反范式。如果你用户体量足够大的时候。system Prompt 全局前缀一致，因为缓存请求溢出的原因，反而会拉低 hit rate。要在开头加入{{SESSION\_ID}}变为会话内一致反而会提升。或者openai 支持在 header 里面添加 session-id/user-id 也是一样的

> 2025-11-26
> 
> 今天组内小伙伴在内部agent平台的自定义prompt里增加了一个{{CURRENT\_DATE}}的模板变量的功能，被我驳回了，发现其实挺多agent工程师并不知道context caching这个机制，举个例子，如果在一个sytem prompt里加了{{当前时间}}的动态变量，你会发现几次对话的cache hit会变成这样，极大增加成本
> 
> ![Image](https://pbs.twimg.com/media/G6qT_6BbwAMuw8z?format=jpg&name=large)

* * *

**yan5xu** @yan5xu [2025-11-27](https://x.com/yan5xu/status/1993893774221877557)

具体原因可参考 openai/prompt cache/运作原理

当相同前缀与提示缓存键组合的请求频率超过一定阈值（约每分钟15次请求），部分请求可能溢出并被路由至额外机器，从而降低缓存效率。

* * *

**axtrur** @axtrur [2025-11-27](https://x.com/axtrur/status/1993897747599237313)

嗯sessionid 路由到推理示例的问题， 说到这个，我在想一个用户体量大的产品，prompts版本变更的时候有没有办法做一些预热，或者对所有人的第一条消息进行sessionid控制呢？

* * *

**yan5xu** @yan5xu [2025-11-27](https://x.com/yan5xu/status/1993924412882735178)

倒也不用，prompt cache 建立很快的。这个技巧 适合gemini 之前的 cache 机制。

* * *

**axtrur** @axtrur [2025-11-27](https://x.com/axtrur/status/1993925727687971164)

哈哈倒也没有体量大道这种地步

* * *

**Pray祈祷** @prayxsy [2025-11-27](https://x.com/prayxsy/status/1993906077159887197)

哈哈哈 老师我记得你公众号的预告是不是提过一嘴 还没填坑😆

* * *

**yan5xu** @yan5xu [2025-11-27](https://x.com/yan5xu/status/1993913243908358242)

那篇删了😂 我就懒得继续写

* * *

**九原客** @9hills [2025-11-27](https://x.com/9hills/status/1993969030034764081)

claude code prompt 一开始就有session id。确实精妙

* * *

**索螺丝** @fiapp\_pro [2025-11-27](https://x.com/fiapp_pro/status/1993912495795523867)

把 uer profile 赛点进去让 llm 更拟人，误打误撞了

* * *

**ハルキ** @sweetliquidtw [2025-11-27](https://x.com/sweetliquidtw/status/1993923676308410833)

热点 key，但是让调用方负责打散🤣

* * *

**Cunningham Card** @Card198454 [2025-11-27](https://x.com/Card198454/status/1993921824577745046)

关注了，和大佬学知识

* * *

**tsj** @Tsj\_estwld [2025-11-27](https://x.com/Tsj_estwld/status/1993908448707399929)

🤔精彩