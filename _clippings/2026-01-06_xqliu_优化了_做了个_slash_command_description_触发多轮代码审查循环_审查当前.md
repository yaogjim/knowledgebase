---
title: "2026-01-06_xqliu_优化了_做了个_slash_command_description_触发多轮代码审查循环_审查当前"
source: "https://x.com/xqliu/status/2008131711448818095"
author:
  - "[[@xqliu]]"
published: 2026-01-06
created: 2026-01-06
description:
tags:
  - "x"
  - "@xqliu"
  - "---"
---

# 优化了，做了个 slash command description 触发多轮代码审查循环，审查当前

**Larry & Leo Bro - Eagle of Full Stack** @xqliu 2026-01-04

优化了，做了个 slash command

\---

description: 触发多轮代码审查循环，审查当前未提交的改动，直到通过

\---

\# Code Review Loop

执行以下流程：

1\. 运行 \`git diff\` 和 \`git diff --cached\` 获取当前所有未提交的改动

2\. 运行 \`/20-code-review\` 获取完整的审查标准

3\. 让 @oracle 根据审查标准审查这些改动

4\. 如果 @oracle 发现 blocking issues：

\- 列出所有 blocking issues

\- 逐一修复

\- 修复后再次让 @oracle 审查

5\. 重复步骤 4，直到 @oracle 明确表示 "LGTM" 或 "No blocking issues"

6\. 输出最终审查报告：

\- 审查轮数

\- 修复的问题列表

\- 最终状态

\## 规则

\- 只处理 blocking issues，suggestions/nitpicks 记录但不阻塞

\- 最多 5 轮，超过则停止并报告剩余问题

\`\`\`

保存到 \`.claude/commands/review-loop.md\`

用法直接：

\`\`\`

/review-loop

> 2026-01-04
> 
> 发现 oh-my-opencode 其实是可以做多 agent 会诊的! 我用了下面的 prompt, 居然就工作了
> 
> 你让 codex 和 gemini 的 sub agent 用 @.claude/commands/20-code-review.md 的7轮审查标准审查了吗? 审查结果你考虑并修复/优化了吗?
> 
> opencode 和 oh-my-opencode 的链接见回复 x.com/xqliu/status/2…

* * *

**Larry & Leo Bro - Eagle of Full Stack** @xqliu [2026-01-05](https://x.com/xqliu/status/2008132283925193092)

/20-code-review 这个 slash command 定义晚上发

* * *

**Larry & Leo Bro - Eagle of Full Stack** @xqliu [2026-01-06](https://x.com/xqliu/status/2008349238783017032)

\---

name: code-review

description: 通用代码审查命令，基于业务需求进行白盒逻辑正确性审查和技术架构评估

\---

\# 代码审查命令

\## 审查任务

请对当前工作区的代码修改进行全面审查，重点关注业务逻辑的正确性和技术架构的合理性。

\## 审查维度

\### 1. 业务层面审查（BLOCKING级别）

\- x.com/xqliu/status/2…

> 2026-01-05
> 
> \---
> 
> name: code-review
> 
> description: 通用代码审查命令，基于业务需求进行白盒逻辑正确性审查和技术架构评估
> 
> \---
> 
> \# 代码审查命令
> 
> \## 审查任务
> 
> 请对当前工作区的代码修改进行全面审查，重点关注业务逻辑的正确性和技术架构的合理性。
> 
> \## 审查维度
> 
> \### 1. 业务层面审查（BLOCKING级别）
> 
> \- x.com/xqliu/status/2…

* * *

**victor-wu** @victor\_wu\_eth [2026-01-05](https://x.com/victor_wu_eth/status/2008161358668497035)

卧槽，我自己写了个skill和你是一个思路，不过用的是codex cloud 的pr review功能，我最高对话过十次，他妈的每次都能发现问题，最后气的我直接关闭pr，重新让codex从需求开始重写

* * *

**QiPing Wan** @QipingWan [2026-01-05](https://x.com/QipingWan/status/2008224498403996095)

我也有类似的，不过我是让他报告高中低三种风险。但是要结合实际的情况，避免一些不必要的修复。等等

* * *

**虾米** @xiamiluo [2026-01-05](https://x.com/xiamiluo/status/2008212561553129841)

Vs code可以吗

* * *

**ElevenLabs** @elevenlabsio

The most realistic voice AI models. Text to speech, voice cloning, voice changer & more—all in one editor. Try for free.