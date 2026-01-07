---
title: "2025-12-30_LotusDecoder_朴素_1_claude_code_里_mcp_只有_context7_和_一个智谱识图_识图的原"
source: "https://x.com/LotusDecoder/status/2005512931790979514"
author:
  - "[[@LotusDecoder]]"
published: 2025-12-30
created: 2025-12-30
description:
tags:
  - "x"
  - "@LotusDecoder"
  - "mcp"
  - "2025-12-29"
---

# 朴素+1。 claude code 里 mcp 只有 context7 和 一个智谱识图。 识图的原

**LotusDecoder** @LotusDecoder 2025-12-29

朴素+1。

claude code 里 mcp 只有 context7 和 一个智谱识图。

识图的原因是，让 claude 读图的话，上下文很快爆炸，变成聊几句自己在 auto-compact。 用上 识图 mcp 读取文本描述就好多了。

plan 模式，安装了一个plugin，claude 官方的 /feature-dev ，用来做规划也很顺手。

skills 也只有两个，自己手搓的python 脚本形式的知心伙伴前置chatbot，Gpt-5.2的 web search，这些都不用别人的mcp或是插件。主打一个自主可控。

> 2025-12-29
> 
> 我的配置也很少, 简单分享一下
> 
> 1\. MCP 只有 context 7 , 仅仅就软件开发这个环节, MCP 似乎并没有我想象中的那么好用, 反而直接吼一句让AI 写好脚本直接显式调用幺蛾子更少 (比如 notion mcp 至今不支持本地md文件一次调用塞到某个database中, 让AI自己拆解任务反而容易出错, 写个脚本反而很快很稳) x.com/tcdwww/status/…

* * *

**kyson** @kingyu26373 [2025-12-29](https://x.com/kingyu26373/status/2005519935657882011)

这就装一个glm识图，那如果要识别图片的话，他会自动切换智谱吗，还是需要手动更换model

* * *

**LotusDecoder** @LotusDecoder [2025-12-29](https://x.com/LotusDecoder/status/2005520443642692062)

不会，要显示调用 mcp 智谱识图。

mcp 和 model 相比，是另外一种概念。

* * *

**BornCoder** @3svSWwc9uBnwiD5 [2025-12-29](https://x.com/3svSWwc9uBnwiD5/status/2005545839507407244)

有用server-memory之类的mcp么？

* * *

**LotusDecoder** @LotusDecoder [2025-12-29](https://x.com/LotusDecoder/status/2005546590845690195)

都还没上。

grep

和

手工指定读取 @ 2025-12-29-\*\*\*\*\*.md

暂时实现memory

* * *

**Hootsuite** @hootsuite

Uncover customer insights, track performance, and boost engagement—all in one platform. Hootsuite makes it easy from day one.

发现客户洞察，追踪表现，提升互动——一站式平台。Hootsuite 从第一天起就让这一切变得简单。