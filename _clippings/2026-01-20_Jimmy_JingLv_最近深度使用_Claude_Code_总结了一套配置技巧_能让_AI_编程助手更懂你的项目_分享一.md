---
title: "2026-01-20_Jimmy_JingLv_最近深度使用_Claude_Code_总结了一套配置技巧_能让_AI_编程助手更懂你的项目_分享一"
source: "https://x.com/Jimmy_JingLv/status/2011241944547279091"
author:
  - "[[@Jimmy_JingLv]]"
published: 2026-01-20
created: 2026-01-20
description:
tags:
  - "#frontmatter"
  - "x"
  - "@Jimmy_JingLv"
  - "https"
---

# 最近深度使用 Claude Code，总结了一套配置技巧，能让 AI 编程助手更懂你的项目。 分享一

**吕立青\_JimmyLv 2𐃏26** @Jimmy\_JingLv [2026-01-14](https://x.com/Jimmy_JingLv/status/2011241944547279091)

最近深度使用 Claude Code，总结了一套配置技巧，能让 AI 编程助手更懂你的项目。

分享一下 Commands、Skills、Subagent、模型选择和 Context Fork 的实战经验。

(Thread)

![Diagram showing Claude Code config directory structure with global ~/.claude and project 项目/.claude folders, commands/, skills/, and settings.json entries and comments.](https://pbs.twimg.com/media/G-ld45ZaIAAb3bN?format=png&name=large)

* * *

**吕立青\_JimmyLv 2𐃏26** @Jimmy\_JingLv [2026-01-14](https://x.com/Jimmy_JingLv/status/2011241959256645983)

1/ 目录结构

Claude Code 支持全局和项目两级配置：

\- ~/.claude/ 全局配置

\- 项目/.claude/ 项目配置（会覆盖全局）

每个目录下可以放 commands、skills 和 settings.json。

同时还有另外一个小技巧：可以通过文件夹软链接，在不同 CLI 工具之间共享 skills

![Image](https://pbs.twimg.com/media/G-ld54SbQAI_4gA?format=png&name=large)

* * *

**吕立青\_JimmyLv 2𐃏26** @Jimmy\_JingLv [2026-01-14](https://x.com/Jimmy_JingLv/status/2011241971223052543)

2/ Commands vs Skills

Commands：简单 prompt 模板，适合快速任务

Skills：多步骤复杂任务，可以包含多个文件和配置

比如 /commit 适合用 Command，/review-commit-push 这种需要多步检查的就适合用 Skill。

* * *

**吕立青\_JimmyLv 2𐃏26** @Jimmy\_JingLv [2026-01-14](https://x.com/Jimmy_JingLv/status/2011241986880356585)

3/ Frontmatter 配置

在 .md 文件开头用 YAML 配置关键参数：

\- model: haiku/sonnet/opus

\- context: fork（独立上下文）

\- tools: 白名单限制可用工具

![Image](https://pbs.twimg.com/media/G-ld7dlbQAcXPe4?format=jpg&name=large)

* * *

**吕立青\_JimmyLv 2𐃏26** @Jimmy\_JingLv [2026-01-14](https://x.com/Jimmy_JingLv/status/2011241999287062664)

4/ Context Fork 是关键

默认 inherit 会占用主对话上下文，大量 git diff 输出会撑爆 context。

设置 context: fork 后，任务在独立 sub-agent 执行，只返回结果，主对话保持清爽。

> 2026-01-13
> 
> 哇哦，贴切！tools 是模型上下文的一部分，所以也不推荐在 .claude 里面设置过多的 MCP，会占用主agent过多的思考空间。
> 
> 我今天就是在把 slash command 和 skill 改成了 context:fork 模式；当然 subagent 本身也不占用 main agent 的上下文窗口。
> 
> ![Image](https://pbs.twimg.com/media/G-it6KDXIAAPXBR?format=png&name=large) ![Image](https://pbs.twimg.com/media/G-iuNw7akAAu3HP?format=jpg&name=large)

* * *

**吕立青\_JimmyLv 2𐃏26** @Jimmy\_JingLv [2026-01-14](https://x.com/Jimmy_JingLv/status/2011242011471544404)

5/ 模型选择策略

\- haiku：便宜快速，适合 commit、lint 等简单任务

\- sonnet：平衡，日常开发

\- opus：高质量输出，文案写作、复杂分析

不同任务配不同模型，既省钱又高效。

* * *

**吕立青\_JimmyLv 2𐃏26** @Jimmy\_JingLv [2026-01-14](https://x.com/Jimmy_JingLv/status/2011242027380576724)

6/ Commit Message 规范

配合 commitlint 使用时注意：

\- NO emoji

\- scope 必填

\- 可以加 Prompt footer 记录上下文

![Image](https://pbs.twimg.com/media/G-ld9zvawAAhEKb?format=jpg&name=large)

* * *

**吕立青\_JimmyLv 2𐃏26** @Jimmy\_JingLv [2026-01-14](https://x.com/Jimmy_JingLv/status/2011242039472767038)

总结：Claude Code 的配置系统非常灵活。

合理配置能让 AI 更懂你的项目规范，减少重复沟通，提高编程效率。

完整配置文档可以参考 Claude Code 官方文档。

https://code.claude.com/docs/en/slash-commands#frontmatter…

另外，记得关注我，下期再来分享 subagents 的最新实践～

P.S. 本推文也是由 Agent Skill 直接发布

* * *

**han xu** @hanxu2018 [2026-01-14](https://x.com/hanxu2018/status/2011277604154982714)

Claude code现在api模式也要登陆 如何跳过有解决方案吗

* * *

**吕立青\_JimmyLv 2𐃏26** @Jimmy\_JingLv [2026-01-14](https://x.com/Jimmy_JingLv/status/2011280364824940695)

那就不确定该怎么办了，cc switch 有解决吗

* * *

**dongbo** @Dongbobob [2026-01-14](https://x.com/Dongbobob/status/2011475678005190985)

有没有降低 token 消耗的技巧？

* * *

**吕立青\_JimmyLv 2𐃏26** @Jimmy\_JingLv [2026-01-15](https://x.com/Jimmy_JingLv/status/2011612294103646474)

没有，😂 只有花钱

context:fork 是为了给 main agent 节省脑力，一定程度上其实是可以省钱的， 比如说把一些简单的任务交给 Subagent，用低价格的模型去干

* * *

**jim lee** @jimlee1414478 [2026-01-15](https://x.com/jimlee1414478/status/2011595583916749263)

m

* * *

**Jamf** @JamfSoftware

Apple just dropped macOS Tahoe. Now what?

Get the guide to navigate upgrade season with confidence.

Apple 刚刚发布了 macOS Tahoe。现在该怎么办？

获取指南，自信应对升级季。