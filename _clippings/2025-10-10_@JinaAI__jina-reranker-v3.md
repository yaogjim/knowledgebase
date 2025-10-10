---
title: "jina-reranker-v3"
source: "https://x.com/JinaAI_/status/1974148565770338705"
author:
  - "[[@JinaAI_]]"
published: 2025-10-10
created: 2025-10-10
description:
tags:
  - "@JinaAI_ #NLP #机器学习 #深度学习 #自然语言处理 #问答系统 #信息检索"
---
**Jina AI** @JinaAI\_ [2025-10-03](https://x.com/JinaAI_/status/1974148565770338705)

Last but not late: jina-reranker-v3 is here! A new 0.6B-parameter listwise reranker that puts query and all candidate documents in one context window and SOTA on BEIR. We call this new query-document interaction "last but not late" - It's "last" because <|doc\_emb|> is placed as the final token of each document for embedding extraction. It's "not late" because, unlike late interaction models i.e. ColBERT that separately encode documents before multi-vector matching, we enable query-document-document interactions early in the forward pass. 

![A horizontal bar chart titled ](https://pbs.twimg.com/media/G2WR074XQAAQk0C?format=jpg&name=large)

---

**Jina AI** @JinaAI\_ [2025-10-03](https://x.com/JinaAI_/status/1974148568563745012)

  
在 jina-reranker-v3 中，查询在输入提示中出现两次——首次位于开头用于任务指令，末次置于结尾用于最终注意力处理。这种双重布局使最终查询位置能通过因果注意力机制关注所有前置文档。两个特殊标记用于标识嵌入提取位置：<|doc\_emb|>标记置于每个文档后标识文档嵌入提取点，而<|query\_emb|>标记则位于最终查询后标识查询嵌入提取点。这些嵌入通过共享的因果注意力机制，同时捕获局部文档语义和全局跨文档上下文信息。

![A diagram with horizontal layers labeled CODE-SCORE PROJECTOR, ENCODER-SCORE, DISCOVER BLOCK 2B, and INPUT PROMPT. Colored blocks represent documents and queries, with tokens <|doc_emb|> and <|query_emb|> marking embedding extraction points. Text includes Document 1, Document 2, Document 3, and Query, arranged in a sequence.](https://pbs.twimg.com/media/G2WUGtOWMAIDrnh?format=png&name=large)

---

**Jina AI** @JinaAI\_ [2025-10-03](https://x.com/JinaAI_/status/1974148570711548213)

  
Hugging Face 模型：https://huggingface.co/jinaai/jina-reranker-v3…

arxiv 报告链接：https://arxiv.org/abs/2509.25085

博客：
