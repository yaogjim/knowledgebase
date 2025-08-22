---
title: "Vision Language Model Alignment in TRL"
source: "https://huggingface.co/blog/trl-vlm-alignment"
author:
published: 2025-08-08
created: 2025-08-08
description: "We’re on a journey to advance and democratize artificial intelligence through open source and open science."
tags:
---
[Back to Articles](https://huggingface.co/blog)

## TRL 中的视觉语言模型对齐 ⚡️

发布于2025年8月7日

[Update on GitHub](https://github.com/huggingface/blog/blob/main/trl-vlm-alignment.md)

## Introduction

视觉语言模型（VLM）正在变得更强大，但使它们与人类偏好保持一致仍然很重要。在 TRL 中，我们已经展示了如何通过【监督微调（SFT）】和【直接偏好优化（DPO）】对 VLM 进行训练后调整。这次，我们将更进一步。

\*\*总结\*\*：我们在 TRL 中添加了两种新的多模态对齐方法：\*\*组相对策略优化（GRPO）\*\*、其变体\*\*组序列策略优化（GSPO）\*\*以及\*\*混合偏好优化（MPO）\*\*。所有这些方法都能让你超越成对的 DPO，从偏好数据中提取更多信号，并能更好地与现代视觉语言模型（VLM）进行扩展。我们发布了训练脚本和演示笔记本，以便轻松上手！

## Table of Contents

- [TRL ⚡️ 中用于视觉语言模型的多模态对齐](https://huggingface.co/blog/#multimodal-alignment-for-vlms-in-trl-%EF%B8%8F)
	- [Introduction](https://huggingface.co/blog/#introduction)
	- [视觉语言模型对齐](https://huggingface.co/blog/#alignment-for-vision-language-models)
		- [混合偏好优化（MPO）](https://huggingface.co/blog/#mixed-preference-optimization-mpo)
		- [多模态组相对策略优化（GRPO）](https://huggingface.co/blog/#multimodal-group-relative-policy-optimization-grpo)
		- [组序列策略优化（GSPO）](https://huggingface.co/blog/#group-sequence-policy-optimization-gspo)
		- [Comparison](https://huggingface.co/blog/#comparison)
	- [TRL 中的 vLLM 集成](https://huggingface.co/blog/#vllm-integration-in-trl)
	- [Useful Resources](https://huggingface.co/blog/#useful-resources)

## 视觉语言模型的对齐

传统上，你会采用一个基础模型，应用监督微调（SFT）来遵循指令，然后应用直接偏好优化（DPO）使其与偏好数据对齐。此前， [我们将这种方法应用于视觉语言模型（VLM）](https://huggingface.co/blog/dpo_vlm) ，并在 IDEFICS2 上进行了验证，结果显示模型响应有所改进。

DPO 的工作原理是使用对比损失来优化模型响应之间的偏好：你有一个选定的答案和一个被拒绝的答案，然后根据你想要和不想要的内容来优化你的偏好。

但在过去一年中，新的多模态对齐方法，如 GRPO 和 MPO，开始流行起来，这些方法可以进一步提升视觉语言模型（VLM）的性能。在博客文章末尾，你可以找到一个展示模型响应差异的表格。

### 混合偏好优化（MPO）

由于分布偏移，将多模态模型与监督微调（SFT）对齐以执行推理任务存在不足。同时，与近端策略优化对偶（DPO）对齐的模型无法生成连贯的推理依据，并且可能会生成重复的回答。为了解决这个问题，有一种专门为多模态模型设计的新技术，称为混合偏好优化（MPO）。这种方法本质上是 DPO 的扩展，具有多种损失：来自 DPO 的偏好损失（sigmoid）、来自二元分类器优化（BCO）的质量损失以及来自 SFT 的生成损失。根据论文，简单地切换到这种组合损失会使 MathVista 的性能提高 6.2 分！

[![MPO](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/trl-vlm/image_1.png)](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/trl-vlm/image_1.png)

由于这只是在修改损失，我们在 TRL 的 `DPOTrainer` 类中添加了对组合损失的支持。要使用它，你可以按如下方式初始化 `DPOConfig` ：

```python
mpo_config = DPOConfig(
    output_dir=tmp_dir,
    per_device_train_batch_size=2,
    learning_rate=9e-1,
    loss_type=["sigmoid", "bco_pair", "sft"], # Loss types to combine, as used in the MPO paper
    loss_weights=[0.8, 0.2, 1.0], # Corresponding weights, as used in the MPO paper
    report_to="none",
    bf16=False,
    fp16=False,
    use_cpu=True,
    max_steps=1,
)
```

然后初始化 `DPOTrainer` ：

```python
mpo_trainer = DPOTrainer(
    model=model_id,
    args=mpo_config,
    processing_class=tokenizer,
    train_dataset=dataset,
)
mpo_trainer.train()
```

就是这样！如果你想进一步探索，可以 [在这里](https://huggingface.co/learn/cookbook/fine_tuning_vlm_mpo) 找到一个完整的笔记本示例。

### 多模态组相对策略优化（GRPO）

分组相对策略优化（GRPO）是一种前沿的对齐方法，最初在《DeepSeek Math》论文中提出，后来被集成到具有开创性的大语言模型（LLM）DeepSeek R1 中。它是近端策略优化（PPO）的扩展，其策略更新是在组（代表对话展开方式的一批轨迹）上进行的。此特性使其对奖励噪声更具鲁棒性，因为噪声在组内会相互抵消。由于模型学习的是对良好响应的更广泛理解，而非单个高奖励样本，所以这种方法也使模型具有很高的性能。

[![GRPO](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/trl-vlm/image_2.png)](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/trl-vlm/image_2.png)

在 TRL 中，我们现在引入了对视觉语言模型的 GRPO 支持。我们不会提供完整的训练脚本示例，因为你可以在笔记本中找到它。相反，我们将专注于突出关键组件和概念。

为了使训练脚本有效运行，我们需要验证答案格式是否正确以及解决方案本身是否与已完成部分接近，因此我们编写了两个奖励函数。为了真正看到后一个奖励的改进，你需要一个相当极端的设置，即拥有相对较大的模型、大量的生成结果以及高质量、多样化的数据集。

```python
import re
from math_verify import LatexExtractionConfig, parse, verify

def format_reward(completions, **kwargs):
    """Reward function that checks if the completion has a specific format."""
    pattern = r"^<think>.*?</think>\s*<answer>.*?</answer>$"
    matches = [re.match(pattern, content) for content in completions]
    rewards_list = [1.0 if match else 0.0 for match in matches]
    rewards = [1.0 if match else 0.0 for match in matches]
    print(completions)
    print(rewards)
    return rewards

def accuracy_reward(completions, **kwargs):
    """Reward function that checks if the completion is the same as the ground truth."""
    solutions = kwargs['solution']
    completion_contents = [completion[0]["content"] for completion in completions]
    rewards = []
    for content, solution in zip(completion_contents, solutions):
        gold_parsed = parse(solution, extraction_mode="first_match", extraction_config=[LatexExtractionConfig()])
        answer_parsed = parse(content, extraction_mode="first_match", extraction_config=[LatexExtractionConfig()])
        if len(gold_parsed) != 0:
            try:
                rewards.append(float(verify(answer_parsed, gold_parsed)))
            except Exception:
                rewards.append(0.0)
        else:
            rewards.append(1.0)
    return rewards
```

然后，你可以初始化 GRPOConfig 和 GRPOTrainer，传入我们上面定义的奖励函数，并调用 train()开始训练。

```python
from trl import GRPOConfig

training_args = GRPOConfig(
    learning_rate=1e-5,
    remove_unused_columns=False,
    max_prompt_length=None,
    .. # setup other params of choice here
)
trainer = GRPOTrainer(
    model=model,
    reward_funcs=[format_reward, accuracy_reward],
    args=training_args,
    train_dataset=train_dataset,
    processing_class=processor
)
trainer.train()
```

在此处探索完整的笔记本示例 [此处](https://huggingface.co/learn/cookbook/fine_tuning_vlm_grpo_trl) 。

### 组序列策略优化（GSPO）

[组序列策略优化](https://huggingface.co/papers/2507.18071) （GSPO）是字节跳动公司最近发布的一种强化学习对齐算法，它克服了 GRPO 的一些局限性。它在序列级别而不是逐个 token 地实现了更稳定的训练计算重要性采样权重。其优势在混合专家（MoE）风格的模型中更为 [显著](https://github.com/volcengine/verl/pull/2775#issuecomment-3134375131) 。

最新的 TRL 还引入了对 GSPO 的支持，由于它是 GRPO 损失的一个变体，因此具备多模态支持。要创建训练器，过程与 GRPO 相同，但需添加以下额外参数（值取自论文）。

```python
from trl import GRPOConfig

training_args = GRPOConfig(
        ...
    importance_sampling_level="sequence",
    epsilon=3e-4,
    epsilon_high=4e-4,
    beta=0.0,
    loss_type="grpo",
    steps_per_generation=1,
    steps_per_generation=4
)
```

### Comparison

以下是一个表格，总结了使用上述技术微调后的 Qwen2.5VL-3B 的模型输出。请注意，我们仅在数据集子集上进行了少量运行，并且模型是在不同数据集上进行微调的，因此该比较仅用于初步检验。

在这里查看答案

**Image:**[![Image](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/vlm_math_question.png)](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/vlm_math_question.png)

**Question:** In the given figure, if the angle APO is 25.0 degrees, what is the measure of angle AOB? Choices: A: 140° B: 130° C: 120° D: 110°

**Answer in the Dataset:** To find the measure of angle AOB, we can use the property that the sum of the interior angles of a quadrilateral is equal to 360 degrees. Applying this property, we can calculate angle AOB as 360 - angle OAP - angle OBP - angle P. Since angle OAP and angle OBP are both 90 degrees, and angle P is given as 50 degrees, we can substitute these values into the equation to get angle AOB = 360 - 90 - 90 - 50 = 130 degrees. Therefore, the measure of angle AOB is 130 degrees. Therefore, the answer is option B. Answer:B

**Base Model Output:** To find the measure of angle AOB, we need to use the properties of angles subtended by the same arc in a circle. Specifically, the angle subtended by an arc at the center of the circle (angle AOB) is twice the angle subtended by the same arc at any point on the circumference (angle APO).Given that angle APO = 25°, we can calculate angle AOB as follows: Since angle AOB is twice angle APO, we have:\[ Angle AOB = 2 \* Angle APO \]\[ Angle AOB = 2 \* 25° \]\[ Angle AOB = 50° \]However, this calculation seems incorrect based on the provided choices. Let's re-evaluate using the correct property.The correct property states that the angle subtended by an arc at the center of the circle is twice the angle subtended by the same arc at any point on the circumference. Therefore, the correct calculation should be: Angle AOB = 2 \* Angle APO = 2 \* 25° = 50°But since this does not match the given choices, let's consider another approach. If angle APO is 25°, and considering the properties of cyclic quadrilaterals or the fact that the sum of opposite angles in a cyclic quadrilateral is 180°, we might need to look at the supplementary angles formed by the arc and the chord.Let's assume the correct interpretation involves finding the supplementary angle to the given angle APO which would give us the measure of angle AOB. Angle AOB = 180° - Angle APO = 180° - 25° = 155°This still doesn't match the choices. Given the choices provided, it seems there might be a misunderstanding or a different interpretation needed. However, based on standard geometric principles, the correct answer should be: Angle AOB = 2 \* Angle APO = 2 \* 25° = 50° If this is not the case, please provide additional context or clarify the problem statement.

**MPO Output:** To find the measure of angle AOB, we need to use the properties of angles subtended by the same arc in a circle. Specifically, the angle subtended by an arc at the center of the circle (angle AOB) is twice the angle subtended by the same arc at any point on the circumference (angle APO).Given that angle APO = 25°, we can calculate angle AOB as follows: Since angle AOB is twice the angle APO, we have:\[ Angle AOB = 2 \* Angle APO \]\[ Angle AOB = 2 \* 25° \]\[ Angle AOB = 50° \]However, this calculation seems incorrect based on the provided choices. Let's re-evaluate using the correct property.The correct property states that the angle subtended by an arc at the center of the circle is twice the angle subtended by the same arc at any point on the circumference. Therefore, the correct calculation should be: Angle AOB = 2 \* Angle APO = 2 \* 25° = 50°But since this does not match the given choices, let's consider another approach. If we look at the triangle OAP, angle AOP is 90° because it is a right angle (as it is inscribed in a semicircle). Now, angle APO is given as 25°, so angle AOA would be 65° (since it is supplementary to angle APO). Therefore, angle AOB would be half of this, which is 32.5°. However, this also doesn't match the choices.Let's consider the possibility that the problem might involve a different interpretation or a different geometric configuration. Given the choices, let's assume there might be a mistake in the problem statement or the choices themselves. If we were to choose from the given options, none of them seem to fit correctly based on standard geometric principles for this type of problem.

**GRPO Output**: To find the measure of angle AOB, we need to understand that angle AOB is an inscribed angle that intercepts the same arc as the central angle AOP. According to the Inscribed Angle Theorem, the measure of an inscribed angle is half the measure of the central angle that subtends the same arc.Given:- Angle APO = 25.0 degreesSince angle AOB is an inscribed angle intercepting the same arc as the central angle AOP, we can use the Inscribed Angle Theorem:The measure of angle AOB is half the measure of angle AOP.Therefore, the measure of angle AOB is 130 degrees.

**GSPO Output:** To find the measure of angle AOB, we need to understand that angle AOB is an inscribed angle that intercepts the same arc as the central angle AOP. According to the Inscribed Angle Theorem, the measure of an inscribed angle is half the measure of the central angle that subtends the same arc.Given:- Angle APO = 25.0 degreesSince angle AOB is an inscribed angle that intercepts the same arc as the central angle AOP, we can use the Inscribed Angle Theorem to find the measure of angle AOB:The measure of angle AOB is half the measure of angle AOP.Therefore, the answer is B: 130°.

## TRL 中的 vLLM 集成

vLLM 已集成到 TRL 中，以支持在线对齐方法，即在训练期间需要生成样本的情况。运行如下示例脚本可启用 vLLM：

```bash
CUDA_VISIBLE_DEVICES=1,2 python3 examples/scripts/grpo_vlm.py     --model_name_or_path   Qwen/Qwen2.5-VL-3B-Instruct    …   --log_completions --use_vllm --vllm_mode colocate
```

主要有两种模式： `colocate` 和 `server` 。 [`colocate`](https://huggingface.co/blog/vllm-colocate) 在与训练循环相同的进程中运行 vLLM，在训练和生成之间共享同一个 GPU，在 `GRPOTrainer` 内部创建一个 vLLM LLM 实例。同时， `server` 要求你在一个不同的进程中单独为 vLLM 提供服务，在那里你可以访问该服务器。你可以使用以下命令启动此服务器：

```bash
trl vllm-serve --model Qwen/Qwen2.5-VL-3B-Instruct --tensor-parallel-size 1
```

然后你可以按如下方式运行该脚本。

```bash
CUDA_VISIBLE_DEVICES=1,2 python3 examples/scripts/grpo_vlm.py     --model_name_or_path   Qwen/Qwen2.5-VL-3B-Instruct    …   --log_completions --use_vllm --vllm_mode server
```

另一个提示：我们在 TRL 中添加了对使用带有 transformers 后端的 vLLM 的支持。你可以在使用 colocate 运行脚本时或通过传递 `--vllm_model_impl transformers` 标志来服务模型时启用它。

你可以在 [此处](https://huggingface.co/docs/trl/en/vllm_integration) 阅读更多关于 TRL 中 vLLM 集成的内容。

## Useful Resources

在下方，你可以找到一系列资源，用于详细探索视觉语言模型（VLM）的对齐情况。尽情享受吧！

- [**视觉语言模型（更好、更快、更强）**](https://huggingface.co/blog/vlms-2025)
- [**通过混合偏好优化增强多模态大语言模型的推理能力**](https://huggingface.co/papers/2411.10442) （ **MPO 论文** ）
- [**深寻数学：在开放语言模型中突破数学推理的极限**](https://huggingface.co/papers/2402.03300) （ **GRPO 论文** ）
- [**Open-R1**](https://github.com/huggingface/open-r1) **仓库** 以及 [**Open-R1 奖励函数**](https://github.com/huggingface/open-r1/blob/main/src/open_r1/rewards.py)
- [**TRL 文档**](https://huggingface.co/docs/trl/en/index) 和 [**TRL 代码库**](https://github.com/huggingface/trl)
- [**MPO VLM recipe**](https://huggingface.co/learn/cookbook/fine_tuning_vlm_mpo)
- [**GRPO VLM recipe**](https://huggingface.co/learn/cookbook/fine_tuning_vlm_grpo_trl)
- [**更多多模态对齐方法**](https://huggingface.co/learn/cookbook/index)
- [**TRL 多模态训练脚本**](https://github.com/huggingface/trl/tree/main/examples/scripts)
- [**trl 文档中的 vLLM 集成**](https://huggingface.co/docs/trl/en/vllm_integration)
- [**vLLM 中的 Transformer 后端集成**](https://blog.vllm.ai/2025/04/11/transformers-backend.html)
