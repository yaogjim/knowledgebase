---
title: "2026-01-14_yan5xu_突然想到一个通用的_agents_框架_只要一个沙盒_llm_tools_就两类_文件操作和_she"
source: "https://x.com/yan5xu/status/2007982011433296005"
author:
  - "[[@yan5xu]]"
published: 2026-01-14
created: 2026-01-14
description:
tags:
  - "x"
  - "@yan5xu"
  - "https"
  - "2026-01-05"
---

# 突然想到一个通用的 agents 框架。只要一个沙盒+llm，tools 就两类，文件操作和 she

**yan5xu** @yan5xu [2026-01-05](https://x.com/yan5xu/status/2007966550737957231)

突然想到一个通用的 agents 框架。只要一个沙盒+llm，tools 就两类，文件操作和 shell 命令，所有工具都是通过程序的方式提供。工具提供 -h 简单描述 和 --help 详细描述。每个目录都有一个自描述文件，说明当前目录做什么的，关联了哪些工具（包括简单描述），哪些方法论。所有通过自描述完成。

那么 agents开发，就可以简化成为，目录设计，工具开发，方法论设计！!!

* * *

**DinoDeer** @xDinoDeer [2026-01-05](https://x.com/xDinoDeer/status/2007977307223228896)

不考虑 token 成本是可以这样做的。我看到 Manus 绝大部分工作都是通过这种方式处理了。

* * *

**yan5xu** @yan5xu [2026-01-05](https://x.com/yan5xu/status/2007982011433296005)

我想到一个很棒的低成本压缩方式，agentic loop 里面每个 fc 有结果之后，拿到小模型总结这次调用做了什么，形成一个 log，因为缓存命中了，所以成本不会太高；到达上下文阈值之后，就可以通过 log+summary，开新 session；上下文最大限度保留

* * *

**yan5xu** @yan5xu [2026-01-05](https://x.com/yan5xu/status/2007987120791793951)

甚至都不用小模型，用原来模型，因为前缀是一致的，成本只会多出来 log 部分的 output token

* * *

**David Protein** @david\_protein

Rigorously Perfected Protein.

David delivers 28g of protein, 150 calories, and 0g of sugar, equating to 75% of its calories from protein. Available in 8 core, indulgent flavors.

Buy 4 cartons on our site, and get the 5th free.

严谨优化的蛋白质

David 含有 28 克蛋白质、150 卡路里、0 克糖，其卡路里的 75%来自蛋白质。有 8 种核心的、令人满足的口味可供选择。

在我们网站上买4箱，第5箱免费。

* * *

**yan5xu** @yan5xu [2026-01-05](https://x.com/yan5xu/status/2007983645454487640)

比较久远的，就再 归档，只留下 summary 在上下文里面

* * *

**Anynomous** @sixwell [2026-01-14](https://x.com/sixwell/status/2011313691913023964)

很早之前就一直这么处理的。用qwen3 0.6b做summary放到缓存。对于连续调用有前后关系，用图dag来做映射。本质上窗口满了，开新窗口。读一遍就行。