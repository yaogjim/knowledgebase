---
title: "LMMs 模拟器化"
source: "https://x.com/karpathy/status/1997731268969304070"
author:
  - "[[@karpathy]]"
date: "2025-12-10T11:57:03+08:00"
created: 2025-12-10
description:
tags:
  - "@karpathy AI 设计 # 人工智能 # 模拟器 # LLMs # 语言模型"
---
**Andrej Karpathy** @karpathy [2025-12-07](https://x.com/karpathy/status/1997731268969304070)

  
不要将 LLMs 视为实体，而应视作模拟器。例如，在探讨某个话题时，不要问：

你对 xyz 有什么看法？

没有"你"。下次试试：

探索 xyz 的合适人群会是哪些？他们会说些什么？

大型语言模型能够模拟多种视角，但它并不会像人类那样经过长期思考对某个问题形成固有见解。若通过"你"这样的称谓强行要求，它只会根据微调数据中的统计特征调用对应的人格嵌入向量进行角色扮演。这种做法虽无不可，但比起人们常赋予"询问 AI"的神秘色彩，其本质实则平淡无奇。

---

**Andrej Karpathy** @karpathy [2025-12-09](https://x.com/karpathy/status/1998245684521353664)

  
顺便说一句，很多人误解了这条推文，这是我的错。我并不是建议人们使用“你是一位专家级 Swift 程序员”之类的旧式推广技巧，没关系。

---

**Dimitris Papailiopoulos** @DimitrisPapail [2025-12-07](https://x.com/DimitrisPapail/status/1997732822887567503)

  
它难道不会采纳最有可能获得最高回报的个性，也就是最适合回答该问题领域的专家个性吗？

---

**Andrej Karpathy** @karpathy [2025-12-07](https://x.com/karpathy/status/1997759548543947249)

  
确实有大量工作投入到构建“你”这个模拟人格上——这个在可验证问题中获得全部奖励、赢得用户/评判 LLMs 所有点赞、或模仿 SFT 回应的人格，最终会涌现出一个复合型人格。我的观点是

---

**Dimitris Papailiopoulos** @DimitrisPapail [2025-12-07](https://x.com/DimitrisPapail/status/1997769606413406443)

  
那么，我们可以这样来理解：

P(输出|输入) = Σ\_角色 P(输出|角色, 输入) × P(角色|输入)

在可验证的领域，强化学习已经将 P(人格|输入)聚焦于奖励最大化的人格塑造（如果操作得当的话）。经过精心设计的"你"是被优化且外显的人格化身。
