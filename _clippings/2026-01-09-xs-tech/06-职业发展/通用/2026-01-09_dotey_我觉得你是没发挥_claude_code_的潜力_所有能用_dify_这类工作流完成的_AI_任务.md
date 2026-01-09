---
title: "2026-01-09_dotey_我觉得你是没发挥_claude_code_的潜力_所有能用_dify_这类工作流完成的_AI_任务"
source: "https://x.com/dotey/status/2009474762070691904"
author:
  - "[[@dotey]]"
published: 2026-01-09
created: 2026-01-09
description:
tags:
  - "x"
  - "@dotey"
  - "2026-01-09"
  - "https"
---

# 我觉得你是没发挥 claude code 的潜力，所有能用 dify 这类工作流完成的 AI 任务，

**宝玉** @dotey 2026-01-09

我觉得你是没发挥 claude code 的潜力，所有能用 dify 这类工作流完成的 AI 任务，几乎都可以用 skills + subagent 完成，除了一些特别要求在云端完成你又没有 API 的。

skill 你不能只当作单一技能，还要把它们组合起来用，先把工作流中需要的能力都拆分成单一的 skill 或者 subagent，然后由一到多个 skills 把这些 skill 用自然语言编排起来，换句话说就是用自然语言去描述你的工作流。

所有的中间结果都保存成本地文件，多用 subagent 去分摊上下文，subagent 只传入文件路径返回文件路径。

其他的都交给 Claude

> 2026-01-09
> 
> 通用agent这个说法棒极了，我的cc已经取代了一多半 @dify\_ai 的任务了，尽管Dify依然是超复杂任务的不二之选，但cc可以使用claude subscription的额度，一些简单任务完全可以做到平替

* * *

**宝玉** @dotey [2026-01-09](https://x.com/dotey/status/2009497792956506253)

是的，基于本地文件系统的 skill/subagent 还有个好处，就是你可以一直迭代，让 claude code 帮你维护更新，一直改进优化，越来越好用

> 2026-01-09
> 
> 多谢玉佬指教😄cc还有一个很强但很少人用的地方，是可以自己迭代subagent的system prompt，配合ralph-loop，已经可以完成自我迭代进化了。在token和系统资源充足的情况下，能进化成非常恐怖的存在。

* * *

**𝙩𝙮≃𝙛{𝕩}^A𝕀²·ℙarad𝕚g𝕞** @TaNGSoFT [2026-01-09](https://x.com/TaNGSoFT/status/2009491309338452294)

宝玉老师这段话，让我想起skills可能就是LLM作为一种语言符号智能价值落地的胶水层，cc还是脚手架。

* * *

**Vincent** @win1688888888 [2026-01-09](https://x.com/win1688888888/status/2009482266960122073)

要让 Skills 组合真正像 Dify 那样稳固，必须引入 Schema Validation。否则 Subagent A 输出的 JSON 缺个字段，Subagent B 读文件时就会直接崩溃或产生幻觉。

* * *

**宝玉** @dotey [2026-01-09](https://x.com/dotey/status/2009484247166537929)

不需要那么严格，不需要json，我都是传文件路径。而且是模型自己在中间控制，出错会自己修复重试

* * *

**刚戈** @gangxiao [2026-01-09](https://x.com/gangxiao/status/2009509876213395468)

完全赞同！您说的其实就是 AI 领域的“乐高”思想或“Unix哲学”—— 每个 Skill 只做一件事并做到极致，然后用 Subagent 像管道一样把它们串联起来。这种模式的想象空间比拖拽式的UI大太多了。感谢分享！

* * *

**pippingg** @Suyanzhenq [2026-01-09](https://x.com/Suyanzhenq/status/2009496471234912751)

多谢玉佬指教😄cc还有一个很强但很少人用的地方，是可以自己迭代subagent的system prompt，配合ralph-loop，已经可以完成自我迭代进化了。在token和系统资源充足的情况下，能进化成非常恐怖的存在。

* * *

**有志出海** @0xValkyrie\_ai [2026-01-09](https://x.com/0xValkyrie_ai/status/2009482327525622086)

dify 这类工作流， 我的理解， 它其实就是帮把相关的skill 封装个了一个个模块， 有点类似乐高的积木， 例如乐高的积木，有车轮的， STEM 模块等。 你想做成什么模型， 就选用相应的模块， 但是客制化很低。 同时需要自己手动的把模块联动起来。

而Claude 的skills ， 除了有dify 这类，

* * *

**柳扶苏** @liuyiwan888 [2026-01-09](https://x.com/liuyiwan888/status/2009502691299385698)

现在不少人用 Dify 这类工具，本质是在把思路固化成一个可视化流程图，舒服是舒服，但上限也基本被锁死了。你说的 skills + subagent，反而是在把流程“拆回语言”，让模型自己去理解和调度，而不是被节点牵着走。

尤其是两点很关键：

一是 skill 不能当成孤立能力用，真正有价值的是组合方式；二是

* * *

**Doiiars Fortune** @Daiiors [2026-01-09](https://x.com/Daiiors/status/2009487157120118803)

skill就是在简化agent的定义。

* * *

**Morris Hsu** @morris754 [2026-01-09](https://x.com/morris754/status/2009507729023619125)

如果有開源的 multi-skill repo 想看看怎麼搭建

* * *

**wsjcfbvkvng** @2647352920 [2026-01-09](https://x.com/2647352920/status/2009486393278710086)

第二段真的学到了！感谢，已收藏(^🙏^)

* * *

**文明的成本** @EbFak99441 [2026-01-09](https://x.com/EbFak99441/status/2009512933630595580)

努力学习状态

* * *

**中重** @sisyphu19507252 [2026-01-09](https://x.com/sisyphu19507252/status/2009477419112202605)

他不是说了烧不起的原因

* * *

**Yiyuan** @yiyuan1359 [2026-01-09](https://x.com/yiyuan1359/status/2009516261265584214)

Dify 的核心价值，是把不确定性压平。

你把流程画出来、节点连好，执行路径是确定的，适合稳定场景、团队协作、低心智成本。

Claude Code 的优势，是把流程还原成语言。

不预先锁死路径，而是通过 skills + subagent 让模型自己理解、组合、修正流程。

上限更高，但前提是你会拆任务、愿意持续迭代。