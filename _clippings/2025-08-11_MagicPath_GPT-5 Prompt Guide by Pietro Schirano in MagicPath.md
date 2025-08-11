---
title: "GPT-5 Prompt Guide by Pietro Schirano in MagicPath"
source: "https://designs.magicpath.ai/v1/sturdy-valley-4825"
author:
  - "[[MagicPath]]"
published: 2025-08-11
created: 2025-08-11
description: "View GPT-5 Prompt Guide, a component created with MagicPath by Pietro Schirano."
tags:
  - "MagicPath 话题标签、主题标签、分类标签"
---
## GPT-5 提示指南：通用最佳实践

## Introduction

GPT-5 代表了语言模型在处理和回应提示方面的重大转变。与之前的模型不同，GPT-5 对指令结构、风格和语气特别敏感。本指南从特定于编码的行为进行推断，以提供适用于所有用例的全面提示策略。

## Core Principles

### 1\. 对指令风格的敏感性

GPT-5 对你构建提示词的方式反应非常灵敏：

- **明确语气和风格** \- 模型会强烈适应你所建立的沟通风格
- **使用一致的格式** \- 在整个提示中保持统一的结构
- **明确界定期望** \- 明确的参数能让 GPT-5 表现更佳

### 2\. 执行前的规划

当给予明确的规划阶段时，GPT-5 表现出色：

```
Before responding, please:
1. Decompose the request into core components
2. Identify any ambiguities that need clarification
3. Create a structured approach to address each component
4. Validate your understanding before proceeding
```

## 结构化提示技术

### The Spec Format

为你希望 GPT-5 遵循的任何行为定义明确的规范：

```
<task_spec>
  Definition: [What exactly you want accomplished]
  When Required: [Conditions that trigger this behavior]
  Format & Style: [How the output should be structured]
  Sequence: [Step-by-step order of operations]
  Prohibited: [What to avoid]
  Handling Ambiguity: [How to deal with unclear inputs]
</task_spec>
```

### 推理和验证步骤

在复杂提示中始终包含以下这些部分：

1. **执行前推理** ：“在开始之前，请解释你对任务的理解以及你的方法”
2. **规划阶段** ：“制定一份详细计划，明确所有子任务”
3. **验证检查点** ：“在每个主要步骤之后，验证输出是否符合要求”
4. **行动后审查** ：“在结束之前确认所有目标均已达成”

## 智能行为增强

### 完成任务解决

对于需要多个步骤或决策的任务：

```
Remember: Continue working until the entire request is fully resolved. 
- Decompose the query into ALL required sub-tasks
- Confirm each sub-task is completed before moving on
- Only conclude when you're certain the problem is fully solved
- Be prepared to handle follow-up questions without losing context
```

### 前言说明

控制 GPT-5 解释其操作的时间和方式：

**为了实现简洁而透明：**

```
Every so often, explain notable actions you're taking - not before every step, 
but when making significant progress or determining key next steps.
```

**如需详细解释：**

```
Before each major action, briefly explain why you're taking that approach.
```

## Parallel Processing

当得到正确指示时，GPT-5 可以同时处理多项任务：

```
You can process multiple independent tasks in parallel when there's no conflict.
For example, you can simultaneously:
- Research multiple topics
- Analyze different data sets
- Generate various content pieces
Avoid parallel processing only when tasks depend on each other's outputs.
```

## 不同用例的最佳实践

### 研究与分析

```
1. Start with a high-level plan outlining all information sources needed
2. Gather data comprehensively before analysis
3. Present findings in a structured format with clear sections
4. Include a summary of key insights at the beginning or end
```

### Creative Writing

```
1. Establish tone, style, and voice parameters upfront
2. Create an outline before writing
3. Maintain consistency throughout the piece
4. Review for coherence and flow before finalizing
```

### Problem-Solving

```
1. Clearly state the problem and constraints
2. Generate multiple solution approaches
3. Evaluate pros and cons of each approach
4. Recommend the optimal solution with justification
```

### Educational Content

```
1. Assess the audience's knowledge level
2. Structure information from foundational to advanced
3. Include examples and analogies
4. Provide checkpoints for understanding
```

## Advanced Techniques

### 待办事项工具实现

考虑实现一个心理待办事项列表结构：

```
Track progress with:
- [ ] Primary objective
- [ ] Sub-task 1
- [ ] Sub-task 2
- [ ] Validation step
- [ ] Final review
```

### Error Prevention

包括验证说明：

```
Before providing your final response:
1. Verify all requirements have been addressed
2. Check for internal consistency
3. Ensure the output format matches specifications
4. Confirm no prohibited elements are included
```

## 示例提示模板

```
<request>
[Your specific request here]
</request>

<instructions>
1. First, create a brief plan outlining your approach
2. Explain your reasoning for this approach
3. Execute the plan step by step
4. Validate each major output against the requirements
5. Provide a final summary confirming all objectives are met
</instructions>

<constraints>
- Verbosity: [low/medium/high]
- Style: [formal/casual/technical]
- Format: [paragraph/bullet points/structured sections]
</constraints>
```