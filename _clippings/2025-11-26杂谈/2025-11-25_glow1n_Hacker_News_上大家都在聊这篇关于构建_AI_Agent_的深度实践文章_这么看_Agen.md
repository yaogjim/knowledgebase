---
title: "2025-11-25_glow1n_Hacker_News_上大家都在聊这篇关于构建_AI_Agent_的深度实践文章_这么看_Agen"
source: "https://x.com/glow1n/status/1992566241031299539"
author:
  - "[[@glow1n]]"
published: 2025-11-25
created: 2025-11-25
description:
tags:
  - "x"
  - "@glow1n"
  - "agent"
  - "https"
status: "inbox"
importance: 2
effort: 2
review_level: 0
review_next: "2025-12-10"
review_interval: null
review_count: 0
decision: null
topics: []
links_out: []
summary: ""
pov: ""
actions: []
---

# Hacker News 上大家都在聊这篇关于构建 AI Agent 的深度实践文章，这么看，Agen

**Glowin** @glow1n [2025-11-23](https://x.com/glow1n/status/1992566241031299539)

Hacker News 上大家都在聊这篇关于构建 AI Agent 的深度实践文章，这么看，Agent 设计确实还很难。​​​​​​​​​​​​​​​​

作者的核心发现：直接用原生 SDK 比高层抽象更灵活；显式缓存管理虽麻烦但更可控；强化学习在循环中作用巨大；需要文件系统般的共享层避免工具死胡同；输出工具的语气控制出乎意料地难。最头疼的是测试评估，目前无完美方案。

* * *

**Glowin** @glow1n [2025-11-23](https://x.com/glow1n/status/1992623907124527429)

这篇文章分享了作者在构建 AI Agent 过程中的实践经验和教训，主要涵盖以下核心要点：

SDK 选择的反思作者

团队最初选择了 Vercel AI SDK，但后来发现直接使用原生 SDK（如 Anthropic SDK）更合适。原因是：不同模型之间差异显著，需要自建 agent 抽象层；高层 SDK 在处理提供商侧工具（如 Anthropic 的网页搜索）时会出现问题；原生 SDK 在缓存管理和错误提示方面更清晰。

缓存管理策略

Anthropic 的显式缓存管理虽然需要手动控制，但作者认为这是优势而非劣势。它让成本和缓存利用更可预测，允许对话分支和上下文编辑。具体策略是：在系统提示后设置一个缓存点，对话开始处设置两个缓存点，最后一个随对话尾部移动。

强化学习的重要性

在 agent 循环中，强化（reinforcement）扮演了比预期更重要的角色。每次工具调用后，不仅返回数据，还可以：提醒 agent 整体目标和任务状态；在工具失败时提供提示；通知后台状态变化。有时甚至使用"自我强化"工具，比如简单地回显任务列表就能有效推动 agent 前进。

故障隔离机制

为避免大量失败污染上下文，可采用两种策略：使用子 agent 运行可能需要迭代的任务，只返回成功结果和失败总结；利用上下文编辑删除不必要的失败信息（但会使缓存失效）。

共享状态系统

Agent 需要一个类似文件系统的共享层来存储数据，避免出现"死胡同"——即任务只能在特定工具内继续执行。通过虚拟文件系统，不同工具（代码执行、图像生成、推理等）可以读写相同位置的数据。

输出工具的挑战

使用专门的输出工具（而非直接用对话输出）与用户沟通时，面临意外的困难：难以控制措辞和语气；有时 agent 不调用输出工具；使用子模型调整语气会降低质量和增加延迟。

模型选择

Haiku 和 Sonnet 仍是最佳工具调用者，适合主循环；Gemini 2.5 适合处理大文档、PDF 和图像提取；GPT 系列在主循环中表现一般。更好的工具调用者虽然单价可能更高，但在循环中总成本可能更低。

测试与评估难题

这是最困难的问题。由于 agent 的复杂性，无法在外部系统简单地做评估，需要基于可观测性数据或实际测试运行。作者坦言目前尚未找到满意的解决方案。

文章最后提到作者正在试用 Amp 编码 agent，欣赏其子 agent（如 Oracle）与主循环的交互设计，认为这是由真正使用自己工具的人构建的产品。

* * *

**Art Lab** @daemonzhang6 [2025-11-24](https://x.com/daemonzhang6/status/1992860408663970137)

如今群雄逐鹿，天下未定。看不清谁是曹操，选个袁绍啥的不能算错。但是，找公孙瓒投靠？是不是觉得自己是赵云🤔啊。

Agent 在目前只能选OpenAI, Anthropic 的工具链。其他的3月后还存在不存在都未可知啊。

* * *

**Zack Chapple** @Zackary\_Chapple [2025-11-24](https://x.com/Zackary_Chapple/status/1992913902041207257)

We have been actively working on the testing and evaluation part and think we've arrived at a really helpful solution, at least for our use cases. The hardest part was evolving benchmarks that are not instantly stale.

我们一直在积极研究测试与评估环节，并认为已经找到了极具实用价值的解决方案——至少对我们的应用场景而言如此。最困难的部分在于构建不会迅速过时的动态基准。