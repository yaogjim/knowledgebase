---
title: "纯前端实现远程 mcp 和 tiny agent"
source: "https://x.com/xincmm/status/1936760675524804618"
author:
  - "[[@xincmm]]"
created: 2025-07-01
description:
tags:
  - "@xincmm #前端 #webworker #ai #代码生成 #模型调用"
---
**xincmm** @xincmm [2025-06-22](https://x.com/xincmm/status/1936760675524804618)

纯前端配合 web worker 实现了调用远程 mcp 和 tiny agent、具体效果可以看视频 demo，可以让大模型生成 js 代码并执行，使用 ai sdk 来调用模型。使用 web worker 有很多想法，配合 markitdown 还可以解析上传的文件，web work 中处理耗时任务。

![Image](https://pbs.twimg.com/media/GuC_5yiXAAACE8O?format=jpg&name=large)

---

**xincmm** @xincmm [2025-06-22](https://x.com/xincmm/status/1936763928606056758)

完全复用了 ai sdk 的 useChat，只是实现了一个 customFetch 来和 web worker 通信

---

**xincmm** @xincmm [2025-06-22](https://x.com/xincmm/status/1936763200692957542)

我觉得你的 pagetalk 可以实现更多的功能了，像生成 mermaid，完全可以让浏览器来测试 mermaid 是否正确，不正确的话让模型重新生成。我整理一下代码，现在是让 AI 跑原型，代码有点乱
