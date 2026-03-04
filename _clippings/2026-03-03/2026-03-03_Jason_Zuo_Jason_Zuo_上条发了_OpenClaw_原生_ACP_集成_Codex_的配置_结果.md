---
title: "2026-03-03_Jason_Zuo_Jason_Zuo_上条发了_OpenClaw_原生_ACP_集成_Codex_的配置_结果"
source: "https://x.com/xxx111god/status/2028309791102132384"
author:
  - "[[@Jason Zuo]]"
published: 2026-03-03
created: 2026-03-03
description:
tags:
  - "#29195"
  - "x"
  - "@Jason Zuo"
  - "codex"
---

# Jason Zuo 上条发了 OpenClaw 原生 ACP 集成 Codex 的配置 结果

**Jason Zuo**

上条发了 OpenClaw 原生 ACP 集成 Codex 的配置 结果这几天让 bot 跑 Codex 任务，发现它根本没走 ACP，一直 fallback 回 PTY spawn 老路径 🤡 查了半天，发现 acpx 插件不读 ~/.acpx/config.json，只从 OpenClaw 主 config 拿配置。但 permissionMode 不能直接放在 plugins.entries.acpx 下面，要再套一层 .config. 最后在 OpenClaw GitHub issues（#29195）找到了正确路径： plugins.entries.acpx.config.permissionMode = "approve-all" 少这一层 .config.，Codex 每次都卡在权限确认然后超时退出 （太脑残了） 修好后直接拿来推 AWI -Agentic Web Interface（刚开源的一个 自己Go 写的网页抓取工具，专门给 AI agent 用的，装完就能跑不用配任何东西） sessions\_spawn( runtime="acp", agentId="codex", task="Fix README paths. Add go test to CI. Add --version flag." ) 5 个任务，十分钟全写完 关键是Opus给的指令够具体，反正别让 Codex 自己理解需求，它不行。正确的流程： • Claude 分析项目 → 拆成具体任务 • 每个任务给 Codex 精确指令：改哪个文件、改成什么样 • Codex 写完 → Claude review 结果 几个注意事项： • acpx --approve-all 这个 flag 放 codex 前面，放后面静默忽略 • Codex 不能自己 go build / npm test，写完就停了，验证得你来 • 依赖版本会编，go.mod 改完手动 go mod tidy 确认一下 • 模糊指令（"优化这个模块"）出来的东西大概率要重做 目标就是让 Claude 当指挥大脑，Codex 负责写代码，互相 cross check。Claude 拆任务 review 质量，Codex 出活快，谁也别单干

> **@xxx111god**
> 
> 昨天刚发完这条，今天OpenClaw就更新支持原生ACP first-class了 之前我是自己 hack 的： • PTY spawn Codex 进程 • 屏幕抓取解析 ANSI escape codes • 手动维护 session 状态和 timeout • 输出不是 JSON，调试全靠 print 属于是能用，但是slow and dirty 现在直接配置OpenClaw： acp.enabled = x.com/xxx111god/stat…

* * *

### 热门回复

**@Jamf** ♥ 133 · 💬 0

Stop the manual grind that's slowing onboarding and exhausting your team. See how.

**@mblank** ♥ 0 · 💬 1

@grok acp是啥

**@QingYue** ♥ 1 · 💬 0

好文！这就拿回去试试看

**@thyself Know** ♥ 0 · 💬 0

acp 支持 cc 没