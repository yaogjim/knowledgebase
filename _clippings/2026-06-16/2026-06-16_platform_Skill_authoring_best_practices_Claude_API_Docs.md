---
title: "2026-06-16_platform_claude_com_Skill_authoring_best_practices_Claude_API_Docs"
source: "https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices"
author:
  - "[[@platform.claude.com]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "#how"
  - "#runtime"
  - "platform"
  - "@platform.claude.com"
---

# Skill authoring best practices - Claude API Docs

优质的技能简洁明了、结构清晰，并且经过实际使用测试。本指南提供实用的创作决策，以帮助你编写 Claude 能够有效发现和使用的技能。

关于技能工作原理的概念背景，请参阅 [技能概览](/docs/en/agents-and-tools/agent-skills/overview) 。

## Core principles

### Concise is key

[上下文窗口](/docs/en/build-with-claude/context-windows) 是一种公共物品。您的技能会与 Claude 需要了解的其他所有内容共享上下文窗口，包括：

- The system prompt
- Conversation history
- Other Skills' metadata
- Your actual request

不是你的技能中的每个 token 都有即时成本。启动时，仅预加载所有技能的元数据（名称和描述）。Claude 仅在技能变得相关时才读取 SKILL.md，并且仅在需要时读取附加文件。不过，在 SKILL.md 中保持简洁仍然很重要：一旦 Claude 加载了它，每个 token 都会与对话历史和其他上下文竞争。

**默认假设：** Claude 已经非常聪明了

只添加 Claude 尚未拥有的上下文。质疑每一条信息。

- Claude 真的需要这个解释吗？
- 我可以假设 Claude 知道这个吗？
- 这段段落是否值得其 token 成本？

**好的示例：简洁** (大约 50 个 token)：

````
## Extract PDF text

Use pdfplumber for text extraction:

```python

import pdfplumber

with pdfplumber.open("file.pdf") as pdf:

 text = pdf.pages[0].extract_text()

```
````

**错误示例：过于冗长** （大约 150 tokens）：

简洁版本假设 Claude 知道什么是 PDF 以及库的工作原理。

### 设置适当的自由度

将详细程度与任务的脆弱性和变异性相匹配。

**高自由度** (基于文本的指令)：

Use when:

- Multiple approaches are valid
- Decisions depend on context
- Heuristics guide the approach

Example:

```
## Code review process

1. Analyze the code structure and organization

2. Check for potential bugs or edge cases

3. Suggest improvements for readability and maintainability

4. Verify adherence to project conventions
```

**中等自由** (伪代码或带参数的脚本):

Use when:

- A preferred pattern exists
- Some variation is acceptable
- 配置影响行为

Example:

````
## Generate report

Use this template and customize as needed:

```python

def generate_report(data, format="markdown", include_charts=True):

 # Process data

 # Generate output in specified format

 # Optionally include visualizations

```
````

**低自由度** （特定脚本，参数较少或没有参数）：

Use when:

- 操作是脆弱且容易出错的
- Consistency is critical
- 必须遵循特定的顺序

Example:

````
## Database migration

Run exactly this script:

```bash

python scripts/migrate.py --verify --backup

```

Do not modify the command or add additional flags.
````

**类比：** 把 Claude 看作一个探索路径的机器人：

- **两侧是悬崖的窄桥：** 只有一条安全的前进道路。提供具体的护栏和确切的指令（低自由度）。示例：必须按确切顺序运行的数据库迁移。
- **无危险的开放场景：** 多条路径通向成功。提供大致方向并信任 Claude 找到最佳路径（高自由度）。例如：代码审查，其中上下文决定最佳方法。

### 测试你计划使用的所有模型

技能是模型的补充，因此其有效性取决于基础模型。请用你计划使用该技能的所有模型测试你的技能。

**模型的测试注意事项**

- **Claude Haiku** (快速、经济的): 该技能是否提供了足够的指导？
- **Claude Sonnet** （平衡型）：技能是否清晰且高效？
- **Claude Opus** (强大的推理能力): 该技能是否避免过度解释？

对于 Opus 来说完美适用的内容，对于 Haiku 可能需要更多细节。如果您计划在多个模型中使用您的技能，应力求说明适用于所有模型。

## Skill structure

### Naming conventions

使用一致的命名模式，使 Skill 更容易被引用和讨论。考虑对 Skill 名称使用动名词形式 （动词 + -ing），因为这种形式能清晰地描述该 Skill 所提供的活动或功能。

请记住， `name` 字段必须仅使用小写字母、数字和连字符。

**良好的命名示例（动名词形式）**

- `processing-pdfs`
- `analyzing-spreadsheets`
- `managing-databases`
- `testing-code`
- `writing-documentation`

**Acceptable alternatives:**

- Noun phrases: `pdf-processing`, `spreadsheet-analysis`
- Action-oriented: `process-pdfs`, `analyze-spreadsheets`

**Avoid:**

- Vague names: `helper`, `utils`, `tools`
- 过于笼统： `文档` ， `数据` ， `文件`
- Reserved words: `anthropic-helper`, `claude-tools`
- 技能集合中存在不一致的模式

一致的命名使以下操作更容易：

- 文档和对话中的参考技能
- 一眼了解技能的作用
- 组织和搜索多个技能
- 维护一个专业、连贯的技能库

### 撰写有效的描述

The `description` 字段支持技能发现，并且应该包括技能的功能以及使用时机。

**具体且包含关键术语** 。既包含该 Skill 的作用，也包含使用时的具体触发条件和场景。

每个技能都有且仅有一个描述字段。描述对技能选择至关重要：Claude 会根据描述从潜在的 100 多种可用技能中选择正确的技能。你的描述必须提供足够的细节，以便 Claude 能够判断何时选择该技能，而 SKILL.md 的其余部分则提供实现细节。

Effective examples:

**PDF Processing skill:**

```
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
```

**Excel Analysis skill:**

```
description: Analyze Excel spreadsheets, create pivot tables, generate charts. Use when analyzing Excel files, spreadsheets, tabular data, or .xlsx files.
```

**Git Commit Helper skill:**

```
description: Generate descriptive commit messages by analyzing git diffs. Use when the user asks for help writing commit messages or reviewing staged changes.
```

避免像这些模糊的描述：

```
description: Helps with documents
```

```
description: Processes data
```

```
description: Does stuff with files
```

SKILL.md 作为概述文档，会根据需要指引 Claude 查阅详细资料，类似于入职指南中的目录。若需了解渐进式披露的工作原理，请参阅概述中的 [How Skills work](/docs/en/agents-and-tools/agent-skills/overview#how-skills-work) 。

**Practical guidance:**

- 为了最佳性能，保持 SKILL.md 的内容不超过 500 行
- 当接近这个限制时，将内容分割成单独的文件
- 使用以下模式来有效地组织说明、代码和资源

#### 视觉概览：从简单到复杂

一个基本的 Skill 以仅包含元数据和说明的 SKILL.md 文件开始：

![Simple SKILL.md file showing YAML frontmatter and markdown body](/docs/images/agent-skills-simple-file.png)

随着你的技能增长，你可以打包额外的内容，这些内容只有在需要时才由 Claude 加载：

![Bundling additional reference files like reference.md and forms.md.](/docs/images/agent-skills-bundling-content.png)

完整的 Skill 目录结构可能如下所示：

```
pdf/
├── SKILL.md # Main instructions (loaded when triggered)
├── FORMS.md # Form-filling guide (loaded as needed)
├── reference.md # API reference (loaded as needed)
├── examples.md # Usage examples (loaded as needed)
└── scripts/
 ├── analyze_form.py # Utility script (executed, not loaded)
 ├── fill_form.py # Form filling script
 └── validate.py # Validation script
```

#### 模式 1：高层级指南（含参考）

````
---

name: pdf-processing

description: Extracts text and tables from PDF files, fills forms, and merges documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.

---

# PDF Processing

## Quick start

Extract text with pdfplumber:

```python

import pdfplumber

with pdfplumber.open("file.pdf") as pdf:

 text = pdf.pages[0].extract_text()

```

## Advanced features

**Form filling**: See [FORMS.md](FORMS.md) for complete guide

**API reference**: See [REFERENCE.md](REFERENCE.md) for all methods

**Examples**: See [EXAMPLES.md](EXAMPLES.md) for common patterns
````

Claude 仅在需要时加载 FORMS.md、REFERENCE.md 或 EXAMPLES.md。

#### 模式 2：领域特定的组织

对于具有多个领域的技能，按领域组织内容以避免加载无关上下文。当用户询问销售指标时，Claude 只需读取与销售相关的模式，而非财务或营销数据。这能降低 token 使用量并使上下文更聚焦。

SKILL.md

````
# BigQuery Data Analysis

## Available datasets

**Finance**: Revenue, ARR, billing → See [reference/finance.md](reference/finance.md)

**Sales**: Opportunities, pipeline, accounts → See [reference/sales.md](reference/sales.md)

**Product**: API usage, features, adoption → See [reference/product.md](reference/product.md)

**Marketing**: Campaigns, attribution, email → See [reference/marketing.md](reference/marketing.md)

## Quick search

Find specific metrics using grep:

```bash

grep -i "revenue" reference/finance.md

grep -i "pipeline" reference/sales.md

grep -i "api usage" reference/product.md

```
````

#### 模式3：条件详情

显示基础内容，链接到高级内容：

```
# DOCX Processing

## Creating documents

Use docx-js for new documents. See [DOCX-JS.md](DOCX-JS.md).

## Editing documents

For simple edits, modify the XML directly.

**For tracked changes**: See [REDLINING.md](REDLINING.md)

**For OOXML details**: See [OOXML.md](OOXML.md)
```

只有当用户需要这些功能时，Claude 才会读取 REDLINING.md 或 OOXML.md。

### 避免深度嵌套的引用

当文件被其他被引用的文件引用时，Claude 可能会部分读取这些文件。当遇到嵌套引用时，Claude 可能会使用类似 `head -100` 的命令来预览内容，而不是读取整个文件，从而导致信息不完整。

保持引用与 SKILL.md 处于同一层级 。所有参考文件应直接从 SKILL.md 进行链接，以确保 Claude 在需要时能读取完整文件。

**Bad example: Too deep**:

```
# SKILL.md

See [advanced.md](advanced.md)...

# advanced.md

See [details.md](details.md)...

# details.md

Here's the actual information...
```

**Good example: One level deep**:

```
# SKILL.md

**Basic usage**: [instructions in SKILL.md]

**Advanced features**: See [advanced.md](advanced.md)

**API reference**: See [reference.md](reference.md)

**Examples**: See [examples.md](examples.md)
```

对于超过 100 行的参考文件，请在顶部包含目录。这确保了 Claude 即使在部分阅读预览时，也能查看可用信息的全部范围。

**Example:**

```
# API Reference

## Contents

- Authentication and setup

- Core methods (create, read, update, delete)

- Advanced features (batch operations, webhooks)

- Error handling patterns

- Code examples

## Authentication and setup

...

## Core methods

...
```

Claude 然后可以读取整个文件，或者按需跳转到特定部分。

有关基于文件系统的架构如何实现渐进式展示的详细信息，请参阅下面高级部分中的 [运行时环境](#runtime-environment) 部分。

### 使用工作流处理复杂任务

将复杂操作分解为清晰、按顺序的步骤。对于特别复杂的工作流程，提供一个清单，Claude 可以将其复制到响应中，并随着进展进行勾选。

**Example 1: 研究综合工作流程** (针对无代码技能):

````
## Research synthesis workflow

Copy this checklist and track your progress:

```

Research Progress:

- [ ] Step 1: Read all source documents

- [ ] Step 2: Identify key themes

- [ ] Step 3: Cross-reference claims

- [ ] Step 4: Create structured summary

- [ ] Step 5: Verify citations

```

**Step 1: Read all source documents**

Review each document in the `sources/` directory. Note the main arguments and supporting evidence.

**Step 2: Identify key themes**

Look for patterns across sources. What themes appear repeatedly? Where do sources agree or disagree?

**Step 3: Cross-reference claims**

For each major claim, verify it appears in the source material. Note which source supports each point.

**Step 4: Create structured summary**

Organize findings by theme. Include:

- Main claim

- Supporting evidence from sources

- Conflicting viewpoints (if any)

**Step 5: Verify citations**

Check that every claim references the correct source document. If citations are incomplete, return to Step 3.
````

本示例展示了工作流如何应用于不需要代码的分析任务。清单模式适用于任何复杂的多步骤流程。

**示例 2: PDF 表单填写工作流** （针对带代码的技能）:

````
## PDF form filling workflow

Copy this checklist and check off items as you complete them:

```

Task Progress:

- [ ] Step 1: Analyze the form (run analyze_form.py)

- [ ] Step 2: Create field mapping (edit fields.json)

- [ ] Step 3: Validate mapping (run validate_fields.py)

- [ ] Step 4: Fill the form (run fill_form.py)

- [ ] Step 5: Verify output (run verify_output.py)

```

**Step 1: Analyze the form**

Run: `python scripts/analyze_form.py input.pdf`

This extracts form fields and their locations, saving to `fields.json`.

**Step 2: Create field mapping**

Edit `fields.json` to add values for each field.

**Step 3: Validate mapping**

Run: `python scripts/validate_fields.py fields.json`

Fix any validation errors before continuing.

**Step 4: Fill the form**

Run: `python scripts/fill_form.py input.pdf fields.json output.pdf`

**Step 5: Verify output**

Run: `python scripts/verify_output.py output.pdf`

If verification fails, return to Step 2.
````

清晰的步骤可防止 Claude 跳过关键验证。检查清单可帮助 Claude 和您在多步骤工作流程中跟踪进度。

**常见模式：** 运行验证器 → 修复错误 → 重复

这种模式极大地提高输出质量。

**示例 1：样式指南合规性** （无代码技能）：

```
## Content review process

1. Draft your content following the guidelines in STYLE_GUIDE.md

2. Review against the checklist:

 - Check terminology consistency

 - Verify examples follow the standard format

 - Confirm all required sections are present

3. If issues found:

 - Note each issue with specific section reference

 - Revise the content

 - Review the checklist again

4. Only proceed when all requirements are met

5. Finalize and save the document
```

这展示了使用参考文档而非脚本的验证循环模式。“验证器”是 STYLE\_GUIDE.md，Claude 通过阅读和比对来执行检查。

**示例 2：文档编辑流程** （适用于包含代码的技能）：

```
## Document editing process

1. Make your edits to `word/document.xml`

2. **Validate immediately**: `python ooxml/scripts/validate.py unpacked_dir/`

3. If validation fails:

 - Review the error message carefully

 - Fix the issues in the XML

 - Run validation again

4. **Only proceed when validation passes**

5. Rebuild: `python ooxml/scripts/pack.py unpacked_dir/ output.docx`

6. Test the output document
```

验证循环能尽早捕获错误。

## Content guidelines

### 避免时效性信息

不要包含会过时的信息：

**错误示例：有时效性的** (将变为错误)：

```
If you're doing this before August 2025, use the old API.

After August 2025, use the new API.
```

**好例子** （使用"旧模式"部分）：

```
## Current method

Use the v2 API endpoint: `api.example.com/v2/messages`

## Old patterns

<details>

<summary>Legacy v1 API (deprecated 2025-08)</summary>

The v1 API used: `api.example.com/v1/messages`

This endpoint is no longer supported.

</details>
```

旧模式部分提供历史背景，而不使主要内容显得杂乱。

### Use consistent terminology

选择一个术语并在整个 Skill 中使用它：

**Good - Consistent:**

- Always "API endpoint"
- Always "field"
- Always "extract"

**Bad - Inconsistent:**

- 混合“API 端点”、“URL”、“API 路由”、“路径”
- 混合使用“字段”、“框”、“元素”、“控件”
- 混合使用 "提取"、"拉取"、"获取"、"检索"

一致性有助于 Claude 理解并遵循指令。

## Common patterns

### Template pattern

提供输出格式模板。使严格程度与您的需求相匹配。

**针对严格要求** （例如 API 响应或数据格式）：

````
## Report structure

ALWAYS use this exact template structure:

```markdown

# [Analysis Title]

## Executive summary

[One-paragraph overview of key findings]

## Key findings

- Finding 1 with supporting data

- Finding 2 with supporting data

- Finding 3 with supporting data

## Recommendations

1. Specific actionable recommendation

2. Specific actionable recommendation

```
````

**为了灵活的指导** （当适应性有用时）：

````
## Report structure

Here is a sensible default format, but use your best judgment based on the analysis:

```markdown

# [Analysis Title]

## Executive summary

[Overview]

## Key findings

[Adapt sections based on what you discover]

## Recommendations

[Tailor to the specific context]

```

Adjust sections as needed for the specific analysis type.
````

### Examples pattern

对于输出质量取决于查看示例的技能，提供输入/输出对，就像常规提示中那样：

````
## Commit message format

Generate commit messages following these examples:

**Example 1:**

Input: Added user authentication with JWT tokens

Output:

```

feat(auth): implement JWT-based authentication

Add login endpoint and token validation middleware

```

**Example 2:**

Input: Fixed bug where dates displayed incorrectly in reports

Output:

```

fix(reports): correct date formatting in timezone conversion

Use UTC timestamps consistently across report generation

```

**Example 3:**

Input: Updated dependencies and refactored error handling

Output:

```

chore: update dependencies and refactor error handling

- Upgrade lodash to 4.17.21

- Standardize error response format across endpoints

```

Follow this style: type(scope): brief description, then detailed explanation.
````

示例比仅靠描述更能帮助 Claude 清晰地理解期望的风格和详细程度。

### Conditional workflow pattern

引导 Claude 通过决策点：

```
## Document modification workflow

1. Determine the modification type:

 **Creating new content?** → Follow "Creation workflow" below

 **Editing existing content?** → Follow "Editing workflow" below

2. Creation workflow:

 - Use docx-js library

 - Build document from scratch

 - Export to .docx format

3. Editing workflow:

 - Unpack existing document

 - Modify XML directly

 - Validate after each change

 - Repack when complete
```

## Evaluation and iteration

### Build evaluations first

**在编写大量文档之前创建评估。** 这确保你的 Skill 解决实际问题，而不是记录想象中的问题。

**评估驱动的开发**

1.  识别差距: 对没有技能的代表性任务运行 Claude。记录具体失败或缺失的上下文
2.  **创建评估:** 构建三个测试这些差距的场景
3.  建立基准： 测量 Claude 在不使用该技能时的性能
4.  **编写最少的指令：** 创建恰好足够的内容以填补空白并通过评估
5.  迭代： 执行评估，与基准对比，并优化

这种方法确保你正在解决实际问题，而不是预测可能永远不会实现的需求。

**Evaluation structure:**

```
{

  "skills": ["pdf-processing"],

  "query": "Extract all text from this PDF file and save it to output.txt",

  "files": ["test-files/document.pdf"],

  "expected_behavior": [

 "Successfully reads the PDF file using an appropriate PDF processing library or command-line tool",

 "Extracts text content from all pages in the document without missing any pages",

 "Saves the extracted text to a file named output.txt in a clear, readable format"

  ]

}
```

本示例演示了使用简单测试评分标准的数据驱动评估。目前没有内置的方式来执行这些评估。用户可以创建自己的评估系统。评估是衡量技能有效性的事实依据。

### 使用 Claude 迭代地开发技能

最有效的技能开发流程涉及 Claude 本身。与一个 Claude 实例（“Claude A”）协作，创建一个供其他实例（“Claude B”）使用的技能。Claude A 帮助你设计和完善指令，而 Claude B 在实际任务中测试这些指令。这一方法有效，因为 Claude 模型既理解如何编写有效的代理指令，也理解代理所需的信息。

**Creating a new Skill:**

1.  **不使用技能完成任务：** 与 Claude A 一起使用常规提示解决一个问题。在你解决问题的过程中，你会自然地提供上下文、说明偏好并分享程序性知识。留意你反复提供的信息。
 
2.  **识别可复用模式：** 完成任务后，识别你提供的、对未来类似任务有用的上下文。
 
 **示例：** 如果你进行过 BigQuery 分析，你可能已经提供了表名、字段定义、过滤规则（比如“始终排除测试账户”）以及常见的查询模式。
 
3.  **请求 Claude A 创建一个技能：** "创建一个能够捕获我们刚刚使用的这个 BigQuery 分析模式的技能。包含表结构、命名规范以及关于过滤测试账户的规则。"
 
4.  **检查简洁性：** 检查 Claude A 没有添加不必要的解释。询问：“移除关于胜率含义的解释——Claude 已经知道这一点。”
 
5.  **改进信息架构:** 请 Claude A 更有效地组织内容。例如："组织这些内容，使表结构位于单独的参考文件中。我们稍后可能会添加更多表。"
 
6.  **在类似任务上进行测试：** 使用该技能，在相关用例上对 Claude B（一个加载了该技能的新实例）进行测试。观察 Claude B 是否能找到正确的信息、正确应用规则并成功完成任务。
 
7.  基于观察进行迭代： 如果 Claude B 遇到困难或遗漏了某些内容，需向 Claude A 反馈具体情况：“当 Claude 使用该技能时，它忘记按日期筛选 Q4 的数据。我们是否应该添加一个关于日期筛选模式的部分？”
 

**Iterating on existing Skills:**

改进技能时，同样的层次化模式会持续。你在以下方面交替进行：

- **与 Claude A 协作** (帮助优化技能的专家)
- **使用 Claude B 进行测试** (使用 Skill 执行实际工作的代理)
- **观察 Claude B 的行为** 并将见解带回给 Claude A

1.  **在真实工作流程中使用该技能：** 给加载了该技能的 Claude B 分配实际任务，而非测试场景
 
2.  **观察 Claude B 的行为：** 注意它在哪些地方遇到困难、取得成功或做出意外的选择
 
 示例观察： "当我向 Claude B 请求区域销售报告时，它生成了查询但忘记过滤掉测试账户，尽管该技能提到了这一规则。"
 
3.  **返回 Claude A 进行改进：** 分享当前的 SKILL.md 并描述你观察到的情况。询问：“我注意到，当我要求生成区域报告时，Claude B 忘记过滤测试账户。该技能提到了过滤功能，但可能不够突出？”
 
4.  **查看 Claude A 的建议：** Claude A 可能会建议重组以突出规则的重要性，使用更强烈的措辞，例如“必须过滤”而非“始终过滤”，或者重组工作流程部分。
 
5.  **应用并测试更改：** 使用 Claude A 的改进更新技能，然后使用 Claude B 对类似请求再次进行测试
 
6.  **根据使用情况重复进行：** 当你遇到新场景时，继续这个观察-优化-测试循环。每次迭代都基于真实的代理行为而非假设来改进该技能。
 

**Gathering team feedback:**

1.  与队友分享技能并观察他们的使用情况
2.  询问：技能是否在预期时激活？说明是否清晰？有什么缺失？
3.  整合反馈以解决自身使用模式中的盲点

**为什么这种方法有效：** Claude A 理解代理需求，您提供领域专业知识，Claude B 通过实际使用揭示差距，而迭代优化基于观察到的行为而非假设来改进技能。

当你迭代优化技能时，请注意 Claude 在实际应用中是如何使用这些技能的。注意以下几点：

- **意外的探索路径：** Claude 是否按你未预料到的顺序读取文件？这可能表明你的结构并不像你想的那样直观
- **连接丢失：** Claude 是否未能遵循对重要文件的引用？你的链接可能需要更明确或更突出
- **过度依赖某些部分：** 如果 Claude 反复阅读同一个文件，考虑该内容是否应该放在主 SKILL.md 中
- **Ignored content:** 如果 Claude 从未访问过捆绑文件，这可能是不必要的，或者在主要说明中信号传递不佳

基于这些观察而非假设进行迭代。技能元数据中的“名称”和“描述”尤为关键。Claude 在决定是否响应当前任务而触发该技能时会使用这些信息。确保它们清晰描述了该技能的功能以及何时应该使用它。

## Anti-patterns to avoid

### Avoid Windows-style paths

始终在文件路径中使用正斜杠，即使在 Windows 上：

- ✓ 好的：scripts/helper.py，reference/guide.md
- ✗ 避免：scripts\\helper.py，reference\\guide.md

Unix 风格路径在所有平台上都能正常工作，而 Windows 风格路径在 Unix 系统上会导致错误。

### 避免提供过多的选项

除非必要，否则不要呈现多种方法

````
**Bad example: Too many choices** (confusing):

"You can use pypdf, or pdfplumber, or PyMuPDF, or pdf2image, or..."

**Good example: Provide a default** (with escape hatch):

"Use pdfplumber for text extraction:

```python

import pdfplumber

```

For scanned PDFs requiring OCR, use pdf2image with pytesseract instead."
````

## 高级：带有可执行代码的技能

以下部分重点关注包含可执行脚本的技能。如果您的技能仅使用 markdown 指令，请跳至 [有效技能检查清单](#checklist-for-effective-skills) 。

### Solve, don't punt

在为技能编写脚本时，应处理错误情况，而不是将问题转交给 Claude。

**好例子：显式处理错误：**

```
def process_file(path):

 """Process a file, creating it if it doesn't exist."""

 try:

 with open(path) as f:

 return f.read()

 except FileNotFoundError:

 # Create file with default content instead of failing

 print(f"File {path} not found, creating default")

 with open(path, "w") as f:

 f.write("")

 return ""

 except PermissionError:

 # Provide alternative instead of failing

 print(f"Cannot access {path}, using default")

 return ""
```

**Bad example: Punt to Claude:**

```
def process_file(path):

 # Just fail and let Claude figure it out

 return open(path).read()
```

配置参数也应进行合理说明并记录，以避免“voodoo constants”（Ousterhout 定律）。如果你不知道正确的值，Claude 如何确定它？

**好例子：自文档化：**

```
# HTTP requests typically complete within 30 seconds

# Longer timeout accounts for slow connections

REQUEST_TIMEOUT = 30

# Three retries balances reliability vs speed

# Most intermittent failures resolve by the second retry

MAX_RETRIES = 3
```

**Bad example: Magic numbers:**

```
TIMEOUT = 47  # Why 47?

RETRIES = 5  # Why 5?
```

### Provide utility scripts

即使 Claude 能够编写脚本，预制脚本也具有优势：

**Benefits of utility scripts:**

- 比生成的代码更可靠
- 保存令牌（无需在上下文中包含代码）
- 节省时间（无需代码生成）
- 确保使用过程中的一致性

![Bundling executable scripts alongside instruction files](/docs/images/agent-skills-executable-scripts.png)

上图展示了可执行脚本如何与指令文件协同工作。指令文件（forms.md）引用了该脚本，且 Claude 无需将其内容加载到上下文中即可执行它。

**重要区别：** 请在你的指令中明确说明 Claude 是否应该：

- **执行脚本** (most common): "运行 `analyze_form.py` 以提取字段"
- **将其作为参考阅读** (用于复杂逻辑): "查看 `analyze_form.py` 以了解字段提取算法"

对于大多数实用脚本，执行更为可取，因为它更可靠且高效。请参阅下方的 [运行时环境](#runtime-environment) 部分，了解脚本执行原理的详细信息。

**Example:**

````
## Utility scripts

**analyze_form.py**: Extract all form fields from PDF

```bash

python scripts/analyze_form.py input.pdf > fields.json

```

Output format:

```json

{

  "field_name": {"type": "text", "x": 100, "y": 200},

  "signature": {"type": "sig", "x": 150, "y": 500}

}

```

**validate_boxes.py**: Check for overlapping bounding boxes

```bash

python scripts/validate_boxes.py fields.json

# Returns: "OK" or lists conflicts

```

**fill_form.py**: Apply field values to PDF

```bash

python scripts/fill_form.py input.pdf fields.json output.pdf

```
````

### Use visual analysis

当输入可以渲染为图像时，让 Claude 分析它们：

```
## Form layout analysis

1. Convert PDF to images:

 ```bash

 python scripts/pdf_to_images.py form.pdf

 ```

2. Analyze each page image to identify form fields

3. Claude can see field locations and types visually
```

Claude 的视觉能力有助于理解布局和结构。

### 创建可验证的中间输出

当 Claude 执行复杂、无明确边界的任务时，可能会犯错。“plan-validate-execute”（计划-验证-执行）模式通过让 Claude 首先以结构化格式制定计划，然后用脚本来验证该计划，再执行，从而提前发现错误。

**示例：** 想象让 Claude 根据电子表格更新 PDF 中的 50 个表单字段。在没有验证的情况下，Claude 可能会引用不存在的字段、创建冲突的值、遗漏必填字段或错误地应用更新。

解决方案： 使用上述的工作流模式（PDF 表单填写），但添加一个中间的 changes.json 文件，该文件在应用变更前会进行验证。工作流变为：分析 → 创建计划文件 → 验证计划 → 执行 → 验证。

**Why this pattern works:**

- **Early error detection:** 验证在应用更改之前发现问题
- **机器可验证的：** 脚本提供客观验证
- **可逆规划：** Claude can iterate the plan without altering the original
- **清晰的调试：** 错误消息指向具体问题

**适用场景：** 批量操作、破坏性变更、复杂验证规则、高风险操作。

**实施提示：** 使验证脚本详细化，包含具体的错误消息，例如“字段 'signature\_date' 未找到。可用字段：customer\_name, order\_total, signature\_date\_signed”，以帮助 Claude 解决问题。

### Package dependencies

技能在具有平台特定限制的代码执行环境中运行：

- **claude.ai:** 可以从 npm 和 PyPI 安装软件包，并从 GitHub 仓库拉取
- **Claude API:** 没有网络访问权限且没有运行时包安装

在你的 SKILL.md 中列出所需的包，并验证它们是否在 [代码执行工具文档](/docs/en/agents-and-tools/tool-use/code-execution-tool) 中可用。

### Runtime environment

技能在具备文件系统访问权限、bash 命令和代码执行能力的代码执行环境中运行。关于该架构的概念性解释，请参阅概述中的 [技能架构](/docs/en/agents-and-tools/agent-skills/overview#the-skills-architecture) 。

**这如何影响你的创作：**

**How Claude accesses Skills:**

1.  **元数据预加载：** 启动时，所有技能的 YAML 前置内容中的名称和描述被加载到系统提示中
2.  **按需读取的文件：** Claude 使用 bash 读取工具在需要时访问 SKILL.md 和文件系统中的其他文件
3.  **脚本执行高效：** 实用脚本可以通过 bash 执行，无需将其全部内容加载到上下文中。仅脚本的输出消耗 token
4.  **大文件无上下文代价：** 参考文件、数据或文档在实际被读取前不会消耗上下文 token

- **文件路径很重要：** Claude 像文件系统一样导航你的技能目录。使用正斜杠 (`reference/guide.md`)，不要使用反斜杠
- **给文件起描述性的名称：** 使用能表明内容的名称： `form_validation_rules.md` ，而非 `doc2.md`
- **为发现而组织：** 按领域或功能组织目录结构
 - Good: `reference/finance.md`, `reference/sales.md`
 - Bad: `docs/file1.md`, `docs/file2.md`
- **整合全面资源：** 包括完整的 API 文档、大量示例、大型数据集；在被访问之前无上下文惩罚
- 更倾向于使用脚本来处理确定性操作： 编写 validate\_form.py 而不是让 Claude 生成验证代码
- **Make execution intent clear:**
 - 运行 `analyze_form.py` 以提取字段 (执行)
 - 查看 `analyze_form.py` 以了解提取算法 (作为参考)
- **测试文件访问模式：** 验证 Claude 能够通过使用真实请求进行测试来浏览你的目录结构

**Example:**

```
bigquery-skill/
├── SKILL.md (overview, points to reference files)
└── reference/
 ├── finance.md (revenue metrics)
 ├── sales.md (pipeline data)
 └── product.md (usage analytics)
```

当用户询问收入时，Claude 读取 SKILL.md，看到对 `reference/finance.md` 的引用，并调用 bash 来读取该文件。sales.md 和 product.md 文件保留在文件系统中，在需要之前不消耗任何上下文令牌。这种基于文件系统的模型正是实现了渐进式披露。Claude 可以进行导航并仅选择性地加载每个任务所需的内容。

有关技术架构的完整详情，请参阅 [技能如何工作](/docs/en/agents-and-tools/agent-skills/overview#how-skills-work) 在技能概述中。

### MCP tool references

如果你的 Skill 使用 MCP（模型上下文协议）工具，始终使用完全限定的工具名称以避免"工具未找到"错误。

**Format:**`ServerName:tool_name`

**Example:**

```
Use the BigQuery:bigquery_schema tool to retrieve table schemas.

Use the GitHub:create_issue tool to create issues.
```

Where:

- `BigQuery` 和 `GitHub` 是 MCP 服务器名称
- `bigquery_schema` 和 `create_issue` 是那些服务器中的工具名称

没有服务器前缀时，Claude 可能无法定位工具，特别是当有多个 MCP 服务器可用时。

### 避免假设工具已安装

不要假设软件包是可用的：

````
**Bad example: Assumes installation**:

"Use the pdf library to process the file."

**Good example: Explicit about dependencies**:

"Install required package: `pip install pypdf`

Then use it:

```python

from pypdf import PdfReader

reader = PdfReader("file.pdf")

```"
````

## Technical notes

SKILL.md 的前置元数据需要 `name` 和 `description` 字段，且这些字段需遵循特定的验证规则：

- `name` ：最多 64 个字符，仅允许小写字母、数字和连字符，无 XML 标签，无保留词
- `description`: 最大 1024 个字符，非空，不含 XML 标签

查看 [技能概述](/docs/en/agents-and-tools/agent-skills/overview#skill-structure) 以了解完整的结构详情。

### Token budgets

将 SKILL.md 主体内容控制在 500 行以内，以获得最佳性能。如果内容超过这个数量，请使用前面描述的渐进式展开模式将其拆分为单独的文件。对于架构细节，请参阅 [Skills overview](/docs/en/agents-and-tools/agent-skills/overview#how-skills-work) 。

## 有效的技能检查清单

在分享 Skill 之前，请验证：

### Core quality

- [ ]  描述具体且包含关键术语
- [ ]  描述应包含该技能的功能以及何时使用该技能
- [ ]  SKILL.md 的正文内容不足 500 行
- [ ]  更多细节位于单独的文件中（如果需要）
- [ ]  没有时效性信息（或在“旧模式”部分）
- [ ]  贯穿始终使用一致的术语
- [ ]  示例是具体的，而非抽象的
- [ ]  文件引用的深度为一级
- [ ]  恰当使用渐进式展示
- [ ]  Workflows have clear steps

### Code and scripts

- [ ]  脚本解决问题，而不是推给 Claude
- [ ]  错误处理清晰明确且有帮助
- [ ]  不要“魔法常量”（所有值都有合理依据）
- [ ]  说明中列出的必需软件包已验证可用
- [ ]  脚本具有清晰的文档
- [ ]  禁止使用 Windows 风格的路径（全部使用正斜杠）
- [ ]  关键操作的验证/核实步骤
- [ ]  质量关键任务包含反馈循环

### Testing

- [ ]  至少三个评估已创建
- [ ]  已测试与 Haiku、Sonnet 和 Opus
- [ ]  经过真实使用场景测试
- [ ]  团队反馈已纳入（如适用）

[](/docs/en/agents-and-tools/agent-skills/quickstart)

[Get started with Agent Skills](/docs/en/agents-and-tools/agent-skills/quickstart)

[

Create your first Skill

](/docs/en/agents-and-tools/agent-skills/quickstart)[

Use Skills in Claude Code

在 Claude Code 中创建和管理技能

](https://code.claude.com/docs/en/skills)[

Use Skills in the Agent SDK

以编程方式在 TypeScript 和 Python 中使用技能

](/docs/en/agent-sdk/skills)[

Use Skills with the API

上传和以编程方式使用技能

](/docs/en/build-with-claude/skills-guide)

Was this page helpful?