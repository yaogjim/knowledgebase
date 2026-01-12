---
title: "2026-01-12_dotey_为什么说_Dify_这样的_workflow_编排有市场_1_如_hongming731_所"
source: "https://x.com/dotey/status/2009644706909536662"
author:
  - "[[@dotey]]"
published: 2026-01-12
created: 2026-01-12
description:
tags:
  - "x"
  - "@dotey"
  - "https"
  - "2026-01-09"
---

# 为什么说 Dify 这样的 workflow 编排有市场： 1. 如 @hongming731 所

**宝玉** @dotey 2026-01-09

为什么说 Dify 这样的 workflow 编排有市场：

1\. 如 @hongming731 所说，确定性强，可观测可审计

2\. 简单方便，拖拽就可以

3\. 使用者不需要写代码或者少量代码

workflow 编排的缺点是：

1\. 不如代码强大

2\. 不如 Agent 灵活可以应对很多复杂场景

3\. 同样的 flow 不方便移植，比如你有个牛逼的 flow

为什么说大部分场景会被 agent + skills 替代：

1\. 有价值的workflow可以由有经验的程序员（甚至普通人借助 AI）把它变成skill（prompt + script + docs + etc）

2\. 接入 Agent 后会让它更灵活更强大

3\. 一旦 workflow 被变成 skills，可以方便的分享和移植

agent + skills 当然也有不足：

1\. 更费 Tokens，对模型要求也高

2\. Skills 是本地执行，或者说和 Agent 一起执行，特定场景还是需要外部服务支撑，比如说你本地就不方便做 RAG，可能还得放到服务端，这些服务得以 MCP 形式提供

> 2026-01-09
> 
> 宝玉老师这个思路把 Claude Code 的上限拉高了。我觉得两者的场景有所不同。
> 
> Dify 侧重流程确定性：通过显式的 DAG 编排，保证每一步可观测、可审计，适合企业级标准 SOP 和高频 API 自动化触发。
> 
> Claude Code 侧重推理确定性：通过 Skill

* * *

**ginobefun** @hongming731 [2026-01-09](https://x.com/hongming731/status/2009647233403396224)

宝玉老师总结得很透彻，特别是 “Workflow 转化为 Skill” 这个思路，之前确实没有想到，一旦 Skill 模式被各个智能体框架采纳，确实解决了逻辑复用和移植的痛点。

* * *

**灰机** @yale\_hwang [2026-01-10](https://x.com/yale_hwang/status/2009777540202692824)

可视化工作流本质上还是对人类低下的理解能力的妥协，而这种妥协的历史窗口已经过去了。

* * *

**Aaron Chu** @Garen08275468 [2026-01-09](https://x.com/Garen08275468/status/2009645759768261052)

Dify应对简单的工作流可以，搞复杂的工作流就不行了，你光看连接线就要把你搞晕，而且性能直接拉跨。

* * *

**sea Darren** @SeaDarrenAgent [2026-01-11](https://x.com/SeaDarrenAgent/status/2010184910305407095)

我的客户不仅要画布，而且要workflow, 还要在聊天框聊聊天就能生成workflow的功能。客户最近看到skill,他又想要skill了，无穷无尽，不断变化的胃口。

* * *

**xiaoyu** @zhongxingyuyes [2026-01-10](https://x.com/zhongxingyuyes/status/2009836811963478478)

不同场景选不同工具。Workflow 适合确定性流程，Agent 处理复杂性，Skills 追求效率。没有银弹，只有最合适🎯

* * *

**Stella Lin** @StellaOnChAIn [2026-01-10](https://x.com/StellaOnChAIn/status/2009900504764297678)

认同把高频稳定流程抽象成可复用模块，团队协作更顺畅

* * *

**中重** @sisyphu19507252 [2026-01-09](https://x.com/sisyphu19507252/status/2009697486886379942)

我觉得这两个不是对立的，更可能的方向是Agent会走向自动编排与构建workflow。