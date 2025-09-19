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

Held-out test set performance of our internal Asana tools

**Analyzing results**  
Agents are your helpful partners in spotting issues and providing feedback on everything from contradictory tool descriptions to inefficient tool implementations and confusing tool schemas. However, keep in mind that what agents omit in their feedback and responses can often be more important than what they include. LLMs don’t always [say what they mean](https://www.anthropic.com/research/tracing-thoughts-language-model).

Observe where your agents get stumped or confused. Read through your evaluation agents’ reasoning and feedback (or CoT) to identify rough edges. Review the raw transcripts (including tool calls and tool responses) to catch any behavior not explicitly described in the agent’s CoT. Read between the lines; remember that your evaluation agents don’t necessarily know the correct answers and strategies.

Analyze your tool calling metrics. Lots of redundant tool calls might suggest some rightsizing of pagination or token limit parameters is warranted; lots of tool errors for invalid parameters might suggest tools could use clearer descriptions or better examples. When we launched Claude’s [web search tool](https://www.anthropic.com/news/web-search), we identified that Claude was needlessly appending `2025` to the tool’s `query` parameter, biasing search results and degrading performance (we steered Claude in the right direction by improving the tool description).

### Collaborating with agents

You can even let agents analyze your results and improve your tools for you. Simply concatenate the transcripts from your evaluation agents and paste them into Claude Code. Claude is an expert at analyzing transcripts and refactoring lots of tools all at once—for example, to ensure tool implementations and descriptions remain self-consistent when new changes are made.

In fact, most of the advice in this post came from repeatedly optimizing our internal tool implementations with Claude Code. Our evaluations were created on top of our internal workspace, mirroring the complexity of our internal workflows, including real projects, documents, and messages.

We relied on held-out test sets to ensure we did not overfit to our “training” evaluations. These test sets revealed that we could extract additional performance improvements even beyond what we achieved with "expert" tool implementations—whether those tools were manually written by our researchers or generated by Claude itself.

In the next section, we’ll share some of what we learned from this process.

## Principles for writing effective tools

In this section, we distill our learnings into a few guiding principles for writing effective tools.

### Choosing the right tools for agents

More tools don’t always lead to better outcomes. A common error we’ve observed is tools that merely wrap existing software functionality or API endpoints—whether or not the tools are appropriate for agents. This is because agents have distinct “affordances” to traditional software—that is, they have different ways of perceiving the potential actions they can take with those tools

LLM agents have limited "context" (that is, there are limits to how much information they can process at once), whereas computer memory is cheap and abundant. Consider the task of searching for a contact in an address book. Traditional software programs can efficiently store and process a list of contacts one at a time, checking each one before moving on.

However, if an LLM agent uses a tool that returns ALL contacts and then has to read through each one token-by-token, it's wasting its limited context space on irrelevant information (imagine searching for a contact in your address book by reading each page from top-to-bottom—that is, via brute-force search). The better and more natural approach (for agents and humans alike) is to skip to the relevant page first (perhaps finding it alphabetically).

We recommend building a few thoughtful tools targeting specific high-impact workflows, which match your evaluation tasks and scaling up from there. In the address book case, you might choose to implement a `search_contacts` or `message_contact` tool instead of a `list_contacts` tool.

Tools can consolidate functionality, handling potentially *multiple* discrete operations (or API calls) under the hood. For example, tools can enrich tool responses with related metadata or handle frequently chained, multi-step tasks in a single tool call.

Here are some examples:

- Instead of implementing a `list_users`, `list_events`, and `create_event` tools, consider implementing a `schedule_event` tool which finds availability and schedules an event.
- Instead of implementing a `read_logs` tool, consider implementing a `search_logs` tool which only returns relevant log lines and some surrounding context.
- Instead of implementing `get_customer_by_id`, `list_transactions`, and `list_notes` tools, implement a `get_customer_context` tool which compiles all of a customer’s recent & relevant information all at once.

Make sure each tool you build has a clear, distinct purpose. Tools should enable agents to subdivide and solve tasks in much the same way that a human would, given access to the same underlying resources, and simultaneously reduce the context that would have otherwise been consumed by intermediate outputs.

Too many tools or overlapping tools can also distract agents from pursuing efficient strategies. Careful, selective planning of the tools you build (or don’t build) can really pay off.

### Namespacing your tools

Your AI agents will potentially gain access to dozens of MCP servers and hundreds of different tools–including those by other developers. When tools overlap in function or have a vague purpose, agents can get confused about which ones to use.

Namespacing (grouping related tools under common prefixes) can help delineate boundaries between lots of tools; MCP clients sometimes do this by default. For example, namespacing tools by service (e.g., `asana_search`, `jira_search`) and by resource (e.g., `asana_projects_search`, `asana_users_search`), can help agents select the right tools at the right time.

We have found selecting between prefix- and suffix-based namespacing to have non-trivial effects on our tool-use evaluations. Effects vary by LLM and we encourage you to choose a naming scheme according to your own evaluations.

Agents might call the wrong tools, call the right tools with the wrong parameters, call too few tools, or process tool responses incorrectly. By selectively implementing tools whose names reflect natural subdivisions of tasks, you simultaneously reduce the number of tools and tool descriptions loaded into the agent’s context and offload agentic computation from the agent’s context back into the tool calls themselves. This reduces an agent’s overall risk of making mistakes.

### Returning meaningful context from your tools

In the same vein, tool implementations should take care to return only high signal information back to agents. They should prioritize contextual relevance over flexibility, and eschew low-level technical identifiers (for example: `uuid`, `256px_image_url`, `mime_type`). Fields like `name`, `image_url`, and `file_type` are much more likely to directly inform agents’ downstream actions and responses.

Agents also tend to grapple with natural language names, terms, or identifiers significantly more successfully than they do with cryptic identifiers. We’ve found that merely resolving arbitrary alphanumeric UUIDs to more semantically meaningful and interpretable language (or even a 0-indexed ID scheme) significantly improves Claude’s precision in retrieval tasks by reducing hallucinations.

In some instances, agents may require the flexibility to interact with both natural language and technical identifiers outputs, if only to trigger downstream tool calls (for example, `search_user(name=’jane’)` → `send_message(id=12345)`). You can enable both by exposing a simple `response_format` enum parameter in your tool, allowing your agent to control whether tools return `“concise”` or `“detailed”` responses (images below).

You can add more formats for even greater flexibility, similar to GraphQL where you can choose exactly which pieces of information you want to receive. Here is an example ResponseFormat enum to control tool response verbosity:

```
enum ResponseFormat {
   DETAILED = "detailed",
   CONCISE = "concise"
}
```

Here’s an example of a detailed tool response (206 tokens):

![This code snippet depicts an example of a detailed tool response.](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F5ed0d30526bf68624f335d075b8c1541be3bb595-1920x1006.png&w=1920&q=75)

This code snippet depicts an example of a detailed tool response.

Here’s an example of a concise tool response (72 tokens):

Even your tool response structure—for example XML, JSON, or Markdown—can have an impact on evaluation performance: there is no one-size-fits-all solution. This is because LLMs are trained on next-token prediction and tend to perform better with formats that match their training data. The optimal response structure will vary widely by task and agent. We encourage you to select the best response structure based on your own evaluation.

### Optimizing tool responses for token efficiency

Optimizing the quality of context is important. But so is optimizing the *quantity* of context returned back to agents in tool responses.

We suggest implementing some combination of pagination, range selection, filtering, and/or truncation with sensible default parameter values for any tool responses that could use up lots of context. For Claude Code, we restrict tool responses to 25,000 tokens by default. We expect the effective context length of agents to grow over time, but the need for context-efficient tools to remain.

If you choose to truncate responses, be sure to steer agents with helpful instructions. You can directly encourage agents to pursue more token-efficient strategies, like making many small and targeted searches instead of a single, broad search for a knowledge retrieval task. Similarly, if a tool call raises an error (for example, during input validation), you can prompt-engineer your error responses to clearly communicate specific and actionable improvements, rather than opaque error codes or tracebacks.

Here’s an example of a truncated tool response:

![This image depicts an example of a truncated tool response.](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fe440d6a69d0ca80e71f3bec5c2d00906ff03ce6d-1920x1162.png&w=1920&q=75)

This image depicts an example of a truncated tool response.

Here’s an example of an unhelpful error response:

![This image depicts an example of an unhelpful tool response. ](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F2445187904704fec8c50af0b950e310ba743fac2-1920x733.png&w=1920&q=75)

This image depicts an example of an unhelpful tool response.

Here’s an example of a helpful error response:

### Prompt-engineering your tool descriptions

We now come to one of the most effective methods for improving tools: prompt-engineering your tool descriptions and specs. Because these are loaded into your agents’ context, they can collectively steer agents toward effective tool-calling behaviors.

When writing tool descriptions and specs, think of how you would describe your tool to a new hire on your team. Consider the context that you might implicitly bring—specialized query formats, definitions of niche terminology, relationships between underlying resources—and make it explicit. Avoid ambiguity by clearly describing (and enforcing with strict data models) expected inputs and outputs. In particular, input parameters should be unambiguously named: instead of a parameter named `user`, try a parameter named `user_id`.

With your evaluation you can measure the impact of your prompt engineering with greater confidence. Even small refinements to tool descriptions can yield dramatic improvements. Claude Sonnet 3.5 achieved state-of-the-art performance on the [SWE-bench Verified](https://www.anthropic.com/engineering/swe-bench-sonnet) evaluation after we made precise refinements to tool descriptions, dramatically reducing error rates and improving task completion.

You can find other best practices for tool definitions in our [Developer Guide](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/implement-tool-use#best-practices-for-tool-definitions). If you’re building tools for Claude, we also recommend reading about how tools are dynamically loaded into Claude’s [system prompt](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/implement-tool-use#tool-use-system-prompt). Lastly, if you’re writing tools for an MCP server, [tool annotations](https://modelcontextprotocol.io/specification/2025-06-18/server/tools) help disclose which tools require open-world access or make destructive changes.

## Looking ahead

To build effective tools for agents, we need to re-orient our software development practices from predictable, deterministic patterns to non-deterministic ones.

Through the iterative, evaluation-driven process we’ve described in this post, we've identified consistent patterns in what makes tools successful: Effective tools are intentionally and clearly defined, use agent context judiciously, can be combined together in diverse workflows, and enable agents to intuitively solve real-world tasks.

In the future, we expect the specific mechanisms through which agents interact with the world to evolve—from updates to the MCP protocol to upgrades to the underlying LLMs themselves. With a systematic, evaluation-driven approach to improving tools for agents, we can ensure that as agents become more capable, the tools they use will evolve alongside them.

## Acknowledgements

Written by Ken Aizawa with valuable contributions from colleagues across Research (Barry Zhang, Zachary Witten, Daniel Jiang, Sami Al-Sheikh, Matt Bell, Maggie Vo), MCP (Theodora Chu, John Welsh, David Soria Parra, Adam Jones), Product Engineering (Santiago Seira), Marketing (Molly Vorwerck), Design (Drew Roper), and Applied AI (Christian Ryan, Alexander Bricken).

<sup>1</sup> Beyond training the underlying LLMs themselves.

![Interlocking puzzle piece with complex geometric shape and detailed surface texture](https://www-cdn.anthropic.com/images/4zrzovbb/website/43abe7e54b56a891e74a8542944dfbd33f07f49c-1000x1000.svg)

### Looking to learn more?

Master API development, Model Context Protocol, and Claude Code with courses on Anthropic Academy. Earn certificates upon completion.