---
title: "Claude 4 prompt engineering best practices"
source: "https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#example-formatting-preferences"
author:
  - "[[Anthropic]]"
published: 2025-07-11
created: 2025-07-11
description:
tags:
  - "clippings"
---
本指南提供了针对 Claude 4 模型（Opus 4 和 Sonnet 4）的特定提示工程技术，以帮助您在应用中获得最佳效果。与前代 Claude 模型相比，这些模型在遵循指令方面经过了更精确的训练。

## 一般原则

### 明确给出你的指令

Claude 4 模型对清晰、明确的指令响应良好。明确你想要的输出有助于提高结果。那些期望 Claude 4 展现出与之前 Claude 模型同样 “超乎预期” 表现的客户，可能需要更明确地请求这些行为。

**效果较差的：**

**更有效：**

### 添加上下文以提高性能

在你的指令背后提供背景信息或动机，比如向 Claude 解释为什么这样的行为很重要，这可以帮助 Claude 4 更好地理解你的目标并给出更有针对性的回答。

**效果较差的：**

**更有效：**

Claude 足够聪明，能够从解释中进行归纳总结。

### 对示例和细节保持警惕

Claude 4 模型在遵循指令时会关注细节和示例。确保你的示例与你想要鼓励的行为保持一致，并尽量减少你想要避免的行为。

## 特定情况的指南

### 控制回复的格式

我们发现有几种方法在引导 Claude 4 模型的输出格式方面特别有效：

1. **告诉 Claude 要做什么，而不是不要做什么**
	- 而不是：“在你的回复中不要使用 Markdown”
	- 尝试：“你的回答应由流畅的散文段落组成。”
2. **使用 XML 格式指示符**
	- 尝试：“将你回复中的散文部分写在<流畅的散文段落>标签内。”
3. **使你的提示词风格与期望的输出相匹配**
	你在提示词中使用的格式风格可能会影响 Claude 的响应风格。如果你在输出格式方面仍遇到可控性问题，我们建议尽可能使你的提示词风格与期望的输出风格相匹配。例如，从你的提示词中去除 Markdown 格式可以减少输出中的 Markdown 内容量。

### 利用思考和交错思考能力

Claude 4 具备思考能力，这对于涉及工具使用后反思或复杂多步推理的任务尤其有帮助。你可以引导它进行初始思考或交错思考，以获得更好的结果。

示例提示

有关思维能力的更多信息，请参阅 [扩展思维](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking) 。

### 优化并行工具调用

Claude 4 模型在并行工具执行方面表现出色。它们在无需任何提示的情况下进行并行工具调用时成功率很高，但一些小提示可以将这种行为提升到约 100%的并行工具使用成功率。我们发现以下提示最为有效：

智能体的示例提示

### 在智能体编码中减少文件创建

Claude 4 模型有时可能会出于测试和迭代目的创建新文件，尤其是在处理代码时。这种方法使 Claude 能够在保存最终输出之前，将文件（特别是 Python 脚本）用作“临时便签簿”。使用临时文件尤其有助于提高代理编码用例的效果。

如果你希望尽量减少新文件的创建，你可以指示 Claude 自行清理：

示例提示

### 增强视觉和前端代码生成

对于前端代码生成，你可以通过给予明确的引导，促使 Claude 4 模型创建复杂、详细且交互式的设计：

示例提示

你还可以通过提供额外的修饰词以及关于重点关注内容的详细信息，来提升 Claude 在特定领域的前端性能：

- 尽可能包含更多相关特征和交互
- 添加诸如悬停状态、过渡效果和微交互等周到的细节
- 创建一个令人印象深刻的演示，展示网页开发能力
- 应用设计原则：层次结构、对比、平衡和动感

### 避免专注于通过测试和硬编码

前沿语言模型有时可能过于专注于使测试通过，而牺牲了更通用的解决方案。为防止这种行为并确保稳健、可推广的解决方案：

示例提示

```
Please write a high quality, general purpose solution. Implement a solution that works correctly for all valid inputs, not just the test cases. Do not hard-code values or create solutions that only work for specific test inputs. Instead, implement the actual logic that solves the problem generally.

Focus on understanding the problem requirements and implementing the correct algorithm. Tests are there to verify correctness, not to define the solution. Provide a principled implementation that follows best practices and software design principles.

If the task is unreasonable or infeasible, or if any of the tests are incorrect, please tell me. The solution should be robust, maintainable, and extendable.
```

## 迁移注意事项

从 Sonnet 3.7 迁移到 Claude 4 时：

1. **明确期望的行为** ：考虑确切描述你希望在输出中看到的内容。
2. **使用修饰词来组织你的指令** ：添加鼓励 Claude 提高输出质量和细节的修饰词有助于更好地塑造 Claude 的表现。例如，不要说“创建一个分析仪表板”，而是说“创建一个分析仪表板。尽可能包含更多相关功能和交互。超越基础，创建一个功能齐全的实现。”
3. 明确请求特定功能：如有需要，应明确请求动画和交互元素。