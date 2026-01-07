---
title: "2026-01-07_RookieRicardoR_强大的_Agent_至少应该包含什么_Orchestrator_Workers_任务委派_Evalu"
source: "https://x.com/RookieRicardoR/status/2008707658304340423"
author:
  - "[[@RookieRicardoR]]"
published: 2026-01-07
created: 2026-01-07
description:
tags:
  - "x"
  - "@RookieRicardoR"
  - "agent"
  - "https"
---

# 强大的 Agent 至少应该包含什么？Orchestrator-Workers 任务委派、Evalu

**耳朵** @RookieRicardoR 2026-01-06

强大的 Agent 至少应该包含什么？Orchestrator-Workers 任务委派、Evaluator-Optimizer 评估优化、Pipeline 管道、Circuit Breaker 断路器、State Machine状态机。

最近 OpenCode 很令人好评的一点就是：能够同时驱动三家模型进行代码设计和编写，每家模型各有所长，充分发挥长处。

听起来很复杂，其实很简单，只需要把它们三个想象成三个 SubAgent，只是连接模型时使用 API 不同，再做一个主 Agent 专门用来调度这三个 SubAgent，就能完成这个效果。

这个过程中稍微复杂的地方就在于要同时兼容三家的协议，不过这么多套壳 APP 都做了这个功能，想来不是太复杂（很多开源框架自带这个功能）😂。

这其实也是很多 Agent 产品的标配，只是它们没有拿出来宣传，尤其是那种不能选择模型的产品，其背后一定是多个模型联动协作完成任务。

最近，我也在做一个自动写故事的 Skill（纯粹学习，我的文章全是我手打的），当然它是一个完整的 Agent，包了 Skill 这个皮是为了我不用真的使用 SDK 去开发一个 Agent，我可以直接复用 Claude Code 的基础能力。

我借着这个 Skill 给大家分享一下，我设计 Agent 时惯用的五大模式。

1️⃣ 委托模式 & Evaluator-Optimizer

1️⃣ 委托模式 & 评估器-优化器

所谓委托，也是大家常说的Orchestrator-Workers（调度者-工人）模式，通过一个调度者 Agent 驱动所有 SubAgent 进行任务执行，在这个过程中，编排者只负责审查任务分发和审查。

我会将 SubAgent 分为两类：Plan Agent 和 Workers Agent，Plan Agent 负责任务规划，经过编排者审查之后交给 Workers Agent 去执行。

当然你可以再细分一个 Evaluator Agent 出来专门对 SubAgent 的结果进行评估，我一般就直接让调度者 Agent 进行评估。

采用这种方式还有一个好处就是：每个 SubAgent 具有独立的上下文，不会发生上下文爆炸。

2️⃣ Pipeline

2️⃣ 管道

通过构建流水线，编排所有 SubAgent 的行动，并将上一个 Agent 的最终输出作为下一个 Agent 的输入。

比如在我这个 Skill 中，流程就是：规划任务 -> 素材库研究 -> 各章节初稿 -> 文档审查（真实性 & 标点符号） -> 润色。

这套流程中，每一个环节结束的时候都会有一个审查机制，用来审查当前环节是否合格，审查者就是前面提到过的调度者 Agent 。

这样做有一个好处，就是一旦中间一个环节失误，无需从头来过，直接找负责此事的 Agent 让它重新迭代即可。

比如当我的任务在编写章节初稿的时候，调度者 Agent 发现前两章故事字数已经超过我们的规划字数，调度者 Agent 在审查的时候就会直接指出这个问题，并且让负责编写章节初稿的 Agent 迭代优化。

而前面的规划、素材库研究这些已经完成的任务都无需重复去做。

3️⃣ 断路器模式

当我们使用调度者 Agent 对每个 SubAgent 进行结果评估的时候，它都会维护一个迭代计数器。

每次它让 SubAgent 进行重新迭代，都会进行计数器 + 1，超过一定阀值之后，调度者 Agent 会暂时停下所有的 Agent 调度，并且向用户陈述目前遇到的困境，等待用户进行抉择。

4️⃣ 状态机模式

状态机存储了所有 Agent 的当前的任务执行结果、任务的中间结果和在任务执行期间会用到一个中间变量（比如迭代计数）。

它还兼顾着类似 Hook 的作用，前面我们提到过，每一个任务结束之后都会受到编排者 Agent的审查，那么审查条件就是放在状态机里面的，当审查通过之后编排者 Agent也会更新状态机中的状态。

你可以把它理解为一个复杂版的 TodoList，并且它的状态只有编排者 Agent 能操作。

除此之外，它还兼顾了恢复现场的重任，如果 Claude Code 意外崩溃，重启之后可以通过状态机中的记录恢复原有现场，编排者 Agent 继续统筹调度，完成剩余任务。

\---

上述这些模式只是我常用的，可以根据需要随时增加合适的模式进去，比如我就可以在素材库研究这一步加上并行 Agent，使用并行模式去提高网络检索的效率。

最后，如果大家有更好的实践，欢迎评论区提出，例子中的 Skill 完成流程在附图。

> 2026-01-06
> 
> 时间线上看到居然有人把豆包、Qwen、Claude 叫做 Agent（智能体）。
> 
> Agent 是什么，早先我曾在帖子里面提到过：LLM（大脑）+ Memory（长期/短期记忆）+ Planner（规划）+ Tool Use（工具调用） = AI Agent。
> 
> 如果一个东西满足了以上定义，它就是 Agent。
> 
> 推上最常见 Code Agent 是： Claude Code
> 
> ![Image](https://pbs.twimg.com/media/G-AD6VVbcAAiasu?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G98cy0CbcAAE3s9?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G98c2MObIAEUWsL?format=jpg&name=large)

* * *

**耳朵** @RookieRicardoR [2026-01-07](https://x.com/RookieRicardoR/status/2008709604516188377)

配图来自@dotey 宝玉老师提示词。

* * *

**Hedgeye** @Hedgeye

Hedgeye called the 2025 crash before it happened. Just like 2022. And 2020. And 2008.

18 years. Every crash called. No guesswork—just a proven, repeatable, data-driven process.

Stay ahead of the next big move. Start with The Macro Show.

Hedgeye 预测了 2025 年的崩盘，就像 2022 年、2020 年和 2008 年一样。

18年。每次崩溃都被预判。没有猜测，只有经过验证、可重复的数据驱动流程。

领先于下一个重大动向。从《宏观秀》开始。

* * *

**耳朵** @RookieRicardoR [2026-01-07](https://x.com/RookieRicardoR/status/2008712095026892916)

关注我，每天上午九点半更新。

* * *

**huangserva** @servasyy\_ai [2026-01-07](https://x.com/servasyy_ai/status/2008713194639159384)

断路器模式

这个我通常用开会模式和人类决策模式并行

* * *

**MindfulReturn 身心修复局** @MindfulReturn [2026-01-07](https://x.com/MindfulReturn/status/2008712488251191433)

不知trae能否用呢

* * *

**Q.Builds** @QBuildsAI [2026-01-07](https://x.com/QBuildsAI/status/2008711011319378093)

把Agent 说的明明白白

* * *

**耳朵** @RookieRicardoR [2026-01-07](https://x.com/RookieRicardoR/status/2008711189728292981)

哈哈哈 谢谢夸赞