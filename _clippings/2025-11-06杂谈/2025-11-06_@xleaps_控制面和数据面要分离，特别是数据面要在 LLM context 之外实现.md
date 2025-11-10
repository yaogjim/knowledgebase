---
title: "控制面和数据面要分离，特别是数据面要在 LLM context 之外实现"
source: "https://x.com/xleaps/status/1986369014558237024"
author:
  - "[[@xleaps]]"
published: 2025-11-06
created: 2025-11-06
description:
tags:
  - "@xleaps # LLM # Token # AI # 智能体 # 代理 AI # 构建效率 AI"
status: "inbox"
importance: 2
effort: 2
review_level: 0
review_next: "2025-11-13"
review_interval: null
review_count: 0
decision: null
topics: []
links_out: []
summary: ""
pov: ""
actions: []
---
**Eric Xu (e/Mettā)** @xleaps 2025-11-05

Anthropic 是在将 agent 从Claude Code 推广到 business 应用时发现这个问题的

实际上对于我们一直深耕商业场景（营销，销售、客服）的厂商来说，这几乎是第一个发现：控制面和数据面要分离 ，特别是数据面要在 LLM context 之外实现

实践中有许多做法，写一个决定性的逻辑意味着控制面里只有工具参数是模型要做的决策，数据面完全可以大规模简化。 用写代码完成任务等于用图灵机的纸带完成数据面，控制面只要写出图灵机的操作程序。

目前我们探索的一些折衷方案是给一些数据面的 schema, 外加 markdown. 其实走来走去 可能又回到了一些都是 CRM 物件这种领域特定的抽象。

> 2025-11-05
> 
> 这篇总结也很好：
> 
> https://x.com/omarsar0/status/1986099467914023194…
> 
> Anthropic 又发布了一篇神级指南。
> 
> 这次的主题是：如何构建更高效的 AI 智能体 (AI Agent)，让它们能更聪明地使用工具，并且极大地节省 Token 。
> 
> 如果你是 AI 开发者，这篇文章绝对不容错过！
> 
> 它主要解决了 AI 智能体在调用工具时遇到的三大难题：Token