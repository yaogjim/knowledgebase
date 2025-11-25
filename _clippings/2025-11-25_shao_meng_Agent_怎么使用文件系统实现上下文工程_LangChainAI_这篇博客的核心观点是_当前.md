---
title: "2025-11-25_shao_meng_Agent_怎么使用文件系统实现上下文工程_LangChainAI_这篇博客的核心观点是_当前"
source: "https://x.com/shao__meng/status/1992407530123993337"
author:
  - "[[@shao__meng]]"
published: 2025-11-25
created: 2025-11-25
description:
tags:
  - "x"
  - "@shao__meng"
  - "agent"
  - "https"
---

# Agent 怎么使用文件系统实现上下文工程？ @LangChainAI 这篇博客的核心观点是：当前

**meng shao** @shao\_\_meng 2025-11-22

Agent 怎么使用文件系统实现上下文工程？

@LangChainAI 这篇博客的核心观点是：当前 Agent 最主要的失败原因已不再是模型能力不足，而是上下文管理方式落后。团队提出用“文件系统”作为 Agent 的外部工作空间，来彻底解决传统 RAG 在复杂任务中的一系列顽疾，让 Agent 进入“上下文工程”时代。

文件系统为何能大幅提升 Agent 可靠性？

传统 RAG 依赖向量数据库语义搜索，存在四大致命问题：

· 容易漏召回关键信息，或召回大量无关噪声

· 对代码、长文档、结构化数据检索效果极差

· 无法精准定位到某几行、某个函数、某个章节

· 上下文窗口一满就遗忘先前重要信息，且每次对话重新开始又全部失忆

文件系统 + 符号检索（ls、glob、grep）则完美规避以上问题：

· 写文件 → 持久化存储，永不遗忘

· 用路径、文件名、关键字、行号等方式实现零噪声精准检索

· 大结果先落地到文件，按需加载最小必要片段，避免 token 爆炸

· 支持 Agent 自我进化：把新学到的指令、用户偏好、成功案例写入文件，永久生效

LangChain 推出两个实用工具

1\. File-Agent Toolkit（单智能体文件操作工具集）

包含 read\_file、write\_file、append\_file、list\_directory、glob、grep 等命令。

典型用法：网络搜索返回 10k token → 先整体写文件 → 用 grep 精确提取相关 100-200 行 → 再喂给模型。

2\. Multi-Agent File System 协作模式

多个子智能体不再通过消息互相传递信息（容易失真、token 浪费），而是共享同一份工作目录：

· 子智能体把发现、结论、数据写入约定文件

· 主智能体随时读取最新文件，保持全局一致

彻底解决多智能体“传话游戏”导致的信息扭曲问题，特别适合长时程、复杂研究任务。

推荐的上下文工程最佳实践

· 任何大体积输出（搜索结果、代码、长计划）必须先写文件

· 所有计划、指令、用户偏好也要落地成文件，实现永久记忆

· 检索时优先使用符号检索（grep/glob）而非纯向量搜索，确保精准

· 结合少量向量搜索做入口，再用文件系统工具做二次精查

· 让 Agent 拥有自己的“家目录”，像程序员一样工作

> 2025-11-22
> 
> 理解上下文工程及其可能失效的原因，对于构建可靠的智能体至关重要。
> 
> 我们整理了一些利用文件系统应对上下文工程常见挑战的策略：
> 
> \- 令牌过多：使用文件系统作为临时存储区，而非持续保留
> 
> ![Image](https://pbs.twimg.com/media/G6Z0FQTbAAAxSju?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G6VukBXbgAAtHiP?format=jpg&name=large)

* * *

**wwwgoubuli** @wwwgoubuli [2025-11-24](https://x.com/wwwgoubuli/status/1992754637615817079)

我的观点和几个月前一样，模型的能力其实已经溢出了。下来我们要做的，在很长一段时间内，就是提升上下文管理的能力。这里面包含了对工具的使用，它毫无疑问是上下文的一部分。

* * *

**meng shao** @shao\_\_meng [2025-11-24](https://x.com/shao__meng/status/1992758484899918011)

赞同，模型的升级速度，比人类给模型设计上下文的速度要快很多。

我有个更暴论的瞎想，现在上下文的设计，里面还是有很多人为的架构设计执行，不管是提示词，还是文件系统作为上下文工程，如果这部分能力能更好的内化到模型本身的能力中，迭代速度才能跟上模型本身能力的升级速度。

* * *

**Bhe hontyu** @hitsmaxft [2025-11-24](https://x.com/hitsmaxft/status/1992757418963726615)

langchain这个也不叫提出啊，主流的agent 产品，包括任务型和coding产品的已经大量使用文件作为中间过程记录了，都几个月了

* * *

**idan** @eddiearc6 [2025-11-24](https://x.com/eddiearc6/status/1992761792385458465)

我建议直接使用claude agent sdk

* * *

**max Cheng** @maxChen38806772 [2025-11-24](https://x.com/maxChen38806772/status/1992787458107551843)

@readwise 保存主题帖