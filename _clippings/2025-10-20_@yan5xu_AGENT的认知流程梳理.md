---
title: "AGENT的认知流程梳理"
source: "https://x.com/yan5xu/status/1979451118876057669"
author:
  - "[[@yan5xu]]"
published: 2025-10-20
created: 2025-10-20
description:
tags:
  - "@yan5xu # Agent # agentic #ChatGPT # AI # 流程"
---
**yan5xu** @yan5xu [2025-10-18](https://x.com/yan5xu/status/1979451118876057669)

最近两个月和非常多团队交流之后有一个强烈感受。很多人因为 agentic 循环过程的体感缺失和理解，这里存在非常大的认知差距。

有人认为存在某种神迹让 Agent 有超越模型智力的表现；有人觉得无非多调用几次 API，哪有那么神奇；

这种差距导致大家很多时候说话都不在一个频道。

所以有了这篇长文，希望能够帮大家构成一个统一的上下文，“当我们在聊 agentic 的时候，我们在说什么”

---

**yan5xu** @yan5xu [2025-10-18](https://x.com/yan5xu/status/1979451304222298528)

全文太长了，一万三千多字，所以发在公众号

https://mp.weixin.qq.com/s/tewBKHgbyrjxUjAOmkXI7A…

---

**yan5xu** @yan5xu [2025-10-18](https://x.com/yan5xu/status/1979452010551480574)

首先是 Chatbot 是如何发展成 Agent 的，中间经历过思维链（CoT），自我反思（Reflexion框架），和最后大家公认的最佳实践 reAct。完整看完发展过程，才能更好的理解流程对结果带来的升级。

---

**yan5xu** @yan5xu [2025-10-18](https://x.com/yan5xu/status/1979452436722147638)

其次是两个古老的理论基础

控制论 (Cybernetics)：它解释了系统如何通过反馈来达成目标，体现了 Agent “逼近”解决方案的过程。

信息论 (Information Theory)：它解释了信息与不确定性的关系，体现了 Agent “探索”问题空间的过程。

---

**yan5xu** @yan5xu [2025-10-18](https://x.com/yan5xu/status/1979454230835662973)

最后是对reAct的一些反思，它本身只是所有 Agent 设计的一个起点，甚至是某个 workflow 的一个环节。在这之上可以发展出工作流编排，更复杂的分层架构。流程设计这将会是现在这个时间点 AI 应用的核心挑战和壁垒。

---

**yan5xu** @yan5xu [2025-10-18](https://x.com/yan5xu/status/1979454969440014805)

文末我列出来了，思维链、思维树、Reflexion框架、ReAct 框架、CodeAct框架，OpenAI Lilian Weng的《LLM-powered Autonomous Agents》（也是 Agent 奠基之作），斯坦福 AI 小镇的链接。有兴趣的可以进一步了解

---

**xincmm** @xincmm [2025-10-18](https://x.com/xincmm/status/1979458500607774758)

我能理解为什么很多人没有这个认知，因为这需要高强度的训练，需要和 AI 高强度协作，需要和 AI 长期共振训练，需要被迫显化、观察和调试自己的思考过程，经历后认知自然而然会涌现出来，这是认知同构的必要条件，缺乏这个过程永远都不会有这个认知

---

**yan5xu** @yan5xu [2025-10-18](https://x.com/yan5xu/status/1979459481659675045)

是，我也是发现很多人，没有经历这个过程和高强度用 AI，认知真的非常模糊。所以才想能有什么方式把这个过程压缩一下，不然真的没办法对话。

---

**xincmm** @xincmm [2025-10-18](https://x.com/xincmm/status/1979454717123268781)

这是必然的涌现吗？我发现做 Agent 做到后面都会形成一种新的认知架构，是对思维的设计、迭代和重构，都开始从工具使用者演化成认知架构师，而 Agent 就是设计者思维的显化

---

**yan5xu** @yan5xu [2025-10-18](https://x.com/yan5xu/status/1979456207292371456)

我觉得产品就是对某个事情的认知和最终体现。怎么理解 AI/Agent 的，怎么使用，思考框架是什么。

---

**orange.ai** @oran\_ge [2025-10-20](https://x.com/oran_ge/status/1980066934675935406)

看完文章 有些疑惑似乎还是没有得到解答

如果 Agent 不能超越模型智力，那 Agent 的边界到底在哪里呢？

---

**yan5xu** @yan5xu [2025-10-20](https://x.com/yan5xu/status/1980085405971308912)

Agent 现在的能力提升不只是模型能力提升带来的，还有流程。

Agent 的边界我觉得接近于公司的边界，模型是人，流程是公司的章程、文化、规章制度。有的公司如midjourney 在一个恰当的时间，11 个人，1 亿

---

**Delibread\_Jason** @Delibread2 [2025-10-19](https://x.com/Delibread2/status/1979730138767261854)

深刻的Agent框架思考，但有个关键矛盾：99%单步准确率×50步≈60%成功率。再精妙的流程或者Agent框架设计也无法根本解决误差累积问题。这解释了为什么Agent目前更适合高容错场景，而非专业生产级系统。

---

**穿拖鞋的猴子** @wendayuan [2025-10-19](https://x.com/wendayuan/status/1980060408716337231)

雄文！是不是deepseek突破性的外显cot，不仅仅是优化前端客户体验，这种骚操作一方面对ai自己输出结果有review的作用，另外一方面让等答案的人了解其思考过程，从而可以干预他或者引导他了，是一盘大旗啊

---

**逍遥子$Ai知识分享官** @linyi64965449 [2025-10-20](https://x.com/linyi64965449/status/1980153116676030666)

Agent的突破源自认知流程设计（规划→执行→反思→迭代），而非单纯依赖大模型参数增长。

---

**jeff** @midshipman [2025-10-18](https://x.com/midshipman/status/1979690909265776930)

怎么说呢，文章有道理，把复杂的流程梳理的不错。但面对复杂的世界这套流程必然会更复杂，最后还是靠人定义框架和流程，agentic只不过是一个光鲜的口号

---

**逍遥子$Ai知识分享官** @linyi64965449 [2025-10-20](https://x.com/linyi64965449/status/1980153179859005867)

“Agent的强大，并非源于模型智力的再次飞跃，而是源于为其赋予的‘认知流程’的巨大提升。”

---

**逍遥子$Ai知识分享官** @linyi64965449 [2025-10-20](https://x.com/linyi64965449/status/1980152863826616320)

Agent的本质：流程驱动的质变

核心误区破除

神秘化：Agent并非“无所不能的魔法”，其能力受限于底层模型和流程设计。

简化论：Agent ≠ “多次调用ChatGPT”，而是通过结构化流程实现认知跃迁。

---

**yyy** @lfevhtdr34565 [2025-10-19](https://x.com/lfevhtdr34565/status/1979957866237726726)

看完痛哭流涕，爆赞

---

**Adam Carter** @AdamCarterCS [2025-10-18](https://x.com/AdamCarterCS/status/1979678922393706946)

说的太对了，gpt5的api就有agentic过程，而这个太重要了