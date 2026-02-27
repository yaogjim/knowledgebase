---
title: "2026-02-27_常为希_币安人生_Ai奇点_常为希_币安人生_Ai奇点_Qwen3_5_35B_A3B_本地_AI_从_demo_走向"
source: "https://x.com/CryptoYunqi/status/2026984257718223184"
author:
  - "[[@常为希 币安人生（Ai奇点）]]"
published: 2026-02-27
created: 2026-02-27
description:
tags:
  - "x"
  - "@常为希 币安人生（Ai奇点）"
  - "币安人生ai奇点"
  - "qwen3"
---

# 常为希 币安人生（Ai奇点） Qwen3.5-35B-A3B：本地 AI 从 demo 走向

**常为希 币安人生（Ai奇点）**

Qwen3.5-35B-A3B：本地 AI 从 demo 走向生产的分水岭 一、Qwen引发的震动 2026 年 2 月，

[@sudoingX](/sudoingX)

在 X 上分享了一段测试数据：Qwen3.5-35B-A3B在单卡 RTX 3090（24GB VRAM）上跑出了 112-114 tok/s的生成速度，原生支持 262K 上下文长度，全程性能平直无衰减。 这听起来可能只是又一个模型评测？不。这是 Local AI（本地人工智能）从 demo 走向生产的分水岭时刻。 量化精度：4-bit Q6\_K（约 19.7GB VRAM），零 offload、全 GPU 运行。

![图片](https://pbs.twimg.com/media/HCFLcAyagAA5m6z?format=jpg&name=large)

* * *

### 热门回复

**@阿蔺A-Lin** ♥ 3.6K · 💬 29

好消息：文章质量很高 坏消息：应该很快就会被搬运到咸鱼上架了

**@Kyle Becker** ♥ 61 · 💬 10

My new book is out soon! Hypernea: The Cursed Kingdom is an epic fantasy novel about collapsing civilizations. The first book in The Fallen Empires series is about the struggle of heroes to overcome social stigma and to display the courage to embrace the ultimate truth. Join

**@常为希 币安人生（Ai奇点）** ♥ 7 · 💬 2

五、给本地部署者的行动建议 如果你已有 RTX 3090/4090 1.编译 llama.cpp from source with CUDA（默认设置会在 262K 时 OOM，需特定 flag） 2.量化到 Q4\_K\_M：省 30% 显存，速度 +20%，质量损失<5% 3.测试 Agent 工作流：尝试本地化 Claude Code、AutoGPT 等工具 如果你还在用 80B+ Transformer

**@常为希 币安人生（Ai奇点）** ♥ 5 · 💬 1

三、技术拆解：为什么能平直缩放？ 传统 Transformer 的困境 过去我们跑长文本推理时，会遇到一个物理瓶颈：KV Cache 随上下文长度线性增长。这意味着： •32K → 64K 翻倍，显存消耗翻倍 •128K → 256K 再翻倍，单卡直接 OOM •要跑更长？加 GPU、加内存、加钱 Qwen3.5-35B-A3B 的解法：Mamba2 + MoE 混合架构 这条推文的技术细节来自 llama.cpp from source with CUDA，作者手动编译解锁了特定 flag 才能跑通 262K。核心设计是： 1.30 out of 40 layers = Mamba2 Statespace（75% 层与上下文长度无关） 2.仅 10 layers 携带 KV Cache（注意力机制只在这部分运行） 3.固定内存占用: 无论 4K 还是 262K，显存消耗一致 http:// 4.MoE 稀疏激活: 每次 token 只激活 3B params

**@常为希 币安人生（Ai奇点）** ♥ 3 · 💬 1

模型GPUtok/s上下文 Qwen3.5-35B-A3B (本次)RTX 3090112262K Qwen Coder Next 80B单卡 30901.332K Qwen Coder Next 80B2×30904632K 关键洞察: 传统 Transformer 架构的 KV Cache 随上下文线性增长，导致长文本推理成本爆炸。Qwen3.5-35B-A3B 用 Mamba2 解决了这个问题——75% 的层根本不需要维护 KV Cache。