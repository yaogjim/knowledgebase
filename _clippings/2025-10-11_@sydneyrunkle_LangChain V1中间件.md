---
title: "LangChain V1中间件"
source: "https://x.com/sydneyrunkle/status/1976753314462417344"
author:
  - "[[@sydneyrunkle]]"
published: 2025-10-11
created: 2025-10-11
description:
tags:
  - "@sydneyrunkle # LangChain # 中间件 # AI"
---
**Sydney Runkle** @sydneyrunkle [2025-10-10](https://x.com/sydneyrunkle/status/1976753314462417344/history)

  
LangChain V1 中间件在 30 秒内快速解析：

在代理启动前 — 加载文件，验证输入

before\_model — 汇总对话内容，精简消息

wrap\_model\_call — 动态提示、模型与工具调用

包装工具调用——工具重试、错误处理

🤵 模型后处理 — 人工介入循环

💾 代理之后 — 保存结果，最终防护措施

超级灵活！超级强大！

![Flowchart diagram with purple rectangular nodes connected by arrows depicting a vertical process from top request to bottom result, including before_agent, before_model, after_model, after_agent nodes in sequence, and a diamond shape in the middle connected bidirectionally to wrap_tool_call on the left with tools label and wrap_model_call on the right with model label.](https://pbs.twimg.com/media/G27VXRZXMAAxEg1?format=png&name=large)