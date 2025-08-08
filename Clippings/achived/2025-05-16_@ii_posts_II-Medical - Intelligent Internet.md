---
title: "II-Medical - Intelligent Internet"
source: "https://ii.inc/web/blog/post/ii-medical"
author:
  - "[[@ii_posts]]"
published:
created: 2025-05-16
description: "* Model CardMedical AI continues to advance at a rapid pace - and our II-Medical-8B is a testament to just how far we’ve come. Despite its compact size, our new model outperforms systems over 10 times larger on key clinical reasoning benchmarks. Designed for precision, transparency, and real-world applicability, II-Medical-8B builds on our commitment to creating trustworthy AI for healthcare and education. With cutting-edge supervised fine-tuning (SFT) and reinforcement learning (RL) pipeline"
tags:
  - "clippings"
---
[

## II 的博客

](https://ii.inc/web/blog)![II-Medical](https://ii.inc/web/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fiipublic-alpha%2F2025%252F05%252FII-Medical-banner.jpg&w=3840&q=75)

- [模型卡](https://huggingface.co/Intelligent-Internet/II-Medical-8B?ref=ghost.ii.inc)

医疗人工智能继续快速发展，我们的 II-Medical-8B 就是我们取得巨大进步的证明。尽管体积小巧，但我们的新模型在关键临床推理基准测试中表现优于规模大 10 倍以上的系统。II-Medical-8B 专为精准、透明和实际适用性而设计，建立在我们为医疗保健和教育创建可靠人工智能的承诺之上。通过前沿的监督微调（SFT）和强化学习（RL）管道，它为复杂的医疗任务带来了强大的、循序渐进的推理能力，为开源医疗智能树立了新的标准。

医疗人工智能带来了独特的挑战：它需要结构化的、循序渐进的推理，基于现实世界临床知识的准确性，以及能够由专家审核的输出结果。II-Medical 的开发就是为了满足这些需求，重点在于决策支持、医学教育和安全的研究应用。

**零成本下的效率**

![](https://storage.googleapis.com/iipublic-alpha/2025%2F05%2FScreenshot%202025-05-15%20at%2012.00.35%20PM.png)

如 HealthBench 性能成本前沿所示，II-Medical-8B 在零推理成本下提供了强大的基准性能。它在效率和可及性方面均优于 GPT-4.5 和 o4-mini 等更大的模型。II-Medical-8B 也足够紧凑，可以在消费级硬件上本地运行，将医生级别的医学推理直接放在您的口袋里。这使临床医生、研究人员和个人无需昂贵的云基础设施即可使用高质量模型，为医疗人工智能开辟了一条快速、私密且经济实惠的前进道路。

**免责声明：** *II-医疗目前并非用于临床用途。它仅应用于研发目的。*

### 为什么专业医疗模型很重要

增强大语言模型（LLMs）的医学推理能力是一个重要且仍在进行的研究领域，这是由医学问题解决中固有的复杂性和特定领域挑战所驱动的。为应对这些挑战，已经开发了几种关键方法，特别是测试时扩展、监督微调、强化学习和知识图谱集成。

II-医疗整合了在近期研究中已被证明至关重要的方法：

- **测试时间缩放（推理 - 时间缩放）：** 在推理期间使用更大的计算预算来提升性能\[[2](https://arxiv.org/abs/2504.00869?ref=ghost.ii.inc)\]。
- **监督微调（SFT）：** 在精心策划的推理路径和详细解释上进行训练\[[2](https://arxiv.org/abs/2504.00869?ref=ghost.ii.inc)\]\[[3](https://arxiv.org/pdf/2412.18925?ref=ghost.ii.inc)\]\[[4](https://arxiv.org/abs/2504.00993?ref=ghost.ii.inc)\]。
- **强化学习（RL）：** 利用验证器反馈进行微调以提高逐步推理质量\[[3](https://arxiv.org/pdf/2412.18925?ref=ghost.ii.inc)\]。
- **知识图谱整合：** 用于 MedReason 中的结构化临床逻辑\[[4](https://arxiv.org/abs/2504.00993?ref=ghost.ii.inc)\]。
- **自我进化框架：** 像 MedS3 一样，结合树搜索和奖励塑造 \[[5](https://arxiv.org/abs/2501.12051v1?ref=ghost.ii.inc)\]。

各种模型和数据集支撑着这些方法：

- **华佗 GPT-o1** ：利用可验证的医疗问题以及结合的监督微调（SFT）和强化学习（RL）训练策略；性能优于通用模型和早期的医疗专用模型。
- **MedReason-8B** ：在 70 亿至 80 亿参数模型中树立了新的标准；通过知识图谱增强的思维链（CoT）解释，在复杂的临床基准测试中取得了领先成果。
- **M1** ：展示了推理时扩展的能力；即使在数据有限和模型规模较小的情况下也能提供强大的性能，可与大得多的专用系统相媲美。

这些创新方法和模型利用了专门的数据集和基准，包括 MedQA \[[6](https://arxiv.org/abs/2009.13081v1?ref=ghost.ii.inc)\]、PubMedQA \[[7](https://arxiv.org/abs/1909.06146?ref=ghost.ii.inc)\]和 MedReason 数据集 \[[4](https://arxiv.org/abs/2504.00993?ref=ghost.ii.inc)\]，以严格评估医学推理能力，强调了详细、透明的推理过程在推进医学人工智能系统方面的重要作用。

### II-医疗数据集设计

II-医学推理数据集包含 581,204 个样本，分为四个主要类别：

1. **公共推理数据集：** 来自以下来源的 103,031 个样本：
	1. [一般医学推理](https://huggingface.co/datasets/GeneralReasoning/GeneralThought-430K?ref=ghost.ii.inc) ：40,544 个样本
	2. [医学-R1-蒸馏数据（英文）](https://huggingface.co/datasets/FreedomIntelligence/Medical-R1-Distill-Data?ref=ghost.ii.inc) ：22,000 个样本
	3. [医学-R1-蒸馏数据（中文）](https://huggingface.co/datasets/FreedomIntelligence/Medical-R1-Distill-Data-Chinese?ref=ghost.ii.inc) ：17,000 个样本
	4. [UCSC-VLAA m23k-tokenized](https://huggingface.co/datasets/UCSC-VLAA/m23k-tokenized?ref=ghost.ii.inc) ：23,487 个样本
2. **通过 QwQ 增强的合成医学问答数据：** 来自 MedMCQA \[[9](https://arxiv.org/abs/2203.14371?ref=ghost.ii.inc)\]、MedQA \[[6](https://arxiv.org/abs/2009.13081v1?ref=ghost.ii.inc)\]和 MedReason \[[4](https://arxiv.org/abs/2504.00993?ref=ghost.ii.inc)\]的 225,700 个样本。
3. **精选推理痕迹：** 来自公共推理痕迹数据集的 338,055 个样本，使用 Qwen2.5 - 32B - Instruct 进行过滤\[12\]。

这个广泛的子集聚合了来自不同来源的公开可用的 R1 推理痕迹：

- [PrimeIntellect/合成-1](https://huggingface.co/collections/PrimeIntellect/synthetic-1-67a2c399cfdd6c9f7fae0c37?ref=ghost.ii.inc)
- [通用推理/通用思维-430K](https://huggingface.co/datasets/GeneralReasoning/GeneralThought-430K?ref=ghost.ii.inc)
- [a-m 团队/AM-DeepSeek-R1-蒸馏版-140 万](https://arxiv.org/abs/2503.19633v1?ref=ghost.ii.inc)
- [开放思想/开放思想2 - 100万](https://huggingface.co/datasets/open-thoughts/OpenThoughts2-1M?ref=ghost.ii.inc)
- [英伟达/羊驼-内莫 tron 训练后数据集](https://huggingface.co/datasets/nvidia/Llama-Nemotron-Post-Training-Dataset?ref=ghost.ii.inc) （科学子集）
- [认知计算/海豚-r1](https://huggingface.co/datasets/cognitivecomputations/dolphin-r1?ref=ghost.ii.inc) ， [ServiceNow 人工智能/R1-提炼-监督微调](https://huggingface.co/datasets/ServiceNow-AI/R1-Distill-SFT?ref=ghost.ii.inc) ，以及其他来源。

一个专门的管道确保与医疗领域相关：

- **嵌入生成** ：使用 [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2?ref=ghost.ii.inc) 模型。
- **聚类** ：使用 K 均值算法聚成 50,000 个簇。
- **领域分类** ：使用 [通义千问 2.5 - 32B - 指令版](https://huggingface.co/Qwen/Qwen2.5-32B-Instruct?ref=ghost.ii.inc) \[[12](https://arxiv.org/abs/2412.15115?ref=ghost.ii.inc)\] 根据医学或生物学内容对聚类进行分类，仅保留相关聚类。
1. **数学补充内容** ：15,000 个示例源自 Light-R1 \[[11](https://arxiv.org/abs/2503.10460?ref=ghost.ii.inc)\]。
	1. 包括在内以增强模型的一般推理能力。

**数据预处理：**

采用了严格的预处理技术来优化数据质量：

- **完整生成过滤** ：排除不完整或截断的推理痕迹。
- **长度过滤** ：仅保留提示词长度超过三个单词的样本。
- **等待令牌过滤** ：移除了包含超过 47 次“等待”出现次数的样本（高于第 97 百分位数阈值）。

**数据净化**

实施了一种两步去污方法：

1. **10 克去污** ：遵循 open-r1 方法以消除与评估数据集的重叠。
2. **模糊去污** ：在严格的 90%阈值下使用 s1 \[[13](https://arxiv.org/abs/2501.19393?ref=ghost.ii.inc)\] 方法，以进一步确保数据集的纯度。

这些细致的步骤确保与评估数据集的重叠最小，保持数据集的完整性和可靠性。

### RL 数据集

一个全面的数据集对于使用强化学习方法训练 II-Medical 至关重要，特别是由于强化学习中医疗推理的复杂性。认识到高质量、相关数据的必要性，我们进行了大量的过滤方法和实验运行来完善我们的数据集。最终，发现 MedReason 数据集\[[4](https://arxiv.org/abs/2504.00993?ref=ghost.ii.inc)\]由于其强大的结构以及与医疗应用中遇到的特定推理挑战的契合度，能够提供最佳性能，为我们模型的先进能力奠定了坚实基础。

原始的 MedReason 数据集包含基准数据样本，因此在训练前需要进行相同的净化处理，以防止数据泄露并确保对 II-医学推理数据集进行无偏评估。这种优化保持了数据质量和实验严谨性，以获得准确的性能指标。

### 模型训练概述

**监督微调（SFT）**

我们使用此配置在 SFT 数据集上对 [Qwen3-8B-Instruct](https://huggingface.co/Qwen/Qwen3-8B?ref=ghost.ii.inc) 模型进行了微调：

- 最大长度：16378
- 批量大小：32
- 学习率：5e-5
- 轮次数量：8
- 总令牌数/批次：16378 × 4

为了优化训练效率，我们采用了一种 **动态批处理策略** 。在每个批次中，我们积累样本，直到达到预定义的令牌限制，从而实现更好的 GPU 利用率和更快的训练。

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcfe7ObUMZdTFbHltrkWvUEKqZi-01sM-LPOM3Y6PJtq0vg78oiuubNVIsSJx3MfZkg8TBN_djAjbuV1JBGbjoNmOPzMdeKNsUtA2wsKx0llpaz4QwMoJ15yInbKBvpPAHWw1eMvg?key=YUFkXEKkeFnSddgZJQ7awA)

为了进一步提升推理能力，我们应用了 **DAPO（解耦剪辑与动态采样策略优化）** \[[8](https://arxiv.org/abs/2503.14476?ref=ghost.ii.inc)\] 算法，这是一种旨在应对长链推理特定挑战的先进强化学习方法。DAPO 引入了多项关键创新：

- **Clip-Higher** ：分别控制下限和上限裁剪边界，以促进探索并防止熵崩溃。
- **动态采样** ：过滤掉琐碎或过于简单的提示，以确保训练专注于有意义的学习信号。
- **令牌级策略梯度损失** ：通过为单个令牌分配更精确的信用来改进梯度更新，这在长回复中尤为重要。

奖励信号结合了多项选择题任务的自动评分以及使用基于大语言模型的评判系统（GPT-4o）进行的评估。

**过长奖励塑造** ：通过应用长度感知惩罚来减少过长生成中的噪声。

强化学习参数：

- 提示长度：2048个标记
- 响应长度：最多12288个标记 + 4096个缓冲区
- 剪辑比率：0.2（低），0.28（高）
- 批次大小：512（训练），1536（生成），32（小批次）
- 每个提示16代，温度：1.0，核采样概率：1.0，核采样数量：-1
- 学习率：1e - 6，热身：10 步，权重衰减：0.1
- 损失：标记均值，梯度裁剪：1.0，熵系数：0

奖励来自于：

- 自动多项选择题评分（带\\boxed{}标签）
- GPT-4o 对开放式任务的判断
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdeBfJgOu4K8ohydn2o13Iq2TvA7VMBzleNPfzvjXkhRBxOeeXbI5q0Tna7WH32uvnEQyRP5NspaOwE7b7lji_Uil2lmF1AbxBe3fuq5ia4UWkiwwqZ548O3mHHIC5bHbwuqIY5?key=YUFkXEKkeFnSddgZJQ7awA)

该图表显示了 250 个步骤中的平均评论家分数百分比。较高的初始分数表明，强化学习（RL）过程建立在经过充分优化的监督微调（SFT）模型之上，使 RL 能够有效地进一步优化和稳定性能。

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd6Gd7MPftEHeaxxtU-n0jRP1aGxzF_ZIFwxP7nNEeU9ODHvn8lOEhYJJUEZHPV8JMYe_QA-MBa6QVhMW-06pq4FC7ppRbBGWg0_g80h72I-gpuNTLPDczBVUqKdNO4VoxA9kL9BQ?key=YUFkXEKkeFnSddgZJQ7awA)

强化学习（RL）训练过程呈现出响应长度逐渐增加的趋势，这表明尽管存在一些波动，但模型在保持性能的同时正在学习生成更精细的输出。

**开放式任务**

实验结果表明，根据 GPT-4o 进行的评估，该模型在开放式答案任务上比在多项选择题任务上学习得更有效。然而，由于缺乏可靠的自动评估系统，实验仍然有限。目前的工作重点是扩大这项研究，并开发一个基于 GPT-4o 生成的数据训练的强大奖励模型。

### 基准评估

我们的 II-Medical-8B 模型在 [HealthBench](https://openai.com/index/healthbench/?ref=ghost.ii.inc) （一个评估大语言模型在医疗保健领域性能和安全性的开源基准测试）上也取得了 40%的分数。这一性能与 OpenAI 的 o1 推理模型以及 GPT-4.5（OpenAI 迄今为止最大、最先进的模型）相当。我们在下面提供了与 ChatGPT 中可用模型的比较。

![](https://storage.googleapis.com/iipublic-alpha/2025%2F05%2FScreenshot%202025-05-15%20at%2012.00.35%20PM.png)

为了保持透明度，我们已在此处发布了完整的 HealthBench 结果 [此处](https://huggingface.co/datasets/Intelligent-Internet/OpenAI-HealthBench-II-Medical-8B-GPT-4.1?ref=ghost.ii.inc) 。

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeQzGw9YKt84NOKjgniSzgoiInMDLASU1cijAgd8DtinUBlP-iRotN-7z_9D6mvSyz9_Y_YKQIxlohIyP45Q-KBiXp7XCCcQZW5zABKqdqyWhd_j1kWL23I5r1Z2EKIav-OmfnHBQ?key=YUFkXEKkeFnSddgZJQ7awA)

II-Medical 在十个领先的医学基准上进行了评估，包括 MedMCQA、MedQA、PubMedQA、MMLU-Pro、GPQA、《柳叶刀》问答、MedB-4、MedB-5、MedX、《医学期刊》（MEJM）

| Model | MedMC | MedQA | PubMed | MMLU-P | GPQA | Lan-cet | MedB-4 | MedB-5 | MedX | NEJM | Avg |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| II-医疗-8B | 71.57 | 87.82 | 78.2 | 80.46 | 67.18 | 70.38 | 78.25 | 72.07 | 25.26 | 73.13 | 70.49 |
| [华佗 GPT-o1-72B](https://huggingface.co/FreedomIntelligence/HuatuoGPT-o1-72B?ref=ghost.ii.inc) | 76.76 | 88.85 | 79.90 | 80.46 | 64.36 | 70.87 | 77.27 | 73.05 | 23.53 | 76.29 | 71.13 |
| [QwQ-32B](https://huggingface.co/Qwen/QwQ-32B?ref=ghost.ii.inc) | 69.73 | 87.03 | 88.5 | 79.86 | 69.17 | 71.3 | 72.07 | 69.01 | 24.98 | 75.12 | 70.68 |
| [华佗 GPT-o1-8B](http://freedomintelligence/HuatuoGPT-o1-8B?ref=ghost.ii.inc) | 63.97 | 74.78 | 80.10 | 63.71 | 55.38 | 64.32 | 58.44 | 51.95 | 15.79 | 64.84 | 59.32 |
| [MedReason-8B](https://huggingface.co/UCSC-VLAA/MedReason-8B?ref=ghost.ii.inc) | 61.67 | 71.87 | 77.4 | 64.1 | 50.51 | 59.7 | 60.06 | 54.22 | 22.87 | 66.8 | 59.92 |
| [M1-7B-23K](https://huggingface.co/UCSC-VLAA/m1-7B-23K?ref=ghost.ii.inc) | 62.54 | 75.81 | 75.80 | 65.86 | 53.08 | 62.62 | 63.64 | 59.74 | 19.59 | 64.34 | 60.3 |
| [文生 3-8B](https://huggingface.co/Qwen/Qwen3-8B?ref=ghost.ii.inc) | 66.53 | 81.38 | 73.9 | 77.85 | 64.87 | 66.26 | 68.83 | 62.66 | 19.59 | 69.65 | 65.15 |

II-医疗在 70 亿至 80 亿参数规模的模型中表现出色，超越了几个更大的模型，同时提供完全开源的可访问性。

### II-医疗入门

II-Medical 是我们将值得信赖的高性能人工智能引入医疗保健领域使命中的重要一步。无论您是研究人员、开发者、医疗保健专业人员还是教育工作者，我们都邀请您探索 II-Medical，并帮助我们推动医疗人工智能的前沿发展。

- 在 **vLLM** 上运行它：

vllm 服务 Intelligent-Internet/II-Medical-8B

- 在 **SGLang** 上运行它：

python -m sglang.launch\_server --model Intelligent-Internet/II-Medical-8B

**资源**

- 模型： [https://huggingface.co/Intelligent-Internet/II-Medical-8B](https://huggingface.co/Intelligent-Internet/II-Medical-8B?ref=ghost.ii.inc)

### 参考文献

*\[1\]* 智能互联网。(2025 年)。 *II-医疗-7B-预览版：医疗推理模型* 。

*\[2\]* 黄, X., 吴, J., 刘, H., 唐, X., & 周, Y. (2025). *m1：释放大语言模型中医疗推理的测试时缩放潜力*

*\[3\]* 陈, J., 蔡, Z., 季, K., 王, X., 刘, W., 王, R., 侯, J., & 王, B. (2024). *华佗 GPT-o1，迈向使用 LLMs 进行医学复杂推理。*

*\[4\] 吴, J., 邓, W., 李, X., 刘, S., 米, T., 彭, Y., 徐, Z., 刘, Y., 赵, H., 崔, C.-I., 曹, Y., 任, H., 李, X., 李, X., & 周, Y. (2025). MedReason：通过知识图谱引出大语言模型中的事实性医学推理步骤。*

*\[5\] 蒋，S.，廖，Y.，陈，Z.，张，Y.，王，Y.，& 王，Y.（2025 年）。MedS³：迈向具有自我进化慢思考能力的医学小语言模型。*

*\[6\] 金，D.，潘，E.，乌法托勒，N.，翁，W.-H.，方，H.，& 绍洛维茨，P.（2020 年）。这位患者患了什么病？一个来自医学考试的大规模开放域问答数据集。*

*\[7\] 金，Q.，丁格拉，B.，刘，Z.，科恩，W. W.，& 卢，X.（2019 年）。PubMedQA：一个用于生物医学研究问答的数据集。*

*\[8\] Yu, Q., Zhang, Z., Zhu, R., Yuan, Y., Zuo, X., Yue, Y., Fan, T., Liu, G., Liu, L., Liu, X., Lin, H., Lin, Z., Ma, B., Sheng, G., Tong, Y., Zhang, C., Zhang, M., Zhang, W., Zhu, H., Zhu, J., Chen, J., Chen, J., Wang, C., Yu, H., Dai, W., Song, Y., Wei, X., Zhou, H., Liu, J., Ma, W.-Y., Zhang, Y.-Q., Yan, L., Qiao, M., Wu, Y., & Wang, M. (2025). DAPO: An open-source LLM reinforcement learning system at scale.*

*\[9\] 帕尔，A.，乌马帕蒂，L. K.，& 桑卡拉斯布，M.（2022 年）。MedMCQA：一个用于医学领域问答的大规模多学科多项选择题数据集。*

*\[10\] 赵, H., 王, H., 彭, Y., 赵, S., 田, X., 陈, S., 季, Y., & 李, X. (2025). 用于赋能大语言模型训练的 140 万开源提炼推理数据集。*

*\[11\] 文, L., 蔡, Y., 肖, F., 何, X., 安, Q., 段, Z., 杜, Y., 刘, J., 唐, L., 吕, X., 邹, H., 邓, Y., 贾, S., & 张, X. (2025). Light-R1: 从零开始及超越的用于长思维链的课程监督微调、近端策略优化和强化学习*

*\[12\] Yang, A., Yang, B., Zhang, B., Hui, B., Zheng, B., Yu, B., Li, C., Liu, D., Huang, F., Wei, H., Lin, H., Yang, J., Tu, J., Zhang, J., Yang, J., Yang, J., Zhou, J., Lin, J., Dang, K., Lu, K., Bao, K., Yang, K., Yu, L., Li, M., Xue, M., Zhang, P., Zhu, Q., Men, R., Lin, R., Li, T., Xia, T., Ren, X., Ren, X., Fan, Y., Su, Y., Zhang, Y., Wan, Y., Liu, Y., Cui, Z., Zhang, Z., & Qiu, Z. (2024). Qwen2.5 technical report.*

*\[13\] 穆尼霍夫，N.，杨，Z.，施，W.，李，X. L.，李，F.-F.，哈吉希尔齐，H.，泽特勒莫耶，L.，梁，P.，坎德斯，E.，& 桥本，T.（2025 年）。s1：简单的测试时缩放。*