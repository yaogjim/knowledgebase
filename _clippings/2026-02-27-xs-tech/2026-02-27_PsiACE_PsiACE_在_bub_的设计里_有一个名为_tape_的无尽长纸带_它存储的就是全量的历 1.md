---
title: "2026-02-27_PsiACE_PsiACE_在_bub_的设计里_有一个名为_tape_的无尽长纸带_它存储的就是全量的历"
source: "https://x.com/repsiace/status/2027063072058490991"
author:
  - "[[@PsiACE]]"
published: 2026-02-27
created: 2026-02-27
description:
tags:
  - "x"
  - "@PsiACE"
  - "anchor"
  - "bub"
---

# PsiACE 在 bub 的设计里，有一个名为 tape 的无尽长纸带，它存储的就是全量的历

**PsiACE**

在 bub 的设计里，有一个名为 tape 的无尽长纸带，它存储的就是全量的历史事实，并且自主进行上下文装配，没有依赖向量、memory 等机制 我们使用两个简单的机制让 agent 自主管理它： - anchor ，用来标记当前的阶段和状态以及需要关注的信息。 - handoff，切换到某个 anchor 并屏蔽无关的历史上下文 任务开始，选取合适的历史和通过工具/技能获取的信息装配。任务完成，上下文的生命周期结束。 我们在群聊多人多 Agent 环境进行了技术验证并且运行了超过两周时间，由 agent 自主管理上下文和 handoff/anchor 时机。

> **@blackanger**
> 
> 我不太懂。 为什么像现在的 agent ，比如 claude code / codex 就不能实现一个「滑动窗口」机制来处理上下文。 不做有损压缩，而是把全量 Session 历史存入外部记忆，窗口里只放当前任务步骤真正需要的内容。 窗口不是按时间顺序固定滑动，而是按需求动态组装。

![🦀](https://abs-0.twimg.com/emoji/v2/svg/1f980.svg)

* * *

### 热门回复

**@PsiACE** ♥ 9 · 💬 1

我有一些文章也讨论了相关的主题，欢迎阅读 https:// psiace.me/zh/posts/prome theus-bound/ …

**@TJ (thaddeus jiang)** ♥ 6 · 💬 2

eue 实现了 bub 的 tape 概念，我刚刚和 ChatGPT 聊天，他给我画了一张图。 求原作者 review 一下架构

**@LotusDecoder** ♥ 3 · 💬 1

开个脑洞，每天早起的时候， anchor 设为收集三部分， 一是长期目标， 二是近期活动， 三是今天待办， 每天早上这样搞一个上下文。 都是处在对自己的位置感知很清醒的样子。

**@PsiACE** ♥ 4 · 💬 1

嗯嗯，这个当然也是可行的，最开始我是把 anchor 设计为某种指针，但是后来发现其实还是可以考虑携带信息的，所以也完全有表达力可以做到这些 另一个有意思的做法是， anchor 也是人可以去添加的，所以也相当于留出了人指导模型的机制，比如每个人都可以打包含自己信息/相关任务的一些锚点，最后

**@PsiACE** ♥ 3 · 💬 1

bub 可以考虑通过比如 bub run 运行一个实例作为 subagent ，fork 出的线程会在完成后 merge 进去并且不改变只追加的语义。 而至于 anchor 机制，你可以指导 agent 自主管理技巧，让其自己分析场景和行为决定如何去做，就像我教 bub 做 handoff 一样：