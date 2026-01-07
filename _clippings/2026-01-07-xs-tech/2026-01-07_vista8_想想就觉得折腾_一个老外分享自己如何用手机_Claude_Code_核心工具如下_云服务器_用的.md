---
title: "2026-01-07_vista8_想想就觉得折腾_一个老外分享自己如何用手机_Claude_Code_核心工具如下_云服务器_用的"
source: "https://x.com/vista8/status/2008161205085720738"
author:
  - "[[@vista8]]"
published: 2026-01-07
created: 2026-01-07
description:
tags:
  - "x"
  - "@vista8"
  - "https"
  - "2026-01-05"
---

# 想想就觉得折腾，一个老外分享自己如何用手机 Claude Code。 核心工具如下： 云服务器：用的

**向阳乔木** @vista8 [2026-01-05](https://x.com/vista8/status/2008161205085720738)

想想就觉得折腾，一个老外分享自己如何用手机 Claude Code。

核心工具如下：

云服务器：用的Vultr 的虚拟机，应该用来运行Claude吧。

Tailscale：把虚拟机接入私有网络。公网 IP 上不开 SSH 端口，所有访问都走 Tailscale 的加密隧道。

Termius + mosh：手机上的终端。mosh 是关键，它能在网络切换时保持连接。从 WiFi 切到 4G，或者手机息屏，连接都不会断。

tmux：会话持久化。关掉 Termius 几小时后再打开，所有窗口还在，Claude 还在跑。

Poke：推送通知服务。Claude 需要你输入时，手机就会震一下。

流程大概这样：

启动一个任务 → 把手机揣兜里 → 收到通知 → 掏出手机回复 → 继续干别的。

推送通知是给 Claude Code 的配置里加了个Hook

用 Git worktree 管理多个分支，分支名做哈希，算出一个确定的端口号，避免冲突。

\---

自己没那么强的需求，就不折腾了，转给需要的朋友。

原文地址见评论。

* * *

**向阳乔木** @vista8 [2026-01-05](https://x.com/vista8/status/2008161325281910998)

手机用Claude Code编程：

* * *

**魔都老猿** @AriXZone [2026-01-06](https://x.com/AriXZone/status/2008682449858093443)

我觉得，工作8小时把效率拉满就可以了。别把自己的时间给拉满。

* * *

**Jamf** @JamfSoftware

Upgrade fast or upgrade right? With Jamf, you get both.

Get the guide to navigate upgrade season with confidence.

快速升级还是正确升级？用 Jamf，你可以两者兼得。

获取指南，自信度过升级季。

* * *

**灰机** @yale\_hwang [2026-01-05](https://x.com/yale_hwang/status/2008182271422103796)

其它差不多 Poke 提醒可以学习下

* * *

**Hao ∞ 浩哥** @haocrypto101 [2026-01-05](https://x.com/haocrypto101/status/2008213256045842843)

用官方App呀。它自己提供了一个VPS. 手机上访问就可以开发。和电脑上本地命令行环境的区别在于它只能在一个branch 代码分支上开发，然后要合并到main，才能发布。还有一些对比看图。

![Image](https://pbs.twimg.com/media/G96bUAabsAAAvpy?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G96bUAcbIAAO8tt?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G96bUAaa0AAvcce?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G96bUAab0AAG_Vk?format=jpg&name=large)

* * *

**Vincent** @win1688888888 [2026-01-05](https://x.com/win1688888888/status/2008171358782709891)

Mosh 的最大硬伤是不支持服务端回滚，这在 Review AI 动辄几百行的代码输出时是灾难性的。建议用 Eternal Terminal (et) 替代 Mosh，它基于 TCP 实现但同样支持漫游和断线重连，最重要的是保留了完整的 Tmux 滚动缓冲区。至于通知，建议直接在 .zshrc 里用 http://ntfy.sh 的 curl 命令劫持

* * *

**elon lee** @elonlee123 [2026-01-06](https://x.com/elonlee123/status/2008363723199488253)

有点复杂了，试试happy的平替版hapi

* * *

**Ein Verne** @einverne [2026-01-06](https://x.com/einverne/status/2008366478974980214)

貌似 tailscale 加上 vibe kanban 两个就能完成呀 【Vibe Kanban 开发方式革新 AI Agent 并行协作-哔哩哔哩】

* * *

**青燃 (Qing Ran)** @toyHanli [2026-01-05](https://x.com/toyHanli/status/2008180163650179518)

Tailscale经常打洞失败，怎么办？

* * *

**Lan Liang** @lan31793328 [2026-01-06](https://x.com/lan31793328/status/2008453080304451596)

推荐happy

推荐快乐

* * *

**KeepMeReal** @keep\_real\_me [2026-01-05](https://x.com/keep_real_me/status/2008326583212270013)

感觉这个方案 对项目初始化的 Prompt 要求很高啊，不然一直用手机交互感觉也不是太方便

* * *

**Bito** @BitoHQ

10x faster production-ready code in Cursor and Claude with Bito’s AI Architect:

1\. System intelligence

2\. Services, APIs, dependencies

3\. Grounded code generation

4\. Production-ready output

在 Cursor 和 Claude 中，借助 Bito 的 AI 架构师，生成 10 倍更快的可生产代码：

系统智能

2\. 服务、API、依赖项

3\. 有根据的代码生成

4\. 可用于生产的输出

* * *

**123olp** @123olp [2026-01-05](https://x.com/123olp/status/2008295333236011054)

似乎交可以实现邮件收发通知和简单控制，移动端终端输入好麻烦

* * *

**HuZhou\_Mr** @HuZhou\_Mr [2026-01-05](https://x.com/HuZhou_Mr/status/2008161888304320716)

这是程序员也要24小时 on call 了么

* * *

**迈克尔** @MarkusAugustu3 [2026-01-06](https://x.com/MarkusAugustu3/status/2008355953310396556)

本末倒置，有大病。折腾工具本身。

* * *

**Tyler Chang** @Myccccccc [2026-01-06](https://x.com/Myccccccc/status/2008441696431059261)

不是有happy这个项目么

* * *

**AL** @AlickZheng157 [2026-01-05](https://x.com/AlickZheng157/status/2008181298289127664)

能不能用quest3+蓝牙键盘

* * *

**Sherell Laffin** @LaffinSher75362 [2026-01-05](https://x.com/LaffinSher75362/status/2008200264017490203)

1 🌐 💰 🌻 🌻 🧢

* * *

**Damian Gilliom** @DGilliom34314 [2026-01-05](https://x.com/DGilliom34314/status/2008207377594749406)

1 🌹 🎌 🌹 🍁 🌺

* * *

**Gertie Schau** @GertieScha9408 [2026-01-05](https://x.com/GertieScha9408/status/2008200320644743640)

1 🔥 🎌 🎉 🍀 🔥

* * *

**Kilo** @kilocode

Kilo offers a single agent that can explain, architect, plan, code, test, debug, review, and deploy.

Kilo 提供一个单一代理，能够解释、架构、规划、编码、测试、调试、评审和部署。