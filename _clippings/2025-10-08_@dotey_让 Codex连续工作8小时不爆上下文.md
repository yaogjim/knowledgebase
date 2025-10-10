---
title: "让 Codex连续工作8小时不爆上下文"
source: "https://x.com/Stephen4171127/status/1972347005931590095"
author:
  - "[[@dotey]]"
published: 2025-10-08
created: 2025-10-08
description:
tags:
  - "@dotey #别问我在做什么 #AI #开发 #工具 #Agent"
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
**宝玉** @dotey [2025-09-28](https://x.com/dotey/status/1972200355506135165)

卧槽，我真解决了让 Codex 连续工作 8 小时的问题，上下文都不会爆掉！

方案就是让 Claude Code 去当监工监督 Codex 干活，大概的步骤如下：

1\. 首先要让 Codex 生成一个任务的 TODO List，就是那种能一步步完成的

2\. 然后让 Codex 更新 Agents md 文件，加上说明，如果输入 continue，要读取 TODO

![A screenshot of a code editor displaying text in a dark-themed interface. The text includes a file named AGENTS.md with lines of code and comments, showing a task list and instructions for automating tasks with Codex and Claude Code. A watermark from Xiaohongshu is visible in the top-right corner.](https://pbs.twimg.com/media/G16ny3rXQAAIruT?format=jpg&name=large) ![A screenshot of a code editor displaying text in a dark-themed interface. The text includes a file named AGENTS.md with lines of code and comments, showing a task list and instructions for automating tasks with Codex and Claude Code. A watermark from Xiaohongshu is visible in the top-right corner.](https://pbs.twimg.com/media/G16oaKPWsAAON4Y?format=png&name=large)

---

**宝玉** @dotey [2025-09-28](https://x.com/dotey/status/1972201961404747780)

另外也没办法真的 8 小时，Claude Code 会偷懒，执行一会就会自行中断，即使没用多少上下文，暂时还没解决这个问题，但是思路可以借鉴一下，如果有更好办法，欢迎留言交流。

---

**宝玉** @dotey [2025-09-28](https://x.com/dotey/status/1972206026112840182)

这个思路可以用在 Claude Code 上，把里面的 Codex 换成 Claude Code 就行，本质上就是一个 Manager 监控 Worker 干活。

要点：

1\. Worker 要有 TODO List，并且 Agents/Claude Code MD 要有引导，这样每次固定提示词（continue）能继续任务

2\. Worker 要开子进程避免上下文爆掉

3\. Manager 去管理

---

**宝玉** @dotey [2025-09-28](https://x.com/dotey/status/1972206225313223136)

Claude Code 虽然上下文不会爆掉，但是用量会爆 😂

![Image](https://pbs.twimg.com/media/G16vGfLWcAAfjN-?format=jpg&name=large)

---

**宝玉** @dotey [2025-09-28](https://x.com/dotey/status/1972207923096142132)

看截图，我以前介绍过：Claude Code 有个特别的工具叫 Task tool，本质就是一个子 Agent，它可以有独立的上下文，所以哪怕它用了很多token，但也不会占用多少主Agent的上下文空间

![Image](https://pbs.twimg.com/media/G16wZ6yWYAAegir?format=jpg&name=large)

---

**宝玉** @dotey [2025-09-28](https://x.com/dotey/status/1972209849997074619)

这样传统的脚本思路其实也可以的

claude code 支持 hook，理论上来说可以借助 hook 来自动化

> 2025-09-28
> 
> 我的办法是用python脚本调用，目前我review小说的流程就是脚本调用claude code， codex没试过应该也可以
> 
> 要点是：claude code完成一个任务后，会写到一个完成文件，然后脚本里有监控流程，出现这个文件n秒后自动close claude，然后由脚本进行下一次task
> 
> 这样每次是新调用claude，跑多少轮都可以

---

**宝玉** @dotey [2025-09-28](https://x.com/dotey/status/1972218473242939896)

这也是个好办法

> 2025-08-28
> 
> 这是我用 Warp 作为编排器来调度多个 coding agent 的一个例子
> 
> 我觉得这比用 Zed ACP 的方式简单和自然多了，还不需要额外适配。
> 
> 不过 Zed 会不会做 multi agent 编排呢？我觉得长远看会的，但前提是它的先把各家 agent 完成适配。但是像 Warp 这种本来就能在终端下调用其他工具的环境，可能就更自然 x.com/zhangjintao902…

---

**宝玉** @dotey [2025-09-28](https://x.com/dotey/status/1972311209363079389)

为什么要用 AI 去监督 AI 干活而不是脚本：

1\. 探索各种可能性

2\. 这样用 AI 监测，比脚本的好处是：

\- 简单易行（但是费 Tokens）

\- 可以根据任务执行的结果动态处理， Prompt 可以不是固定的

https://x.com/geniusvczh/status/1972246705090523237…

---

**宝玉** @dotey [2025-09-28](https://x.com/dotey/status/1972345128439226793)

后来还是让 Codex 用传统脚本思路写了个版本也不错，每 5 分钟执行一次，仅供参考：

#!/usr/bin/env bash

#

\# codex\_task\_monitor.sh — minimal scheduler that runs

\# \`export TERM=xterm && codex exec "continue to next task" --full-auto\`

\# every five minutes and reports each run's outcome.  
后来还是让 Codex 用传统脚本思路写了个版本也不错，每 5 分钟执行一次，仅供参考：

#!/usr/bin/env bash

#

\# codex\_task\_monitor.sh — 运行任务的最小调度器

\# \`export TERM=xterm && codex exec "继续执行下一个任务" --full-auto\`

每五分钟执行一次，并报告每次运行的结果。

---

**熊布朗** @Stephen4171127 [2025-09-28](https://x.com/Stephen4171127/status/1972347005931590095)

如果中间不自动追加 TODO 的话，会不会很快就做完了？

——

前面做 DR Agent 的时候，会面临集中选择

Plan-Execute 模式下

1\. 每次做完一个 Task，直接 Replan

2\. 某个 Task 扩展成许多 Sub-tasks，做完了再收敛。

3\. 一次性 Plan，等全部 Task 完成，结束。