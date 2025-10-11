---
title: "Chrome DevTools MCP 与 Playwright MCP 的区别"
source: "https://x.com/dani_avila7/status/1976257576644891006"
author:
  - "[[@dani_avila7]]"
published: 2025-10-11
created: 2025-10-11
description:
tags:
  - "@dani_avila7 # Chromium # Playwright # Chrome DevTools # 浏览器自动化 # UI 测试 # 问答"
---
**Daniel San** @dani\_avila7 2025-10-09

  
Chrome DevTools MCP 专用于深度调试与性能分析（追踪记录、网络检查、核心网页指标）

而 Playwright MCP 则专注于用户界面测试和浏览器自动化（如点击操作、表单填写及工作流测试）。

使用 DevTools MCP 诊断性能问题，利用 Playwright MCP 自动化用户交互并测试 UI 功能。

> 2025-10-09
> 
>   
> 真实疑问：其功能与 Playwright MCP 提供的相比有很大差异吗？

---

**KASPAR** @iamkasparp [2025-10-09](https://x.com/iamkasparp/status/1976295785877676184)

  
我肯定没正确使用 Playwright。目前我的流程是让它打开网站、截图、分析并修复，然后循环使用 Playwright 直到达成预期效果。但这个方法很少奏效，八成情况下它不会关闭上一个 Playwright 会话，导致重新打开时程序卡死。
