---
title: "《AI Coding实践技巧：如何验证数据》"
source: "https://x.com/dotey/status/1979684614949007460"
author:
  - "[[@dotey]]"
published: 2025-10-20
created: 2025-10-20
description:
tags:
  - "@dotey #CodingAgent #Codex #实践技巧 #验证数据 #TDD"
status: "inbox"
importance: 2
effort: 2
review_level: 0
review_next: "2025-11-13"
review_interval: null
review_count: 0
decision: null
topics: []
links_out: []
summary: ""
pov: ""
actions: []
---
**宝玉** @dotey 2025-10-11

分享一点 AI Coding/Codex 实践技巧：告诉 AI 如何验证

这个方法其实我提到多次，只不过再随手贡献一个案例罢了。

Coding Agent 能力挺强的，能自己写代码自己调用工具，但是它有时候并不知道该如何验证数据。

如果说你只是告诉它哪里错了，它并不一定能通过阅读代码找出问题所在，但如果你告诉它如何验证，那么它就能在修改完后自行验证，验证时如果发现问题就会继续修复，直到完全修复为止。

比如我在调试一个 API 发现返回结果不对，那么我就告诉它输入是什么，实际输出是什么，期望结果是什么（甚至于我没说它也猜得到），然后让它自行写测试代码验证。

那么它就不仅阅读代码修改问题，还会写测试程序去验证，直到解决问题。

> 2025-10-11
> 
> 分享一点 Codex 实践经验：照葫芦画瓢法
> 
> 需求是这样的，我要重构一个基于 Claude Agent SDK 写的 Agent UI 的消息发送功能，让它能支持发送图片（当前只支持发送文本，图1）
> 
> 我不会说：帮我把输入框改造一下，支持图片上传🙅
> 
> 因为上下文信息太少，你这么说它肯定做不了。 x.com/dotey/status/1…
> 
> ![First image shows code snippets for handling message parsing in a file upload context, including functions for processing attachments, base64 conversion, and error handling in a Node.js environment. Second image displays a JavaScript function getProjectFiles that retrieves and filters project files without conflicts, including logic for reading directories, handling async operations, and returning file paths with content previews.](https://pbs.twimg.com/media/G3lAcZfXIAAYmOl?format=jpg&name=large) ![First image shows code snippets for handling message parsing in a file upload context, including functions for processing attachments, base64 conversion, and error handling in a Node.js environment. Second image displays a JavaScript function getProjectFiles that retrieves and filters project files without conflicts, including logic for reading directories, handling async operations, and returning file paths with content previews.](https://pbs.twimg.com/media/G3lAqEiXcAAIhgI?format=png&name=large) ![Image](https://pbs.twimg.com/media/G28nOYIW8AA2JwW?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G28o1zfWgAAVeKe?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G28qGz4WQAAIBJO?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G28qXvqWYAAUeCF?format=jpg&name=large)

---

**老鬼** @laogui [2025-10-19](https://x.com/laogui/status/1979728473993482318)

如果是开发网页应用，输入和输出现在用 google 自家的 devtool mcp 就可以搞定了，有奇效，经常说半天都说不明白，让它自己调浏览器看接口请求就搞定了。

---

**宝玉** @dotey [2025-10-19](https://x.com/dotey/status/1979729334584893901)

看场景，很多场景确实可以用 devtool mcp，但我这个如果用 mcp，无效上下文非常多，它很难准确拿到数据以及反复验证。devtool mcp 虽然强大，但是上下文消耗也是很大的。

---

**20xbrights** @eagle6616 [2025-10-19](https://x.com/eagle6616/status/1979831709568057599)

宝玉哥哥，有没有自动化测试API的MCP推荐

---

**JimmyJacy** @ljhspurs [2025-10-18](https://x.com/ljhspurs/status/1979689270739898505)

是的，coding agent更像有无限记忆能力的资深程序员，态度好，无怨无悔，只需让它更好地理解上下文和预期的结果，它会自我解决😁

---

**1** @single\_cluster [2025-10-19](https://x.com/single_cluster/status/1979939081242214824)

codex 是我试过很多个 ai 唯一一个能真正把我写的 bdd 正确实现的 ai，其他的要么直接 hardcode，要么直接 skip

---

**Dalin Huang** @DalinHuang [2025-10-19](https://x.com/DalinHuang/status/1979743967253287378)

是的，因为不提供真实运行日志和数据 AI就会猜测然后进入死循环🤣

---

**feiandxs** @feiandxs [2025-10-20](https://x.com/feiandxs/status/1980197915558822069)

其实都是最早的 prompt 技巧。

说清楚，讲人话。

---

**朽木愚夫** @davis926tw [2025-10-19](https://x.com/davis926tw/status/1979717577627824370)

確實是如此。之前都是寫測試案例(Testing Case)來完成驗證工作。AI 似乎大多數不會認為自己有錯

---

**Max** @hillsmao [2025-10-19](https://x.com/hillsmao/status/1979723738578133149)

@readwise save thread  
@readwise 保存对话

---

**Tom Cao** @tomcaokol35578 [2025-10-19](https://x.com/tomcaokol35578/status/1979839561523191831)

great！  
太好了！

---

**noon** @noon55950671 [2025-10-19](https://x.com/noon55950671/status/1979829168788664663)

看上去是 ts 项目，测试代码又是 Python

---

**ian** @Tsubame\_99 [2025-10-19](https://x.com/Tsubame_99/status/1979847081654440052)

多次使用下来的体验是让ai以TDD的模式进行开发会相对省事很多

---

**撸毛小狗T** @awesomeHunter\_z [2025-10-19](https://x.com/awesomeHunter_z/status/1979977609858728182)

比如说我写Telegram 机器人， 就让他注册个客户端， end to end,自己调试