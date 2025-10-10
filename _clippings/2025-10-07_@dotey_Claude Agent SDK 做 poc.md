---
title: Claude Agent SDK 做 poc
source: https://x.com/dotey/status/1973937260220330005
author:
  - "[[@dotey]]"
published: 2025-10-07
created: 2025-10-07
description: 
tags:
  - "@dotey"
  - 提取带
  - "#"
  - 的中文标签
status: "inbox"
importance: 2
effort: 2
review_level: 0
review_next: "2025-10-17"
review_interval: null
review_count: 0
decision: null
topics: []
links_out: []
summary: ""
pov: ""
actions: []
---
**宝玉** @dotey 2025-09-29

如果你想开发一个 Agent，无论你是打算做 CLI 还是做 Web 还是 Windows，都可以考虑使用 Claude Agent SDK，和 Claude Code 共享的底层代码，Claude Code 就是基于它之上加了个 CLI 的 UI，也就是说你完全可以基于它写一个 Claude Code 出来。

我昨天帮朋友花了几个小时就实现了个简单的 Agent，实现了输入提示词，就可以基于某个没训练的 Design System 写一套 UI 出来。

他写的这个 Agent 原理很简单，就是把这套设计系统的所有 Markdown 文档（几百个）放到一个它可以访问的目录，然后在 Systme Prompt 里面引导它去检索这个文档目录。

当用户输入提示词或者 Screenshot 要做一个 UI，Agent 就根据提示词规划可能要用到的组件，然后用 SDK 自带的 GREP 工具去检索文档库找到这些组件的 API，最后基于收集到的信息用这个 Design System 组件生成页面。

这个 SDK API 很简单，但很强大，你不止是可以用它内置的工具（Task、Grep、WebFetch 等等），你还可以添加自己的工具，还可以用 MCP。并且它可以把整个交互的结果通过 API 让你可以获取到原始的请求和返回消息，这样你可以自己实现一套比 CLI 更好用的交互 UI。

当然这个局限也有：

1\. 只能用 Claude 模型兼容的 API，如果你想用 GPT-5 之类模型，估计效果不会太好

2\. 只支持 Python 和 TypeScript

3\. Tokens 消耗飞快

如果你只是做前期的 POC，强烈建议你试试。

> 2025-09-29
> 
> The Claude Agent SDK gives you access to the same core tools, context management systems, and permissions frameworks that power Claude Code.
> 
> Read how devs are building agents with the SDK:
> 
> https://anthropic.com/engineering/building-agents-with-the-claude-agent-sdk…  
> Claude Agent 软件开发工具包使您能够使用与 Claude 法典相同的核心工具、上下文管理系统和权限框架。
> 
> 阅读开发者如何使用软件开发工具包构建智能体：
> 
> https://anthropic.com/engineering/building-agents-with-the-claude-agent-sdk…

---

**宝玉** @dotey [2025-10-03](https://x.com/dotey/status/1973953633629974613)

它和 OpenAI 的 Agent SDK 不一样的地方在于 Claude Agent SDK 这个是开箱即用，内置了 Claude Code 的所有工具，包括子智能体、Slask Command、MCP 支持，OpenAI 的只是开发框架，你还要自己写一堆工具

> 2025-10-03
> 
> OpenAI也有个Agent SDK  
> OpenAI 也有个 Agent SDK

---

**宝玉** @dotey [2025-10-03](https://x.com/dotey/status/1973953891357372911)

OpenAI 的 SDK 地址：

JS 版：https://github.com/openai/openai-agents-js…

Python版：

> 2025-10-03
> 
> https://openai.github.io/openai-agents-python/…

---

**宝玉** @dotey [2025-10-03](https://x.com/dotey/status/1973954612920266876)

Vercel 的 AISDK 也跟 OpenAI 的 Agent SDK 一样，你从头搭一个是可以的，也很轻量，API 设计很好（我很喜欢），但是做不到像 Claude Agent SDK 这样直接内置了各种实用工具（Task、Edit、Read、TodoWrite、Grep 等等），何况是被 Claude Code 验证过的！

> 2025-10-03
> 
> @aisdk Vercel ai agent sdk, please! x.com/dotey/status/1…  
> @aisdk 请给我 Vercel 人工智能代理软件开发工具包！x.com/dotey/status/1…

---

**宝玉** @dotey [2025-10-05](https://x.com/dotey/status/1974634520206065883)

如果你只是 POC 或者原型，我不推荐 Gemini cli，因为目前 Gemini 2.5 Pro 的 Agentic 能力不足，效果并不好，还是得 GPT-5/GPT-Code-5 或者 Claude 4.x 效果 才好，如果你是基于它代码魔改，那应该没问题，但是开发工作量比较大

> 2025-10-05
> 
> 我现在正尝试基于 Gemini CLI 开发，请教下你觉得怎么样

---

**宝玉** @dotey [2025-10-05](https://x.com/dotey/status/1974665530503315732)

我推荐 claude agent sdk 是因为它内置了 Claude Code 用的所有工具，基本上可以完成绝大部分普通 Agent 的事情，只需要根据写新的提示词或者增加少量工具即可完成一个原型

> 2025-10-05
> 
> 我用 Agent 的场景是没有涉及命令行工具，这一块的支持还未上手使用过。不过 ADK 支持对接 Langchain 生态的现成 tools，粗看了一下有个 Shell (bash) tool：https://python.langchain.com/docs/integrations/tools/bash/…  
> 我用 Agent 的场景是没有涉及命令行工具，这一块的支持还未上手使用过。不过 ADK 支持对接 Langchain 生态的现成 tools，粗看了一下有个 Shell (bash) tool：https://python.langchain.com/docs/integrations/tools/bash/…
> 
> 我使用 Agent 的场景并不涉及命令行工具，我还没有开始使用这方面的支持。不过，ADK 支持连接到 Langchain 生态系统中的现成工具，粗略看了一下，有一个 Shell (bash) 工具：https://python.langchain.com/docs/integrations/tools/bash/…

---

**宝玉** @dotey [2025-10-05](https://x.com/dotey/status/1974665641153253887)

这是为 Agent 写提示词的方法

> 2025-10-05
> 
> 如何编写 prompt 才能让大模型更好地理解工具？
> 
> 这个问题的答案很简单：让模型来写 Prompt，让模型给你反馈。
> 
> 举个案例，我上个帖子说到帮朋友做一个他们设计系统的 Coding Agent，初始提示词的产生是这样的：
> 
> 1\. 先让 Claude Code，去基于设计系统（Design System）做一个 Login x.com/thatcoolwall/s…

---

**Jiaju LIN** @JiajuAgency [2025-10-07](https://x.com/JiajuAgency/status/1975430365704822840)

After admitting Claude Code is built on that SDK , Bro spent hours to design an agent again for a task which Claude Code can definitely do. how about using Claude Code to design your UI ?  
在承认 Claude 法典基于该软件开发工具包构建之后，布罗又花了几个小时为一项 Claude 法典肯定能完成的任务重新设计一个智能体。用 Claude 法典来设计你的用户界面怎么样？

---

**宝玉** @dotey [2025-10-07](https://x.com/dotey/status/1975445974303539635)

Because this agent is specifically designed to generate UI code based on an internal Design System. While Claude Code \*can\* technically do the same thing, there are several reasons for building a dedicated agent:

1\. Ease of use

\- Getting Claude Code to generate UI based on an  
因为这个智能体是专门设计用于基于内部设计系统生成用户界面代码的。虽然从技术上讲 Claude 法典也能做同样的事情，但构建一个专用智能体有几个原因：

易于使用

\- 让 Claude 法典基于某个（内容）生成用户界面

---

**thechaos** @Noreasonsu [2025-10-03](https://x.com/Noreasonsu/status/1974059654927044697)

尝试了下 。 请问对于startup 做production生产， 成本如何控制？ 现在每个可能的task基本都花费0.5million token以上

---

**宝玉** @dotey [2025-10-03](https://x.com/dotey/status/1974116677735625005)

用国产模型替代试试

---

**小钟同学** @Zhongjiafe74922 [2025-10-03](https://x.com/Zhongjiafe74922/status/1974086763493929234)

这个sdk能用来做RAG吗？上下文管理这么好用，但第一眼看到grep，是我们认为的那个grep吗？

---

**宝玉** @dotey [2025-10-03](https://x.com/dotey/status/1974116411422515486)

不做rag，只用grep做关键词检索

---

**LinearUncle** @LinearUncle [2025-10-03](https://x.com/LinearUncle/status/1974098918448447531)

你这个case看起来就像是一个lovable呀

---

**宝玉** @dotey [2025-10-03](https://x.com/dotey/status/1974116057540669867)

差得远

---

**Menschheit@claudebuddy.fun** @oops073111 [2025-10-05](https://x.com/oops073111/status/1974639429978644680)

老师，可以用它来搭配playwrite 来实现一些场景的自动化吗？ 比如自动筛选简历？

---

**宝玉** @dotey [2025-10-05](https://x.com/dotey/status/1974639806845173812)

完全没问题，读简历 playwright 都不需要，claude code 能直接读取pdf

---

**小姜** @jiangbingd [2025-10-03](https://x.com/jiangbingd/status/1973954067874619602)

使用LangGraph开发Agent更合适吧

---

**宝玉** @dotey [2025-10-03](https://x.com/dotey/status/1973954799994572942)

我想不到使用它的理由……

---

**STRRL.gpt** @strrlthedev [2025-10-03](https://x.com/strrlthedev/status/1973938952529965464)

我们最近也在用类似的事情, 不过我们的更简陋用的一个 bash 脚本写的 loop, 一些预制好的 xxx\_prompt.txt, 还有 gemini cli headless mode(

挺顺利的, 直到我们想 open the box 看看到底发生了什么...

> 2025-10-01
> 
> 最近要用到 headless 的 claude code / gemini 做点事情
> 
> 结果发现这部分的 observability 根本没人在意啊... 🥹

---

**xincmm** @xincmm [2025-10-03](https://x.com/xincmm/status/1973937844692623785)

的确，但我想用 GLM Coding Plan 来完成编码外的任务，成本应该还好

> 2025-10-02
> 
> 如果是我，我会用 Claude Agent SDK 来搭建个人的通用AI 助手，主要是手机端操作，没有具体的想法，但我认为潜力巨大

---

**axtrur** @axtrur [2025-10-03](https://x.com/axtrur/status/1973951366826721382)

哈哈我司内的项目就是这么干的，所有物料相关文档放到一个docs目录下，claude code sdk去找，不过就是grep慢了点token大了点，其他的没啥毛病，甚至有些case比用rag效果更好

---

**Thinking Garden** @chenqing663 [2025-10-03](https://x.com/chenqing663/status/1974054605358260324)

这些额外的能力是Claude code cli本身 提供的，所以强依赖 Claude code cli 要安装。

---

**Jeffery Kaneda　金田達也** @JefferyTatsuya [2025-10-03](https://x.com/JefferyTatsuya/status/1973966155019923536)

GBase就是把CC集成到团队的文档、云盘、会议里。回头邀请你来使用一下。

---

**XiaoPeng** @PenngXiao [2025-10-03](https://x.com/PenngXiao/status/1973975409328074767)

有没有方法可以让它使用CC的token？

---

**Yangyi** @Yangyixxxx [2025-10-03](https://x.com/Yangyixxxx/status/1973944827042775520)

我也在写 可惜早上挂了……

---

**Vaayne** @LiuVaayne [2025-10-03](https://x.com/LiuVaayne/status/1973962503903384055)

Cherry Studio 的 Agent 就是基于 Claude Agent SDK 做的 

> 2025-09-29
> 
> Cherry Studio Agent 内测版本终于上线了！
> 
> \- 3周时间，496 次 Commits
> 
> \- 支持 Anthropic 官方 API 以及任何兼容 Anthropic API 的模型
> 
> \- Claude Code 作为 Agent Core， Cherry Studio 提供 GUI
> 
> \- 支持所有内置工具，支持通过 MCP 扩展工具
> 
> \- 我们将 Claude Code 作为通用 Agent，而不只是 Code
> 
> ![Image](https://pbs.twimg.com/media/G2AaP0ta8AAbnWO?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G2AaRAibUAAaZDz?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G2AaR2Ta0AAgKgy?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G2AaminaAAAfbI-?format=jpg&name=large)

---

**Art Lab** @daemonzhang6 [2025-10-03](https://x.com/daemonzhang6/status/1973952445211685229)

All in openAI, 不考虑别的技术了。openAI-NVDA-Oracle三家互相换股票。这是在往曼哈顿计划走。

Antr-Amzon是一起的。team 2。

---

**ailands19** @ailands19 [2025-10-06](https://x.com/ailands19/status/1975228357848744134)

@grok 请仔细阅读这篇推文及其引用的原文，深入思考这个方案有哪些优势和不足，然后仔细讲讲

---

**仓里 · 忙割** @kylesean6 [2025-10-03](https://x.com/kylesean6/status/1973944225596387484)

OpenAI也有个Agent SDK 

---

**SuperPig** @Jimmy\_superpig [2025-10-03](https://x.com/Jimmy_superpig/status/1974099818801963166)

以后知识库类的应用，用这个来做基本开箱即用吧？就是响应速度有点慢

---

**Mr. Nawk** @NawkUiy [2025-10-03](https://x.com/NawkUiy/status/1974057650154582110)

這個SDK 背後也是直接調Claude code CLI, 不寫python/typescript的也可以直接調用cli -p

---

**一箱抽纸** @orangeburncgw [2025-10-06](https://x.com/orangeburncgw/status/1975190004344439007)

其实可以做各种语言、文字类的套壳，不仅限于cli

---

**lessismore** @snwkng50462474 [2025-10-03](https://x.com/snwkng50462474/status/1973994908223746328)

不是说只增加了一个 type 文件么？我还没实践～

---

**No More Robots** @nomorerobotshq

I'm Alex Horne and I'm in a new video game, EARTH MUST DIE! Wishlist on Steam now!