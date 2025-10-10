---
title: "深度搜索代理 (DeepSearchAgents) Web UI开发中的体验"
source: "https://x.com/zzwz/status/1949794596591964223"
author:
  - "[[@zzwz]]"
created: 2025-07-29
description:
tags:
  - "@zzwz #深度搜索代理 #WebUI #交互设计 #混合沙盒 #异步流式 #可视化工具"
status: "inbox"
importance: 2
effort: 2
review_level: 0
review_next: "2025-10-17"
review_interval: null
review_count: 0
decision: null
topics: []
links_out: []
summary: ""
pov: ""
actions: []
---
**不鍊金丹不坐禪** @zzwz [2025-07-28](https://x.com/zzwz/status/1949794596591964223)

这两天 Debug DeepSearchAgents 的 Web 过程中费劲儿解决的一个个 stream to web UI 的 bug 体验:

1\. GUI 还是很重要的, 是大众人类用户逐渐信赖👻硅基智能很重要的一环 (不可能人人都是"程序员", 即使是 VIBE 程序员);

2\. Manus, 天工 这些 ...

![Image](https://pbs.twimg.com/media/Gw8P09VbYAENQie?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/Gw8P1h1aMAAhDBI?format=jpg&name=large)

---

**不鍊金丹不坐禪** @zzwz [2025-07-28](https://x.com/zzwz/status/1949794668503584831)

2\. Manus, 天工 这些 Agent 混合沙盒UI 一开始就花心思给用户看的产品决策👍, UI"伪沙盒" 想丝滑起来细节爆炸, 但也值得;

3\. 设计混合沙盒与 Agent 架构时一定要提前把沙盒架构与异步的流式 UI消息充分解耦!

4\. ...

---

**不鍊金丹不坐禪** @zzwz [2025-07-28](https://x.com/zzwz/status/1949794705346052471)

4\. Artifacts & Canvas ... 等可视化渲染工具的非前端部分也会是混合沙盒的一部分 (Browser/VM/Py-interpreter/shell)