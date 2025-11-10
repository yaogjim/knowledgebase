---
title: "功能层次设计：Manus LLM 系统的 3 层工具分离"
source: "https://x.com/dotey/status/1979041449892004117"
author:
  - "[[@dotey]]"
published: 2025-10-17
created: 2025-10-17
description:
tags:
  - "@dotey # Manus # LLM # AI # 峰谷技术 #"
status: "inbox"
importance: 2
effort: 2
review_level: 0
review_next: "2025-10-27"
review_interval: null
review_count: 0
decision: null
topics: []
links_out: []
summary: ""
pov: ""
actions: []
---
**宝玉** @dotey 2025-10-17

确实，Manus 很聪明，他们把工具分成了 3 层：  
  
第 1 层：函数调用 (Function Calling)  
第一层：函数调用  
  
这是最基础的一层，只保留一小组固定的、原子化的函数，比如：读写文件、执行 Shell 命令、搜索文件等。在 LLM 的系统提示词中就只有这一层的工具定义，相对比较少，15 个以内，输入格式和输出格式都很清晰，不容易出错，但这里面有两个工具很特殊，一个是 Shell， 一个是 File。  
  
第 2 层：沙箱工具 (Sandbox Utilities)  
  
每个 Manus 会话都运行在一个完整的虚拟机沙箱里。就是原推文提到的，虚机预装了很多命令行工具，比如格式转换器、语音识别工具，甚至一个 mcp 命令行客户端。  
  
然后这些工具都通过第 1 层中定义的 Shell 来调用，就是命令行工具，命令行调用。  
  
但是这么多工具模型怎么知道呢？  
  
Manus 在系统提示词里会直接告诉 LLM，在一个特定的文件夹里有很多预装的命令行工具。对于最常用的工具，直接列出它们的名字。不常用的，LLM 可以直接通过原推提到的命令列出所有命令行工具，通过 --help 参数来查看任何一个工具的用法，因为所有这些工具都是他们自己开发的，格式统一。  
  
第 3 层：代码包与 API (Packages and APIs)  
  
这一层其实就是 LLM 实时编写 Python 代码，通过代码实现更复杂的功能。比如用户想查询某个 API 的数据，可以直接用 Python 写一个函数，fetch API 的数据，并解析成需要的格式。  
  
其实在 Codex 中，用 Python 代码当工具已经用的很多了。  
  
由于复杂的运算都是代码完成的，返回给 主 Agent 的知识计算后的结果，所以并不会占用主 Agent 的上下文。  
  
这样 3 层设计的好处是，从模型的角度看，它需要调用的工具就固定是第 1 层的十几个，而借助命令行和代码，它又可以衍生出无数的工具组合。  
  
还有一点就是我在之前推文提到的子智能体，Manus 也是大量采用“智能体即工具 (agent as tool)”的模式。把子智能体当工具用，比如负责检索是一个子智能体，但是这个子智能体在主 Agent 看来就是一个工具。同时也可以很好的起到减少上下文的效果。

> 2025-10-17
> 
> Claude 的 Agent Skills 本质上是一种“上下文卸载”，把冗长的技能信息移出上下文，按需加载。巧的是最近 Manus 的 Peak 也分享一些“上下文卸载”的技巧。Manus x.com/dotey/status/1…
> 
> ![Diagram titled Context Offloading shows three layers: top layer with functions like message, shell, search, create model, browser connected downward to second layer with 1-minute message, analyze data, and third layer with 5-minute analysis, using colors blue, pink, gray for elements and arrows indicating flow.](https://pbs.twimg.com/media/G3b0_NUWcAAl8y9?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G3bqREpWkAAE-Qx?format=png&name=large)

---

**Tz** @Tz\_2022 [2025-10-17](https://x.com/Tz_2022/status/1979139414874845623)

可这么搞迟早会撞上停机问题的。。。

---

**Feynmion** @feynmion [2025-10-17](https://x.com/feynmion/status/1979057565741822294)

智能体即工具这种思路其实就是用调用关系组建智能体调用树，分解复杂任务。这种思路的先天缺陷是调用关系是单向的，一旦子agent出错会影响整个任务的成功率。解决方法其实也简单，引入双向对话代替调用关系，即交互式智能体调用树，这个在2023年开源的AIlice中就引入，可惜业界沉迷于静态拓扑不能自拔

---

**Tom.Hady** @TomCaoOnline [2025-10-17](https://x.com/TomCaoOnline/status/1979087044371530219)

各服务层的颗粒度定义很清晰👍【PS：想到了微服务时代的分层：原子服务+领域服务+聚合服务，可惜很多团队落地时就崩了😄】，看得出来manus的架构+工程化水平，这肯定不是靠Vibe Coding出来的～😂