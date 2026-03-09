---
title: "2026-03-09_Elvis_Elvis_OpenClaw_CodexClaudeCode_智能体集群_一人开发"
source: "https://x.com/elvissun/status/2025920521871716562"
author:
  - "[[@Elvis]]"
published: 2026-03-09
created: 2026-03-09
description:
tags:
  - "#341"
  - "x"
  - "@Elvis"
  - "codex"
---

# Elvis # OpenClaw + CodexClaudeCode 智能体集群：一人开发

**Elvis**

# OpenClaw + Codex/ClaudeCode 智能体集群：一人开发团队 \[完整设置\]

我不再直接使用 Codex 或 Claude Code。

我使用 OpenClaw 作为我的编排层。我的编排器 Zoe 生成代理、编写它们的提示词、为每个任务选择合适的模型、监控进度，并在 PR 准备合并时通过 Telegram 给我发消息。

过去4周的证明要点

\- 一天 94 次提交 。我最有成效的一天 - 我打了 3 个客户电话，一次也没打开过编辑器。平均每天大约 50 次提交。

\- 30 分钟内 7 个 PR。从想法到生产的速度极快，因为编码和验证大多是自动化的。

\- 提交 → 月经常性收入 : 我在构建一个真实的 B2B SaaS 时使用了这个——将其与创始人主导的销售相结合，以在当天交付大多数功能请求。速度将潜在客户转化为付费客户。

before Jan: CC/codex only | after Jan: Openclaw orchestrates CC/codex

我的 Git 历史看起来就像我刚雇了一个开发团队。实际上，只是我从管理 Claude 代码，转变为管理一个 OpenClaw 代理，而这个 OpenClaw 代理又管理着一支由其他 Claude 代码和 Codex 代理组成的舰队。

成功率：系统几乎能一次性完成所有中小型任务，无需任何干预。

费用：Claude 约 100 美元/月，Codex 90 美元/月，但你可以以 20 美元起价。

这就是为什么这种方法比直接使用 Codex 或 Claude Code 更有效：

Codex 和 Claude Code 对您的业务了解很少。

他们看到代码。他们看不到你业务的全貌。

OpenClaw 改变了这一格局。它在你和所有代理之间充当编排层——它将我所有的业务上下文（客户数据、会议记录、过往决策、成功经验、失败教训）存储在我的 Obsidian 库中，并将历史上下文转化为针对每个编码代理的精准提示词。代理专注于代码，编排器则处于高层战略层面。

系统的高层工作原理如下：

上周 Stripe 发表了关于他们名为“Minions”的后台代理系统的文章——由集中式编排层支持的并行编码代理。我意外地构建了同样的系统，但它在我的 Mac mini 上本地运行。

在我告诉你如何设置这个之前，你应该知道为什么需要一个代理编排器。

## 为什么一个 AI 无法同时完成两者

上下文窗口是 零和 。你必须选择什么内容进入。

用代码填充它 → 没有业务背景的空间。用客户历史填充它 → 没有代码库的空间。这就是为什么两层系统能发挥作用：每个 AI 都恰好加载了它所需要的内容。

OpenClaw 和 Codex 具有截然不同的背景:

通过上下文实现专业化，而非通过不同的模型。

## 完整的8步工作流程

让我讲解一下上周的一个真实例子。

步骤 1: 客户请求 → 与 Zoe 进行范围确定

我与一位代理客户进行了通话。他们希望在整个团队中复用他们已经设置好的配置。

通话结束后，我和 Zoe 讨论了这个请求。因为我所有的会议记录都会自动同步到我的 Obsidian 库，我这边不需要任何解释。我们一起确定了这个功能的范围，并确定了一个模板系统，这个系统可以让他们保存和编辑现有的配置。

然后佐伊做三件事：

1.  充值余额以立即解除客户限制 — 她拥有管理员 API 访问权限
2.  从生产数据库拉取客户配置 — 她拥有生产数据库的只读访问权限（我的 codex 代理绝不会有此权限），以检索他们现有的设置，该设置会被包含在提示中
3.  生成一个 Codex 代理——附带包含所有上下文的详细提示词

步骤 2: 生成代理

每个代理拥有自己的工作树（隔离分支）和 tmux 会话：

```bash
# Create worktree + spawn agent
git worktree add ../feat-custom-templates -b feat/custom-templates origin/main
cd ../feat-custom-templates && pnpm install

tmux new-session -d -s "codex-templates" \
  -c "/Users/elvis/Documents/GitHub/medialyst-worktrees/feat-custom-templates" \
  "$HOME/.codex-agent/run-agent.sh templates gpt-5.3-codex high"
```

该代理在一个 tmux 会话中运行，通过脚本进行完整的终端日志记录。

以下是我们启动代理的方式：

```bash
# Codex
codex --model gpt-5.3-codex \
  -c "model_reasoning_effort=high" \
  --dangerously-bypass-approvals-and-sandbox \
  "Your prompt here"

# Claude Code  
claude --model claude-opus-4.5 \
  --dangerously-skip-permissions \
  -p "Your prompt here"
```

我过去常用 codex exec 或 Claude -p，但最近切换到了 tmux：

tmux 之所以更好，是因为任务中途重定向非常强大。代理方向错误？不要杀掉它：

```bash
# Wrong approach:
tmux send-keys -t codex-templates "Stop. Focus on the API layer first, not the UI." Enter

# Needs more context:
tmux send-keys -t codex-templates "The schema is in src/types/template.ts. Use that." Enter
```

该任务在 .clawdbot/active-tasks.json 中被跟踪：

```json
{
  "id": "feat-custom-templates",
  "tmuxSession": "codex-templates",
  "agent": "codex",
  "description": "Custom email templates for agency customer",
  "repo": "medialyst",
  "worktree": "feat-custom-templates",
  "branch": "feat/custom-templates",
  "startedAt": 1740268800000,
  "status": "running",
  "notifyOnComplete": true
}
```

完成后，它会更新 PR 编号和检查信息。(更多内容见步骤 5)

```json
{
  "status": "done",
  "pr": 341,
  "completedAt": 1740275400000,
  "checks": {
 "prCreated": true,
 "ciPassed": true,
 "claudeReviewPassed": true,
 "geminiReviewPassed": true
  },
  "note": "All checks passed. Ready to merge."
}
```

步骤 3：循环监控

一个 cron 任务每 10 分钟运行一次，以照看所有代理。这基本上相当于一个改进版的 Ralph Loop，稍后再详细介绍。

但它不会直接轮询代理——那样会很昂贵。相反，它会运行一个脚本，该脚本读取 JSON 注册表并检查：

```bash
.clawdbot/check-agents.sh
```

该脚本是 100%确定性的，并且极其 token 高效：

检查 tmux 会话是否存活 检查已跟踪分支上的开放拉取请求 通过 gh CLI 检查 CI 状态 自动重新生成失败的代理（最多 3 次尝试），如果 CI 失败或关键审查反馈 仅在需要人工关注时发出警报

我没有在监视终端。系统会告诉我什么时候该查看。

步骤 4: Agent 创建拉取请求

代理提交、推送并通过 \`gh pr create --fill\` 打开一个 PR。此时我不会收到通知——仅一个 PR 还未完成。

完成标准（非常重要，您的代理需知晓这一点）：

拉取请求已创建 分支已同步到主分支（无合并冲突） CI 通过（Lint、类型检查、单元测试、端到端测试） Codex 审核通过 Claude 代码审查通过 Gemini 审核通过 包含截图（如果 UI 有变更）

步骤5: 自动化代码评审

每个 PR 都会被三个 AI 模型审查。它们会发现不同的问题：

- Codex Reviewer — 在边缘情况处理方面表现出色。进行最全面的审查。能够捕捉逻辑错误、遗漏的错误处理以及竞态条件。误报率非常低。
- Gemini 代码辅助评审器 — 免费且极其有用。能发现安全问题、其他代理程序遗漏的可扩展性问题，并提出具体修复方案。安装起来毫不费力。
- Claude 代码审查员 — 大多没用 - 往往过于谨慎。很多“考虑添加...”的建议通常都是过度设计的。除非标为关键，否则我都会跳过所有内容。它很少能自己发现关键问题，但会验证其他审查员指出的问题。

这三条评论都直接发表在 PR 上。

步骤 6：自动化测试

我们的 CI 流水线运行大量的自动化测试：

Lint 和 TypeScript 检查 单元测试 端到端测试 对与生产环境相同的预览环境运行 Playwright 测试

我上周新增了一条规则：如果 PR 修改了任何 UI，必须在 PR 描述中包含一张截图，否则 CI 会失败。这极大地缩短了审查时间——我无需点击预览即可确切看到哪些内容发生了变化。

步骤 7：人工审核

现在我收到了 Telegram 的通知：“PR #341 准备好进行审核。”

至此：

CI 通过 三名 AI 评审员批准了代码 截图显示了 UI 的变化 所有边界情况都在评审意见中被记录

我的代码审查需要 5-10 分钟。很多 PR 我都不看代码就合并了——截图里已经显示了我需要的所有信息。

步骤8：合并

PR 合并。每日 cron 任务清理孤立的工作树和任务注册表 JSON。

## 拉尔夫循环 V2

这本质上是 Ralph 循环，但更好。

Ralph 循环从内存中提取上下文，生成输出，评估结果，保存学习成果。但大多数实现都会在每个循环中使用相同的提示词。提炼出的学习成果会提升未来的检索效果，而提示词本身则保持不变。

我们的系统有所不同。当代理（agent）失败时，佐伊（Zoe）不会仅仅用相同的提示重新生成它。她会结合完整的业务背景审视失败情况，并找出如何解决它。

- Agent 上下文用完了？“只关注这三个文件。”
- 业务员走错方向了？“停！客户想要的是 X，不是 Y。这是他们在会议上说的。”
- 座席需要澄清吗？“这是客户的邮箱和他们公司的业务。”

佐伊全程跟进代理完成任务。她掌握着代理所不具备的背景信息——客户历史、会议记录、我们之前的尝试以及失败原因。她利用这些背景信息，在每次重试时生成更有效的提示词。

但她也不会等我分配任务。她会主动找活干：

- 上午: 扫描哨兵 → 发现 4 个新错误 → 生成 4 个代理进行调查和修复
- 会议结束后： 扫描会议记录 → 标记出客户提到的 3 个功能需求 → 生成 3 个 Codex 代理
- 晚上： 扫描 git 日志 → 启动 Claude Code 以更新变更日志和客户文档

客户通话后我去散步。回到 Telegram：“7 个 PR 等待审核。3 个功能，4 个 bug 修复。”

当代理成功时，该模式会被记录。"这种提示词结构适用于账单功能。""Codex 需要预先提供类型定义。""始终包含测试文件路径。"

奖励信号包括：CI 通过、所有三次代码审查通过、人工合并。任何失败都会触发循环。随着时间的推移，Zoe 能写出更好的提示词，因为她记得哪些内容被发布了。

## 选择合适的代理

并非所有编码代理都一样。快速参考：

Codex 是我的主力工具。后端逻辑、复杂的 bug、多文件重构，任何需要在代码库中进行推理的工作。它速度较慢但很彻底。我 90%的任务都使用它。

Claude Code 在前端工作方面更快、更好。它的权限问题也更少，因此非常适合 Git 操作。（我过去更多地使用它来处理日常工作，但现在 Codex 5.3 显然更好、更快）

Gemini 拥有一项不同的超能力——设计感。为了打造美观的用户界面，我会先让 Gemini 生成 HTML/CSS 规范，然后将其交给 Claude Code 在我们的组件系统中实现。Gemini 设计，Claude 构建。

佐伊为每个任务选择合适的代理，并在它们之间路由输出。一个计费系统漏洞被路由到 Codex。一个按钮样式修复被路由到 Claude Code。一个新的仪表盘设计从 Gemini 开始。

## 如何设置这个

复制这整篇文章到 OpenClaw 中，并告诉它：“为我的代码库实现这个智能体群体设置。”

它会读取架构，创建脚本，设置目录结构，并配置 cron 监控。10 分钟内完成。

没有课程卖给你。

## 没人预料到的瓶颈

这就是我现在遇到的瓶颈：RAM。

每个代理都需要自己的工作树。每个工作树都需要自己的 \`node\_modules\`。每个代理都会执行构建、类型检查和测试。五个代理同时运行意味着五个并行的 TypeScript 编译器、五个测试运行器以及五组加载到内存中的依赖项。

我的 Mac Mini 配备 16GB 内存，最多只能支持 4-5 个代理，否则就会开始交换（虚拟内存）——而且我得庆幸它们不会同时尝试构建。

所以我买了一台配备 128GB 内存的 Mac Studio M4 max（3500 美元）来驱动这个系统。它将于 3 月底到货，我会分享它是否值得。

## 接下来：一人百万美元公司

我们将看到大量单人百万美元公司从2026年开始涌现。对于那些懂得如何构建递归自改进代理的人来说，杠杆作用非常巨大。

这就是它的样子：一个 AI 编排器，作为你自己的延伸（就像 Zoe 对我而言那样），将工作委托给处理不同业务职能的专业代理。工程、客户支持、运维、营销。每个代理都专注于自己擅长的领域。你保持如激光般的精准专注和完全的控制。

新一代企业家不会雇佣一个10人的团队去做一个拥有合适系统的人能完成的工作。他们会这样构建——保持小规模、快速行动、每日交付。

现在有太多 AI 生成的垃圾内容了。围绕 AI 代理和“任务控制”有太多炒作，却没有真正做出任何有用的东西。花哨的演示，却没有实际的现实世界价值。

我正在尝试做相反的事情：少一些炒作，多一些关于构建实际业务的文档。真实的客户、真实的收入、提交到生产环境的真实代码提交，以及真实的损失。

我在做什么项目？Agentic PR——一家一人公司，挑战企业 PR 领域的现有巨头。这些代理服务帮助初创企业无需每月支付 1 万美元的服务费即可获得媒体报道。

如果你想看看我能把这件事做到什么程度，那就继续关注吧。