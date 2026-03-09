---
title: "2026-03-09_Trevin_Peterson_Trevin_Peterson_构建了适用于_Apple_Silicon_MLX_的自动"
source: "https://x.com/TrevinPeterson/status/2030611877198221458"
author:
  - "[[@Trevin Peterson]]"
published: 2026-03-09
created: 2026-03-09
description:
tags:
  - "x"
  - "@Trevin Peterson"
  - "peterson"
  - "apple"
---

# Trevin Peterson 构建了适用于 Apple Silicon  MLX 的自动

**Trevin Peterson**

构建了适用于 Apple Silicon / MLX 的自动研究版本——可在 Mac 上原生运行，无需 PyTorch。循环实验发现，在 M4 Max 上，深度=4 优于深度=8，因为在 5 分钟的预算内，更多的优化器步数＞更多的参数。[http://github.com/trevin-creator/autoresearch-mlx…](http://github.com/trevin-creator/autoresearch-mlx)

[@karpathy](/karpathy)

[GitHub - trevin-creator/autoresearch-mlx: Apple Silicon (MLX) 移植自 Karpathy 的 autoresearch —...](https://t.co/BRvG6kLzuc)

* * *

### 热门回复

**@The Mighty** ♥ 6.6K · 💬 57

在罕见的公开问责时刻，一位权威的神经科医生告诉美国参议员，FDA 的拖延可能使患者失去本就不多的宝贵岁月。

**@Andrej Karpathy** ♥ 266 · 💬 4

太棒了!! 已添加到值得关注的分叉列表中

**@TradeZella** ♥ 170 · 💬 8

如果我能重启交易，我会遵循这些： 仅这一点本可以为我节省 14K 美元和 2 年的痛苦： 选择一个设置并交易100次，然后再进行判断。 2. 风险如此之小，以至于损失几乎感觉不到。在验证之后再进行评估，而非仅凭信心。 3. 给每笔交易评分 A、B 或

**@Yongrui Su** ♥ 2 · 💬 1

太赞了。在固定的实际时间预算下，深度与步骤的权衡是这里真正的关键。很好奇你有没有尝试过按阶段分配计算资源，比如先进行浅层搜索以找到有前景的差异，然后对排名靠前的几个进行更长时间的运行。另外，你是否会记录完整的补丁以及

**@Trevin Peterson** ♥ 4 · 💬 0

是的，循环自己就弄明白了，这一点很酷。 关于分阶段计算：一直在思考这个问题。难点在于，有些好想法起步慢，30秒时表现不佳，但到第4分钟时会反超。或许可以做软终止运行，即60秒后损失值仍未偏离初始值，让...