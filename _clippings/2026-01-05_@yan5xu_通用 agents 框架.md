---
title: "通用 agents 框架"
source: "https://x.com/yan5xu/status/2007966550737957231"
author:
  - "[[@yan5xu]]"
date: "2026-01-05T16:12:39+08:00"
created: 2026-01-05
description:
tags:
  - "@yan5xu # agents 框架"
  - "# LLM"
  - "# tools"
  - "# shell 命令"
---
**yan5xu** @yan5xu [2026-01-05](https://x.com/yan5xu/status/2007966550737957231)

突然想到一个通用的 agents 框架。只要一个沙盒+llm，tools 就两类，文件操作和 shell 命令，所有工具都是通过程序的方式提供。工具提供 -h 简单描述 和 --help 详细描述。每个目录都有一个自描述文件，说明当前目录做什么的，关联了哪些工具（包括简单描述），哪些方法论。所有通过自描述完成。

那么 agents开发，就可以简化成为，目录设计，工具开发，方法论设计！!!

---

**yan5xu** @yan5xu [2026-01-05](https://x.com/yan5xu/status/2007967254257017029)

工具还可以通过管道符，串联使用

---

**IndenScale** @david0520782123 [2026-01-05](https://x.com/david0520782123/status/2007976976326558140)

没那么简单。

1，你需要设计 工作区和账本区。账本区应该只增不改，使用指针维护提供可追溯性。因为两者都曾经是事实。

2，你需要设计 本体论区 和 逻辑约束区 ，描述在这个有序系统中，要怎样才不会破坏逻辑自洽性。

3，你需要提供自动执行 schema 校验 和 业务逻辑校验的测试脚本。

---

**yan5xu** @yan5xu [2026-01-05](https://x.com/yan5xu/status/2007978054556287001)

棒，但这些我觉得是 llm 那一层配套的工程去做的

---

**IndenScale** @david0520782123 [2026-01-05](https://x.com/david0520782123/status/2007981463384502591)

怎么处理事实和记忆我认为属于应用层。

记住什么，遗忘什么，在系统提示词中指引Agent发现什么，这些我觉得模型厂商缺乏特定场景最佳实践的先验知识。

---

**yan5xu** @yan5xu [2026-01-05](https://x.com/yan5xu/status/2007982519757811741)

我表达不清晰哈，就是 LLM 调用完，就需要程序化的工程去做的，不是 agent 自己主动控制

---

**IndenScale** @david0520782123 [2026-01-05](https://x.com/david0520782123/status/2008003289141702911)

claude code hooks ？

---

**PetLab Co** @petlabco

If you’ve spotted any of these 3 signs in your dog… it could be due to yeast! Discover how thousands of owners are supporting their pups with the help of 1 effective chew!

---

**耳朵** @RookieRicardoR [2026-01-05](https://x.com/RookieRicardoR/status/2008031653080473734)

你说的这个东西好像叫 Claude Code + Skill🤔

---

**axtrur** @axtrur [2026-01-05](https://x.com/axtrur/status/2007979764867567833)

听着像是skill + skill scope mcp.json，不过我最近觉得这种方式要达到很好的效果挺不容易，很多上下文的工作

---

**LotusDecoder** @LotusDecoder [2026-01-05](https://x.com/LotusDecoder/status/2007977544642081165)

👍是的， mcp 太占上下文了。

---

**Vaayne** @LiuVaayne [2026-01-05](https://x.com/LiuVaayne/status/2008002829127172490)

Agent 的本质就是 loop + tools，skills 其实就是你说的工具自描述外加渐进式披露。

我现在最喜欢的是 pi agent，正在基于它构建自己的 workflow。

https://github.com/badlogic/pi-mono…

https://github.com/badlogic/pi-skills…

---

**yan5xu** @yan5xu [2026-01-05](https://x.com/yan5xu/status/2008009593818079403)

我觉得渐进式不足够，渐进+自描述

---

**Vaayne** @LiuVaayne [2026-01-05](https://x.com/LiuVaayne/status/2008009768661876765)

https://github.com/badlogic/pi-skills… 看看这个

---

**DinoDeer** @xDinoDeer [2026-01-05](https://x.com/xDinoDeer/status/2007977307223228896)

不考虑 token 成本是可以这样做的。我看到 Manus 绝大部分工作都是通过这种方式处理了。

---

**yan5xu** @yan5xu [2026-01-05](https://x.com/yan5xu/status/2007982011433296005)

我想到一个很棒的低成本压缩方式，agentic loop 里面每个 fc 有结果之后，拿到小模型总结这次调用做了什么，形成一个 log，因为缓存命中了，所以成本不会太高；到达上下文阈值之后，就可以通过 log+summary，开新 session；上下文最大限度保留

---

**yan5xu** @yan5xu [2026-01-05](https://x.com/yan5xu/status/2007987120791793951)

甚至都不用小模型，用原来模型，因为前缀是一致的，成本只会多出来 log 部分的 output token

---

**薛定AI** @lusya68911418 [2026-01-05](https://x.com/lusya68911418/status/2007983440613007834)

请教一下，这样的话搜索算shell命令吗

---

**yan5xu** @yan5xu [2026-01-05](https://x.com/yan5xu/status/2007983714605961584)

grep 一直都是呀

---

**薛定AI** @lusya68911418 [2026-01-05](https://x.com/lusya68911418/status/2007984171940192733)

刚没说完整lol，网页搜索部分看作是命令行执行无头浏览器指令吗

---

**yan5xu** @yan5xu [2026-01-05](https://x.com/yan5xu/status/2007984987983999232)

😏你完全可以把网页搜索封装成一个工具，里面到底是 API/还是 playwright 就不用暴露出来了，因为常用网站完全可以 RPA 话。

当然留一个playwright 作为 fallback 是没问题的。

---

**albert** @albertmokt [2026-01-05](https://x.com/albertmokt/status/2008004063615672600)

最终还是回到了工具设计这一块

---

**yan5xu** @yan5xu [2026-01-05](https://x.com/yan5xu/status/2008009499769278680)

目录结构设计， 和方法论也很重要呀

---

**Zkers** @Tangpin78255362 [2026-01-05](https://x.com/Tangpin78255362/status/2007969741886165329)

文件操作也是shell的一部分吗？

---

**yan5xu** @yan5xu [2026-01-05](https://x.com/yan5xu/status/2007984012766417277)

文件操作，emmm 虽然可以，但我觉得还是封装一次更好，可以看看这个讨论

> 2026-01-03
> 
> 关于 context engineering。有两个问题，我觉得特别能看出人的水平，问他在 XX 业务场景下面，read\_file, write\_file 如何设计。如果真的只有读，写具体文件，就可以到此结束。

---

**Sam Song** @SamSongAI [2026-01-05](https://x.com/SamSongAI/status/2007978806632755606)

show

---

**yan5xu** @yan5xu [2026-01-05](https://x.com/yan5xu/status/2007982583574089910)

在搞了在搞了

---

**fangjun** @fjun99 [2026-01-05](https://x.com/fjun99/status/2008014285193236926)

这个思路很赞

---

**Jay** @jma7889 [2026-01-05](https://x.com/jma7889/status/2008020697520705884)

这是一个不支持agent调用的agent框架吗？ agent调用被转化成了tool调用

---

**Bypass** @bypass47078 [2026-01-05](https://x.com/bypass47078/status/2008004816740696261)

有个同事做过类似的，区别是他用的不是 Shell，而是自己设计的一套 Python DSL。