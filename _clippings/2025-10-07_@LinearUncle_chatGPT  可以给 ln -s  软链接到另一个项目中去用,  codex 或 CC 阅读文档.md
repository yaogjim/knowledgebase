---
title: "chat2website chatGPT   以及  聊天机器人结合 "
source: "https://x.com/LinearUncle/status/1975424139516170473"
author:
  - "[[@LinearUncle]]"
published: 2025-10-07
created: 2025-10-07
description:
tags:
  - "@LinearUncle #chatGPT #chat2website #软链接 #codex #CC #自动化文档 #网页内容提取"
---
**LinearUncle** @LinearUncle 2025-10-06

这个方案实测非常管用：

1\. 使用ln -s将文档目录软链接到另外一个项目中，变成另外一个项目的子目录

2\. 然后从此就可以用codex或CC阅读文档，让其根据文档来实现需求了

3\. 也可以先在文档目录中，先用codex阅读文档，整理出来如何实现一个需求的详细步骤，然后再拷贝到另外一个项目中。我倾向方案2软链接的方式

> 2025-10-06
> 
> 受到宝哥这个帖子的启发，我刚才花10分钟实验了下chat2website，当RAG用了。
> 
> 1\. 使用claude code + chrome-devtools-mcp下载了一个webiste的部分文档到本地目录（请遵纪守法，切勿把别人站搞挂了，后果自负）
> 
> 2\. 新开一个claude code，针对文档询问问题
> 
> 3\. 准备打磨提示词，看看claude x.com/dotey/status/1…
> 
> ![Image](https://pbs.twimg.com/media/G2j56W3WsAAkS9G?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G2j6MTzWUAAf2ft?format=jpg&name=large)

---

**宝玉** @dotey [2025-10-07](https://x.com/dotey/status/1975440574472954207)

你看，我就说干就完了吧，跟 AI 结对做着做着就搞定了
