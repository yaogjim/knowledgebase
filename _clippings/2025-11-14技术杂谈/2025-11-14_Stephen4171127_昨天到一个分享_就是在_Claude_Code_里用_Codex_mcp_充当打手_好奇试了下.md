---
title: "2025-11-14_Stephen4171127_昨天到一个分享_就是在_Claude_Code_里用_Codex_mcp_充当打手_好奇试了下"
source: "https://x.com/Stephen4171127/status/1989095732285153614"
author:
  - "[[@Stephen4171127]]"
published: 2025-11-14
created: 2025-11-14
description:
tags:
  - "x"
  - "@Stephen4171127"
  - "https"
  - "cc"
status: "inbox"
importance: 2
effort: 2
review_level: 0
review_next: "2025-12-10"
review_interval: null
review_count: 0
decision: null
topics: []
links_out: []
summary: ""
pov: ""
actions: []
---

# 昨天到一个分享，就是在 Claude Code 里用 Codex（ mcp ）充当打手，好奇试了下，

**熊布朗** @Stephen4171127 [2025-11-13](https://x.com/Stephen4171127/status/1989095732285153614)

昨天到一个分享，就是在 Claude Code 里用 Codex（ mcp ）充当打手，好奇试了下，然后又改造成了一版 Skill，我再测试下看看，确定不是脱裤子放屁以后再分享出来。

——

我确实遇到 Claude Code 和 Codex 没法交换上下文这样的小问题，而且没法只用 Codex 是因为有些任务太慢了，原来只能看个短视频的，现在都能看半部电影了。

![Screenshot displays a GitHub repository page for Claude Code Workflow Orchestrator Skill with installation guide in Chinese, including steps for Node.js version 18.x or higher, cloning project via git, installing dependencies with npm install, configuring claude_desktop.conf.json, supporting Windows macOS Linux, and mentions integration of thinking with ctrl+t to hide tasks using 40 2.2k tokens.](https://pbs.twimg.com/media/G5quunDW8AA5rrx?format=jpg&name=large)

* * *

**Leun Ho** @kRonos13v [2025-11-14](https://x.com/kRonos13v/status/1989127801858101297)

同步阻塞运行的话其实应用场景很小的，可以看看我这个，可以同时开无数个 codex 子进程，然后还能继续跟你交互。也可以看看我 github 首页，还有同类型的 cc mcp 和 gemini cli mcp，都是异步运行。 不过这种多 agent 协作的最佳应用场景其实未必是 coding ，看想象力了

* * *

**Leun Ho** @kRonos13v [2025-11-14](https://x.com/kRonos13v/status/1989128994516566319)

其中一个场景是这样的：我跟 cc 提出一个科学设想，他开始把任务分配给多个 cc，用 PubMed mcp 按不同方向检索文献，让他们把结果保存在本地而不读取，仅报告（减少主 cc 的上下文损耗）。接着 cc 再派出 gemini cli ，利用1M 上下文，读取所有结果并写成综述，同样存在本地。