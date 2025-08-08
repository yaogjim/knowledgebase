---
title: "如何使用 Claude 代码"
source: "https://x.com/BadUncleX/status/1938389296815440319"
author:
  - "[[@BadUncleX]]"
created: 2025-07-04
description:
tags:
  - "@BadUncleX #Claude #代码 #AI开发 #AI工具"
---
**BadUncle** @BadUncleX [2025-06-27](https://x.com/BadUncleX/status/1938389296815440319)

来自reddit用户分享的claude code 16条使用建议

\---比如：verbose，Opus优先，github cli代替fetch，分开维护git  
  
1\. 维护 CLAUDE\[.\]md 文件

建议为不同子目录（如测试、前端、后端）分别维护 CLAUDE\[.\]md，记录指令和上下文，便于 Claude 理解项目背景。  
  
2\. 善用内置命令

▫ Plan mode（shift+tab）：提升任务完成度和可靠性。

▫ Verbose mode（CTRL+R）：查看 Claude 当前的全部上下文。

▫ Bash mode（!前缀）：运行命令并将输出作为上下文。

▫ Escape 键：中断或回溯对话历史。  
  
3\. 并行运行多个实例

前后端可分别用不同实例开发，提高效率，但复杂项目建议只用一个实例以减少环境配置麻烦。

4\. 使用子代理（subagents）

让多个子代理从不同角度解决问题，主代理负责整合和比较结果。  
  
5\. 利用视觉输入

支持拖拽截图，Claude Code 能理解视觉信息，适合调试 UI 或复现设计。

6\. 优先选择 Claude 4 Opus

高级订阅用户建议优先用 Opus，体验和能力更强。  
  
7\. 自定义项目专属 slash 命令

在 \`.claude/commands\` 目录下编写常用任务、项目初始化、迁移等命令，提升自动化和复用性。

8\. 使用 Extended Thinking

输入 \`think\`、\`think harder\` 或 \`ultrathink\`，让 Claude 分配更多“思考预算”，适合复杂任务。  
  
9\. 文档化一切

让 Claude 记录思路、任务、设计等到中间文档，便于后续追溯和上下文补充。

10\. 频繁使用 Git 进行版本控制

Claude 可帮写 commit message，AI 辅助开发时更要重视版本管理。  
  
11\. 优化工作流

▫ 用 \`--resume\` 继续会话，保持上下文。

▫ 用 MCP 服务器或自建工具管理上下文。

▫ 用 GitHub CLI 获取上下文而非 fetch 工具。

▫ 用 ccusage 监控用量。  
  
12\. 追求快速反馈循环

给模型提供验证机制，减少“奖励劫持”（AI 取巧而非真正解决问题）。

13\. 集成到 IDE

体验更像“结对编程”，Claude 可直接与 IDE 工具交互。  
  
14\. 消息排队

Claude 处理任务时可继续发送消息，排队等待处理。

15\. 注意会话压缩与上下文长度

合理压缩对话，避免丢失重要上下文，建议在自然停顿点进行。

16\. 自定义 PR 模板

不要用默认模板，针对项目定制更合适的 PR（pull request) 模板。

![Image](https://pbs.twimg.com/media/GuZ_EzgaQAAKXeF?format=jpg&name=large)

---

**BadUncle** @BadUncleX [2025-06-27](https://x.com/BadUncleX/status/1938389299692769294)

原文：How I use Claude Code  
我如何使用 Claude 代码