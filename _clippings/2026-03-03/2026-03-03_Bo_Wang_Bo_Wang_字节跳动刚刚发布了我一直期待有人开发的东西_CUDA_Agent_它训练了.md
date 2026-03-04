---
title: "2026-03-03_Bo_Wang_Bo_Wang_字节跳动刚刚发布了我一直期待有人开发的东西_CUDA_Agent_它训练了"
source: "https://x.com/BoWang87/status/2028599174992949508"
author:
  - "[[@Bo Wang]]"
published: 2026-03-03
created: 2026-03-03
description:
tags:
  - "x"
  - "@Bo Wang"
  - "https"
  - "cuda"
---

# Bo Wang 字节跳动刚刚发布了我一直期待有人开发的东西：CUDA Agent！ 它训练了

**Bo Wang**

字节跳动刚刚发布了我一直期待有人开发的东西：CUDA Agent！ 它训练了一个能够编写快速 CUDA 内核的模型。而且不仅仅是正确的内核——而是真正经过优化的内核。 在简单/中等内核上，它的性能比 torch.compile 高出 2 倍；在复杂内核上，它的性能比 torch.compile 高出约 92%；即使在最难的设置下，它的性能也比 Claude Opus 4.5 和 Gemini 3 Pro 高出约 40%。 核心理念很简单，但却非常巧妙： CUDA 性能并非取决于正确性，而是取决于硬件。线程束、内存带宽、内存冲突——这些只有在性能分析器中才能看到的东西。 因此，他们不再奖励“是否编译成功”，而是奖励实际的 GPU 速度。真实的性能分析数据。强化学习直接基于性能进行训练。 这是一个很大的转变。 论文： [http://arxiv.org/abs/2602.24286](http://arxiv.org/abs/2602.24286) 项目： [https://cuda-agent.github.io](https://cuda-agent.github.io)

![图片](https://pbs.twimg.com/media/HCcICc5aMAApBbn?format=jpg&name=large)![图片](https://pbs.twimg.com/media/HCcH6O8akAA_Lj4?format=jpg&name=large)

* * *

### 热门回复

**@TGL** ♥ 20.9K · 💬 342

想随时了解 TGL 的最新动态吗？ 关注此帖，我们将为您提供所有即将到来的 TGL 比赛信息。

**@Jinjie Ni** ♥ 781 · 💬 49

生活近况：我加入了 @GoogleDeepMind 作为一名研究科学家 ，在 Yi Tay 的领导下 从事 双子座缩放和强化学习方面的工作 （ @YiTayML ）和 Quoc Le（ @quocleix ）。 我感到非常幸运能够站在通往通用人工智能的关键道路上，迫不及待地想要帮助推动这一领域的发展。

**@StepFun** ♥ 609 · 💬 20

“我们能拿到基础型号吗？” 当然。这里有两个。 “我们可以拿到代码吗？” 当然。这是 SteptronOSS。 “SFT 数据呢？” 即将推出。 最大限度的真诚，最小限度的障碍。 - 步骤 3.5 Flash Base — 预训练基础 - 步骤 3.5 Flash Base-Midtrain — 代码、代理和

**@Webflow** ♥ 15 · 💬 0

亨利·贝尔卡斯特用66秒讲述互联网的历史

**@Yongrui Su** ♥ 2 · 💬 0

这对于任何使用 CUDA 代理的人来说都非常重要。我很好奇，当你从规划器驱动代理时，瓶颈更常出现在内核启动开销还是内存传输上？我一直看到控制循环才是瓶颈所在。