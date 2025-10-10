---
title: "九原客关于LangChain及LangGraph的讨论"
source: "https://x.com/9hills/status/1976294376415559887"
author:
  - "[[@9hills]]"
published: 2025-10-10
created: 2025-10-10
description:
tags:
  - "@9hills #LangChain #LangGraph #工作流 #智能助手 #AI开发 #机器学习 #深度学习"
---
**九原客** @9hills 2025-10-09

langchain团队挺有意思的。

最早他们喜欢workflow，设计了Chain这个概念。

后来Agent火，于是支持了 ReActAgent

但是Chain表达能力有限，Agent当时难堪大用，于是开发了 langgraph，把workflow 推上顶峰，我认为是表现力最强的workflow实现，open dr 大部分都是workflow。

但是现在全自主Agent 又随着模型能力发展能行了，又把langchain的agents给翻出来，做自主agent，这个deepagents就是自主agent.

逻辑主要靠给agent加middleware来实现。

> 2025-10-09
> 
> 库地址：https://github.com/langchain-ai/deepagents…
> 
> research实现：https://github.com/langchain-ai/deepagents/blob/master/examples/research/research\_agent.py…
> 
> UI: https://github.com/langchain-ai/deep-agents-ui…
> 
> 兄弟，够不够，还有配套Youtube视频，我就不发了。

---

**九原客** @9hills [2025-10-09](https://x.com/9hills/status/1976294638333067522)

新的agents实现依赖langchain的v1版本代码： https://github.com/langchain-ai/langchain/tree/master/libs/langchain\_v1/langchain/agents/middleware…

---

**100gle** @1oogle [2025-10-09](https://x.com/1oogle/status/1976298685924622476)

LangChain毫不夸张地说设计得就是一坨💩，吸取了批评和经验之后设计的LangGraph才看起来像是个完成品，已在生产上稳定运行超几个月了。

---

**九原客** @9hills [2025-10-09](https://x.com/9hills/status/1976301883208892582)

workflow 才是目前生产环境里的王道

---

**siyuan cao** @sonaldc [2025-10-09](https://x.com/sonaldc/status/1976308844029755408)

之前用 langchain 做 rag 的时候，为了支持端到端的流式输出，不知道改了多少地方代码，回调设计的一塌糊涂，各种后端实现不一致，从此以后再也不用他家任何代码

---

**仓里 · 忙割** @kylesean6 [2025-10-09](https://x.com/kylesean6/status/1976297462290579507)

确实。LangGraph是他们主推方向，现在LangChain的定位更多是围绕LLM的组件集成库，根据官方文档可以完全不依赖LangChain而只用LangGraph构建Agent，当然配合使用更自然。这个月应该会发布1.0正式版了。