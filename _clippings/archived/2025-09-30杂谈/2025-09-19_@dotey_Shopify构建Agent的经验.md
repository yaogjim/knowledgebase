---
title: "Shopify构建 Agent 的经验"
source: "https://x.com/dotey/status/1967786556288028720"
author:
  - "[[@dotey]]"
published: 2025-09-19
created: 2025-09-19
description:
tags:
  - "@dotey #AI #程序员 #软件开发 #Shopify #LLM"
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
**宝玉** @dotey 2025-09-09

Shopify 分享了他们构建 Agent 的经验，整体架构也是目前主流的 Agentic Loop，就是不停的循环，让大模型判断需要调用什么工具，Agent 去调用工具，根据调用工具的结果看是继续调用工具还是任务完成。

他们针对打造 AI 智能体给了4条核心建议

1\. 架构简单化，工具要清晰有边界

2\. 模块化设计（如即时指令）

3\. LLM 评估必须与人类高度相关

4\. 提前应对奖励作弊，持续优化评估体系

我看下来主要是两点值得借鉴的地方：

1\. 工具不要太多，尽量控制在 20 个以内；如果数量太多会极其影响 Agent 的能力，很难精确选择工具

那么解决方案是什么呢？

不要看他们分享的 JIT 方案，明显是一个过渡性的产物，需要动态的去生成调用工具的指令，为了保证不影响 LLM 的 Cache，还要动态去修改消息历史，过于复杂。

真正的靠谱方案其实 PPT 里面也写了（看图3），只是它们还没实现，而实际上 Claude Code 这部分已经很成熟了，就是用 SubAgent（子智能体），通过 Sub Agent 分摊上下文，把一类工具放在一个 SubAgent 中，这样不会影响主 Agent 上下文长度，也可以让子 Agent 有一定自制能力，有点类似于一个公司大了就分部门，每个部门就是一个 SubAgent。

> 2025-09-09
> 
> At #RailsWorld2025, Staff Engineer @ReallyChar shares how we build production LLM systems through Sidekick’s Rails architecture, and its orchestration patterns and tool integration strategies. 🛤️🛠️
> 
> Learn more here: https://shopify.engineering/building-production-ready-agentic-systems…  
> 在#RailsWorld2025 上，高级工程师@ReallyChar 分享了我们如何通过 Sidekick 的 Rails 架构、编排模式和工具集成策略来构建生产级 LLM 系统。 🛤️ 🛠️
> 
> 在此了解更多：https://shopify.engineering/building-production-ready-agentic-systems…
> 
> ![Three diagrams on a light green background. The first shows a flowchart with ](https://pbs.twimg.com/media/G077SQ0WUAAq0-2?format=jpg&name=large) ![Three diagrams on a light green background. The first shows a flowchart with ](https://pbs.twimg.com/media/G077TMOXEAAtlJb?format=jpg&name=large) ![Three diagrams on a light green background. The first shows a flowchart with ](https://pbs.twimg.com/media/G077UF9WIAAc7mT?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G0a4vpMXIAEE8Tk?format=jpg&name=large)

---

**宝玉** @dotey [2025-09-16](https://x.com/dotey/status/1967786558632698323)

2\. Agent 生成的结果要 Evaluate（评估）

Agent 要做得好，很重要的一点就是要能评估它生成的结果是好还是坏，这样 Agent 自己就能对自己的结果进行改进优化。

那么怎么评估 Agent 的优化结果呢？靠人太慢，靠机器太不靠谱。

所以他们先找了一些人类专家，从正式环境中抽取了足够多样的结果，来人工标记是好还是坏，然后把这个结果作为基准数据集，再去写提示词让 LLM 来评估，让 LLM 评估的结果和人类的结果保持一致。当 LLM 评估结果和人类一致后，后续就可以放心的让 LLM 来评估 Agent 的生成结果，这样就不需要人工介入。

至于会不会误伤，我想肯定还是会的，但不管怎么说还是一个比较好的折中方案。

其他还有一些强化学习的训练方法，有兴趣可以自己去看看原文。

https://baoyu.io/translations/building-production-ready-agentic-systems…

![Image](https://pbs.twimg.com/media/G077WGvWcAA7q0f?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G077XEjXgAAlJ3F?format=jpg&name=large)

---

**宝玉** @dotey [2025-09-16](https://x.com/dotey/status/1967920183219290320)

sub-agent 在主 Agent 看来是工具，通常用于特定领域任务

sub-agent 有自己的工具集合，既可以共享主 agent 工具又可以有自己工具

sub-agent 也是agent，是基于 system prompt 选择工具，不需要也不应该做 RAG 或者更复杂的动态工具检索

> 2025-09-16
> 
> 工具过载这个问题有2种解法
> 
> 第一种解法是提供一个工具帮助Agent选择工具，相当于RAG一个路径检索
> 
> 第二种解法是围绕任务来构建工具
> 
> 就是 Agents除了自己原始的工具集外，针对任务也有工具集，这两个工具集都能用
> 
> 但不论哪种方式，信息过载了就会混乱

---

**宝玉** @dotey [2025-09-18](https://x.com/dotey/status/1968487026870698002)

其实shopify本身有一套自己的业务查询QL 。这张图才是关键。有确定性的输入DSL 有确定性的 UI展示和link

> 2025-09-18
> 
> 其实shopify本身有一套自己的业务查询QL 。这张图才是关键。有确定性的输入DSL 有确定性的 UI展示和link
> 
> ![Image](https://pbs.twimg.com/media/G1F3lkaaQAAQHWB?format=jpg&name=large)

---

**rocky** @rock83 [2025-09-18](https://x.com/rock83/status/1968486480562823353)

其实shopify本身有一套自己的业务查询QL 。这张图才是关键。有确定性的输入DSL 有确定性的 UI展示和link

![Two side-by-side interface screenshots labeled ](https://pbs.twimg.com/media/G1F3lkaaQAAQHWB?format=jpg&name=large)

---

**宝玉** @dotey [2025-09-18](https://x.com/dotey/status/1968487149965041784)

确实有参考价值👍

---

**小小流浪者** @Lkevin394004 [2025-09-17](https://x.com/Lkevin394004/status/1968310784091677153)

宝玉老师，我们目前公司也在尝试构建agent，基于现有的业务来做AI Native重构。但做出来的产品AI Agent使用体验非常糟糕。传统公司如何正确的通告agent来做产品重构，感觉挑战还是很大。意图理解不清晰，Agent框架设计非主流，缺乏数据训练和方法，也没有评估分析和模型。太难了。

---

**宝玉** @dotey [2025-09-17](https://x.com/dotey/status/1968318681924161838)

嗯，那肯定很不容易，也许可以先从workflow开始，从简单的地方开始，能有正反馈最重要

---

**小小流浪者** @Lkevin394004 [2025-09-17](https://x.com/Lkevin394004/status/1968332742204297597)

感谢宝玉老师的回复。确实是很好的切入，老板的目标，实际执行，总是相差十万八千里。

---

**DafuWZ** @a\_dafu [2025-09-17](https://x.com/a_dafu/status/1968257385082093710)

这个循环，如何决定是否进行下一次调用，依靠评估模块吗，如果ai返回的内容是一个选择项，需要回答问题推进流程

---

**宝玉** @dotey [2025-09-17](https://x.com/dotey/status/1968320463102455843)

依赖LLM返回结果，如果是工具调用就执行工具，如果是询问就输出询问的消息，如果是结束就输出结束的消息，后两者是一个理性，都是文本消息，用户有回应继续新的循环

---

**布鲁斯** @bulusi\_0830 [2025-09-17](https://x.com/bulusi_0830/status/1968181616486015171)

能不能理解为用一个router来给不同的subagent分发任务呢

---

**宝玉** @dotey [2025-09-17](https://x.com/dotey/status/1968183092172214414)

可以这么理解的，manager 派活

---

**LeoK** @Leok\_Lee [2025-09-16](https://x.com/Leok_Lee/status/1967813846808346647)

这不是标准的react模式吗？

---

**宝玉** @dotey [2025-09-16](https://x.com/dotey/status/1967825292774478076)

不是

> 2025-09-13
> 
> 如果你的 Agent 还要用 ReAct 框架写 Prompt，那么要么说明你在用没有 Agent 能力的模型（比如 GPT-4o、Gemini 2.5 Pro），要么就是用错了。
> 
> 因为有 Agent 能力的模型，比如 Claude 4 系列（包括前面的 Claude 3.7 和 GPT-5），是不需要通过 ReAct 提示词来激发 Agent x.com/wwwgoubuli/sta…