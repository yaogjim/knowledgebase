---
title: "Writing effective tools for AI agents—using AI agents"
source: "https://www.anthropic.com/engineering/writing-tools-for-agents"
author:
  - "[[@AnthropicAI]]"
published: 2025-09-19
created: 2025-09-19
description: "Writing effective tools for AI agents—using AI agents"
tags:
  - "@AnthropicAI"
---
[Anthropic 公司的工程团队](https://www.anthropic.com/engineering) ![This is an abstract illustration for the Eng Blog article, Writing effective tools for agents -- with agents.](https://www-cdn.anthropic.com/images/4zrzovbb/website/876165247ba5668bd195854eef4631ad9a184001-1000x1000.svg)

## 为智能体编写高效工具——借助智能体

模型上下文协议（MCP）可以为 LLM 智能体提供可能多达数百种的工具，以解决现实世界中的任务。但是，我们如何使这些工具发挥出最大效力呢？

在这篇文章中，我们描述了在各种智能体人工智能系统中提高性能的最有效技术 <sup>1</sup> 。

我们首先介绍如何：

- 构建并测试你的工具原型
- 使用智能体对你的工具进行全面评估并运行
- 与 Claude 法典等智能体协作，自动提升工具性能

我们总结了在这个过程中确定的编写高质量工具的关键原则：

- 选择合适的工具来实施（以及不实施）
- 对工具进行命名空间划分以在功能上定义清晰的边界
- 将工具中的有意义上下文返回给智能体
- 针对令牌效率优化工具响应
- 提示工程工具描述与规格

![This is an image depicting how an engineer might use Claude Code to evaluate the efficacy of agentic tools.](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fcdc027ad2730e4732168bb198fc9363678544f99-1920x1080.png&w=1920&q=75)

构建评估可以让你系统地衡量工具的性能。你可以使用 Claude 法典来根据此评估自动优化你的工具。

## What is a tool?

在计算领域，确定性系统在每次给定相同输入时都会产生相同的输出，而像智能体这样的 *非确定性* 系统即使在相同的初始条件下也可能产生不同的响应。

当我们传统地编写软件时，我们正在确定性系统之间建立一份契约。例如，像 `getWeather(“NYC”)` 这样的函数调用每次被调用时，都会以完全相同的方式获取纽约市的天气。

工具是一种新型软件，它反映了确定性系统与非确定性智能体之间的一种契约。当用户问“我今天应该带伞吗？”时，智能体可能会调用天气工具，从常识中给出答案，或者甚至先询问一个关于位置的澄清问题。偶尔，智能体可能会产生幻觉，甚至不知道如何使用工具。

这意味着在为智能体编写软件时要从根本上重新思考我们的方法：我们不应像为其他开发者或系统编写函数和 API 那样编写工具和 [MCP 服务器](https://modelcontextprotocol.io/) ，而是需要为智能体来设计它们。

我们的目标是通过使用工具来追求各种成功策略，从而扩大智能体能够有效解决广泛任务的范围。幸运的是，根据我们的经验，对智能体来说最“符合人体工程学”的工具，对人类而言最终也出奇地易于理解。

## How to write tools

在本节中，我们将描述如何与智能体协作来编写和改进你提供给它们的工具。首先，快速搭建工具的原型并在本地进行测试。接下来，进行全面评估以衡量后续的更改。与智能体一起工作时，你可以重复评估和改进工具的过程，直到你的智能体在实际任务中取得出色的表现。

### 构建一个原型

如果不亲自上手尝试，很难预测哪些工具对智能体来说使用起来顺手，哪些则不然。首先快速搭建工具的原型。如果你正在使用 Claude 编写工具（可能是一次性完成），为工具所依赖的任何软件库、API 或 SDK（包括可能的 MCP SDK）向 Claude 提供文档会很有帮助。适合大语言模型（LLM）的文档通常可以在官方文档网站上的平面 llms.txt 文件中找到（这是我们 API 的文档）。

将你的工具包装在本地 MCP 服务器或桌面扩展（DXT）中，将使你能够在 Claude 法典或 Claude 桌面应用程序中连接和测试你的工具。

要将本地 MCP 服务器连接到 Claude 法典，请运行 `claude mcp add <name> <command> [args...]` 。

要将本地 MCP 服务器或 DXT 连接到 Claude 桌面应用程序，请分别导航到 `  设置>开发者  ` 或 `  设置>扩展  ` 。

工具也可以直接传入 [Anthropic API](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview) 调用中进行编程测试。

亲自测试这些工具，找出其中的任何瑕疵。收集用户反馈，以便围绕你期望工具能够支持的用例和提示建立直观认识。

### 运行评估

接下来，你需要通过运行评估来衡量 Claude 使用你的工具的效果。首先生成大量基于实际应用的评估任务。我们建议与一个智能体合作，以帮助分析你的结果并确定如何改进你的工具。在我们的 [工具评估指南](https://github.com/anthropics/anthropic-cookbook/blob/main/tool_evaluation/tool_evaluation.ipynb) 中从头到尾查看这个过程。

![This graph measures the test set accuracy of human-written vs. Claude-optimized Slack MCP servers.](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F6e810aee67f3f3c955832fb7bf9033ffb0102000-1920x1080.png&w=1920&q=75)

我们内部 Slack 工具的留出测试集性能

**生成评估任务**

使用早期原型，Claude 法典可以快速探索您的工具，并创建数十个提示和响应对。提示应从实际应用中获取灵感，并基于现实的数据源和服务（例如，内部知识库和微服务）。我们建议您避免使用过于简单或表面的“沙盒”环境，这些环境无法以足够的复杂性对您的工具进行压力测试。强大的评估任务可能需要多次调用工具，可能多达数十次。

以下是一些强大任务的示例：

- 安排下周与简开会，讨论我们最新的 Acme 公司项目。附上上次项目规划会议的记录，并预订一间会议室。
- 客户 ID 9182 报告称，他们在一次购买尝试中被收取了三次费用。查找所有相关日志条目，并确定是否有其他客户受到同样问题的影响。
- 客户 Sarah Chen 刚刚提交了取消请求。准备一份挽留提议。确定：(1) 他们离开的原因，(2) 最有吸引力的挽留提议是什么，以及(3) 在提出提议之前我们应该了解的任何风险因素。

以下是一些难度较低的任务：

- 下周安排与 jane@acme.corp 开会。
- 在支付日志中搜索 `purchase_complete` 以及 `customer_id=9182` 。
- 通过客户 ID 45892 查找取消请求。

每个评估提示都应与一个可验证的响应或结果配对。你的验证器可以简单到对真实值和采样响应之间进行精确的字符串比较，也可以复杂到让 Claude 来评判响应。避免使用过于严格的验证器，以免因格式、标点或有效的替代措辞等虚假差异而拒绝正确的响应。

对于每一个提示-响应对，你还可以选择指定在解决任务时期望智能体调用的工具，以便在评估过程中衡量智能体是否成功理解每个工具的用途。然而，由于可能存在多种正确解决任务的有效路径，所以要尽量避免过度指定或过度拟合策略。

**运行评估**

我们建议通过直接调用大语言模型（LLM）API 以编程方式运行评估。使用简单的智能体循环（ `while` 循环，将 LLM API 调用和工具调用交替包裹起来）：每个评估任务使用一个循环。每个评估智能体应被给予一个单一的任务提示和你的工具。

在评估智能体的系统提示时，我们建议指示智能体不仅要输出结构化的响应块（用于验证），还要输出推理和反馈块。指示智能体在工具调用和响应块之前输出这些内容，可能会通过触发思维链（CoT）行为来提高大语言模型（LLMs）的有效智能。

如果您正在使用 Claude 运行评估，您可以开启 [交错式思考](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking#interleaved-thinking) 以获得类似的现成功能。这将帮助您探究智能体为何调用或不调用某些工具，并突出工具描述和规格中需要改进的特定领域。

除了顶级准确性之外，我们建议收集其他指标，如单个工具调用和任务的总运行时间、工具调用的总数、总令牌消耗以及工具错误。跟踪工具调用有助于揭示智能体所采用的常见工作流程，并为工具整合提供一些机会。

![This graph measures the test set accuracy of human-written vs. Claude-optimized Asana MCP servers.](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F3f1f47e80974750cd924bc51e42b6df1ad997fab-1920x1080.png&w=1920&q=75)

我们内部 Asana 工具的留出测试集性能

**Analyzing results**  
智能体是你发现问题并提供反馈的得力伙伴，反馈内容涵盖从相互矛盾的工具描述到低效的工具实现以及令人困惑的工具架构等方方面面。不过，请记住，智能体在反馈和回应中遗漏的内容往往比包含的内容更重要。大语言模型（LLMs）并不总是 [心口如一](https://www.anthropic.com/research/tracing-thoughts-language-model) 。

观察你的智能体在哪些地方陷入困境或感到困惑。通读你的评估智能体的推理和反馈（或思维链），以找出不足之处。查看原始记录（包括工具调用和工具响应），以捕捉智能体思维链中未明确描述的任何行为。要透过字里行间去理解；记住，你的评估智能体不一定知道正确答案和策略。

分析你的工具调用指标。大量冗余的工具调用可能表明需要对分页或令牌限制参数进行一些调整；大量因无效参数导致的工具错误可能表明工具可以使用更清晰的描述或更好的示例。当我们推出 Claude 的 [网络搜索工具](https://www.anthropic.com/news/web-search) 时，我们发现 Claude 在工具的 `查询` 参数中不必要地附加了 `2025` ，这会使搜索结果产生偏差并降低性能（我们通过改进工具描述让 Claude 走上了正轨）。

### 与智能体协作

你甚至可以让智能体分析你的结果并为你改进工具。只需将评估智能体的记录连接起来，然后粘贴到 Claude 法典中。Claude 擅长分析记录并一次性重构大量工具，例如，在进行新更改时确保工具实现和描述保持自洽。

事实上，这篇文章中的大部分建议都来自于使用 Claude 法典对我们的内部工具实现进行反复优化。我们的评估是在我们的内部工作区之上创建的，反映了我们内部工作流程的复杂性，包括实际项目、文档和消息。

我们依靠留出的测试集来确保我们不会过度拟合于我们的“训练”评估。这些测试集表明，即使超出我们使用“专家”工具实现所取得的成果，我们仍能进一步提升性能——无论这些工具是由我们的研究人员手动编写的，还是由 Claude 自身生成的。

在下一节中，我们将分享一些我们从这个过程中学到的东西。

## 编写有效工具的原则

在本节中，我们将所学内容提炼为一些编写有效工具的指导原则。

### 为智能体选择合适的工具

更多的工具并不总是能带来更好的结果。我们观察到一个常见的错误是，有些工具只是简单地包装现有软件功能或 API 端点，而不管这些工具是否适合智能体。这是因为智能体与传统软件有着不同的 “可供性”，也就是说，它们对于可以使用这些工具采取的潜在行动有着不同的认知方式。

大语言模型（LLM）智能体的“上下文”有限（即它们一次能处理的信息量有限），而计算机内存既便宜又充足。以在通讯录中搜索联系人的任务为例。传统软件程序可以高效地逐个存储和处理联系人列表，在继续处理下一个之前检查每一个。

然而，如果一个大语言模型（LLM）智能体使用一个返回所有联系人的工具，然后必须逐令牌地阅读每个联系人，那么它就是在将其有限的上下文空间浪费在无关信息上（想象一下，通过逐页从上到下阅读来在你的通讯录中搜索联系人——也就是说，通过暴力搜索）。更好且更自然的方法（对智能体和人类都是如此）是先跳到相关页面（也许是按字母顺序找到它）。

我们建议构建一些针对特定高影响力工作流程的精心设计的工具，这些工具要与你的评估任务相匹配，并在此基础上进行扩展。在通讯录的案例中，你可能会选择实现一个 `search_contacts` 或 `message_contact` 工具，而不是一个 `list_contacts` 工具。

工具可以整合功能，在底层处理可能的多个离散操作（或 API 调用）。例如，工具可以用相关元数据丰富工具响应，或者在单个工具调用中处理频繁链接的多步骤任务。

以下是一些示例：

- 与其实现一个 `list_users` 、 `list_events` 和 `create_event` 工具，不如考虑实现一个 `schedule_event` 工具，该工具可以查找可用时间并安排活动。
- 与其实现一个 `read_logs` 工具，不如考虑实现一个 `search_logs` 工具，该工具只返回相关的日志行和一些上下文信息。
- 不要实现 `get_customer_by_id` 、 `list_transactions` 和 `list_notes` 工具，而是实现一个 `get_customer_context` 工具，该工具可以一次性汇总某个客户的所有近期相关信息。

确保你构建的每个工具都有明确、独特的用途。工具应使智能体能够像人类在获得相同底层资源时那样细分和解决任务，同时减少原本会被中间输出所占用的上下文。

工具过多或工具重叠也可能会使智能体偏离追求高效策略的方向。精心、有选择地规划你构建（或不构建）的工具会带来切实的回报。

### 对你的工具进行命名空间处理

你的人工智能代理可能会访问数十个 MCP 服务器和数百种不同的工具，包括其他开发者提供的工具。当工具在功能上重叠或目的不明确时，代理可能会对使用哪些工具感到困惑。

命名空间（将相关工具分组在通用前缀下）有助于划分众多工具之间的界限；MCP 客户端有时会默认进行此操作。例如，按服务（如 `asana_search` 、 `jira_search` ）和资源（如 `asana_projects_search` 、 `asana_users_search` ）对工具进行命名空间划分，可帮助智能体在正确的时间选择正确的工具。

我们发现，在基于前缀和后缀的命名空间之间进行选择，会对我们的工具使用评估产生重要影响。不同的大语言模型（LLM）效果各异，我们鼓励你根据自己的评估选择一种命名方案。

智能体可能会调用错误的工具，使用错误的参数调用正确的工具，调用的工具数量过少，或者对工具响应的处理不正确。通过有选择地实现名称反映任务自然细分的工具，你可以同时减少加载到智能体上下文中的工具和工具描述的数量，并将智能体上下文的智能计算卸载回工具调用本身。这降低了智能体犯错的总体风险。

### 从你的工具中返回有意义的上下文信息

同样，工具实现应注意仅将高价值信息返回给智能体。它们应优先考虑上下文相关性而非灵活性，并避免使用底层技术标识符（例如： `uuid` 、 `256px_image_url` 、 `mime_type` ）。像 `name` 、 `image_url` 和 `file_type` 这样的字段更有可能直接指导智能体的下游操作和响应。

与难以理解的标识符相比，智能体在处理自然语言名称、术语或标识符方面往往要成功得多。我们发现，仅仅将任意字母数字的通用唯一识别码（UUID）解析为更具语义意义和可解释性的语言（甚至是从零开始索引的 ID 方案），就能通过减少幻觉显著提高 Claude 在检索任务中的精确率。

在某些情况下，智能体可能需要具备与自然语言和技术标识符输出进行交互的灵活性，哪怕只是为了触发下游工具调用（例如， `search_user(name='jane')` → `send_message(id=12345)` ）。你可以通过在工具中公开一个简单的 `response_format` 枚举参数来实现这两种功能，使你的智能体能够控制工具返回的是 `“简洁”` 还是 `“详细”` 响应（见下图）。

你可以添加更多格式以获得更大的灵活性，这类似于 GraphQL，在 GraphQL 中你可以精确选择想要接收的信息片段。以下是一个用于控制工具响应详细程度的\`ResponseFormat\`枚举示例：

```
enum ResponseFormat {
   DETAILED = "detailed",
   CONCISE = "concise"
}
```

以下是一个详细工具响应的示例（206个令牌）：

![This code snippet depicts an example of a detailed tool response.](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F5ed0d30526bf68624f335d075b8c1541be3bb595-1920x1006.png&w=1920&q=75)

This code snippet depicts an example of a detailed tool response.

以下是一个简洁的工具响应示例（72个词元）：

![This code snippet depicts a concise tool response.](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fd4f649a66482efb5a80cf14ea85e84974ede1c49-1920x725.png&w=1920&q=75)

Slack 线程和线程回复由唯一的 thread\_ts 标识，获取线程回复需要用到它。 和其他 ID（ channel\_id 、 user\_id ）可以从 “详细” 工具响应中获取，以便进行需要这些 ID 的进一步工具调用。 “简洁” 工具响应仅返回线程内容并排除 ID。在这个示例中，我们在 工具响应中使用了约三分之一的令牌。

即使是你的工具响应结构（例如 XML、JSON 或 Markdown）也会对评估性能产生影响：不存在适用于所有情况的解决方案。这是因为大型语言模型是基于下一个 token 预测进行训练的，并且在与它们的训练数据相匹配的格式下往往表现得更好。最佳的响应结构会因任务和智能体的不同而有很大差异。我们鼓励你根据自己的评估选择最佳的响应结构。

### 针对令牌效率优化工具响应

优化上下文的质量很重要。但优化工具响应中返回给智能体的上下文的\*\*数量\*\*也同样重要。

对于任何可能会消耗大量上下文的工具响应，我们建议实施分页、范围选择、过滤和/或截断等方法的某种组合，并设置合理的默认参数值。对于 Claude 法典，我们默认将工具响应限制为 25,000 个令牌。我们预计随着时间的推移，智能体的有效上下文长度会增加，但对上下文高效工具的需求仍将存在。

如果你选择截断回复，一定要用有用的指令引导智能体。你可以直接鼓励智能体采用更节省令牌的策略，比如在知识检索任务中进行多次小范围的针对性搜索，而不是进行一次宽泛的搜索。同样，如果工具调用引发了错误（例如在输入验证期间），你可以精心设计错误回复，清晰地传达具体且可操作的改进建议，而不是给出晦涩难懂的错误代码或回溯信息。

以下是一个截断的工具响应示例：

![This image depicts an example of a truncated tool response.](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fe440d6a69d0ca80e71f3bec5c2d00906ff03ce6d-1920x1162.png&w=1920&q=75)

This image depicts an example of a truncated tool response.

以下是一个无用的错误响应示例：

![This image depicts an example of an unhelpful tool response. ](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F2445187904704fec8c50af0b950e310ba743fac2-1920x733.png&w=1920&q=75)

This image depicts an example of an unhelpful tool response.

以下是一个有用的错误响应示例：

![This image depicts an example of a helpful error response.](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F810661bd44a35fb273806ae95160040155978c3e-1920x850.png&w=1920&q=75)

工具截断和错误响应可以引导智能体采取更节省令牌的工具使用行为（使用过滤器或分页），或者给出格式正确的工具输入示例。

### 为你的工具描述进行提示工程设计

现在我们来介绍一种改进工具最有效的方法：对你的工具描述和规格进行提示工程。由于这些会被加载到你的智能体的上下文中，它们可以共同引导智能体采取有效的工具调用行为。

在编写工具描述和规范时，思考一下你会如何向团队中的新员工描述你的工具。考虑你可能会隐含带入的上下文信息——专门的查询格式、小众术语的定义、底层资源之间的关系——并使其明确化。通过清晰描述（并使用严格的数据模型来强制执行）预期的输入和输出，避免歧义。特别是，输入参数的命名应该明确无误：不要使用名为 `user` 的参数，而尝试使用名为 `user_id` 的参数。

通过你的评估，你可以更有信心地衡量提示工程的影响。即使对工具描述进行微小的改进也能带来显著的提升。在我们对工具描述进行精确改进后，Claude Sonnet 3.5 在 [SWE-bench 验证](https://www.anthropic.com/engineering/swe-bench-sonnet) 评估中取得了领先的性能，大幅降低了错误率并提高了任务完成率。

你可以在我们的《开发者指南》中找到工具定义的其他最佳实践。如果你正在为 Claude 构建工具，我们还建议阅读有关工具如何动态加载到 Claude 的“系统提示”中的内容。最后，如果你正在为 MCP 服务器编写工具，“工具注释”有助于揭示哪些工具需要开放世界访问权限或进行破坏性更改。

## Looking ahead

为了构建适用于智能体的有效工具，我们需要将软件开发实践从可预测的、确定性的模式重新调整为非确定性的模式。

通过我们在本文中描述的迭代式、评估驱动的过程，我们已经确定了工具成功的一致模式：有效的工具经过精心且清晰的定义，明智地使用智能体上下文，可以在不同的工作流程中组合在一起，并使智能体能够直观地解决现实世界的任务。

未来，我们预计智能体与世界交互的具体机制将会不断演进——从对 MCP 协议的更新到基础 LLMs 本身的升级。通过一种系统的、以评估为驱动的方法来改进智能体的工具，我们可以确保随着智能体能力的提升，它们所使用的工具也会随之演进。

## Acknowledgements

作者：Ken Aizawa，研究团队（Barry Zhang、Zachary Witten、Daniel Jiang、Sami Al-Sheikh、Matt Bell、Maggie Vo）、MCP 团队（Theodora Chu、John Welsh、David Soria Parra、Adam Jones）、产品工程团队（Santiago Seira）、市场营销团队（Molly Vorwerck）、设计团队（Drew Roper）以及应用人工智能团队（Christian Ryan、Alexander Bricken）的同事们也做出了宝贵贡献。

<sup>1</sup> 除了训练底层的语言模型本身之外。

![Interlocking puzzle piece with complex geometric shape and detailed surface texture](https://www-cdn.anthropic.com/images/4zrzovbb/website/43abe7e54b56a891e74a8542944dfbd33f07f49c-1000x1000.svg)

### 想了解更多？

通过 Anthropic 学院的课程掌握 API 开发、模型上下文协议和 Claude 法典。完成课程后可获得证书。

## 获取开发者时事通讯

产品更新、操作指南、社区亮点等等。每月发送到您的收件箱。