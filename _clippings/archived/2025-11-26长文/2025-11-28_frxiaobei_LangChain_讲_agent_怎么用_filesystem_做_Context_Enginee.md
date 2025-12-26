---
title: "2025-11-28_frxiaobei_LangChain_讲_agent_怎么用_filesystem_做_Context_Enginee"
source: "https://x.com/frxiaobei/status/1994021524899013096"
author:
  - "[[@frxiaobei]]"
published: 2025-11-28
created: 2025-11-28
description:
tags:
  - "x"
  - "@frxiaobei"
  - "https"
  - "context"
status: "inbox"
importance: 2
effort: 2
review_level: 0
review_next: "2025-12-10"
review_interval: null
review_count: 0
decision: null
topics: []
links_out: []
summary: ""
pov: ""
actions: []
---

# LangChain 讲 agent 怎么用 filesystem 做 Context Enginee

**凡人小北** @frxiaobei 2025-11-22

LangChain 讲 agent 怎么用 filesystem 做 Context Engineering，看的我想笑。

这不就是 Manus 那套上下文工程的灵魂思路嘛？

把信息从 prompt 里解放出来，

放到外部状态里，

该读读、该丢丢、不要把模型当仓库塞爆。

核心都是把 context 变成可控资源，上下不可控猛堆料跟祈祷没什么区别。

但有些许区别，LangChain 走得更彻底。

它让 agent 把 filesystem 当自己的大脑皮层，

目录结构就是抽象层级，grep/glob 就是检索机制。

（是不是很熟悉，有两家大模型也是这么干的）

搜索结果先写进文件系统，再按需召回。

提示词/工具说明/路线图/思考过程全写到文件里，

由 agent 自己增删改查。

这种感觉特别熟悉，

在前互联网时代，当架构走到系统级，大家最后都会殊途同归。

无论是 Manus 的 context-threads / scratchpad / lifecycle management，

还是 LangChain 的 filesystem-first / modular-agents / lazy-context，

最后都指向一句话：

Context ≠ Token Window，Context = 外部化状态 + 调度机制 + 可维护结构。

模型再大，拼到最后还是工程，至少现阶段看还是这样。

> 2025-11-22
> 
> Understanding context engineering - and how it can fail - is crucial for building reliable agents.
> 
> We wrote up some strategies for using a filesystem to address common challenges with context engineering:
> 
> \- Too many tokens: use the filesystem as a scratch pad instead of keeping
> 
> 理解上下文工程及其可能失效的原因，对于构建可靠的智能体至关重要。
> 
> 我们整理了一些利用文件系统应对上下文工程常见挑战的策略：
> 
> \- 令牌过多：使用文件系统作为临时存储区，而非持续保留
> 
> ![Image](https://pbs.twimg.com/media/G6VukBXbgAAtHiP?format=jpg&name=large)

* * *

**TimNew** @TimNew [2025-11-27](https://x.com/TimNew/status/1994129221288169900)

這麼幹最大的問題就是「它不知道它不知道」，既然不知道也就不會去 search。

CC 最近的 Tool Search Tool 有類似的問題，但是那個還能通過 Prompt 模型來找回。

但是 Context 是徹底動態的，這個找補不是絕對做不到，但是會難很多。

結果就是模型可能要麼不停瞎搜索，要麼遺漏數據

* * *

**蔡荔谈AI (公众号）** @JonathanCaiSG [2025-11-28](https://x.com/JonathanCaiSG/status/1994222032075280769)

用filesystem做rag的，OpenAI、Anthropic、Google都有各自的方案，不过都比较适合小规模的数据，比如200G一下，30-30000个文件(适用范围会根据模型不同有所差异)，再大一点的，还是要用传统的RAG方式

* * *

**Pass** @Pass22917887 [2025-11-27](https://x.com/Pass22917887/status/1994093462032200119)

langgraph 也有自己开源的 cil，基于 deepagents 项目实现的

* * *

**墨白Labs主任** @mobailabs [2025-11-27](https://x.com/mobailabs/status/1994056549514526832)

目前这块做得好的，也就是cc了，plugin扩展性太棒了

* * *

**Pass** @Pass22917887 [2025-11-27](https://x.com/Pass22917887/status/1994092846983659988)

我记得 langchain 有请教 manus ，有专门的博客，还参考了 claude 的相关提示词

* * *

**Yanhua 彦华** @yanhua1010 [2025-11-27](https://x.com/yanhua1010/status/1994055568172962088)

context可以无限大，但是token window不会

* * *

**slade** @sladee1992 [2025-11-28](https://x.com/sladee1992/status/1994223218136109181)

跟 speckit 一个思路呀

* * *

**QiPing Wan** @QipingWan [2025-11-27](https://x.com/QipingWan/status/1994100438493483107)

用时探索