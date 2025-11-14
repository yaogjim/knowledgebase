---
title: "2025-11-14_Stephen4171127_说说_Anthropic_官方关于_MCP_代码执行的文章_首先这篇文章发现了俩问题_也确实是困扰大"
source: "https://x.com/Stephen4171127/status/1989062513871237256"
author:
  - "[[@Stephen4171127]]"
published: 2025-11-14
created: 2025-11-14
description:
tags:
  - "x"
  - "@Stephen4171127"
  - "mcp"
  - "tokens"
---

# 说说 Anthropic 官方关于 MCP 代码执行的文章 首先这篇文章发现了俩问题，也确实是困扰大

**熊布朗** @Stephen4171127 [2025-11-13](https://x.com/Stephen4171127/status/1989062513871237256)

说说 Anthropic 官方关于 MCP 代码执行的文章

—

https://anthropic.com/engineering/code-execution-with-mcp…

—

首先这篇文章发现了俩问题，也确实是困扰大家的。

1\. MCP 的 Tools 对 tokens 的消耗巨大，这个已经困扰我们很久了，我在用 CC 的时候，非必要，不加载 MCP。

因为预加载若干个 MCP ，还没动工，可能近 10 万的 tokens 已经嗷嗷待出了。

文章中示例：

\- GitHub MCP: 10,000+ tokens

\- Slack MCP: 8,000+ tokens

\- Database MCP: 5,000+ tokens

\- 10个 MCP 服务器 = 100,000+ tokens

——

2\. MCP 使用过程中，中间结果反复传递。每次工具调用都返回完整数据，但其实大部分时候免不了，都是必要的，文章中的示例相对极端。

——

这些是常见问题了，看看官方给出了什么解决方案。

* * *

**熊布朗** @Stephen4171127 [2025-11-13](https://x.com/Stephen4171127/status/1989062515918078070)

方案说来也特别简单，就是不预加载 MCP ，不把中间过程给 model，需要用什么工具的时候自己去找，在执行环境中把结果“算”出来，然后给模型最后的结果。

——

不把工具定义放到初始上下文中应该是目前 Agent 的通用做法了，做个一 Tools 的列表，再把文章中的例子拿出来看看

——

\# ❌

* * *

**熊布朗** @Stephen4171127 [2025-11-13](https://x.com/Stephen4171127/status/1989062517901885801)

具体的做法：

1\. 按需工具加载

——

\# 工具定义作为文件系统

tools/

├── github/

│ ├── create\_issue.md

│ ├── list\_prs.md

│ └── merge\_pr.md

├── slack/

│ ├── send\_message.md

│ └── list\_channels.md

\# Agent 只读取需要的工具

tool =