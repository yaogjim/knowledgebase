---
title: "(1) Yuker on X: "“Manus”级智能体：用 MCP 协议，让你的 Claude Code 第一次真正触碰世界（附完整步骤）" / X"
source: "https://x.com/0xYuker/status/2010298647553138714"
author: ""
created: 2026-01-12 09:01:10
date: 2026-01-12 09:01:10
description: ""
tags: ""
---
在前三篇的旅程中，我们共同拆解了

、Skills 和 Sub-Agent 的原理。看到评论区里那些鲜活的实践案例，我能感受到这些工具正悄然在大家手中生根发芽。

在这个过程中，你是否产生过一种奇妙的错觉：你的 Agent 似乎正变得越来越像 ‘你’？它不仅承载了你的知识体系，甚至开始复刻你的思维偏好。这种感觉，就像在精心雕琢一个平行世界的自己。

但这个平行世界的自己，他却没法真正的接触这个世界，自始至终的被困在主机的牢笼之中。

既然‘灵魂’已初具雏形，那么今天，我们将正式推开新手村的大门。是时候让你的 Agent 告别实验室环境，去迎接真实世界的挑战了。

我们今天要讲 -- 模型上下文协议（Model Context Protocol, MCP）。

[

![Image](https://pbs.twimg.com/media/G-W25NBW4AEU6AG?format=png&name=medium)



](https://x.com/0xYuker/article/2010298647553138714/media/2010213902554947585)

你有没有想过，为什么我们的AI如此强大，却像被困在一个玻璃盒子里？这就是 “M×N 困境”。 每个应用（M）想接入不同的 AI（N），都需要编写特定的集成代码。这堵墙，把 AI 困在了本地，让它成了一个信息孤岛。

MCP 的诞生，就是为应用提供了一个统一的、开放的协议；像一把万能钥匙，打开了 AI 通往外部世界的大门。有了它，你的 AI 不再是一个只能在本地读写文件的“单机工具”。

它能连接 GitHub 创建 PR、查询生产数据库、读取 Jira 任务、甚至发送 Slack 消息。这不仅仅是能力的叠加，而是质的飞跃——从一个工具，进化为一个真正意义上的智能代理（Agent）。

而今天，我将从一个最简单却最实用的例子进行讲解； 看完后，你也可以轻松让你的 Claude Code 随意支配你的浏览器。

这部分会分两部分进行讲解，分别是“基础组件”和“运行架构”。

可以这样去理解：运行架构（Host/Client/Server）是“物流管道”，而基础组件（Tools/Resources/Prompts）是管道里运输的“货物”。

现在我们带着这样的理解，继续深入了解他们各自包含着什么。

> 不论你想要做多么复杂的 Agent，归根结底，你只需要搞定三件事情：Tools，Resources，Prompts

[

![Image](https://pbs.twimg.com/media/G-W7i_2a0AAqSnu?format=jpg&name=medium)



](https://x.com/0xYuker/article/2010298647553138714/media/2010219018620424192)

[

![Image](https://pbs.twimg.com/media/G-W-kJ-WQAAtiM4?format=png&name=medium)



](https://x.com/0xYuker/article/2010298647553138714/media/2010222337052786688)

-   🛠️Tools：可以理解为AI的“武器”或“道具”，控制方是Claude Code，本质是一组可执行的函数，让AI决定何时进行调用。实际上Claude Code内置了Filesystem MCP，里面有一组工具，你可以输入 /mcp 进行查看。 也正是这组工具，让Claude Code可以随时查看和修改本地文件。
    
-   🧱Resources：可以理解为“Read-only”的数据源，为 CC 提供上下文。因为数据源具有敏感性，所以一般由应用或用户来进行控制。
    
-   🧠Prompts：一套“SOP”。它不是智商本身（智商是模型给的），它是经验。它把复杂的任务拆解好，手把手教 AI “第一步做什么，第二步做什么”。
    

```
┌────────────────────────────────────────────────┐
│                 MCP Host                       │
│            (如 Claude Code)                    │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐      │
│  │ Client 1 │  │ Client 2 │  │ Client 3 │      │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘      │
└───────┼─────────────┼─────────────┼────────────┘
        │ 1:1         │ 1:1         │ 1:1
        ▼             ▼             ▼
   ┌─────────┐   ┌─────────┐   ┌─────────┐
   │ GitHub  │   │ Sentry  │   │ 数据库  │
   │ Server  │   │ Server  │   │ Server  │
   └─────────┘   └─────────┘   └─────────┘
```

这张图看上去很晦涩难懂，但是不用担心，他们其实并不复杂。我们只需要弄明白他们各自代表着什么即可。

我想了很久，到底它像什么呢？然后我发现它其实跟我们的电脑非常相似：

-   🖥️MCP Host ：我们的笔记本电脑 - 角色： 它是“大脑”和“环境”。你通过键盘输入指令，在屏幕上看结果。 - 实例： Claude Code 或 Cursor 就是当前的 Host，它决定了 AI 在什么环境下为你服务。
    
-   🖱️Server ： 各种外设 - 角色： 它是能力提供者。它不直接和用户说话，只静静等待 Client 的调用。 - 实例： Google Maps Server（查地图）、File System Server（读写文件）。只要插上（配置好）这个“外设”，你的 Host 电脑就立刻拥有了新的技能。
    
-   🔌Client ： 电脑侧边的USB接口 - 角色： 它是连接桥梁。虽然外设在外面，但必须通过这个标准的“接口”才能与电脑通信。 - 特性： 就像一个接口对应一个设备，Host 内部会为每一个集成的 Server 启动一个 Client 实例。它负责把 Host 的意图翻译成 Server 能听懂的语言，并把结果带回来。 - 为什么叫 Client： 因为在网络关系中，它是主动拨号、请求连接的那一方。
    

现在再去 Claude Code 界面输入 /mcp 查看时，大家应该会有更直观的感受：

[

![Image](https://pbs.twimg.com/media/G-XrlCVa0AIi19b?format=png&name=medium)



](https://x.com/0xYuker/article/2010298647553138714/media/2010271830205190146)

-   MCP Host：Claude Code 本身  
    MCP 主机：Claude 代码本身
    
-   Server ： Filesystem，Chrome-devtools  
    服务器：文件系统，Chrome 开发者工具
    
-   Client ： 这个比较隐形，但是看到“Connected”的话，代表Client已经对接上Server了
    

到这里如果大家已经理解了，那我们要开始直接进行实操了！

> 我们在配置MCP前，先要敏锐洞察我们实际的需求到底是什么。

比如玩英雄联盟，我们想要获得高攻击力，就需要出物理装备；对面刺客多，我们就需要出金身保命。

而今天我想核心解决的需求是：我的Claude Code没有办法替我上网干活！

现在已经有不少开发者，在 Github 上发布了非常好用且免费的开源 MCP；我们只需要根据我们的需求来进行配置即可。

而这次我们为了解决 Claude Code 无法操作浏览器这个问题，使用的 MCP 是：

我进入Github页面后，我们可以非常清晰查看到，这个MCP有什么样的 Tools 可供调用：

[

![Image](https://pbs.twimg.com/media/G-XxY5UbIAAP4N6?format=jpg&name=medium)



](https://x.com/0xYuker/article/2010298647553138714/media/2010278218696433664)

我们发现这个 MCP 居然拥有 Click，Fill等功能；因此我感觉哪怕它只是一个调试浏览器页面的一个 MCP，或许它也能帮我实现让我的Claude code 自行上网的功能！

[

![Image](https://pbs.twimg.com/media/G-XzooMagAILgQi?format=jpg&name=medium)



](https://x.com/0xYuker/article/2010298647553138714/media/2010280688000598018)

在 Github 的页面上，我们能看到有一行这样的代码：

```
claude mcp add chrome-devtools npx chrome-devtools-mcp@latest
```

只需要把这行代码输入到命令行，即可以完成安装，就这么简单！随后只需要打开Claude Code，输入 /mcp 进行查看，如果你的画面跟我一样，那么恭喜你！你已经拥有了这个 MCP 的能力了！

[

![Image](https://pbs.twimg.com/media/G-X0u-aaAAAgyom?format=png&name=medium)



](https://x.com/0xYuker/article/2010298647553138714/media/2010281896555708416)

现在我们再试试询问文章开头的问题，发现我们的Claude Code居然会自己调用 MCP 来操作浏览器进行检索信息了！

[

![Image](https://pbs.twimg.com/media/G-X2R0ZbwAAEYjs?format=png&name=medium)



](https://x.com/0xYuker/article/2010298647553138714/media/2010283594674323456)

不单如此，当你询问一些你想知道的问题时，Claude Code甚至会自己打开浏览器进行检索信息，并把结果返回给你！

[

![Image](https://pbs.twimg.com/media/G-X51obbwAAbTdh?format=png&name=medium)



](https://x.com/0xYuker/article/2010298647553138714/media/2010287508471660544)

我这里问Claude Code：A16Z最近是不是募资了一笔钱。Claude Code理解了我对信息及时性的需求，而他目前可以用的工具只有Chrome-devtools，因此它开启了浏览器进行检索信息。

[

![Image](https://pbs.twimg.com/media/G-X6Pg9bYAAXcXq?format=jpg&name=medium)



](https://x.com/0xYuker/article/2010298647553138714/media/2010287953143357440)

甚至当Claude Code发现dev的Chrome被Google拦截了的时候，还会主动尝试其他方法，去用了百度检索！直到最后检索到了答案，再把答案返回给你，非常的聪明可靠！

[

![Image](https://pbs.twimg.com/media/G-X6lnPbsAIC0-G?format=png&name=medium)



](https://x.com/0xYuker/article/2010298647553138714/media/2010288332786610178)

从“万能插头”的构想，到“手、眼、脑”的协同工作，再到“组合使用”的惊艳效果，MCP 为我们描绘了一幅 AI 深度融入软件开发全流程的蓝图。

它不再仅仅是一个协议，更是一种全新的工作范式。它将 AI 从一个被动的“代码补全工具”，转变为一个主动的“问题解决伙伴”。通过 MCP，我们每个人都可以将自己的本地开发环境，逐步调教、扩展成一个强大、高效、高度定制化的“Manus”级智能体。

考虑到篇幅限制与阅读体验，本文暂未深入探讨涉及身份认证的 MCP 服务。目前展示的能力仅是冰山一角；诸如 Claude Code 在单次任务中的多轮 MCP 调用，以及它与 Skills、Sub-agent 之间的协同作战技巧等进阶内容，我们将在后续文章中进一步拆解。