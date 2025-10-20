---
title: "\"从零实现vLLM系列 - 第四篇: RMSNorm(均方根归一化)\""
source: "https://x.com/dotey/status/1979951205607674197"
author:
  - "[[@dotey]]"
published: 2025-10-20
created: 2025-10-20
description:
tags:
  - "@dotey # vLLM # Transformer # RMSNorm # 人工智能 # 自然语言处理"
---
**宝玉** @dotey 2025-10-19

推荐阅读汉松写的《从零实现 vLLM》系列，都写的挺浅显易懂的👍

> 2025-10-19
> 
> 从零实现 vLLM 的第四篇文章，我们将目光转向 Transformer 架构中另一个看似简单、却至关重要的组件：RMSNorm（均方根归一化）。
> 
> 我们先来看看什么是归一化，假设你刚考完期末考试，三门课的成绩出来了：
> 
> 数学：120分（满分150）
> 
> 英语：80分（满分100）
> 
> 物理：160分（满分200）
> 
> ![Image](https://pbs.twimg.com/media/G3oHA3CXQAAGh2Y?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G3oHA26XsAAAxmS?format=jpg&name=large)

---

**汉松** @Yonah\_x [2025-10-19](https://x.com/Yonah_x/status/1980046402643234906)

感谢宝玉老师推荐，我也是边学边写，写的不对的地方，欢迎大家指正。

---

**Nebius AI Studio** @nebiusaistudio

Your AI deserves freedom, not friction. Discover how Nebius gives you ownership with complete privacy.  
您的 AI 应享有自由，而非束缚。探索 Nebius 如何让您在完全隐私中拥有自主权。