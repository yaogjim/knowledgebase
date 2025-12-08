---
title: "2025-11-13_dotey_艹_看到最后没绷住喷了_作者看完_Anthropic_那篇_用_MCP_执行代码_的文章时_灵光一"
source: "https://x.com/dotey/status/1988455101447471308"
author:
  - "[[@dotey]]"
published: 2025-11-13
created: 2025-11-13
description:
tags:
  - "x"
  - "@dotey"
  - "https"
  - "2025-11-12"
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

# 艹，看到最后没绷住喷了 作者看完 Anthropic 那篇“用 MCP 执行代码”的文章时，“灵光一

**宝玉** @dotey 2025-11-10

艹，看到最后没绷住喷了

作者看完 Anthropic 那篇“用 MCP 执行代码”的文章时，“灵光一现”把 MCP 都扔到子 Agent，这样就不占用主 Agent 的上下文窗口。

放到 SubAgent 后果然不会污染主上下文了，但处理这么大量的 MCP 服务器工具，仍然很消耗 Token，很快就达到了 Claude 的使用上限。

所以，作者把那部分处理 MCP 的工作，转移给了…… “gemini-cli”

> 2025-11-10
> 
> solution to use MCP servers without context bloat:
> 
> when I finished reading Anthropic’s “Code execution with MCP” article, a sudden idea flashed in my mind...
> 
> as many people may already know, subagents have their own context windows, while using MCP as it currently does will
> 
> 使用 MCP 服务器而避免上下文膨胀的解决方案：
> 
> 读完 Anthropic 那篇《基于 MCP 的代码执行》文章后，我脑海中突然闪过一个念头……
> 
> 正如许多人可能已经了解的那样，子代理拥有各自的上下文窗口，而目前使用 MCP 的方式则会
> 
> ![Image](https://pbs.twimg.com/media/G5XMz0KaIAAuShn?format=jpg&name=large)

* * *

**Jintao Zhang 张晋涛** @zhangjintao9020 [2025-11-12](https://x.com/zhangjintao9020/status/1988484904238411909)

我一直是把 gemini cli作为一个 sub-agent 给 @warpdotdev 用的， 用来补全它的网络/搜索能力 🤣 （不过最近据说 Warp 也会加上这部分功能，还没试

> 2025-09-03
> 
> To be honest, I don’t have a MCP that I actually use on a daily basis.
> 
> But from the perspective of scalability, I put Gemini CLI in @warpdotdev as a sub-agent, specifically for it to search and access URLs. It works just like a MCP server. 🤣
> 
> 说实话，我并没有一个真正日常使用的 MCP。
> 
> 但从可扩展性的角度考虑，我将 Gemini CLI 作为子代理部署在 @warpdotdev 中，专门用于搜索和访问 URL。它的工作方式就像 MCP 服务器一样。 🤣

* * *

**灰机** @yale\_hwang [2025-11-12](https://x.com/yale_hwang/status/1988601804066836982)

差不多啊，我基本都是在 subagent 里面写 code 。下午在想是不是搞个 subagent 用 GLM 写简单的 code 。

* * *

**Bhe hontyu** @hitsmaxft [2025-11-12](https://x.com/hitsmaxft/status/1988620680045252868)

又是一个典型的资源分配问题. 不断把价值不高的工作交给低一级的模型, 但是, 它们可能给出错误的反馈. 又需要进一步验证. 反反复复, 最后还是需要一个裁判介入.

* * *

**今日は風が騒がしいな** @noisykaze [2025-11-12](https://x.com/noisykaze/status/1988465527938052467)

嘿嘿嘿，gemini-cli本质也是一个sub agent，他这就相当于把Claude转到Gemini来分担token压力了🌝

* * *

**Sam Song** @SamSongAI [2025-11-13](https://x.com/SamSongAI/status/1988768100389404894)

geminicli确实适合干这种脏活累活。我连聚类分析都让他干然后再给到Claude

* * *

**Justdoit** @DogeJustdoit [2025-11-12](https://x.com/DogeJustdoit/status/1988472985020416399)

没有人谈论GitHub copilot吗，copiot内置就支持选择其他模型调用mcp，所以copilot一次可以用几百个mcp工具

* * *

**你的伊芙琳** @lover\_reze [2025-11-12](https://x.com/lover_reze/status/1988475089810321846)

还真别说，gemini 除了指令跟随需要专门调教、没 claude 方便，context window 那是真滴长啊