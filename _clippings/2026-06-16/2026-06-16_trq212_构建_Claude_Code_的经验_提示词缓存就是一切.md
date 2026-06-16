---
title: "2026-06-16_trq212_构建_Claude_Code_的经验_提示词缓存就是一切"
source: "https://x.com/trq212/status/2024574133011673516"
author:
  - "[[@trq212]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "#prompt"
  - "x"
  - "@trq212"
  - "claude"
---

# 构建 Claude Code 的经验：提示词缓存就是一切

**Thariq**

# 构建 Claude Code 的经验：提示词缓存就是一切

工程领域中常有人说“缓存主宰我周围的一切”，同样的规则也适用于代理。

长期运行的智能代理产品（如 Claude Code）的实现得益于提示词缓存，这使得我们能够重用之前往返中的计算，并显著降低延迟和成本。

What is prompt caching, how does it work and how do you implement it technically?

[Read more in @RLanceMartin's piece on prompt caching and our new auto-caching launch.](https://x.com/RLanceMartin/status/2024573404888911886)

在 Claude Code，我们围绕提示词缓存构建整个系统。高提示词缓存命中率可降低成本，并帮助我们为订阅计划设置更宽松的速率限制，因此我们会监控提示词缓存命中率，若其过低则宣布 SEV。

这些是（往往不直观的）我们在大规模优化提示词缓存过程中获得的经验教训。

## 设置用于缓存的提示

![Image](https://pbs.twimg.com/media/HBipHa1boAAXD_A?format=jpg&name=large)

提示缓存通过前缀匹配实现——API 会缓存从请求开始到每个 cache\_control 断点为止的所有内容。这意味着你放置内容的顺序极为重要，你希望尽可能多的请求共享一个前缀。

完成此操作的最佳方式是先处理静态内容，最后处理动态内容。对于 Claude Code，这表现为：

1.  Static system prompt & Tools (globally cached)
2.  Claude.MD (cached within a project)
3.  Session context (cached within a session)
4.  Conversation messages

这样我们最大化了共享缓存命中的会话数量。

但这可能会出人意料地脆弱！我们之前破坏这种顺序的原因包括：在静态系统提示中放入详细的时间戳、非确定性地打乱工具顺序定义、更新工具的参数（例如 AgentTool 可以调用的代理）等。

## 使用消息接收更新

有时，你输入提示中的信息可能会过时，例如当你有时间或者用户修改了文件时。更新提示可能会很诱人，但这会导致缓存未命中，并且可能最终对用户来说成本很高。

考虑一下下次是否可以通过消息传递这些信息。在 Claude Code 中，我们会在下一次用户消息或工具结果中添加 <system-reminder> 标签，包含模型的更新信息（例如现在是星期三），这有助于保留缓存。

## 不要在会话中途更改模型

提示缓存是模型独有的，这可能会使提示缓存的计算相当难以理解。

如果你已经与 Opus 进行了 10 万个 token 的对话，并且想要提出一个比较容易回答的问题，实际上切换到 Haiku 会比让 Opus 回答更昂贵，因为我们需要为 Haiku 重建提示词缓存。

如果需要切换模型，最好的方法是使用子代理，其中 Opus 会准备一条“交接”消息给另一个需要执行该任务的模型。我们经常在使用 Haiku 的 Claude Code 中的探索代理中这样做。

## 切勿在会话期间添加或移除工具

在对话过程中更改工具集是人们破坏提示词缓存的最常见方式之一。这似乎很直观——你应该只给模型你认为它现在需要的工具。但由于工具是缓存前缀的一部分，添加或移除工具会使整个对话的缓存失效。

规划模式 — 围绕缓存设计

计划模式是围绕缓存限制设计功能的一个很好的例子。直观的方法应该是：当用户进入计划模式时，替换掉工具集，只保留只读工具。但这会破坏缓存。

相反，我们始终保留所有工具在请求中，并将 EnterPlanMode 和 ExitPlanMode 本身用作工具。当用户开启计划模式时，代理会收到一条系统消息，说明它处于计划模式以及指令内容——探索代码库，不要编辑文件，计划完成后调用 ExitPlanMode。工具定义永远不会改变。

这有一个额外的好处：因为 EnterPlanMode 是模型可以自我调用的工具，当它检测到难题时，能够自主进入规划模式，不会造成任何缓存中断。

工具搜索 — 推迟而非移除

同样的原则适用于我们的工具搜索功能。Claude Code 可以加载数十个 MCP 工具，在每个请求中包含所有这些工具的成本会很高。但在对话过程中移除它们会破坏缓存。

我们的解决方案：defer\_loading。而不是移除工具，我们发送轻量级存根——仅包含工具名称，并附带 defer\_loading: true——，模型可以通过 ToolSearch 工具在需要时"发现"这些存根。完整的工具架构仅在模型选择它们时才会被加载。

Luckily you can use the

[tool search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool) tool through our API to simplify this.

## 分支上下文 — 压缩

![Image](https://pbs.twimg.com/media/HBitEdRbUAMVSnM?format=jpg&name=large)

Compaction is what happens when you run out of the context window. We summarize the conversation so far and continue a new session with that summary.

Surprisingly, compaction has many edge cases with prompt caching that can be unintuitive.

In particular, when we compact we need to send the entire conversation to the model to generate a summary. If this is a separate API call with a different system prompt and no tools (which is the simple implementation), the cached prefix from the main conversation doesn't match at all. You pay full price for all those input tokens, drastically increasing the cost for the user.

The Solution — Cache-Safe Forking

When we run compaction, we use the exact same system prompt, user context, system context, and tool definitions as the parent conversation. We prepend the parent's conversation messages, then append the compaction prompt as a new user message at the end.

From the API's perspective, this request looks nearly identical to the parent's last request — same prefix, same tools, same history — so the cached prefix is reused. The only new tokens are the compaction prompt itself.

This does mean however that we need to save a "compaction buffer" so that we have enough room in the context window to include the compact message and the summary output tokens.

Compaction is tricky but luckily, you don't need to learn these lessons yourself — based on our learnings from Claude Code we built

[compaction](https://platform.claude.com/docs/en/build-with-claude/compaction#prompt-caching) directly into the API, so you can apply these patterns in your own applications.

## Lessons Learned

1.  提示缓存是一种前缀匹配。前缀中的任何位置发生的更改都会使之后的所有内容失效。围绕这个约束设计整个系统。正确处理顺序，大部分缓存工作都会自动有效。
2.  使用消息而非修改系统提示。你可能会想要编辑系统提示来完成诸如进入计划模式、更改日期等操作，但实际上，在对话过程中将这些内容插入消息中会更好。
3.  Don't change tools or models mid-conversation. Use tools to model state transitions (like plan mode) rather than changing the tool set. Defer tool loading instead of removing tools.
4.  Monitor your cache hit rate like you monitor uptime. We alert on cache breaks and treat them as incidents. A few percentage points of cache miss rate can dramatically affect cost and latency.
5.  Fork operations need to share the parent's prefix. If you need to run a side computation (compaction, summarization, skill execution), use identical cache-safe parameters so you get cache hits on the parent's prefix.

Claude Code is built around prompt caching from day one, you should do the same if you’re building an agent.