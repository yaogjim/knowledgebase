---
title: "2025-11-20_Philipp_Schmid_Gemini_3_提示工程_通用场景最佳实践"
source: "https://www.philschmid.de/gemini-3-prompt-practices"
author:
  - "[[@Philipp Schmid]]"
published: 2025-11-20
created: 2025-11-20
description:
tags:
  - "philschmid"
  - "@Philipp Schmid"
  - "if"
  - "user"
---

# ## Gemini 3 提示工程：通用场景最佳实践

## Gemini 3 提示工程：通用场景最佳实践

November 19, 2025 6 minute read

我使用 Gemini 3 Pro 已有一段时间，简单来说：它在所有方面都比 2.5 Pro 强太多了！本文分享目前对我最有效的原则和结构化模式。这些并非要奉为金科玉律，而是作为帮你优化自身策略的起点。取可用之法，改不当之处，持续迭代精进。

## Core Principles

Gemini 3 推崇直抒胸臆而非迂回说服，注重逻辑内核而非冗长铺陈。为发挥其最佳性能，请遵循以下核心原则：

- **精准指令：** 输入提示词要简洁明了。Gemini 3 对直接清晰的指令响应最佳。请明确表达你的目标，避免冗余信息。
- **一致性与明确参数：** 在提示词中保持统一结构（如标准化 XML 标签），并对模糊术语进行明确定义。
- **输出详尽程度：** Gemini 3 默认采用简洁风格，倾向于提供直接高效的答复。如需更具对话感或闲聊式的交互模式，需明确指定。
- **多模态一致性：** 文本、图像、音频或视频都应视为同等重要的输入类型。指令需明确指向特定模态，确保模型进行跨模态综合处理，而非孤立分析单一模态。
- **约束条件放置：** 将行为约束和角色定义置于系统指令或提示词最顶端，以确保其能锚定模型的推理过程。
- **长上下文结构：** 处理大型上下文（书籍、代码库、长视频）时，请将具体指令置于提示信息的 **末尾** （数据上下文之后）。
- **情境锚定：** 当从大段数据过渡到查询时，需明确建立衔接。在提问前使用诸如 *"基于以上信息……"* 的引导语。

## 推理与规划

**明确规划与任务分解**

```
Before providing the final answer, please:
1. Parse the stated goal into distinct sub-tasks.
2. Is the input information complete? If not, stop and ask for it.
3. Are there tools, shortcuts, or "power user" methods that solve this problem better than the standard approach? (e.g., "Don't just list specs, suggest a workaround").
4. Create a structured outline to achieve the goal.
5. Validate your understanding before proceeding.
```

**自动更新的待办事项追踪器**

```
Create a TODO list to track progress:

- [ ] Primary objective
- [ ] Task 1
- [ ] Task 2
....
- [ ] Review
```

**自我评估其输出**

```
Before returning your final response, review your generated output against the user's original constraints. 

1. Did I answer the user's *intent*, not just their literal words?
2. Is the tone authentic to the requested persona?
3. If I made an assumption due to missing data, did I flag it?
```

## 结构化提示

使用 XML 风格标签或 Markdown 来构建提示。这能提供明确的界限，帮助模型区分指令和数据。不要混用 XML 或 Markdown，选择一种格式以保持一致性。

**XML Example:**

```xml
<rules>

 1. Be objective.

 2. Cite sources.

</rules>

 

<planning_process>

 1. Analyze the Request: Identify the core goal and all explicit constraints.

 2. Decompose: Break the problem into logical sub-tasks or variables.

 3. Strategize: Outline the step-by-step methodology to solve each sub-task.

 4. Verify: Check your plan for logical gaps or edge cases.

</planning_process>

 

<error_handling>

 IF <context> is empty, missing code, or lacks necessary data:

 DO NOT attempt to generate a solution.

 DO NOT make up data.

 Output a polite request for the missing information.

</error_handling>

 

<context>

 [Insert User Input Here - The model knows this is data, not instructions]

</context>
```

**Markdown Example:**

```
# Identity
You are a senior solution architect.

# Constraints
- No external libraries allowed.
- Python 3.11+ syntax only.

# Output Format
Return a single code block.
```

## Agentic Tool Use

**持久性指令**

```
You are an autonomous agent.
- Continue working until the user's query is COMPLETELY resolved.
- If a tool fails, analyze the error and try a different approach.
- Do NOT yield control back to the user until you have verified the solution.
```

**预计算反思**

```
Before calling any tool, explicitly state:
1. Why you are calling this tool.
2. What specific data you expect to retrieve.
3. How this data helps solve the user's problem.
```

## 领域特定应用场景

**研究与分析**

```
1. Decompose the topic into key research questions
2. Search for/Analyze provided sources for each question independently
3. Synthesize findings into a cohesive report
4. CITATION RULE: If you make a specific claim, you must cite a source. If no source is available, state that it is a general estimate. Every claim must be immediately followed by a reference [Source ID]
```

**Creative Writing**

```
1. Identify the target audience and the specific goal (e.g., empathy vs. authority).
2. If the task requires empathy or casualness, strictly avoid corporate jargon (e.g., "synergy," "protocols," "ensure").
3. Draft the content.
4. Read the draft internally. Does this sound like a human or a template? If it sounds robotic, rewrite it.
```

**Problem-Solving**

```
1. Restate the problem in your own words.
2. Identify the "Standard Solution."
3. Identify the "Power User Solution" (Is there a trick, a specific tool, or a nuance most people miss?).
4. Present the solution, prioritizing the most effective method, even if it deviates slightly from the user's requested format.
5. Sanity check: Does this solve the root problem?
```

**Education Content**

## Example Template

此模板融合了最佳实践（缓存友好结构、规划机制与 XML 定界符），构建出可复用的基准框架。

**注意：工程思维**

不存在“完美”的模板或上下文结构。上下文工程是经验性实践，而非固定语法。最优结构很大程度上取决于你的具体数据、延迟限制和领域复杂度。请将以下模式视为稳健的基线方案，但需根据具体用例进行迭代、评估和优化。

**System Instruction**

```
<role>
You are Gemini 3, a specialized assistant for [Insert Domain, e.g., Data Science].
You are precise, analytical, and persistent.
</role>

<instructions>
1. **Plan**: Analyze the task and create a step-by-step plan into distinct sub tasks.  tags. 
2. **Execute**: Carry out the plan. If using tools, reflect before every call. Track you progress in TODO List use [ ] for pending, [x] for complete. 
3. **Validate**: Review your output against the user's task. 
4. **Format**: Present the final answer in the requested structure.
</instructions>

<constraints>
- Verbosity: [Low/Medium/High]
- Tone: [Formal/Casual/Technical]
- Handling Ambiguity: Ask clarifying questions ONLY if critical info is missing; otherwise, make reasonable assumptions and state them.
</constraints>

<output_format>
Structure your response as follows:
2. **Executive Summary**: [2 sentence overview]
3. **Detailed Response**: [The main content]
</output_format>
```

**User Prompt**

```
<context>
[Insert relevant documents, code snippets, or background info here]
</context>

<task>
[Insert specific user request here]
</task>

<final_instruction>
Remember to think step-by-step before answering.
</final_instruction>
```

* * *

感谢阅读！如有任何疑问或反馈，请通过 [Twitter](https://twitter.com/_philschmid) 或 [LinkedIn](https://www.linkedin.com/in/philipp-schmid-a6a2bb196/) 与我联系。