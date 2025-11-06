---
title: "2025-11-06_dotey_对于向深入学习上下文工程_Context_Engineering_的同学_这又是一篇必看的文章_这"
source: "https://x.com/dotey/status/1985927706035269731"
author:
  - "[[@dotey]]"
published: 2025-11-06
created: 2025-11-06
description:
tags:
  - "x"
  - "@dotey"
  - "mcp"
  - "https"
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

# 对于向深入学习上下文工程（Context Engineering）的同学，这又是一篇必看的文章。 这

**宝玉** @dotey 2025-11-04

对于向深入学习上下文工程（Context Engineering）的同学，这又是一篇必看的文章。

这篇文章讲的是如何解决 MCP 工具太多的问题，但凡你做过 Agent 开发，用了大量 MCP 工具，就会知道 MCP 工具多了后最大的问题就是上下文占用太多，不仅导致成本高，还会影响推理和生成质量。

另外一个问题就是 MCP 工具返回的中间结果也会挤占大量的上下文空间。

看这文章的时候忍不住夸了一下 Manus，他们确实在上下文工程方面探索的很深入了，里面的工程技巧和他们以前分享过的很类似（我一会把之前分享过的 Manus 相关的文章在评论也发一下）。

Anthropic 的方案也很简单直接，就是把“代码”也当作工具的一种，然后从代码中去调用 MCP。

这样做有很多好处：

1\. 解决了系统提示词中工具定义太多的问题

不需要在系统提示词中加载所有 MCP 工具，只需要定义一个“代码”工具。

那需要工具了怎么办呢？

这些代码都保存在统一的目录下，去目录检索下就能找到合适的工具了，比如这是文中的一个目录示例：

servers

├── google-drive

│ ├── getDocument.ts

│ ├── ... (other tools)

│ └── index.ts

├── salesforce

│ ├── updateRecord.ts

│ ├── ... (other tools)

│ └── index.ts

└── ... (other servers)

找不到现成的工具怎么办？

直接现写一个！写完了还可以保存起来下次继续用。

2\. 解决了 MCP 工具返回结果太长的问题

比如说我们要用 MPC 工具获取 1 万行数据后筛选转换出合格的数据，就可以先从代码中调用 MCP 工具获取这 1 万行数据，然后从代码中去筛选过滤，最后只返回 5 条数据，这样上下文中就只需要保留那 5 条过滤的数据，而不是像以前一样有 1 万条数据在里面。

3\. 解决了数据隐私问题

如果你直接使用 MCP 工具，工具返回的数据都要加载到上下文每次上传给 LLM，用代码就可以对敏感数据先二次处理再加到上下文

4\. 中间结果持久化和技能沉淀

代码可以把一些中间结果写入文件保存到硬盘，一方面可以不占用上下文空间，另一方面也可以随时从硬盘避免反复调用 MCP。

还有就是虽然很多代码是临时生成的，但是这些临时生成的代码可以保存下来，沉淀为“技能”（Skill），加上 SKILL .MD 文件就和 Claude Code 的技能一样可以被反复使用了。

> 2025-11-04
> 
> New on the Anthropic Engineering blog: tips on how to build more efficient agents that handle more tools while using fewer tokens.
> 
> Code execution with the Model Context Protocol (MCP): https://anthropic.com/engineering/code-execution-with-mcp…
> 
> ![Diagram illustrates MCP system architecture with model on left connected to context client in center and MCP server on right. Client layer includes tool def tool use and tool result modules. Server layer shows user msg1 call tool1 user msg2 call tool2 user msg3. Assistants depicted as colored rectangles labeled assistant1 and assistant2. Connections via arrows indicate data flow between components. Overall structure uses boxes lines and labels for technical visualization.](https://pbs.twimg.com/media/G49ut7vX0AAVZ8C?format=jpg&name=large)

* * *

**宝玉** @dotey [2025-11-05](https://x.com/dotey/status/1985927708656742607)

可能有人还记得 2023 年 @DrJimFan 他们团队做的一个玩 Minecraft 的 Agent Voyager，就能把玩游戏的技能写成代码，保存起来后续使用，最终让 Agent 在 Minecraft 中做很多事。现在想想还是蛮超前的。

> 2023-05-26
> 
> What if we set GPT-4 free in Minecraft? ⛏️
> 
> I’m excited to announce Voyager, the first lifelong learning agent that plays Minecraft purely in-context. Voyager continuously improves itself by writing, refining, committing, and retrieving \*code\* from a skill library.
> 
> GPT-4 unlocks

* * *

**宝玉** @dotey [2025-11-05](https://x.com/dotey/status/1985928224329642315)

Manus 把工具分成了 3 层，预定义了很多 Shell 工具，也是让 Agent 通过文件系统直接检索，另外也会实时编写 Python 代码来创造工具

> 2025-10-17
> 
> 确实，Manus 很聪明，他们把工具分成了 3 层：
> 
> 第 1 层：函数调用 (Function Calling)
> 
> 这是最基础的一层，只保留一小组固定的、原子化的函数，比如：读写文件、执行 Shell 命令、搜索文件等。在 LLM 的系统提示词中就只有这一层的工具定义，相对比较少，15 x.com/Yonah\_x/status…
> 
> ![Image](https://pbs.twimg.com/media/G3b0_NUWcAAl8y9?format=jpg&name=large)

* * *

**宝玉** @dotey [2025-11-05](https://x.com/dotey/status/1985928226334449771)

Manus 早期分享的《AI 智能体的上下文工程：构建 Manus 的经验教训》

> 2025-07-21
> 
> Manus 这篇文章《AI 智能体的上下文工程：构建 Manus 的经验教训》对于做 Agent 的同行很有借鉴意义，这篇文章内容干货很多，这些经验不是真的踩了很多坑是写不出来的，能这么无私的分享出来还是挺难的的，必须给他们点个赞。
> 
> 但这篇文章写的相对比较专业和技术化，不太容易理解，需要你有一定的 x.com/ManusAI/status…
> 
> ![Image](https://pbs.twimg.com/media/GwVu0JvWcAATUq0?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/GwVu7LJXoAAhkAh?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/GwVvAesW4AEOe8r?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/GwVvCeUXoAAGXa4?format=jpg&name=large)