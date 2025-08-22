---
title: "单线程 RAG 代替多智能体？"
source: "https://x.com/xicilion/status/1958589312527999440"
author:
  - "[[@xicilion]]"
published: 2025-08-22
created: 2025-08-22
description:
tags:
  - "@xicilion #AI智能体 #RAG #阅读理解"
---
**响马** @xicilion 2025-08-20

单一 rag 是初代增强的产物。我现在的做法是将 rag 实现为 mcp，提供 ask 和 fetch 两个 api，检索依然使用传统 rag 机制，延展阅读让 ai 调用 fetch 读取前后上下文。机制上和 cline grep 再读取文件是相似的。

> 2025-08-20
> 
> 深以为然：1. 多智能体并行协作不如单线程稳定； 2. RAG 不靠谱还不如传统检索；3. 提示词里面的指令越多模型越不知道该怎么选。
> 
> ——原推翻译如下——
> 
> 在构建 AI 智能体（AI Agent）的道路上，我们团队 @Cline x.com/arafatkatze/st…