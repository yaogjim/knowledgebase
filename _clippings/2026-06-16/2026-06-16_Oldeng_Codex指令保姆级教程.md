---
title: "2026-06-16_dengdry_Codex指令保姆级教程"
source: "https://x.com/dengdry/status/2052026438442725525"
author:
  - "[[@dengdry]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "x"
  - "@dengdry"
  - "codex"
  - "```"
---

# Codex指令保姆级教程

**Oldeng**

# Codex指令保姆级教程

这是一篇写给完全没用过 Codex 的新手教程。

每条指令我都会先讲它是干嘛的，再用大白话解释什么时候用，最后给一个可以照抄的例子。

读完你就能上手。

先说结论：

Codex 不是聊天机器人。

它更像一个坐在你项目目录里的 AI 编程同事。

你可以让它读代码、改文件、跑命令、写测试、看 diff、做 review。

但你要先学会控制它。

不然它很聪明，也很容易聪明过头。

## 一、什么是 Codex 指令？

![Image](https://pbs.twimg.com/media/HHowTgaWwAEm5fj?format=jpg&name=large)

Codex 里有两种输入。

一种是普通 prompt。

比如：

```text
帮我看一下这个项目怎么启动

帮我修一下登录页 bug

帮我把这个函数重构得清楚一点
```

这是你让 Codex 干活。

另一种是斜杠指令，也就是以 / 开头的命令。

比如：

```text
/init
/model
/plan
/diff
/review
/compact
```

这些不是让 AI 写代码的需求。

这些是你控制 Codex 工作方式的按钮。

一句话区分：

```text
普通 prompt = 你让 Codex 干什么活

斜杠指令 = 你怎么管理 Codex 这个工具
```

这点先搞清楚，后面就不乱了。

## 二、先记住 3 个常识

第一个，指令必须放在开头

```plaintext
/model
```

这样是对的。

```text
请帮我 /model
```

这样就不对。

因为 Codex 只有在输入框第一个字符看到 /，才会把它当指令。

你把 /model 放在句子中间，它就只是普通文字。

第二个，忘了指令就直接输入 /

在 Codex 里输入一个 /，它会弹出当前能用的指令列表。

你可以继续输入字母过滤。

比如输入：

```text
/mo
```

就能看到 /model。

注意，每个人看到的指令可能不一样。

因为你的系统、版本、插件、权限、实验功能都可能不同。

所以教程只能给你地图。

你本地输入 / 看到的列表，永远最准。

第三个，不要把 Claude Code 的东西硬套过来

很多人是从 Claude Code 转过来的，容易混。

Claude Code 里常见 'CLAUDE.md'、'/btw'、'/branch'。

Codex 里更常见的是 'AGENTS.md'、'/side'、'/fork'。

尤其是项目说明文件。

Codex 用的是 AGENTS.md。

你可以把它理解成写给 Codex 的项目入职手册。

以后 Codex 进项目，会先读它，知道项目规矩。

## 三、新手最该掌握的 10 条指令

别一上来背一堆。

先把这 10 条用熟，你就能完成 90% 的日常开发任务。

![Image](https://pbs.twimg.com/media/HHoxA6UWMAQxie-?format=jpg&name=large)

1\. /init

Codex 第一次进项目时，对你的代码库一无所知。

它不知道项目怎么启动，不知道测试怎么跑，不知道哪些目录不能动，也不知道你们团队有什么约定。

这时候先敲：

```text
/init
```

它会生成一个 AGENTS.md。

生成以后，最好你自己再补几句。

比如：

```text
本项目使用 pnpm
开发命令是 pnpm dev
测试命令是 pnpm test
不要修改 dist 和 generated 目录
所有接口请求都走 src/lib/api.ts
```

这几句很值钱。

因为你不用每次都重新教育 Codex。

你把规矩写进去，它以后自己会看。

2\. /status

你不知道 Codex 现在用什么模型、什么权限、在哪个目录、还能用多少上下文，就敲它。

```text
/status
```

它会告诉你当前模型、权限策略、可写目录、上下文情况。

什么时候用？

你怕它改错目录的时候。

你怀疑模型没切成功的时候。

你不知道现在是不是只读模式的时候。

你感觉对话太长的时候。

新手排查问题，第一反应就是 /status。

3\. /model

简单任务用快模型。

复杂任务用强模型。

敲：

```text
/model
```

它会弹出模型选择器。

什么时候该用强模型？

- 大型重构
- 复杂 bug
- 陌生代码库分析
- 跨模块迁移
- 架构设计
- 安全敏感改动

什么时候不用？

- 改文案
- 看一个小函数
- 修简单类型错误
- 解释一段代码
- 生成小脚本

一句话：

小活别烧钱，大活别省钱。

4\. /permissions

Codex 不是只会说话。

它真的会动你的文件。

所以权限很重要。

敲：

```text
/permissions
```

你可以控制它是只读，还是可以改文件，还是跑命令前必须问你。

新手建议保守一点。

一开始别全自动。

先让它读项目、出方案、解释原因。

等你熟悉它的行为，再逐步放开。

尤其是生产项目、老项目、没有 git 的项目，别一上来就让它撒开跑。

5\. /plan

大任务不要直接让 Codex 动手。

先让它想清楚。

比如你不要一上来就说：

```text
帮我重构权限系统
```

你应该说：

```plaintext
/plan 帮我分析当前权限系统，给出最小风险的重构方案，先不要改代码。
```

这个指令很适合:

- 重构
- 迁移
- 复杂 bug
- 性能优化
- 多文件修改
- 不确定风险的任务

新手记住一句话：

越大的任务，越要先 /plan。

6\. /mention

你不想让 Codex 全项目乱翻，就直接点名。

比如：

```text
/mention src/api/user.ts
```

然后再问：

```text
帮我解释这个文件的请求流程。
```

适合这些场景：

- 指定报错文件
- 指定组件
- 指定配置文件
- 让 Codex 只围绕某个文件分析
- 避免它在全项目乱找

很多新手的问题是，明明只是一个小 bug，却让 Codex 读半个项目。

你给它文件，它就少走弯路。

7\. /diff

Codex 改完代码以后，不要只看它的总结。

一定要看真实改动。

敲：

```text
/diff
```

增了哪些文件，删了哪些内容，有没有未跟踪文件。

这条非常重要。

Codex 说「我只做了一个小改动」，你别全信。

看 diff。

AI 的总结会漏。

diff 不会。

8\. /review

Codex 写完代码后，你可以让它切换成 reviewer 视角再看一遍。

敲：

```text
/review
```

它会重点看：

- 有没有 bug
- 有没有行为回归
- 有没有缺测试
- 有没有边界条件漏掉
- 有没有安全风险

提交前建议固定跑一次。

推荐组合：

```text
/diff
/review
```

先看改动，再让它审。

9\. /compact

你和 Codex 聊久了，对话会越来越长。

它每次回答都要带着前面的历史一起思考。

越聊越慢，越聊越贵。

这时候敲：

```text
/compact
```

它会把前面的对话压缩成摘要，然后继续当前任务。

注意：

/compact 不是清空。

它是压缩历史，继续当前话题。

如果你要彻底换任务，用 /new 或 /clear。

10\. /resume

昨天你让 Codex 修一个 bug，没修完。

今天回来继续。

敲：

```text
/resume
```

它会打开历史会话列表。

选中之前那条，就能接着干。

适合：

- 跨天任务
- 大项目迁移
- 长时间 debug
- 分阶段开发
- 开了 fork 后想回主线

## 四、新手最容易混的两个指令：/side 和 /fork

![Image](https://pbs.twimg.com/media/HHowgmZW8AIjL2q?format=jpg&name=large)

这个必须单独讲。

因为很多人一旦开了分支，就不知道自己在哪条线上。

先记一句话：

```text
/side 是临时问一句

/fork 是开一条新路线
```

/side 是什么？

它是临时侧聊。

比如你正在修 bug，突然想问：

```text
这个方案有没有明显风险？
```

你不想打断主线，就敲：

```text
/side 这个方案有没有明显风险？
```

它会开一个临时侧边对话。

问完之后，回到主线继续干活。

适合：

- 临时问一个判断
- 让它检查方案风险
- 问一句概念解释
- 不想污染主线

不适合：

- 复杂多轮讨论
- 认真尝试另一套实现
- 长期保存实验路线

/fork 是什么？

它是真的开新线程。

比如你现在有一个方案，但你想试另一种实现，又不想破坏当前讨论。

敲：

```text
/fork
```

Codex 会复制当前会话，开一条新线。

这就像 git branch。

适合：

- 试另一种架构
- 比较两个方案
- 保留主线同时开实验线
- 让 Codex 用完全不同思路实现

怎么回去？

用：

```text
/resume
```

选择原来的那条会话。

一句话总结：

/side 是临时小窗口。

/fork 是真正开分支。

## 五、第一次用 Codex，照着这个流程走

![Image](https://pbs.twimg.com/media/HHowphaWwAYdutr?format=jpg&name=large)

第一步，进项目目录。

```text
cd my-project
codex
```

第二步，初始化项目说明。

```text
/init
```

第三步，看状态。

```text
/status
```

第四步，先让它读项目，不要直接改。

```text
先不要改代码，帮我读一下这个项目结构，告诉我启动命令、测试命令、主要模块和最危险的目录。
```

第五步，大任务先计划。

```text
/plan 帮我修复登录页提交后 loading 状态不消失的问题。先定位相关文件，给出最小改动方案，不要直接改代码。
```

第六步，确认方案后再让它改。

```text
按方案实现，保持改动尽量小。
```

第七步，看真实改动。

```text
/diff
```

第八步，提交前审查。

```text
/review
```

这就是新手最稳的一套流程。

别一上来就全自动。

先让它读，再让它想，再让它改，最后你验收。

## 六、写好 AGENTS.md，Codex 才不会每次都像新员工

![Image](https://pbs.twimg.com/media/HHowsukXEAY-iCJ?format=jpg&name=large)

/init 只是生成脚手架。

真正有价值的是你写进去的项目规则。

一个好用的 AGENTS.md 可以这么写：

```text
# Project Guide for Codex

## Commands

Install: pnpm install
Dev: pnpm dev
Test: pnpm test
Lint: pnpm lint
Build: pnpm build

## Rules

Do not edit dist/
Do not edit generated files
Keep changes minimal
Run tests after touching business logic
Use existing components before creating new ones

## Architecture

API clients live in src/lib/api
Shared UI components live in src/components
Route pages live in src/pages
Auth logic lives in src/auth

## Before finishing

Explain changed files
Mention tests run
Mention tests not run
```

这东西很重要。

你不要每次都重新告诉 Codex：

我们项目用 pnpm。

不要改 dist。

提交前要跑测试。

这些全写进 AGENTS.md。

一次写好，长期复用。

这才是把 Codex 从聊天工具变成项目同事的关键。

## 七、常见疑问

Q1：我看到的指令比文章里少，正常吗？

正常。

你能看到哪些指令，取决于 Codex 版本、系统、插件、实验功能和配置。

以本地输入 / 弹出的列表为准。

Q2：Codex 会不会乱改我的代码？

会不会乱改，主要取决于三件事：

- 你的权限设置
- 你的 prompt 是否清楚
- 你有没有看 /diff

新手不要一上来放全自动。

Q3：/compact 会不会让 Codex 忘东西？

它会压缩历史，不是完整保留每个细节。

如果你担心关键信息丢失，可以这样写：

```text
/compact 保留登录模块的结论、已修改文件、剩余 bug 和测试失败信息。
```

Q4：/new 和 /clear 有什么区别？

/new 是开新对话。

/clear 是清空终端显示并 fresh chat。

新手不用太纠结。

任务没结束，用 /compact。

任务结束了，要换新话题，用 /new 或 /clear。

Q5：/fork 后怎么回主线？

用：

```text
/resume
```

从历史会话里选原来的那条。

Q6：Codex 改完代码我应该做什么？

固定三步：

```text
/diff

/review

运行测试
```

不要只看它的总结。

Q7：Codex 和 ChatGPT 写代码有什么区别？

ChatGPT 更像远程顾问。

你要把代码贴给它。

Codex 更像坐在你项目目录里的同事。

它能直接读文件、改文件、跑命令、看 diff。

## 八、最后给新手的使用口诀

先 /init，让 Codex 认识项目。

再 /status，确认状态。

大任务先 /plan。

关键文件用 /mention。

改完必须 /diff。

提交前跑 /review。

对话长了用 /compact。

明天回来用 /resume。

临时问一句用 /side。

想试新路线用 /fork。

就这么简单。

Codex 指令看起来多，其实新手不用背全部。

你先把这几条练熟，就已经能跑通大部分日常开发流程了。

最后说句实在的：

别一上来就追求全自动。

先把 Codex 当成一个很聪明、但需要你管理的编程同事。

你给它上下文，它就少猜。

你给它边界，它就少乱动。

你看 diff，它就不敢糊弄你。

会用 Codex 的人，不是把方向盘交给 AI。

而是让 AI 坐上副驾，帮你看路、查地图、修车。

必要的时候，再让它替你开一段。

参考资料：

[Codex CLI 官方文档](https://developers.openai.com/codex/cli)

[Codex CLI Slash Commands 官方文档](https://developers.openai.com/codex/cli/slash-commands)