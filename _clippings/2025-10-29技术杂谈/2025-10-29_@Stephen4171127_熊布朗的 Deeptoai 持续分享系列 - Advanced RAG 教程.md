---
title: 熊布朗的 Deeptoai 持续分享系列 - Advanced RAG 教程
source: https://x.com/Stephen4171127/status/1983281697022972150
author:
  - "[[@Stephen4171127]]"
published: 2025-10-29
created: 2025-10-29
description: 
tags:
  - RAG
  - "#"
  - AI
  - 从业者
  - "#"
  - 企业级
  - "#"
  - DeepResearch
  - "#"
  - Agent
  - "#"
  - 多模态
  - "#"
  - 创作平台
  - "#"
  - 知识库
  - "#"
  - 文档问答
  - "#"
  - AI
  - 能力
  - "#"
  - 技术选型
  - "#"
  - 架构设计
  - "#"
  - 落地实施
  - "#"
  - 服务企业
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
**熊布朗** @Stephen4171127 [2025-10-28](https://x.com/Stephen4171127/status/1983281697022972150)

熊布朗的 Deeptoai持续分享系列 - Advanced RAG 教程

——

我做了一个 Advanced RAG 系列的学习文档，今天正式发布

包含理论、实践和 9 个 RAG 开源项目的深度剖析拆解

完全开放，完全免费

教程地址：https://rag.deeptoai.com

\----

这个教程是标准得面向AI从业者，目标是能服务得了企业级的 RAG 研发，当然产品经理也可以看，可以学。

设计了几个等级

📚 Level 0：新手入门 手把手教你搭建第一个 RAG 系统 从环境配置到完整实现。

📖 Level 1：理论建立 RAG 核心概念、发展历程、技术综述 建立完整的知识框架。

🔬 Level 2：深入原理 核心技术的算法实现和性能调优 向量搜索、Chunking、混合检索、Rerank、查询转换等。

💻 Level 3：动手实践 真实案例、代码实现、工程最佳实践 Milvus 混合检索、多模态 RAG、GraphRAG、Agent RAG 等。

🏗️ Level 4：项目落地 9 个生产级开源项目的深度剖析。

——

这一层是给需要做技术选型和架构设计的人准备的，我也是这么学过来的，到目前能面向企业交付私有知识库和 AI Agent，基本上面向企业用户，RAG 是必需的。

各位朋友看看，如果有帮助

还请 📢 转发给需要的人 💬 提建议和反馈（私信我）

![Screenshot of a web page titled Advanced RAG Tutorial displaying a structured learning path with sections for Level 0 beginner setup Level 1 theory Level 2 principles including vector search chunking hybrid retrieval rerank query transformation Level 3 practice with Milvus hybrid retrieval multimodal RAG GraphRAG Agent RAG and Level 4 project analysis of 9 production-grade open-source projects shown in colorful flowchart diagrams and sidebar navigation.](https://pbs.twimg.com/media/G4XCv2pWkAACLb2?format=jpg&name=large)

---

**熊布朗** @Stephen4171127 [2025-10-28](https://x.com/Stephen4171127/status/1983281700567138395)

为什么我要做这个教程项目？

说说我的观察和思考 👇

——

先说说我的背景，我不是程序员，虽然看着我天天 Vibe Coding、Vibe Project，那不是我的工作职责，多是兴趣研究+工作辅助。准确说，应该是 AI 产品负责人，to B/to C 都有在做。  
  
工作和个人热爱的原因，过去两年，我应该平均每天有花 6+ 小时学习和实践 AI 的各种乱七八糟的能力，主要的信息来源就是X （这里有各路大神，尤其是宝玉老师）

我入门是从 Character AI 开始的，Character AI 讲求的是提示词工程和 Memory，后面我也会把这部分独立成教程。

后来基本上就开始做大型企业AI 项目的落地了，从 RAG 到 DeepResearch Agent 到类 Manus 的 MultiAgent，还有类似可灵这样的多模态创作平台的设计交付。

——

再说说，为啥整理和写这个教程：  
  
原因一：做企业 AI 的必修课

虽然 RAG 目前在 X 上出现的越来越少，但是实际在服务企业的过程中，RAG 几乎是绕不开的，私有化文档、企业内部的各类数据来源，都要接入了，才能让AI 充分发挥价值。RAG 并不是向量数据库或者某些技术组合，核心要点还是如何结合自己的数据特点和业务场景，来给到 LLM 合适的上下文，重点在“合适的上下文”，所有的工程都是服务这一目的。  
  
所以就不会有某个企业级 RAG 产品能像 ChatGPT 那样可以轻松安装部署，所见即所得。大概率要用工程手段来服务业务场景，所以 RAG 还是得学，而且还得学以致用。  
  
原因二：网上的 RAG 教程要么太理论，要么太碎片  
  
理论派：只讲原理，不讲怎么做 实践派：只有代码片段，看不到完整架构 缺一个能把"原理 + 开源项目架构 + 企业落地实践"串起来的东西。  
  
———

所以我决定把这些经验系统地整理出来 不只是技术文档 而是一个从理论到实践、从学习到落地的完整路径，看到新的、有价值的东西，我还会持续更新。

———

RAG 还只是第一个教程（教程地址：https://rag.deeptoai.com），下一个是 AI Agent 系列（DeepResearch、Multi-Agent 和 Code Agent） ，后续再补上一个 Character AI（Prompt 、Memory和多模态），希望 2025 年内都搞定。

---

**熊布朗** @Stephen4171127 [2025-10-28](https://x.com/Stephen4171127/status/1983281702802751565)

关于开放和商业

有人可能会问：你做免费教程以及开源项目，企业还会找你做实施吗？

我的想法很简单： 能从教程里学会并自己实施的人，本来就不是我的目标客户

绝大部分企业不懂技术，懂技术的企业也不见得有能做企业级 AI Agent 落地的人。需要专业协助的企业（你)，看到详实的教程反而会更信任我。

如果你的企业正在考虑引入 AI 能力

我可以帮你做这些 👇

\--- 前期咨询（免费）：

\- 聊聊业务场景，看 AI 能在哪里产生价值

\- 梳理数据情况，评估技术可行性

\- 估算投入和收益，判断值不值得做

\--- 方案设计 + 落地实施：

\- 设计适合你们的系统架构（RAG/Agent/AIGC）

\- 规划技术实现路径和选型

\- 和团队一起完整落地

\- 性能调优、部署、监控

\--- 我做过的项目类型：

\- RAG 系统（知识库、文档问答）

\- DeepResearch（深度研究分析）

\- Character AI（对话式 AI 角色）

\- AIGC 平台（文生图、文生视频）

\- AI Agent（自动化工作流）

——

联系方式：

X 直接 DM 我

💬 微信：Browncony999（备注"AI咨询"）

我们可以先聊聊 看看你的情况适不适合做、怎么做比较靠谱