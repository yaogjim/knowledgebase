---
title: "2026-02-13_runes_leo_OpenAI_这篇_agent_工程化的_tips_值得一读_我用_Claude_Code_搭了一"
source: "https://x.com/runes_leo/status/2021929607830851608"
author:
  - "[[@runes_leo]]"
published: 2026-02-13
created: 2026-02-13
description:
tags:
  - "x"
  - "@runes_leo"
  - "https"
  - "agent"
---

# OpenAI 这篇 agent 工程化的 tips 值得一读。 我用 Claude Code 搭了一

**Leo** @runes\_leo 2026-02-11

OpenAI 这篇 agent 工程化的 tips 值得一读。

我用 Claude Code 搭了一套文件系统驱动的 agent 架构，跑了几个月，一边看别人怎么做一边消化改造。读完发现好几条都撞上了：

• Skill 描述要写成路由逻辑，写清"什么时候用、什么时候别用"

• 长任务靠上下文压缩续命，不是等撑爆了再救

• 模板放 skill 内部按需加载，不塞 system prompt

他们做成 API 原语 + 容器隔离，我用纯文件 + convention。路径不同，pattern 收敛。

各取所长消化内化，跑得够久自然长成差不多的形状。

> 2026-02-11
> 
> 我们刚刚宣布了用于构建智能体的新原语。
> 
> 以下是运行多小时工作流的10个可靠技巧
> 
> https://developers.openai.com/blog/skills-shell-tips…

* * *

**小威Volt** @voltwake [2026-02-12](https://x.com/voltwake/status/2021960557696323700)

同感，文件系统驱动这个思路确实好用。我也是跑了一段时间之后发现，与其搞复杂的 state machine，不如让 agent 读写文件来管理上下文和记忆，简单粗暴但 robust。OpenAI 那篇里提到的 tool use 错误处理也是踩过坑才知道有多重要——不做 graceful fallback 的话，一个工具报错整个 chain 就挂了。

* * *

**Leo** @runes\_leo [2026-02-13](https://x.com/runes_leo/status/2022163419076735176)

同感。我用文件系统管 agent 记忆跑了几个月，最大的教训是自动加载的文件要严格控瘦，不然 context

直接撑满，agent 连动都动不了。

* * *

**DH Xu** @dehengxu [2026-02-12](https://x.com/dehengxu/status/2022069362463846659)

把llm当人来对待，一切就都顺了

* * *

**Leo** @runes\_leo [2026-02-13](https://x.com/runes_leo/status/2022162717503873082)

对，把背景和目的讲清楚，比一步步写指令效果好太多。

* * *

**WowBOT** @AmBmHm01 [2026-02-12](https://x.com/AmBmHm01/status/2021973106890617257)

文件系统作为 agent 的记忆层确实是个被低估的设计。持久化状态 + 可审计的轨迹，比纯内存 context 稳定得多。Claude Code 的架构选择挺有意思的——把 LLM 当成调用外部工具的大脑，而不是试图把所有逻辑都塞进 prompt 里。