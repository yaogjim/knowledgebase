---
title: "使用 ColQwen2 对 PDF 进行多模态检索增强生成（RAG）"
source: "https://x.com/helloiamleonie/status/1962482840810975527"
author:
  - "[[@helloiamleonie]]"
published: 2025-09-03
created: 2025-09-03
description:
tags:
  - "@helloiamleonie #ColQwen2 #PDF #多模态检索 #RAG"
---
**Leonie** @helloiamleonie [2025-09-01](https://x.com/helloiamleonie/status/1962482840810975527)

  
使用 ColQwen2 对 PDF 进行多模态检索增强生成（RAG）

（无需任何光学字符识别、布局检测或分块）

在本教程中，我和我的同事托比亚斯将向你展示如何构建一个基于 PDF 的多模态 RAG 管道：

• 使用多模态后期交互模型 ColQwen2 将 PDF 页面的截图作为图像嵌入

• 存储在 @weaviate\_io 向量数据库中

• 使用 ColQwen2 嵌入文本查询，以便在查询时从数据库中检索 PDF 文件

• 使用 VLM Qwen2.5-VL 生成答案

GitHub: https://github.com/weaviate/recipes/blob/main/weaviate-features/multi-vector/multi-vector-colipali-rag.ipynb…

（注：这段英文中包含的网址等内容无需翻译，直接保留原文即可，因为其属于特定的链接标识，在中文语境下也常以英文形式呈现。如果硬要翻译链接中的单词，反而不符合网络链接的使用习惯。所以整体翻译后还是保留链接部分英文原文）

GitHub: https://github.com/weaviate/recipes/blob/main/weaviate-features/multi-vector/multi-vector-colipali-rag.ipynb…

![A diagram illustrating a multimodal RAG pipeline over PDFs. The process starts with ingesting PDF documents as images, followed by interaction with ColQwen2. The images are then stored in a Weaviate vector database. At query time, the text query is embedded with ColQwen2 to retrieve relevant PDFs from the database. Finally, Qwen2.5-VL generates an answer based on the retrieved PDFs and the query. The diagram includes steps labeled as Ingest, Retrieve, and Augment, with specific models and tools mentioned.](https://pbs.twimg.com/media/Gzwjt1FWwAAkOao?format=png&name=large)

---

**Rishi** @anxious599 [2025-09-01](https://x.com/anxious599/status/1962483282676969493)

  
它能针对医疗处方进行微调吗？

我无法使用语言模型从医疗处方中获取准确数据

---

**Leonie** @helloiamleonie [2025-09-01](https://x.com/helloiamleonie/status/1962483955040395631)

  
是的，我认为那应该是可行的。

标记 @ManuelFaysse 以及 @tonywu\_71 以便获取更好的信息 :)
