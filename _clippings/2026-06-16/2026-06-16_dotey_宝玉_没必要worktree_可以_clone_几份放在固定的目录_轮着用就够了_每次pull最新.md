---
title: "2026-06-16_dotey_宝玉_没必要worktree_可以_clone_几份放在固定的目录_轮着用就够了_每次pull最新然"
source: "https://x.com/dotey/status/2039514661331034299"
author:
  - "[[@dotey]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "x"
  - "@dotey"
  - "💬"
  - "clone"
---

# 宝玉: 没必要worktree，可以 clone 几份放在固定的目录，轮着用就够了，每次pull最新然后checkout一个新的branch，完成后提PR合并到main

**宝玉**

没必要worktree，可以 clone 几份放在固定的目录，轮着用就够了，每次pull最新然后checkout一个新的branch，完成后提PR合并到main

> **@hyspace**
> 
> 请教monorepo太大导致没法git worktree，如何更好的并行开发？

* * *

### 热门回复

**@Miami HEAT** ♥ 208 · 💬 0

Win your way into the final game of the Regular Season :fire: Download the Hard Rock Bet app and enter now!

**@CME Group Active Trader** ♥ 48 · 💬 5

Gold futures and options provide the flexibility to trade in both directions, maximizing capital efficiency.

**@宝玉** ♥ 23 · 💬 4

这一条推文争议很大，我说的确实不够严谨，有过多个人偏好在里面（我自己不喜欢用worktree），提供了一种选择，但没必要否定另一种，这点是我不对

同样的，我原推提供的多个固定目录 clone 方案是没问题的，如果你觉得 worktree 好也必要去否定我的方案，大家都求存同异就好

适合的就是好的

**@leifu \_/** ♥ 12 · 💬 4

宝玉老师好，对这个问题我有不同看法，monorepo大才更应该用worktree而不是多clone。

Worktree只多出一份工作树文件，共享同一个.git目录。多clone则是每份都要完整复制.git，monorepo越大，多clone的磁盘和clone时间代价越高。

**@狐狸布布** ♥ 6 · 💬 2

多repo clone的方案其实在大厂搜索推荐团队很常见

我们做A/B实验的时候 一个需求可能同时开3-4个实验分支 用worktree确实不如直接clone几份来得直觉

核心原因：AI coding agent（Claude Code/Cursor）天然就是一个agent一个目录 物理隔离比逻辑隔离更不容易出幺蛾子

唯一的坑是push前记得sync main