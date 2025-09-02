---
title: "关于 ZEd ACP 代理的讨论"
source: "https://x.com/blackanger/status/1961126887335588186"
author:
  - "[[@blackanger]]"
published: 2025-08-29
created: 2025-08-29
description:
tags:
  - "@blackanger"
---
**AlexZ** @blackanger [2025-08-28](https://x.com/blackanger/status/1961126887335588186/history)

看了下 Zed 刚出的 ACP 协议，虽然它设计面向“编辑器 ↔ 代理”的标准化通信场景，但本质上还是一个通过 JSON-RPC 交流的协议。

我在想，如果把我的 AI Workflow 封装成 ACP 代理进程，然后让 Zed 来调用我的 Workflow ，而我的 Workflow 已经实现了多 Provider （包括 claude code / codex）的集成，以及 mcp 的支持。

那么，这会产生一个什么效果？

---

**迈克 Mike Chong** @mike\_chong\_zh [2025-08-28](https://x.com/mike_chong_zh/status/1961141569568059651)

我觉得：产生的直接效果就是很多 AI 开源项目就没必要了。。。直接包一个 AI coding agent 做出来的产品就可以直接拿出去卖了！

---

**AlexZ** @blackanger [2025-08-28](https://x.com/blackanger/status/1961142571016790491)

😅我先实现出来看看

---

**Jintao Zhang 张晋涛** @zhangjintao9020 [2025-08-29](https://x.com/zhangjintao9020/status/1961242382785286444)

🤣 可你如果不套这个 ACP 继续用 MCP 不也可以的么

---

**AlexZ** @blackanger [2025-08-29](https://x.com/blackanger/status/1961274046508847449)

可以是可以，但目前感觉workflow能有个界面更好一些，我还在看日志。。

---

**不鍊金丹不坐禪** @zzwz [2025-08-29](https://x.com/zzwz/status/1961237426376249455)

可能产生效果之一:

\[Coding Agent CLI\] --ACP-- as Code-Act Agent -- as 泛化通用型"可动态/一次性"的 万能工具 (且 纯文本流, 上层无需过多适配).

能帮一些上层 DSL 类代理节点提高泛化能力, 灵活性...

PS: any cli-tools & pypi, npm... 全都是 "Code-Act Agent as Universal Tool" 的工具箱

---

**夜奏花** @O\_\_Ollllllllll [2025-08-29](https://x.com/O__Ollllllllll/status/1961258742722564391)

给你的agent 加了一个ui ❓
