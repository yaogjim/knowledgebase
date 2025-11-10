---
title: "线性 Uncle  用 Claude 代码实现 chat2website  "
source: "https://x.com/LinearUncle/status/1975104961311646181"
author:
  - "[[@LinearUncle]]"
published: 2025-10-07
created: 2025-10-07
description:
tags:
  - "@LinearUncle #聊天机器人 #生成AI #Claude_Code"
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
**LinearUncle** @LinearUncle 2025-10-03

受到宝哥这个帖子的启发，我刚才花10分钟实验了下chat2website，当RAG用了。

1\. 使用claude code + chrome-devtools-mcp下载了一个webiste的部分文档到本地目录（请遵纪守法，切勿把别人站搞挂了，后果自负）

2\. 新开一个claude code，针对文档询问问题

3\. 准备打磨提示词，看看claude code能否根据本地这堆文档，快速实现相关功能（这个不知道宝哥 @dotey 能分享一些经验不）

最好是转成md格式文件，因为html中有很多无关内容，后续优化。

> 2025-10-03
> 
> 如果你想开发一个 Agent，无论你是打算做 CLI 还是做 Web 还是 Windows，都可以考虑使用 Claude Agent SDK，和 Claude Code 共享的底层代码，Claude Code 就是基于它之上加了个 CLI 的 UI，也就是说你完全可以基于它写一个 Claude Code 出来。
> 
> 我昨天帮朋友花了几个小时就实现了个简单的 x.com/claudeai/statu…
> 
> ![A terminal window displaying directory contents with filenames like quick-start.html, basic-implementation.html, and generic-authority-control.html. Text includes paths and file names in a black background with white text. An arrow points to a specific line mentioning generic-authority-control.html.](https://pbs.twimg.com/media/G2j56W3WsAAkS9G?format=jpg&name=large) ![A terminal window displaying directory contents with filenames like quick-start.html, basic-implementation.html, and generic-authority-control.html. Text includes paths and file names in a black background with white text. An arrow points to a specific line mentioning generic-authority-control.html.](https://pbs.twimg.com/media/G2j6MTzWUAAf2ft?format=jpg&name=large)

---

**宝玉** @dotey [2025-10-06](https://x.com/dotey/status/1975186903545827462)

没啥经验，干就完了

---

**SuperPig** @Jimmy\_superpig [2025-10-07](https://x.com/Jimmy_superpig/status/1975361260436005290)

上firecrawl，抓下来就是md

测试的时候，直接用他在线的免费api，用爽了再自建