---
title: "2026-06-16_chenchengpro_陈成_Claude_Code_负责人_bcherny_说他已经不_prompt_Claude_了"
source: "https://x.com/chenchengpro/status/2064221035734646916"
author:
  - "[[@chenchengpro]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "x"
  - "@chenchengpro"
  - "agent"
  - "💬"
---

# 陈成: Claude Code 负责人 @bcherny 说他已经不 prompt Claude 了

**陈成**

Claude Code 负责人 [@bcherny](/bcherny)

说他已经不 prompt Claude 了。是循环在 prompt Claude、在决定下一步，他的活变成了写那个循环。Addy Osmani 给这事起了个名，叫 loop engineering：你不再是那个一轮轮敲 prompt 的人，而是搭一个会自己找活、分发、检查、记账、定下一步的系统，让它去捅 agent。

循环就五个零件，Claude Code 和 Codex 现在都备齐了。Automations 是心跳：定时自己跑、自己发现和分流，有结果进 Triage 收件箱，没结果就归档（/loop 按周期重跑，/goal 跑到你写的可验证条件为真才停，每轮完一个独立小模型来判断算不算完成，写代码的 agent 没资格给自己打分）。Worktrees：git worktree 给每个并行 agent 一份独立 checkout，从机制上断了它们踩同一个文件的可能。Skills：SKILL.md 把项目知识摊在外面，省得 agent 每次像金鱼一样重猜一遍，没它循环每轮都从零重推你的项目。Connectors（建在 MCP 上）：让循环够得着 issue tracker、数据库、staging API、Slack，差别就在「这是修复方案」和「自己开 PR、关联 ticket、CI 绿了就 ping 频道」之间。Sub-agents：写的人和检查的人分开，毕竟写代码的模型给自己打分总是手软。

还有第六件，最不起眼，可能也最要命：memory。一个 markdown 文件，或者一块 Linear board，活在单次对话之外，记着做过什么、下一步干嘛。模型每跑一次就忘光上一次，所以记忆得落在磁盘上，不能搁在 context 里。一句话，agent 会忘，repo 不会。

但有三件事循环没替你解决，而且循环越顺，这三件越扎手。第一，验证还是你的事：没人盯着的循环，也是在没人盯着地犯错，done 只是它的声明，不是证明。第二，你的理解会烂掉：循环越快地 ship 那些你没亲手写的代码，你和代码之间的鸿沟就越宽。第三，最舒服的姿势往往最危险——循环自己转起来，你很容易就不再有观点、照单全收。所以那句话是对的：Build the loop, stay the engineer，循环你来搭，但工程师这个位子得你自己坐着。

> **@addyosmani**
> 
> Addy Osmani @addyosmani · 10h 文章 循环工程 循环工程正在取代你作为提示代理的角色。你设计一个系统来替代你完成这个任务。这里的循环可以被视为一个递归目标，在这个目标中你定义一个目的... Addy Osmani @addyosmani · 10h 文章 循环工程 循环工程正在取代你作为提示代理的角色。你设计一个系统来替代你完成这个任务。这里的循环可以被视为一个递归目标，在这个目标中你定义一个目的...

![引用图片](https://pbs.twimg.com/media/HKU_Us-bMAAZO3J?format=jpg&name=large)

* * *

### 热门回复

**@Viking** ♥ 494 · 💬 22

分享一篇文章：《How LLMs Actually Work》

https://

0xkato.xyz/how-llms-actua

lly-work/

…

好像是前几天 HackerNews 排名第一来着，类似的文章很多，但是这篇深入浅出和直观的例子非常适合有一定编程但没深入学Transformer的人阅读，里面的比喻也恰当，一看就是活人写的，没什么 AI 味道。

**@宝玉** ♥ 237 · 💬 164

微信格局还是不够，总是想着大家都去他们家一亩三分地耕耘，还幻想着未来微信会继续是超级入口，人人都在用微信，所以只需要让 AI 去操作小程序。

但现实是，未来微信的入口属性会越来越少，以后的年轻人，不会再去打开微信，只会问自己的

**@陈成** ♥ 345 · 💬 43

Cloudflare CTO 随口问了句"大家都怎么用 loops?"，三分钟后自己补刀"To orchestrate agents"，结果 245 条回复把 2026 年中 AI agent 圈最热的"循环"玩法扒了个底朝天。

真正有料的就四类。CI/PR 保姆：循环盯 CI 跑绿、监控 PR 评论、改完自动同步 README 和下游文档，有人让 agent

**@Max For AI** ♥ 118 · 💬 28

没想到微信官方这个Skill最佳实践文档居然写得这么好？？

里面几个点写得特别细。

比如用户意图模糊时，什么时候该追问，什么时候该直接给默认方案，什么时候该把多个可能意图列出来让用户选。

**@Benjamin Meng** ♥ 0 · 💬 0

有几个文件现在完全是agent写的，我改都不敢随便改，怕动一行崩一片。速度是快了，但"我的项目里有些地方我自己看不懂"这感觉挺别扭的。