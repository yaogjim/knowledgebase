---
title: "发布 Jupyter Agent 数据集！"
source: "https://x.com/a_yukh/status/1962911097452683710"
author:
  - "[[@a_yukh]]"
published: 2025-09-03
created: 2025-09-03
description:
tags:
  - "@a_yukh #数据科学 #机器学习 #代码执行 #JupyterNotebook"
status: "inbox"
importance: 2
effort: 2
review_level: 0
review_next: "2025-10-17"
review_interval: null
review_count: 0
decision: null
topics: []
links_out: []
summary: ""
pov: ""
actions: []
---
**Hanna Yukhymenko** @a\_yukh [2025-09-02](https://x.com/a_yukh/status/1962911097452683710)

  
发布 Jupyter Agent 数据集！

使用这些数据进行训练能显著提高执行代码和分析数据的能力。

它由 7TB 的真实 Kaggle 数据集和 2 万个笔记本构建而成，使用 Qwen3-Coder 和 E2B 创建真实的代码执行跟踪。

https://huggingface.co/datasets/data- 代理/jupyter-代理数据集 … （注：这里的“数据-代理”不太明确准确含义，可能需要结合更多背景来准确翻译“data-agents”，“jupyter-agent-dataset”直译为“Jupyter 代理数据集” ）

![A diagram of a data pipeline with arrows connecting Kaggle datasets, Qwen3-Coder, and E2B, leading to Jupyter Agent. A bar chart displays model performance with DAPT-easy scores for PL and F1 metrics. Code snippet shows Python text for loading datasets and using Jupyter Agent.](https://pbs.twimg.com/media/Gz2oafGWgAEKiol?format=jpg&name=large)

---

**Hanna Yukhymenko** @a\_yukh [2025-09-02](https://x.com/a_yukh/status/1962911101366026409)

  
我们使用 Datatrove 构建了一个管道，用于获取、去重和清理真实的 Kaggle 笔记本。我们还使用 Meta Kaggle 数据集提取了与这些真实笔记本相关的 Kaggle 数据集，这使我们能够获得非幻觉的代码执行回溯。

![Image](https://pbs.twimg.com/media/Gz2ofv9W8AAx-bN?format=jpg&name=large)

---

**Hanna Yukhymenko** @a\_yukh [2025-09-02](https://x.com/a_yukh/status/1962911103853203707)

  
然后我们使用带有 Qwen3 的教育评分管道来过滤掉嘈杂或低质量的笔记本。这大大提高了数据质量，但即使是清理后的笔记本通常也没有很好的数据分析痕迹，可能过于冗长或有点随意。

---

**Hanna Yukhymenko** @a\_yukh [2025-09-02](https://x.com/a_yukh/status/1962911106373996597)

  
我们通过使用 Qwen3 基于原始的 Kaggle 笔记本生成问答对来解决这个问题。然后，我们让 Qwen-3-Coder 使用原始数据集和通过 E2B 沙盒进行的实际代码执行来回答问题，或者使用 LLM 模拟代码执行。

此类笔记本的示例：

![Image](https://pbs.twimg.com/media/Gz2otbzWgAAveBy?format=png&name=large)

---

**Hanna Yukhymenko** @a\_yukh [2025-09-02](https://x.com/a_yukh/status/1962911109817536695)

  
通过采用受 tiny-agents 和 Qwen-Agent 启发的自定义脚手架技术，我们在工具调用和代码执行方面实现了显著的性能提升。我们使用无外部依赖的简化脚手架，从而获得了一个简单、高效的管道。

![Image](https://pbs.twimg.com/media/Gz2o1L7WoAEddkJ?format=png&name=large)

---

**Hanna Yukhymenko** @a\_yukh [2025-09-02](https://x.com/a_yukh/status/1962911112942284840)

  
那么这个数据集好用吗？我们在我们的数据集上训练了 Qwen-3 指令模型和思维模型，并使用 DABstep 基准测试来验证该数据集对模型的探索性数据分析（EDA）技能的影响。Jupyter Agent 数据集在简易分数上最多可提高 22%！

![Image](https://pbs.twimg.com/media/Gz2o4tSWYAAgF4b?format=jpg&name=large)

---

**Hanna Yukhymenko** @a\_yukh [2025-09-02](https://x.com/a_yukh/status/1962911115966349690)

  
朱庇特代理数据集是与 @\_BaptisteColle 和 @lvwerra 共同开展的一个项目

我们构建了一个具有高效脚手架的新型合成数据生成管道，在训练您的编码代理后，它能大幅提升性能

使用数据集时非常简单：

![Image](https://pbs.twimg.com/media/Gz2o83cX0AEkDgK?format=jpg&name=large)

---

**scuzzlebot** @scuzzlebot [2025-09-03](https://x.com/scuzzlebot/status/1963093460539298081)

  
对 Jupyter Agent 数据集感到兴奋！很期待看到它将如何提升数据执行能力。