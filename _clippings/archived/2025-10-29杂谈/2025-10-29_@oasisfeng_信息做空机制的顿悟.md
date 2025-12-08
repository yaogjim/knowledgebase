---
title: "信息做空机制的顿悟"
source: "https://x.com/oasisfeng/status/1983098673384026382"
author:
  - "[[@oasisfeng]]"
published: 2025-10-29
created: 2025-10-29
description:
tags:
  - "@oasisfeng #信息做空 #GTA模型 #GeminiAI #负值经济学 #信息经济学"
status: "inbox"
importance: 2
effort: 2
review_level: 0
review_next: "2025-11-13"
review_interval: null
review_count: 0
decision: null
topics: []
links_out: []
summary: ""
pov: ""
actions: []
---
**Oasis Feng** @oasisfeng 2025-08-20

最近实在太开心了！

在一次不经意的泛泛交流中，Gemini 2.5 Pro 提出了一些天马行空的想法。当我读到其中一条时，心里猛然一惊，「莫非这就是我苦苦研究了好几年信息做空机制，都未曾找到答案的正确方向？！」

虽然 Gemini 设想的是债务，但我立刻联想到了「做空」。我知道这时候该请出 GPT-5 了。\\

> 2025-08-20
> 
> 今天下午沉浸在泳池中完成 Zen Swimming，重启思维之际，突然闪现顿悟，找到了那块困扰我近两年的最后一片拼图🧩。
> 
> 此前一直在苦苦思索如何在彻底摒弃了交易的模型中实现「信息做空」，以解决「造谣一张嘴，辟谣跑断腿」的信息经济学困境。今天才意识到，需要的不是做空这个手段，而是它的震慑机制。\\ x.com/oasisfeng/stat…
> 
> ![First image displays a screenshot of a conversation with Gemini AI model in Chinese text discussing concepts like negative value in economics, short-selling mechanisms, and examples involving debt and information asymmetry with bullet points and explanations. Second image shows another AI chat screenshot elaborating on short-selling ideas applied to information, including scenarios of rumor spreading and deterrence, with structured points on economic models and value creation.](https://pbs.twimg.com/media/G4VXHMPasAAS6Ki?format=jpg&name=large) ![First image displays a screenshot of a conversation with Gemini AI model in Chinese text discussing concepts like negative value in economics, short-selling mechanisms, and examples involving debt and information asymmetry with bullet points and explanations. Second image shows another AI chat screenshot elaborating on short-selling ideas applied to information, including scenarios of rumor spreading and deterrence, with structured points on economic models and value creation.](https://pbs.twimg.com/media/G4VXH4lasAEwB6V?format=jpg&name=large)

---

**Oasis Feng** @oasisfeng [2025-10-28](https://x.com/oasisfeng/status/1983098675799962041)

GPT-5 似乎也意识到了这个课题的重要性，严肃地思考了 5 分多钟，然后给出了肯定的回答。这让我信心大增，立刻着手开始模型的调整。

过程中，我不断反思自己为什么就没能想到这个如此简洁的思路。Cost 构造函数中对 amount 必须位正的人为设限，反而给 Gemini 以挑战的灵感，终成我的「希帕索斯」。\\

![Image](https://pbs.twimg.com/media/G4VY_aTb0AAb8Np?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G4VZAhtbMAAsGvR?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G4VZ0fxa0AApmvi?format=jpg&name=large)

---

**Oasis Feng** @oasisfeng [2025-10-28](https://x.com/oasisfeng/status/1983098678371070379)

我想，早年求学中数学基础不扎实，可能就是自己一直未能发现眼前这一关键线索的根本原因吧。如果数学思维足够敏锐，或许早就像 Gemini 那样看这个正数限制不顺眼了。

接下来用了一周时间对模型进行深入的解剖、重写，再仿真验证。这个导火索所掀起的核心算法重写，竟然意外地进一步简化了算法实现。\\

---

**Oasis Feng** @oasisfeng [2025-10-28](https://x.com/oasisfeng/status/1983103381603529138)

不由得感叹，数学的简洁之美，才是最重要也最坚实的支柱。

所有的人为设限、所有的 if 判断，在它面前都如摧枯拉朽般被击碎，彻底扫进了 Git 的历史 log 中。最终，核心算法部分只剩下了仅有的一个检查迭代收敛的 if 语句。

而 GPT-5 一开始所担忧的「除零」情景，也完全被系统的混沌之力自然消解。\\

---

**LiUgOd** @LiuGods [2025-10-28](https://x.com/LiuGods/status/1983137599444115524)

厉害，不过资产与负债正常不应该是用两个不同的表来存储吗？

---

**Oasis Feng** @oasisfeng [2025-10-28](https://x.com/oasisfeng/status/1983142486227800190)

对央行而言，资产和负债是同一张表。