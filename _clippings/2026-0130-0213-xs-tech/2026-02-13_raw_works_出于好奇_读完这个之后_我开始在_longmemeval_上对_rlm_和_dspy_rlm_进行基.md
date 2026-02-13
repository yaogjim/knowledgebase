---
title: "2026-02-13_raw_works_出于好奇_读完这个之后_我开始在_longmemeval_上对_rlm_和_dspy_rlm_进行基"
source: "https://x.com/raw_works/status/2021323835413348845"
author:
  - "[[@raw_works]]"
published: 2026-02-13
created: 2026-02-13
description:
tags:
  - "#leaderboard"
  - "x"
  - "@raw_works"
  - "https"
---

# 出于好奇，读完这个之后，我开始在 longmemeval 上对 rlm 和 dspy.rlm 进行基

**Raymond Weitekamp** @raw\_works [2026-02-10](https://x.com/raw_works/status/2021303970929479795)

出于好奇，读完这个之后，我开始在 longmemeval 上对 rlm 和 dspy.rlm 进行基准测试。

tl;dr - 我觉得今天结束前我可能会有一个新的'SOTA 内存系统'。

cc @DSPyOSS @a1zhang @lateinteraction

> 2026-02-09
> 
> 🚨宣布推出一种新的 SOTA 内存系统——观测记忆（OM），现已在最新 @mastra 版本中可用。
> 
> 它在 LongMemEval 上取得了有史以来最高的分数（gpt-4o 84.2%，gpt-5-mini 94.9%）
> 
> 无 RAG，无图表，无基于输入的检索，仅仅是一个简单的不断演进的

* * *

**Raymond Weitekamp** @raw\_works [2026-02-10](https://x.com/raw_works/status/2021303973471268923)

初步结果:

dspy.RLM + Gemini 3 Flash：87.2% on LongMemEval\_S

优于 Mastra Observational Memory + GPT-4o（84.23%），且每令牌成本仅为其五分之一。

* * *

**Raymond Weitekamp** @raw\_works [2026-02-10](https://x.com/raw_works/status/2021304330003824997)

同一个 Gemini 3 Flash 使用独立的 rlm 包时得分 57.9%。切换到 dspy.RLM（结构化输入、迭代式 REPL、SUBMIT()）后，分数增加了 29 分。

脚手架至关重要。

* * *

**Raymond Weitekamp** @raw\_works [2026-02-10](https://x.com/raw_works/status/2021307467494289911)

独立 rlm + Gemini 3 Flash: 58.0%

\- 独立 rlm + Gemini 3 Pro: 87.0%

\- dspy.RLM + Flash: 87.2%

\- Mastra OM + GPT-4o: 84.2%

* * *

**Raymond Weitekamp** @raw\_works [2026-02-10](https://x.com/raw_works/status/2021315145994056116)

并且您可能需要我的时间和成本以及 GEPA 助手围绕 DSPy.rlm =>https://github.com/rawwerks/dspy/tree/feat/rlm-multimodal-media-support…

* * *

**Raymond Weitekamp** @raw\_works [2026-02-10](https://x.com/raw_works/status/2021316718782517369)

https://github.com/stanfordnlp/dspy/issues/9289… 抄送 @DSPyOSS

* * *

**Raymond Weitekamp** @raw\_works [2026-02-10](https://x.com/raw_works/status/2021323835413348845)

dspy.RLM + Pro 最终: 89.4% (500/500)

\`\`\`

Mastra OM + GPT-4o: 84.2%（报告的）

独立的 rlms + Flash: 58.0% (500/500)

独立的 rlms + Pro: 87.0% (500/500)

dspy.RLM + Flash: 87.2% (500/500)

dspy.RLM + Pro: 89.4% (500/500) ← 新最佳

\`\`\`

按类别分解：

\- 单会话助手: 98.2%

单会话用户: 95.7%

时间推理: 91.0%

知识更新: 89.7%

单会话偏好: 90.0%

多会话: 80.5% ← 仍然是最难的

* * *

**Raymond Weitekamp** @raw\_works [2026-02-11](https://x.com/raw_works/status/2021407670197252300)

在250/500时达到91.2%。保持稳定在91%以上。预测值为216+，且判断正在追赶。

* * *

**Raymond Weitekamp** @raw\_works [2026-02-11](https://x.com/raw_works/status/2021612574488359287)

博客文章在这里：

* * *

**Mike Hostetler // Chief Agent Officer** @mikehostetler [2026-02-11](https://x.com/mikehostetler/status/2021404556576555364)

我正在用我的 Jido 框架在 Elixir 上实现 RLM，愿意就如何将其映射到 BEAM 进行合作

* * *

**Raymond Weitekamp** @raw\_works [2026-02-11](https://x.com/raw_works/status/2021406994750652537)

当然，不过是哪部分呢？我对 Elixir 一无所知，但我不确定我添加到 dspy.rlm 中的内容在完全不同的语言中是否真的会有帮助。

* * *

**Tyler Barnes** @tylbar [2026-02-10](https://x.com/tylbar/status/2021352947893109050)

我们的 Gemini 3 Flash 分数是 89.2% https://mastra.ai/research/observational-memory#leaderboard… 很乐意分享分类明细，如果你感兴趣的话

* * *

**nuclear+fallout\_imminent** @aleafindwind [2026-02-10](https://x.com/aleafindwind/status/2021343768268636478)

先生，你能测试一下 gpt-5-mini 吗？就为了满足一下好奇心

* * *

**Fabio Pauli** @fabioivsantos [2026-02-10](https://x.com/fabioivsantos/status/2021331284669219165)

在 Oolong Benchmark 测试中，使用 Grok 和我开源的 RLM-ADK 框架（一种通过智能子调用来处理长 token 上下文的递归分解方法），我获得了出色的性能

* * *

**Kev** @KevConti [2026-02-10](https://x.com/KevConti/status/2021355199307317479)

你为什么忽略 gpt-5-mini 的 94.9%分数？

* * *

**Advanced Super Intelligence** @SexyTechNews [2026-02-10](https://x.com/SexyTechNews/status/2021373535181210057)

@grok 解释这一点并将其置于上下文中

* * *

**turbo** @turbo\_xo\_ [2026-02-11](https://x.com/turbo_xo_/status/2021375970096087363)

了不起的工作！

* * *

**HPC-AI Tech** @HPCAITech

🚀 Want to get the most cost-efficient GPUs for AI?

Get access to bare-metal NVIDIA B200 Clusters. • 3.2Tb/s InfiniBand • 1.1TB+ Memory Bandwidth • Pre-configured PyTorch/LLM Stack

Run AI, ML, and HPC workloads on powerful GPUs—without any limits or wasted spend!