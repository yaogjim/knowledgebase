---
title: "Inside Kaiju - building conversational models at scale"
source: "https://blog.character.ai/technical/inside-kaiju-building-conversational-models-at-scale/"
author:
  - "[[The Character.AI Team]]"
published: 2025-11-12
created: 2025-11-12
description: "What made Character.ai's early models so engaging? Before open-source models became the norm, our team built Kaiju - a family of in-house LLMs designed to power millions of fast, expressive conversations every day with an eye towards safety.Our latest blog post looks back at that foundational work."
tags:
  - "The Character.AI Team"
---
随着 Character.ai 团队转向基于 [开源模型](https://blog.character.ai/breaking-news-our-open-source-models-are-a-lot-of-fun/) 进行构建，我们希望分享一些我们原创研究的工作成果。毕竟，我们的创始人诺姆·沙泽尔正是 Transformer 架构的发明者！

Kaiju 是 Character.ai 自主研发的 LLM 系列模型，专为追求高速响应、强互动性与安全性而构建。

怪兽模型提供三种规模，融合了稠密 Transformer 架构与激进的效率优化技术，包括 int8 量化、多查询注意力机制、滑动窗口注意力以及跨层缓存共享。此前博客文章已提及部分技术（及更多内容）： [https://blog.character.ai/optimizing-ai-inference-at-character-ai/](https://blog.character.ai/optimizing-ai-inference-at-character-ai/) 与 [https://blog.character.ai/optimizing-ai-inference-at-character-ai-part-deux-2/](https://blog.character.ai/optimizing-ai-inference-at-character-ai-part-deux-2/) 。

若您是对打造下一代 Character.ai 模型感兴趣的工程师，并且这项工作让您心动，欢迎查看我们的 [开放职位](https://jobs.ashbyhq.com/character/?ref=blog.character.ai) ！

## Model Overview

Kaiju 模型家族包含 3 个生产版本： **小型（130 亿参数）** 、 **中型（340 亿参数）** 和 **大型（1100 亿参数）** 。

Kaiju 模型的核心设计理念聚焦于提升对话互动性与服务效率，而非追求学术基准测试成绩。

## 架构创新

所有 Kaiju 模型均采用基于 Transformer 的稠密自回归 LLMs 架构，并融入了多项独特的组件设计。

## 多头查询注意力（MQA）

Kaiju 高度依赖 [MQA](https://arxiv.org/pdf/1911.02150?ref=blog.character.ai) 来减少每个令牌的键值缓存大小，从而提升推理效率。由于对话推理任务中相邻轮次的输入令牌特征高度相似，这类工作负载通常能极大受益于键值缓存的命中率，而更小的单令牌键值缓存尺寸显著提升了系统性能。

MQA 已被证实会对某些 AGI 基准测试（如 MMLU）产生可量化的负面影响——这一结论既 [有公开文献记载](https://arxiv.org/pdf/2405.04434?ref=blog.character.ai) ，也经我们团队内部复现验证。由于我们并非为通用人工智能而优化模型，因此发现用微小的质量损失换取推理效率的大幅提升是完全值得的。

## 滑动窗口注意力

Kaiju 生产模型采用了 [滑动窗口](https://arxiv.org/pdf/2004.05150v2?ref=blog.character.ai) 注意力机制，这种机制降低了注意力计算所需的浮点运算次数，尤其在处理长上下文场景时效果显著。

所有 Character.ai 模型都采用滑动窗口与全局注意力层交替的结构。当前生产模型中的滑动注意力与全局注意力比例约为 6:1，滑动窗口长度为 1024 个标记。

在长文本处理中，简单的滑动窗口注意力机制会导致模型质量下降。而在内部实验中，采用 *交错式* 滑动窗口注意力机制时，"大海捞针"式的长文本检索质量几乎未见衰减。

同样值得注意的是，我们当前的滑动窗口注意力机制 *并未* 实现 [注意力汇聚机制。](https://arxiv.org/abs/2309.17453v1?ref=blog.character.ai)

## 跨层键值共享

除了 MQA 之外，Kaiju 模型在具有相同注意力机制的相邻层之间 [共享 KV 缓存](https://arxiv.org/pdf/2405.12981?ref=blog.character.ai) 。与 MQA 类似，这可以减少推理所需的 KV 缓存大小，并且不会导致模型准确性的显著下降。通常，2-3 层共享一个 KV 缓存。

## Int8

当前 Kaiju 系列模型将其参数和 KV 值以 int8 格式存储。在推理过程中，矩阵乘法运算采用 int8 精度执行。在多数现代加速器上，int8 矩阵乘法的浮点运算能力是 bf16 的两倍。

**注意：** Kaiju 模型目前均通过量化感知训练进行训练。采用 QAT 技术可使模型在保持 bf16 级别精度的同时，训练速度提升 20-30%。

## 其他创新成果

**预层归一化** ——Kaiju 模型采用预层归一化技术。这意味着模型在每个层的主要矩阵乘法运算之前，先对输入应用 RMSNorm 进行归一化处理，而非在层计算完成后再执行归一化。换言之，归一化操作发生在每层的起始阶段，而非结束阶段。

**动态钳位** \- 对激活值进行动态钳位有助于确保训练过程中的稳定性。模型会"学会"利用这种钳位，且在推理阶段仍需此操作。

![](https://blog.character.ai/content/images/size/w600/2025/11/data-src-image-ef29ca21-3d87-49a6-a733-88e531f80be0-1.png)

![](https://blog.character.ai/content/images/size/w600/2025/11/data-src-image-3739c4b0-75ba-4ad1-a93a-57f6330b608f.png)

![](https://blog.character.ai/content/images/size/w600/2025/11/data-src-image-c4c8808f-f950-4c77-8e34-b78acdc83cb7.png)

## Model Training

除了架构效率之外，Kaiju 的性能在很大程度上依赖于其训练技术栈。量化感知训练、低比特梯度通信和稳定性增强共同构成了 Kaiju 可扩展学习系统的基础。

Kaiju 模型完全在 GCP 集群的 H100 GPU 上通过模型并行技术进行训练，该技术包含节点内的张量与序列并行以及跨节点的 FSDP（全分片数据并行）。

## 量化感知训练

Kaiju 模型采用多种精度进行训练，以平衡模型质量与训练成本。

**Int8 -** 前向传播权重，键值缓存  
**Bf16** \- 激活值，局部梯度  
**Fp32** - 梯度累积，FSDP 主权重

梯度通信采用 Squinch 技术以 6 位精度实现。

## 梯度压缩（Squinch）

Squinch 是一种创新的分块梯度压缩算法，其核心目标是最小化梯度重建的期望对数误差。该算法将每 8 个梯度元素划分为一个数据块，并通过有限域上的对数均匀分布来建模梯度幅值的概率分布。

## 其他效率创新

**虚拟标量（Bungee）** ——为稳定 int8 训练，引入虚拟标量使模型能表达更广范围的激活值和梯度。该技术对小型模型尤为有效。

**三元权重更新** ——在训练小型 int8 模型时，若完整 int8 权重可容纳于节点内，权重可固定于节点上，类似 zero-2 方法。当 int8 权重更新幅度较小时，可传输 0、1 或-1 来代表每个权重，从而将权重广播压缩至 1.6 比特/参数。

## Data Strategy

Kaiju 模型基于优化的数据混合进行训练。数据混合目标分为两大类：

- **MMLU Max** - 这些数据混合旨在最大化“AGI 基准测试”的表现。
- **生产最大化** \- 这些数据组合旨在打造极具吸引力的模型。

通常，该方法涉及选择一个与待优化任务尽可能相似（例如通过 T5 嵌入计算相似度）的预训练数据组合。

Kaiju 模型基于网络规模的文本、代码和合成数据的广泛混合进行训练。每个变体根据其目标采用略有不同的平衡——例如，追求自然、高互动性的对话所需的数据输入，与为基准性能优化的模型截然不同。

在预训练接近尾声时，我们执行 **退火** 处理，对 MMLU Max 部分及其他指令数据进行调度安排。这一过程通过解锁模型在基准任务中的指令遵循能力和特定知识，有效提升了模型的最终性能。

## 安全与对齐

在部署前，Kaiju 模型需经历多阶段安全对齐流程，包括：

1. **监督式微调** 基于高质量（安全相关、指令遵循）数据
2. **强化学习** （基于用户滑动数据和反馈的在线 DPO 优化）
3. **Classifier training**

值得注意的是，Kaiju 模型配备了一个可选的额外分类器头部。该分类器头部是一个线性层，能够沿多个维度输出关于输入安全性的标记级指标。

虽然怪兽模型可与任何传统采样方法配合使用，但我们实现了分类器引导的束搜索，在推理时利用分类器结果来增强我们对标记的采样方式。

## 以安全为核心、可扩展的人工智能未来

Kaiju 证明，生产环境性能——而不仅仅是基准测试分数——能够且应当主导架构选择。诸如 int8 量化感知训练、多头注意力机制优化及键值共享等技术，共同将推理内存需求和成本降低了数个数量级，从而实现了大规模部署。

随着我们未来将重心放在开源 LLMs 上，我们将持续推动高效部署、动态互动对话以及稳健的安全与对齐性目标。

Character.ai 团队在交互式 AI 的前沿领域，专注于模型架构、安全对齐和生产基础设施的研发。如果您是热衷于为大规模、以人为本的机器学习系统贡献力量的工程师或研究人员，请点击 [**此处**](https://jobs.ashbyhq.com/character/?ref=blog.character.ai) 查看我们的职位招聘信息。我们期待您的加入！