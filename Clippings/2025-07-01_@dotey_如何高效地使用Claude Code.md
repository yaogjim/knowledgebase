---
title: "Claude Code的子任务机制"
source: "https://x.com/dotey/status/1935794151293083803"
author:
  - "[[@dotey]]"
created: 2025-07-01
description:
tags:
  - "@dotey #AI #编程 #大模型 #ClaudeCode #子任务"
---
**宝玉** @dotey 2025-06-06

我看到有人在让“Claude Code”自己开新进程 \`claude -p \`实现多任务，其实没必要，有更简单的办法。这个简单办法就是让它自己开子 Agent。Claude Code 现在有 18 个工具，最特殊的一个工具叫 Task，它本质就是一个 Claude Code 的克隆工具，只不过是作为 Claude Code 的一个工具。  
  
如果你懂递归的话就很好理解。如果你不懂递归，可以这么理解：Claude Code 是个 AI 程序员，它可以用一堆工具，其中最神奇的一个工具叫 Task，就是克隆一个自己的分身去干活！  
  
这样做有什么好处呢？就是可以并行多任务，还可以控制上下文，让子任务更专注。  
  
举例来说，你粘贴一段错误代码让 Claude Code 去 Debug，并且还让它写测试代码覆盖这个错误。Claude Code 会先调用 TodoWrite 这个工具写一个 TODO List。把任务分成 3 步：  
  
\- \[ \] 根据错误信息收集相关代码

\- \[ \] 根据错误信息和相关代码解决 Bug

\- \[ \] 写新的测试覆盖  
  
这一步完了后它会起一个 Task，这个 Task 就是专门根据错误信息去找到相关代码的位置，那么这个子任务只需要接受错误信息找上下文，它不管怎么解决 Bug，也不管怎么写测试覆盖。  
  
主任务就会等这个子任务完成，子任务完成后，主任务就调用 TODO Write 更新 TODO List。  
  
\- \[x\] 根据错误信息收集相关代码

\- \[ \] 根据错误信息和相关代码解决 Bug

\- \[ \] 写新的测试覆盖  
  
然后调用 TodoRead 工具看下一步要干嘛，现在有充足上下文了，它可以再起一个子任务去根据错误信息和代码修复 Bug，等修复 Bug 的子任务完成了，再回到主任务，继续更新 TODO List，继续读取下一个 Item  
  
最后再启动一个子任务去写测试，测试子任务也完成了，返回结果到主任务，这时候调用 TodoRead 一看任务都处理完了，最后根据前面的任务情况给你一个总结摘要，表示任务都完成了。  
  
Claude Code 真的没有做什么工程上的优化，什么上下文压缩、临时存储，都没有的！就是简单粗暴：

1\. 把用户问题、系统提示词、能用到的工具一股脑发给 Claude，问下一步该干嘛

2\. Claude 就返回说现在你要到 TodoWriter 工具

3\. Claude Code 就去调用 TodoWriter 工具，本质上也是一个 AI 请求，最后返回生成的 Todo List

4\. 然后 Claude Code 把工具返回结果和前面的所有消息继续发给 Claude，Claude 返回说你现在要去起一个新的 Task 去收集代码了

5\. 然后 Claude Code 就起一个新的 Task，把错误信息和要求收集相关代码的任务说明、系统提示词、环境说明、能用到的工具一股脑发给 Claude，问下一步该干嘛

\- 在新的 Task 里面，就是不停的问 Claude 该用啥工具，然后发送工具结果和前面所有历史消息

\- 任务完成后，返回任务结果

6\. 然后 Claude Code 把子 Task 的结果和前面历史信息一起发给 Claude 问下一步干嘛

7\. 就这样循环直到 Claude 认为任务完成了  
  
所以你经常看到 Claude Code 在那几十分钟上下文也没爆掉，因为它会启动子任务，这样上下文就分摊到子任务中了，主任务中只是保留子任务完成后的内容。

> 2025-06-06
> 
> 开个 Thread 来整理一些我使用 CluadeCode 的经验和心得，也欢迎留言分享。去年起我是 Cursor 的重度用户，最近一个月，我用 Cursor 越来越少了，开发方式也发生了变化，现在大部分时候都是：ClaudeCode 先做，做完了我去 IDE 去审查修改，所以不再需要 Cursor 的绝大部分功能，反而由于 Cursor
> 
> ![Image](https://pbs.twimg.com/media/Gt1LrTkWkAAINrA?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/Gt1OLcTXEAIP9Cp?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/Gt1O7j0WIAAf2kW?format=jpg&name=large)

---

**宝玉** @dotey [2025-06-19](https://x.com/dotey/status/1935794229994770624)

视频来源：

> 2025-06-19
> 
> Btw, since people don’t seem to know this, you can literally spawn subagents in Claude Code just by asking.  
> 顺便说一句，既然大家似乎都不知道，在 Claude Code 里，你只要开口要求，就能直接创建子智能体。

---

**宝玉** @dotey [2025-06-19](https://x.com/dotey/status/1935797021270483411)

配合他们自己写的 《构建高效 Agent \[译\]》更好理解

https://baoyu.io/translations/building-effective-agents…

![Image](https://pbs.twimg.com/media/Gt1U4_NWEAAIBu-?format=jpg&name=large)
