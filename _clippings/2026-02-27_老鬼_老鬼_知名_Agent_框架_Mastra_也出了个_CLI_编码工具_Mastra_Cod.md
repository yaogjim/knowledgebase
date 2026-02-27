---
title: "2026-02-27_老鬼_老鬼_知名_Agent_框架_Mastra_也出了个_CLI_编码工具_Mastra_Cod"
source: "https://x.com/laogui/status/2027066517142356273"
author:
  - "[[@老鬼]]"
published: 2026-02-27
created: 2026-02-27
description:
tags:
  - "x"
  - "@老鬼"
  - "mastra"
  - "ai"
---

# 老鬼 知名 Agent 框架 Mastra 也出了个 CLI 编码工具 Mastra Cod

**老鬼**

知名 Agent 框架 Mastra 也出了个 CLI 编码工具 Mastra Code，最大的特色是“永不丢失上下文”。 在使用传统编码 Agent 进行长对话时，开发者经常需要面对“上下文窗口耗尽”的问题，Agent 会被迫压缩（Compact）历史对话，导致 AI “遗忘”之前的关键设定。 Mastra Code 推出一个叫观察性记忆（Observational Memory）引擎： 会持续观察并监控你与 AI 之间的交互和对话，从而自动提取、生成并留存上下文记忆，全部存储在本地的 LibSQL (SQLite) 数据库中 。 这种设计确保了数据不会离开本地开发环境，并且官方宣称实现了“无压缩停顿且无明显性能衰退”，让其成为一个“永不遗忘”的编程助手 。 Mastra Code 本质上是 Mastra 这个开源 TypeScript AI 框架的一个能力展示，支持 MCP、Hook 和Subagents。可以接入 Claude Code 和 Codex 订阅以及其他大模型厂商 API。