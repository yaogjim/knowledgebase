---
title: "2026-03-03_Jason_Zuo_Jason_Zuo_昨天刚发完这条_今天OpenClaw就更新支持原生ACP_first_c"
source: "https://x.com/xxx111god/status/2027552065111630317"
author:
  - "[[@Jason Zuo]]"
published: 2026-03-03
created: 2026-03-03
description:
tags:
  - "x"
  - "@Jason Zuo"
  - "codex"
  - "claude"
---

# Jason Zuo 昨天刚发完这条，今天OpenClaw就更新支持原生ACP first-c

**Jason Zuo**

昨天刚发完这条，今天OpenClaw就更新支持原生ACP first-class了 之前我是自己 hack 的： • PTY spawn Codex 进程 • 屏幕抓取解析 ANSI escape codes • 手动维护 session 状态和 timeout • 输出不是 JSON，调试全靠 print 属于是能用，但是slow and dirty 现在直接配置OpenClaw： acp.enabled = true acp.backend = "acpx" acp.defaultAgent = "codex" acp.allowedAgents = \["codex", "claude", "gemini"\] Claude 可以直接 sessions\_spawn(runtime="acp", agentId="codex") WebSocket 传输，结构化 JSON 输出，thinking / tool\_calls / done 状态机，官方维护 session 生命周期 还支持 named sessions（-s backend -s frontend 并行）和 prompt queue（上一个还在跑可以排队下一个） 折腾了一下午把配置迁移过去，顺便把之前的 hack 代码删了🤣

![图片](https://pbs.twimg.com/media/HCF19sAW0AEc3Wt?format=jpg&name=large)

> **@xxx111god**
> 
> Codex CLI 昨天更新支持 多Agent，果断把它接进 OpenClaw 了。 之前没接是因为 Codex 单独用不够聪明，写代码快，但理解需求和记上下文是真不太行 现在的架构： Claude = 大脑 记住上下文、拆任务、做决策 Codex = 双手 沙盒改代码、多agent并行执行、自动跑测试 Claude Opus拆成 3 个任务 给Codex

![引用图片](https://pbs.twimg.com/media/HCF19sAW0AEc3Wt?format=jpg&name=large)

* * *

### 热门回复

**@Save Our States** ♥ 684 · 💬 37

NEW AD: The big banks that closed President Trump's bank accounts want to SABOTAGE his affordability agenda. Tell President Trump: Keep big bank hidden fees out of the open banking rule.

**@Jason Zuo** ♥ 1 · 💬 1

相对来说用Claude多一些

**@Fahmi Yumi** ♥ 0 · 💬 1

想请问 您的 claude 和 chatgpt 都是属于 primary agent吗？

**@nk912114** ♥ 0 · 💬 0

claude code cli支持？好像它不支持acp吧？

**@rootial** ♥ 0 · 💬 0

貌似claude cli没法支持，只支持codex