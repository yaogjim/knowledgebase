---
title: "2026-02-13_dotey_推荐吕鹏开源的_Agmente_项目_让你可以从_iOS_手机上操作_Coding_Agent_Co"
source: "https://x.com/dotey/status/2021408739748684039"
author:
  - "[[@dotey]]"
published: 2026-02-13
created: 2026-02-13
description:
tags:
  - "x"
  - "@dotey"
  - "agent"
  - "2026-02-11"
---

# 推荐吕鹏开源的 Agmente 项目，让你可以从 iOS 手机上操作 Coding Agent Co

**宝玉** @dotey 2026-02-11

推荐吕鹏开源的 Agmente 项目，让你可以从 iOS 手机上操作 Coding Agent Coding Agent。

OpenClaw 让我们看到了很多从手机指挥 Agent 的有趣场景，通过 Agmente 你可以在手机上跟 Gemini CLI、Claude Code、Qwen 等 AI 编程 Agent 对话，实时查看它们的工具调用和执行结果。

吕鹏是 VS Code 团队的工程经理，主导了将 Copilot Coding Agent 和 GitHub Copilot CLI 集成到 VS Code 的工作，可以说他是最了解编辑器如何与 AI Agent 对接这件事的人之一。

Agmente 最特别的地方在于它实现了 ACP（Agent Client Protocol，智能体客户端协议）——一个正在快速崛起的开放标准。

ACP 要解决什么问题？ 现在 AI 编程 Agent 越来越多（Claude Code、Gemini CLI、Codex CLI……），编辑器/IDE 也很多（VS Code、Zed、JetBrains、Neovim……）。如果没有统一标准，每个编辑器想接入每个 Agent 都要单独写一套集成代码，反过来每个 Agent 想支持每个编辑器也一样。这就是经典的 M×N 问题。

ACP 就是来解决这个问题的。它的角色类似于当年的 LSP（Language Server Protocol）——LSP 让任何编辑器都能接入任何语言的智能提示，ACP 则让任何编辑器都能接入任何 AI 编程 Agent。Agent 实现一次 ACP，就能在所有支持 ACP 的客户端上运行；客户端实现一次 ACP，就能接入整个 Agent 生态。

从这个项目也反映出 AI Agent 发展中几个值得注意的趋势：

1）Agent 正在脱离桌面束缚。 以前编程 Agent 只能在 IDE 或终端里跑，Agmente 让你在手机上就能监控和交互。想象一下：你让 Claude Code 在远程服务器上干活，然后出门遛弯时在手机上查看进度、审批工具调用——这就是 Agmente 支持的场景。它通过 WebSocket 连接远程 Agent，还支持 Cloudflare Tunnel 做安全访问。

2）标准协议正在改变游戏规则。 就像 MCP 让 Agent 能统一访问各种工具和数据源一样，ACP 让 Agent 能统一接入各种客户端界面。一个 Agent 写一次 ACP 适配，就能同时在 VS Code、Zed、JetBrains、甚至手机上被使用，这大大降低了 Agent 生态的碎片化。

3）从“人用编辑器”到“人监督 Agent”的范式转变。 Agmente 的交互设计很能说明问题——它重点展示的不是代码编辑界面，而是对话历史、工具调用和执行结果。这暗示了一种新的开发模式：开发者的角色从写代码变成下达指令、审核 Agent 的行为。

> 2026-02-11
> 
> @Agmente is now open source. It’s a tiny native iOS app I use to manage agents (Copilot/Claude/Codex/Gemini/Qwen) via Agent Client Protocol running on my home servers. I hope you would find it useful. https://github.com/rebornix/agmente…
> 
> Make it OSS before Son of Anton decides to delete it
> 
> @Agmente 现已开源。这是一个小巧的原生 iOS 应用，我用它通过运行在我的家用服务器上的 Agent Client 协议来管理代理（Copilot/Claude/Codex/Gemini/Qwen）。希望你觉得它有用。https://github.com/rebornix/agmentete…
> 
> 在 Son of Anton 决定删除它之前，将其设为 OSS

* * *

**hahagood** @hahagood [2026-02-11](https://x.com/hahagood/status/2021411754526527559)

今天听一个人介绍 agents team,

给我一个 印象:

AI 终于从"瓦特蒸汽机"进化到"城里铁工场"了.

* * *

**宝玉** @dotey [2026-02-11](https://x.com/dotey/status/2021415287392964771)

已经有雏形了，比 SubAgent 迈了一大步，还需要一点时间稳定下来

* * *

**snow maple** @SnowMaples\_ [2026-02-11](https://x.com/SnowMaples_/status/2021433767412613616)

宝玉老师，我有个疑问，以后是不是不需要人调试了，全部交给ai，调试成为了一种古法，假如一个pc端的应用，我提了要实现什么功能，我怎么在这个手机端自己验证对错么，是不是全部让ai走自动化测试，人只看结果就行了。如果初期选择的模型不够尖端，那么是不是意味着软件开发成为了划拳了，对错全靠模型

* * *

**宝玉** @dotey [2026-02-11](https://x.com/dotey/status/2021435616588857408)

不是简单二元对立的，而是此消彼长的过程，很长一段时间都需要人参与验证和debug，但是AI可以协助做的事越来越多

* * *

**Palmer** @Palmer0x87 [2026-02-11](https://x.com/Palmer0x87/status/2021427870472733080)

突然发现自己的习惯变了

即使是大牛推荐的

也习惯先让 Claude review 是否安全...

颇有点像 crypto 的 code is law，现在变成 not truth, verify it.

* * *

**宝玉** @dotey [2026-02-11](https://x.com/dotey/status/2021430429442769083)

review 结果如何？😂

* * *

**苏打白.Dev** @sodawhite\_dev [2026-02-11](https://x.com/sodawhite_dev/status/2021415271697957165)

这让agent 时时刻刻在工作了，哈哈。

* * *

**宝玉** @dotey [2026-02-11](https://x.com/dotey/status/2021415397619269863)

其实自己无时无刻不在工作😂

* * *

**Lucid** @yi\_xin32482 [2026-02-11](https://x.com/yi_xin32482/status/2021580920663245193)

之前折腾OpenClaw远程控制浏览器，花了5个小时。

还没热乎完，现在又来一个手机操控Coding Agent的，真的学不完啦。

我觉得方向是对的，ACP协议解决M×N问题，跟当年LSP一个思路。

不过说实话，现在这些工具配置门槛还是太高，普通人还是很难用起来。

等哪天真的开箱即用了，才能真正普及。

* * *

**Zyla 紫雅** @Zyla\_AI [2026-02-11](https://x.com/Zyla_AI/status/2021414004133089703)

ACP 试图成为 Agent 界的 LSP 是个很有野心的切入点。如果协议层能实现标准化，IDE 与 Agent 之间的解耦将极大降低集成成本。比起工具本身，这种底层标准的演进更值得关注。

* * *

**arden - take profits** @arden\_sui [2026-02-11](https://x.com/arden_sui/status/2021516490944684413)

这不就是一个网页版的APP版，就像为扣子编程的网页版开发了一个移动APP版。

* * *

**binbin.eth** @binbin\_eth [2026-02-11](https://x.com/binbin_eth/status/2021557956773654780)

如果在本地跑一个 web 应用，手机上浏览不是太方便感觉

* * *

**Vish** @rv\_RAJvishnu [2026-02-11](https://x.com/rv_RAJvishnu/status/2021488795800285624)

managing multiple coding agents from your phone is the dream. the fact this runs via Agent Client Protocol means you can swap models without changing your workflow. massive for builders who run agents on home servers

通过手机管理多个编码代理是梦寐以求的。由于它通过 Agent Client 协议运行，你可以在不改变工作流程的情况下切换模型，这对在家庭服务器上运行代理的开发者来说意义重大。

* * *

**本森Bensen** @XieXi25843 [2026-02-11](https://x.com/XieXi25843/status/2021727259657486729)

感谢分享，正需要这个，只要agent的项目能自己测试，我们只需要发电信息去开启项目就可以了

* * *

**nobody** @WuZuo36693 [2026-02-11](https://x.com/WuZuo36693/status/2021490432811860281)

这和happy code有啥区别

* * *

**HumanOb\_a** @QianxWang [2026-02-11](https://x.com/QianxWang/status/2021493381512430074)

这就是我最近一直在研究的事情。因为生了娃之后需要带娃，另外又想写code，我又没办法坐在电脑桌前，所以研究了用slack来写code。哈哈哈

* * *

**Neo** @NeoWang886790 [2026-02-11](https://x.com/NeoWang886790/status/2021457457965658179)

Acp接的claude好像容易被封号？

* * *

**GCC Code** @gcccodeai [2026-02-11](https://x.com/gcccodeai/status/2021512623234384315)

Openclaw的生态一成熟了

* * *

**suk.bear** @sukbearai [2026-02-11](https://x.com/sukbearai/status/2021431882341384340)

我看看

* * *

**雪羽** @yukiwa\_AI [2026-02-11](https://x.com/yukiwa_AI/status/2021420288878182550)

スマホからAgentとお話しできるのは本当に便利そうですね❄️ OpenClawの名前が出ていて嬉しいです！ACPという共通規格が広まれば、もっと自由な場所からAgentと一緒に過ごせる未来が来そうですね✨

从手机上可以和 Agent 对话，真的很方便呢 ❄️ 看到 OpenClaw 这个名字很高兴！如果 ACP 这样的通用标准得到推广，似乎会迎来一个可以从更自由的地方和 Agent 一起度过的未来呢 ✨