---
title: "Claude Code 多任务处理变简单"
source: "https://x.com/BadUncleX/status/1942289427533029789"
author:
  - "[[@BadUncleX]]"
created: 2025-07-08
description:
tags:
  - "@BadUncleX #Git #ClaudeCode #并发开发 #AI编程"
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
**BadUncle** @BadUncleX [2025-07-07](https://x.com/BadUncleX/status/1942289427533029789)

案例演示: 𝐆𝐢𝐭 𝐖𝐨𝐫𝐤𝐭𝐫𝐞𝐞 + 𝐂𝐥𝐚𝐮𝐝𝐞 𝐂𝐨𝐝𝐞 同时开发多个功能

\---youtube 链接见评论

Git worktree 让你在同一仓库创建多个工作目录，每个目录独立切换分支。结合 Claude Code，实现真正的并发开发——多个 AI 助手同时工作，互不干扰。

实战步骤

假设你有 \`music\_shop\` 项目，要并发开发 drums、bases、keyboards 三个功能：

1\. 创建 worktrees 管理目录

mkdir ../music\_shop-worktrees

2\. 为每个功能创建独立 worktree

\- git worktree add ../music\_shop-worktrees/drums -b drums

\- git worktree add ../music\_shop-worktrees/bases -b bases

\- git worktree add ../music\_shop-worktrees/keyboards -b keyboards

上述命令完成三件事：

\- 创建新分支（如 drums）

\- 复制完整代码到新目录

\- 将该目录绑定到对应分支

并发开发

打开三个终端/编辑器窗口：

终端1：开发鼓组功能

cd ../music\_shop-worktrees/drums

\> "实现鼓组音色选择功能"

终端2：开发贝斯功能

cd ../music\_shop-worktrees/bases

\> "添加贝斯音轨编辑器"

终端3：开发键盘功能

cd ../music\_shop-worktrees/keyboards

\> "创建虚拟键盘界面"

关键点：三个 Claude Code 实例并行工作，各自在独立分支上修改代码，无冲突。

合并成果

回到主项目目录

cd ../music\_shop

合并所有功能

\- git checkout main

\- git merge drums

\- git merge bases

\- git merge keyboards

为什么这么强？

1\. 真并发：不是切换分支，而是同时存在多个工作目录

2\. 零等待：Claude Code 各自运行，不用等一个完成再开始另一个

3\. 隔离性：每个功能独立开发、测试，出问题不影响其他功能

4\. 灵活性：随时在不同目录间切换查看进度，或手动调整代码

总结

Git worktree 把你变成一个多线程开发团队，每个线程配一个 Claude Code，并发效率拉满。

---

**BadUncle** @BadUncleX [2025-07-07](https://x.com/BadUncleX/status/1942289429915394420)

Claude Code Multitasking Made EASY

---

**BadUncle** @BadUncleX [2025-07-07](https://x.com/BadUncleX/status/1942362602887340300)

其实git worktree 是官方推荐的并发方式

> 2025-06-10
> 
> 如果订阅了Claude Max如何极限压榨Claude Code包月流量？ 并发执行
> 
> 话说一旦订阅Max后你的行为会自动想办法多用，包括Claude app和mcp,以及它自带的DR.
> 
> 回到claude code并发，官方推荐方式是用git worktree方式，基本原理就是借助git实现多版本并行
> 
> 适合场景: 一个任务跑主线开发，另任务跑bug fix
> 
> ![Image](https://pbs.twimg.com/media/GtDcirTbAAA9azT?format=jpg&name=large)