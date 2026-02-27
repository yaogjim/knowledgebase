---
title: "2026-02-27_PsiACE_PsiACE_在_bub_的设计里_有一个名为_tape_的无尽长纸带_它存储的就是全量的历"
source: "https://x.com/LotusDecoder/status/2027183203724001305"
author:
  - "[[@PsiACE]]"
published: 2026-02-27
created: 2026-02-27
description:
tags:
  - "x"
  - "@PsiACE"
  - "anchor"
  - "agent"
---

# PsiACE 在 bub 的设计里，有一个名为 tape 的无尽长纸带，它存储的就是全量的历

**PsiACE**

在 bub 的设计里，有一个名为 tape 的无尽长纸带，它存储的就是全量的历史事实，并且自主进行上下文装配，没有依赖向量、memory 等机制 我们使用两个简单的机制让 agent 自主管理它： - anchor ，用来标记当前的阶段和状态以及需要关注的信息。 - handoff，切换到某个 anchor 并屏蔽无关的历史上下文

> **@blackanger**
> 
> 我不太懂。 为什么像现在的 agent ，比如 claude code / codex 就不能实现一个「滑动窗口」机制来处理上下文。 不做有损压缩，而是把全量 Session 历史存入外部记忆，窗口里只放当前任务步骤真正需要的内容。 窗口不是按时间顺序固定滑动，而是按需求动态组装。

![🦀](https://abs-0.twimg.com/emoji/v2/svg/1f980.svg)

* * *

### 热门回复

**@LotusDecoder** ♥ 3 · 💬 1

开个脑洞，每天早起的时候， anchor 设为收集三部分， 一是长期目标， 二是近期活动， 三是今天待办， 每天早上这样搞一个上下文。 都是处在对自己的位置感知很清醒的样子。

**@PsiACE** ♥ 4 · 💬 1

嗯嗯，这个当然也是可行的，最开始我是把 anchor 设计为某种指针，但是后来发现其实还是可以考虑携带信息的，所以也完全有表达力可以做到这些 另一个有意思的做法是， anchor 也是人可以去添加的，所以也相当于留出了人指导模型的机制，比如每个人都可以打包含自己信息/相关任务的一些锚点，最后 agent 收集起来分别响应

**@LotusDecoder** ♥ 0 · 💬 1

是的， 我之前给自己的 陪伴agent ， 长期目标是一份静态的md， 近期活动，想做一层动态的收集 git 变更历史再浓缩， 待办事项，从todo app 里拉取进来。 如果是 bub 的话，每天早起一个 anchor ，自己看一下再手工修正。

**@MagBak** ♥ 0 · 💬 0

All-new Samsung S26 Ultra/Plus Elite case. Strongest magnets, S-Pen functionality, fast MagSafe charging, and more.