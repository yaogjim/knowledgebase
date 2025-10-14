---
title: "# nanochat极速通关"
source: "https://x.com/karpathy/status/1977755427569111362"
author:
  - "[[@karpathy]]"
published: 2025-10-14
created: 2025-10-14
description:
tags:
  - "@karpathy # AI # LLM # ChatGPT # Andrej Karpathy # nanochat # 自动化 # 机器学习 # 深度学习"
---
**Andrej Karpathy** @karpathy [2025-10-13](https://x.com/karpathy/status/1977755427569111362)

  
激动地发布新仓库：nanochat！

（这是我写过最天马行空的作品之一）。

与我之前仅涵盖预训练的类似项目 nanoGPT 不同，nanochat 是一个极简的、从零构建的全栈训练/推理流水线，用单一且依赖极少的代码库实现了简易版 ChatGPT 克隆。只需启动云 GPU 实例，运行单个脚本，最快 4 小时后就能通过类 ChatGPT 的网页界面与你自己的 LLM 对话。

其代码量约为8000行，在我看来相当简洁，旨在：

使用新的 Rust 实现训练分词器

在 FineWeb 上对 Transformer LLM 进行预训练，通过多项指标评估 CORE 得分

\- 在 SmolTalk 的用户与助手对话、多项选择题及工具使用数据上进行中期训练。

\- SFT，在多项世界知识选择题（ARC-E/C、MMLU）、数学（GSM8K）和编程（HumanEval）上评估聊天模型

\- 可选地在 GSM8K 数据集上使用“GRPO”方法对模型进行强化学习

在引擎中高效推断模型，利用 KV 缓存、简单的预填充/解码功能及工具使用（轻量级沙箱中的 Python 解释器），可通过 CLI 或类似 ChatGPT 的 Web 界面与其对话。

\- 撰写一份简化的成绩报告单，以总结并游戏化整个流程。

即使成本低至约 100 美元（在 8 个 H100 节点上训练约 4 小时），你也能训练出一个小型 ChatGPT 克隆模型，可以与之简单对话，还能创作故事诗歌、回答基础问题。训练约 12 小时即可超越 GPT-2 的核心指标。当训练成本逐步提升至约 1000 美元（训练 41.6 小时）时，模型会迅速变得条理清晰，能够解决简单数学编程问题并通过选择题测试。例如深度为 30 的模型训练 24 小时（计算量相当于 GPT-3 Small 125M 版本，为 GPT-3 的千分之一），在 MMLU 测试中得分达 40 多分，ARC-Easy 获 70 多分，GSM8K 得 20 多分等。

我的目标是将完整的“强基线”技术栈整合进一个统一、精简、可读性强、易于修改且最大限度可复制的代码库中。nanochat 将成为 LLM101n（目前仍在开发中）的收官项目。我认为它还有潜力发展成为类似之前 nanoGPT 的研究框架或基准平台。虽然该项目远未完成、调优或优化（实际上我认为还存在不少容易改进的地方），但整体框架已初具雏形，足以在 GitHub 上发布，供大家共同完善各个组成部分。

仓库链接及 nanochat 极速通关的详细教程详见回复内容。

![Black background with white bold text displaying nano nochatchat repeated twice in a stylized font resembling a logo or banner for the nanochat project.](https://pbs.twimg.com/media/G3JjbtjbIAAQdaz?format=png&name=large)

---

**Andrej Karpathy** @karpathy [2025-10-13](https://x.com/karpathy/status/1977755430093980034)

  
GitHub 仓库：

https://github.com/karpathy/nanochat…

更详细且技术性的逐步讲解：

https://github.com/karpathy/nanochat/discussions/1…

在 WebUI 中与价值 100 美元、训练 4 小时的 nanochat 进行的示例对话。这...挺有意思的:) 更大规模的模型（例如训练 12 小时、深度 26 或训练 24 小时、深度 30 的模型）会迅速展现出更强的能力。

![Image](https://pbs.twimg.com/media/G3Jjxmba8AA5mSs?format=jpg&name=large)

---

**Andrej Karpathy** @karpathy [2025-10-13](https://x.com/karpathy/status/1977755433172443626)

  
以下是报告中 100 美元速通所生成的部分总结指标示例。当前代码库略超 8000 行，但我尽力保持代码简洁且注释清晰。

现在进入有趣的环节——调优与逐步优化。

![Image](https://pbs.twimg.com/media/G3Jj9ibbAAIqLPr?format=jpg&name=large)

---

**Sebastian Raschka** @rasbt [2025-10-13](https://x.com/rasbt/status/1977761176592273467)

  
哦，不错！感谢分享！好奇问一下，这个训练是基于什么模型架构的呢？

---

**Andrej Karpathy** @karpathy [2025-10-13](https://x.com/karpathy/status/1977763273786507691)

  
基本上类似 Llama，但更简化一些，融合了改进版 nanoGPT 的部分特点。我们试图为这个规模找到一个可靠的基础模型。

密集型变压器

旋转嵌入（无位置嵌入）

\- QK 归一化

\- 用于嵌入和解嵌入的非绑定权重

\- 词嵌入后的归一化

\-

---

**Creative Dreamer** @FuturistASI [2025-10-13](https://x.com/FuturistASI/status/1977765238243008654)

@grok explain this to me like I’m in high school 

---

**Grok** @grok [2025-10-13](https://x.com/grok/status/1977765364089151755)

Andrej Karpathy just released "nanochat," a simple code project that lets anyone build their own basic version of ChatGPT from scratch. It's like a recipe: you rent a powerful computer (GPU), run one script, and in about 4 hours (for ~$100), you train an AI that can chat, answer 

---

**Ricky creator | builder | learner | maker** @rcmisk [2025-10-13](https://x.com/rcmisk/status/1977758774459859325)

  
哇，太感谢了！这还是开源的啊？

那么，这是否意味着我可以使用自己提供的数据来训练它？比如我所有的 Notion 笔记、健康数据，以及其他 LLM 的聊天记录？

一个懂我的个人聊天机器人？

---

**Andrej Karpathy** @karpathy [2025-10-13](https://x.com/karpathy/status/1977760627730051214)

  
好问题，ty。我认为这个代码库不太适合这个用途。你可以把微型模型想象成非常年幼的孩子（比如幼儿园阶段），它们确实不具备大型模型那种原始智能。如果你用自己的数据对它进行微调或训练，结果很可能会——

---

**Ricky creator | builder | learner | maker** @rcmisk [2025-10-13](https://x.com/rcmisk/status/1977788217005936902)

  
感谢您如此详尽的回复，安德烈！

我明白了，那么这个代码库主要是用于微型模型训练的吗？

我会去看看这个！

---

**Trackme** @NgOtha\_deiii [2025-10-13](https://x.com/NgOtha_deiii/status/1977794784967225777)

  
这是为了从零开始学习一切。
