---
title: "2025-12-31_hwchase17_真的很喜欢_opencode_的_agent_spec_来自_httpsopencode_ai"
source: "https://x.com/hwchase17/status/2003922408240304245"
author:
  - "[[@hwchase17]]"
published: 2025-12-31
created: 2025-12-31
description:
tags:
  - "#覆盖"
  - "x"
  - "@hwchase17"
  - "https"
---

# 真的很喜欢@opencode 的 agent spec，来自：httpsopencode.ai

**Harrison Chase** @hwchase17 [2025-12-24](https://x.com/hwchase17/status/2003922408240304245)

真的很喜欢@opencode 的 agent spec，来自：https://opencode.ai/docs/agents/

我喜欢的关键特性（据我所知，Claude Code 不支持这个，其他人也不支持）：能够将这里定义的代理用作主代理或子代理

cc 和其他人只允许你把代理用作子代理。如果我想把 cc 变成一个非常擅长编写 LangGraph 代码的代理，我不想要子代理，而是想要类似这样的东西

* * *

**Harrison Chase** @hwchase17 [2025-12-24](https://x.com/hwchase17/status/2003924165100032083)

@thdxr 你有没有想过在这里创建代理时不只是用 markdown 文件？用例是我想定义一个拥有自己技能、自己的 mcps 甚至自己子代理的代理

我能看到对这类事物的一些支持（例如 https://opencode.ai/docs/skills/#覆盖-每个代理...），但我认为让代理成为一个文件夹或者

* * *

**Glitchy** @Glitchymagic [2025-12-25](https://x.com/Glitchymagic/status/2004139646159303154)

关于主代理和子代理灵活性的观点很有意思。这种解锁的模块化对于复杂任务似乎很强大！很想看看嵌套代理架构下的性能基准测试！

* * *

**Creatify AI** @Creatify\_AI [2025-12-24](https://x.com/Creatify_AI/status/2003929908339527864)

能够在任何层级运行代理而无需重建是正确的设计

* * *

**Himanshu Kumar** @codewithimanshu [2025-12-26](https://x.com/codewithimanshu/status/2004474560754938015)

我发现 Opencode 的代理规范非常有用。我喜欢它。

* * *

**EJ Campbell** @ejc3 [2025-12-25](https://x.com/ejc3/status/2004073394120413307)

这就是技能的作用。加载 langgraph 技能。

* * *

**Anayat** @anayatkhan09 [2025-12-25](https://x.com/anayatkhan09/status/2004075811478139019)

以规范为输入在这里被低估了，但难点在于如何让那些高层级的流程与不断演进的代码和基础设施合约保持同步，这样 Copilot 就不会在几次重构中偏离架构。

* * *

**Esteban Puerta** @Esteban\_Puerta9 [2025-12-25](https://x.com/Esteban_Puerta9/status/2004044556048777238)

子代理架构是关键差异点。能够将代理用作主代理或子代理，解锁了线性框架无法触及的并行执行模式。

* * *

**Somi AI** @somi\_ai [2025-12-25](https://x.com/somi_ai/status/2004006255158055319)

主要的代理区分对于专业工作流来说是合理的。我们一直在运行特定领域的代理，在这些代理中，上下文工程比通用能力更重要。让代理规范定义在任何任务开始前加载哪些上下文，这是关键的突破口。

* * *

**Paras** @buildwithparas [2025-12-24](https://x.com/buildwithparas/status/2003923234874638749)

主代理与子代理的灵活性被低估了。大多数工具都迫使你采用一种模式，但实际工作流程需要两者兼具。

* * *

**Abhilash Mekala** @abhilashreddi [2025-12-25](https://x.com/abhilashreddi/status/2003992770298761529)

次级代理和主代理的区别被低估了。大多数工具都默认你总是从零开始统筹。

* * *

**Brian Cheung** @justBCheung [2025-12-25](https://x.com/justBCheung/status/2004223098711953774)

是的，能够定义一个自定义的主代理超级有用

* * *

**Brian Kelley** @capturedbybk [2025-12-26](https://x.com/capturedbybk/status/2004653782823837790)

Claude 的代码现在确实支持通过在 settings.json 文件中使用自定义代理定义来更改主代理配置文件，并且该代理仍然可以作为子代理使用。我认为这个版本是在以.74 结尾的版本中发布的，或者接近这个版本。

* * *

**Arun** @arunHere\_ [2025-12-25](https://x.com/arunHere_/status/2004182782373925136)

在 CC 中，一种替代方法是使用命令行选项：系统提示、权限等。

* * *

**permissionless\_logistics** @noreally567 [2025-12-25](https://x.com/noreally567/status/2004078183327604841)

还能使用计划模式吗？在 opencode 里

* * *

**Arti Yadav** @ArtiYadav158641 [2025-12-25](https://x.com/ArtiYadav158641/status/2004178154202775861)

很有趣的分享