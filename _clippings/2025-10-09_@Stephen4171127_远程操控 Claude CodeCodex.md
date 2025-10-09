---
title: 远程操控 laudeCode/Codex
source: https://x.com/Stephen4171127/status/1976011856146767989
author:
  - "[[@Stephen4171127]]"
published: 2025-10-09
created: 2025-10-09
description: 
tags:
  - "@Stephen4171127"
  - "#"
  - 线上协作
  - "#"
  - 远程操控
  - "#"
  - Claude
  - Code
  - "#"
  - CodeX
  - "#"
  - AI
---
**熊布朗** @Stephen4171127 [2025-10-08](https://x.com/Stephen4171127/status/1976011856146767989)

有时候出门就没法安排家里的 AI 员工干活，作为当代资本家，tokens 消耗者，内心十分不爽。在能彻底脱手，让 AI 自助 24 小时工作之前，先解决如何用手机/平板更省事地远程操控 Claude Code/CodeX。

\_

1\. Happy 最省心，专为 Claude Code/Codex）

手机装 App（iOS/Android/web），电脑上把 claude/codex 换成 happy 或 happy codex；扫二维码即配对。会话端到端加密、可推送提醒、可随时在手机/桌面切换控制。无需自己暴露端口或折腾隧道。

https://happy.engineering

2\. SSH/Mosh + tmux（通用而稳，几乎零改造）

在 Mac 上用 tmux new -s cc 跑 claude（或 Codex CLI）；手机上用 Blink Shell 之类的终端 App 通过 SSH/Mosh 连接，tmux attach -t cc 即可无缝继续。Mosh对移动/弱网很友好（换网、锁屏后也能自动恢复），Blink 在 iOS/iPadOS 上体验成熟。配合 Tailscale SSH 可免端口映射。

3.Web 终端（ttyd / goTTY 等）+ 零信任隧道

把本地 CLI 变成浏览器可用的 Web 终端页面，然后用 Cloudflare Tunnel / Tailscale Funnel 暴露出来。上手快，但要自己做好 TLS 与鉴权（写入权限尤其要小心）

---

**未知的健忘** @Activer\_cn [2025-10-09](https://x.com/Activer_cn/status/1976095156282765421)

简单点，手机上直接codex 安排干活，不用电脑，只需要下达命令。

![Image](https://pbs.twimg.com/media/G2yADxAaAAAxqRI?format=jpg&name=large)

---

**Bezi** @bezi\_ai

With Bezi, AI meets real-time project context—no more generic snippets; every suggestion respects your hierarchy, naming conventions and packages, so it just plugs in and works.  
借助 Bezi，AI 融入实时项目情境——告别通用代码片段；每项建议都遵循您的层级结构、命名规范和包管理，实现即插即用的无缝集成。

---

**柯来** @connect\_kai [2025-10-09](https://x.com/connect_kai/status/1976103788839829551)

happy 可以在移动端切配置文件吗

---

**少濬** @tydezhang [2025-10-09](https://x.com/tydezhang/status/1976100986788999430)

CC 很快就能iOS了

---

**Lewis的随笔日志** @lewis\_memo [2025-10-09](https://x.com/lewis_memo/status/1976090881032966513)

一直用happy，确实好用

---

**eLongZ** @eLongZq [2025-10-09](https://x.com/eLongZq/status/1976136303562658276)

确实有这个需求