---
title: "2026-03-06_Aliez_Ren_Aliez_Ren_跑本地大模型真令人上瘾_从最开始的用_LM_Studio_Ollama"
source: "https://x.com/aliez_ren/status/2029588517148672415"
author:
  - "[[@Aliez Ren]]"
published: 2026-03-06
created: 2026-03-06
description:
tags:
  - "x"
  - "@Aliez Ren"
  - "ren"
  - "lm"
---

# Aliez Ren 跑本地大模型真令人上瘾，从最开始的用 LM Studio，Ollama，

**Aliez Ren**

跑本地大模型真令人上瘾，从最开始的用 LM Studio，Ollama，改为使用 llama.cpp，使用 Unsloth 量化的 GGUF。再到 vLLM，SGLang，KTransformers 都摸索了一遍，然后发现目前的工具其实对于 RTX 5090 (sm120) 的 FP4 支持的都不太好，虽然能运行 4bit 量化模型省显存，但都还无法利用原生 FP4 硬件加速。虽然都是 Blackwell 架构，但服务器上的 B200 和家用的 RTX 5090 区别很大，最终走向了自己修改编译 SGLang 的道路。

![图片](https://pbs.twimg.com/media/HCqL_4pbAAAs2ka?format=jpg&name=large)

* * *

### 热门回复

**@IndenScale** ♥ 3 · 💬 2

羡慕有 5090 4090 玩起来还是太麻烦了。

**@鸭雀无声** ♥ 3 · 💬 0

DGX Spark上的GB10 (sm121) 也是一个境遇，不好优化主要是每个SM可访问共享内存只有99KB，相比之下B200的是227KB。目前在这两个上用vLLM跑NVFP4还是只能靠社区的补丁。我测试5090上的qwen3.5-35b-a3b-nvfp4可以到200t/s，250k上下文的情况下依然有160k/s，Spark上只有50t/s，250k上下文35t/s，速度还行

**@LotusDecoder** ♥ 2 · 💬 0

同感， lm studio 做 api 还是不太稳， 适合快速拉起在gui里聊天。

**@Elaina** ♥ 0 · 💬 1

羡慕有5090 32GB可以直接把27B模型8bit塞进去了

**@Aliez Ren** ♥ 0 · 💬 1

但那样留给 kv cache 的空间就太少了，上下文太短没法用。我用的是 Q6\_K\_XL