---
title: "MCP与Skills的本质区别"
source: "https://x.com/SaitoWu/status/2000245067936837667"
author:
  - "[[@SaitoWu]]"
date: "2025-12-17T19:26:05+08:00"
created: 2025-12-17
description:
tags:
  - "@SaitoWu # AI # LLM # MCP # Skills # 协议 # 训练 # 习惯 # 企业规范 # 行业 know-how #"
---
**Saito** @SaitoWu [2025-12-14](https://x.com/SaitoWu/status/2000245067936837667/history)

现在大部分 MCP Server，其实就是披着“协议”外衣的 Skill 大杂烩。

返回结论、不返回原始能力，内部塞满 prompt、规则和流程，替模型想好了顺序。MCP 本该告诉你能调用什么，不该告诉你该怎么做。一旦把“怎么做事”写进 MCP，Agent 就退化成 RPC 客户端。

Anthropic 推 Skills，其实是把思路、流程、决策拉回模型里。核心得出：把“怎么做事”塞进 MCP，就是不相信 Agent。

---

**Bruce Van** @brucevanfdm [2025-12-16](https://x.com/brucevanfdm/status/2000806881204531416)

刷到了很多人说分不清MCP 跟Skills，我想尝试自己回答好像也不太能说清楚并举例出来。。。

于是我去整理了一下，尝试说清楚这个事情，顺便分享出来：

Skills 就像是一道菜的完整制作指南——从原材料的选择、到制作步骤、再到口味调整。

但是，大模型学的是“通用做法”，它不知道你的口味。

大模型知道"红烧肉怎么做"，但不知道你们家喜欢甜口还是咸口

大模型知道“PPT 要有层次感”，但不知道你们公司的品牌色是什么、汇报风格是严谨还是活泼

所以，真正让 AI 落地产生价值的，是私域的 Skills —— 融入了你个人习惯、企业规范、行业 know-how 的"独家菜谱"。

MCP 则像是厨房里的水电煤气和采购渠道——它让你能打开冰箱取食材、拧开燃气灶点火、叫跑腿去菜市场买肉。它解决的是“能不能连接到”的问题，而不是“怎么做才对味”。

总结起来：

MCP 解决“能不能拿到原材料”

通用 Skills 解决“会不会做这道菜”

私域 Skills 解决“做出来的菜合不合你的口味”

![Image](https://pbs.twimg.com/media/G8RLOUJa4AQGaJk?format=jpg&name=large)

---

**Weilian** @WeilianDu [2025-12-15](https://x.com/WeilianDu/status/2000387919664844991)

而且MCP server由于是开发者开发的，prompt大部分写得太简单了。所以说skills大杂烩，MCP想做，但是又做不到。skills让专业人员总结出他们的SOP，MCP只承担接口的作用。

---

**Lobay** @sagiwei [2025-12-15](https://x.com/sagiwei/status/2000609177207804041)

可 MCP 协议核心特性之一就是 Prompts 啊。

---

**大梦想家迪士尼** @discountifu [2025-12-15](https://x.com/discountifu/status/2000376516237312075)

我已经分不清mcp/skill/plugin了😀

---

**化骨绵掌** @likefeiwu [2025-12-15](https://x.com/likefeiwu/status/2000373080158613545)

我理解 mcp应该是 提供给llm 的tool use 合集。 skill 是预制的prompt 合集

---

**allen** @angela781105 [2025-12-15](https://x.com/angela781105/status/2000416460469125374)

MCP核心应该也就是一个函数吧，定好输入，获得输出，只是这个黑盒过程可以很简单，也可以很复杂

---

**Drew Zhao** @drew\_color [2025-12-16](https://x.com/drew_color/status/2000806793359056966)

mcp tools 怎么用 vs 怎么用好。感觉后者放在 mcp server 里，辅以 /prompts 和 /resources 也没有什么问题。而且对于「怎么用好」，还是 tools 开发者最清楚。

---

**X** @ohyourgod\_x [2025-12-15](https://x.com/ohyourgod_x/status/2000412167598928271)

炒概念的必然失败，归根结底模型能力不行

---
