---
title: "openkl: 基于文件分层结构的文档理解和知识接入系统"
source: "https://x.com/wey_gu/status/1975352713497223653"
author:
  - "[[@wey_gu]]"
published: 2025-10-07
created: 2025-10-07
description:
tags:
  - "@wey_gu #文档理解 #知识接入 #AGENT #企业级 #RAG #分层结构 #数据结构"
---
**Wey Gu 古思为** @wey\_gu 2025-10-03

我和宝玉老师有一样的观察和看法，并且在 pycon 上的主题中也给出了分享/做了一些探索。  
  
用 swe agent（claude code/ claude agent sdk）作为 agent execution runtime 可能是目前非常经济、有效的应用构建范式。  
  
同时，我们在这两年的企业级 rag 探索中看到，满足真实世界的复杂文档理解的任务需要推荐多文档分层结构理解的索引和对应的召回，并 agentic 地按需利用这些结构去组合、探索召回（我的 blog 里分享了这个方法 fusion graphRAG、看到业界也出了类似的方法和论文）  
  
两者结合，在应用中涉及成百上千个文档理解/知识接入时候，目前最适合的范式是：  
  
\- cli utils/pipeline 友好的文件结构和格式 > 精心封装的复杂索引召回系统与工具抽象

\- 以分层文件系统为核心的索引结构  
  
为此，我们发起了一个项目 openkl  
  
\- 融合了 rag/memory/rag-memory 增强的系统，以文件分层结构存储：统一长期记忆和复杂文档理解抽象  
  
\- 分层结构可以同时被 shell utils 访问或者 cli cypher query：如果需要，可以写出复杂的图模式查询，在 cli 上！  
  
\- 成为可以被 claude code/agent sdk 最佳插拔的 cli文档接入工具（有 agents. md 引入 sys promot 例子）  
  
这个项目还在探索状态，已经开源  
  
https://github.com/nowledge-co/OpenKL…

> 2025-10-03
> 
> 如果你想开发一个 Agent，无论你是打算做 CLI 还是做 Web 还是 Windows，都可以考虑使用 Claude Agent SDK，和 Claude Code 共享的底层代码，Claude Code 就是基于它之上加了个 CLI 的 UI，也就是说你完全可以基于它写一个 Claude Code 出来。
> 
> 我昨天帮朋友花了几个小时就实现了个简单的 x.com/claudeai/statu…

---

**Hao Zhang** @zhanghaoxxxx [2025-10-07](https://x.com/zhanghaoxxxx/status/1975435480071348356)

太好了，我正在思索把知识markdown化，然后存入wiki.js->graphrag->agent这样的流程，star学习一下，看起来大佬这个框架更完备。
