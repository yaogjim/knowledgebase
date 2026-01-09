---
title: "2026-01-09_RookieRicardoR_最近一直在使用一个绝对被低估的开源宝藏组合_OpenCode_oh_my_opencode_如"
source: "https://x.com/RookieRicardoR/status/2007450352350834837"
author:
  - "[[@RookieRicardoR]]"
published: 2026-01-09
created: 2026-01-09
description:
tags:
  - "x"
  - "@RookieRicardoR"
  - "https"
  - "耳朵"
---

# 最近一直在使用一个绝对被低估的开源宝藏组合：OpenCode + oh-my-opencode。 如

**耳朵** @RookieRicardoR [2026-01-03](https://x.com/RookieRicardoR/status/2007450352350834837)

最近一直在使用一个绝对被低估的开源宝藏组合：OpenCode + oh-my-opencode。

如果你觉得 Claude Code 已经是体验天花板，那这个组合可能会刷新你的认知。

它不仅免费开源，更汇聚了 Claude Code 和 AmpCode 的所有优势，甚至在某些方面完成了超越。

🔥 什么是 OpenCode？它抛弃了枯燥的命令行，采用极其性感的 TUI (终端用户界面) 模式（见图一）。

这就好比把你的终端变成了一个 Cyberpunk 风格的指挥舱，信息流一目了然。

Oh my opencode 则是 OpenCode 的一个开源插件，它为 OpenCode 提供了一整套 Agent 任务处理机制，作者说他为了设计这套 Agent 架构，烧掉了价值 24,000 美元的 Token。

Oh my opencode 的核心在于多智能体编排和上下文治理，它解决了当前 AI 编程中最痛的几个点：

1️⃣ 异步 SubAgent

1️⃣ 异步子代理

它不是一个模型在干活，而是模仿了类似 Claude Code 的工作流，但更开放。

它会将不同的任务分派给不同的模型，默认情况下你需要设置 ChatGPT（ 架构审查）、Claude（规划委派） 和 Gemini（前端 UI） 三个模型。

当你下达复杂指令时，它会派生出专门的 Search Agent 或 Plan Agent 在后台异步工作，主线程不阻塞。

2️⃣ 关键词触发模式

Ultrawork Mode (ulw)：火力全开模式，并行调度多个 Agent 解决难题。

Think Mode：检测到关键词（如 "think deeply"）时，自动调整模型参数，强制 AI 进行长思维链推理（类似 o1/Gemini 3 的思考过程）。

Search/Librarian Mode：专门负责翻阅文档和检索代码库。

3️⃣ LSP & AST 深度集成

不像普通的 AI 只是“看文本”，它集成了 LSP (Language Server Protocol) 和 AST-Grep。

这意味着 AI 能像 IDE 一样理解你的代码结构（函数引用、定义跳转），而不是瞎猜。

4️⃣ 上下文焦虑管理

当 Context Window 用量达到 70% 或 85% 时，它会自动触发 Auto Compact，把旧的对话压缩总结，防止上下文溢出导致 AI 变笨或任务中断。

Tips：最近我在使用 Claude Code 的时候经常遇到上下文中断，上下文中断不是说上下文不够了，而是模型一次性给你吐出的字数是有限的，你如果用来写代码可能很少遇到，但是写文章我经常会遇到。

5️⃣防“太监”机制

AI 写长代码最爱写一半就停（// ...rest of code），这个插件会强制检查 TODO，逼着 AI 把代码写完。

6️⃣ 内置 MCP

Exa：用来网络搜索。

Context7：用来寻找文档。

Grep app：用来搜索 Github 上的代码。

除了以上特点，它还完美兼顾了兼容性，它兼容 Claude Code 的命令、代理、技能、MCP、钩子（PreToolUse、PostToolUse、UserPromptSubmit、Stop）机制。

并且它作为开源明星项目，还提供了不少免费模型，比如 GLM4.7 、MiniMax 2.1、Grok 免费用，甚至不用登录就能用，有点过于良心了。

对 Agent 有兴趣的小伙伴可以体验下～

![Image](https://pbs.twimg.com/media/G9vlc5fasAMdnsv?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G9viyk9asAIzjIt?format=jpg&name=large)

* * *

**耳朵** @RookieRicardoR [2026-01-03](https://x.com/RookieRicardoR/status/2007450355316265270)

Oh my opencode 这个插件需要先安装 Bun，这也是前段时间被 Claude 母公司 Anthropic 收购的那个开源项目。

Github 地址：

* * *

**Otter** @otterpal24 [2026-01-04](https://x.com/otterpal24/status/2007671022187884791)

为啥codex 只支持5.2，不支持5.2-codex-max ，也不支持5.2-max，按理说都是订阅登陆的

* * *

**耳朵** @RookieRicardoR [2026-01-04](https://x.com/RookieRicardoR/status/2007681123783184509)

可以选模型看看，这个你也可以自己改

* * *

**Spot & Tango** @spotandtango

Get 50% Off + FREE Fi Collar 🎁

100% real ingredients

No fillers or preservatives

Vet-developed recipes

Fresh without the fridge

50%折扣 + 免费 Fi 项圈 🎁

100%真实原料

不含填充剂或防腐剂

兽医研发的配方

新鲜不用冰箱

* * *

**雪踏乌云** @Pluvio9yte [2026-01-03](https://x.com/Pluvio9yte/status/2007468973269389621)

“强制检查TODO”怎么说 是检查自己维护的ToDo吗

* * *

**耳朵** @RookieRicardoR [2026-01-03](https://x.com/RookieRicardoR/status/2007473497938026823)

对 没执行完就继续的意思，其实这个功能 cc 本来就有，但是 opencode 应该是加了更多细致的 check，cc 有可能会自动断掉。

* * *

**一地鸡毛** @zhang\_baoqing [2026-01-06](https://x.com/zhang_baoqing/status/2008542283721822442)

工具太多了，我纯小白，我今天才搞懂怎么在windows 终端用claude code 。怨不得程序员掉头发，发现太快了，需要学的太多了。程序员都是用脑过度

* * *

**耳朵** @RookieRicardoR [2026-01-06](https://x.com/RookieRicardoR/status/2008542664552308982)

哈哈哈 win 好像是比 mac 困难点

* * *

**吹衣轻飏** @jasonya76775253 [2026-01-03](https://x.com/jasonya76775253/status/2007488768824205637)

它有一个硬伤：无法看到你ide当前打开的是哪个文件，当你给他说这个是啥，它会问你，你说的这是指什么

* * *

**耳朵** @RookieRicardoR [2026-01-03](https://x.com/RookieRicardoR/status/2007489345771745723)

这个问题是因为它没有上下文焦点，如果你用的是插件可能会好点，最简单的方式就是使用 @ 符号，我在使用 CC 的时候也会使用 @ 直接引用文件。

* * *

**Jakku 彼岸樱** @JakkuSakura [2026-01-04](https://x.com/JakkuSakura/status/2007755511564030287)

确实很漂亮，不过纯订阅的成本太高了，还不支持codex代理

* * *

**耳朵** @RookieRicardoR [2026-01-04](https://x.com/RookieRicardoR/status/2007756577613521371)

安装插件可以

* * *

**Vincent** @Vincentcharming [2026-01-03](https://x.com/Vincentcharming/status/2007452300391157862)

插件听起来很强大啊，也可以调用Opus 4.5模型嘛？

* * *

**耳朵** @RookieRicardoR [2026-01-03](https://x.com/RookieRicardoR/status/2007452349921697839)

可以 默认就是 ops4.5