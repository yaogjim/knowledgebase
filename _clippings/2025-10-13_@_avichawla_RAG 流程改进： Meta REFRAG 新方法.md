---
title: "RAG 流程改进： Meta REFRAG 新方法"
source: "https://x.com/_avichawla/status/1977260787027919209"
author:
  - "[[@_avichawla]]"
published: 2025-10-13
created: 2025-10-13
description:
tags:
  - "@_avichawla #机器学习 #NLP #人工智能 #RAG #REFRAG #Meta #Llama"
---
**Avi Chawla** @\_avichawla [2025-10-12](https://x.com/_avichawla/status/1977260787027919209)

  
Meta 的研究人员开发了一种新的 RAG 方法，在 16 个 RAG 基准测试中表现优于 LLaMA。

\- 首令牌生成时间缩短了30.85倍。

处理16倍更大的上下文窗口。

\- 并且它使用的 token 数量减少了 2-4 倍。以下是 Meta 解决的典型 RAG 设置中的核心问题：我们在 RAG 设置中检索到的大部分内容实际上从未帮助过 LLM。在经典 RAG 中，当查询到达时：- 你将其编码成一个向量。

从向量数据库中获取相似的数据块。

\- 将检索到的上下文直接输入 LLM。这种方法通常有效，但代价巨大：大多数文本块包含无关内容。

\- LLM 需要处理更多的令牌。

\- 你为计算能力、延迟和上下文付费。这正是 Meta AI 新方法 REFRAG 所解决的问题。它从根本上重新思考了检索机制，下图展示了其工作原理。本质上，REFRAG 并非将每个文本块和每个词元都喂给 LLM，而是在向量层级对上下文进行压缩和过滤：块压缩技术将每个文本块编码为单个压缩嵌入向量，而非数百个词元嵌入向量。

相关性策略：一种轻量级强化学习训练策略，用于评估压缩嵌入向量，仅保留最相关的文本块。

\- 选择性扩展：只有通过强化学习策略选中的文本块才会被扩展回完整的嵌入表示，并传递给 LLM。这样一来，模型仅处理关键内容而忽略其余部分。以下是分步详解：

\- 步骤 1-2）对文档进行编码并存储到向量数据库中。

\- 步骤3-5）对完整用户查询进行编码并查找相关文本块。同时，为查询（步骤7）和匹配文本块计算词元级别的嵌入向量。

\- 第六步）运用相关性策略（通过强化学习训练）筛选需保留的文本块。

\- 步骤8）将输入查询的令牌级表示与所选文本块的令牌级嵌入以及被拒绝文本块的压缩单向量表示进行拼接。

\- 步骤 9-10）将所有内容发送给 LLM。强化学习步骤使 REFRAG 成为一个更具相关性感知能力的 RAG 流程。根据研究论文，该方法具有以下特点：首次令牌生成速度快 30.85 倍（比之前的 SOTA 技术提升 3.75 倍）

提供16倍更大的上下文窗口

在 16 个 RAG 基准测试中表现优于 LLaMA，同时使用的解码器标记数量减少了 2 至 4 倍。

在 RAG、摘要和多轮对话任务中均未导致准确性损失。这意味着您能以 30 倍的速度处理 16 倍大的上下文，同时保持相同的准确性。该代码尚未由 Meta 发布，但他们计划很快公开。

![Flowchart diagram divided into two main sections side by side labeled RAG on the left and REFRAG on the right both showing processes for document encoding embedding indexing vector database similarity search chunk retrieval and LLM query processing to generate final response. RAG section includes steps for encoding additional documents into embedding model indexing in vector database performing similarity search retrieving chunks and passing to LLM. REFRAG section expands with user query encoding computation of token-level embeddings application of RL-trained relevance policy for chunk selection selective expansion of chosen chunks concatenation of query and selected chunk embeddings with compressed rejected chunks and input to LLM. Elements include numbered steps arrows connecting components like documents query chunks policy and final response boxes.](https://pbs.twimg.com/media/G3CkNK8aoAAVzyJ?format=jpg&name=large)

---

**Karim C** @BrandGrowthOS [2025-10-12](https://x.com/BrandGrowthOS/status/1977378832152711265)

  
看起来很有前景。有代码或 API 可用吗？我想在内容代理中测试一下——需要快速的首字节时间、去重的内容块、按租户的认证，以及 CMS 更新时的缓存失效功能。

---

**Avi Chawla** @\_avichawla [2025-10-12](https://x.com/_avichawla/status/1977394466404098233)

  
他们尚未发布代码。论文中虽附有 GitHub 仓库链接（即：https://github.com/facebookresearch/refrag…），但当前仍未公开代码。
