---
title: "2026-01-08_vista8_Git_worktree工具_更好的控制AI_Agent并行_地址见评论区_目前自己都是开多个T"
source: "https://x.com/vista8/status/2008890723979100654"
author:
  - "[[@vista8]]"
published: 2026-01-08
created: 2026-01-08
description:
tags:
  - "x"
  - "@vista8"
  - "https"
  - "2026-01-07"
---

# Git worktree工具，更好的控制AI Agent并行。 地址见评论区。 目前自己都是开多个T

**向阳乔木** @vista8 [2026-01-07](https://x.com/vista8/status/2008890723979100654)

Git worktree工具，更好的控制AI Agent并行。

地址见评论区。

目前自己都是开多个Terminal Tab对话。

因为不是程序员，谁能讲讲Git worktree的使用场景和必要性？

![Image](https://pbs.twimg.com/media/G-EDJ-FbUAEMZuk?format=jpg&name=large)

* * *

**向阳乔木** @vista8 [2026-01-07](https://x.com/vista8/status/2008890763883753805)

工具地址

* * *

**wwwgoubuli** @wwwgoubuli [2026-01-07](https://x.com/wwwgoubuli/status/2008891745321550332)

以前的常用场景是，你开了一个新功能分支，正在那美滋滋地写代码。然后突然有一个补丁更新来了，你又不想放弃自己这边写的东西，就可以拉一个新的出来。大家共享的是同一套仓库信息，但是在物理上又实现了某种隔绝。

今天它能火起来，主要是大家发现可以充分的使用这个特性来实现同一个项目内的多路并行开发。

带来的问题就是相当严重的合并冲突，以及心智负担。

* * *

**Aranet Home** @aranet\_home

Radon exposure can build up over time without warning.

During Radon Action Month, learn what’s in your home with Aranet radon sensors.

氡暴露会随着时间毫无征兆地逐渐积累。

在氡气行动月期间，使用 Aranet 氡传感器了解你家中有什么。

* * *

**wwwgoubuli** @wwwgoubuli [2026-01-07](https://x.com/wwwgoubuli/status/2008892054420726058)

以前的常用场景是，你开了一个新功能分支，正在那美滋滋地写代码。然后突然有一个补丁更新来了，你又不想放弃自己这边写的东西，就可以拉一个新的出来。大家共享的是同一套仓库信息，但是在物理上又实现了某种隔绝。

今天它能火起来，主要是大家发现可以充分的使用这个特性来实现同一个项目内的多路并行开发。

带来的问题就是相当严重的合并冲突，以及心智负担。

* * *

**香蕉Banana** @treydtw [2026-01-07](https://x.com/treydtw/status/2008892089950679407)

我一般就是用来做产品的多模块开发，

比如一个登陆注册的模块开一个，

产品主逻辑开一个。

或者是多开不同的feature

* * *

**第九比特** @ninthbit\_ai [2026-01-08](https://x.com/ninthbit_ai/status/2009061512871334220)

其实开多个 terminal 如果是在不同分支也有一样的效果啊。如果是同一个分支就是很多人在线改同一个文件，如果是 worktree 就是把文件复制成了很多副本，每个人在这个副本上做修改，不会影响其他副本。

* * *

**yiplee** @yipleeyin [2026-01-08](https://x.com/yipleeyin/status/2009067666129211410)

worktree 就是把 codebase 复制一份然后切换到一个新分支但是共享 .git 信息，这样你就可以同时在多个分支修改代码了。