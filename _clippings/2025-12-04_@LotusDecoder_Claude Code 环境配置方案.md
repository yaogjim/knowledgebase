---
title: "Claude Code 环境配置方案"
source: "https://x.com/LotusDecoder/status/1996051137108345097"
author:
  - "[[@LotusDecoder]]"
date: "2025-12-04T15:15:05+08:00"
created: 2025-12-04
description:
tags:
  - "@LotusDecoder # Claude Code # Docker # Opus # GLM # K2 # Kimi # SSH # tmux"
---
**LotusDecoder** @LotusDecoder [2025-12-03](https://x.com/LotusDecoder/status/1996051137108345097)

研究了 Claude code 环境配置方案，考虑生产级开发，  
  
\- 整体稳定性最优。依赖少。  
  
New-API (聚合 Opus + GLM-4.6)

│ │

│ ▼

│ Docker 容器 (安全隔离)

│ │

│ └── 原生 Claude Code

│ │

│ ├── 主窗口 Opus (规划/验收)

│ └── Subagent GLM-4.6 (开发)

│

│ 访问方式：

│ ├── 本地: 直接终端

│ └── 移动端: SSH + tmux (手机/其他设备)

│

│ 不需要：

│ ├── Claude-code-router (不需要自动任务分流)

│ ├── CC-Switch (手动管理配置足够)

│ └── Happy (SSH + tmux 更稳定)

---

**熊布朗** @Stephen4171127 [2025-12-03](https://x.com/Stephen4171127/status/1996115009877770716)

哥，GLM 4.6 做不了严肃开发任务，当然，要是你说 opus 把代码都写好了，让 GLM4.6 去誊上去，那没问题。

---

**LotusDecoder** @LotusDecoder [2025-12-03](https://x.com/LotusDecoder/status/1996148702470410454)

做点小东西还够用，

让 Opus-4.5 写详细文档，

交给 subagent glm 写代码。

Opus-4.5 再验收。

主要 glm 可以包年，实现 sonnet-4 级 model 自由。
