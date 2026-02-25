---
title: "2026-02-25_G_kdeniz_G_lmez_G_kdeniz_G_lmez_因此_我们提供了一个包含大量_MLX_LM_LoRA_示例的"
source: "https://x.com/ActuallyIsaak/status/2022414004623479014"
author:
  - "[[@Gökdeniz Gülmez]]"
published: 2026-02-25
created: 2026-02-25
description:
tags:
  - "x"
  - "@Gökdeniz Gülmez"
  - "https"
  - "github"
---

# Gökdeniz Gülmez 因此，我们提供了一个包含大量 MLX-LM-LoRA 示例的

**Gökdeniz Gülmez**

因此，我们提供了一个包含大量 MLX-LM-LoRA 示例的新仓库，可用于训练您自己的适用于 Apple Silicon 的 LLM，即使在超长上下文长度下也能快速高效地运行：

微调 Qwen3 4B 指令，上下文为 32K： [https://github.com/Goekdeniz-Guelmez/mlx-lm-lora-example-notebooks/blob/main/finetuning/Qwen3\_4B\_Instruct\_32k.ipynb…](https://t.co/XnPTtvyUmM) 训练

[@IBMResearch](/IBMResearch)

Granite 350M 模型在 RL-GRPO 推理中： [https://github.com/Goekdeniz-Guelmez/mlx-lm-lora-example-notebooks/blob/main/rl/Granite\_4-0\_350M\_Gabliterated\_GRPO.ipynb…](https://t.co/yhAbXrSNoQ) 或

[@liquidai](/liquidai)

LFM2.5 1.2B on GRPO: [https://github.com/Goekdeniz-Guelmez/mlx-lm-lora-example-notebooks/blob/main/rl/LFM2-5\_1.2B\_Instruct\_GRPO.ipynb…](https://t.co/jxeTvOA17i) 或者训练 Qwen3 4B 指令进行偏好优化:ORPO 内存高效且速度极快: [https://github.com/Goekdeniz-Guelmez/mlx-lm-lora-example-notebooks/blob/main/preference/Qwen3\_4B\_Gabliterated\_ORPO.ipynb…](https://t.co/fZqUcUjdLO) DPO: [https://github.com/Goekdeniz-Guelmez/mlx-lm-lora-example-notebooks/blob/main/preference/Qwen3\_4B\_Gabliterated\_DPO.ipynb…](https://t.co/KsqZb4XvaN) 或者甚至

[@GoogleDeepMind](/GoogleDeepMind)

Gemma3 1B 在线 DPO (RLHF)： [https://github.com/Goekdeniz-Guelmez/mlx-lm-lora-example-notebooks/blob/main/preference/Gemma\_3\_1B-IT\_Gabliterated\_Online\_DPO.ipynb…](https://t.co/FmRADWR4gK) 以及更多信息： [https://github.com/Goekdeniz-Guelmez/mlx-lm-lora-example-notebooks…](https://t.co/mWLDb8oCbC)

* * *

### 热门回复

**@Alexander Fischer** ♥ 2 · 💬 1

是否支持曼巴/混合型机型？ :D

**@Gökdeniz Gülmez** ♥ 1 · 💬 0

是的，所有 MLX-LM 模型都支持，但不支持超长上下文训练（通过 seq\_step\_size 参数）。这个问题以后再讨论。