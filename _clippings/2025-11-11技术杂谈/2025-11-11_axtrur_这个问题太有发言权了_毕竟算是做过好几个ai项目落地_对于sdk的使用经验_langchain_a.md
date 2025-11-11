---
title: "2025-11-11_axtrur_这个问题太有发言权了_毕竟算是做过好几个ai项目落地_对于sdk的使用经验_langchain_a"
source: "https://x.com/axtrur/status/1988054243631395115"
author:
  - "[[@axtrur]]"
published: 2025-11-11
created: 2025-11-11
description:
tags:
  - "x"
  - "@axtrur"
  - "https"
  - "2025-11-11"
---

# 这个问题太有发言权了（毕竟算是做过好几个ai项目落地） 对于sdk的使用经验：langchain，a

**axtrur** @axtrur 2025-11-10

这个问题太有发言权了（毕竟算是做过好几个ai项目落地）

对于sdk的使用经验：langchain，ai-sdk是最早使用的工具，6月份claude code出来就用上了并且开始研究claude code 生态，后来尝试使用openai sdk开发项目（体验还行），再然后看到越来越多的基于claude agent sdk的开源二开项目，开始在公司内那种需要agentic search场景引入claude agent sdk快速落地，再然后ai-sdk做了大版本break change升级到v5, 现在基于ai-sdk v5, v6对以往的经验进行一次整合重构扩展

我的感受是：如果你是一个特别需要开箱即用或者需要agentic search的场景，可以直接使用 claude agent sdk, 如果是想长期维护且可能未来会自定义扩展能力，openai sdk其实设计还是蛮不错的，但我更喜欢ai-sdk，并且ai-sdk经历v5大更新以及v6小更新，能力已经跟Claude agent sdk 很类似了，甚至你可以用ai-sdk v6重做一个Claude code ，我最近的工作也是基于这个生态进行过往经验的一次重构扩展

> 2025-11-10
> 
> 推上做AI应用开发的老师们，请教一下。
> 
> 2025年快结束了，如果用代码写AI workflow/agent，什么最好用？langchain刚出来的时候用过，觉得有点脱裤子放屁。不知道现在有没有更好的选择？或者它更好了？

* * *

**axtrur** @axtrur [2025-11-11](https://x.com/axtrur/status/1988106624503083330)

补充一下另外2个用过的sdk ： python的algno 和 typescript的mastra(基于ai-sdk扩展的）

* * *

**axtrur** @axtrur [2025-11-11](https://x.com/axtrur/status/1988107705090011217)

之前分享的claude code 生态项目

> 2025-08-30
> 
> Claude Code 生态项目！（不到2个月不知不觉已经看了这么多项目了，回头针对每个分类下梳理一下）
> 
> 之前说Claude Code会带动一波开源生态繁荣，结果大家看到了，各家Coding IDE 逐渐推行Coding Cli，SubAgent&Hook&Commands的机制，以及Headless模式和Claude Code
> 
> ![Image](https://pbs.twimg.com/media/GzlsJj7bYAAMUxO?format=jpg&name=large)

* * *

**寿司云VPN 置顶抽套餐** @ssyunorg [2025-11-11](https://x.com/ssyunorg/status/1988104676747981016)

做基于知识库的ai客服，适合用agent吗？向量搜索rag的话，很多用户描述问题不清楚匹配得不准确，感觉都需要多轮对话推理弄清楚了才能回答

* * *

**axtrur** @axtrur [2025-11-11](https://x.com/axtrur/status/1988106192934371710)

可以用agent，你说的场景如果你们知识库本身不多是足够的，如果多的话单靠rag不太行，感觉如果要效果好的话，一般你需要对你们存量的数据集做一个qa扩散生成进行数据集补充，然后做一下grpo偏好数据对其训练，才能有足够的泛化，能够尽可能快速的引导到清晰的问题；

* * *

**Syteca** @SytecaPlatform

Manage privileges dynamically, convert user activities into actionable insights, and respond swiftly to potential threats. Transform your organization’s human risk into human assets.

动态管理权限，将用户行为转化为可操作的洞察，并迅速应对潜在威胁。将组织的人力风险转变为核心资产。

* * *

**Qing** @import\_qing [2025-11-11](https://x.com/import_qing/status/1988102894835691591)

Google的sdk怎么样？

* * *

**axtrur** @axtrur [2025-11-11](https://x.com/axtrur/status/1988105096115425419)

google的还没直接用过的，是google哪个sdk ?

* * *

**Felix 的上下文** @pzx553 [2025-11-11](https://x.com/pzx553/status/1988120458131378439)

ai-adk 没有用过，研究过claude agent sdk,确实很不错，功能很完善。不过我前两周分析了一些Agent岗位JD，langchain依然是大部分团队的首选，一个都没有提到claude agent sdk的