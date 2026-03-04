---
title: "2026-03-02_Alex_Cheema_Alex_Cheema_It_feels_ironic_that_stacking_mac"
source: "https://x.com/alexocheema/status/2027883427358281848"
author:
  - "[[@Alex Cheema]]"
published: 2026-03-02
created: 2026-03-02
description:
tags:
  - "x"
  - "@Alex Cheema"
  - "memory"
  - "run"
---

# Alex Cheema It feels ironic that stacking mac

**Alex Cheema**

It feels ironic that stacking mac studios is the cheapest way to run frontier AI today. But it actually makes sense. Nothing else beats the memory unit economics of Apple Silicon. Memory and memory bandwidth (not FLOPS) is what matters for local inference. Everything runs at batch\_size=1.

[@karpathy](/karpathy)

talked about this at his AI SUS keynote: personal computing v2 is coming. Just look at the numbers: M3 Ultra: $18/GB, $6.70/GB/s DGX Spark: $36/GB, $17/GB/s B200 (DGX): $360/GB, $8/GB/s Memory for B200 is 20x more expensive. Memory bandwidth for DGX Spark is 2.5x more expensive. If DeepSeek V4 is >1T parameters (as it’s rumoured to be), by far the cheapest way to run it will be Apple Silicon. M5 Ultra will likely push this further. NVIDIA has completely missed this segment of the market.

![图片](https://pbs.twimg.com/media/HCR9Oj2WoAA_Ip2?format=jpg&name=large)

> **@\_\_tinygrad\_\_**
> 
> This isn't the right question. The question is what's the cheapest hardware that will run the largest open source models at 100+ tok/s. Something is out of alignment if it's stacks of Mac Studios, which it actually might be. x.com/KimNoel399/sta…

![Square profile picture](https://pbs.twimg.com/profile_images/1772444459625766913/1meZwC16_normal.jpg)

* * *

### 热门回复

**@Alex Cheema** ♥ 30 · 💬 6

For now. You can run Kimi K2.5 on two, $19k. Consumers aren’t doing this today, but a lot of businesses are.

**@Cryptaveli** ♥ 21 · 💬 3

AMD isn't far behind. Ryzen AI Max+395 mini PC's deliver m3 ultra level inference perf on 70B-120B models with the added benefit of the ability to install Linux. AMD has a shot at pulling ahead in running local AI in the near future. AMD AI Max +395: $16/GB, $7.8/GB/s

**@Alex Cheema** ♥ 20 · 💬 3

To be a serious competitor for this they need: - More than 128GB memory per device. - Tensor parallelism with low-latency RDMA.

**@Matthew Berman** ♥ 16 · 💬 2

Which model do you run on that?

**@Eric Fontaine** ♥ 14 · 💬 2

For Qwen3.5-35B-A3B-GGUF I'm getting 150 tok/sec on my 5090 seems like good economics are you looking only at unquant?