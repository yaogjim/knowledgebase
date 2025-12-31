---
title: "2025-12-31_jolestar_前一段时间我摸索出了一套_AI_coding_的工作流_之前这条推里提过_httpsx_com"
source: "https://x.com/jolestar/status/2005860894585282596"
author:
  - "[[@jolestar]]"
published: 2025-12-31
created: 2025-12-31
description:
tags:
  - "x"
  - "@jolestar"
  - "https"
  - "holon"
---

# 前一段时间我摸索出了一套 AI coding 的工作流（之前这条推里提过：httpsx.com

**jolestar** @jolestar 2025-12-22

前一段时间我摸索出了一套 AI coding 的工作流（之前这条推里提过：https://x.com/jolestar/status/2002918725125820839… ），

但在真正用的时候发现，并没有一个工具能非常完整地贴合这套流程，于是干脆自己顺手做了一个。

我的核心诉求其实很简单：

我已经把需求和方案写成了 issue，我希望一个工具能直接拿到这个 issue，把事情做完，然后给我一个 PR 让我 review。

如果我在 review 里提了 comment，希望它能再跑一遍，把问题修掉，并且逐条告诉我它是怎么修的。

于是就有了 holon。

用法也很直接：

holon solve github\_issue\_pr\_url

如果是一个 issue，它就直接解决并提交 PR；

如果是一个 PR，它就去修 review comments 或 CI 错误，然后再提交。

holon 也可以配置成 GitHub workflow，只要在 issue 或 PR 下面评论 holonbot，就会触发它去提交 PR，或者修已有的 PR。

整个 holon 工具本身，就是用这套流程写出来的。

我先写 issue，然后 holonbot 开发，开发完让 copilot review，review 的结果出来以后，再让 holonbot 修复，我只负责最后合并代码。

大概一周多的时间，合并了 200 多个 PR，close 了 150 多个 issue。

只有在 holon 把自己改坏的时候，才需要我亲自下场修。

大多数 PR 我其实不会细看代码，主要看的是 copilot 和 holonbot 在哪些地方产生了分歧，看看他们在争论什么点、为什么会争论这些点。

有时候我会补一两个 review comment，但也不是每次都会被接受，偶尔还会被 holonbot 直接驳回😅。

后来发现有一类 review comment，比如需要补测试、或者需要比较大的重构，其实不适合当下直接修，于是干脆让 holon 在这种情况下自动创建一个 issue，把问题记录下来，等未来再处理。

整体体验还是比较丝滑，项目在这里：

https://github.com/holon-run/holon

欢迎大家在自己的项目里试一试，有问题可以直接提 issue，让 holonbot 来修。

![Image](https://pbs.twimg.com/media/G9Y_X6ebYAA1HRa?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G9Y_hfVboAAhe6v?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G9Y_n3NaYAAIxRe?format=jpg&name=large)

> 2025-12-22
> 
> 最近摸索出来了一套 AI Coding 工作流。
> 
> 首先开一个 Agent 窗口，这个 Agent 的角色是产品经理或者架构师，负责和我聊需求与架构设计，拆分任务，最后转换成可执行的需求说明，直接写到 github issue。如果功能比较复杂，就拆分成多个子 issue。注意，这个 Agent

* * *

**working to earn** @coder\_yyyyy [2025-12-30](https://x.com/coder_yyyyy/status/2005948065576804419)

我试试

* * *

**Jay | Web3 Insights** @JayNam2878 [2025-12-30](https://x.com/JayNam2878/status/2006085880021238015)

Creating an Agent window for task breakdown is smart. It simplifies turning needs into actionable GitHub issues.