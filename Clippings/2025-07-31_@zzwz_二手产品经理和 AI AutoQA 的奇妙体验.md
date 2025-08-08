---
title: "AI 辅助修复 Bug 的新模式"
source: "https://x.com/zzwz/status/1950496526322765832"
author:
  - "[[@zzwz]]"
created: 2025-07-31
description:
tags:
  - "@zzwz #AI #产品经理 #AutoQA #软件测试"
---
**不鍊金丹不坐禪** @zzwz [2025-07-30](https://x.com/zzwz/status/1950496526322765832)

二手产品经理 "全沾干中学" 和 claude code 一起 AutoQA Fixed 的感觉太奇妙了! 像极了把以前带的团队里的(前/后端)+测试 同事拉到一起 "冲刺" Debug 的加班时光 🙌

![Image](https://pbs.twimg.com/media/GxGOPJZbAAABtDH?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/GxGOPprbkAAf3C-?format=jpg&name=large)

---

**LinearUncle** @LinearUncle [2025-07-30](https://x.com/LinearUncle/status/1950497503234928938)

这个有点厉害的，我看很多老外也都在做。上次看有个文档驱动的产品，那个老外也是用browser相关的mcp在做autofix.

估计做AI mvp的那几个知名站点目前也是采用了类似技术。

---

**不鍊金丹不坐禪** @zzwz [2025-07-30](https://x.com/zzwz/status/1950498621469962454)

就让他用你项目技术栈的自动化测试库按照 产品和issues 的debug后写的测试计划，用相应的库写测试工具就行，我让TA直接用 playwright 无头加各种对应的前后端打点相结合自己搓TA自己的调试&回归测试脚本自己运行/观测/分析/reDeBug … Loop —> issues fixed report

---

**LinearUncle** @LinearUncle [2025-07-30](https://x.com/LinearUncle/status/1950496921048785296)

为啥叫二手产品经理？是因为以前是工程师吗？现在做产品？

---

**不鍊金丹不坐禪** @zzwz [2025-07-30](https://x.com/zzwz/status/1950497111969034376)

因为以前是产品经理➕项目经理 🤦

---

**LinearUncle** @LinearUncle [2025-07-30](https://x.com/LinearUncle/status/1950497847411118241)

那你也太强了 我看你技术顶尖呀

居然不是专业工程师？

推上啥牛人都有，你和那个巴黎产品经理都是agent方面的高手。

---

**不鍊金丹不坐禪** @zzwz [2025-07-30](https://x.com/zzwz/status/1950506445595922547)

都是 LM 结对伙伴有耐心, 感谢 gpt3--> LM 一路陪伴狂试错 "干中学么" 🤣

---

**熊布朗** @Stephen4171127 [2025-07-30](https://x.com/Stephen4171127/status/1950534516935680324)

左边是？

---

**不鍊金丹不坐禪** @zzwz [2025-07-30](https://x.com/zzwz/status/1950537274984223116)

左边是配合 issues debug task 需求文档（其实就一两句Bug描述）和一个用浏览器测试库➕前后端埋点➕自动截图的测试脚本用例）Examps配合的 rules，然后丢和他 issues 让他开始YOLO Round(1): 分析/定位/抓包/修复/后端测试，前后联测/观察/反思循环。直到fixed输出经验报告，我再去功能验收测试一遍

---

**熊布朗** @Stephen4171127 [2025-07-30](https://x.com/Stephen4171127/status/1950538171495670044)

这个有点 NB，好用吗？有效吗

---

**不鍊金丹不坐禪** @zzwz [2025-07-30](https://x.com/zzwz/status/1950539808045953453)

今儿下用这个方式修复两个我自己半手动（我和TA一起分析log猜想，然后TA写前/后 单测脚本，我再手动测试给他报log… 修复了两天都没修好的后端Agent Run特定事件格式化—>websocket—>前端解析—组件的全链路Bug）我觉得主要是链路长手动给他callback上下文不好选，UI DOM我菜🐓也过滤不好

---

**熊布朗** @Stephen4171127 [2025-07-30](https://x.com/Stephen4171127/status/1950626151476465704)

有没有想过不借助浏览器 是不是一样能修好