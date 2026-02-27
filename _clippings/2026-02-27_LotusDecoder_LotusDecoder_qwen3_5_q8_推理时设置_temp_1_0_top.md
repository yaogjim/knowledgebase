---
title: "2026-02-27_LotusDecoder_LotusDecoder_qwen3_5_q8_推理时设置_temp_1_0_top"
source: "https://x.com/LotusDecoder/status/2027166166616330619"
author:
  - "[[@LotusDecoder]]"
published: 2026-02-27
created: 2026-02-27
description:
tags:
  - "x"
  - "@LotusDecoder"
  - "--temp"
  - "--top-p"
---

# LotusDecoder qwen3.5-q8 推理时设置 --temp 1.0 --top

**LotusDecoder**

qwen3.5-q8 推理时设置 --temp 1.0 --top-p 0.95 --top-k 20 --min-p 0.00 避免 thinking 陷入死循环。 实测有降低概率。

> **@danielhanchen**
> 
> This sometimes happens due to over thinking. I checked Q8\_0 & BF16, and if the params in our guide https://unsloth.ai/docs/models/qwen3.5… ie --temp 1.0 --top-p 0.95 --top-k 20 --min-p 0.00 weren't used, then it'll loop sometimes. Also Qwen suggested presence penalty so that should help.
> 
> 这种情况有时是由于想得太多了。我检查了 Q8\_0 和 BF16，如果未使用我们指南 https://unsloth.ai/docs/models/qwen3.5 … 中的参数 （例如 --temp 1.0 --top-p 0.95 --top-k 20 --min-p 0.00），则有时会出现循环。此外，Qwen 建议使用存在惩罚，这应该会有所帮助。