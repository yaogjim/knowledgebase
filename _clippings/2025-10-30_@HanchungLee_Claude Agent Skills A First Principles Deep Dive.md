---
title: "Claude Agent Skills: A First Principles Deep Dive"
source: "https://leehanchung.github.io/blogs/2025/10/26/claude-skills-deep-dive/"
author:
  - "[[@HanchungLee]]"
published: 2025-10-30
created: 2025-10-30
description: "Technical deep dive into Claude Agent Skills' prompt-based meta-tool architecture. Learn how context injection design, two-message patterns, LLM-based routin..."
tags:
  - "@HanchungLee"
---
Claude 的智能体 `技能` 系统代表了一种基于提示词的精妙元工具架构，通过专业化指令注入来扩展 LLM 能力。与传统函数调用或代码执行不同， ` 技能` 通过\*\*提示词扩展\*\*和\*\*上下文修改\*\*来运作，无需编写可执行代码即可改变 Claude 处理后续请求的方式。

本次深度解析从第一性原理出发，拆解了 Claude 智能体 `技能` 系统的架构，重点阐述了名为“ `  技能  ` ”的工具如何作为元工具，将领域特定的提示词注入对话上下文的运作机制。我们将以 `技能创建器` 和 `内部通信` 技能为案例，完整走查其生命周期——从文件解析到 API 请求结构，再到 Claude 的决策流程。

## Claude 智能体技能概览

Claude 通过 `  技能  ` 来提升特定任务的执行效果。 `  技能  ` 被定义为包含指令、脚本和资源的文件夹，Claude 可在需要时加载这些内容。Claude 采用一套 **声明式的、基于提示的系统** 来实现技能发现与调用。人工智能模型（Claude）会根据系统提示中呈现的文本描述，自行决定是否调用 `  技能  ` 。 **代码层面并不存在算法驱动的 `  技能  ` 选择或人工智能驱动的意图检测** ，所有决策完全基于所提供的技能描述，在 Claude 的推理过程中完成。

`技能` 并非可执行代码。它们 **不会** 运行 Python 或 JavaScript，背后也没有 HTTP 服务器或函数调用的过程。这些技能也并非硬编码在 Claude 的系统提示中。 ` 技能` 存在于 API 请求结构的独立部分。

那么它们究竟是什么呢？ ` 技能` 是专门化的提示模板，能够向对话上下文注入特定领域的指令。当技能被调用时，它既会修改对话上下文（通过注入指令提示），也会改变执行上下文（通过调整工具权限并可能切换模型）。技能并非直接执行操作，而是扩展为详细的提示信息，让 Claude 为解决特定类型的问题做好准备。每个技能在 Claude 可见的工具模式中，都表现为动态新增的功能模块。

当用户发送请求时，Claude 会接收到三样东西：用户消息、可用工具（如读取、写入、Bash 等）以及 `技能` 工具。 ` 技能` 工具的描述包含一个格式化列表，其中汇总了每个可用技能的 `名称 ` 、 ` 描述` 等字段。Claude 会读取该列表，并运用其自然语言理解能力将用户意图与技能描述进行匹配。例如当用户说“帮我创建日志技能”时，Claude 会看到 `内部通讯` 技能描述（“当用户需要按照公司惯用格式撰写内部通讯时使用”），识别出匹配项后，便会以 `指令："internal-comms"` 的参数调用 `技能` 工具。

> **Terminology Note**:
> 
> - **`Skill` 工具** （大写 S）= 用于管理所有技能的元工具。它出现在 Claude 的 `tools` 工具数组中，与 Read、Write、Bash 等工具并列。
> - **技能** （小写 s）= 如 `pdf` 、 `skill-creator` 、 `internal-comms` 等独立技能。这些是 `Skill` 工具加载的专用指令模板。

以下是关于 Claude 如何使用 `技能` 的更直观展示。

![Claude Skill Flowchart](https://leehanchung.github.io/assets/img/2025-10-26/01-claude-skill-1.png)

技能选择机制在代码层面没有算法路由或意图分类。Claude Code 不使用嵌入向量、分类器或模式匹配来决定调用哪个技能。相反，系统将所有可用技能格式化成文本描述，嵌入到 `Skill` 工具的提示中，让 Claude 的语言模型自行决策。这是纯粹的 LLM 推理过程——没有正则表达式，没有关键词匹配，没有基于机器学习的意图检测。决策发生在 Claude 的前向传播过程中，而非应用程序代码里。

当 Claude 调用技能时，系统遵循一个简单的工作流程：加载 Markdown 文件（ `SKILL.md` ），将其展开为详细指令，将这些指令作为新用户消息注入对话上下文，修改执行上下文（允许使用的工具、模型选择），并在这个增强的环境中继续对话。这与传统工具执行后返回结果的方式存在根本区别。技能的作用是 *让 Claude 做好准备* 来解决问题，而非直接解决问题。

以下表格有助于更清晰地区分工具与技能及其能力之间的差异：

| Aspect | Traditional Tools | Skills |
| --- | --- | --- |
| **Execution Model** | Synchronous, direct | Prompt expansion |
| **Purpose** | 执行特定操作 | 指导复杂工作流程 |
| **Return Value** | Immediate results | 对话上下文与执行上下文的变更 |
| **Example** | `Read`, `Write`, `Bash` | `internal-comms`, `skill-creator` |
| **Concurrency** | Generally safe | 非并发安全 |
| **Type** | Various | Always `"prompt"` |

## 构建智能体技能

现在让我们通过研究 Anthropic 技能代码仓库中的 [`skill-creator` 技能](https://github.com/anthropics/skills/tree/main/skill-creator) 作为案例，深入探讨如何构建技能。需要说明的是，智能体 `技能` 是由指令、脚本和资源组成的结构化文件夹，智能体能够动态发现并加载这些内容，从而在特定任务中表现更出色。 ` 技能` 通过将您的专业知识打包成可组合的资源供 Claude 使用，从而扩展其能力，将通用智能体转化为符合您需求的专用智能体。

> **关键洞察** ：技能 = 提示模板 + 对话上下文注入 + 执行上下文修改 + 可选数据文件和 Python 脚本

每个 `技能` 都定义在名为 `SKILL.md` （不区分大小写）的 markdown 文件中，并附带可选的捆绑文件，这些文件存储在 `/scripts` 、 `/references` 和 `/assets` 目录下。这些捆绑文件可以是 Python 脚本、Shell 脚本、字体定义、模板等。以 `skill-creator` 为例，它包含 `SILL.md` 、许可证文件 `LICENSE.txt` ，以及 `/scripts` 文件夹下的若干 Python 脚本。 `skill-creator` 没有 `/references` 或 `/assets` 目录。

![skill-creator package](https://leehanchung.github.io/assets/img/2025-10-26/03-claude-skill-package.png)

技能可从多个来源发现并加载。Claude Code 会扫描用户设置（ `~/.config/claude/skills/` ）、项目设置（`.claude/skills/` ）、插件提供的技能以及内置技能，从而构建可用技能列表。对于 Claude Desktop，我们可以通过以下方式上传自定义技能。

![Claude Desktop Skill](https://leehanchung.github.io/assets/img/2025-10-26/02-claude-desktop-skill.png)

> **注意：** 构建技能最重要的概念是 **渐进式披露** ——仅展示足够信息帮助智能体决定下一步行动，待其需要时再逐步揭示更多细节。就 `智能体技能` 而言，它
> 
> 1. 披露前置元数据：最小化（名称、描述、许可证）
> 2. 如果选择了 `技能 ` ，则加载 SKILL.md：内容全面但重点突出
> 3. 然后在执行 `技能` 时加载辅助资源、引用和脚本

## Writing SKILL.md

`SKILL.md` 是技能提示的核心文件。该 Markdown 文件采用双部分结构——前言和内容。前言配置技能运行的方式（权限、模型、元数据），而 Markdown 内容则告知 Claude 需要执行的任务。 [前言](https://docs.github.com/en/contributing/writing-for-github-docs/using-yaml-frontmatter) 是采用 YAML 格式编写的 Markdown 文件头部信息。

```
┌─────────────────────────────────────┐
│ 1. YAML Frontmatter (Metadata)      │ ← Configuration
│    ---                              │
│    name: skill-name                 │
│    description: Brief overview      │
│    allowed-tools: "Bash, Read"      │
│    version: 1.0.0                   │
│    ---                              │
├─────────────────────────────────────┤
│ 2. Markdown Content (Instructions)  │ ← Prompt for Claude
│                                     │
│    Purpose explanation              │
│    Detailed instructions            │
│    Examples and guidelines          │
│    Step-by-step procedures          │
└─────────────────────────────────────┘
```

前置元数据包含了控制 Claude 如何发现和使用技能的元信息。例如，这是 `skill-creator` 中的前置元数据：

让我们逐一梳理前言部分的各个字段。

![Claude Skills Frontmatter](https://leehanchung.github.io/assets/img/2025-10-26/04-claude-skill-frontmatter.png)

#### name (Required)

顾名思义，这是 `技能` 的名称。 ` 技能` 的 `名称` 在 `技能工具` 中作为 `指令` 使用。

> `name` 是 `skill` 在 `Skill Tool` 中作为 `command` 使用的名称。

#### description (Required)

`description` 字段提供了对该技能功能的简要概述。这是 Claude 用于判断何时调用技能的主要依据。在上例中，描述明确说明“当用户想要创建新技能时应使用此技能”——这类清晰、以行动为导向的表述有助于 Claude 将用户意图与技能能力进行匹配。

系统会自动在描述后附加来源信息（例如 `"(plugin:skills)"` ），这有助于在加载多个技能时区分不同来源的技能。

#### 何时使用 （未记录——可能已弃用或为未来功能）

> **⚠️ 重要提示** ： `when_to_use` 字段在代码库中广泛出现，但 **未在任何官方 Anthropic 文档中记载** 。该字段可能具有以下特性：
> 
> - 一项正在逐步淘汰的过时功能
> - 一项内部/实验性功能，尚未获得官方支持
> - 一项尚未发布的计划功能
> 
> **建议** ：请依赖详细的 `description` 字段。在官方文档明确说明前，请勿在生产技能中使用 `when_to_use` 参数。

尽管没有相关文档，以下是代码库中 `when_to_use` 功能的当前实现方式：

```javascript
function formatSkill(skill) {
  let description = skill.whenToUse
    ? \`${skill.description} - ${skill.whenToUse}\`
    : skill.description;

  return \`"${skill.name}": ${description}\`;
}
```

当存在时， `when_to_use` 会以连字符分隔符的形式附加到描述之后。例如：

```
"skill-creator": Create well-structured, reusable skills... - When user wants to build a custom skill package with scripts, references, or assets
```

这个组合字符串就是 Claude 在技能工具提示中看到的内容。但由于该行为未在文档中记录，未来版本中可能会更改或移除。更稳妥的做法是直接将使用指南包含在 `description` 字段中，如上文 `skill-creator` 示例所示。

Self explanatory.

#### allowed-tools (Optional)

`allowed-tools` 字段定义了技能无需用户批准即可使用的工具，类似于 Claude 的 allowed-tools 设置。

这是一个逗号分隔的字符串，会被解析成允许使用的工具名称数组。您可以使用通配符来限定权限范围，例如 `Bash(git:*)` 仅允许 git 子命令，而 `Bash(npm:*)` 则允许所有 npm 操作。skill-creator 技能使用 `"Read,Write,Bash,Glob,Grep,Edit"` 来赋予其广泛的文件和搜索能力。常见的错误是列出所有可用工具，这会带来安全风险并破坏安全模型。

> 仅包含技能实际所需内容——若仅涉及读写文件， `"读取,写入"` 便已足够。

```yaml
# ✅ skill-creator allows multiple tools
allowed-tools: "Read,Write,Bash,Glob,Grep,Edit"

# ✅ Specific git commands only
allowed-tools: "Bash(git status:*),Bash(git diff:*),Bash(git log:*),Read,Grep"

# ✅ File operations only
allowed-tools: "Read,Write,Edit,Glob,Grep"

# ❌ Unnecessary surface area
allowed-tools: "Bash,Read,Write,Edit,Glob,Grep,WebSearch,Task,Agent"

# ❌ Unnecessary surface area with all npm commands
allowed-tools: "Bash(npm:*),Read,Write"
```

#### model (Optional)

`model` 字段定义了技能可使用的模型，默认继承用户会话中的当前模型。对于代码审查等复杂任务，技能可请求调用更强大的模型，例如 Claude Opus 或其他开源中文模型。懂的都懂。

```yaml
model: "claude-opus-4-20250514"  # Use specific model
model: "inherit"                 # Use session's current model (default)
```

#### 版本 、 禁用模型调用和模式 （可选）

技能支持三个可选的前置元数据字段，用于版本控制和调用管理。 `version` 字段（例如 version: “1.0.0”）作为元数据字段用于追踪技能版本，该字段虽从前置元数据中解析，但主要服务于文档记录和技能管理用途。

`disable-model-invocation` 字段（布尔类型）可阻止 Claude 通过 `Skill` 工具自动调用该技能。当设置为 true 时，该技能将从展示给 Claude 的列表中排除，仅能由用户通过 \`/技能名称\` 手动触发，这使其特别适用于危险操作、配置命令或需要显式用户控制的交互式工作流。

`mode` 字段（布尔类型）将技能归类为“模式命令”，这类命令会修改 Claude 的行为或上下文环境。当设置为 true 时，该技能会出现在技能列表顶部的特殊“模式命令”区域（与常规工具技能分开显示），使得诸如调试模式、专家模式或评审模式这类建立特定操作环境或工作流的技能能够更加突出。

### 技能.md 提示内容

前导内容之后是 Markdown 内容——即调用 ` 技能` 时 Claude 接收到的实际提示。这里定义了 ` 技能` 的行为、指令和工作流程。编写高效技能提示的关键在于保持聚焦并采用渐进式呈现：在 SKILL.md 中提供核心指令，详细内容则引用外部文件。

以下是推荐的内容结构

```markdown
---
# Frontmatter here
---

# [Brief Purpose Statement - 1-2 sentences]

## Overview
[What this skill does, when to use it, what it provides]

## Prerequisites
[Required tools, files, or context]

## Instructions

### Step 1: [First Action]
[Imperative instructions]
[Examples if needed]

### Step 2: [Next Action]
[Imperative instructions]

### Step 3: [Final Action]
[Imperative instructions]

## Output Format
[How to structure results]

## Error Handling
[What to do when things fail]

## Examples
[Concrete usage examples]

## Resources
[Reference scripts/, references/, assets/ if bundled]
```

例如， `skill-creator` 技能包含以下指令，详细说明了创建技能所需工作流程的每个步骤。

```markdown
## Skill Creation Process

### Step 1: Understanding the Skill with Concrete Examples
### Step 2: Planning the Reusable Skill Contents
### Step 3: Initializing the Skill
### Step 4: Edit the Skill
### Step 5: Packaging a Skill
```

当 Claude 调用此技能时，它会接收到完整提示作为新指令，并在其前附加基础目录路径。 `{baseDir}` 变量将解析为技能的安装目录，使 Claude 能够通过读取工具加载参考文件： `Read({baseDir}/scripts/init_skill.py)` 。这种模式既保持了主提示的简洁性，又能按需获取详细文档。

**提示内容的最佳实践**

- 内容控制在5,000字（约800行）以内，避免信息过载
- 使用祈使语气（“分析代码以…”），而非第二人称（“你应该分析…”）
- 参考外部文件以获取详细内容，而非全部内嵌
- 使用 `{baseDir}` 作为路径，切勿硬编码绝对路径，例如 `/home/user/project/`
```markdown
❌ Read /home/user/project/config.json
✅ Read {baseDir}/config.json
```

当技能被调用时，Claude 仅能访问 `allowed-tools` 中指定的工具，若前置元数据中有定义，模型配置也可能被覆盖。技能的基础目录路径会自动提供，使得捆绑资源可供访问。

### 将资源与您的技能捆绑打包

当您将支持资源与 SKILL.md 文件捆绑使用时， ` 技能` 将变得强大。标准结构采用三个目录，每个目录都有特定用途：

```
my-skill/
├── SKILL.md              # Core prompt and instructions
├── scripts/              # Executable Python/Bash scripts
├── references/           # Documentation loaded into context
└── assets/               # Templates and binary files
```

**为何要打包资源？** 保持 SKILL.md 简洁（不超过 5000 字）可避免超出 Claude 上下文窗口的承载极限。打包资源能让您在不过度膨胀主提示词的前提下，提供详细的文档、自动化脚本和模板。Claude 会通过渐进式披露机制，仅在需要时加载这些资源。

#### The scripts/ Directory

`scripts/` 目录包含由 Claude 通过 Bash 工具运行的可执行代码——这些自动化脚本、数据处理器、验证器或代码生成器执行确定性操作。

例如， `skill-creator` 的 SKILL.md 文件会这样引用脚本：

```markdown
When creating a new skill from scratch, always run the \`init_skill.py\` script. The script conveniently generates a new template skill directory that automatically includes everything a skill requires, making the skill creation process much more efficient and reliable.

Usage:

\`\`\`scripts/init_skill.py <skill-name> --path <output-directory>\`\`\`

The script:
  - Creates the skill directory at the specified path
  - Generates a SKILL.md template with proper frontmatter and TODO placeholders
  - Creates example resource directories: scripts/, references/, and assets/
  - Adds example files in each directory that can be customized or deleted
```

当 Claude 看到这条指令时，它会执行 `python {baseDir}/scripts/init_skill.py` 。 `{baseDir}` 变量会自动解析为技能的安装路径，这使得技能能够在不同环境中实现便携部署。

**使用 scripts/ 目录处理** 复杂的多步骤操作、数据转换、API 交互，或任何需要精确逻辑且更适合用代码而非自然语言表达的任务。

#### The references/ Directory

`references/` 目录存储着被引用时 Claude 会读入上下文的文档。这些是文本内容——包括 Markdown 文件、JSON 模式、配置模板，或任何 Claude 完成任务所需的文档。

例如， `mcp-creator` 的 SKILL.md 参考引用如下所示：

```markdown
#### 1.4 Study Framework Documentation

**Load and read the following reference files:**

- **MCP Best Practices**: [📋 View Best Practices](./reference/mcp_best_practices.md) - Core guidelines for all MCP servers

**For Python implementations, also load:**
- **Python SDK Documentation**: Use WebFetch to load \`https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md\`
- [🐍 Python Implementation Guide](./reference/python_mcp_server.md) - Python-specific best practices and examples

**For Node/TypeScript implementations, also load:**
- **TypeScript SDK Documentation**: Use WebFetch to load \`https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/README.md\`
- [⚡ TypeScript Implementation Guide](./reference/node_mcp_server.md) - Node/TypeScript-specific best practices and examples
```

当 Claude 遇到这些指令时，会使用 Read 工具： `Read({baseDir}/references/mcp_best_practices.md)` 。相关内容将被载入 Claude 的上下文，既提供了详细信息，又避免了 SKILL.md 文件的冗余。

**使用 references/ 目录存放** 详细文档、大型模式库、检查清单、API 架构说明，或任何在 SKILL.md 中过于冗长但对任务必要的文本内容。

#### The assets/ Directory

`assets/` 目录包含模板和二进制文件，Claude 会通过路径引用这些文件但不会将其加载到上下文中。可以将其视为技能的静态资源——HTML 模板、CSS 文件、图像、配置样板或字体。

In SKILL.md:

```markdown
Use the template at {baseDir}/assets/report-template.html as the report structure.
Reference the architecture diagram at {baseDir}/assets/diagram.png.
```

Claude 能看到文件路径但不会读取内容。相反，它可能会将模板复制到新位置、填充占位符，或在生成的输出中引用该路径。

**使用 assets/ 目录存放** HTML/CSS 模板、图像、二进制文件、配置模板，或任何 Claude 通过路径操作而非读入上下文的文件。

`references/` 与 `assets/` 之间的关键区别在于

- **references/** ：通过读取工具加载到 Claude 上下文中的文本内容
- **assets/** ：仅通过路径引用的文件，未加载到上下文中

这种区分对上下文管理至关重要。存放在 `references/` 目录下的 10KB Markdown 文件被载入时会消耗上下文令牌，而存放在 `assets/` 目录下的 10KB HTML 模板则不会。Claude 仅知晓该路径存在。

> **最佳实践：** 始终使用 `{baseDir}` 作为路径基准，切勿硬编码绝对路径。这能确保技能在不同用户环境、项目目录及安装路径间具备可移植性。

### 常见技能模式

如同工程领域的一切，理解常见模式有助于设计出高效的技能。以下是工具集成与工作流设计中最实用的模式。

#### 模式一：脚本自动化

**使用场景：** 需要执行多个命令或确定性逻辑的复杂操作。

这种模式将计算任务卸载到 `scripts/` 目录中的 Python 或 Bash 脚本。技能提示会指示 Claude 执行脚本并处理其输出。

![Claude Skill Script Automation](https://leehanchung.github.io/assets/img/2025-10-26/09-script-automation.png)

**SKILL.md example:**

```markdown
Run scripts/analyzer.py on the target directory:

\`python {baseDir}/scripts/analyzer.py --path "$USER_PATH" --output report.json\`

Parse the generated \`report.json\` and present findings.
```

**Required tools:**

```yaml
allowed-tools: "Bash(python {baseDir}/scripts/*:*), Read, Write"
```

#### 模式二：读取—处理—写入

**用例：** 文件转换与数据处理。

最简单的模式——读取输入，按照指令进行转换，然后输出结果。适用于格式转换、数据清理或报告生成等场景。

![Claude Skill Read Process Write](https://leehanchung.github.io/assets/img/2025-10-26/10-read-process-write.png)

**SKILL.md example:**

```markdown
## Processing Workflow
1. Read input file using Read tool
2. Parse content according to format
3. Transform data following specifications
4. Write output using Write tool
5. Report completion with summary
```

**Required tools:**

```yaml
allowed-tools: "Read, Write"
```

**使用场景：** 代码库分析与模式识别。

使用 Grep 在代码库中搜索模式，阅读匹配文件以获取上下文，分析发现并生成结构化报告。或者，在企业数据存储中搜索数据，分析检索到的信息并生成结构化报告。

![Claude Skill Search Analyze Report](https://leehanchung.github.io/assets/img/2025-10-26/06-search-analyze-report.png)

**SKILL.md example:**

```markdown
## Analysis Process
1. Use Grep to find relevant code patterns
2. Read each matched file
3. Analyze for vulnerabilities
4. Generate structured report
```

**Required tools:**

```yaml
allowed-tools: "Grep, Read"
```

#### 模式四：命令链执行

**使用场景：** 具有依赖关系的多步骤操作。

执行一系列命令，其中每个步骤的成功都依赖于前一步的完成。常见于类似 CI/CD 的工作流程。

![Claude Skill Command Chain Execution](https://leehanchung.github.io/assets/img/2025-10-26/05-command-chain-execution.png)

**SKILL.md example:**

```markdown
Execute analysis pipeline:
npm install && npm run lint && npm test

Report results from each stage.
```

**Required tools:**

```yaml
allowed-tools: "Bash(npm install:*), Bash(npm run:*), Read"
```

### Advanced Patterns

#### 巫师风格多步骤工作流程

**使用场景：** 需要用户在每一步都提供输入的复杂流程。

将复杂任务分解为多个独立步骤，并在每个阶段之间设置明确用户确认环节。适用于设置向导、配置工具或引导式流程。

**SKILL.md example:**

```markdown
## Workflow

### Step 1: Initial Setup
1. Ask user for project type
2. Validate prerequisites exist
3. Create base configuration
Wait for user confirmation before proceeding.

### Step 2: Configuration
1. Present configuration options
2. Ask user to choose settings
3. Generate config file
Wait for user confirmation before proceeding.

### Step 3: Initialization
1. Run initialization scripts
2. Verify setup successful
3. Report results
```

#### 基于模板的生成

**使用场景：** 从存储在 `assets/` 目录中的模板创建结构化输出。

加载模板，使用用户提供或生成的数据填充占位符，并输出结果。常用于报告生成、样板代码创建或文档编写。

**SKILL.md example:**

```markdown
## Generation Process
1. Read template from {baseDir}/assets/template.html
2. Parse user requirements
3. Fill template placeholders:
   -  → user-provided name
   -  → generated summary
   -  → current date
4. Write filled template to output file
5. Report completion
```

#### 迭代优化

**用例：** 需要多次逐步深入处理的过程。

先进行广泛分析，再针对已识别问题逐步深入探究。适用于代码审查、安全审计或质量分析场景。

**SKILL.md example:**

```markdown
## Iterative Analysis

### Pass 1: Broad Scan
1. Search entire codebase for patterns
2. Identify high-level issues
3. Categorize findings

### Pass 2: Deep Analysis
For each high-level issue:
1. Read full file context
2. Analyze root cause
3. Determine severity

### Pass 3: Recommendation
For each finding:
1. Research best practices
2. Generate specific fix
3. Estimate effort

Present final report with all findings and recommendations.
```

#### Context Aggregation

**使用场景：** 整合多方信息以构建全面理解。

从不同文件和工具中收集数据，整合成连贯的整体视图。适用于项目总结、依赖关系分析或影响评估。

**SKILL.md example:**

```markdown
## Context Gathering
1. Read project README.md for overview
2. Analyze package.json for dependencies
3. Grep codebase for specific patterns
4. Check git history for recent changes
5. Synthesize findings into coherent summary
```

## 代理技能内部架构

在概述和构建过程介绍完毕后，我们现在可以深入探究技能的实际运作原理。该技能系统通过元工具架构运行，其中名为 `Skill` 的工具作为所有独立技能的容器和调度器。这种设计从实现方式和用途上，将技能与传统工具进行了根本性区分。

> `技能` 工具是一个管理所有技能的元工具

## 技能对象设计

传统工具如 `读取 ` 、 `Bash` 或 `写入` 执行的是离散操作并立即返回结果。技能的工作方式则不同——它们并非直接执行操作，而是向对话历史中注入专用指令，并动态修改 Claude 的执行环境。这一过程通过两条用户消息实现：一条包含用户可见的元数据，另一条则包含对用户界面隐藏但会发送给 Claude 的完整技能提示；同时还会通过调整智能体的上下文来变更权限、切换模型，并在技能使用期间动态调节思维令牌参数。

![Claude Skill Execution Flow](https://leehanchung.github.io/assets/img/2025-10-26/08-claude-skill-execution-flow.png)

| Feature | Normal Tool | Skill Tool |
| --- | --- | --- |
| **Essence** | 直接行动执行器 | 提示注入 + 上下文修改器 |
| **Message Role** | 助手 → 工具使用   用户 → 工具结果 | 助手 → 工具使用技能   用户 → 工具结果   用户 → 技能提示 ← 已注入！ |
| **Complexity** | 简单（3-4条消息） | 复杂（5-10条以上消息） |
| **Context** | Static | 动态（每回合调整） |
| **Persistence** | 仅限工具交互 | 工具交互 + 技能提示 |
| **Token Overhead** | 最小化（约100个词元） | 每轮显著（约1500+个标记） |
| **Use Case** | 简单直接的任务 | 复杂、引导式工作流程 |

复杂性相当显著。普通工具仅生成简单的消息交换——一次助手工具调用后接用户结果。而技能则注入多条消息，在动态修改的上下文中运行，并需承担可观的令牌开销，以此提供专门指导 Claude 行为的指令。

理解 `Skill` 元工具的工作原理，便能揭示该系统的运行机制。让我们来剖析其结构：

```javascript
Pd = {
  name: "Skill",  // The tool name constant: $N = "Skill"

  inputSchema: {
    command: string  // E.g., "pdf", "skill-creator"
  },

  outputSchema: {
    success: boolean,
    commandName: string
  },

  // 🔑 KEY FIELD: This generates the skills list
  prompt: async () => fN2(),

  // Validation and execution
  validateInput: async (input, context) => { /* 5 error codes */ },
  checkPermissions: async (input, context) => { /* allow/deny/ask */ },
  call: async *(input, context) => { /* yields messages + context modifier */ }
}
```

`prompt` 字段将技能工具与 `Read` 或 `Bash` 等具有静态描述的工具区分开来。技能工具不使用固定字符串，而是采用动态提示生成器，通过聚合所有可用技能的名称和描述在运行时构建其描述。这实现了 **渐进式披露** ——系统仅将最小元数据（来自 frontmatter 的技能名称和描述）加载到 Claude 的初始上下文中，为模型提供刚好足够的信息来判断哪个技能符合用户意图。完整的技能提示仅在 Claude 做出选择后加载，既避免了上下文膨胀，又保持了可发现性。

```javascript
async function fN2() {
  let A = await atA(),
    {
      modeCommands: B,
      limitedRegularCommands: Q
    } = vN2(A),
    G = [...B, ...Q].map((W) => W.userFacingName()).join(", ");
  l(\`Skills and commands included in Skill tool: ${G}\`);
  let Z = A.length - B.length,
    Y = nS6(B),
    J = aS6(Q, Z);
  return \`Execute a skill within the main conversation

<skills_instructions>
When users ask you to perform tasks, check if any of the available skills below can help complete the task more effectively. Skills provide specialized capabilities and domain knowledge.

How to use skills:
- Invoke skills using this tool with the skill name only (no arguments)
- When you invoke a skill, you will see <command-message>The "{name}" skill is loading</command-message>
- The skill's prompt will expand and provide detailed instructions on how to complete the task
- Examples:
  - \\`command: "pdf"\\` - invoke the pdf skill
  - \\`command: "xlsx"\\` - invoke the xlsx skill
  - \\`command: "ms-office-suite:pdf"\\` - invoke using fully qualified name

Important:
- Only use skills listed in <available_skills> below
- Do not invoke a skill that is already running
- Do not use this tool for built-in CLI commands (like /help, /clear, etc.)
</skills_instructions>

<available_skills>
${Y}${J}
</available_skills>
\`;
}
```

与某些工具（如 ChatGPT 助手）将功能置于系统提示中的做法不同，Claude **的智能体技能并不存在于系统提示中** 。它们作为 `Skill` 工具描述的一部分，存放在 `tools` 数组中。具体技能的名称通过 `Skill` 元工具的输入模式中的 `command` 字段来体现。为更直观地展示其结构，以下是实际的 API 请求示例：

```json
{
  "model": "claude-sonnet-4-5-20250929",
  "system": "You are Claude Code, Anthropic's official CLI...",  // ← System prompt
  "messages": [
    {"role": "user", "content": "Help me create a new skill"},
    // ... conversation history
  ],
  "tools": [  // ← Tools array sent to Claude
    {
      "name": "Skill",  // ← The meta-tool
      "description": "Execute a skill...\n\n<skills_instructions>...\n\n<available_skills>\n...",
      "input_schema": {
        "type": "object",
        "properties": {
          "command": {
            "type": "string",
            "description": "The skill name (no arguments)"  // ← Name of individual skill
          }
        }
      }
    },
    {
      "name": "Bash",
      "description": "Execute bash commands...",
      // ...
    },
    {
      "name": "Read",
      // ...
    }
    // ... other tools
  ]
}
```

`<available_skills>` 部分位于技能工具描述中，并在每次 API 请求时重新生成。系统通过动态聚合来自用户和项目配置的当前加载技能、插件提供的技能以及任何内置技能来构建此列表，默认情况下受限于 15,000 个字符的令牌预算。此预算限制迫使技能作者编写简洁的描述，并确保工具描述不会超出模型的上下文窗口容量。

## 技能对话与执行上下文注入设计

大多数 LLM API 支持理论上可承载系统提示的 `role: "system"` 消息。实际上，OpenAI 的 ChatGPT 就在其系统提示中内置了默认工具集，包括用于记忆的 `bio` 、任务调度的 `automations` 、画布控制的 `canmore` 、图像生成的 `img_gen` ，以及 `file_search` 、 `python` 和用于网络搜索的 `web` 。最终这些工具提示会占据系统提示中约 90%的令牌数量。虽然这种设计有一定实用性，但当我们需要载入大量工具或技能到上下文时，其效率显然不尽如人意。

然而，系统消息具有不同的语义特性，使其不适用于技能设定。系统消息用于设置贯穿整个对话的全局上下文，其权威性高于用户指令，会影响后续所有交互轮次。

技能需要临时的、有范围限制的行为。 `skill-creator` 技能应仅影响技能创建相关任务，而不会将 Claude 转变为当前会话中永久的 PDF 专家。使用 `role: "user"` 配合 `isMeta: true` 可使技能提示以用户输入的形式呈现给 Claude，从而保持其临时性并局限于当前交互。技能执行完毕后，对话将恢复正常会话上下文和执行上下文，不会残留行为修改。

像 `读取 ` 、 ` 写入` 或 `Bash` 这类常规工具具有简单的通信模式。当 Claude 调用 `读取` 工具时，它发送文件路径、接收文件内容后继续工作。用户会在对话记录中看到“Claude 使用了读取工具”，这种透明度就足够了。工具执行单一操作并返回结果，交互就此结束。而技能的工作机制则截然不同——它们并非执行独立操作后返回结果，而是注入完整的指令集来改变 Claude 对任务的思考和处理方式。这带来了常规工具从未面临的设计挑战：用户需要了解正在运行的技能及其具体作用，而 Claude 则需要详尽（甚至可能冗长）的指令来正确执行技能。若在聊天记录中完整显示技能提示，界面将被数千字的内置 AI 指令淹没；若完全隐藏技能激活状态，用户又将失去对系统代其执行操作的可见性。 解决方案要求将这两个通信渠道分离为具有不同可见性规则的独立消息。

技能系统通过每条消息上的 `isMeta` 标志来控制其是否在用户界面中显示。当 `isMeta: false` 时（或标志被省略默认值为 false 时），消息会呈现在用户可见的对话记录中。而当 `isMeta: true` 时，消息会作为 Claude 对话上下文的一部分发送至 Anthropic API，但绝不会出现在用户界面中。这个简单的布尔标志实现了精妙的双通道通信：一条流向人类用户，另一条流向 AI 模型。这正是为元工具设计的元提示技术！

当技能执行时，系统会向对话历史中注入两条独立的用户消息。第一条携带技能元数据，其中包含 `isMeta: false` 参数，使其作为状态指示器对用户可见。第二条则携带完整技能提示，包含 `isMeta: true` 参数，在界面上隐藏该内容的同时仍可供 Claude 调用。这种分离设计通过向用户展示运行状态而非繁琐的实现细节，巧妙解决了透明度与界面简洁性之间的权衡问题。

元数据消息采用简洁的 XML 结构，前端可解析并正确显示：

```javascript
let metadata = [
  \`<command-message>${statusMessage}</command-message>\`,
  \`<command-name>${skillName}</command-name>\`,
  args ? \`<command-args>${args}</command-args>\` : null
].filter(Boolean).join('\n');

// Message 1: NO isMeta flag → defaults to false → VISIBLE
messages.push({
  content: metadata,
  autocheckpoint: checkpointFlag
});
```

当 PDF 技能激活时，例如，用户会在他们的对话记录中看到一个简洁的加载指示器

```xml
<command-message>The "pdf" skill is loading</command-message>
<command-name>pdf</command-name>
<command-args>report.pdf</command-args>
```

此消息特意保持简洁，通常为 50 到 200 个字符。XML 标签使前端能够以特殊格式渲染内容，验证是否存在正确的 `<command-message>` 标签，并维护会话期间执行技能的审计追踪。由于省略时 `isMeta` 标志默认为 false，这些元数据会自动显示在用户界面中。

技能提示信息则采用相反的方法。它从 `SKILL.md` 加载完整内容，可能还会用额外上下文进行增强，并明确设置 `isMeta: true` 以对用户隐藏：

```javascript
let skillPrompt = await skill.getPromptForCommand(args, context);

// Augment with prepend/append content if needed
let fullPrompt = prependContent.length > 0 || appendContent.length > 0
  ? [...prependContent, ...appendContent, ...skillPrompt]
  : skillPrompt;

// Message 2: Explicit isMeta: true → HIDDEN
messages.push({
  content: fullPrompt,
  isMeta: true  // HIDDEN FROM UI, SENT TO API
});
```

典型技能提示词长度在 500 到 5000 词之间，通过全面指导来改变 Claude 的行为模式。PDF 技能提示词可能包含：

```markdown
You are a PDF processing specialist.

Your task is to extract text from PDF documents using the pdftotext tool.

## Process

1. Validate the PDF file exists
2. Run pdftotext command to extract text
3. Read the output file
4. Present the extracted text to the user

## Tools Available

You have access to:
- Bash(pdftotext:*) - For running pdftotext command
- Read - For reading extracted text
- Write - For saving results if needed

## Output Format

Present the extracted text clearly formatted.

Base directory: /path/to/skill
User arguments: report.pdf
```

此提示设定了任务背景，勾勒了工作流程，明确了可用工具，定义了输出格式，并提供了环境特定的路径。采用包含标题、列表和代码块的 Markdown 结构，有助于 Claude 解析并遵循指令。通过 `isMeta: true` 的设置，整个提示内容会发送至 API 接口，但不会在用户对话记录中造成杂乱显示。

除了核心元数据和技能提示外，技能还能为附件和权限注入额外的条件性消息

```javascript
let allMessages = [
  createMessage({ content: metadata, autocheckpoint: flag }),  // 1. Metadata
  createMessage({ content: skillPrompt, isMeta: true }),       // 2. Skill prompt
  ...attachmentMessages,                                       // 3. Attachments (conditional)
  ...(allowedTools.length || skill.model ? [
    createPermissionsMessage({                                 // 4. Permissions (conditional)
      type: "command_permissions",
      allowedTools: allowedTools,
      model: skill.useSmallFastModel ? getFastModel() : skill.model
    })
  ] : [])
];
```

附件消息可携带诊断信息、文件引用或补充技能提示的额外上下文。权限消息仅在技能的前置元数据中指定 `allowed-tools` 或请求模型覆写时出现，提供用于修改运行时执行环境的元数据。这种模块化组合使每条消息都能具备特定用途，并根据技能配置决定是否包含，从而将基础的双消息模式扩展至更复杂的场景，同时通过 `isMeta` 标记保持相同的可见性控制。

### 为何是两条消息而非一条？

单条消息的设计会迫使人们做出不可能的选择。若将 `isMeta: false` 设置为可见状态，整条消息内容将完全暴露，导致数千字的人工智能指令涌入用户聊天记录。用户会看到类似这样的内容：

```
┌─────────────────────────────────────────────┐
│ The "pdf" skill is loading                  │
│                                             │
│ You are a PDF processing specialist.        │
│                                             │
│ Your task is to extract text from PDF       │
│ documents using the pdftotext tool.         │
│                                             │
│ ## Process                                  │
│                                             │
│ 1. Validate the PDF file exists             │
│ 2. Run pdftotext command to extract text    │
│ 3. Read the output file                     │
│ ... [500 more lines] ...                    │
└─────────────────────────────────────────────┘
```

用户界面变得无法使用，充斥着本为 Claude 而非人类准备的内部实现细节。或者，设置 `isMeta: true` 会隐藏所有内容，完全不透明地展示哪个技能被激活或接收了哪些参数。用户将无法了解系统正在代表他们执行什么操作。

双消息分离机制通过为每条消息赋予不同的 `isMeta` 值来解决这个问题。第一条消息设置 `isMeta: false` 实现面向用户的透明度，第二条消息设置 `isMeta: true` 则为 Claude 提供详细指令。这种精细化的控制既保证了透明度，又避免了信息过载。

这些信息面向的受众和目的也截然不同：

| Aspect | Metadata Message | 技能提示信息 |
| --- | --- | --- |
| **Audience** | Human user | Claude (AI) |
| **Purpose** | Status/transparency | 指示/指导 |
| **Length** | ~50-200 chars | ~500-5,000 words |
| **Format** | Structured XML | 自然语言标记语言 |
| **Visibility** | Should be visible | Should be hidden |
| **Content** | “发生什么事了？” | “该怎么做？” |

代码库甚至通过不同的路径处理这些消息。元数据消息会被解析其中的 \` `<command-message>` \` 标签，经过验证并格式化以供界面显示。而技能提示消息则直接发送至 API，无需解析或验证——这是仅供 Claude 推理过程使用的原始指令内容。若将两者合并，将迫使同一条消息通过两种不同的处理流程服务于两个不同的受众群体，这违背了单一职责原则。

## 案例研究：执行生命周期

在介绍了智能体技能的内部架构之后，现在让我们通过一个假设的 `pdf` 技能作为案例研究，通过完整的执行流程来解析当用户提出“从 report.pdf 中提取文本”时会发生什么。

![Claude Skill Execution Flow](https://leehanchung.github.io/assets/img/2025-10-26/07-claude-skill-sequence-diagram.png)

当 Claude Code 启动时，它会扫描技能：

```javascript
async function getAllCommands() {
  // Load from all sources in parallel
  let [userCommands, skillsAndPlugins, pluginCommands, builtins] =
    await Promise.all([
      loadUserCommands(),      // ~/.claude/commands/
      loadSkills(),            // .claude/skills/ + plugins
      loadPluginCommands(),    // Plugin-defined commands
      getBuiltinCommands()     // Hardcoded commands
    ]);

  return [...userCommands, ...skillsAndPlugins, ...pluginCommands, ...builtins]
    .filter(cmd => cmd.isEnabled());
}

// Specific skill loading
async function loadPluginSkills(plugin) {
  // Check if plugin has skills
  if (!plugin.skillsPath) return [];

  // Two patterns supported:
  // 1. Root SKILL.md in skillsPath
  // 2. Subdirectories with SKILL.md

  const skillFiles = findSkillMdFiles(plugin.skillsPath);
  const skills = [];

  for (const file of skillFiles) {
    const content = readFile(file);
    const { frontmatter, markdown } = parseFrontmatter(content);

    skills.push({
      type: "prompt",
      name: \`${plugin.name}:${getSkillName(file)}\`,
      description: \`${frontmatter.description} (plugin:${plugin.name})\`,
      whenToUse: frontmatter.when_to_use,  // ← Note: underscores!
      allowedTools: parseTools(frontmatter['allowed-tools']),
      model: frontmatter.model === "inherit" ? undefined : frontmatter.model,
      isSkill: true,
      promptContent: markdown,
      // ... other fields
    });
  }

  return skills;
}
```

对于 PDF 技能，这会产生：

```javascript
{
  type: "prompt",
  name: "pdf",
  description: "Extract text from PDF documents (plugin:document-tools)",
  whenToUse: "When user wants to extract or process text from PDF files",
  allowedTools: ["Bash(pdftotext:*)", "Read", "Write"],
  model: undefined,  // Uses session model
  isSkill: true,
  disableModelInvocation: false,
  promptContent: "You are a PDF processing specialist...",
  // ... other fields
}
```

### 第二阶段：第一回合 - 用户请求与技能选择

用户发送请求：“从 report.pdf 中提取文本”。Claude 接收到此消息时，其工具数组中包含 `Skill` 工具。在 Claude 决定调用 pdf 技能之前，系统必须在 Skill 工具的描述中展示可用的技能。

#### 技能筛选与展示

并非所有加载的技能都会显示在技能工具中。技能必须在前置元数据中包含 `description` 或 `when_to_use` ，否则将被过滤掉。过滤标准：

```javascript
async function getSkillsForSkillTool() {
  const allCommands = await getAllCommands();

  return allCommands.filter(cmd =>
    cmd.type === "prompt" &&
    cmd.isSkill === true &&
    !cmd.disableModelInvocation &&
    (cmd.source !== "builtin" || cmd.isModeCommand === true) &&
    (cmd.hasUserSpecifiedDescription || cmd.whenToUse)  // ← Must have one!
  );
}
```

#### Skill Formatting

每项技能都按照 `<available_skills>` 部分的格式进行编排。例如，我们假设的 `pdf` 技能可被格式化为  
`"pdf": Extract text from PDF documents - When user wants to extract or process text from PDF files`

```javascript
function formatSkill(skill) {
  let name = skill.name;
  let description = skill.whenToUse
    ? \`${skill.description} - ${skill.whenToUse}\`
    : skill.description;

  return \`"${name}": ${description}\`;
}
```

#### 克劳德的决策过程

现在，当用户提示：“从 report.pdf 中提取文本”。Claude 接收到带有 `技能` 工具的 API 请求，读取 `<available_skills>` ，并进行推理（假设性地，因为我们看不到推理痕迹）：

```
Internal reasoning:
- User wants to "extract text from report.pdf"
- This is a PDF processing task
- Looking at available skills...
- "pdf": Extract text from PDF documents - When user wants to extract or process text from PDF files
- This matches! The user wants to extract text from a PDF
- Decision: Invoke Skill tool with command="pdf"
```

需要注意的是，这里并不涉及算法匹配。没有词汇匹配，没有语义匹配，也没有搜索过程。这完全是 LLM 基于技能描述进行纯推理后做出的决策。完成后，Claude 会返回一个工具调用结果：

```json
{
  "type": "tool_use",
  "id": "toolu_123abc",
  "name": "Skill",
  "input": {
    "command": "pdf"
  }
}
```

### 第三阶段：技能工具执行

技能工具现已开始执行。这对应序列图中黄色的“技能工具执行”框，该环节会执行验证、权限检查、文件加载和上下文修改等操作，最终生成结果。

#### Step 1: Validation

```javascript
async validateInput({ command }, context) {
  let skillName = command.trim().replace(/^\//, "");

  // Error 1: Empty
  if (!skillName) return { result: false, errorCode: 1 };

  // Error 2: Unknown skill
  const allSkills = await getAllCommands();
  if (!skillExists(skillName, allSkills)) {
    return { result: false, errorCode: 2 };
  }

  // Error 3: Can't load
  const skill = getSkill(skillName, allSkills);
  if (!skill) return { result: false, errorCode: 3 };

  // Error 4: Model invocation disabled
  if (skill.disableModelInvocation) {
    return { result: false, errorCode: 4 };
  }

  // Error 5: Not prompt-based
  if (skill.type !== "prompt") {
    return { result: false, errorCode: 5 };
  }

  return { result: true };
}
```

该 PDF 技能通过了所有验证检查 ✓

```javascript
async checkPermissions({ command }, context) {
  const skillName = command.trim().replace(/^\//, "");
  const permContext = (await context.getAppState()).toolPermissionContext;

  // Check deny rules
  for (const [pattern, rule] of getDenyRules(permContext)) {
    if (matches(skillName, pattern)) {
      return { behavior: "deny", message: "Blocked by permission rules" };
    }
  }

  // Check allow rules
  for (const [pattern, rule] of getAllowRules(permContext)) {
    if (matches(skillName, pattern)) {
      return { behavior: "allow" };
    }
  }

  // Default: ask user
  return { behavior: "ask", message: \`Execute skill: ${skillName}\` };
}
```

假设无规则限制，用户被提示：“执行技能：pdf？”  
用户已批准 ✓

#### 第三步：加载技能文件并生成执行上下文修改

验证和权限通过后，技能工具将加载技能文件并准备执行上下文修改：

```javascript
async *call({ command }, context) {
  const skillName = command.trim().replace(/^\//, "");
  const allSkills = await getAllCommands();
  const skill = getSkill(skillName, allSkills);

  // Load the skill prompt
  const promptContent = await skill.getPromptForCommand("", context);

  // Generate metadata tags
  const metadata = [
    \`<command-message>The "${skill.userFacingName()}" skill is loading</command-message>\`,
    \`<command-name>${skill.userFacingName()}</command-name>\`
  ].join('\n');

  // Create messages
  const messages = [
    { type: "user", content: metadata },  // Visible to user
    { type: "user", content: promptContent, isMeta: true },  // Hidden from user, visible to Claude
    // ... attachments, permissions
  ];

  // Extract configuration
  const allowedTools = skill.allowedTools || [];
  const modelOverride = skill.model;

  // Yield result with execution context modifier
  yield {
    type: "result",
    data: { success: true, commandName: skillName },
    newMessages: messages,

    // 🔑 Execution context modification function
    contextModifier(context) {
      let modified = context;

      // Inject allowed tools
      if (allowedTools.length > 0) {
        modified = {
          ...modified,
          async getAppState() {
            const state = await context.getAppState();
            return {
              ...state,
              toolPermissionContext: {
                ...state.toolPermissionContext,
                alwaysAllowRules: {
                  ...state.toolPermissionContext.alwaysAllowRules,
                  command: [
                    ...state.toolPermissionContext.alwaysAllowRules.command || [],
                    ...allowedTools  // ← Pre-approve these tools
                  ]
                }
              }
            };
          }
        };
      }

      // Override model
      if (modelOverride) {
        modified = {
          ...modified,
          options: {
            ...modified.options,
            mainLoopModel: modelOverride
          }
        };
      }

      return modified;
    }
  };
}
```

技能工具产生的结果包含 `newMessages` （元数据+技能提示+对话上下文注入权限）和 `contextModifier` （工具权限+执行上下文修改的模型覆写）。这完成了序列图中黄色的“技能工具执行”框。

### 第四阶段：发送至 API（第一轮完成）

系统构建完整的消息数组以发送至 Anthropic API，包含对话中的所有消息及新注入的技能消息：

```javascript
// Complete message array sent to API for Turn 1
{
  model: "claude-sonnet-4-5-20250929",
  messages: [
    {
      role: "user",
      content: "Extract text from report.pdf"
    },
    {
      role: "assistant",
      content: [
        {
          type: "tool_use",
          id: "toolu_123abc",
          name: "Skill",
          input: { command: "pdf" }
        }
      ]
    },
    {
      role: "user",
      content: "<command-message>The \"pdf\" skill is loading</command-message>\n<command-name>pdf</command-name>"
      // isMeta: false (default) - VISIBLE to user in UI
    },
    {
      role: "user",
      content: "You are a PDF processing specialist...\n\n## Process\n1. Validate PDF exists\n2. Run pdftotext...",
      isMeta: true  // HIDDEN from UI, sent to API
    },
    {
      role: "user",
      content: {
        type: "command_permissions",
        allowedTools: ["Bash(pdftotext:*)", "Read", "Write"],
        model: undefined
      }
    }
  ]
}
```

![Turn 1 Completion](https://leehanchung.github.io/assets/img/2025-10-26/11-turn-1-completion.png)

以上展示了我们到目前为止完成的工作。执行上下文修饰符已应用，预先批准了后续工具调用中的 `Bash(pdftotext:*)` 、 `Read` 和 `Write` 操作。该请求随后被发送至 Anthropic API。至此技能执行阶段结束。若这是普通工具，整个流程便已完成。但技能有所不同——智能体技能仅注入了对话上下文和执行上下文。这意味着我们仍需调用注入了全部上下文的 Claude 智能体来完成用户请求！

### 第五阶段：Bash 工具执行（结合技能情境使用工具！）

Claude 接收到包含注入对话上下文的 API 响应。技能提示已改变了 Claude 的行为，为其提供了：

- 专业 PDF 处理说明（对话上下文）
- 预先批准对 `Bash(pdftotext:*)` 、 `  读取  ` 和 `  写入  ` 工具（执行上下文）的访问权限
- 一个清晰可遵循的工作流程（对话上下文）

Claude 处理上下文并遵循 PDF 技能的工作流程：

```
I'll extract text from report.pdf. Let me process the file.

[Following pdf skill's instructions]
1. Validate that report.pdf exists
2. Run pdftotext command to extract text
3. Read the output file
4. Present the extracted text to you
```

Claude 使用 Bash 工具（已预授权，无需用户提示）：

```json
{
  "type": "tool_use",
  "id": "toolu_456def",
  "name": "Bash",
  "input": {
    "command": "pdftotext report.pdf output.txt",
    "description": "Extract text from PDF using pdftotext"
  }
}
```

Bash 工具成功执行并返回结果。随后，Claude 通过 Read 工具读取输出文件，并将提取的文本呈现给用户。该技能通过向对话上下文注入指令并修改工具权限的执行上下文，成功引导 Claude 完成了专业 PDF 提取工作流。

---

## 结论：心智模型回顾

Claude Code 中的技能是 **基于提示的对话与执行上下文修改器** ，它们通过元工具架构实现功能：

**Key Takeaways:**

1. 技能是 `SKILL.md` 文件中的 **提示模板** ，而非可执行代码。
2. **Skill 工具** （首字母大写）是 `tools` 数组中用于管理独立技能（而非系统提示中）的元工具
3. 技能通过注入指令提示（通过 `isMeta: true` 消息）来 **修改对话上下文**
4. 技能通过改变工具权限和模型选择来 **调整执行上下文**
5. 选择通过 **LLM 推理** 实现，而非算法匹配
6. 工具权限通过执行上下文修改 **限定在技能执行范围内**
7. 每次调用技能时，会注入两条用户消息：一条是用户可见的元数据，另一条是发送给 API 的隐藏指令

**优雅设计：** 通过将专业知识视为 *修改对话上下文的提示* 和 *修改执行上下文的权限* ，而非 *执行的代码* ，Claude Code 实现了传统函数调用难以企及的灵活性、安全性和可组合性。

---

## References

- [介绍代理技能](https://www.anthropic.com/news/skills)
- [为现实世界配备智能体技能](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- [Claude 代码文档](https://docs.claude.com/en/docs/claude-code/overview)
- [Anthropic API 参考文档](https://docs.anthropic.com/en/api/messages)
- [官方文档记录的前置元数据字段](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview#skill-structure)
- [内部沟通技能](https://github.com/anthropics/skills/tree/main/internal-comms)
- [Skill Creator Skill](https://github.com/anthropics/skills/tree/main/skill-creator)
- [ChatGPT 5 系统提示（泄露版，非官方）](https://github.com/elder-plinius/CL4R1T4S/blob/main/OPENAI/ChatGPT5-08-07-2025.mkd)
```
@article{
    leehanchung_bullshit_jobs,
    author = {Lee, Hanchung},
    title = {Claude Agent Skills: A First Principles Deep Dive},
    year = {2025},
    month = {10},
    day = {26},
    howpublished = {\url{https://leehanchung.github.io}},
    url = {https://leehanchung.github.io/blogs/2025/10/26/claude-skills-deep-dive/}
}
```