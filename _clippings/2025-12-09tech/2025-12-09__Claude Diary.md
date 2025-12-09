---
title: "Claude Diary"
source: "https://rlancemartin.github.io/2025/12/01/claude_diary/"
author:
date: "2025-12-09T16:06:34+08:00"
created: 2025-12-09
description: "Creating a memory system for Claude Code."
tags:
---
[Lance Martin](https://x.com/RLanceMartin)

人类通过经验不断精进技能并形成偏好。但许多 AI 智能体缺乏这种 [持续学习](https://www.dwarkesh.com/p/timelines-june-2025) 的能力。我开发了一款名为 [Claude 日记](https://github.com/rlancemartin/claude-diary) 的 [插件](https://code.claude.com/docs/en/plugins) ，让 Claude 法典能够从经验中学习并更新自身记忆。相关代码可 [在此](https://github.com/rlancemartin/claude-diary) 查阅。

![](https://rlancemartin.github.io/assets/claude_diary.png)

## Agent Memory

Sumers 等人（2023）在 [CoALA 论文](https://arxiv.org/pdf/2309.02427) 中提出了一个智能体记忆框架，包含“程序性记忆”（如提示指令）和“情景记忆”（如过往行动）。

Claude 法典将其系统指令存储于 `CLAUDE.md` 文件中，会话日志则保存至 `~/.claude/projects/` 目录。然而，我们该如何将日志中的过往操作转化为可纳入指令的持久性通用规则呢？

Park 等人（2023）发表的 [生成式智能体论文](https://arxiv.org/pdf/2304.03442) 展示了一种实现路径。其智能体通过反思机制，将过往行为整合成指导未来规划与决策的通用准则。

![](https://rlancemartin.github.io/assets/gen_agents.png)

近期， [张等人（2025）](https://arxiv.org/pdf/2510.04618) 采用类似的"生长与精炼"智能体指令方法：通过生成器产生推理轨迹，反射器从成功与失败中提取经验，再由整合者将洞见融入结构化更新中。

![](https://rlancemartin.github.io/assets/ace.png)

在 [近期访谈](https://www.youtube.com/watch?v=IDSAMqip6ms&t=352s) 中，吴猫（Claude Code 产品负责人）提到 Anthropic 部分员工会采用类似模式：从 Claude Code 会话中生成日记条目，通过反思来识别行为模式。

## 实施 Claude 日记

我采用这种基于反思的方法与 Claude Code 协作，让 Claude 从对话记录中提炼日记条目，并通过整合收集的条目进行反思，最终更新 `CLAUDE.md` 文件。

![](https://rlancemartin.github.io/assets/claude_diary_flow.png)

#### 用什么来创建日记条目？

我最初让 Claude Code 解析 JSONL 会话日志，但这需要调用数十次 bash 工具。我决定直接利用已载入 Claude Code 会话的上下文来生成日记条目。

#### 日记中应记录什么？

我创建了一个 `/diary` [斜杠命令](https://code.claude.com/docs/en/slash-commands) ，用于提示 Claude Code 记录关键会话细节，包括完成事项、设计决策、遇到的挑战、用户偏好和 PR 反馈。日记条目将保存至：

`~/.claude/memory/diary/YYYY-MM-DD-session-N.md`

#### 何时创建日记条目？

我采用混合方式创建日记条目：手动调用 `/diary` 指令和/或通过 [PreCompact 钩子](https://code.claude.com/docs/en/hooks-guide#hook-events-overview) 自动触发。这样既能自主选择记录时机，又能在使用压缩功能的长时间会话中自动生成日记。

#### 倒影中应捕捉什么？

`/reflect` 指令指示 Claude 代码分析日记条目并生成 CLAUDE.md 更新。它会读取 CLAUDE.md 文件，检查日记条目中的规则违规情况，并强化薄弱规则。同时还会跨日记条目扫描以识别重复出现的模式。

由于 `CLAUDE.md` 文件会在每次会话时加载，通过反思提出的更新内容会以单行项目符号的形式呈现。反思过程会将分析结果保存，并自动用综合规则更新 CLAUDE.md 文件。反思内容保存至：

`~/.claude/memory/reflections/YYYY-MM-reflection-N.md`

#### 如何追踪已处理的条目？

`processed.log` 文件用于防止日记条目被重复分析。反思命令会优先检查此日志文件。该日志保存于：

`~/.claude/memory/reflections/processed.log`

#### 何时进行反思？

我保留了手动反思功能，因为它会直接更新 CLAUDE.md 文件。我希望在将拟议的更新写入 CLAUDE.md 文件之前先进行审阅。

#### 需要更新哪些记忆文件？

我只让 Claude 更新其用户级文件 `~/.claude/CLAUDE.md` ，因为日记中捕捉到的许多模式（提交规范、测试方法、代码质量）具有普适性。

## Examples

过去一个月我一直在使用 Claude Diary。只需在需要记录的对话中运行 `diary` 命令，然后定期执行 `reflect` 来更新我的 `CLAUDE.md` 文件。以下是我发现 Claude Diary 特别有用的几个场景：

**PR 审核反馈** ：PR 评论（可通过 Claude Code 的 `pr-comments` 命令加载）是更新 Claude Code 记忆的重要反馈来源。

**Git 工作流** ：该系统擅长捕捉 Git 工作流中展现的偏好——从原子化提交和分支命名规范，到提交信息的格式化风格。

**测试实践** ：反思发现了一些模式，例如先运行针对性测试以快速获得反馈，然后执行全面测试套件，并使用专门的测试库。

**代码质量** ：系统学会了规避反模式，例如文件与包目录之间的命名冲突、重构后遗留过时目录以及不必要的冗长代码。

**智能体设计** ：在 AI 智能体工作中，反思总结出对令牌效率的偏好，倾向于采用单智能体委派模式而非过早并行化，并通过文件系统实现上下文卸载。

**自我修正** ：有时 CLAUDE.md 中的规则需要强化；该系统非常擅长发现 Claude 未遵循指令的情况并加以纠正。

## Conclusion

《克劳德日记》只是一个简单的尝试，旨在将原始克劳德会话转换为 `CLAUDE.md` 中的记忆更新。这些命令只是提示词，便于修改。我虽然限制了自动化程度，但通过钩子函数可以轻松实现任何命令的进一步自动化。正如 [此处](https://github.com/rlancemartin/claude-diary?tab=readme-ov-file#future-work) 所述，该项目还有很大的改进空间。代码可通过克劳德代码插件 [此处](https://github.com/rlancemartin/claude-diary) 获取。