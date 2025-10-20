---
title: "MCP集成Agentic RAG系统演进"
source: "https://x.com/Aurimas_Gr/status/1976633701564809382"
author:
  - "[[@Aurimas_Gr]]"
published: 2025-10-11
created: 2025-10-11
description:
tags:
  - "@Aurimas_Gr #LLM #AI #机器学习 #RAG #MCP #智能体化"
status: "inbox"
importance: 2
effort: 2
review_level: 0
review_next: "2025-10-27"
review_interval: null
review_count: 0
decision: null
topics: []
links_out: []
summary: ""
pov: ""
actions: []
---
**Aurimas Griciūnas** @Aurimas\_Gr [2025-10-10](https://x.com/Aurimas_Gr/status/1976633701564809382)

  
通过𝗠𝗖𝗣集成𝗔𝗴𝗲𝗻𝘁𝗶𝗰 𝗥𝗔𝗚系统 👇 若您正在构建 RAG 系统并为检索打包多个数据源，那么至少在检索阶段的数据源选择环节很可能存在某种代理机制。这正是 MCP 在此类场景下丰富您 Agentic RAG 系统演进的方式（要点 2）：𝟭. 用户查询分析：我们将原始用户查询传递给基于 LLM 的智能体进行分析。此阶段将实现： ➡️ 原始查询可能被重写（有时会多次重写），生成单个或多个查询传递至后续流程。

代理判断是否需要额外数据源来回答查询。𝟮. 若需补充数据，则触发检索步骤。我们可以接入多种数据类型，例如： ➡️ 实时用户数据。

用户可能感兴趣的内部文件。

网络上可获取的数据。

➡️ …这正是 MCP 发挥作用之处： ✅ 每个数据领域都能管理各自的 MCP 服务器，明确数据使用的具体规则。

在 Servel 层面可为每个域名确保安全性与合规性。

新数据域可通过标准化方式轻松加入 MCP 服务器池，无需重写代理程序，从而实现系统在程序性记忆、情景记忆和语义记忆层面的解耦演进。

平台构建者能够以标准化方式向外部用户开放数据，便于在网络上轻松获取信息。

人工智能工程师可继续专注于智能体的拓扑结构优化。3. 检索到的数据会通过比常规嵌入模型更强大的系统进行整合与重排序，数据点将被大幅精简。

4\. 若无需额外数据，我们会尝试直接通过 LLM 生成答案（或多个答案或一系列操作）。

5\. 答案经过分析、总结，并对其正确性和相关性进行评估：如果智能体判定答案足够优质，便会将其返回给用户。

➡️ 若智能体判定答案需要改进，我们将尝试重写用户查询并重新执行生成循环。  
  
您是否在智能体化 RAG 系统中使用 MCP？欢迎在评论区分享您的使用体验 👇 #LLM #AI #机器学习

![Diagram titled Agentic RAG plus MCP shows flowchart with chat interface user query leading to LLM agent analysis deciding on additional data needs then retrieval from MCP servers reranking results and final answer generation includes elements like rewrite query retrieved data reranked results answer analysis and icons for brain and person with LinkedIn and newsletter links at bottom](https://pbs.twimg.com/media/G25p3APXUAALlVQ?format=jpg&name=large)