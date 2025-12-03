---
title: "2025-11-28_yan5xu_再分享一个驯服_Code_Agent_的实用技巧_在用_ClineCursorWindsurf"
source: "https://x.com/yan5xu/status/1882410703375736886"
author:
  - "[[@yan5xu]]"
published: 2025-11-28
created: 2025-11-28
description:
tags:
  - "x"
  - "@yan5xu"
  - "https"
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

# 再分享一个驯服 Code Agent 的实用技巧！ 在用 ClineCursorWindsurf

**yan5xu** @yan5xu [2025-01-23](https://x.com/yan5xu/status/1882410703375736886)

再分享一个驯服 Code Agent 的实用技巧！

在用 Cline/Cursor/Windsurf 处理大型需求时，与 AI 的多轮对话会遇到两个问题：

\- 上下文积累导致：

\- AI 效果变差

\- token 用量暴涨，费用激增 💸

\- 历史错误内容污染后续对话

经过实践，我总结了一套"双文档"方案：

1\. 准备两个文档（直接让 AI 生成）：

\- 任务文档：记录需求和整体规划

\- 进度文档：追踪已完成的内容

2\. 工作流程：

\- 每轮对话都携带这两个文档

\- 当 token 接近上限时，让 AI 更新进度文档

\- 启动新对话，带着最新文档继续

\- 循环以上步骤直到完成整个开发

\- 完成后删除这两个临时文档

这样做的效果：

\- 文档作为记忆，解决上下文丢失

\- 新对话避免了历史错误的影响

\- 压缩历史内容，大幅节省 token 费用

用了一段时间，效果不错，分享给大家参考。

![Image](https://pbs.twimg.com/media/Gh-hWfDaUAAogpk?format=png&name=large)

* * *

**祥仔Leo | 行走的Meta Prompt** @leodknuth [2025-01-23](https://x.com/leodknuth/status/1882477066488311861)

我也是这么干，都是被坑过后总结的经验

* * *

**ⓥictor-wu.eth** @victor\_wu\_eth [2025-11-28](https://x.com/victor_wu_eth/status/1994234207866937420)

你这个做法不就是openspc的做法么？看来英雄所见略同呀

* * *

**WquGuru** @wquguru [2025-11-28](https://x.com/wquguru/status/1994213902482297328)

感谢分享，我的做法是写一个command，上下文快满了让它保存一下当前的主要信息，不过这里的方法更自动一些😁

* * *

**小橘子** @xiaojuzi\_orange [2025-02-10](https://x.com/xiaojuzi_orange/status/1888773658694582314)

请问文档保持什么内容啊？ 可以给两个例子，任务文档和进度文档？ 感谢