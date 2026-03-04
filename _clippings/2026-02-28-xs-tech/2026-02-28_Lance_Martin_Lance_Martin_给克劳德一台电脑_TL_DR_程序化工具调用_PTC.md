---
title: "2026-02-28_Lance_Martin_Lance_Martin_给克劳德一台电脑_TL_DR_程序化工具调用_PTC"
source: "https://x.com/RLanceMartin/status/2027450018513490419"
author:
  - "[[@Lance Martin]]"
published: 2026-02-28
created: 2026-02-28
description:
tags:
  - "x"
  - "@Lance Martin"
  - "claude"
  - "ptc"
---

# Lance Martin # 给克劳德一台电脑 TL;DR – 程序化工具调用 (PTC)

**Lance Martin**

# 给克劳德一台电脑

TL;DR – 程序化工具调用 (PTC) 是 Claude Opus/Sonnet 4.6 中一项有趣的功能。它不再像以往那样每次工具调用都要经过 Claude 的上下文，而是让 Claude 编写代码，直接在容器内协调工具调用。工具的中间结果返回到代码，而不是 Claude 的上下文窗口。这减少了令牌的使用，并提高了搜索等多步骤任务的性能。最近，搭载 PTC 的 Opus 4.6 在……中排名第一。LMArena 的搜索基准请参阅我们的文档以了解更多信息。PTC 以及我们新的网络搜索默认使用 PTC 的工具。

电脑使用是克劳德最重要的能力之一。仅仅给克劳德一个 bash 工具这开辟了广阔的行动空间，并引出了一个常见问题：bash 就是你所需要的一切 ？ 以及如何决定还要给经纪人提供哪些其他工具？

动作是克劳德与世界互动的方式。工具是一种以声明方式指定克劳德可以执行的动作的方法。API 允许您添加工具通过给 Claude 提供工具名称、描述和输入参数。

如果 Claude 想要调用一个工具，它会返回一个包含要运行的工具参数的 JSON 对象。工具处理程序（例如，MCP 服务器 （例如，你编写的代码等）运行该工具并返回上下文。如果你在一个循环中运行它，你找个代理人例如，bash 工具通过生成包含命令的 JSON 对象来生成 bash 命令。该对象将传递给 bash 工具处理器以执行：

```json
{"command": "pip install requests"}
```

何时使用工具

克劳德带着 bash 工具循环运行是一种计算机使用代理。这是 Claude Code 的核心。但 Claude Code 不仅仅使用 bash。它使用工具作为某些操作的控制界面 。参见 @trq212 的这些要点的详细分析在少数情况下，将某个操作推广到工具中是有意义的：

- 用户体验： @trq212 谈论 AskUserQuestion 工具。这个例子表明，当需要捕获特定操作并以特定方式呈现给用户时，工具非常有用。
- 安全防护措施 。某些操作需要安全防护措施。例如，文件编辑工具可以运行过期检查，以验证文件自模型上次读取以来是否已更改。
- 并发控制 。有时，根据并发安全性对操作进行分组会很有用（例如，只读工具可以并行运行）。
- 可观测性。 它可以用于隔离特定操作进行日志记录（例如，测量延迟或令牌使用情况）。
- 自主性 。您可能需要按自主级别对操作进行分组。如果框架可以撤销某个操作，那么它就可以更自由地批准该操作。

工具的问题

工具需要在控制和可组合性之间进行权衡。假设有三个操作，它们都是工具调用。每次工具调用都会将上下文返回给 Claude。每次往返都会增加延迟，将工具结果序列化为上下文（例如，即使下一步只需要五行，它也会传递数千行），并且引入一个推理步骤。组合成本会随着操作数量的增加而增加。

程序化工具调用

Claude 正在开发一种将代码可组合性与工具控制界面相结合的功能。Claude 可以执行程序化工具调用 （PTC，参见） 。 文档在此您可以像往常一样定义工具。但与单独调用工具不同，Claude 可以将它们组合成函数，并在代码执行容器中运行。每个函数的输出都会返回到容器， 而不是 Claude 的上下文窗口。

当代码调用工具（例如，\`await web\_search(query)\`）时，容器会暂停。该调用会以类型化工具使用事件的形式跨越沙箱边界。其处理方式与模型直接调用工具（例如，通过处理程序、MCP 服务器等）完全相同。但结果会返回给正在运行的代码 ，而不是返回给 Claude 的上下文窗口。代码会按照 Claude 指定的控制流处理结果（例如，调用另一个工具、过滤数据、累积结果）。只有最终输出会到达 Claude。

和作品 4.6 我们已经看到令牌效率和非编码评估（例如， 浏览竞赛和深度搜索问答为了网络搜索例如，与其让 Claude 处理 50 条原始搜索结果，不如让代码以编程方式解析、筛选和交叉引用结果。这样就能保留相关信息，丢弃其余信息（例如， 动态滤波在 BrowseComp 和 DeepsearchQA 测试中，Opus 4.6 与 PTC 结合使用，平均准确率提高了 11%，同时输入标记数量减少了 24%。目前，Opus 4.6 与 PTC 结合使用在 LMarena 的测试中排名第一。 搜索竞技场 。

考虑到这些优势，PTC 现在已内置于…… 网络搜索工具在 API 上进行优化，以提高性能并在使用搜索时节省令牌：

```json
{
  "model": "claude-opus-4-6",
  "max_tokens": 4096,
  "tools": [
 {
 "type": "web_search_20260209",
 "name": "web_search"
 },
  ],
  "messages": [
 {
 "role": "user",
 "content": < query > 
 }
  ]
}
```

PTC 提供了一种在保留工具控制界面的同时，获得代码执行优势（例如可组合性）的方法：工具实现运行在沙箱的你的一侧，而不是沙箱内部。工具处理程序仍然作为控制界面位于每次调用的中间，能够进行检查、拒绝、记录日志或排队等待人工审批。但它允许 Claude 流畅地编排代码中的操作。

* * *

### 热门回复

**@Adams Toyota** ♥ 107 · 💬 0

Tacoma or Tundra — either way, you win. 0% APR available, serious discounts on select trucks, and a Nationwide Lifetime Warranty. 300+ vehicles in stock now at Adams Toyota. Find your truck today.

**@ZeroClick** ♥ 53 · 💬 0

\*checks numbers\* ... ZeroClick has processed 35 million AI native ad impressions in the past WEEK

**@Evan Chipman** ♥ 35 · 💬 1

2025: Wow cool, Claude Code can just write this feature for me. I'll go for a walk. 2026: My agent is building a pipeline to deploy agents that automate 90% of my job. I haven't been outside in 4 days.

**@Vaclav Milizé** ♥ 4 · 💬 0

一旦查看基准测试结果，关于“bash 是否满足所有需求”的问题就不言自明了：PTC + bash + 网络搜索在可靠性方面胜过所有自定义 MCP 集成。 没人公开说出口的潜台词是：MCP 生态系统中有一半都在增加复杂性，反而让代理变得更糟，而不是更好。极简工具才是王道。

**@will** ♥ 0 · 💬 1

我不太明白容器是如何调用更多工具的？容器是通过编程方式调用的，还是 Claude 在容器内部编写了自己的 LLM 调用？