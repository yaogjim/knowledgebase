---
title: ""
source: "https://x.com/ryancarson/status/2020931274219594107"
author: ""
created: 2026-02-13 17:54:47
date: 2026-02-13 17:54:47
description: ""
tags: ""
---
本文将向您展示如何通过一条简单的命令，将一整个代理团队安装到您的 OpenClaw 配置中。

然后你的 lobster 将能够管理代理团队，并让他们执行可重复的、确定性的工作流来发布真实的 PR。

2.  你会获得一个仪表盘，以可视化方式呈现正在发生的情况……
    

[

![Image](https://pbs.twimg.com/media/HAvEy13aAAEKXgF?format=jpg&name=medium)



](https://x.com/ryancarson/article/2020931274219594107/media/2020925235537772545)

你可以点击进入一个任务以查看所有详情，包括你的 agent 团队正在全力推进的用户故事（带验收标准）...

[

![Image](https://pbs.twimg.com/media/HAvFXLNa0AE5zv9?format=jpg&name=medium)



](https://x.com/ryancarson/article/2020931274219594107/media/2020925859742535681)

-   一条命令即可将完整的代理团队安装到您现有的@openclaw 设置
    
-   确定性工作流——相同的步骤，相同的顺序，每次
    
-   代理们验证彼此的工作
    
-   每个代理获得新的上下文
    
-   YAML 定义的，因此你可以构建你自己的工作流
    
-   零基础设施——没有 Docker，没有 Redis，没有 Kafka
    

```
install github.com/snarktank/antfarm
```

一条命令即可配置一切：代理工作区、cron 轮询、子代理权限。

提交一个功能请求。得到一个经过测试的 PR。计划器将你的任务分解为用户故事。每个用户故事都在独立环境中被实现、验证和测试。失败时会自动重试。

```
plan → setup → implement → verify → test → PR → review
```

将其指向一个代码库。返回一个包含回归测试的安全修复拉取请求。扫描漏洞，按严重程度排序，为每个漏洞打补丁，在所有修复应用后重新审计。

```
scan → prioritize → setup → fix → verify → test → PR
```

粘贴错误报告。获得带回归测试的修复。分类员重现问题，调查员找到根本原因，修复者打补丁，验证者确认。无需专人照看。

```
triage → investigate → setup → fix → verify → PR
```

```
$ antfarm workflow install feature-dev
✓ Installed workflow: feature-dev

$ antfarm workflow run feature-dev "Add user authentication with OAuth"
Run: a1fdf573
Workflow: feature-dev
Status: running

$ antfarm workflow status "OAuth"
Run: a1fdf573
Workflow: feature-dev
Steps:
  [done   ] plan (planner)
  [done   ] setup (setup)
  [running] implement (developer)  Stories: 3/7 done
  [pending] verify (verifier)
  [pending] test (tester)
  [pending] pr (developer)
  [pending] review (reviewer)
```

相同的工作流程、相同的步骤、相同的顺序。而不是“希望代理能记得测试”。

开发者不会自行检查自己的工作。由独立的验证人员对照验收标准检查每个用户故事。

每个代理通过 Ralph 循环获得一个干净的会话。没有上下文窗口膨胀。没有来自 50 条消息之前的幻觉状态。

失败步骤会自动重试。如果重试次数用尽，会升级通知给您。没有任何失败会悄无声息。

YAML 中的代理和步骤。每个代理拥有一个角色、一个工作空间和严格的验收标准。关于谁做什么没有歧义。

一条命令即可配置所有内容：代理工作区、cron 轮询、子代理权限。无需 Docker，无需队列，无需外部服务。

代理独立轮询工作。认领步骤，执行工作，将上下文传递给下一个代理。SQLite 跟踪状态。Cron 保持其运行。

YAML + SQLite + cron。就这些。

没有 Redis，没有 Kafka，没有容器编排工具。

Antfarm 是一个 TypeScript CLI，零外部依赖。它能在 OpenClaw 运行的任何地方运行。

[

![Image](https://pbs.twimg.com/media/HAvGvPDWkAA8BY_?format=jpg&name=medium)



](https://x.com/ryancarson/article/2020931274219594107/media/2020927372602544128)

每个代理在一个全新的会话中运行，拥有干净的上下文。记忆通过 git 历史和进度文件持续存在——来自

，扩展到多代理工作流。

内置的工作流是起点。你可以用纯 YAML 和 Markdown 定义自己的代理、步骤、重试逻辑和验证门。如果你能编写提示词，你就能构建一个工作流。

```
id: my-workflow
name: My Custom Workflow
agents:
  - id: researcher
    name: Researcher
    workspace:
      files:
        AGENTS.md: agents/researcher/AGENTS.md

steps:
  - id: research
    agent: researcher
    input: |
      Research {{task}} and report findings.
      Reply with STATUS: done and FINDINGS: ...
    expects: "STATUS: done"
```

你正在安装在你的机器上运行代码的代理程序。这很吓人，我们对此非常重视。

-   仅精选代码仓库 — Antfarm 仅从官方 snarktank/antfarm 代码仓库安装工作流。不允许任意远程源。
    
-   针对提示注入进行审查 — 每个 Antfarm 工作流程在合并前都会针对提示注入攻击和恶意代理文件进行审查。
    
-   欢迎社区贡献 — 想要添加一个工作流？提交一个 PR。所有提交在发布前都经过仔细的安全审查。
    
-   默认透明 — 每个工作流都是纯 YAML 和 Markdown 格式。在安装之前，你可以确切地查看每个代理将会执行的操作。
    

监控运行情况、跟踪步骤进度并实时查看代理输出，使用：

[

![Image](https://pbs.twimg.com/media/HAvHHY5XwAAQi1Y?format=jpg&name=medium)



](https://x.com/ryancarson/article/2020931274219594107/media/2020927787561893888)

```
antfarm workflow run <id> <task>
```

```
antfarm workflow status <query>
```

```
antfarm workflow resume <run-id>
```

```
antfarm workflow install <id>
```

```
antfarm workflow uninstall <id>
```

```
install github.com/snarktank/antfarm
```

...并运行你的第一个工作流。我很想听听你的使用情况——哪些地方好用，哪些地方出问题，以及你希望看到哪些工作流。可以通过私信联系我，或者在 Antfarm 仓库。

我已经在构建可靠、可重复的代理式开发流程方面工作了一段时间了。

它始于 ai-dev-tasks（现在已有 7500 颗星）——一个用于获取 AI 代理一致输出的严密约束系统。当时的模型能力较弱，因此需要这些严密的约束。每一步都必须明确界定和检查。在我接受@clairevo 的采访后，GitHub 仓库变得异常火爆。

claire vo ![🖤](https://abs-0.twimg.com/emoji/v2/svg/1f5a4.svg) 

Distilled

的超受欢迎的 How I AI 剧集以及 3 部分 vibe 编码流程在 3 分钟以内完成。 如果你正在毫无结构地进行 YOLO 式编码，那就让他来救你 ![👇](https://abs-0.twimg.com/emoji/v2/svg/1f447.svg)

然后 Opus 4.5 和 Gemini 3 发布了，一切都变了。模型终于有足够的能力（主要）自主运行，因此

（刚刚获得了 9,800 星标）成为可能——一个自主代理循环，它会接收任务并执行直到完成。

人们似乎很喜欢 Ralph 指南，它在 X 上的观看量飙升至 180 万。

![Article cover image](https://pbs.twimg.com/media/G9-gtHmW0AE8pmK?format=jpg&name=medium)

让 Ralph 工作并部署代码的分步指南

每个人都在对 Ralph 赞不绝口。它是什么？ Ralph 是一个自主的 AI 编码循环，能在你睡觉时推出功能。 由@GeoffreyHuntley 创建并在他的原始帖子中宣布，它运行@AmpCode...

我意识到我需要把我学到的一切运用起来，组建一个我的 OpenClaw 能够管理的代理团队。但他们需要可重复、确定性的工作流以及 Ralph 循环模式——每次会话都有新的上下文，通过 git 进行记忆，自动重试。

所以我构建了

为我自己的需求，并决定开源它。我希望人们能提交带有新工作流的 PR。我们会在合并前审核每一个提交，检查安全性和提示注入问题，并且希望构建一个社区工作流库，供所有人使用。