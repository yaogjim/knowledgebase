---
title: "Equipping agents for the real world with Agent Skills"
source: "https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills"
author:
  - "[[@AnthropicAI]]"
published: 2025-11-06
created: 2025-11-06
description: "Discover how Anthropic builds AI agents with practical capabilities through modular skills, enabling them to handle complex real-world tasks more effectively and reliably."
tags:
  - "@AnthropicAI"
status: "inbox"
importance: 2
effort: 2
review_level: 0
review_next: "2025-11-13"
review_interval: null
review_count: 0
decision: null
topics: []
links_out: []
summary: ""
pov: ""
actions: []
---
## 为现实世界中的智能体配备代理技能

随着模型能力的提升，我们现在可以构建能够与成熟计算环境交互的通用智能体。例如， [Claude Code](https://claude.com/product/claude-code) 就能通过本地代码执行和文件系统完成跨领域的复杂任务。但随着这些智能体日益强大，我们需要更可组合、可扩展且可移植的方式来为它们配备领域专业知识。

这促使我们创建了 [**智能体技能**](https://www.anthropic.com/news/skills) ：一种结构化的指令、脚本和资源文件夹，智能体能够动态发现并加载这些内容，从而在特定任务中表现更优。技能通过将您的专业知识打包成可组合的资源供 Claude 使用，有效扩展了 Claude 的能力，将通用智能体转化为符合您需求的专用智能体。

为智能体构建技能，就如同为新员工编写入职指南。如今，无需为每个用例零散地定制专属智能体，任何人都能通过捕捉和分享流程知识，以可组合的能力来专业化自己的智能体。本文将阐述何为技能，展示其运作方式，并分享构建专属技能的最佳实践。

![To activate skills, all you need to do is write a SKILL.md file with custom guidance for your agent.](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fddd7e6e572ad0b6a943cacefe957248455f6d522-1650x929.jpg&w=1920&q=75)

技能是一个包含 SKILL.md 文件的目录，该文件内含组织有序的指令、脚本及资源文件夹，能为智能体赋予额外能力。

## 技能剖析

要了解技能的实际应用，让我们来看一个真实案例：支撑 [Claude 最新推出的文档编辑功能](https://www.anthropic.com/news/create-files) 的其中一项技能。Claude 本身已具备丰富的 PDF 解析能力，但在直接操作 PDF 方面存在局限（例如填写表格）。这项 [PDF 技能](https://github.com/anthropics/skills/tree/main/document-skills/pdf) 使我们能够为 Claude 赋予这些新能力。

最简单来说，一个技能就是包含 `SKILL.md 文件` 的目录。该文件必须以包含必要元数据的 YAML 前置内容开头： `name` （名称）和 `description` （描述）。启动时，代理会将每个已安装技能的 `name` （名称）和 `description` （描述）预加载到其系统提示中。

此元数据属于 **第一层级** 的 *渐进式呈现* ：仅提供足够信息让 Claude 判断何时该调用相应技能，而无需将其全部内容载入上下文。文件的实际主体部分构成 **第二层级** 的详细信息。若 Claude 判定某技能与当前任务相关，便会通过完整读取该技能的 `SKILL.md` 文件将其载入上下文。

![Anatomy of a SKILL.md file including the relevant metadata: name, description, and context related to the specific actions the skill should take.](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F6f22d8913dbc6228e7f11a41e0b3c124d817b6d2-1650x929.jpg&w=1920&q=75)

SKILL.md 文件必须以包含文件名和描述的 YAML Frontmatter 开头，这些内容会在启动时加载到系统提示中。

随着技能复杂度的提升，单个 `SKILL.md` 文件可能无法容纳全部上下文，或存在仅适用于特定场景的内容。此时，技能可以在技能目录中捆绑附加文件，并通过 `SKILL.md` 按名称引用它们。这些附加的链接文件构成了 **第三层级** （及更深入）的细节内容，Claude 可根据需要自主选择浏览和探索。

在下图所示的 PDF 技能中， `SKILL.md` 引用了技能作者选择与核心 `SKILL.md` 捆绑的两个附加文件（ `reference.md` 和 `forms.md` ）。通过将表格填写说明移至独立文件 `forms.md` ，技能作者得以保持技能核心的简洁性，并确信 Claude 仅在填写表格时才会读取 `forms.md` 。

![How to bundle additional content into a SKILL.md file.](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F191bf5dd4b6f8cfe6f1ebafe6243dd1641ed231c-1650x1069.jpg&w=1920&q=75)

您可以将更多上下文（通过附加文件）整合到技能中，随后 Claude 可根据系统提示触发该技能。

渐进式披露是使智能体技能具备灵活性和可扩展性的核心设计原则。正如编排精良的手册先呈现目录，再展示具体章节，最后提供详细附录那样，技能让 Claude 能够按需加载信息：

![This image depicts how progressive disclosure of context in Skills.](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fa3bca2763d7892982a59c28aa4df7993aaae55ae-2292x673.jpg&w=3840&q=75)

This image depicts how progressive disclosure of context in Skills.

拥有文件系统和代码执行工具的智能体在处理特定任务时，无需将整个技能内容全部载入其上下文窗口。这意味着可整合进技能的上下文量实际上是无限的。

### 技能与上下文窗口

下图展示了当用户消息触发技能时，上下文窗口如何变化。

![This image depicts how skills are triggered in your context window.](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F441b9f6cc0d2337913c1f41b05357f16f51f702e-1650x929.jpg&w=1920&q=75)

技能在上下文窗口中通过您的系统提示触发。

所示操作顺序为：

1. 首先，上下文窗口包含了核心系统提示、已安装各项技能的元数据以及用户的初始消息；
2. Claude 通过调用 Bash 工具读取 `pdf/SKILL.md` 文件内容来触发 PDF 技能；
3. Claude 选择读取与该技能捆绑的 `forms.md` 文件；
4. 最终，Claude 在从 PDF 技能加载了相关指令后，开始执行用户的任务。

### 技能与代码执行

技能也可以包含代码，供 Claude 自行决定作为工具执行。

大型语言模型在众多任务中表现出色，但某些操作更适合传统代码执行。例如，通过令牌生成来排序列表，远比直接运行排序算法成本高昂。除了效率考量外，许多应用场景还需要代码才能提供的确定性可靠性。

在我们的示例中，PDF 技能包含一个预编写的 Python 脚本，用于读取 PDF 并提取所有表单字段。Claude 无需将脚本或 PDF 加载到上下文中即可运行此脚本。由于代码具有确定性，这一工作流程具有一致性和可重复性。

![This image depicts how code is executed via Skills.](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fc24b4a2ff77277c430f2c9ef1541101766ae5714-1650x929.jpg&w=1920&q=75)

技能还可以包含代码，让 Claude 根据任务性质自行决定是否将其作为工具来执行。

## 开发与评估技能

以下是一些关于编写和测试技能的实用入门指南：

- **从评估入手：** 通过让智能体执行代表性任务并观察其薄弱环节或需要补充信息之处，从而识别能力短板。随后逐步构建技能以弥补这些不足。
- **规模化结构：** 当 `SKILL.md` 文件变得臃肿时，将其内容拆分至独立文件并进行引用。若某些上下文互斥或极少同时使用，保持路径分离将有效减少令牌消耗。最后，代码既可充当可执行工具，也能作为文档使用。必须明确 Claude 应直接运行脚本，还是将其作为参考文档读入上下文。
- **从 Claude 的视角思考：** 在实际场景中监控 Claude 如何使用你的技能，并根据观察结果进行迭代：留意意外执行路径或对特定上下文的过度依赖。特别关注技能的 `name` 和 `description` ，Claude 将根据当前任务决定是否触发技能时使用这些信息。
- **与 Claude 迭代协作：** 在与 Claude 处理任务时，可要求其将成功的方法和常见错误转化为可复用的上下文代码并收录为技能。若使用技能执行任务时出现偏差，可要求其进行自我反思分析问题根源。这一过程将帮助您发现 Claude 实际需要的上下文信息，而非预先揣测其需求。

### 使用技能时的安全注意事项

技能通过指令和代码为 Claude 赋予新的能力。虽然这使得技能功能强大，但也意味着恶意技能可能会在使用环境中引入安全漏洞，或诱导 Claude 泄露数据并执行非预期操作。

我们建议仅从可信来源安装技能。当从可信度较低的来源安装技能时，请在使用前对其进行彻底审查。首先阅读技能包中文件的内容以了解其功能，尤其要注意代码依赖项及捆绑资源（如图像或脚本）。同样地，需重点关注技能中指示 Claude 连接至可能不可信的外部网络资源的指令或代码。

## 技能的未来

Agent Skills 现已在 [Claude.ai](https://www.anthropic.com/news/skills) 、Claude Code、Claude Agent SDK 以及 Claude 开发者平台中 [获得支持](http://claude.ai/redirect/website.v1.17cccc01-972b-4feb-bd4e-df10a759d36a) 。

在接下来的几周里，我们将持续增加支持技能创建、编辑、发现、共享和使用全生命周期的功能。我们特别期待技能能帮助组织和个人与 Claude 共享其背景信息和工作流程。我们还将探索技能如何通过教授智能体更复杂的工作流程（涉及外部工具和软件）来补充 [模型上下文协议](https://modelcontextprotocol.io/) （MCP）服务器。

展望未来，我们希望让智能体能够自主创建、编辑和评估技能，使它们能够将自身的行为模式固化为可复用的能力。

技能是一个简单的概念，拥有相应的简洁格式。这种简洁性使得企业、开发者和最终用户能够更轻松地构建定制化智能体，并为其赋予新的能力。

我们期待看到大家利用技能构建出怎样的成果。立即开始，查看我们的技能 [文档](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) 和 [实用指南](https://github.com/anthropics/claude-cookbooks/tree/main/skills) 吧。

## Acknowledgements

本文由巴里·张、基思·拉祖卡和马赫什·穆拉格共同撰写，他们都对文件夹情有独钟。特别感谢 Anthropic 公司内外众多推动、支持并构建技能功能的同仁。

## 获取开发者通讯

产品更新、使用指南、社区亮点等更多内容。每月定期发送至您的收件箱。