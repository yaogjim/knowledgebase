---
title: "2026-03-09_Leo_Leo_终端崩了想恢复对话_之前的做法是让_Claude_自己在_claudepro"
source: "https://x.com/runes_leo/status/2029217049365680164"
author:
  - "[[@Leo]]"
published: 2026-03-09
created: 2026-03-09
description:
tags:
  - "#FreeJimmyLai"
  - "x"
  - "@Leo"
  - "session"
---

# Leo 终端崩了想恢复对话，之前的做法是让 Claude 自己在 ~.claudepro

**Leo**

终端崩了想恢复对话，之前的做法是让 Claude 自己在 ~/.claude/projects/ 下面翻 JSONL 文件，Glob + Grep 一通搜，能找到但慢，还吃 context。 装了 recall 之后，一条命令按关键词搜，纯本地 SQLite 索引，3000 多条历史对话 23 秒建完，秒出 session ID，直接 resume。 工具补的就是这种"能做但别扭"的缝隙。

![图片](https://pbs.twimg.com/media/HCkftg2XkAAg7oE?format=jpg&name=large)

> **@vista8**
> 
> 感觉Recall这个Skill值得测试下，同时支持CC和Codex。 场景：Claude Code虽然会在本地存jsonl聊天记录，但重启或上下文爆后。 中断再次输入Claude 进入，发现失忆了。。。 这个Skill能搜索所有你跟CC的对话。 直接问："找一下我们之前聊过的那个关于数据库优化的对话"，它就能把相关的会话翻出来。

* * *

### 热门回复

**@#FreeJimmyLai** ♥ 7.9K · 💬 200

Jimmy Lai knows exactly why he's being persecuted. The rest of the world knows why he's being persecuted. Today, he explained it to a judge in his sham trial under the CCP-backed National Security Law. Jimmy Lai has spent the last four years in solitary confinement as a

**@砚知 yanki** ♥ 5 · 💬 1

fucheng830/casr-gui 推荐这个项目，可以找对话，codex转claude 或者claude 转codex 很方便

**@Leo** ♥ 0 · 💬 2

resume 后要跟 session id，得先recall才能知道是哪个对话id

**@Leo** ♥ 1 · 💬 1

Feel free to share it sir, looking forward. 先生，请随意分享它，期待着。

**@xfu** ♥ 1 · 💬 1

这说明gui适合大多数人，cli太麻烦了