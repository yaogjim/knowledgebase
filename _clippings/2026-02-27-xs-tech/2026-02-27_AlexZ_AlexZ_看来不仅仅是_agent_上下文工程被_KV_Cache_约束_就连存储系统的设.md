---
title: "2026-02-27_AlexZ_AlexZ_看来不仅仅是_agent_上下文工程被_KV_Cache_约束_就连存储系统的设"
source: "https://x.com/blackanger/status/2027121925433258157"
author:
  - "[[@AlexZ]]"
published: 2026-02-27
created: 2026-02-27
description:
tags:
  - "x"
  - "@AlexZ"
  - "agent"
  - "kv-cache"
---

# AlexZ 看来不仅仅是 agent 上下文工程被 KV-Cache 约束，就连存储系统的设

**AlexZ**

看来不仅仅是 agent 上下文工程被 KV-Cache 约束，就连存储系统的设计也要受 KV-Cache 主导了。 刚刷到一篇论文：《DualPath: Breaking the Storage Bandwidth Bottleneck in Agentic LLM Inference》（2026-02-21 版本） prefill 需要从外部存储读取大量 KV-Cache，prefill 侧的存储 NIC 很容易被打满，而 decode 侧的存储 NIC 却闲着，造成系统整体吞吐上限被 prefill 侧的 I/O 卡死。 这就是论文说的“prefill-side storage network bandwidth bottleneck”。 agent 推理体系战场要从算力转移到数据搬运上了？ RDMA 又有用武之地了。

> **@blackanger**
> 
> 我不太懂。 为什么像现在的 agent ，比如 claude code / codex 就不能实现一个「滑动窗口」机制来处理上下文。 不做有损压缩，而是把全量 Session 历史存入外部记忆，窗口里只放当前任务步骤真正需要的内容。 窗口不是按时间顺序固定滑动，而是按需求动态组装。

![🦀](https://abs-0.twimg.com/emoji/v2/svg/1f980.svg)

* * *

### 热门回复

**@CrazyCao** ♥ 1 · 💬 0

llm也在推pd（prefill/decode）分离，llm的kv cache是在p阶段，任何外部的上下游优化都不能忽略了这一层缓存。它傻瓜又高效，和传统的缓存一样。复杂的是，他会先对input做tokenization，而且会随着session的延续而膨胀。