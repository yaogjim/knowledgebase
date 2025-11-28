---
title: "2025-11-28_shao_meng_Anthropic_工程博客_构建长运行智能体的高效框架_Anthropic_最新工程博客探"
source: "https://x.com/shao__meng/status/1993832318977581405"
author:
  - "[[@shao__meng]]"
published: 2025-11-28
created: 2025-11-28
description:
tags:
  - "x"
  - "@shao__meng"
  - "anthropic"
  - "git"
---

# [Anthropic 工程博客] 构建长运行智能体的高效框架 Anthropic 最新工程博客探

**meng shao** @shao\_\_meng 2025-11-26

\[Anthropic 工程博客\] 构建长运行智能体的高效框架

Anthropic 最新工程博客探讨了如何为长运行智能体设计有效的“框架”，以应对复杂任务在多会话间的持续执行挑战。基于 Claude Agent SDK 实际经验，强调通过结构化环境和渐进式工作流程，让智能体像人类软件工程师一样，逐步推进项目，而非试图一蹴而就。

长运行智能体的核心挑战

长运行智能体目标是处理跨小时或数天的复杂任务，例如构建一个完整复杂的软件项目。但由于上下文窗口的容量限制，每个会话都像从零开始：智能体缺乏先前记忆，容易陷入“一次性完成”的陷阱——试图在单一会话中搞定整个项目，导致上下文耗尽、代码杂乱或文档缺失。其他常见问题包括：

· 过早宣告完成：后续智能体看到部分进展，就错误地标记任务结束。

· 状态恢复困难：智能体花大量时间猜测未完成工作，或在 buggy 环境中挣扎。

· 测试缺失：功能看似就位，但未通过端到端验证，隐藏潜在问题。

通过实验（如构建 200+ 功能的网页克隆项目）总结这些失败模式，并提供针对性解决方案，借鉴软件工程最佳实践，如 Git 版本控制和自动化测试。

提出的解决方案：双智能体框架与结构化环境

解决方案是引入“框架”——一个由提示、脚本和文件组成的系统，确保会话间状态持久化和干净交接。具体分为两个角色：

1\. 初始化智能体（Initializer Agent）：仅用于首轮会话，负责搭建初始环境。生成关键文件，包括：

· feature\_list.json：一个JSON格式的功能清单，列出所有任务（如“创建新聊天”），每个包含描述、步骤和初始“passes”状态（false）。JSON格式确保不可变性，防止后续编辑。

· claude-progress.txt：日志文件，记录动作和进展。

· init. sh：启动脚本，用于运行开发服务器、测试基础功能，减少后续设置开销。

初始化后，进行首次 Git 提交，形成干净基线。

2\. 编码智能体（Coding Agent）：后续会话专用，专注于渐进式进展。每个会话仅处理一个功能：

· 会话启动例程：检查目录（pwd）、审阅 Git 日志和进展文件、运行 init. sh 启动环境、验证核心测试。

· 工作流程：从 JSON 清单选一未完成功能，编码、提交描述性 Git 变更、更新 “passes” 状态（仅在通过测试后），并记录日志。

· 强调“干净状态”（clean state）：结束时，代码须无bug、文档齐全、可直接合并到主分支。

关键实践与工具集成

· 功能清单与 Git：JSON 清单防止“过早完成”，Git 提供回滚和历史追踪。实验显示，相比 Markdown，JSON 减少了不当修改。

· 端到端测试：集成浏览器自动化工具（如 Puppeteer MCP 服务器），模拟人类操作（如点击模态框、截图验证）。这捕捉代码审查忽略的交互 bug，但文章也指出局限，如原生浏览器元素的处理。

· 提示策略：初始化和编码提示不同——前者聚焦搭建，后者强调单一功能和验证。使用强约束语言（如“绝不编辑测试”）规避失败。

· 失败模式表格：文章附表总结问题（如“设置混淆”）及应对（如标准化脚本），便于实际应用。

结论与展望

Anthropic 的经验证明，这种框架能显著提升长运行智能体的可靠性：从混乱的“一击即溃”转向工程化的持续迭代。关键启示是借用人类工程实践（如版本控制、测试驱动开发），结合 AI 的自动化潜力。从简单项目起步，审视失败模式，并扩展到多智能体系统（如专职测试智能体）。未来方向可以泛化到其他领域，如科学研究或财务建模，探索更复杂的协作架构。

博客地址：

https://anthropic.com/engineering/effective-harnesses-for-long-running-agents…

> 2025-11-26
> 
> New on the Anthropic Engineering Blog: Long-running AI agents still face challenges working across many context windows.
> 
> We looked to human engineers for inspiration in creating a more effective agent harness. https://anthropic.com/engineering/effective-harnesses-for-long-running-agents…
> 
> Anthropic 工程博客最新发布：长期运行的 AI 智能体在跨越多重上下文窗口协作时仍面临挑战。
> 
> 我们从人类工程师那里汲取灵感，打造更高效的智能体管理工具。https : //anthropic.com/engineering/effective-harnesses-for-long-running-agents …
> 
> ![Image](https://pbs.twimg.com/media/G6uD6C6aEAAAsuS?format=jpg&name=large)