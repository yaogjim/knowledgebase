---
title: ""
source: "https://x.com/rohit4verse/status/2021622526112358663"
author: ""
created: 2026-02-13 17:56:01
date: 2026-02-13 17:56:01
description: ""
tags: ""
---
将 AI 视为通用聊天机器人的时代已正式结束。虽然 99%的用户仍在编写基础提示词，但顶尖的 1%用户正在培养技能。这就是拥有一个玩具和拥有一个专业的、全天候工作的员工之间的区别。

但要实现这一点，你需要停止编写提示词，转而运用技能开始交付代码。

这是关于新技能标准的完整技术指南。 由 Anthropic 于 2025 年 10 月推出，技能不仅仅是指令，而是动态、有组织的软件包，允许代理按需加载上下文。它曾是独家功能，现已演变为开放标准，包括 OpenAI 和 Microsoft 在内的主要平台均采用了该规范，以及像 Vercel 的 CLI 这样的工具，让全球开发者都能轻松进行技能管理。

与传统的函数调用或代码执行不同，技能通过复杂的提示词扩展和上下文修改来发挥作用，它们教会智能体如何思考和解决问题，而不是简单地执行预定义的函数。

```
your-skill-name/
├── SKILL.md              # Required - main skill file
├── scripts/              # Optional - executable code
│   ├── process_data.py
│   └── validate.sh
├── references/           # Optional - documentation
│   ├── api-guide.md
│   └── examples/
└── assets/               # Optional - templates, fonts, icons
    └── report-template.md
```

每一项技能的核心是

文件，该文件包含用于元数据的 YAML 前置内容和用于说明的 Markdown 内容：

```
---
name: project-workspace-setup
description: Automates complete project workspace creation including pages, databases, and templates. Use when user asks to "set up a new project", "create a workspace", or "initialize a project structure".
---

# Project Workspace Setup

## Instructions
[Step-by-step guidance for Claude to follow]

## Examples
[Concrete usage scenarios]

## Troubleshooting
[Common issues and solutions]
```

这些技能非常简单且设计有目的性，这使得非开发人员也能轻松使用这些技能，同时又足够可靠以支持企业级部署。

理解技能的内部运作机制对于构建有效的技能至关重要。根据深入的技术分析，技能代表着一种基于提示的元工具架构，其运作机制与传统 AI 工具有着根本的不同。

1 级 - YAML front matter（始终加载）： 技能名称和描述被注入到 Claude 的系统提示中。这提供了足够的信息，让 Claude 能够决定何时加载完整技能，而不会消耗不必要的 token。

2 级 -

正文（相关时加载）： 当 Claude 确定某个技能相关时，它会从 Markdown 正文中加载完整的指令。其中包含详细的分步指导、示例和最佳实践。

3 级 - 关联资源（按需加载）： 在 scripts/、references/和 assets/目录中的额外文件仅在特定需要时才会被访问，进一步减少令牌使用。

这种渐进式披露方法意味着，技能可以极其详细而不会让上下文窗口不堪重负。Claude 只会在需要的时候加载它所需的内容。

技能最巧妙的一个方面是它们如何处理可见性。当 Claude 激活一项技能时，系统会发送两种类型的消息：

-   用户可见消息 (isMeta: false): 这些出现在对话记录中
    
-   meta messages (isMeta: true): these contain the full skill instructions and are sent to claude's api but never shown to users
    

这种分离解决了一个关键的用户体验问题：用户需要了解哪些技能正在运行，但他们不需要看到数千字的技术说明杂乱地充斥在他们的聊天界面中。

在编写任何代码之前，确定2-3个你的技能应该处理的具体场景。最常见的类别有：

类别 1: 文档 & 资产创建 用于创建一致、高质量的输出，例如文档、演示文稿或设计作品。示例：前端设计技能能够生成专业的网页界面，而非通用的 AI 劣质内容。

类别 2: 工作流自动化 受益于一致方法的多步骤流程。例如：引导用户构建新技能的 skill-creator 技能。

类别 3: MCP 增强 在模型上下文协议（MCP）服务器集成的基础上提供工作流指导。例如：Sentry 的代码审查技能，该技能能够利用错误监控数据自动分析并修复 GitHub 拉取请求中的缺陷。

-   触发准确率： 技能应在 90%的相关查询中加载
    
-   工具效率： 通过 X 次工具调用完成工作流（与基准相比）
    
-   错误率: 每个工作流零次失败的 API 调用
    
-   一致性： 相同任务在不同会话中产生相似结果
    

描述字段至关重要，这是 Claude 用来决定何时加载你的技能的依据。使用此结构：

```
[What it does] + [When to use it] + [Key capabilities]

Good Example:

description: Analyzes Figma design files and generates developer handoff documentation. Use when user uploads .fig files, asks for "design specs", "component documentation", or "design-to-code handoff".

Bad Example:
description: Helps with projects.
```

包含用户实际会说的触发短语，提及相关的文件类型，并明确说明该技能解决什么问题。

```
---
name: your-skill
description: [Clear, specific description]
---

# Your Skill Name

## Instructions
Step 1: [First major step with clear explanation]
Step 2: [Second major step]
...

## Examples
Example 1: [Common scenario]
User says: "Set up a new marketing campaign"
Actions:
1. Fetch existing campaigns via MCP
2. Create new campaign with provided parameters
Result: Campaign created with confirmation link

## Troubleshooting
Error: [Common error message]
Cause: [Why it happens]
Solution: [How to fix]
```

最有效的方法是针对单一的挑战性任务进行迭代，直到 Claude 成功，然后将该方法提取为你的技能。测试：

-   触发： 它是否在应该加载的时候加载？它是否避免误报？
    
-   功能： 是否能持续产生正确的输出？
    
-   表现： 是否优于基准水平（无技能）？
    

2026 年初，Vercel 发布了

一个命令行工具，已成为 AI 代理的 npm。这个 CLI 工具帮助在不同 AI 平台上安装和管理技能。

```
# Install a skill from GitHub
npx skills add vercel-labs/agent-skills

# Install a specific skill from a repo
npx skills add vercel-labs/agent-skills@vercel-react-best-practices

# Install from a direct path
npx skills add https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines

# List installed skills
npx skills list

# Check for updates
npx skills check

# Update all skills
npx skills update
```

该

CLI 自动检测你已安装的哪些 AI 编码代理，并适当地配置技能。目前它支持 35+个代理，包括 Claude 代码、cursor、codex、open code、windsurf 等多种代理。

该平台包括基于安装遥测数据的受欢迎度排名、按使用场景分类的浏览功能、用于查找相关技能的搜索功能以及用于一键安装的直接安装链接

当被要求创建一个着陆页时，Claude 编写的代码如果没有前端设计技能，会生成一个看起来通用的结果，功能齐全但明显是 AI 生成的。然而，当具备了这些技能后，同样的任务会产出一个专业、现代的网站，具有复杂的设计模式、适当的间距和当代的 UI 元素。

这说明了一个关键原则：技能编码超出 Claude 训练数据的专业知识。前端设计技能包含来自专业设计师的色彩理论、布局原则和可访问性指南等提炼智慧，这些内容被包装为过程性知识。

Anthropic 的 PowerPoint、Excel、Word 和 PDF 预构建技能展示了企业级能力。这些技能能够：

-   品牌一致性： 自动应用企业风格指南
    
-   模板遵循: 遵循组织文档结构
    
-   公式智能: 生成复杂的 Excel 公式
    
-   PDF 表单填写： 通过编程方式完成可填写的 PDF 表单
    

使用这些技能的组织报告称，之前需要30多分钟的任务现在能在3分钟内完成。

```
Phase 1: Design Export (Figma MCP)
- Export design assets from Figma
- Generate design specifications
- Create asset manifest

Phase 2: Asset Storage (Google Drive MCP)
- Create project folder
- Upload all assets
- Generate shareable links

Phase 3: Task Creation (Linear MCP)
- Create development tasks
- Attach asset links to tasks
- Assign to engineering team

Phase 4: Notification (Slack MCP)
- Post handoff summary
- Include asset links and task references
```

一个编排此工作流的技能消除了人工协调的需要，确保步骤按正确顺序执行，并自动处理错误恢复。

```
Decision Tree:
1. Check file type and size
2. Determine best storage:
   - Large files (>10MB): Cloud storage MCP
   - Collaborative docs: Notion/Docs MCP
   - Code files: GitHub MCP
   - Temporary files: Local storage
3. Execute with appropriate tool
4. Explain choice to user
```

```
Before Processing (Compliance Check):
1. Fetch transaction details via MCP
2. Apply compliance rules:
   - Check sanctions lists
   - Verify jurisdiction allowances
   - Assess risk level
3. Document compliance decision

Processing:
IF compliance passed:
  - Process transaction
  - Apply fraud checks
ELSE:
  - Flag for review
  - Create compliance case
```

这融入了 Claude 本身并不固有具备的监管专业知识。

```
Initial Draft:
- Generate first version
- Save to temporary file

Quality Check:
- Run validation script
- Identify issues

Refinement Loop:
- Address each issue
- Regenerate affected sections
- Re-validate
- Repeat until quality threshold met
```

这种模式对于文档生成、代码审查和数据分析特别有效。

技能非常强大，它们可以执行代码并调用工具。这种能力需要谨慎的安全考量：

Anthropic 强烈建议仅使用来自可信来源的技能：

-   Anthropic 创建的技能: 专业维护和验证
    
-   自主创建的技能： 你控制代码
    
-   合作伙伴技能： 来自经过验证的商业合作伙伴
    

社区技能在安装前应进行审查，因为恶意技能可能会引导 Claude 执行意外操作。

-   Claude 代码: 完全网络访问但在用户的机器上本地运行
    
-   API: 在具有可配置权限的代码执行容器中运行
    

YAML frontmatter 可以指定 allowed-tools 来限制技能可以访问的 API：

```
allowed-tools: "Bash(python:*) Bash(npm:*) WebFetch"
```

人工智能行业正将重心从原始模型能力转向实际应用价值。

技能代表了从令人印象深刻的演示转向能够交付可衡量业务价值的生产工作流这一演进。

1\. 技能作为竞争差异化因素 拥有完善技能库的公司将具备生产力优势。先行企业正将内部技能库建设为战略资产。

2\. 技能市场 我们已经看到类似应用商店的商业技能市场正在兴起，在这些市场中，专业技能可以被购买以用于特定行业或使用场景。

3\. 人工智能辅助的技能创建 技能创建技能展示了人工智能构建人工智能能力的能力。这种递归式改进将加速未来版本可能从自然语言描述中生成复杂技能。

4\. 代理编排技能 随着多智能体系统变得越来越普遍，技能将演进以协调多个 AI 智能体在复杂项目上协同工作。

5\. 法规与合规技能 在高度受监管的行业（金融、医疗保健、法律）中，技能编码、合规规则和审计跟踪将变得至关重要。

从小处着手： 构建一项你反复做的事情的技能。当你消除重复工作时，时间投入会很快得到回报。

使用技能创建器：Anthropic 的技能创建器技能（可在

和 Claude Code）可以在 15-30 分钟内搭建你的第一个技能。

加入社区： 在 skills.sh 探索技能目录

，安装热门技能，并从实际案例中学习。

识别高价值工作流：团队成员反复向 AI 解释相同流程的地方是哪里？那些正是关键技能的候选点。

创建一个技能代码仓库： 在 Git 中对组织技能进行版本控制。在团队间共享这些技能并根据反馈迭代。

标准化开放规范： 构建技能以使用开放标准，确保随着人工智能领域的发展具备可移植性。

投资于技能维护： 就像任何代码一样，技能需要更新。分配所有权并建立审查流程。

运用组织部署： 使用管理员控制在全工作区范围内配置技能，以实现一致的操作。

与供应商合作： 现在许多 SaaS 工具提供官方技能（Atlassian、Notion、Figma 等）。这些工具能与您现有的工作流程无缝集成。

培养合规技能： 编码监管要求作为技能，以确保人工智能辅助工作符合标准。

衡量投资回报率(ROI)：跟踪时间节省、错误减少和一致性改进。技能应体现明确的业务价值。

问题 : 技能从不自动加载 解决方案 : 修改你的描述，包含用户实际会说的特定触发短语。测试用户可能表述该请求的不同方式。

问题 : 针对不相关查询的技能负载 解决方案：添加负面触发条件并更明确地限定范围。示例：不用于简单的数据探索（改用数据可视化技能）。

问题 : 技能加载但 Claude 不遵循指令 解决方案 ：

-   保持说明简洁，使用项目符号
    
-   将关键指令放在顶部，使用类似 \`## CRITICAL\` 的标题
    
-   对于确定性验证，考虑打包可执行脚本而非依赖自然语言
    

问题: 技能加载但 MCP 调用失败 解决方案 :

-   验证 MCP 服务器是否已连接 (设置 > 扩展)
    
-   检查 API 密钥和认证
    
-   独立测试 mcp 而没有技能
    
-   验证工具名称与 MCP 服务器文档完全一致（区分大小写）
    

代理技能代表了我们与 AI 协作方式的根本性变革。技能不再将每次对话视为空白状态，而是使我们能够积累组织知识、编码最佳实践，并创建真正理解我们领域的专业 AI 助手。 开放标准确保这不是专有锁定，而是一个创新能够蓬勃发展的生态系统。无论你是独立开发者开发生产力工具、团队标准化工作流程，还是企业大规模部署人工智能，技能都提供了框架，将通用人工智能转化为专业伙伴。 入门门槛从未如此之低。借助像

CLI 和技能市场这样的工具，创建和部署一个技能只需几分钟，而非几天。学习曲线很平缓——从你经常执行的任务开始，先掌握一个简单的技能，然后在此基础上逐步提升。 随着我们展望未来，AI 代理将处理日益复杂的工作，技能将成为区分仅使用 AI 的组织与真正将 AI 作为战略优势加以利用的组织的关键因素。 问题不在于是否要投资于技能，而在于你能多快开始培养这些技能。 欢迎来到专业 AI 代理时代。欢迎来到技能时代。