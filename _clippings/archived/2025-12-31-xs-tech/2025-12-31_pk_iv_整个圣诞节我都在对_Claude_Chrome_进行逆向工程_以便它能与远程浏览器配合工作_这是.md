---
title: "2025-12-31_pk_iv_整个圣诞节我都在对_Claude_Chrome_进行逆向工程_以便它能与远程浏览器配合工作_这是"
source: "https://x.com/pk_iv/status/2005694082627297735"
author:
  - "[[@pk_iv]]"
published: 2025-12-31
created: 2025-12-31
description:
tags:
  - "x"
  - "@pk_iv"
  - "https"
  - "2025-12-29"
---

# 整个圣诞节我都在对 Claude Chrome 进行逆向工程，以便它能与远程浏览器配合工作。 这是

**Paul Klein IV** @pk\_iv [2025-12-29](https://x.com/pk_iv/status/2005694082627297735)

整个圣诞节我都在对 Claude Chrome 进行逆向工程，以便它能与远程浏览器配合工作。

这是 Anthropic 教 Claude 如何浏览网页的方法（1/7）

* * *

**Paul Klein IV** @pk\_iv [2025-12-29](https://x.com/pk_iv/status/2005694085320040898)

当你在 Chrome 中安装 Claude 时，它会在你的设备上创建一个原生消息宿主。

Claude Code 使用 --Chrome 原生主机 参数运行，并通过标准输入/标准输出与 Chrome 通信，使用二进制协议。

![Image](https://pbs.twimg.com/media/G9Wnp_nXsAAiRWP?format=jpg&name=large)

* * *

**Paul Klein IV** @pk\_iv [2025-12-29](https://x.com/pk_iv/status/2005694088038015106)

协议简单但巧妙：

4字节小端序长度前缀

JSON 有效载荷与 MCP 工具调用

像导航、截图、点击这类操作来回进行。

![Image](https://pbs.twimg.com/media/G9Wnt0HW4AAbc_X?format=jpg&name=large)

* * *

**Paul Klein IV** @pk\_iv [2025-12-29](https://x.com/pk_iv/status/2005694091015909569)

这个扩展是一个 MCP 服务器。Claude Code 作为 MCP 客户端连接。

19 个浏览器工具遵循 MCP 规范——所以它们都被命名为 mcp\_\_claude-in-chrome\_\_\*

![Image](https://pbs.twimg.com/media/G9WnxFOWMAAosTD?format=jpg&name=large)

* * *

**Paul Klein IV** @pk\_iv [2025-12-29](https://x.com/pk_iv/status/2005694093960307076)

问题是？只适用于本地 Chrome。

原生主机必须与浏览器在同一台机器上运行。Claude Code 期望生成一个本地进程。

那很危险。恶意网站可能会做提示注入来提取你的个人数据。

![Image](https://pbs.twimg.com/media/G9Wn0jQXkAAf5KJ?format=jpg&name=large)

* * *

**Paul Klein IV** @pk\_iv [2025-12-29](https://x.com/pk_iv/status/2005694096791523692)

所以我搭建了一个服务器，它能拦截浏览器的套接字并将命令转换为 CDP（Chrome 开发者工具协议）。

Claude 认为自己在和本地的 Chrome 对话。命令实际上运行在 Browserbase 的云浏览器上。

![Image](https://pbs.twimg.com/media/G9Wn3WTXwAAz5Qd?format=jpg&name=large)

* * *

**Paul Klein IV** @pk\_iv [2025-12-29](https://x.com/pk_iv/status/2005694099123478579)

想试试吗？打开 Claude Code 并安装插件。

/插件市场 添加 browserbase/claude-code-plugin

/plugin 安装 browserbase@browserbase-cloud

运行安装脚本，然后正常使用 Claude 代码。

浏览器命令上云

* * *

**Wayne Culbreth** @wayne\_culbreth [2025-12-29](https://x.com/wayne_culbreth/status/2005772447186874547)

跟 Claude 花了 20 分钟尝试用这个，最后放弃了。如果要成为 Browserbase 的一个途径，可能需要一些配置测试（我之前没听说过 Browserbase，直到看到这个）。不过我挺喜欢这个想法的。

* * *

**Paul Klein IV** @pk\_iv [2025-12-29](https://x.com/pk_iv/status/2005772730625392692)

很乐意帮忙！你遇到什么麻烦了？你运行安装脚本了吗？

* * *

**Nick Khami** @skeptrune [2025-12-29](https://x.com/skeptrune/status/2005767069632221548)

这个的整个用户体验惊人地流畅

* * *

**Paul Klein IV** @pk\_iv [2025-12-29](https://x.com/pk_iv/status/2005767583900000398)

🙏

* * *

**Nikunj Kothari** @nikunj [2025-12-29](https://x.com/nikunj/status/2005701763966607381)

谁让一个创始人有空闲时间做这种事了..这太厉害了，保罗 👏

* * *

**Paul Klein IV** @pk\_iv [2025-12-29](https://x.com/pk_iv/status/2005702001175535728)

顺便说一句，如果这还不明显的话：这条推文里的所有图片都是 nano banana pro 做的

* * *

**Erika** @brickywhat [2025-12-29](https://x.com/brickywhat/status/2005694466653552756)

这就是假期里会发生的事？？我们应该多来点这样的

* * *

**Paul Klein IV** @pk\_iv [2025-12-29](https://x.com/pk_iv/status/2005694746644340827)

超爱不开会！

* * *

**ari dutilh** @aridutilh [2025-12-29](https://x.com/aridutilh/status/2005694362798477796)

好的，这太酷了