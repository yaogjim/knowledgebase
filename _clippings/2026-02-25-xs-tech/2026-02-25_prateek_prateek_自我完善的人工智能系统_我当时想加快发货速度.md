---
title: "2026-02-25_prateek_prateek_自我完善的人工智能系统_我当时想加快发货速度"
source: "https://x.com/agent_wrapper/status/2025986105485733945"
author:
  - "[[@prateek]]"
published: 2026-02-25
created: 2026-02-25
description:
tags:
  - "#1121"
  - "#125"
  - "x"
  - "@prateek"
---

# prateek # 自我完善的人工智能系统 我当时想加快发货速度。

**prateek**

# 自我完善的人工智能系统

我当时想加快发货速度。

我当时有一堆代码库，一堆待开发的功能，但一天的时间根本不够用。所以我开始并行运行多个 AI 编码代理——给每个代理分配任务，让它们编写代码，审查 PR，合并，然后重复这个过程。一开始我只有两三个。然后是五个。然后是十个。

那些开发人员速度很快，问题出在我身上。我跟不上他们的节奏。我得检查持续集成是否通过，阅读评审意见，还要把错误复制粘贴回去。我从写代码变成了照顾那些写代码的开发人员。这根本无法扩展。

所以我写了一些 Bash 脚本来实现自动化协调——大约 2500 行代码，用于管理 tmux 会话、git 工作树和标签页切换。每个代理都有自己独立的 tmux 会话和工作树。编排器可以启动这些代理，查看它们的运行情况，将 CI 失败转发回去，并且让我只需说“带我到 PR #1121 的标签页”就能在不同会话之间切换。它勉强能用。

然后我让代理程序直接运行这些 bash 脚本。它们构建了第一个版本的编排器。第一个版本管理着构建第二个版本的代理程序。而第二个版本此后一直在自我改进。

[

![Image](https://pbs.twimg.com/media/HB27wXlbgAAmysl?format=jpg&name=medium)


](/agent_wrapper/article/2025986105485733945/media/2025981847025713152)

From bash scripts to self-improving system

最终成果：40,000 行 TypeScript 代码、17 个插件、3,288 个测试——仅用 8 天时间构建完成，其中大部分由系统协调的智能体完成。每次提交都带有 Git 尾部，明确标识出是哪个 AI 模型编写的。这样一来，人类和智能体的工作就一目了然了。 我们已经将其开源：Agent Orchestrator（

[github.com/ComposioHQ/agent-orchestrator](http://github.com/ComposioHQ/agent-orchestrator)

）。 关键在于理解：编排器本身就是一个 AI 代理，而不是仪表盘、定时任务或轮询 GitHub 的脚本。它是一个代理——它会读取你的代码库，理解你的待办事项列表，决定如何将一个功能分解成可并行化的任务，将每个任务分配给一个编码代理，并监控它们的进度。当持续集成 (CI) 失败时，它会将失败信息注入到代理会话中——代理会读取日志并修复问题。当收到代码审查意见时，它会将意见连同上下文一起路由到正确的代理会话。整个过程无需人工干预。 这正是它与所有“并行运行代理”设置的不同之处。管理代理的程序本身就具有智能。

[

![Image](https://pbs.twimg.com/media/HB28HOUbcAA50NX?format=jpg&name=medium)


](/agent_wrapper/article/2025986105485733945/media/2025982239675478016)

## 

人工智能辅助编码的真正瓶颈

大多数人对人工智能编码代理问题的理解是错误的。代理本身会编码，这不是瓶颈所在，瓶颈在于你。

你创建了五个任务，去喝杯咖啡，20 分钟后回来，现在你只是在刷新 GitHub 标签页——等待 PR、检查 CI、阅读代码审查意见。恭喜，你实现了工程自动化，并将其替换成了项目管理。糟糕的项目管理。

协调代理会取代你在这个循环中的位置。它不是通过脚本实现的，而是一个真正的 AI 代理，它掌握着每个活跃会话、每个未完成的 PR、每次 CI 运行的上下文信息。它会追踪所有信息，监控故障，将审查意见转发给编码代理，并且只有在真正需要人工决策时才会通知你。一旦瓶颈——你的注意力——消失，问题就会迅速累积。

你打开仪表盘查看状态。但编排代理已经在运行了——它已经检查了你所有的工作流，并告诉你：“这个 PR 阻塞了其他三个任务，这个 CI 失败是因为测试不稳定，而这条评审意见才是真正重要的。”它不是在向你展示数据，而是在为你做出决策。

[

![Image](https://pbs.twimg.com/media/HB29MSUa4AARMkw?format=jpg&name=medium)


](/agent_wrapper/article/2025986105485733945/media/2025983426160156672)

[

![Image](https://pbs.twimg.com/media/HB29AxhawAAFPx4?format=jpg&name=medium)


](/agent_wrapper/article/2025986105485733945/media/2025983228377743360)

另一点也很重要：即插即用。不同的代理运行时？不同的问题跟踪器？不同的通知渠道？统统都能替换。编排器不在乎你用的是 Claude Code 还是 Aider，tmux 还是 Docker，GitHub 还是 Linear。八个插件槽位，全部可替换。

## 

时间线

人们看到“8天4万行”就以为我遁世隐居了。我还有一份正职工作。这其中可能只有大约3天是真正集中精力完成的，其余时间都是代理人填补的。

[

![Image](https://pbs.twimg.com/media/HB29ic6aIAANudb?format=jpg&name=medium)


](/agent_wrapper/article/2025986105485733945/media/2025983806960967680)

模式很简单：睡前设置会话，代理人通宵工作，早上上班前进行审核和合并，设置新的会话，重复此过程。

最精彩的一天：2 月 14 日星期六。一天之内合并了 27 个 PR。整个平台都上线了——核心服务、CLI、Web 控制面板、全部 17 个插件以及 npm 发布。我审核和合并 PR 的速度比阅读的速度还快，但每个 PR 都事先通过了持续集成和自动化代码审查。

[

![Image](https://pbs.twimg.com/media/HB2-L03boAIXTT8?format=jpg&name=medium)


](/agent_wrapper/article/2025986105485733945/media/2025984517765570562)

Daily activity — commits and PRs merged over 8 days

## 

哪些模型做了什么

每次提交都会通过 git trailers 跟踪模型：

[

![Image](https://pbs.twimg.com/media/HB2-SmdbgAAtq_X?format=jpg&name=medium)


](/agent_wrapper/article/2025986105485733945/media/2025984634157498368)

总共提交次数超过 722 次，是因为有些提交是由一个模型编写，然后由另一个模型审核/修复的。Opus 4.6 处理了最棘手的部分——复杂的架构和跨包集成。Sonnet 则处理了大量工作——插件实现、测试和文档。

## 

完全自动化的代码审查：700 条评论，1% 为人工干预。

代理商不会只是编写代码然后就把它扔出去。这里有一个完整的自动化审查流程：

1.  代理创建 PR 并推送代码
 
2.  Cursor Bugbot 会自动审核并发布内联评论
 
3.  代理读取评论，修复代码，再次推送
 
4.  Bugbot 重新评测
 

[

![Image](https://pbs.twimg.com/media/HB2-hhlbUAA4nlZ?format=jpg&name=medium)


](/agent_wrapper/article/2025986105485733945/media/2025984890546900992)

700 条自动代码审查评论。Bugbot 发现了一些真正的问题——通过 exec() 注入 shell、路径遍历、未闭合的区间以及缺失的空值检查。代理程序立即修复了约 68% 的问题，将约 7% 的问题解释为有意为之，并将约 4% 的问题推迟到未来的 PR 中处理。

[

![Image](https://pbs.twimg.com/media/HB2-l8kbUAAlobN?format=jpg&name=medium)


](/agent_wrapper/article/2025986105485733945/media/2025984966509940736)

Code review pipeline — from agent PR to ship

## 

AO-58 的故事

最典型的例子是 PR #125，一个仪表盘重新设计。它经历了 12 个 CI 失败→修复的循环 。每次，代理都会获取失败输出，诊断问题（类型错误、代码检查失败、测试回归），然后推送修复程序。整个过程无需人工干预。

12轮射击。无人为干预。出厂时已清洁。

[

![Image](https://pbs.twimg.com/media/HB2-uy2aoAE7fJD?format=jpg&name=medium)


](/agent_wrapper/article/2025986105485733945/media/2025985118519861249)

9 个分支机构的 41 个 CI 故障最终均由代理程序自行纠正。总体 CI 成功率：84.6%。

[

![Image](https://pbs.twimg.com/media/HB2-yrnasAA-gy-?format=jpg&name=medium)


](/agent_wrapper/article/2025986105485733945/media/2025985185297379328)

## 

建筑学

该编曲器使用插件系统，共有 8 个可互换的插槽：

[

![Image](https://pbs.twimg.com/media/HB2-3nybUAEp3ZE?format=jpg&name=medium)


](/agent_wrapper/article/2025986105485733945/media/2025985270169161729)

会话生命周期：

1.  Tracker 拉取了一个 issue（GitHub 或 Linear）。
 
2.  工作区会创建一个独立的工作树或克隆。
 
3.  运行时启动 tmux 会话或进程
 
4.  代理 （Claude Code、Aider 等）自主运行
 
5.  终端允许您通过 iTerm2 或 Web 控制面板进行实时观察。
 
6.  SCM 创建 PR 并为其添加上下文信息。
 
7.  当 CI 故障或收到评论时， 反应会自动重新启动代理。
 
8.  通知器仅在需要人工判断时才会向您发送提醒。
 

[

![Image](https://pbs.twimg.com/media/HB2-87oagAA3_PI?format=jpg&name=medium)


](/agent_wrapper/article/2025986105485733945/media/2025985361395220480)

Session lifecycle — from issue to merged PR

不用 tmux？那就用进程运行时。不用 GitHub？那就用 Linear。不用 Claude Code？那就用 Aider 或 Codex。任何组件都可以替换。

## 

自愈式 CI：能够修复自身故障的代理

最实用的功能：自动回复 GitHub 事件：

yaml

```yaml
reactions:
  ci_failed:
 action: spawn_agent
 prompt: "CI failed on this PR. Read the failure logs and fix the issues."

  changes_requested:
 action: spawn_agent
 prompt: "Review comments have been posted. Address each comment and push fixes."

  approved:
 action: notify
 channel: slack
 message: "PR approved and ready to merge."
```

CI 失败？代理程序检测到。审核人员提出修改意见？代理程序阅读评论并修复代码。PR 获得批准？你会收到 Slack 通知。这就是这 41 个 CI 失败是如何自动纠正的——反应系统会自动将失败转发给代理程序。

## 

起源：人工智能代理构建自己的编排器

我同时运行了 30 个代理程序来管理 Agent Orchestrator。它们负责构建 TypeScript 的替代版本，而我则使用 bash 脚本版本来管理它们。被构建的程序本身也在管理自身的构建过程。

我实际做的是：

- 架构决策（插件槽位、配置模式、会话生命周期）
 
- 生成会话并分配问题
 
- 审核 PR（主要是架构方面的，而不是逐行审核）
 
- 解决跨代理冲突（两个代理编辑同一个文件）
 
- 判断性决策（拒绝这种方法，尝试那种方法）
 

特工们做了什么：

- 所有实现（40000 行 TypeScript 代码）
 
- 所有测试（3,288 个测试用例）
 
- 所有 PR 创建（102 个 PR 中的 86 个）
 
- 所有评论意见的修正
 
- 所有 CI 故障解决
 

我从未直接将代码提交到功能分支。每一行代码都是通过 PR（Pull Request，拉取请求）提交的。

[

![Image](https://pbs.twimg.com/media/HB2_PnubYAAu2za?format=jpg&name=medium)


](/agent_wrapper/article/2025986105485733945/media/2025985682469249024)

## 

活动检测

其中一个比较棘手的问题：如何在不询问的情况下弄清楚代理人实际在做什么。

Claude Code 在每个会话期间都会写入结构化的 JSONL 事件文件。编排器不会依赖代理进行自我报告（代理会撒谎，或者至少会感到困惑），而是直接读取这些文件：

- 代理是否正在主动生成令牌？
 
- 是否正在等待工具执行？
 
- 它处于空闲状态吗？
 
- 结束了吗？
 

agent-claude-code 插件能够解析 Claude 的会话文件。未来的 agent-aider 插件将读取 Aider 的对应文件。

## 

网络仪表盘

Next.js 15，采用服务器发送事件 (Server-Sent Events) 实现实时更新，无需轮询。

- 关注区域 ——按需要您关注的内容分组的会话（持续改进失败、等待审核、运行正常）
 
- 实时终端 ——浏览器中的 xterm.js，实时显示代理的实际终端输出
 
- 会话详情 ——当前正在编辑的文件、最近的提交、PR 状态、CI 状态
 
- 配置发现 ——自动查找您的 ao.config.yaml 文件并显示可用会话
 

## 

自我改进的人工智能循环

每次代理会话都会产生信号。哪些提示促成了干净的 PR？哪些提示导致了 12 次 CI 失败循环？哪些模式导致了合并冲突？

大多数代理设置都会丢弃这个信号。会话结束，下一个会话从零开始。

Agent Orchestrator 拥有一个自我改进系统（ao-52，它本身也是由一个代理构建的），该系统会记录性能、跟踪会话结果并进行回顾。它能够学习哪些任务一次就能成功，哪些任务需要更严格的约束。

代理构建功能 → 协调器观察哪些功能有效 → 调整其管理未来会话的方式 → 代理构建更好的功能。如此循环往复。

由于代理构建了协调器，协调器又提升了代理的效率，而这些代理又不断改进协调器——这是一个递归过程。该工具通过其管理的代理不断改进自身。

我认为这就是为什么编排比任何单个代理的改进都更重要的原因。瓶颈不在于“Claude Code 的 TypeScript 水平有多高”，而在于“一个系统在部署、观察和改进数十个并行工作的代理方面能达到多高的性能”。这个瓶颈要高得多，而且每次循环运行都会提升。

## 

下一步：迈向完全自主的软件工程

随时随地与您的代理沟通。 目前您需要坐在办公桌前。但您应该能够在散步时通过 Telegram 或 Slack 与调度员联系——查看状态、批准合并、重新分配代理。

更及时的会话中反馈至关重要。 智能体容易偏离目标，开始解决错误的问题，过度设计简单的解决方案，或者陷入无尽的探索。组织者需要对照最初的目标检查智能体的工作，并在他们浪费 20 分钟走错方向之前及时纠正。

自动升级。 代理无法解决问题？升级至协调器。协调器需要判断？升级至您。您只会看到真正需要人工决策的问题。其他所有问题都会自动解决。

除此之外：还包括用于自动解决并行代理之间冲突的协调器、用于长期运行分支的自动变基功能、用于云部署的 Docker/K8s 运行时，以及用于社区贡献的插件市场。

## 

试试看

狂欢

```bash
git clone https://github.com/ComposioHQ/agent-orchestrator.git
cd agent-orchestrator
pnpm install && pnpm build
ao init --tracker github --agent claude-code --runtime tmux
ao start
```

启动编排器，打开控制面板，然后与它交互。告诉它要构建什么。剩下的事情它都会处理——生成代理、创建 PR、监控 CI、转发评审意见等等。你只需要做出决策。

我们正在寻找贡献者：新的插件（代理运行时、跟踪器、通知器）、Docker/K8s 运行时、用于自动冲突检测的协调器以及更好的升级规则。

代码库已上线：

[github.com/ComposioHQ/agent-orchestrator](//github.com/ComposioHQ/agent-orchestrator)

完整指标报告：

[github.com/ComposioHQ/agent-orchestrator/releases/tag/metrics-v1](//github.com/ComposioHQ/agent-orchestrator/releases/tag/metrics-v1)

构建数据的交互式可视化：

[pkarnal.com/ao-labs/](//pkarnal.com/ao-labs/)

我在 Composio 负责开发 Agent Orchestrator 和开发者工具层 。如果你对开发自我改进的 AI 系统感兴趣——我们在旧金山和班加罗尔都有招聘：

[jobs.ashbyhq.com/composio](//jobs.ashbyhq.com/composio)