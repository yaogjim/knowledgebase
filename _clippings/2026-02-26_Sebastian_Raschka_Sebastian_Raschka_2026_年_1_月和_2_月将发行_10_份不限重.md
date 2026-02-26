---
title: "2026-02-26_Sebastian_Raschka_Sebastian_Raschka_2026_年_1_月和_2_月将发行_10_份不限重"
source: "https://x.com/rasbt/status/2026659971467706603"
author:
  - "[[@Sebastian Raschka]]"
published: 2026-02-26
created: 2026-02-26
description:
tags:
  - "x"
  - "@Sebastian Raschka"
  - "https"
  - "image"
---

# Sebastian Raschka # 2026 年 1 月和 2 月将发行 10 份不限重

**Sebastian Raschka**

# 2026 年 1 月和 2 月将发行 10 份不限重量级 LLM 债券

如果你上个月一直难以跟上开源软件的发布，这里按时间顺序概述了主要的开源软件，重点关注其架构设计。

## 

1) Arcee AI Trinity Large（1 月 27 日）

Arcee 的 Trinity 系列对我们很多人来说都是横空出世。它是一款 400 字节 MoE（13 字节活动）处理器，外加两个更小的衍生型号。从架构上看，它融合了我们熟悉的元素：混合专家（MoE）+ 分组查询注意力（GQA）+ 滑动窗口注意力（SWA）。

[

![Image](https://pbs.twimg.com/media/HB-Yu-qWkAAKgUc?format=jpg&name=medium)


](/rasbt/article/2026659971467706603/media/2026506290202054656)

## 

2) Moonshot Kimi K2.5（1 月 27 日）

与 Kimi K2 类似，Kimi K2.5 也是参数量最大的开放权重模型之一，拥有 1 万亿个参数。同样，它也采用了类似 DeepSeek 的模型模板。

[

![Image](https://pbs.twimg.com/media/HB-YzIuW8AAxNHf?format=jpg&name=medium)


](/rasbt/article/2026659971467706603/media/2026506361622687744)

## 

3) StepFun Step 3.5 Flash（2 月 1 日）

步骤 3.5 Flash 主要侧重于性能和吞吐量的平衡。总体而言，它与 Arcee Trinity 有些相似，都采用了 GQA + SWA 技术，但体积只有 Arcee Trinity 的一半。

[

![Image](https://pbs.twimg.com/media/HB-Y05QXkAAGDDL?format=jpg&name=medium)


](/rasbt/article/2026659971467706603/media/2026506391830106112)

## 

4) Qwen3-Coder-Next（2 月 3 日）

Qwen3-Coder-Next 延续了 Qwen 在编码模型中混合注意力机制方面的研究方向。其架构（和规模）与之前的 800 亿 Qwen3-Next 模型类似，但针对编码环境进行了优化调整。

[

![Image](https://pbs.twimg.com/media/HB-Y3RyXkAAxVhe?format=jpg&name=large)


](/rasbt/article/2026659971467706603/media/2026506432774901760)

## 

5）

[z.AI](//z.AI)

GLM-5（2 月 12 日）

GLM-5 是一个旗舰级版本，它与当前“大幅提升性能 + 效率优化”的共识基本一致。它还包含一些受 DeepSeek 启发的改进（例如 MLA 和 DeepSeek 稀疏注意力机制）。

[

![Image](https://pbs.twimg.com/media/HB-Y-muXQAAWjFe?format=jpg&name=medium)


](/rasbt/article/2026659971467706603/media/2026506558654332928)

## 

6) MiniMax M2.5（2 月 12 日）

MiniMax M2.5 特别有趣，因为它性能强劲，但外观却保持了非常经典的风格，采用了普通的 GQA 镜片。

[

![Image](https://pbs.twimg.com/media/HB-ZAutXMAAZTB6?format=jpg&name=medium)


](/rasbt/article/2026659971467706603/media/2026506595157356544)

## 

7) 南贝米色 4.1 3B（2 月 13 日）

Nanbeige 4.1 3B 是本次发布系列中比较有趣的“小巧”型号之一。它本质上是一款 Llama 3 风格的型号（类似于 Qwen3 系列的密集型型号）。

[

![Image](https://pbs.twimg.com/media/HB-ZCjaW4AAFNo8?format=jpg&name=medium)


](/rasbt/article/2026659971467706603/media/2026506626484592640)

## 

8) Qwen3.5（2 月 15 日）

Qwen3.5 (397B-A17B) 很有意思，因为 Qwen 团队现在似乎也将混合注意力机制应用到了他们的主要（非 Next）产品线中。

[

![Image](https://pbs.twimg.com/media/HB-ZEREWwAA3ZVK?format=jpg&name=medium)


](/rasbt/article/2026659971467706603/media/2026506655920209920)

## 

9) 蚂蚁群凌2.5/环2.5（2月16日）

与 Kimi 类似，Ling/Ring 2.5 也是一个参数量达 1 万亿的迭代模型。它采用了一种混合方案，结合了 Lightning Attention 和 MLA 式压缩。从概念上讲，它与 Qwen3.5 有些相似，但其线性注意力机制略微简化（与 Gated DeltaNet 相比）。

[

![Image](https://pbs.twimg.com/media/HB-ZF-jW0AE280x?format=jpg&name=medium)


](/rasbt/article/2026659971467706603/media/2026506685309702145)

## 

10) Cohere Tiny Aya（2 月 17 日）

Tiny Aya 是一个较小的多语言模型，但从架构角度来看，它采用了有趣的并行 Transformer 模块设计。

[

![Image](https://pbs.twimg.com/media/HB-ZKa6XwAAgypg?format=jpg&name=medium)


](/rasbt/article/2026659971467706603/media/2026506761641902080)

## 

摘要概述

如果说 2026 年春季架构发展趋势有什么关键点，那就是架构基本上都是以自回归 Transformer 为中心。没有什么全新的东西（不过，DeepSeek V4 还没发布呢）。

然而，我们看到越来越多的架构从更经典的 GQA 转向 MLA 甚至线性注意力混合架构，这意味着效率（更低的延迟和更长的上下文性能扩展）变得越来越重要。

[

![Image](https://pbs.twimg.com/media/HB-ZPhXW4AA-ddH?format=jpg&name=medium)


](/rasbt/article/2026659971467706603/media/2026506849273438208)

这只是对一篇篇幅更长、内容更详尽的文章的简要概述。如果您感兴趣，可以阅读《开放权重 LLM 的春天之梦：2026 年 1 月至 2 月的 10 种架构》一文，了解更多信息。

[https://magazine.sebastianraschka.com/p/a-dream-of-spring-for-open-weight](https://magazine.sebastianraschka.com/p/a-dream-of-spring-for-open-weight)