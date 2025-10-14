---
title: "nanochat"
source: "https://simonwillison.net/2025/Oct/13/nanochat/"
author:
  - "[[Simon Willison]]"
published: 2025-10-14
created: 2025-10-14
description: "Really interesting new project from Andrej Karpathy, described at length in this discussion post. It provides a full ChatGPT-style LLM, including training, inference and a web Ui, that can be …"
tags:
  - "Simon Willison"
---
**[nanochat](https://github.com/karpathy/nanochat)** （ [经由](https://twitter.com/karpathy/status/1977755427569111362 "@karpathy") ）安德烈·卡帕西推出的一个非常有趣的新项目， [在这篇讨论帖](https://github.com/karpathy/nanochat/discussions/1) 中有详细阐述。

它提供了一个完整的 ChatGPT 风格 LLM，包含训练、推理和网页界面，最低仅需 100 美元即可完成训练

> 这个仓库是一个全栈实现，采用单一、简洁、极简、可定制且依赖轻量的代码库，构建了类似 ChatGPT 的 LLM。

代码量大约在 8000 行左右，主要是 Python（使用 PyTorch）加上少量 Rust 用于 [训练分词器](https://github.com/karpathy/nanochat/tree/master/rustbpe) 。

安德烈建议租用一台 8XH100 NVIDIA 节点，每小时约 24 美元来训练模型。4 小时（约 100 美元）足以获得一个能够进行对话的模型—— [这里有一个基本连贯的示例](https://twitter.com/karpathy/status/1977755430093980034) 。若运行 12 小时，得到的模型表现会略优于 GPT-2。我期待听到更长时间训练后的成果！

最终模型参数约为 5.61 亿，因此几乎能在任何设备上运行。我曾在 iPhone 上运行过 40 亿参数的模型，5.61 亿参数的模型即便在廉价的树莓派上也能轻松运行。

该模型默认使用来自 [karpathy/fineweb-edu-100b-shuffle](https://huggingface.co/datasets/karpathy/fineweb-edu-100b-shuffle) （源自 [FineWeb-Edu](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu) ）的约 24GB 数据进行训练，随后在 [SmolTalk](https://huggingface.co/datasets/HuggingFaceTB/smol-smoltalk) （46 万条）、 [MMLU 辅助训练集](https://huggingface.co/datasets/cais/mmlu) （10 万条）和 [GSM8K](https://huggingface.co/datasets/openai/gsm8k) （8000 条）共 56.8 万条样本上进行 [中期训练](https://github.com/karpathy/nanochat/blob/5fd0b138860a76beb60cf099fa46f74191b50941/scripts/mid_train.py) ，最后基于 [ARC-Easy](https://huggingface.co/datasets/allenai/ai2_arc#arc-easy-1) （2300 条）、 [ARC-Challenge](https://huggingface.co/datasets/allenai/ai2_arc#arc-challenge) （1100 条）、 [GSM8K](https://huggingface.co/datasets/openai/gsm8k) （8000 条）和 [SmolTalk](https://huggingface.co/datasets/HuggingFaceTB/smol-smoltalk) （1 万条）共 2.14 万条样本进行 [监督微调](https://github.com/karpathy/nanochat/blob/5fd0b138860a76beb60cf099fa46f74191b50941/scripts/chat_sft.py) 。

这是 [网络服务器](https://github.com/karpathy/nanochat/blob/5fd0b138860a76beb60cf099fa46f74191b50941/scripts/chat_web.py) 的代码，其前端采用了这段简洁明了的原生 JavaScript [HTML+JavaScript 前端](https://github.com/karpathy/nanochat/blob/5fd0b138860a76beb60cf099fa46f74191b50941/nanochat/ui.html) 实现。

**更新** ：Sam Dobson 已将模型构建版本推送到 Hugging Face 上的 [sdobson/nanochat](https://huggingface.co/sdobson/nanochat) 。该模型原本设计在 CUDA 上运行，但我让 Claude Code 在代码库中进行调试，不断尝试直到它成功实现在 macOS 的 CPU 上运行，最终产生了 [这个脚本](https://gist.github.com/simonw/912623bf00d6c13cc0211508969a100a) ，我已将其作为 Gist 发布。您应该可以通过以下方式使用 uv 尝试该模型：

```
cd /tmp
git clone https://huggingface.co/sdobson/nanochat
uv run https://gist.githubusercontent.com/simonw/912623bf00d6c13cc0211508969a100a/raw/80f79c6a6f1e1b5d4485368ef3ddafa5ce853131/generate_cpu.py \
--model-dir /tmp/nanochat \
--prompt "Tell me about dogs."
```

我收到了这个（因超出令牌限制而被截断）：

> 很高兴能与您分享我对狗狗的热爱。作为一名兽医，我有幸帮助许多宠物主人照顾他们的毛茸伙伴。训练它们、成为它们生活中的一部分，以及看到它们见到最爱的零食或玩具时脸上绽放的光芒，这些经历都格外特别。
> 
> 我曾有幸与超过1000只狗狗共事，不得不说，这是一段收获满满的经历。主人与宠物之间的纽带

发布于 [2025 年 10 月 13 日](https://simonwillison.net/2025/Oct/13/) 晚上 8:29
