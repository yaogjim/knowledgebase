---
title: "上下文工程实践：Claude Code 的之道"
source: "https://x.com/dotey/status/1950617831369740782"
author:
  - "[[@dotey]]"
created: 2025-07-31
description:
tags:
  - "@dotey #上下文工程 #AI #LLM # ClaudeCode"
---
**宝玉** @dotey 2025-07-30

论上下文工程的实践，Claude Code 的做法我觉得是大道至简：

1\. 当前会话所有历史记录保留（90%上下文之前不会主动压缩），不变换工具列表

这样可以保证上下文不因为压缩损耗，不修改历史会话记录也可以确保命中 Prompt Caching 节约成本

2\. 通过子 Agent （Task 工具），既可以让子 Agent 的上下文独立完整，又可以让主 Agent 的上下文清晰简洁。

就像一个专业的管理者，规划好后让下属去完成各种子任务，自己聚焦于主任务

3\. 用 TODO 工具，做计划，实时更新进度，让执行路径清晰，并可以让 AI 不迷失在上下文中，聚焦于要执行的 TODO List Item

> 2025-07-30
> 
> 《How to Fix Your Context》这篇上下文工程指南，建议跟 Manus 六大上下文工程法则一起看，它们分别来自两个方向：一个是跑在工程一线踩过坑的 Agent 系统实践者，一个是站在系统架构角度思考 LLM 工作方式的认知构建者。
> 
> 我把这两篇文章有一起读了一篇，有种“内功交叉灌顶”的感觉。 x.com/frxiaobei/stat…

---

**Booker** @being99 [2025-07-31](https://x.com/being99/status/1950721308263698550)

这个和 Manus 分享的上下文工程的实践完全一致