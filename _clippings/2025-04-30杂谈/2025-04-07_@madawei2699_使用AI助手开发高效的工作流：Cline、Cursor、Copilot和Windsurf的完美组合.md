---
title: "使用AI助手开发高效的工作流：Cline、Cursor、Copilot和Windsurf的完美组合"
source: "https://x.com/madawei2699/status/1905860072795681017"
author:
  - "[[@madawei2699]]"
created: 2025-04-07
description: "最近一周完全用 Cline/Cursor/Copilot/Windsurf 等 AI Agent开发完了下面两个专注 LLM动态工作流编排（非 DAG 这种预定义工作流）的项目： https://github.com/i365dev/agent_forge… https:/"
tags:
  - "@madawei2699 #AI #工作流 #自动化 #LLM #Cline #Cursor #Copilot #Windsurf #开发"
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
**Dawei Ma** @madawei2699 [2025-03-29](https://x.com/madawei2699/status/1905860072795681017)

最近一周完全用 Cline/Cursor/Copilot/Windsurf 等 AI Agent开发完了下面两个专注 LLM动态工作流编排（非 DAG 这种预定义工作流）的项目：

🔗 https://github.com/i365dev/agent\_forge…

🔗 https://github.com/i365dev/llm\_agent…

一行代码没写，全程 AI agent 搞定，过程有点曲折，下面是我的折腾记录👇

---

**Dawei Ma** @madawei2699 [2025-03-29](https://x.com/madawei2699/status/1905862440128070044)

一开始用 cline + Copilot 和 Claude 3.5 开发，设计让官网的 Claude 3.7 完成。结果 Copilot 额度太低（2小时50条消息），开发断断续续，每天只能搞一点。更惨的是，遇到一个无限死循环，Claude 3.5 反复失败，3.7 也分析不下来… 尝试了 Trae 的 Claude 3.7，表现更差，直接在错误的方向狂奔！

---

**Dawei Ma** @madawei2699 [2025-03-29](https://x.com/madawei2699/status/1905862442510327896)

无奈切换新分支测试，还是不行。又试了 Cursor，免费额度用了一些，但还是死循环，毫无进展…感觉要崩溃了😭

在闲鱼花了20块买了五个 Windsurf 试用账户（本来想买 Cursor，但 Copilot 额度实在不够用）。

Windsurf 便宜又好用，但一开始还是死循环，测试一直挂。

---

**Dawei Ma** @madawei2699 [2025-03-29](https://x.com/madawei2699/status/1905862444779508057)

后来换了个思路，让 Claude 3.7 把需求拆成几个小 PR，步步推进。

这个策略终于奏效了！Windsurf 上的 Claude 3.7 跳出了死循环，开发一路畅通。两个项目大概用了1000个 flow，累计时间不到10小时就搞定！

---

**Dawei Ma** @madawei2699 [2025-03-29](https://x.com/madawei2699/status/1905862448969887995)

成果：两个项目近200个测试全过，几个大 example 也完美运行！我甚至没细看代码，Claude 分析源码后说完全符合最初设计。

Claude 预测人工写得8周，AI 这么快，感觉程序员距离失业更近一步，这状态有点像汽车加入自动挡后，专业司机大量被下岗了，薪资也从高薪变成普通的工作。

![Image](https://pbs.twimg.com/media/GnL7Czyb0AA9PoL?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/GnL7FqmbIAAxOrl?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/GnL7Iiwa4AAhcfJ?format=jpg&name=large)

---

**Dawei Ma** @madawei2699 [2025-03-29](https://x.com/madawei2699/status/1905862451796803792)

顺便吐槽下：中途用 cline 试了 OpenRouter 的 Gemini 和 DeepSeek 模型。和 Claude 比，简直弱智，复杂需求完全玩不转。ChatGPT 的 4o 模型更是差劲，Copilot 默认用 ChatGPT 也拉胯，额度还低。

---

**Dawei Ma** @madawei2699 [2025-03-29](https://x.com/madawei2699/status/1905862453830750507)

总结AI Agent开发的小技巧：

1️⃣ 先用 Claude 规划整体设计与开发规则，创建各种 Agent 的 Rules，定下基调。

2️⃣ 遇到死循环别硬刚，拆小 PR 推进更靠谱。

3️⃣ Cline/Cursor/Windsurf 功能强大，当然前提是用 Claude 最新的模型，其他模型（Gemini/DeepSeek/ChatGPT）在复杂需求面前都不行。

---

**Yang** @yangpten

Build powerful AI agents and automations for your business today.

Check out our step-by-step video tutorials 100% FREE 🥳  
立即为您的企业构建强大的人工智能代理和自动化工具。

查看我们的分步视频教程，完全免费 🥳

![](https://pbs.twimg.com/media/GQrbMqGbMAETYdf?format=png&name=large)

---

**Julian** @EricZhupq [2025-03-30](https://x.com/EricZhupq/status/1906246378021585164)

Elixir是个什么开发语言？

---

**小偷** @sthiejobs [2025-03-31](https://x.com/sthiejobs/status/1906567676757225814)

开发环境最佳实践是什么，windsurf+claude3.7吗

---

**晨光** @hearyousayworld [2025-03-30](https://x.com/hearyousayworld/status/1906469284089381170)

自己使用心得是同模型不同时刻表现的智力也时常不一样。除了cline都会被限制使用啊，可cline真是好贵，一天不小心就能跑出其他agent的月费来。

---

**Dawei Ma** @madawei2699 [2025-03-31](https://x.com/madawei2699/status/1906499108636131611)

是的，不同时刻同模型同agent表现的也不一样😂，可能都会降智吧