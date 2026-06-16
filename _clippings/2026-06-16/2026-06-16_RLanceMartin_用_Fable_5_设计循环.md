---
title: "2026-06-16_RLanceMartin_用_Fable_5_设计循环"
source: "https://x.com/RLanceMartin/status/2064397389189071163"
author:
  - "[[@RLanceMartin]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "x"
  - "@RLanceMartin"
  - "https"
  - "claude"
---

# 用 Fable 5 设计循环

**Lance Martin**

# 用 Fable 5 设计循环

Mythos 类模型（如 Claude Fable 5）改变了我们许多人在 Anthropic 的工作方式。我想分享两个充分利用这类模型的技巧。

自校正循环

最近，人们对循环的兴趣很大。

[@bcherny](https://x.com/@bcherny)

[提到](https://x.com/sairahul1/status/2064279904989147577?s=20)

，“（他的）工作是编写循环。”让模型在评估中进行爬山操作是提高任务性能的常见方法：

[/goal](https://code.claude.com/docs/en/goal)

在 Claude Code 中以及

[Outcomes](https://platform.claude.com/docs/en/managed-agents/define-outcomes)

在 Claude Managed Agent 中是原语，让你可以将这一通用方法应用于特定任务。

如我们在

[提示指南](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5) , Fable 5 擅长循环自我修正。精心设计的目标或评分标准会为 Claude 运行的环境添加反馈。这使得 Claude 能够运行、通过目标或评分标准收集反馈、自我修正，并继续进行直到目标或评分标准得到满足。

![Image](https://pbs.twimg.com/media/HKYoS3maMAoXYHR?format=jpg&name=large)

我将分享一个我用来测试 Fable 的小例子：

[参数高尔夫](https://github.com/openai/parameter-golf)是一个开源的机器学习工程挑战，旨在训练一个能适配 16MB 工件且在 8 个 H100 上运行时间小于 10 分钟的最佳模型。

这有点像

[@karpathy](https://x.com/@karpathy) 的

[autoresearch](https://github.com/karpathy/autoresearch)

项目：它测试智能体编辑基础训练代码（单个 train\_gpt.py 文件）、启动训练、轮询日志、读取分数并决定下一步运行什么实验的能力。

我在这个挑战中使用

[Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview)（CMA）。CMA 提供

[代理框架以及托管沙箱](https://www.anthropic.com/engineering/managed-agents)

，因此它非常适合与 Fable 5 一起执行长时间运行的任务。对于参数高尔夫，我为 CMA 提供了对 8xH100 GPU 的访问权限，作为

[自托管沙箱](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)

。

一个微妙的点： 什么 does the judging is important。 我们发现模型在对自身输出进行自我批判时存在问题。Prithvi Rajasekaran 在我们的工程博客中对此进行了阐述，

[这里](https://www.anthropic.com/engineering/harness-design-long-running-apps) 。

![Image](https://pbs.twimg.com/media/HKYo5xEaMAAjeKL?format=jpg&name=large)

我们发现，验证器子代理

[往往表现优于](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)自我批判（使用 Fable 5），因为评分是在独立的上下文窗口中完成的。

[结果](https://platform.claude.com/docs/en/managed-agents/define-outcomes)

在 CMA 中，通过为您生成一个评分器子代理来处理这一问题。

每次测试，我提供了一份评分标准（一个文件），其中包含九个可检查的标准（例如：运行基准测试、运行 20 次实验等）。然后，我运行了 Parameter Golf 长达 8 小时。结果评估器确认所有实验标准均已满足，之后才允许 Claude 停止工作。

Fable 5 改进了训练流程，相比 Opus 4.7 提升了 ~6 倍。如果我们将实验分为结构性（例如架构变更）或标量性（例如调整常数），Fable 5 押注于更大的结构性变更，并展现出了韧性（例如，成功克服了量化回归的挑战，最终实现了最大成果）。

Opus 4.7 的首次实验取得了小幅优势，此后几乎所有步骤都遵循了相同的模板：调整一个标量，测量，若为正则保留。

内存

内存是

[Fable 表现出色的另一个领域](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) . 我们可以将其视为一个跨会话的外部循环：Claude 在会话期间向内存写入数据，这些数据可在未来的会话中被检索。

[@pgasawa](https://x.com/@pgasawa)

> 今天，我们发布了持续学习基准 1.0：首个用于衡量人工智能系统如何在在线环境中改进的真实基准。 如今的基准测试假定模型是无状态的。每个示例都是独立的，一旦系统完成一个任务，它就继续处理，仿佛...
> 
> — Parth Asawa
> 
> [https://x.com/pgasawa/status/2051361012838957144](https://x.com/pgasawa/status/2051361012838957144)
> 
> ![图片](https://pbs.twimg.com/profile_images/1781024526580715520/CgNx_SUf_x96.jpg)![Image](https://pbs.twimg.com/media/HHfibYdbgAAl6n3?format=jpg&name=large)![Download](chrome-extension://jfphcjkiccfhcmggdncpidahnkfpngfa/blueicon.jpg)

我在基准测试的其中一项任务上比较了 Fable 5、Opus 4.7 和 Sonnet 4.6：该任务要求代理在可访问 SQL 数据库的情况下回答一系列问题。每个问题对应一个独立的代理会话，并且提供了记忆功能。

为此，我使用了带有

[内存](https://platform.claude.com/docs/en/managed-agents/memory) ，这使得每个代理都能访问一个已挂载的文件系统，该文件系统可在会话间共享。

![Image](https://pbs.twimg.com/media/HKYq6HvaMAEfFJg?format=jpg&name=large)

对于这项任务，有效利用记忆得益于一个流程：失败（犯错并记录），调查（继续前进前，弄清楚原因），验证（将诊断转化为经过检验的事实），提炼（将验证转化为一般规则），以及查阅（阅读规则，而不是重新推导它）。

Sonnet 4.6 在步骤 1 附近退出：它的存储是一个包含失败记录和待验证猜测的列表（例如："maybe prc instead of prc\_usd?"）。它很少查阅先前的记录。为了提高性能，需要特定于任务的内存指令。

Opus 4.7 大约在第 3 步退出：它创建了一个带有不确定性标记的模式引用（例如：“可能是美分中的 prc？核实。”）但验证覆盖率较低：在 7-33%的问题中（中位数运行~17%）。

Fable 5 倾向于完成这一进展：在其表现最佳的运行中，验证覆盖率达到 73%（30 中 22），并将学习成果提炼为通用规则，以助力未来任务。

* * *

与其直接提示和引导 Fable 5，通常更好的做法是设计循环，让模型根据环境反馈（例如，/goal 或结果）进行自我修正，并管理自身上下文（例如，通过记忆）。

我分享了一些我做过的小规模实验，但你自己值得在挑战性任务上测试 Fable 5，并且使用循环进行自我修正或记忆处理。

要开始使用，请参阅我们的

[文档](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)或者询问最新版本的 Claude Code，它可以使用我们内置的

[/claude-api](https://github.com/anthropics/skills/tree/main/skills/claude-api)

技能来告诉您关于 Fable 5（例如，提示最佳实践）、/goal、Claude 托管代理或其他 API 功能。

* * *

### 热门回复

**@May 4** ♥ 1.2K · 💬 42

今天，我们发布了持续学习基准 1.0：首个用于衡量人工智能系统如何在在线环境中改进的真实基准。

如今的基准测试假定模型是无状态的。每个示例都是独立的，一旦系统完成一个任务，它就继续处理，仿佛...