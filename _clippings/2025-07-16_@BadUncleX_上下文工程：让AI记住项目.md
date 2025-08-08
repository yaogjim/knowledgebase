---
title: "上下文工程：让AI记住项目"
source: "https://x.com/BadUncleX/status/1944563958108864831"
author:
  - "[[@BadUncleX]]"
created: 2025-07-16
description:
tags:
  - "@BadUncleX #上下文工程 #AI #编程助手 #开发效率 #代码质量"
---
**BadUncle** @BadUncleX [2025-07-14](https://x.com/BadUncleX/status/1944563958108864831)

𝐂𝐨𝐧𝐭𝐞𝐱𝐭 𝐅𝐨𝐫𝐠𝐞 快速指南：让 𝐀𝐈记住你的项目上下文

\---context engineering 具体应用

\---借助hooks应用到claude code  
  
又一个和记忆相关的github项目，之前介绍了一个手工”复读机“模式有点简单粗暴， 这个管理更细化，供参考。  
  
链接见评论  
  
解决什么问题？  
  
AI 编程助手的"健忘症"：

◆ 聊着聊着就忘了你的技术栈

◆ 反复解释相同的编码规范

◆ 上下文窗口满了，之前的指令都丢了  
  
具体用途：

• 自动化项目文档生成：根据你的项目需求（PRD），自动生成分阶段的开发计划、项目结构、工作流规则等文档。

• 技术迁移与升级：内置迁移助手，帮助项目安全地从一种技术栈迁移到另一种（如 Express → Next.js），并生成详细的迁移计划和回滚方案。

• 人机协作开发：通过“Checkpoints”机制，在关键开发节点暂停，要求人工审核，确保开发过程可控且高质量。

• 代码质量保障：集成验证系统，自动检查语法、测试、构建和安全等环节，生成详细报告。  
  
原理：“上下文工程”（Context Engineering）理念和自动化文档生成流程  
  
上下文工程：不等 AI 忘记，主动管理和注入关键信息  
  
三个关键文件：

\- \`CLAUDE. md\` - 项目的"宪法"（技术栈、规范、命令）

\- \`PRPs/\*.md\` - 每个功能的独立"说明书"

\- \`Implementation. md\` - 分阶段开发计划  
  
三步上手  
  
🔹 1. 安装并初始化

npm install -g context-forge

context-forge init --ide claude  
  
🔹 2. 选择适合的预设

\- \`startup-mvp\` - 快速原型开发

\- \`enterprise\` - 企业级项目

\- \`hackathon\` - 黑客松极速模式  
  
🔹 3. 开始开发

在 Claude Code 中打开项目，AI 自动读取上下文，理解你的一切需求  
  
📁 生成的文件结构

your-project/

├── CLAUDE. md # AI 必读手册

├── PRPs/ # 功能需求文档

│ ├── auth-prp. md

│ └── payment-prp. md

├── Docs/

│ ├── Implementation. md # 开发路线图

│ └── Bug\_tracking.md # 问题追踪

└── .claude/hooks/ # 自动注入钩子

---

**BadUncle** @BadUncleX [2025-07-14](https://x.com/BadUncleX/status/1944563960671506909)

github链接