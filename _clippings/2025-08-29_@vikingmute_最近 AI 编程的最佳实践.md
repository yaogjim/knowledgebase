---
title: 最近 AI 编程的最佳实践
source: https://x.com/vikingmute/status/1960982879485485132
author:
  - "[[@vikingmute]]"
published: 2025-08-29
created: 2025-08-29
description:
tags:
  - "@vikingmute #AI编程 #AGNETS"
---
**Viking** @vikingmute [2025-08-28](https://x.com/vikingmute/status/1960982879485485132/history)

最近 AI 编程的最佳实践：使用 http://AGNETS.md 替换了之前的各种各样的指令文件，每家都有一个格式，维护起来非常麻烦。

如果有人不太熟悉 AGNETS md 可以去它的官网看看：

https://agents.md（这网址厉害，就是文件的名称）

由 OpenAI、Google 等组织的协作开发，是一个开放格式，得到广泛采用已有 2 万多个开源项目使用，就是一个标准的 Markdown 文件，兼容多个 AI 编码代理（如 OpenAI Codex、Cursor 等，现在12个工具支持），一个文件即可服务于不同工具，减少重复配置，官网里还有怎样写，最佳实践等等。

而且支持嵌套，离文件最近的文件会生效，替换以后就会非常清爽了，只不过 CLAUDE 还不支持，现在还需要单独创建一个文件。

注意替换的时候有个小技巧：

替换完毕以后可以用

"ln -s http://AGENTS.md http://AGENT.md" 创建一个链接，这样可以做到向后兼容。

![Image](https://pbs.twimg.com/media/GzbOcAHXAAEDUVu?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/GzbPazdXYAAfRJ3?format=jpg&name=large)

---

**waterwu** @watert [2025-08-28](https://x.com/watert/status/1960992313284436022)

第一个网址错别字了 🤣