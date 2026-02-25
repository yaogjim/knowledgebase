---
title: "2026-02-25_Augment_Code_Augment_Code_规范驱动开发的错误之处_唯一可以100_信任的文档就是代码本身"
source: "https://x.com/augmentcode/status/2025993446633492725"
author:
  - "[[@Augment Code]]"
published: 2026-02-25
created: 2026-02-25
description:
tags:
  - "x"
  - "@Augment Code"
  - "what"
  - "spec"
---

# Augment Code # 规范驱动开发的错误之处 唯一可以100%信任的文档就是代码本身

**Augment Code**

# 规范驱动开发的错误之处

唯一可以100%信任的文档就是代码本身。

设计文档、变更日志、README 文件、架构图、新手入门指南。这些资料几乎每一份都会立即过时。

保持书面文档与不断变化的系统同步是一项持续的成本，而工程师的工作模式是爆发式的。他们写完文档，发布功能，然后继续下一个任务。更新文档的工作是隐形的，它与当天所有其他工作竞争，而且几乎每次都败下阵来。我们尝试过流程优化，尝试过工具改进，也尝试过将其打造为团队价值观。但这些都无济于事，因为我们一直在要求人们去做一件他们通常不会做的事情。

这就是规范驱动开发通常会失败的地方。这个想法本身是合理的：当你与编码代理合作时，在放手让他们工作之前，先把你的需求写下来。这显然比把提示粘贴到聊天窗口然后祈祷好得多。

但规范是一份文件。而我们刚才已经确定了文件的处理方式。

区别在于事关重大。一份过时的设计文档会误导下一个偶然看到它的工程师。一份过时的规范会误导那些缺乏相关知识的代理商。他们会自信地执行一个早已脱离实际情况的方案，而不会指出任何问题。

So when we started building

[意图](https://www.augmentcode.com/product/intent)

, the question we kept circling was: what if the spec wasn't something you maintained? What if it maintained itself?

这就是我们最终决定的方案。

规范并非人为产物，也非代理产物。双方都可以读取和写入规范。

您描述想要构建的内容。协调代理会起草一份规范，并将其分解为多个任务。您查看、编辑并批准该规范，然后才能开始运行。代理开始工作后，会将更新信息反馈给您：它们发现了什么、做了哪些更改、遇到了哪些计划之外的限制。您可以随时暂停，重写规范的某些部分，代理会从新的状态继续执行。

想想当你把任务交给一位优秀的初级工程师时会发生什么。你把工单交给他，他开始着手处理，当他发现 API 不支持工单中假设的分页方式时，他会主动更新工单。他不会等你发现问题，也不会直接构建错误的东西。他会回来告诉你：“这个假设是错误的，我做了以下更改，原因如下。” 你审核他的更新，然后决定批准还是拒绝。

That's the relationship we wanted between the developer and the spec. The ticket stays honest because both sides are maintaining it.

The junior engineer analogy goes further than you'd think. A good junior doesn't narrate every line of code. They surface the decisions that change direction: "I found an existing auth context, so I wired into that instead of creating a new one." That's the signal. That's what you want from agents too. Getting this granularity right turns out to be one of the genuinely interesting design problems in the system. Too much and the spec becomes noise you learn to ignore. Too little and you're back to guessing what happened.

Here's what a task actually looks like. You write: "Add a dark mode toggle to the settings page that respects system preferences." The coordinator reads your codebase, drafts a spec with three subtasks: add the toggle component, wire it to a preference store, update the CSS variables.

You scan it, notice it missed the bit about persisting the choice across sessions, and add a line.

You approve.

Agents pick up the work.

Fifteen minutes later, one of them has updated the spec: "Found an existing theme context provider in the codebase. Wired into that instead of creating a new store."

You review the code change (clearly grouped by agent and task).

The spec now reflects what was actually built, not what was originally planned. And nobody had to remember to update it.

Every documentation-first initiative in software has failed for the same reason: it asked developers to do continuous maintenance work that nobody sees and nobody rewards.

SDD will fail for the same reason unless the agents do their share of the maintenance.

If agents can write code, they can update the plan.

[Let them.](https://www.augmentcode.com/product/intent)