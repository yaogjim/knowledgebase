---
title: "让Claude Code 使用其他AI模型 "
source: "https://x.com/dotey/status/1932231895682589162"
author:
  - "[[@dotey]]"
created: 2025-06-11
description:
tags:
  - "@dotey claude-bridge"
  - "claude-trace"
---
**宝玉** @dotey 2025-06-04

如果你想你的 Claude Code 能使用 Claude 之外的 AI 模型，比如 o3、Gemini 2.5 pro，你可以试试 claude-bridge，它可以使用 Claude Code 拦截并转换 API 请求，让你可以轻松集成 OpenAI、Google 等多个大语言模型服务。当然还是搭配 Claude 4 Opus、Sonnet 效果最佳，建议还是考虑 Claude Max 订阅。

> 2025-06-04
> 
> 如果你使用 ClaudeCode，推荐试试claude-trace，它可以记录所有 claudecode 的请求日志，包括 prompt，所有内容会保存在一个 html 文件中，方便查看。它的原理很巧妙，就是自己先启动过，然后注入修改 nodejs 的 global.fetch API，然后再通过它启动 ClaudeCode，这样后续 ClaudeCode x.com/badlogicgames/…

---

**宝玉** @dotey [2025-06-10](https://x.com/dotey/status/1932231942503838139)

项目地址：https://github.com/badlogic/lemmy/tree/main/apps/claude-bridge…

---

**jinghui su** @sujingshen [2025-06-10](https://x.com/sujingshen/status/1932274189781860853)

请教一下宝玉老师，Claude code能否多个进程同时跑？即几个项目同时运行那种。

---

**宝玉** @dotey [2025-06-10](https://x.com/dotey/status/1932280844007219557)

可以的，不同目录和终端下打开