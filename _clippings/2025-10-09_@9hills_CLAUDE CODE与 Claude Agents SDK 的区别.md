---
title: "CLAUDE CODE与 Claude Agents SDK 的区别"
source: "https://x.com/9hills/status/1976206512155660582"
author:
  - "[[@9hills]]"
published: 2025-10-09
created: 2025-10-09
description:
tags:
  - "@9hills # Deep Learning # AI Model # Claude Code # Agents SDK"
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

如果要自己快速做一个 Demo，可以用 Claude Agents SDK 快速搞一个出来。

他能让你通过十几行代码，组装 Claude Code + 你定制的Prompt、Tool、SubAgent ，变成你的 Agent 发出去惊艳所有人😄

P.S. Claude Agents SDK 也可以使用 GLM 4.6 等第三方模型，所以不用担心 vendor lock。

> 2025-10-09
> 
> 如果对 DeepResearch 这类复杂的 Agent 感兴趣，我建议学一下LangGraph的免费课程 Deep Research with LangGraph。
> 
> 课程比较循序渐进，先做一个单Agent系统，然后进化为多 Agent。
> 
> 最主要是架构简单，外部依赖非常少，一个大模型一个搜索API就完了。
> 
> https://academy.langchain.com/courses/deep-research-with-langgraph…

---

**dogedoge** @Guyguydoge [2025-10-09](https://x.com/Guyguydoge/status/1976208282340725032)

能用gpt5 Gemini等等吗 目前就缺一个现成的agent sdk来套壳

---

**九原客** @9hills [2025-10-09](https://x.com/9hills/status/1976209297966235725)

不过 Claude Agents SDK 与其说是 Agents SDK，不如理解为 Claude Code 封装，本质是一个 Claude Code。

---

**YanG** @minimalist\_2637 [2025-10-09](https://x.com/minimalist_2637/status/1976208440625426442)

有文档吗

---

**九原客** @9hills [2025-10-09](https://x.com/9hills/status/1976208861196689767)

https://docs.claude.com/en/api/agent-sdk/python…

---

**XiaoPeng** @PenngXiao [2025-10-09](https://x.com/PenngXiao/status/1976227487286952093)

是不是只能做本地跑的东西？Token让用户自己出？

---

**仓里 · 忙割** @kylesean6 [2025-10-09](https://x.com/kylesean6/status/1976235213178155284)

这团队太高产了，核心开发就三个人还要做社区做文档做视频。在这教程之前就出了一个 deepagents 库，模拟了claude code的实现，社区有基于这个库做的deep research实现，设置有一个专门deepagents-ui配套。

---

**少濬** @tydezhang [2025-10-09](https://x.com/tydezhang/status/1976212684371812504)

你能惊艳的别人也可以