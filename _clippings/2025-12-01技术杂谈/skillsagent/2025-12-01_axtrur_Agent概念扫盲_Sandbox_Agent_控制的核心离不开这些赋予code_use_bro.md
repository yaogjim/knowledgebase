---
title: "2025-12-01_axtrur_Agent概念扫盲_Sandbox_Agent_控制的核心离不开这些赋予code_use_bro"
source: "https://x.com/axtrur/status/1995109870861754543"
author:
  - "[[@axtrur]]"
published: 2025-12-01
created: 2025-12-01
description:
tags:
  - "x"
  - "@axtrur"
  - "https"
  - "axtrur"
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

# Agent概念扫盲【Sandbox】 Agent 控制的核心离不开这些赋予code-use, bro

**axtrur** @axtrur 2025-11-29

Agent概念扫盲【Sandbox】

Agent 控制的核心离不开这些赋予code-use, browser-use的行动空间的沙箱环境，比如 Skill，Programmatic Tool Calling, Search Tool 这些控制机制，背后都需要一个执行环境承载

> 2025-11-29
> 
> Agent概念扫盲【SKILL】
> 
> Skill不是一个“协议”，而是一个“思维方式”，是在一个环境（Sandbox）中对“Experience”编排的一种很好的表达方式
> 
> ![Image](https://pbs.twimg.com/media/G7AN1o0bQAAFVAq?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G66mmDQawAAZt_Q?format=jpg&name=large)

* * *

**axtrur** @axtrur [2025-11-30](https://x.com/axtrur/status/1995133559565332712)

年初也实现了轻量版code use，如果内部使用且不需要考虑隔离性的也可以通过这种方式实现

> 2025-07-06
> 
> 年初因为ServerLess太重，所以自己实现了一整套轻量级的Nodejs（V8沙箱），python（原生服务环境），Golang（yaegi解析器），目的是动态执行一些人为生成或者AI生成的代码，但是这种方案需要内置一些常用的第三方库，甚至Yaegi还得实现一个内存文件系统做目录依赖管理。今天看了下microsandbox的实现， x.com/ProgramerJohan…

* * *

**Frank** @Spades317 [2025-12-01](https://x.com/Spades317/status/1995310453552185702)

AI 小册了属于是

* * *

**axtrur** @axtrur [2025-12-01](https://x.com/axtrur/status/1995311194073370719)

哈哈感觉需要有人写这个，市面上少了这样的面向agent builder的小册