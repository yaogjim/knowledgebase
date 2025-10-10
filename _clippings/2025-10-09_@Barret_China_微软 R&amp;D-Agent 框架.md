---
title: "微软 R&amp;D-Agent 框架"
source: "https://x.com/Barret_China/status/1975904199683752364"
author:
  - "[[@Barret_China]]"
published: 2025-10-09
created: 2025-10-09
description:
tags:
  - "@Barret_China #微软 #R&amp;D-Agent #AI #科研 #量化投资 #智能体"
---
**Barret李靖** @Barret\_China [2025-10-08](https://x.com/Barret_China/status/1975904199683752364)

推荐学习下微软搞的这个 R&D-Agent 框架，https://github.com/microsoft/RD-Agent… ，它是一个让 AI 能够自己做科研的系统——能提出问题、设计实验、验证结果、总结规律，整套科研流程都能自动化执行。

微软还基于这套框架，构建了一个用于量化投资研究的智能体 R&D-Agent(Q)，https://github.com/microsoft/qlib，并与开源量化平台 Qlib 结合，实现了自动化因子挖掘与策略优化。照这个趋势发展下去，未来的量化研究，恐怕真得交给 AI 来操盘了，😅

R&D-Agent 的整体架构分为两个阶段：研究阶段（Research Phase）和开发阶段（Development Phase）。研究阶段由四个部分组成：规划、探索路径结构、推理管线和记忆上下文，它们通过反馈机制持续循环，不断在假设、实验与分析之间往复，让系统在多轮探索中自动调整方向、积累知识、优化策略；开发阶段则承接研究成果，主要包括编码工作流与评估策略，前者把想法变成可执行代码，后者负责验证与对比结果，确保系统演化出的改进真实可靠。两个阶段形成首尾相接的闭环，让科研过程实现持续反馈与自我进化。

从本质上看，R&D-Agent 不是在“模拟科研”，而是在“系统化科研”。它让科学探索从线性的人力流程，转变为并行的智能网络。每一次假设的提出与验证，都会被记录下来，形成一份不断扩展的知识图谱，让科研活动变得可编排、可追踪、可积累。

相关论文：1）《R&D-Agent: An LLM-Agent Framework Towards Autonomous Data Science》，https://arxiv.org/abs/2505.14738 ；2）《Qlib: An AI-oriented Quantitative Investment Platform》，https://arxiv.org/abs/2009.11189

![Image](https://pbs.twimg.com/media/G2vSSnvaoAEQkzX?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G2vSV7RbUAA6pHj?format=jpg&name=large)
