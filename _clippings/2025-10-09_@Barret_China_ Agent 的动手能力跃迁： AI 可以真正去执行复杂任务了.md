---
title: " Agent 的动手能力跃迁： AI 可以真正去执行复杂任务了"
source: "https://x.com/Barret_China/status/1975861192548548974"
author:
  - "[[@Barret_China]]"
published: 2025-10-09
created: 2025-10-09
description:
tags:
  - "@Barret_China # AI # 传统软件工程 # 机器学习  # 人工智能 # 机器人"
---
**Barret李靖** @Barret\_China [2025-10-08](https://x.com/Barret_China/status/1975861192548548974)

Agent 的动手能力，已经在过去一年经历了显著的跃迁。它不再只是会“聊天”的模型，而是可以真正去动手、去执行复杂任务的智能体。那么现在它能做到什么？已经能解决多复杂的软件工程问题？又该如何在社区里找到最强框架并复用到自己的项目？下面是几条更实用的思路。  
  
要评估一个 Agent 的动手能力，无论它是单一的 LLM，还是 LLM 加上外部工具的工程实现，最终都要回到数据集上。因为数据集定义了“考试题目”，而 benchmark 决定了“评分标准”。目前能全面评估 Agent 工程执行力的两个核心数据集，一个是 OpenAI 的 SWE-bench（software engineering-bench），另一个是 THUDM 提供的 Agent-Bench。前者聚焦真实软件仓库的 bug 修复与功能实现，是“AI 程序员”的试炼场；后者覆盖更广，从软件、操作系统、网络、推理、工具使用到多模态交互，是对 Agent 通用智能和工具操作能力的系统化测评。  
  
什么才算一个好的 Agent，还得回到问题域上看。SWE-bench 的目标是让 Agent 能像程序员一样理解代码、修补缺陷、通过单测；而 Agent-Bench 则像是在考察一个“通才型工程助理”，既要能读懂文档、用命令行、写代码，又要能跨工具协作、执行复杂任务链。前者考工程深度，后者考任务广度。这两个维度，几乎定义了 Agent 的“手工能力边界”。  
  
理解这个边界，还得区分哪些问题是 LLM 本身可以解决的，哪些必须依赖外部工具。从大模型的演进来看，许多原本需要显式工具链配合的能力，正在逐步被“内化”进模型本体。Chain of Thought 已经演化为参数化的推理能力（Reasoning），知识图谱的结构化记忆也被吸收到模型的参数知识（Parametric Knowledge）中。而最近阿里开源的 Tongyi DeepResearch，正是这种趋势的最新代表：它通过强化学习（RL）直接训练模型具备“研究型行为”，主动检索、阅读、摘要、再检索，在真实网络环境中形成自我迭代的探索闭环。  
  
要找到好用的 Agent 框架或最佳实践，最直接的办法就是去看各大数据集的打榜记录，榜单上往往能看到社区最新的开源成果与架构思路。SWE-bench 有一个官方 leaderboard，目前得分最高的方案往往来自一些 AI IDE 工具，比如 TRAE、Augment Code 等，因为 SWE 要解决的软件工程问题，和 AI IDE 的目标几乎完全重叠，它们都想让模型在真实项目里“动手干活”。在这些榜单里，你可以找到大量可以直接复用的开源实现，例如 github@augmentcode/augment-swebench-agent、github@ByteDance-Seed/Seed-Coder 等。  
  
如果你正好在做相关方向的工作，不妨先采取“拿来主义”。SWE-bench 上最好的模型得分已经达到了 78.8 分，意味着这些 Agent 已经能解决绝大多数真实工程问题。要知道，在 2024 年三月，这个榜单的最高分还只有 12.4。短短一年，从“会写代码”到“能维护项目”，AI 的动手能力，已经跨过了一个关键分水岭。

---

**Derick** @Derick1900 [2025-10-08](https://x.com/Derick1900/status/1975905851883077841)

得分最高的没想到是trae+豆包

---

**Barret李靖** @Barret\_China [2025-10-08](https://x.com/Barret_China/status/1975906606727708756)

打榜只能作为参考，不排除对数据集过拟合的可能😄，不过能冲到第一的，肯定是有几把刷子的。

---

**Chris John** @ChrisL65886707 [2025-10-09](https://x.com/ChrisL65886707/status/1976087975655268831)

Agent 不再是聊天模型，而是不抱怨的工程师。

---

**刘皇叔** @liuhuangshuu [2025-10-08](https://x.com/liuhuangshuu/status/1975913611953623279)

接替人用电脑做的事，只是 Agent 的第一步。

重点要是接替人与人打交道的事务，联系、谈判、合作、冲突等。