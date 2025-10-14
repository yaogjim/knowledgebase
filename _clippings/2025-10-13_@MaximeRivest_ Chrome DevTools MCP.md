---
title: " Chrome DevTools MCP"
source: "https://x.com/MaximeRivest/status/1977463062174060645"
author:
  - "[[@MaximeRivest]]"
published: 2025-10-13
created: 2025-10-13
description:
tags:
  - "@MaximeRivest # Chrome DevTools # MCP # Claude Code # Chrome浏览器 # 浏览器开发者控制台 # AI #  # 自动化 #"
---
**Maxime Rivest** @MaximeRivest [2025-10-12](https://x.com/MaximeRivest/status/1977463062174060645)

  
Chrome DevTools 是我迄今为止最喜欢的 mcp 服务器。

通过在终端中运行这两个命令，你就能让 Claude Code 在浏览器中全功能运行：

启动 Chrome 浏览器：

google-chrome --remote-debugging-port=9222 --user-data-dir="$HOME/.config/google-chrome"

安装连接浏览器的 MCP：

为 Claude 添加 Chrome 开发者工具 MCP：npx -y chrome-devtools-mcp@latest -u http://localhost:9222

![Split-screen screenshot displays two browser windows on a dark-themed interface. Left window shows a chat-like panel with text about using Chrome DevTools for Claude integration, listing steps like launching Chrome with remote debugging and installing MCP via npx command. Right window exhibits code output for adding chrome-devtools MCP, including URL connection to localhost:9222 and JSON-like protocol details for browser automation.](https://pbs.twimg.com/media/G3FcAcnWgAA6_qb?format=jpg&name=large)

---