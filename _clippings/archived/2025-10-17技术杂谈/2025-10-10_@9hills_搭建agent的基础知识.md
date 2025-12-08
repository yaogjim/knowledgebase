---
title: "搭建agent的基础知识"
source: "https://x.com/9hills/status/1976301290490871998"
author:
  - "[[@9hills]]"
published: 2025-10-10
created: 2025-10-10
description:
tags:
  - "@9hills #  AI框架 #  自主agent #  deepResearch #  Claude code"
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
**九原客** @9hills 2025-10-09

给个建议，首先先不要学任何llm调用以外的库。

1\. 从这里学习workflow agent https://deeplearning.ai/courses/agentic-ai… 学习时可以顺手将课程里的workflow用dify复刻下，把dify workflow 模式学了。一定要知道如何手搓工作流。

2\. 跟着文档示例了解下dify 的agent 模式，主要是学 openai agents sdk，了解什么是自主agent，并搭建一个简单的端到端语音对话agent。

3\. 到此你掌握了workflow和自主agent的概念，接下来就是Claude code以及DeepResearch 这种超复杂 Agent，目前还比较乱，之后我再推荐。

但是不管用什么框架，一定要看发给模型的原始请求，不要被框架的功能所迷惑。

> 2025-10-09
> 
> 我是新手，请教，如果我向学习如何搭建agent, 有哪些书籍和教程推荐？无敌感谢

---

**Miko su** @Mikotingting [2025-10-09](https://x.com/Mikotingting/status/1976302318481178685)

我主要有2个最求，我有很多产品画册，有时候客户带着图片问我们有没有这个家具的时候，我每次都要翻越多个画册，找很久才找到跟客户提供的照片一样的家具产品，或者类似的家居产品。这个问题，都是很多外贸公司的痛点。我想有一个ai只要我上传客户的照片，ai就自动在我的画册数据库寻找，是否有一样的

---

**九原客** @9hills [2025-10-09](https://x.com/9hills/status/1976304049634017590)

我大概说下，最简单暴力就是用一个图片的embedding 模型做以图搜图。

复杂点可以结合图片标记的文字，分别作图搜图和文搜文。 图片标记文字可以用gemini 2.5 pro生成。

---

**Miko su** @Mikotingting [2025-10-09](https://x.com/Mikotingting/status/1976308706137841967)

这个情况，可以在本地电脑进行么？就是画册都在本地电脑里面。

---

**九原客** @9hills [2025-10-09](https://x.com/9hills/status/1976310029591748817)

如果你用先把图片转换为文字（gemini），然后文字搜文字。是可以本地跑的。

如果是直接图搜图，那你大概需要一个gpu来运行这个模型。

---

**Miko su** @Mikotingting [2025-10-09](https://x.com/Mikotingting/status/1976310617305968911)

如果找把图片转文字，我是否要把所有画册的图片，都一张张上传到gemini ，然后生成文字？

---

**九原客** @9hills [2025-10-09](https://x.com/9hills/status/1976310971133272314)

是，而且要为图片生成你想要的输出。

其实最好还是图搜图，可惜没有太好的开源模型。

---

**Miko su** @Mikotingting [2025-10-09](https://x.com/Mikotingting/status/1976311319818273121)

因为我看淘宝都是用图搜图的方式，在淘宝海量的产品找相似的，那么如何在本地电脑也可以这样操作，就这么太好了

---

**九原客** @9hills [2025-10-09](https://x.com/9hills/status/1976313155891704053)

可以试试 https://github.com/baaivision/EVA/tree/master/EVA-CLIP… 但是这个上手成本可比llm高多了