---
title: "工作流 与 Agent"
source: "https://x.com/dotey/status/1949852823891431839"
author:
  - "[[@dotey]]"
created: 2025-07-29
description:
tags:
  - "@dotey #工作流 #Agent #AI"
---
**宝玉** @dotey 2025-07-09

最近我也在思考 Workflow 和 Agent 到底什么关系，我的一个初步想法：

Workflow 本质上是工具，只是工具中用到了 AI 能力，所有能被定义成 Work Flow 的就应该能被做成工具。

Agent 更像是 AI，它能主动规划、去调用工具，Workflow 应该是 Agent 的一个可以被调用的工具。

你怎么看？

> 2025-07-09
> 
> 之前在团队内讨论时写的一段话：Agentic 和 Workflow 不是非黑即白的开关，而是一个连续的光谱。我们的架构要提供可持续的迭代能力，从而在 LLM 能力足够的地方更自主化，在 LLM 还不太擅长的地方通过固定编排把专家经验固定下来，随着模型的进化可以低成本的替换节点实现逻辑。

---

**宝玉** @dotey [2025-07-28](https://x.com/dotey/status/1949853975580234032)

@frxiaobei 的观点：

> 2025-07-28
> 
> 现实中最靠谱的路径就是 agent 和 workflow 就是这种组合优化。
> 
> 哪里擅长自动就让模型顶上，哪里风险高就继续靠规则兜底，这才是可持续演化的方式。
> 
> 但也点出了未来智能系统架构的演进：以编排承载的经验最终会被模型逐步吞噬。 x.com/atian25/status…

---

**宝玉** @dotey [2025-07-28](https://x.com/dotey/status/1949854096707481999)

@wwwgoubuli 的观点

> 2025-07-08
> 
> 其实吧，workflow 才是 agent 的高级和成熟形式。
> 
> 不要想着拿现在已有的workflow和agent来对比，都还处在不成熟的阶段。我描述的不是目前已有的场景。

---

**宝玉** @dotey [2025-07-28](https://x.com/dotey/status/1949894464719274392)

马老师的定义，Agent 有能力自己动态的临时构建 flow

> 2025-04-22
> 
> 「Multi-Agent, Reasoning」论文
> 
> FlowReasoner: Reinforcing Query-Level Meta-Agents
> 
> 轻云顺风即变，FlowReasoner 使 multi-agent workflow 随query应变于瞬息之间。
> 
> 这篇论文十分精彩，作者瞄准“one system per user query”的目标：为每一条用户 query 即时推理出一个专属的multi-agent
> 
> ![Image](https://pbs.twimg.com/media/GpKtuTwXYAAlSui?format=jpg&name=large)

---

**宝玉** @dotey [2025-07-28](https://x.com/dotey/status/1949894656113987768)

雷总：主agent的这些query和执行就是一套workflow。

> 2025-07-28
> 
> 以让agent买机票为例，
> 
> 一个正常的流程是，用户跟agent说你帮我订一张下周五去London，下下周三返回的经济舱，直飞机票。
> 
> 主agent收到后，首先像一堆agent 发消息，谁能查票？
> 
> 一堆agent返回说，我我我。
> 
> 主agent把消息扔给说可以查票的agent。
> 
> 然后等各家回消息。 x.com/wwwgoubuli/sta…

---

**宝玉** @dotey [2025-07-28](https://x.com/dotey/status/1949895011241464291)

@cryptonerdcn： workflow迟早会内化进agent的概念里。

> 2025-07-28
> 
> 在这里不能讨论 狭义or前LLM时代workflow：定义死的一段流程，和agent差别很大。
> 
> 但后llm时代这俩可难以分清了。
> 
> 虽然@dotey 提到的根据anthropic定义，一个是定义好的流程中用到agent，一个是让agent自由发挥。
> 
> 但 @dongxi\_nlp x.com/dongxi\_nlp/sta…

---

**宝玉** @dotey [2025-07-28](https://x.com/dotey/status/1949940870003773482)

@eraera: agent/workflow是工作自动化的延续，agent描述工作顺序的逻辑判断，workflow描述工作依赖关系的空间结构。二者的关系类比代数和几何，是对逻辑结构的不同描述方式。

> 2025-07-28
> 
> 试着以回答一组问题的方式，来阐述对agent/workflow的看法。缘起是这个 https://x.com/eraera/status/1949902260785598475… 问题1.文档的目的是什么。文档是人类的外存，很多文档都有记录当前状态的功能，相当多的文档还包括执行指令，也就是从当前状态迁移到下一个状态的指令。

---

**宝玉** @dotey [2025-07-28](https://x.com/dotey/status/1949941176443732383)

@TaNGSoFT: 随着llm的生成能力的提升，完全可以由agent来生成workflow。类似flowreasoner的方向。

> 2025-07-28
> 
> 非常棒的讨论。必须要mark。
> 
> agent和workflow并不互斥，可以并存，我倾向于是嵌套的关系，agent>workflow，确定性的、经常重复的过程可以固化下来成为workflow，为agent解决问题所用。
> 
> 我觉得随着llm的生成能力的提升，完全可以由agent来生成workflow。类似flowreasoner的方向。 x.com/dotey/status/1…

---

**Yangyi** @Yangyixxxx [2025-07-28](https://x.com/Yangyixxxx/status/1949974992818442321)

我的理解👇

> 2025-05-25
> 
> 如果你搞不懂什么是Agent / workflow / Agentic / ReACT
> 
> 那可以看看我的大白话注释：
> 
> \----------------
> 
> Agent ， 广泛意义上讲，是一个智能黑盒，你给一个input，Agent识别意图，按照它自己的设定去给你一个output
