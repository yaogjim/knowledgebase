---
title: "On-Policy Distillation - Thinking Machines Lab"
source: "https://thinkingmachines.ai/blog/on-policy-distillation/"
author: ""
created: 2025-11-11 16:04:19
published: 2025-11-11 16:04:19
description: ""
tags: ""
---
ForgetStudyLearnfrommistakestrajectoriesblog postyour ownthe teacher’swellbestquickly

-   [Introduction](https://thinkingmachines.ai/blog/on-policy-distillation/#introduction)
-   [On-policy distillation — best of both worlds](https://thinkingmachines.ai/blog/on-policy-distillation/#on-policy-distillation--best-of-both-worlds)
-   [Implementation](https://thinkingmachines.ai/blog/on-policy-distillation/#implementation)
    -   [Loss function: reverse KL](https://thinkingmachines.ai/blog/on-policy-distillation/#loss-function-reverse-kl)
    -   [Illustration](https://thinkingmachines.ai/blog/on-policy-distillation/#illustration)
    -   [Pseudocode](https://thinkingmachines.ai/blog/on-policy-distillation/#pseudocode)
-   [Distillation for reasoning](https://thinkingmachines.ai/blog/on-policy-distillation/#distillation-for-reasoning)
    -   [Off-policy distillation](https://thinkingmachines.ai/blog/on-policy-distillation/#off-policy-distillation)
    -   [Reinforcement learning](https://thinkingmachines.ai/blog/on-policy-distillation/#reinforcement-learning)
    -   [On-policy distillation](https://thinkingmachines.ai/blog/on-policy-distillation/#on-policy-distillation)
-   [Distillation for personalization](https://thinkingmachines.ai/blog/on-policy-distillation/#distillation-for-personalization)
    -   [Training an internal assistant](https://thinkingmachines.ai/blog/on-policy-distillation/#training-an-internal-assistant)
    -   [Training on new knowledge degrades learned behavior](https://thinkingmachines.ai/blog/on-policy-distillation/#training-on-new-knowledge-degrades-learned-behavior)
    -   [On-policy distillation recovers post-training behavior](https://thinkingmachines.ai/blog/on-policy-distillation/#on-policy-distillation-recovers-post-training-behavior)
-   [Discussion](https://thinkingmachines.ai/blog/on-policy-distillation/#discussion)
    -   [Dense supervision greatly improves compute efficiency](https://thinkingmachines.ai/blog/on-policy-distillation/#dense-supervision-greatly-improves-compute-efficiency)
    -   [Distillation can effectively reuse training data for data efficiency](https://thinkingmachines.ai/blog/on-policy-distillation/#distillation-can-effectively-reuse-training-data-for-data-efficiency)
    -   [RL searches in the space of semantic strategies](https://thinkingmachines.ai/blog/on-policy-distillation/#rl-searches-in-the-space-of-semantic-strategies)
    -   [On-policy learning as a tool for continual learning](https://thinkingmachines.ai/blog/on-policy-distillation/#on-policy-learning-as-a-tool-for-continual-learning)
-   [Conclusion](https://thinkingmachines.ai/blog/on-policy-distillation/#conclusion)
-   [Citation](https://thinkingmachines.ai/blog/on-policy-distillation/#citation)

大型语言模型能够在特定领域展现出专家级表现，这得益于多种能力的叠加：输入感知、知识检索、方案选择以及可靠执行。这种能力需要依托一系列训练方法，我们可将其大致划分为三个阶段：

-   预训练教授通用能力，如语言运用、广泛推理和世界知识。
-   训练中期会融入领域知识，例如代码、医疗数据库或公司内部文件。
-   训练后引导出特定行为，例如遵循指令、解决数学问题或进行对话。

经过强化训练的小型模型在其专业领域内，往往能超越规模更大、功能更全面的通用模型。使用小型模型益处良多：出于隐私或安全考量，它们可部署于本地环境，便于持续训练与更新，同时还能节省推理成本。要充分利用这些优势，关键在于为训练后期阶段选择恰当的策略。

训练“学生”模型的后处理方法可分为两种：

-   在策略训练样本从学生模型本身展开，并赋予它们一定的奖励。
-   离策略训练依赖于学生学会模仿的外部来源的目标输出。

例如，我们可能希望训练一个紧凑模型来解决数学问题，例如：

 ![](https://thinkingmachines.ai/blog/on-policy-distillation/svgs/prompt.svg)

我们可以通过强化学习进行策略内训练，依据学生每次尝试是否能解决问题来评分。这种评分可由人工完成，也可由能可靠给出正确答案的“教师”模型执行。

 ![](https://thinkingmachines.ai/blog/on-policy-distillation/svgs/reinforcement-learning.svg)

策略蒸馏的优势在于，学生模型通过自身产生的样本进行训练，能以更直接的方式学会避免错误。但强化学习存在一个主要缺点：它提供的反馈极其稀疏，无论训练过程中使用了多少标记，每个训练周期只能传递固定比特数的信息。在我们上述示例中，学生模型仅能认识到“21”是错误答案，并据此调整不再生成已尝试的推演结果。但它无法精确识别错误发生的具体位置——究竟是运算顺序出错还是算术计算本身存在偏差。这种反馈的稀疏性使得强化学习在许多应用场景中效率低下。

离策略训练通常通过监督微调（SFT）进行：即在一套精心筛选的、针对特定任务的标注样本集上进行训练。这些标注样本的来源可以是一个已被证实在当前任务上表现优异的教师模型。

我们可以采用一种称为“蒸馏”的机制：训练学生模型以匹配教师模型的输出分布。我们基于教师轨迹进行训练：这包括生成标记的完整序列，其中涵盖中间思考步骤。我们可以使用教师模型在每个步骤的完整下一个标记分布（通常称为“对数蒸馏”），或仅对给定序列进行采样。实践中，采样序列能提供对教师分布的无偏估计，并达成相同目标。学生模型根据自身生成该标记的不可能性比例，对序列中的每个标记进行更新，如下例中较深颜色所示：

 ![](https://thinkingmachines.ai/blog/on-policy-distillation/svgs/off-policy-distillation.svg)

大型模型教师的知识蒸馏已被证明在训练小型模型遵循指令方面效果显著，羊驼：一款强大且可复现的指令遵循模型（Taori 等人，2021 年） 在数学和科学领域进行推理，《开放思维：推理模型的数据配方》（Guha 等人，2025 年） [提取临床信息](https://arxiv.org/html/2501.00031v1)大型语言模型蒸馏用于高效临床信息提取（Vedula 等人，2025 年）从医疗笔记中提取信息，并进行多轮对话交流。通过扩展高质量教学对话增强聊天语言模型（Ding 等人，2023）用于这些及其他应用的蒸馏数据集通常是开源并公开发布的。

离策略训练的弊端在于，学生是在教师经常遇到的情境中学习，而非其自身常处的情境。这可能导致误差累积：如果学生犯了教师从未犯过的早期错误，就会发现自己越来越偏离训练时观察到的状态。当我们关注学生在长序列上的表现时，这一问题尤为突出。为避免这种偏离，学生必须学会从自身错误中恢复。

在非策略蒸馏中观察到的另一个问题是，学生可能学会模仿教师的风格和自信，却未必掌握其事实准确性。模仿专有大型语言模型的虚假承诺（Gudibande 等人，2023）

学习国际象棋时，在线策略强化学习就如同无人指导的对弈。胜负反馈直接关联到你的棋局表现，但每局仅能获得一次结果反馈，且无法揭示哪些棋步对最终结果影响最大。而离线策略蒸馏则如同观摩大师对弈——你能观察到精妙的棋招，但这些招式出现的棋局态势，新手棋手往往难以企及。

我们希望将强化学习的策略相关性与蒸馏的密集奖励信号相结合。以学习国际象棋为例，这就像拥有一位能对你每一步走棋从“严重失误”到“精妙绝伦”进行评分的导师。而对于 LLM 的后训练阶段，这便是策略蒸馏法。

![](https://thinkingmachines.ai/blog/on-policy-distillation/images/chess.png)

chess.com 截图展示。每一步棋都由分析引擎进行色彩分级，标记为失误（红色）、错误（橙色）、不精确（黄色）或精妙（蓝色）。

## 策略蒸馏——集两者之长的完美融合[#](https://thinkingmachines.ai/blog/on-policy-distillation/#on-policy-distillation--best-of-both-worlds "Link to this section")

同策略蒸馏的核心思想是从学生模型中采样轨迹，并利用高性能的教师模型对每条轨迹中的每个标记进行评分。回到我们之前的数学示例，同策略蒸馏会对解题过程的每一步进行评分，惩罚导致学生得出错误答案的错误步骤，同时强化正确执行的步骤。

 ![](https://thinkingmachines.ai/blog/on-policy-distillation/svgs/on-policy-distillation.svg)

本文探讨了在线策略蒸馏在数学推理模型训练及融合领域知识与指令跟随的辅助模型训练等任务中的应用。我们针对已具备预训练及中期训练能力基础的模型实施在线策略蒸馏，发现这是一种成本低廉且效果显著的训练后优化方法，兼具在线策略训练的优势与密集奖励信号的特点。

| Method | Sampling | Reward signal |
| --- | --- | --- |
|   监督微调 | off-policy | **dense** |
|   强化学习 | **on-policy** | sparse |
|   同策略蒸馏 | **on-policy** | **dense** |

我们在策略蒸馏方面的工作借鉴了 DAGGER 的灵感，模仿学习与结构化预测简化为无遗憾在线学习（Ross 等人，2010 年）一种包含教师对学生访问状态评估的迭代监督微调算法，该过程也与奖励建模流程相似。逐步验证（莱特曼等人，2023）一种强化学习方法，该方法对学生在思维链中的每一步进行评分。我们扩展了 Agarwal 等人先前提出的在线策略蒸馏研究，语言模型的在线策略提炼：从自我生成的错误中学习（Agarwal 等人，2023 年） [Gu et al,](https://arxiv.org/abs/2306.08543)MiniLLM：大型语言模型的知识蒸馏（顾等人，2023 年） and [the Qwen3 team](https://arxiv.org/abs/2505.09388)Qwen3 技术报告（Qwen 团队，2025 年）借助 Tinker 训练 API，我们复现了 Qwen3 的成果：通过策略内蒸馏，在推理基准测试中以远低于强化学习的成本实现了同等性能。

## Implementation[#](https://thinkingmachines.ai/blog/on-policy-distillation/#implementation "Link to this section")

您可以在 Tinker 手册中跟随每个实现步骤进行操作。

### 损失函数：反向 KL 散度[#](https://thinkingmachines.ai/blog/on-policy-distillation/#loss-function-reverse-kl "Link to this section")

在策略蒸馏中，可采用多种损失函数来评估学生策略的轨迹表现。请参阅 Agarwal 等人的研究，以了解不同损失函数选择的分析。为简化起见，我们选择逐标记反向 KL 散度——即在相同先验轨迹条件下，学生模型（ πθ\\pi\_\\theta ）与教师模型（ πteacher\\pi\_\\text{teacher} ）对每个标记的分布差异：

KL(πθ∣∣πteacher)\=Ex∼πθ\[log⁡πθ(xt+1∣x1..t)−log⁡πteacher(xt+1∣x1..t)\]\\text{KL}\\Bigl(\\pi\_\\theta \\lvert\\rvert \\pi\_\\text{teacher}\\Bigr) = \\mathbb{E}\_{x \\sim {\\pi\_\\theta}} \\Bigl\[ \\log \\pi\_\\theta(x\_{t+1} | x\_{1..t}) - \\log \\pi\_\\text{teacher}(x\_{t+1} | x\_{1..t}) \\Bigr\]

我们的奖励函数旨在最小化反向 KL 散度，这促使学生模型在其所处的每个状态下都尽可能接近教师模型的行为。当学生与教师行为完全一致时，反向 KL 散度为零。为简化计算，我们采用零折扣因子：即在任意给定时间步，尽管从数学角度更为严谨，但我们发现实践中折扣因子大于零并未提升性能，因此为求简便，我们选择将其设为零。学生仅优化紧邻的下一个标记，而不考虑未来的标记。

反向 KL 散度与强化学习天然契合，后者通常优化由奖励模型诱导的序列级反向 KL 形式。然而与实践中大多数奖励模型不同，反向 KL 具有“不可篡改”的特性——从教师模型的视角来看，低 KL 值始终对应着高概率的理想行为。反向 KL 另外两个实用特性在于其“模式追寻”倾向。更多关于模式寻求行为的讨论，请参见 Eric Jang 的帖子。它学习的是特定行为（即教师的行为），而非将其分布分散于多个次优选项之中——这减少了暴露偏差。用于循环神经网络序列预测的预定采样（Bengio 等人，2015 年）。更多讨论请参阅 Gu 等人的研究。

此方法显著节省了计算资源。由于无需完成整个推演过程来采样计算奖励，我们可以在训练中使用更短或部分的推演。查询教师模型的概率对数仅需大型模型进行一次前向传播，而轨迹则由更小巧、成本更低的学生模型生成。

我们同样不需要独立的奖励或标注模型。将基于蒸馏的逐标记奖励与序列级环境奖励相结合可能具有优势，这是未来潜在研究的一个有趣方向。

### Illustration[#](https://thinkingmachines.ai/blog/on-policy-distillation/#illustration "Link to this section")

下面我们来看一个由教师评分的错误学生轨迹的真实案例。该案例取自 SimpleBench，关键在于模型需意识到问题前提的重要性：正确答案应为“B. 0”，因为冰块在煎锅中会融化。而学生Qwen3-4B-Instruct-2507错误地将其视为纯数学问题，完全没有考虑物理情境。

2025-10-24T22:10:41.375034 image/svg+xml Matplotlib v3.10.1, https://matplotlib.org/

由教师模型评分的示例轨迹。颜色越深的标记对应越高的反向 KL 散度。

较深的颜色代表那些受到教师模型Qwen3-235B-A22B-Instruct-2507较高惩罚的标记，该模型正确解决了此问题。可以看出，它对那些引导学生偏离正确方向的短语起始标记施加了惩罚，直观上对应着指导推理过程中关键的“分岔标记”。[Beyond the 80/20 Rule: High-Entropy Minority Tokens Drive Effective Reinforcement Learning for LLM Reasoning](https://arxiv.org/abs/2506.01939) (Wang et al, 2025)最终答案虽错，却未受惩罚——这完全是在整个先前序列条件下可预见的。

### Pseudocode[#](https://thinkingmachines.ai/blog/on-policy-distillation/#pseudocode "Link to this section")

我们在 Tinker 的强化学习脚本基础上实现了同策略蒸馏，该脚本已包含采样、奖励计算及策略梯度式训练功能。我们的实现实际上只需在使用 KL 正则化的强化学习实现基础上进行一行代码的修改：我们仅需替换正则化模型。

1.  初始化教师客户端。Tinker API 能够轻松为不同模型创建各类客户端，无需担忧模型引擎的利用率问题。我们采用采样客户端，因为无需通过教师模型传播对数概率。
2.  样本轨迹。我们按照强化学习中的方式从学生模型中采样轨迹。在采样过程中，强化学习算法已计算学生模型的对数概率 log⁡πθ(x)\\log \\pi\_\\theta(x) ，将其作为重要性采样损失的一部分使用。
3.  计算奖励。我们使用 `compute_logprobs` 对采样的轨迹向教师客户端发起查询，该查询返回教师对学生采样的令牌 xx 的对数概率 log⁡πteacher(x)\\log \\pi\_\\text{teacher}(x) 。在本文中，我们的所有实验均未考虑使用 logit（top-k）蒸馏技术，该技术本可进一步提升计算效率。我们随后利用这一结果来计算反向 KL 散度。
4.  使用强化学习进行训练。我们将每个标记的优势设定为负向逆向 KL 散度，并调用强化学习的重要性采样损失函数，以对学生模型执行训练更新。

```
# Initialize teacher client (main):
teacher_client = service_client.create_sampling_client(
    base_model=teacher_config.base_model,
    model_path=teacher_config.load_checkpoint_path,
)

# Sample trajectories (main):
trajectories = do_group_rollout(student_client, env_group_builder)
sampled_logprobs = trajectories.loss_fn_inputs["logprobs"]

# Compute reward (compute_teacher_reverse_kl):
teacher_logprobs = teacher_client.compute_logprobs(trajectories)
reverse_kl = sampled_logprobs - teacher_logprobs
trajectories["advantages"] = -reverse_kl

# Train with RL (train_step):
training_client.forward_backward(trajectories, loss_fn="importance_sampling")
```

在以下实验中，我们通常将策略蒸馏应用于已在特定领域知识上经过中期训练的模型。这种训练增加了学生模型在教师分布范围内生成标记的概率，尽管这通常远不足以复制教师的性能。SFT 采用前向 KL 方法，新增了对新词元的支持。随后，反向 KL 方法可在初始支持的范围内进行模式搜寻。正如我们将在个性化示例中看到的，由于学生缺乏相关领域知识，生成相关标记的概率通常从零开始。

我们采用在线策略蒸馏进行后训练，并将其与专家模型训练最后关键阶段的其他方法进行比较。

## 用于推理的蒸馏[#](https://thinkingmachines.ai/blog/on-policy-distillation/#distillation-for-reasoning "Link to this section")

我们采用蒸馏技术训练 Qwen3-8B-Base 模型的数学推理能力，以 Qwen3-32B 作为教师模型。教师模型（Qwen3-32B）与学生模型（Qwen3-8B-Base）均为 Tinker 平台当前支持的模型，因此您可以通过 Tinker 操作指南复现我们的实验。

###   离策略蒸馏[#](https://thinkingmachines.ai/blog/on-policy-distillation/#off-policy-distillation "Link to this section")

如上所述，我们所有实验均以离线蒸馏形式的中期训练为起点——即在教师模型生成的示例数据集上进行监督微调。用于数学推理的数据集为 OpenThoughts-3，该数据集包含由 QwQ-32B（类似 Qwen3-32B 的推理模型）生成的推理提示与对应回答。

对 Qwen3-8B-Base 模型进行 40 万条提示词的全面微调后，在数学问题基准测试 AIME'24 中达到了 60%的得分。我们亦可采用 LoRA 进行训练，LoRA：大型语言模型的低秩自适应（Hu 等人，2021 年）尽管在处理大规模数据集时，其表现仍落后于全面微调。在所有情况下，我们观察到性能呈对数线性提升——初期的性能提升成本较低，而后期的提升则代价高昂。

2025-10-26T05:38:33.849913 image/svg+xml Matplotlib v3.10.1, https://matplotlib.org/

AIME'24 在离线策略蒸馏（SFT）过程中的得分表现。在最初的 5 万至 10 万次提示后，性能遵循可预测的对数线性扩展曲线。正如《无遗憾的 LoRA》中所预测，我们观察到当采用大批次规模进行大规模 SFT 时，LoRA 性能会有所下降。

我们可以将基于 40 万条提示微调后的模型视为一个检查点，在尝试各种后训练方法以提升其性能之前使用。我们可以比较将 AIME’24 基准测试得分从 60%提升至 70%所需投入的工作量。

默认方法是基于更多提示进行微调，延续离策略蒸馏的过程。通过外推对数线性趋势，我们估计该模型在大约 200 万条提示时能达到 AIME’24 测试 70%的准确率。这一外推需要规模定律持续有效而不出现停滞，这并非易事。然而，已有大规模离策略蒸馏提升 80 亿参数模型性能超过 70%的实例，例如 OpenThoughts-3 和DeepSeek-R1-0528-Qwen3-8B模型。DeepSeek-R1-0528-Qwen3-8B在基准测试中达到了 86%的准确率，其训练提示词数量未具体说明。较早期模型（Qwen2.5-7B、Qwen2.5-14B）在使用 DeepSeek-R1 提供的 80 万条蒸馏提示词训练后，分别实现了 55.5%和 69.7%的性能表现。我们可以将这一推断作为对离线策略蒸馏成本效益比的乐观估计。

###   强化学习[#](https://thinkingmachines.ai/blog/on-policy-distillation/#reinforcement-learning "Link to this section")

Qwen3 技术报告显示，在相似 SFT 初始化基础上，经过 17,920 GPU 小时的强化学习训练，该模型在基准测试中达到了 67.6%的性能。虽然难以直接与蒸馏成本进行对比，但基于对 SFT 训练栈的合理假设，这一成本相当于处理 200 万条离线策略蒸馏提示的训练开销。

| Method | AIME’24 | GPQA-Diamond | GPU Hours |
| --- | --- | --- | --- |
|   离策略蒸馏 | 55.0% | 55.6% | Unreported |
| \+ 强化学习 | 67.6% | 61.3% | 17,920 |
|   **\+ 在线策略蒸馏** | **74.4%** | **63.3%** | **1,800** |

出自 Qwen3 技术报告，表 21。

Qwen 团队还报告称，通过策略蒸馏技术，在 AIME’24 上以仅十分之一的强化学习成本取得了 74.4 分的更高成绩，这为我们的研究提供了灵感。我们将在基础配置中尝试复现这一成果。

###   同策略蒸馏[#](https://thinkingmachines.ai/blog/on-policy-distillation/#on-policy-distillation "Link to this section")

作为离线策略蒸馏或强化学习的替代方案，我们采用了上述的在线策略蒸馏方法。实际上，我们选用 Qwen3-8B 作为教师模型，因其表现略胜一筹。但出于计算量对比的目的，我们仍可测算 32B 模型的浮点运算次数。从 40 万步的 SFT 检查点出发，策略内蒸馏在大约 150 步内实现了 70%的 AIME’24 得分。150 步大约对应 7.7 万条提示；我们按每条提示 4 个样本进行训练。

2025-10-26T06:25:04.994156 image/svg+xml Matplotlib v3.10.1, https://matplotlib.org/

在策略蒸馏过程中，AIME'24 项目通过训练浮点运算次数来衡量额外计算量（详见下文）。相较于监督微调，策略蒸馏的计算效率显著更高，尤其对于 LoRA 模型而言。当秩为 32 时，LoRA 模型在监督微调后落后全参数微调 13%，但在策略蒸馏后仅落后 6%。

比较不同方法的计算成本并非易事，因为训练、采样与对数概率计算之间的成本比例会因实现方式而有显著差异。下文我们将以浮点运算次数（FLOPs）为单位进行成本估算，这种计算方式会对能有效在 GPU 上并行化的方法产生不利影响。特别是，它会高估实际计算对数概率的成本。

| Method | AIME’24 | Teacher FLOPs | Student FLOPs | CE vs SFT-2M |
| --- | --- | --- | --- | --- |
|   *初始化：SFT-400K* | 60% | 8.5 × 1020 |   3.8 乘以 10 的 0 次方 | – |
|   SFT-2M（外推值） | ~70% (extrapolated) |   3.4 乘以 10 的 0 次方 |   1.5 乘以 10 的 0 次方 | 1× |
|   强化学习 | 68% | \- | \- | ≈1× |
|   同策略蒸馏 | 70% |   8.4 乘以 10 的 0 次方 |   8.2 乘以 10 的 0 次方 | **9-30×** |

我们发现，当提供 SFT 数据集时（如我们使用 OpenThoughts-3 的示例），或将其成本分摊到多次训练中，基准成本可降低 9 倍。CE = (学生 + 教师) / (学生)在此情况下，我们不计入教师模型 FLOPs 在离线策略训练中的成本，但会计入在线策略训练的成本，因为必须运行教师模型来计算学生轨迹的对数概率。由于这项计算可轻松跨 GPU 并行处理，GPU 时长的成本降低幅度接近 18 倍。

然而，我们常常需要针对新任务训练一个小型模型，而该任务并无现成的离线蒸馏数据集可用。若将教师模型在离线蒸馏中的全部成本——即包括从教师模型采样的额外成本——纳入考量，总成本降低约为 30 倍。CE = （学生 + 教师）/（学生 + 教师）

## 个性化蒸馏[#](https://thinkingmachines.ai/blog/on-policy-distillation/#distillation-for-personalization "Link to this section")

除了在常见任务上训练小模型以达到高性能外，蒸馏技术的另一应用场景是个性化定制。例如，在对话中保持特定语气与输出格式，或实现工具使用、成本预算等能力。我们通常希望将这类行为训练与新的领域知识相结合。

同时进行训练通常较为困难，而轻量级的微调往往不足以达成此目标，陌生微调样本控制语言模型如何产生幻觉（Kang 等人，2024）因此需要更大的中期训练。在掌握新知识的基础上学习训练后行为，需要一个复杂的后训练技术栈，通常包含专有数据和奖励模型。尽管这种方法对前沿实验室而言是可实现的，但对其他实践者来说，复制这一过程可能困难重重或成本高昂至难以承受。

在本节中，我们将展示如何有效运用同策略蒸馏技术来对特定行为进行后训练。该方法同样适用于持续学习或“测试时训练”：即在模型部署期间进行更新，同时不降低其基础性能。我们以公司内部文档进行中期训练的模型为例进行说明。

### 训练内部助手[#](https://thinkingmachines.ai/blog/on-policy-distillation/#training-an-internal-assistant "Link to this section")

定制模型的一个常见目标是扮演助手角色：既要在某一领域具备专家知识，又要展现出可靠的助手般行为。我们可能需要对这两方面分别进行训练，特别是当专业领域无法仅通过预训练数据掌握，或是专业知识学习会干扰行为模式时。

我们的示例是一个公司内部助手，我们对其有两个期望：

1.  该模型具备领域（公司文件）相关知识。预训练模型未曾接触过公司的任何内部文件，因此无论模型规模大小，都只能进行推测。我们将通过内部知识召回评估（“内部问答”）来衡量这一点。
2.  该模型展现出强大的训练后行为，即指令遵循能力。我们将通过常用的 IF-eval 指标对此进行衡量。大型语言模型的指令遵循评估（Zhou 等，2023）

### 学习新知识会削弱已习得行为[#](https://thinkingmachines.ai/blog/on-policy-distillation/#training-on-new-knowledge-degrades-learned-behavior "Link to this section")

我们将从 Qwen3-8B 而非基础模型开始。Qwen3-8B 经过针对助手实用技能的后训练，例如指令遵循和强化学习推理。先前研究表明，此类强化学习仅训练原始模型中的小型子网络，强化学习微调大型语言模型中的小型子网络（Mukherjee 等人，2025 年）因此，当网络在大量数据上进一步训练时，其表现可能变得脆弱。我们探究了这种情况发生的程度，以及如何恢复期望的行为。

为减少此类灾难性遗忘，训练中期的一种常见做法是混入来自原始模型预训练分布的“背景数据”。中期训练桥接预训练与后训练分布（刘等人，2025 年）在此情况下，我们无法获取 Qwen3 的预训练分布。因此，我们考虑采用一个更强大但成本更高的基线方法：选用 Tulu3。Tulu 3：开拓开放语言模型后训练新前沿（Ivison 等人，2024）提示语——一个广泛的聊天和指令遵循数据集——通过 Qwen3-8B 模型进行重新采样，以充当聊天背景数据。

由 Qwen3-8B 采样的这种“同策略”背景数据充当了前向 KL 正则化器，在中期训练过程中强化了模型的原始行为。我们发现，在中期训练期间为保持对话能力，采用 Qwen3-8B 采样优于 Qwen3-32B，这凸显了数据源的敏感性；类似同策略 SFT 的结果在 Chen 等人的研究中亦有发现。在实践中保持：策略内数据在缓解遗忘中的作用（陈等人，2025 年）我们假设这种方法可能比直接获取原始预训练数据分布更为有效，但代价是需要对大规模数据集进行采样。

随后，我们在内部文档与对话数据的不同混合比例上对 Qwen3-8B 进行微调。增加文档数据的占比能直接提升模型的知识储备。然而，尽管混入至少 30%的对话数据有助于保留大部分指令遵循能力，但任何配比都无法在 IF-eval 评估中维持原始性能水平。即便 SFT 数据集包含 100%的对话数据，情况依然如此。我们将在关于持续学习的讨论中进一步探讨这一点。

2025-10-26T06:57:03.021695 image/svg+xml Matplotlib v3.10.1, https://matplotlib.org/

在内部文档比例上的全面审视：中期训练期间的背景聊天数据。尽管混入少量聊天数据有助于防止灾难性回归，但没有任何权重能保持原有的 IF 评估性能。

对于任何给定的混合情况，我们观察到在微调过程中 IF 评估性能有所下降。这削弱了我们通过延长训练时间来进一步优化模型的能力。从方向上看，我们或许期望一个在特定数据集上训练的过参数化模型，仅在该数据集背景下调整其行为，而不影响其他情境下的表现。然而，实践中我们并未观察到这一现象，因为对原始文档数据的训练甚至会导致问答场景下的性能退化。

2025-10-26T07:30:12.322163 image/svg+xml Matplotlib v3.10.1, https://matplotlib.org/

在所有数据混合情况下，IF 评估值在训练中期均出现下降。当我们采用线性学习率（如图所示）时，随着学习率的衰减，这种下降最终会趋于平缓并开始缓慢回升。然而，性能始终未能完全恢复。

一种常用的替代方法是使用 LoRA 来约束参数更新，从而降低灾难性遗忘的可能性。然而，这种方法在保持 IF 评估能力方面仍显不足，且 LoRA 学习到的内容较少。LoRA 学习更少，遗忘更少（Biderman 等人，2024 年）

2025-10-26T07:44:43.009994 image/svg+xml Matplotlib v3.10.1, https://matplotlib.org/

在基于后训练 Qwen3-8B 模型进行个性化中期训练时，LoRA 学习到的知识较少，且仍会遗忘其原有的后训练行为。

### 策略蒸馏恢复训练后行为[#](https://thinkingmachines.ai/blog/on-policy-distillation/#on-policy-distillation-recovers-post-training-behavior "Link to this section")

接下来，我们旨在完成对内部文档的微调后，恢复模型的指令遵循能力。该能力最初通过强化学习训练而成，成本高昂且如我们所见具有不稳定性。为此，我们改用策略蒸馏方法，以早期版本的模型 Qwen3-8B 作为教师模型，在 Tulu3 提示集上进行训练。需注意的是，此阶段训练与内部文档数据无关，其设计初衷纯粹是为了重建指令遵循功能。

采用早期版本模型作为教师模型，以“重新唤醒”在微调过程中丧失的能力，使得同策略蒸馏在持续学习领域展现出巨大潜力。我们可以交替进行新数据微调与行为恢复的蒸馏阶段，从而使模型能够不断学习并保持知识更新。这种阶段交替的方法此前已由 Cobbe 等人进行过探索。阶段性策略梯度（Cobbe 等人，2020 年）

在采用内部文档数据与聊天数据以 70 比 30 的比例进行微调后，策略蒸馏技术几乎完全恢复了 IF-eval 评估中的性能，且未损失任何知识；我们还观察到聊天能力与模型在内部问答评估中的“知识”表现之间存在一定的正向迁移效应。

| Model | 内部质量评估（知识） | IF-eval (Chat) |
| --- | --- | --- |
| *Qwen3-8B* | 18% | **85%** |
| *\+ midtrain (100%)* | **43%** | 45% |
| \+ midtrain (70%) | 36% | 79% |
| \+ 训练中期（70%）+ 蒸馏 | **41%** | **83%** |

领域特定（内部质量评估）与对话（IF 评估）在中期训练后的表现。尽管中期训练使 Qwen3-8B 遗忘了后训练阶段习得的行为，但通过策略内蒸馏可低成本恢复这些行为，同时保留中期训练中获得的新知识。

本质上，我们将语言模型本身视为奖励模型，对高概率行为予以奖励。直接偏好优化：你的语言模型实为奖励模型（Rafailov 等人，2023 年）这与逆强化学习相关：高概率行为对应于假设的潜在偏好模型中的有利奖励。逆向强化学习算法（Ng 与 Russell，2000）任何经过指令调优的开放权重模型在此意义上均可作为奖励模型使用；我们仅需调用其 `compute_logprobs` 函数即可。

蒸馏作为整合行为与知识的工具，已在混合推理模型（如 Qwen3）及专家蒸馏领域得到探索。DeepSeek-V3.2-Exp：借助 DeepSeek 稀疏注意力提升长上下文处理效率（DeepSeek-AI 团队，2025 年）我们与陈等人的研究结果均表明，在策略学习可成为增强类似基于蒸馏的“模型融合”方案的关键工具。

## Discussion[#](https://thinkingmachines.ai/blog/on-policy-distillation/#discussion "Link to this section")

### 密集监督显著提高了计算效率[#](https://thinkingmachines.ai/blog/on-policy-distillation/#dense-supervision-greatly-improves-compute-efficiency "Link to this section")

强化学习与在线策略蒸馏均通过反向 KL 散度进行学习，对基础策略中的行动空间进行剪枝。差异在于奖励的密集程度。在《无遗憾的 LoRA》中，我们从信息论角度提出：强化学习每回合仅传授 O(1)O(1) 比特信息。相比之下，蒸馏每回合传授 O(N)O(N) 比特信息，其中 NN 为标记数量。我们能否通过更密集的奖励来量化所提升的训练效率？

我们进行了一项实验，旨在对两者进行直接比较：

1.  从 Qwen3-8B-Base 开始（无需额外 SFT）。
2.  在 DeepMath 上运行强化学习，遵循我们在《LoRA Without Regret》中的流程。我们采用 128 的 LoRA 秩。所得模型将作为蒸馏教学的教师模型。
3.  从强化学习训练模型（2）向基础模型（1）进行同策略蒸馏。

2025-10-26T08:48:38.017170 image/svg+xml Matplotlib v3.10.1, https://matplotlib.org/

从相同的初始状态出发，策略蒸馏技术仅需约 7-10 倍更少的梯度步数即可习得经过强化学习训练的策略，相当于实现了 50-100 倍的计算效率提升。

我们观察到，蒸馏方法以约 7-10 倍的速度达到了与教师模型相当的性能水平，且模型架构保持一致（LoRA 秩为 128）。反向 KL 散度在不到 10 次梯度步骤内降至接近零，AIME 分数也得以恢复，而强化学习则需要 70 步才能达到同等水平。

总的来说，所需计算量的减少幅度约为 50 到 100 倍：

-   虽然强化学习需要在接近评估上下文长度的情况下进行训练（以便策略学会上下文限制并避免格式惩罚），但蒸馏学习在较短的上下文长度下也能取得不错的效果，因为已完成采样的轨迹与继续采样的轨迹之间并不存在明显的奖励断崖。
-   当 SFT 初始化足够强大时，例如：当教师策略处于学生策略的支持范围内时。若情况并非如此，比如在“推理蒸馏”中，我们需要显著增大批次规模。策略蒸馏方法在较小批量大小下依然高效，因为它每回合提供的信息量显著增多，从而降低了梯度噪声。

尽管通常难以通过过程监督来训练强化学习模型，但这些结果表明，作为一个宏观方向，过程监督与密集奖励机制有望将学习效率提升一个数量级。这一发现与莱特曼等人早先在强化学习研究中取得的成果相吻合。

### 蒸馏法能有效复用训练数据，提升数据利用效率[#](https://thinkingmachines.ai/blog/on-policy-distillation/#distillation-can-effectively-reuse-training-data-for-data-efficiency "Link to this section")

对实践者而言，收集大量训练提示数据集既困难又耗时。因此，我们希望能在训练中多次复用提示内容。然而在强化学习中，对同一提示进行多轮训练往往会导致模型简单记忆最终答案，这一现象在大型模型中尤为明显。（Wang 等人，2025 年）在《基于单一训练样本的大语言模型推理强化学习》中展示了积极成果，但仅限于特定场景。相比之下，策略蒸馏通过最小化反向 KL 散度来学习逼近教师的完整分布，而非仅记忆单一答案。这使得我们能够基于同一提示训练多个样本。

我们在数学领域上重复了训练 Qwen3-8B-Base 的上述实验，但这次仅使用数据集中随机选取的一个提示。求极限： lim⁡x→∞x(x+13−x−13)\\lim\_{x \\to \\infty} \\sqrt{x} \\left( \\sqrt\[3\]{x+1} - \\sqrt\[3\]{x-1} \\right)

我们在此提示上连续训练 20 步，每步使用 256 次模拟运行批次，共计 5120 条分级序列。我们采用顺序方式对同一提示进行多步训练，这通常会导致过拟合。尽管这种方法计算效率自然较低，但仅基于单一提示训练后，我们仍能大致达到教师模型的性能水平。

2025-10-26T08:48:38.488241 image/svg+xml Matplotlib v3.10.1, https://matplotlib.org/

在此示例中，基于单个训练样本进行多轮训练足以提炼出教师模型在 AIME'24 中的表现。我们的默认配置（亦用于个性化实验）采用同策略蒸馏法，每批次处理 64 个提示，每个提示生成 4 个样本。所示所有方法均以每批次 256 个样本进行训练。需注意右侧图表展示的是训练 KL 散度，因此总体 1 个提示的表现优于每批次 1 个提示是正常现象。

### 强化学习在语义策略空间中进行搜索[#](https://thinkingmachines.ai/blog/on-policy-distillation/#rl-searches-in-the-space-of-semantic-strategies "Link to this section")

我们已观察到，策略蒸馏能够以远少于强化学习的训练步数复制其学习成果。对此结果的一种解读是，与预训练不同，强化学习并未在梯度更新步骤本身消耗大量算力。我们应当将强化学习视为将大部分算力用于搜索——即策略推演与功劳分配——而非参数更新。来自《苦涩的教训》（里奇·萨顿）：“突破性进展最终往往源于一种相反的方法，即通过搜索和学习来扩展计算能力。”

通过随机梯度下降进行的预训练正在探索高维参数空间。预训练需要海量信息且难以提炼，部分原因在于每个网络的参数空间都具有一定独特性。“彩票假说：寻找稀疏、可训练的神经网络”（Frankle 与 Carbin，2018 年）预训练所需的梯度步骤计算成本极高且耗时漫长。

相反，我们应将强化学习视为探索语义策略空间的过程。需要注意的是，对策略的探索与对结果的探索存在微妙差异；强化学习要求基础模型具备一定的初始成功率才能启动，这意味着它已经“找到了结果”，但在强化学习过程中可以不断优化策略，以提高成功结果的出现概率。在每一步中，强化学习都会尝试对过去发现的策略进行微小调整。它并非在参数空间中探索，而是通过运气“偶然”发现新策略——从已有权重集合中随机采样。

一旦找到优秀策略，蒸馏便成为学习该策略的捷径：在线策略蒸馏无需对强化学习课程中的中间策略进行建模，而只需关注最终习得的策略。如果我们仅对最终策略感兴趣（这在生产用例中十分常见），便无需耗费算力对所有中间策略进行建模。

打个比方：在科学研究中，我们花费大量时间和资源寻找答案、探索新思路。一旦发现成果，用自然语言表达出来传授给他人就会简单得多。这可以对比像体育运动这样的直觉性技能，由于这类知识存在于只有我们自身能直接理解的先天语言（如肌肉记忆）中，传授给他人要困难得多。体育技能只能通过反复练习来掌握。

### 作为持续学习工具的策略上学习[#](https://thinkingmachines.ai/blog/on-policy-distillation/#on-policy-learning-as-a-tool-for-continual-learning "Link to this section")

在个性化蒸馏部分，我们探讨了策略上蒸馏技术将专门训练的行为重新引入模型的能力。这一方法可推广至更广泛的持续学习任务范畴，这些任务要求在不削弱已有能力的前提下获取新知识。

先前的研究发现，在线策略学习（强化学习）比离线策略学习遗忘更少。《强化学习的剃刀：为何在线强化学习遗忘更少》（申菲尔德等人，2025 年）然而，强化学习仅能塑造行为——它无法很好地传授新知识，因此不足以实现持续学习。

在上一节中，我们看到监督微调（包括离策略蒸馏）由于会降低模型表现，因此无法支撑持续学习。我们将更深入地研究这一问题，并通过具体实例加以说明。与上文类似，我们通过提取 Tulu3 提示词并采样 Qwen3-32B 在 `temperature = 1.0` 温度下的输出构建数据集，且不作进一步修改。因此该数据集与 Qwen3-32B 的 KL 散度为零。在我们之前的文章《击败 LLM 推理中的非确定性》中，也探讨了“真正同策略”KL=0 数据的重要性。

当我们对模型自身样本的数据集进行监督微调时会发生什么？我们发现，任何大于零的实际学习率都会导致指令遵循评估的性能下降！

2025-10-26T08:56:17.792340 image/svg+xml Matplotlib v3.10.1, https://matplotlib.org/

在 Qwen3-32B 自身样本上运行 SFT 会导致性能下降。我们采用了与个性化部分相同的学习率，该学习率是基于实际性能考量进行扫描确定的。线性学习率虽能防止前向 KL 散度/IF 评估无限回退，但在学习率衰减至零前无法恢复原有性能。

对此的一种可能解释是，虽然 KL 散度在期望值上为零，但实践中每个有限批次都会呈现出略微不同的分布。基于这些有限批次进行训练会导致非零梯度更新，从而使更新后模型的策略偏离其原始状态。随着时间的推移，这一过程使得对自身样本的训练逐渐转变为异策略训练，进而导致与异策略训练相同的误差累积和长序列发散问题。

同策略蒸馏始终保持同策略性，且由于教师模型固定不变，学生模型能够稳定收敛至教师模型的理想行为，不会像监督微调那样在自我蒸馏场景中出现性能衰退。这使得同策略蒸馏成为持续学习中极具前景的工具。

## Conclusion[#](https://thinkingmachines.ai/blog/on-policy-distillation/#conclusion "Link to this section")

我们已探索了策略上蒸馏在数学推理小模型训练及持续学习助手等场景中的应用。通过将策略上蒸馏与另外两种后训练方法——策略外蒸馏和策略上强化学习进行对比，发现策略上蒸馏兼具两者优势：既保持了策略训练稳定可靠的性能，又获得了密集奖励信号带来的成本效益。

后训练是实现前沿模型能力的关键环节。通过采用学生模型的策略上采样与教师模型的密集监督相结合，策略蒸馏方案能够以远低于前沿高计算量强化学习训练的成本，达成同等能力水平。

我们的实现可在 Tinker 实践手册中找到。本研究探索了策略蒸馏的简洁直观实现方式，以清晰展现其优势。我们期望继续深入研究蒸馏技术的新应用场景、提升教师监督效能的新方法，以及提高数据利用效率与持续学习能力的途径。

在 Thinking Machines，我们的使命是借助集前沿性能、适应性与个性化于一体的 AI 模型，赋予人们力量。策略内蒸馏正是实现这一目标的有力工具。

## Citation[#](https://thinkingmachines.ai/blog/on-policy-distillation/#citation "Link to this section")

请引用本作品为：

```
Lu, Kevin and Thinking Machines Lab, "On-Policy Distillation",
Thinking Machines Lab: Connectionism, Oct 2025.
```

或使用 BibTeX 引用格式：

```
@article{lu2025onpolicydistillation,
  author = {Kevin Lu and Thinking Machines Lab},
  title = {On-Policy Distillation},
  journal = {Thinking Machines Lab: Connectionism},
  year = {2025},
  note = {https://thinkingmachines.ai/blog/on-policy-distillation},
  doi = {10.64434/tml.20251026},
}
```