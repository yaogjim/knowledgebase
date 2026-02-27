---
title: "2026-02-27_Datou_Datou_Agent_场景的特点是多轮短追加_KV_命中率极高_95_每轮对话都要读"
source: "https://x.com/Datou/status/2027040329598410987"
author:
  - "[[@Datou]]"
published: 2026-02-27
created: 2026-02-27
description:
tags:
  - "#DeepSeek"
  - "#AI"
  - "x"
  - "@Datou"
---

# Datou Agent 场景的特点是多轮短追加，KV 命中率极高（95%+），每轮对话都要读

**Datou**

Agent 场景的特点是多轮短追加，KV 命中率极高（95%+），每轮对话都要读取海量历史 KV，prefill 忙到冒烟，decode 干等数据，推理瓶颈从算力变成了存储 I/O 。 DualPath 让 decode 也直连存储拉 KV，并经 RDMA 分流给 prefill，把单入口 I/O 变双入口，带宽翻倍，推理速度也几乎翻倍。 ![👍](https://abs-0.twimg.com/emoji/v2/svg/1f44d.svg)![👍](https://abs-0.twimg.com/emoji/v2/svg/1f44d.svg)

![图片](https://pbs.twimg.com/media/HCFDL-6awAAxJwE?format=jpg&name=large)

> **@Bunnsuck**
> 
> DeepSeek released new paper!!! DualPath: Breaking the Storage Bandwidth Bottleneck in Agentic LLM Inference https://arxiv.org/abs/2602.21548 #DeepSeek #AI
> 
> DeepSeek 发布了新论文！！！DualPath：打破智能体 LLM 推理中的存储带宽瓶颈 https://arxiv.org/abs/2602.21548 #深度探索 ＃人工智能

![引用图片](https://pbs.twimg.com/media/HCFDL-6awAAxJwE?format=jpg&name=large)