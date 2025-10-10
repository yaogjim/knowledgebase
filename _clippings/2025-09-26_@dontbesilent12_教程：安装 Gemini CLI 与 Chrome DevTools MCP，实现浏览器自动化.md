---
title: "don神动手能力真强，貌似不管什么AI工具，都能使用地游刃有余。"
source: "https://x.com/dontbesilent12/status/1971139321152598417"
author:
  - "[[@dontbesilent12]]"
published: 2025-09-26
created: 2025-09-26
description:
tags:
  - "@dontbesilent12 #AI工具 #GeminiCLI #ChromeDevToolsMCP #浏览器自动化 #数据提取"
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
**dontbesilent** @dontbesilent12 [2025-09-25](https://x.com/dontbesilent12/status/1971139321152598417)

《如何解决 agent 无法提取小红书标题的问题》

我之前发过一个推文，说现在客户端 AI agent 有两类，一个是浏览器里面的（比如 comet），一个是命令行里面的（比如 cc 或者 gemini cli）

二者获取的数据不同，如果要得到本地电脑里面的数据，就用命令行里面的 cc/gemini cli，如果要获取浏览器里面的数据，就用 AI 浏览器

其中一个案例是，比如我要批量提取某个博主的短视频标题，cc/gemini cli 就拿不到数据，comet 可以拿到

但是有个问题没解决，就是比如小红书这种页面是用 DOM 动态加载的内容，即便是 comet 也搞不到自身浏览器里面的数据

前两天谷歌发布了 Chrome DevTools MCP，把 gemini cli 和 chrome 浏览器打通了，这个问题被解决了，现在通过命令行里面的 gemini cli，就可以爬取小红书 DOM 结构里面的数据

![A screenshot of a social media post on Xiaohongshu with a profile picture showing a tower, text in Chinese and English about AI agents and data extraction, and three rectangular cards with text overlays. The profile picture includes a circular image of a tower, and the cards display text in Chinese, including phrases like ](https://pbs.twimg.com/media/G1rkfIxaAAQZWY1?format=jpg&name=large) ![A screenshot of a social media post on Xiaohongshu with a profile picture showing a tower, text in Chinese and English about AI agents and data extraction, and three rectangular cards with text overlays. The profile picture includes a circular image of a tower, and the cards display text in Chinese, including phrases like ](https://pbs.twimg.com/media/G1rkjuUaAAQTALd?format=jpg&name=large)

---

**dontbesilent** @dontbesilent12 [2025-09-25](https://x.com/dontbesilent12/status/1971141321919430984)

教程：安装 Gemini CLI 与 Chrome DevTools MCP，实现浏览器自动化

https://j8v8p5qtm3.feishu.cn/wiki/Ut7Vwo9N7ihGCOkhNhucwcLanMf?from=from\_copylink…

---

**LinearUncle** @LinearUncle [2025-09-25](https://x.com/LinearUncle/status/1971141835621007747)

don神动手能力真强，貌似不管什么AI工具，都能使用地游刃有余。

真正的AI commander.

---

**dontbesilent** @dontbesilent12 [2025-09-25](https://x.com/dontbesilent12/status/1971143241954427146)

wrap 里面有 agent，用中文交互就行了呗，都让它去安装

---

**warmshao** @warmshao [2025-09-26](https://x.com/warmshao/status/1971367016239079675)

可以试试开源的browser assistant：VibeSurf，本质也是cdp连接浏览器做agent自动化操作，爬各种网站不在不在话下

---

**TOMATOMA** @Tttx967715T [2025-09-25](https://x.com/Tttx967715T/status/1971244950148067417)

跟着dont哥学ai😍

---

**Ken** @Ken\_shafa [2025-09-25](https://x.com/Ken_shafa/status/1971148544515187120)

我这里有app端数据接口😄