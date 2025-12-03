---
title: "2025-11-28_anthropic_com_Anthropic_的工程实践_engineering_Illustration_for"
source: "https://www.anthropic.com/engineering/advanced-tool-use"
author:
  - "[[@anthropic.com]]"
published: 2025-11-28
created: 2025-11-28
description:
tags:
  - "#providing"
  - "anthropic"
  - "@anthropic.com"
  - "claude"
status: "inbox"
importance: 2
effort: 2
review_level: 0
review_next: "2025-12-10"
review_interval: null
review_count: 0
decision: null
topics: []
links_out: []
summary: ""
pov: ""
actions: []
---

# [Anthropic 的工程实践](engineering) ![Illustration for

[Anthropic 的工程实践](/engineering) ![Illustration for advanced tool use article.](https://www-cdn.anthropic.com/images/4zrzovbb/website/151600be7f9c23247aad8dcb6aacb2e1ab024f44-1000x1000.svg)

## Claude 开发者平台高级工具使用指南

人工智能代理的未来，是模型能在数百甚至数千种工具间无缝协作的图景。一个集成 Git 操作、文件管理、包管理器、测试框架和部署流程的 IDE 助手；一个能同时联动 Slack、GitHub、Google 云端硬盘、Jira、企业数据库及数十个 MCP 服务器的运维协调器。

要 [构建高效智能体](https://www.anthropic.com/research/building-effective-agents) ，必须让它们能够调用无限工具库，而无需预先将所有定义塞入上下文。我们关于 [通过 MCP 执行代码](https://www.anthropic.com/engineering/code-execution-with-mcp) 的博客文章曾讨论过，工具结果和定义有时会占用超过 5 万个标记，之后智能体才能读取请求。智能体应当按需发现和加载工具，仅保留与当前任务相关的部分。

代理也需要具备从代码调用工具的能力。使用自然语言工具调用时，每次调用都需要完整的推理过程，无论中间结果是否有用都会堆积在上下文中。代码天然适合编排逻辑，比如循环、条件判断和数据转换。代理需要根据当前任务的特性，灵活选择执行代码还是进行推理。

智能体不仅需要从模式定义中学习，更需要通过实例掌握正确的工具使用方法。JSON 模式定义了结构上的有效性，但无法表达使用习惯：何时包含可选参数、哪些参数组合有意义，或是你的 API 期望遵循怎样的约定俗成。

今天，我们推出三项实现这一目标的功能：

- **工具搜索工具，** 让 Claude 能够使用搜索工具访问数千种工具，而无需消耗其上下文窗口
- **程序化工具调用** ，使 Claude 能够在代码执行环境中调用工具，减少对模型上下文窗口的影响
- **工具使用示例** ，为有效演示如何使用特定工具提供了通用标准

在内部测试中，我们发现这些功能帮助我们实现了传统工具使用模式无法达成的目标。例如， **[Claude for Excel](https://www.claude.com/claude-for-excel)** 利用编程式工具调用功能，能够读取和修改包含数千行数据的电子表格，而不会使模型的上下文窗口过载。

根据我们的经验，这些功能将为您使用 Claude 构建应用开启新的可能性。

### The challenge

MCP 工具定义提供了重要上下文，但随着连接服务器增多，这些令牌会不断累积。以五台服务器的配置为例：

- GitHub：35 种工具（约 2.6 万词元）
- Slack：11 种工具（约 2.1 万词元）
- Sentry：5 种工具（约 3K 词元）
- Grafana：5 种工具（约 3000 个词元）
- Splunk：2 个工具（约 2000 个词元）

这相当于对话尚未开始，就有 58 个工具消耗了约 5.5 万个 token。若再添加像 Jira 这样的服务器（仅它就需要约 1.7 万个 token），很快就会逼近 10 万+的 token 开销。在 Anthropic，我们曾观察到工具定义在优化前消耗了 13.4 万个 token。

但令牌成本并非唯一问题。最常见的失败原因是工具选择错误和参数设置不当，尤其是当工具名称相似时，比如 `notification-send-user` 与 `notification-send-channel` 这种情况。

### Our solution

工具搜索工具并非预先加载所有工具定义，而是按需发现工具。Claude 仅能看到当前任务实际需要的工具。

![Tool Search Tool diagram](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Ff359296f770706608901eadaffbff4ca0b67874c-1999x1125.png&w=3840&q=75)

工具搜索工具可保留 191,300 个标记的上下文，而 Claude 传统方法仅能保留 122,800 个。

传统方法：

- 所有工具定义预先加载（约 7.2 万个标记，对应 50 多款 MCP 工具）
- 对话历史与系统提示词争夺剩余空间
- 在开始任何工作前，总上下文消耗量约为7.7万个词元

借助工具搜索工具：

- 仅预先加载了工具搜索工具（约500词）
- 按需发现工具（3-5个相关工具，约3000个词元）
- 总上下文消耗量：约 8.7K 词元，保留 95%的上下文窗口

在保持完整工具库访问的同时，这实现了令牌使用量减少 85%。内部测试表明，在处理大型工具库时，MCP 评估的准确率显著提升：启用工具搜索功能后，Opus 4 从 49%提升至 74%，Opus 4.5 从 79.5%提升至 88.1%。

工具搜索功能让 Claude 能够动态发现工具，而非一次性加载所有定义。您需要将所有工具定义提供给 API，但可通过设置 `defer_loading: true` 标记工具以实现按需发现。延迟加载的工具最初不会载入 Claude 的上下文环境，Claude 仅能直接使用工具搜索功能本身以及标记为 `defer_loading: false` 的关键高频工具。

当 Claude 需要特定功能时，它会搜索相关工具。工具搜索工具会返回匹配工具的引用，这些引用将在 Claude 的上下文中展开为完整定义。

例如，若 Claude 需与 GitHub 交互，它会搜索“github”，此时仅加载 `github.createPullRequest` 和 `github.listIssues` ——而不会载入您来自 Slack、Jira 和 Google Drive 的其他 50 多种工具。

这样一来，Claude 就能调用你的全部工具库，同时只需为实际使用的工具支付 token 费用。

**提示缓存说明：** 工具搜索工具不会破坏提示缓存，因为延迟工具在初始提示中完全被排除。它们仅在 Claude 搜索后才会被添加上下文，因此您的系统提示和核心工具定义仍可缓存。

**Implementation:**

```
{
  "tools": [
 // Include a tool search tool (regex, BM25, or custom)
 {"type": "tool_search_tool_regex_20251119", "name": "tool_search_tool_regex"},

 // Mark tools for on-demand discovery
 {
 "name": "github.createPullRequest",
 "description": "Create a pull request",
 "input_schema": {...},
 "defer_loading": true
 }
 // ... hundreds more deferred tools with defer_loading: true
  ]
}
```

对于 MCP 服务器，您可以在保持特定高频使用工具加载的同时，延迟加载整个服务器：

```
{
  "type": "mcp_toolset",
  "mcp_server_name": "google-drive",
  "default_config": {"defer_loading": true}, # defer loading the entire server
  "configs": {
 "search_files": {
"defer_loading": false
 }  // Keep most used tool loaded
  }
}
```

Claude 开发者平台内置了基于正则表达式和 BM25 的搜索工具，同时您也可以通过嵌入技术或其他策略实现自定义搜索工具。

与任何架构决策一样，启用工具搜索功能也需要权衡利弊。该特性在工具调用前增加了搜索步骤，因此当节省的上下文成本和准确率提升超过额外延迟时，才能实现最佳投资回报。

**Use it when:**

- 工具定义消耗超过1万字符
- 遇到工具选择准确性问题
- 构建基于多服务器的 MCP 系统
- 10+ tools available

**在以下情况下效果较差：**

- 小型工具库（工具数量<10）
- 每个会话中频繁使用的所有工具
- 工具定义简洁明了

## 程序化工具调用

### The challenge

随着工作流程日益复杂，传统工具调用会引发两个根本性问题：

- **中间结果造成的上下文污染** ：当 Claude 分析 10MB 的日志文件以查找错误模式时，整个文件都会进入其上下文窗口，即使 Claude 只需要错误频率的摘要。在跨多个表获取客户数据时，每条记录无论相关性如何都会在上下文中累积。这些中间结果消耗大量 token 预算，并可能将重要信息完全挤出上下文窗口。
- **推理开销与人工整合** ：每次工具调用都需要完整的模型推理过程。获取结果后，Claude 必须通过自然语言处理来"目测"数据以提取相关信息，推理各片段如何衔接，并决定后续操作。一个包含五个工具的工作流意味着需要进行五次推理，外加 Claude 解析每个结果、比对数值并综合结论。这种方式既低效又容易出错。

### Our solution

编程化工具调用使 Claude 能够通过代码编排工具，而非通过单独的 API 往返请求。Claude 不再逐个请求工具并将每个结果返回其上下文，而是编写代码来调用多个工具、处理它们的输出，并控制实际进入其上下文窗口的信息。

Claude 在编写代码方面表现出色，通过让其用 Python 表达编排逻辑而非自然语言工具调用，您能获得更可靠、精确的控制流。循环、条件判断、数据转换和错误处理都在代码中明确体现，而非隐含在 Claude 的推理过程中。

#### 示例：预算合规性检查

设想一个常见的业务场景："哪些团队成员超出了第三季度的差旅预算？"

您目前可使用三种工具：

- `get_team_members(department)` - 返回包含 ID 和级别的团队成员列表
- `get_expenses(user_id, quarter)` - 返回用户的费用明细项
- `get_budget_by_level(level)` - 根据员工级别返回预算限额

**传统方法** :

- 获取团队成员 → 20人
- 为每位员工获取其第三季度开支 → 调用20次工具，每次返回50-100条明细（航班、酒店、餐饮、票据）
- 按员工级别获取预算限额
- 所有这些内容都会进入 Claude 的上下文：2000 多条费用明细项（超过 50KB）
- Claude 手动汇总每个人的开支，查询他们的预算，并将支出与预算限额进行对比
- 模型往返次数增多，上下文消耗显著增加

**通过程序化工具调用** :

不再需要每个工具的结果都返回给 Claude 处理，而是由 Claude 编写一个 Python 脚本来统筹整个工作流程。该脚本在代码执行工具（沙盒环境）中运行，当需要获取工具结果时会暂停执行。当您通过 API 返回工具结果时，这些结果将由脚本处理而非直接交给模型。脚本会继续执行后续操作，最终 Claude 只会看到最终输出结果。

![Programmatic tool calling flow](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F65737d69a3290ed5c1f3c3b8dc873645a9dcc2eb-1999x1491.png&w=3840&q=75)

程序化工具调用使 Claude 能够通过代码编排工具，而非通过单独的 API 往返调用，从而实现并行工具执行。

为预算合规任务编排的代码示例如下：

```
team = await get_team_members("engineering")

# Fetch budgets for each unique level
levels = list(set(m["level"] for m in team))
budget_results = await asyncio.gather(*[
 get_budget_by_level(level) for level in levels
])

# Create a lookup dictionary: {"junior": budget1, "senior": budget2, ...}
budgets = {level: budget for level, budget in zip(levels, budget_results)}

# Fetch all expenses in parallel
expenses = await asyncio.gather(*[
 get_expenses(m["id"], "Q3") for m in team
])

# Find employees who exceeded their travel budget
exceeded = []
for member, exp in zip(team, expenses):
 budget = budgets[member["level"]]
 total = sum(e["amount"] for e in exp)
 if total > budget["travel_limit"]:
 exceeded.append({
 "name": member["name"],
 "spent": total,
 "limit": budget["travel_limit"]
 })

print(json.dumps(exceeded))
```

Claude 的上下文仅接收最终结果：那两三位超出预算的人员。两千多行明细、中间汇总及预算查询均不影响 Claude 的上下文，使其消耗从 200KB 原始支出数据骤减至仅 1KB 结果数据。

效率提升显著：

- **节省令牌数** ：通过将中间结果排除在 Claude 上下文之外，PTC 显著降低了令牌消耗。在复杂研究任务中，平均使用量从 43,588 个令牌降至 27,297 个令牌，降幅达 37%。
- **降低延迟** ：每次 API 往返都需要模型推理（耗时数百毫秒至数秒）。当 Claude 在单个代码块中协调 20 多个工具调用时，您可消除 19 次以上的推理过程。API 会在不每次返回模型的情况下处理工具执行。
- **准确性提升** ：通过编写明确的编排逻辑，Claude 在处理多个工具结果时比使用自然语言时的错误更少。内部知识检索准确率从 25.6%提升至 28.5%； [GIA 基准测试](https://arxiv.org/abs/2311.12983) 从 46.5%提升至 51.2%。

生产工作流涉及杂乱的数据、条件逻辑以及需要扩展的操作。程序化工具调用让 Claude 能够以编程方式处理这种复杂性，同时保持对可操作结果的关注，而非原始数据处理。

### 程序化工具调用的工作原理

#### 1\. 将工具标记为可从代码调用

将 code\_execution 添加至工具集，并将 allowed\_callers 设置为选择性启用的工具以支持程序化执行：

```
{
  "tools": [
 {
 "type": "code_execution_20250825",
 "name": "code_execution"
 },
 {
 "name": "get_team_members",
 "description": "Get all members of a department...",
 "input_schema": {...},
 "allowed_callers": ["code_execution_20250825"] # opt-in to programmatic tool calling
 },
 {
 "name": "get_expenses",
 ...
 },
 {
 "name": "get_budget_by_level",
 ...
 }
  ]
}
```

API 会将这些工具定义转换为可供 Claude 调用的 Python 函数。

#### 2\. Claude 编写编排代码

Claude 不再逐个请求工具，而是直接生成 Python 代码：

```
{
  "type": "server_tool_use",
  "id": "srvtoolu_abc",
  "name": "code_execution",
  "input": {
 "code": "team = get_team_members('engineering')\n..." # the code example above
  }
}
```

#### 3\. 工具执行无需占用 Claude 的上下文资源

当代码调用 get\_expenses() 时，您会收到一个带有调用者字段的工具请求：

```
{
  "type": "tool_use",
  "id": "toolu_xyz",
  "name": "get_expenses",
  "input": {"user_id": "emp_123", "quarter": "Q3"},
  "caller": {
 "type": "code_execution_20250825",
 "tool_id": "srvtoolu_abc"
  }
}
```

结果由代码执行环境处理，而非 Claude 的上下文。每次代码中的工具调用都会重复这个请求-响应循环。

#### 4\. 仅最终输出进入上下文

当代码运行完毕时，仅将代码执行结果返回给 Claude：

```
{
  "type": "code_execution_tool_result",
  "tool_use_id": "srvtoolu_abc",
  "content": {
 "stdout": "[{\"name\": \"Alice\", \"spent\": 12500, \"limit\": 10000}...]"
  }
}
```

Claude 看到的只是最终结果，而非处理过程中涉及的 2000 多条支出明细。

### 何时使用编程式工具调用

编程式工具调用为你的工作流增加了一个代码执行步骤。当节省的令牌数量、延迟改善和准确率提升显著时，这一额外开销是值得的。

**最适用场景：**

- 处理仅需聚合或摘要的大型数据集
- 运行包含三个或更多依赖工具调用的多步骤工作流
- 在 Claude 查看之前对工具结果进行筛选、排序或转换
- 处理不应影响 Claude 推理过程的中间数据任务
- 同时对多个项目执行并行操作（例如检查50个端点）

**在以下情况下效果较差：**

- 实现简单的单工具调用
- 在需要 Claude 观察并推理所有中间结果的任务中工作
- 快速查询并获取简短响应

## Tool Use Examples

### The challenge

JSON Schema 擅长定义结构——类型、必填字段、允许的枚举值——但它无法表达使用模式：何时包含可选参数、哪些组合有意义，或你的 API 期望遵循哪些约定。

考虑一个工单支持 API：

```
{
  "name": "create_ticket",
  "input_schema": {
 "properties": {
 "title": {"type": "string"},
 "priority": {"enum": ["low", "medium", "high", "critical"]},
 "labels": {"type": "array", "items": {"type": "string"}},
 "reporter": {
 "type": "object",
 "properties": {
 "id": {"type": "string"},
 "name": {"type": "string"},
 "contact": {
 "type": "object",
 "properties": {
 "email": {"type": "string"},
 "phone": {"type": "string"}
 }
 }
 }
 },
 "due_date": {"type": "string"},
 "escalation": {
 "type": "object",
 "properties": {
 "level": {"type": "integer"},
 "notify_manager": {"type": "boolean"},
 "sla_hours": {"type": "integer"}
 }
 }
 },
 "required": ["title"]
  }
}
```

架构定义了何为有效，却留下关键问题悬而未决：

- **格式模糊：** `due_date` 应使用"2024-11-06"、"Nov 6, 2024"还是"2024-11-06T00:00:00Z"？
- **ID 命名规范：** `reporter.id` 是 UUID 格式、"USR-12345"格式，还是纯数字"12345"？
- **嵌套结构使用场景：** Claude 应在何时填充 `reporter.contact` 字段？
- **参数关联性：** `escalation.level` 和 `escalation.sla_hours` 如何与优先级关联？

这些模糊之处可能导致工具调用格式错误和参数使用不一致。

### Our solution

工具使用示例功能允许您直接在工具定义中提供调用范例。这不再仅依赖模式描述，而是向 Claude 展示具体的使用方式：

从这三个例子中，Claude 学会了：

- **格式规范** ：日期采用 YYYY-MM-DD 格式，用户 ID 遵循 USR-XXXXX 格式，标签使用短横线命名法
- **嵌套结构模式** ：如何构建包含嵌套联系人对象的记者对象
- **可选参数关联** ：严重错误需包含完整联系信息及严格服务等级协议的升级流程；功能请求需记录提交者但无需联系信息或升级流程；内部任务仅需标题

在我们内部的测试中，工具使用示例将复杂参数处理的准确率从72%提升至90%。

### 何时使用工具使用示例

工具使用示例会在您的工具定义中添加标记，因此当准确性提升超过额外成本时，它们的价值最为显著。

**最适用场景：**

- 复杂嵌套结构中，有效的 JSON 并不等同于正确使用
- 拥有众多可选参数和包含模式的功能工具至关重要
- 不包含在模式中的特定领域约定 API
- 在类似工具中，示例会说明应使用哪一个（例如 `create_ticket` 与 `create_incident` 的区别）

**在以下情况下效果较差：**

- 功能明确、参数单一的简单工具
- Claude 已能识别的标准格式（如网址或电子邮件）
- JSON Schema 约束能更有效地处理验证问题

## Best practices

构建能够执行现实世界行动的智能体，意味着需要同时处理规模性、复杂性和精确性。这三项特性协同作用，共同解决工具使用工作流中的不同瓶颈。以下是如何有效整合它们的方法。

### 战略性地分层布局功能

并非每个智能体都需要为特定任务使用全部三项功能。先从最突出的瓶颈入手：

- 工具定义导致的上下文膨胀 → 工具搜索工具
- 大型中间结果污染上下文 → 编程式工具调用
- 参数错误与调用格式异常 → 工具使用示例

这种聚焦式方法让你能针对性地解决制约智能体性能的具体瓶颈，而非一开始就增加复杂度。

然后根据需要添加额外功能。这些功能互为补充：工具搜索工具确保找到合适的工具，程序化工具调用确保高效执行，而工具使用示例则确保正确调用。

工具搜索会匹配名称和描述，因此清晰、描述性的定义能提高发现准确度。

```
// Good
{
 "name": "search_customer_orders",
 "description": "Search for customer orders by date range, status, or total amount. Returns order details including items, shipping, and payment info."
}

// Bad
{
 "name": "query_db_orders",
 "description": "Execute order query"
}
```

添加系统提示指引，让 Claude 了解可用的功能：

```
You have access to tools for Slack messaging, Google Drive file management, 
Jira ticket tracking, and GitHub repository operations. Use the tool search 
to find specific capabilities.
```

将最常用的三到五种工具常驻内存，其余按需加载。这样既保证了高频操作的即时响应，又实现了其他功能的按需发现。

### 设置程序化工具调用以确保正确执行

由于 Claude 需要编写代码来解析工具输出，请明确记录返回格式。这有助于 Claude 编写正确的解析逻辑：

```
{
 "name": "get_orders",
 "description": "Retrieve orders for a customer.
Returns:
 List of order objects, each containing:
 - id (str): Order identifier
 - total (float): Order total in USD
 - status (str): One of 'pending', 'shipped', 'delivered'
 - items (list): Array of {sku, quantity, price}
 - created_at (str): ISO 8601 timestamp"
}
```

以下列出可从程序化编排中获益的可选工具：

- 可以并行运行的工具（独立操作）
- 可安全重试的操作（幂等）

### 设置工具使用示例以确保参数准确性

为行为清晰度设计范例：

- 使用真实数据（真实的城市名称、合理的价格，而非"字符串"或"数值"）
- 以最少、部分和完整规范模式展现多样性
- 保持简洁：每种工具列举1-5个示例
- 专注于模糊性（仅在模式无法明确正确用法时添加示例）

## Getting started

这些功能目前处于测试阶段。如需启用，请添加测试版标头并包含您所需的工具：

```
client.beta.messages.create(
 betas=["advanced-tool-use-2025-11-20"],
 model="claude-sonnet-4-5-20250929",
 max_tokens=4096,
 tools=[
 {"type": "tool_search_tool_regex_20251119", "name": "tool_search_tool_regex"},
 {"type": "code_execution_20250825", "name": "code_execution"},
 # Your tools with defer_loading, allowed_callers, and input_examples
 ]
)
```

如需详细 API 文档和 SDK 示例，请参阅我们的：

- [工具搜索工具 文档](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool) 与 [使用指南](https://github.com/anthropics/claude-cookbooks/blob/main/tool_use/tool_search_with_embeddings.ipynb)
- [文档](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling) 与 [指南](https://github.com/anthropics/claude-cookbooks/blob/main/tool_use/programmatic_tool_calling_ptc.ipynb) ：程序化工具调用
- [工具使用示例文档](https://platform.claude.com/docs/en/agents-and-tools/tool-use/implement-tool-use#providing-tool-use-examples)

这些功能将工具使用从简单的函数调用提升至智能编排层面。随着智能体处理涉及数十种工具和海量数据集的复杂工作流，动态发现、高效执行与可靠调用已成为核心基础能力。

我们迫不及待想看到你的构建成果。

## Acknowledgements

本文由吴斌撰写，Adam Jones、Artur Renault、Henry Tay、Jake Noble、Nathan McCandlish、Noah Picard、Sam Jiang 及 Claude 开发者平台团队共同参与。这项研究建立在 Chris Gorgolewski、Daniel Jiang、Jeremy Fox 和 Mike Lambert 的基础性工作之上。我们还从整个 AI 生态系统中汲取灵感，包括 [Joel Pobar 的 LLMVM](https://github.com/9600dev/llmvm) 、 [Cloudflare 的代码模式](https://blog.cloudflare.com/code-mode/) 以及 [将代码执行作为 MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) 。特别感谢 Andy Schumeister、Hamish Kerr、Keir Bradwell、Matt Bleifer 和 Molly Vorwerck 提供的支持。

## 订阅开发者通讯

产品更新、使用指南、社区精选等内容，每月直达您的收件箱。