---
title: "2026-03-04_Leo_Leo_MercadoLibre_拉美最大电商_市值_1000_亿级_2_万开发者在推的"
source: "https://x.com/runes_leo/status/2029050955204051277"
author:
  - "[[@Leo]]"
published: 2026-03-04
created: 2026-03-04
description:
tags:
  - "x"
  - "@Leo"
  - "agent"
  - "http"
---

# Leo MercadoLibre（拉美最大电商，市值 $1000 亿级） 2 万开发者在推的

**Leo**

MercadoLibre（拉美最大电商，市值 $1000 亿级） 2 万开发者在推的方法论，说 AI 编程 agent 好不好用取决于四根杠杆——规则文件、MCP 工具、Skills 按需加载、规格驱动开发。 个人开发者也能直接抄： 规则文件：写一个 [http://CLAUDE.md](http://CLAUDE.md)，把你的技术栈、命名规范、常见坑写进去，每次开 session 自动注入。注意要拆文件——全塞一起会撑爆 context。文章引了一个研究：填到 60% 就开始退化。 MCP：给 agent 接工具。浏览器、数据库、内部文档、API 都行。装上之后 agent 就不只是"能读写文件"了。 Skills：这根最值。把特定任务的详细指令写成 skill 文件，只有一行描述常驻 context，调用时才加载全文。既不浪费 context 预算，又能随时扩展能力。 四根杠杆之外，文章单独讲了反馈闭环——hooks 在 agent 的关键节点挂检查，提交前跑 lint、装新插件时扫安全。agent 没法跳过，只能老实通过。四根杠杆决定 agent 能做什么，闭环决定它做得对不对。 还有一根：规格驱动开发，先写 spec 再让 agent 动手。之前分析过，对个人开发者偏重——生成的 spec 冗余，反而消耗精力。我的做法反过来：先干活、先踩坑，把教训沉淀成规则文件，让规则反哺一轮。效果一样，路径相反。

* * *

### 热门回复

**@Sam Morris** ♥ 3 · 💬 0

Any site. Any workflow. One description. Agents build the API.

**@Show PNL（不定期更新资金曲线）** ♥ 1 · 💬 0

ai时代skill应该成为一个新的文件类型