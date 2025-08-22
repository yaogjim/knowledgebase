---
title: "Open-source DeepResearch – Freeing our search agents"
source: "https://huggingface.co/blog/open-deep-research"
author:
published: 2025-02-04
created: 2025-06-26
description: "We’re on a journey to advance and democratize artificial intelligence through open source and open science."
tags:
  - "clippings"
---
[返回文章](https://huggingface.co/blog)

## 开源深度研究——解放我们的搜索代理

发布于2025年2月4日

[GitHub 上的更新](https://github.com/huggingface/blog/blob/main/open-deep-research.md)

## TLDR

昨天，OpenAI 发布了《深度研究》，这是一个通过浏览网页来总结内容并基于总结回答问题的系统。该系统令人印象深刻，我们首次试用时就被它震撼到了。

这篇博客文章的主要成果之一是在通用人工智能助手基准测试（GAIA）中性能有了显著提升，这也是我们最近一直在研究的一个基准测试。在该测试中，他们平均在单样本情况下成功达到了近 67%的正确答案率，在特别具有挑战性的涉及多步推理和工具使用的“3 级”问题上达到了 47.6%的正确率（有关 GAIA 的介绍见下文）。

DeepResearch 由一个大语言模型（LLM）（可以从 OpenAI 提供的当前大语言模型列表中选择，如 4o、o1、o3 等）和一个内部“智能体框架”组成，该框架引导大语言模型使用网络搜索等工具，并按步骤组织其行动。

虽然强大的语言模型（LLMs）现在在开源领域可以免费获取（例如，参见最近的 DeepSeek R1 模型），但 OpenAI 并未过多披露 Deep Research 背后的智能体框架……

于是我们决定展开一场为期24小时的任务，重现他们的研究成果，并在此过程中开源所需的框架！

时间紧迫，我们走吧！⏱️

## 目录

- [开源深度研究——解放我们的搜索代理](https://huggingface.co/blog/#open-source-deepresearch--freeing-our-search-agents)
	- [TLDR](https://huggingface.co/blog/#tldr)
	- [目录](https://huggingface.co/blog/#table-of-contents)
	- [什么是智能体框架以及它们为何重要？](https://huggingface.co/blog/#what-are-agent-frameworks-and-why-they-matter)
	- [GAIA 基准测试](https://huggingface.co/blog/#the-gaia-benchmark)
	- [构建一个开放的深度研究](https://huggingface.co/blog/#building-an-open-deep-research)
		- [使用代码智能体](https://huggingface.co/blog/#using-a-codeagent)
		- [打造合适的工具 🛠️](https://huggingface.co/blog/#making-the-right-tools-%EF%B8%8F)
	- [结果 🏅](https://huggingface.co/blog/#results-)
	- [社区复现](https://huggingface.co/blog/#community-reproductions)
	- [最重要的后续步骤](https://huggingface.co/blog/#most-important-next-steps)

## 什么是智能体框架以及它们为何重要？

> 智能体框架是位于大语言模型（LLM）之上的一层，用于使该大语言模型执行操作（如浏览网页或读取 PDF 文档），并将其操作组织成一系列步骤。如需快速了解智能体，请查看 [吴恩达的这篇精彩访谈](https://youtu.be/sal78ACtGTc?feature=shared&t=52) 以及我们关于 smolagents 库的 [介绍博客文章](https://huggingface.co/blog/smolagents) 。如需更深入地了解智能体，你可以订阅我们即将在几天内开课的智能体课程： [此处链接](https://huggingface.us17.list-manage.com/subscribe?u=7f57e683fa28b51bfc493d048&id=9ed45a3ef6) 。

几乎每个人都已经通过与聊天机器人互动体验到了大语言模型（LLMs）的强大之处。然而，并非每个人都意识到，将这些大语言模型集成到智能体系统中可以赋予它们真正的超能力！

以下是一个近期的例子，比较了几个前沿的大语言模型（LLMs）在有无智能体框架（在这种情况下是简单的 [smolagents](https://github.com/huggingface/smolagents) 库）时的性能——使用智能体框架可将性能提升多达 60 分！

[![Benchmarks](https://huggingface.co/datasets/huggingface/documentation-images/resolve/6c7ed2035810565043c92b472d5564c3f1fa4d7e/blog/open-deep-research/benchmarks.png)](https://huggingface.co/datasets/huggingface/documentation-images/resolve/6c7ed2035810565043c92b472d5564c3f1fa4d7e/blog/open-deep-research/benchmarks.png)

事实上，OpenAI 也在其发布的博客文章中强调了 Deep Research 在知识密集型的“人类最后一场考试”基准测试中，表现比独立的大语言模型（LLMs）好得多。

那么，当我们将当前顶级的语言模型集成到一个智能体框架中，以朝着“开源深度研究”的目标努力时，会发生什么呢？

**快速说明：** 我们将在相同的 GAIA 挑战上对结果进行基准测试，但请记住，这仍在进行中。深度研究是一项巨大的成就，对其进行开源复现需要时间。特别是，要实现完全对等，需要改进浏览器的使用和交互，就像 OpenAI Operator 所提供的那样，即超越我们在第一步中探索的当前仅文本的网络交互。

让我们首先了解一下挑战的范围：GAIA。

## GAIA 基准测试

[GAIA](https://huggingface.co/datasets/gaia-benchmark/GAIA) 可以说是针对智能体最全面的基准测试。它的问题非常难，涉及基于大语言模型（LLM）系统的诸多挑战。以下是一个难题示例：

> 在2008年画作《乌兹别克斯坦刺绣》中展示的水果中，哪些是1949年10月那艘远洋客轮早餐菜单的一部分？那艘客轮后来被用作电影《最后航程》的水上道具。请以逗号分隔的列表形式给出这些水果，按照它们在画作中从12点位置开始顺时针排列的顺序。每个水果都使用复数形式。

你可以看到这个问题涉及几个挑战：

- 以受限格式回答
- 利用多模态功能（从图像中提取成果）
- 收集多条信息，其中一些信息依赖于其他信息：
	- 识别图片上的水果
	- 找出哪艘远洋客轮被用作电影《最后航程》的浮动道具
	- 查找上述远洋客轮1949年10月的早餐菜单
- 以正确的顺序将解决问题的轨迹串联起来。

要解决这个问题，既需要高层次的规划能力，也需要严谨的执行能力，而这两个方面恰恰是 LLMs 单独使用时所难以应对的。

所以它对智能体系统来说是一个很棒的测试集！

在 GAIA 的 [公开排行榜](https://huggingface.co/spaces/gaia-benchmark/leaderboard) 上，当没有任何智能体设置时，GPT-4 在验证集上的得分甚至未达到 7%。而在另一端，通过深度研究，OpenAI 在验证集上达到了 67.36%的分数，整整高出一个数量级！（不过我们不知道它们在私人测试集上的实际表现如何。）

让我们看看能否借助开源工具做得更好！

## 构建一个开放的深度研究

### 使用代码智能体

我们要解决的对传统人工智能代理系统的第一个改进是使用所谓的“代码代理”。正如王等人（2024年）所表明的，让代理用代码来表达其行动有几个优点，但最显著的是，\*\*代码是专门设计用来表达复杂的行动序列的\*\*。

考虑王等人给出的这个例子：

[![Code Agent](https://huggingface.co/datasets/huggingface/documentation-images/resolve/6c7ed2035810565043c92b472d5564c3f1fa4d7e/blog/open-deep-research/code_agent.png)](https://huggingface.co/datasets/huggingface/documentation-images/resolve/6c7ed2035810565043c92b472d5564c3f1fa4d7e/blog/open-deep-research/code_agent.png)

这凸显了使用代码的几个优点：

- 代码操作比 JSON **简洁得多** 。
	- 需要运行 4 个并行流，每个流包含 5 个连续动作？在 JSON 中，你需要生成 20 个 JSON 块，每个块在单独的步骤中；而在代码中，这只需要 1 步。
	- 该论文平均表明，代码操作所需的步骤比 JSON 少 30%，这相当于生成的令牌数量也减少了相同比例。由于大语言模型（LLM）调用通常是智能体系统的成本决定因素，这意味着你的智能体系统运行成本降低了约 30%。
- 代码能够复用通用库中的工具
- 在基准测试中表现更佳，原因有二：
	- 表达动作的更直观方式
	- 在训练中让语言模型大量接触代码

上述优势在我们对 [agent\_reasoning\_benchmark](https://github.com/aymeric-roucher/agent_reasoning_benchmark) 进行的实验中得到了证实。

通过构建 `smolagents` ，我们还可以列举一个显著的额外优势，即对状态的处理更好：这在多模态任务中尤其有用。需要存储此图像/音频/其他内容以供后续使用？没问题，只需将其作为状态中的变量进行赋值，如果需要，4 步之后就可以重新使用它。在 JSON 中，你必须让 LLM 在字典键中为其命名，并相信 LLM 之后会明白它仍然可以使用该内容。

### 打造合适的工具 🛠️

现在我们需要为智能体提供正确的工具集。

**1.** 一个网络浏览器。虽然要实现全面性能需要像 [Operator](https://openai.com/index/introducing-operator/) 这样功能完备的网络浏览器交互，但目前我们为首个概念验证构建了一个极其简单的基于文本的网络浏览器。你可以 [在此处](https://github.com/huggingface/smolagents/tree/main/examples/open_deep_research/scripts/text_web_browser.py) 找到代码。

**2.** 一个简单的文本检查器，能够 **读取一堆文本文件格式** ，可在此处 [找到它](https://github.com/huggingface/smolagents/tree/main/examples/open_deep_research/scripts/text_inspector_tool.py) 。

这些工具取自微软研究院出色的 [Magentic-One](https://www.microsoft.com/en-us/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks/) 智能体，向他们致敬！我们对其改动不大，因为我们的目标是以尽可能低的复杂度获得尽可能高的性能。

以下是我们认为能切实提升这些工具性能的简短改进路线图（欢迎随时提交拉取请求并做出贡献！）：

- 扩展可读取的文件格式数量。
- 提出对文件进行更细粒度的处理。
- 用基于视觉的浏览器取代网络浏览器，我们已经在\[此处\](a id=0)开始这样做了。

## 结果 🏅

在我们长达 24 小时以上的复制冲刺过程中，我们已经看到我们的智能体在 GAIA 上的性能稳步提升！

我们已经迅速从之前使用开源框架的最优技术水平（Magentic-One 约为 46%）提升到了我们目前在验证集上 55.15%的性能。

性能的提升主要归功于让我们的智能体用代码编写它们的行动！实际上，当切换到一个用 JSON 而不是代码编写行动的标准智能体时，相同设置在验证集上的性能立即下降到平均 33%。

[这是最终的智能体系统。](https://github.com/huggingface/smolagents/tree/main/examples/open_deep_research)

我们在此为您设置了一个实时演示 [（点击此处查看）](https://m-ric-open-deep-research.hf.space/) ，供您试用！

然而，这仅仅是个开始，还有很多需要改进的地方！我们的开源工具可以变得更好，smolagents 框架也可以进行优化，并且我们很乐意探索性能更优的开源模型来支持智能体。

我们欢迎社区加入我们的这项事业，这样我们就可以共同利用开放研究的力量，构建一个出色的开源智能体框架！这将使任何人都能够在家中使用自己喜欢的模型，通过完全本地化和定制化的方式运行类似 DeepResearch 的智能体！

## 社区复现

当我们致力于此并专注于 GAIA 时，社区中出现了其他出色的深度研究开源实现，特别是来自于

- [dzhng](https://x.com/dzhng/status/1886603396578484630),
- [阿萨费洛维奇](https://github.com/assafelovic/gpt-researcher) ，
- [nickscamara](https://github.com/nickscamara/open-deep-research) ，
- [豆包](https://github.com/jina-ai/node-DeepResearch) 和
- [mshumer](https://x.com/mattshumer_/status/1886558939434664404) 。 （这里的“mshumer”看起来像是一个特定名称，未进行翻译，保留原样）

这些实现中的每一个都使用不同的库来索引数据、浏览网页和查询大语言模型（LLMs）。在这个项目中，我们希望<强 id=0>重现 OpenAI 提出的基准测试（通过率@1 平均分数），对切换到开源大语言模型（如百川 R1）进行基准测试并记录我们的发现，使用视觉大语言模型，针对代码原生智能体对传统工具调用进行基准测试。

## 接下来最重要的步骤

OpenAI 的深度研究可能得益于他们随 [Operator](https://openai.com/index/introducing-operator/) 推出的出色网络浏览器。

所以我们接下来就要解决这个问题！在一个更普遍的问题上：我们要构建图形用户界面代理，即“能够查看你的屏幕并可直接通过鼠标和键盘进行操作的代理”。如果你对这个项目感到兴奋，并且想通过开源帮助每个人都能获得如此酷炫的功能，我们非常欢迎你的贡献！