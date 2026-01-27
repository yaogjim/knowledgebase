---
title: "Ashpreet Bedi on X: "Agents Need a Database" / X"
source: "https://x.com/ashpreetbedi/status/2015935966268018823"
author: ""
created: 2026-01-27 13:40:32
date: 2026-01-27 13:40:32
description: ""
tags: ""
---
推理核心不记得它收到的消息。它不记得自己发起的工具调用。它不记得用户偏好、多步骤计划，也不记得三轮前发生的事情。

如果推理核心是无状态的，那么状态必须存在于某个地方。

-   跨会话继续对话
    
-   记住用户偏好、历史和上下文
    
-   通过从每次互动中学习来变得更好
    
-   当它们失败时可以被调试
    
-   给我们结构化数据来评估和改进
    

是这么回事：就连我最爱的 Claude 也不会“记住”任何东西。当它想起我的名字或提到过去的对话时，其实是从注入到上下文的存储记忆中读取，或者在运行时搜索这些记忆。我们体验到的连续性并不是 LLM 的属性，而是由数据库驱动的精妙工程。我们的代理也应该这样工作。

我们可以忽略这个。大多数教程都这么做。但这样一来，我们的助手会忘记请求之间的一切，无法从错误中学习，也让我们无法调试失败或改进性能。

或者我们可以将状态视为基础原语，释放无状态包装器无法触及的能力。

-   完整上下文控制: 决定什么内容会进入上下文窗口。阅读之前的消息。包含最后3轮对话、10轮对话或者只是一个总结。上下文是我们的护城河，我们掌控它。
    
-   更智能的上下文管理： 总结冗长的对话。压缩冗长的工具输出。修剪无关的历史记录。用检索到的知识丰富内容。这才是优秀的智能体工程的真谛：为正确的响应提供正确的上下文。
    
-   零供应商依赖: 无出口费用。无留存成本。没有“我们要弃用这个 API”的邮件。用 SQL 查询我们自己的数据。构建一个快速仪表盘，或者集成到任何可观测性工具中。我们的数据。我们的选择。
    
-   评估数据集：提取示例，构建少样本提示词，进行多轮模拟。标记低质量回答以供审核。全程无需向供应商请求导出。
    
-   自学习循环：跟踪用户编辑了哪些回复。哪些工具调用失败了。哪些会话以沮丧告终。自动将这些反馈回系统。
    

```
from agno.agent import Agent
from agno.db.sqlite import SqliteDb

agent = Agent(
    db=SqliteDb(db_file="agent.db"),
    add_history_to_context=True,
    num_history_runs=3,
)
```

三行代码。这个代理现在能保持会话、包含对话历史，并让我们完全控制我们的数据。

```
# Access your data directly
history = agent.get_chat_history(session_id="session_123")
messages = agent.get_session_messages(session_id="session_123")
session = agent.get_session(session_id="session_123")

# Long conversations? Summarize them automatically
agent = Agent(
    db=SqliteDb(db_file="agent.db"),
    enable_session_summaries=True,   # Compress old context
    store_tool_messages=False,       # Skip the bloat
)
```

没有 API 调用。没有导出请求。不用等供应商开发你需要的功能。只需 SQL。

```
from agno.db.mongodb import MongoDb
from agno.db.postgres import PostgresDb
# ...13+ databases supported

db = PostgresDb(db_url="postgresql://user:pass@localhost:5432/mydb")
agent = Agent(db=db)
```

SQLite 用于测试。Postgres 用于生产。我们的基础设施。我们的数据。

行业已经将在别人的数据库中存储我们的数据视为常态。

Responses API 给我们提供了一个 \`previous\_response\_id\`。托管内存服务保存了我们的上下文。这很方便，但存在值得考虑的权衡因素。

我们要付双份费用：一次是 API 调用，另一次是存储和流出费用。我们依赖他们的架构、导出工具和路线图。需要某个功能时，我们提交工单然后等。他们出故障，我们也会受影响。

关键是：我们还是需要一个数据库。那个\`response\_id\`？我们把它存在某个地方。用户会话？那个在我们的系统里。我们刚刚把状态拆分到两个地方，还加了一次网络跳转。

代理需要数据库的原因和网页应用需要数据库的原因一样：无状态计算需要有状态存储。这些模式并不新鲜，只是我们忘了怎么用它们。

Agno 是面向代理的开源基础设施。内置了数据库支持。