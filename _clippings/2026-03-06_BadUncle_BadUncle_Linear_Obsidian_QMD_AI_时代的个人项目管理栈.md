---
title: "2026-03-06_BadUncle_BadUncle_Linear_Obsidian_QMD_AI_时代的个人项目管理栈"
source: "https://x.com/BadUncleX/status/2029750070204322171"
author:
  - "[[@BadUncle]]"
published: 2026-03-06
created: 2026-03-06
description:
tags:
  - "x"
  - "@BadUncle"
  - "issue"
  - "linear"
---

# BadUncle Linear + Obsidian + QMD：AI 时代的个人项目管理栈

**BadUncle**

Linear + Obsidian + QMD：AI 时代的个人项目管理栈 (这个组合解决了我长期关注的问题） 核心理念：任务和知识分离 - Linear 管「做什么」— issues、checklists、状态流转 - Obsidian 管「做了什么、为什么」— 设计决策、架构文档、操作记录 - 两者通过 commit links 和 issue ID 双向关联，互不侵入 Linear 侧的实践 - 每个项目一个 Linear Project，issue title 带编号前缀（P1、P2）方便口头引用 - Issue description 用 markdown checklist 当执行清单，完成一项勾一项 - 完成 issue 时在 description 末尾加 ## Commits 段，链接对应的 git commit - Linear 状态管理：个人项目直接 main 提交 + 手动更新 Linear；协作项目走 PR 流程（gh pr create 在终端完成，Closes BUNOTES-xx 自动关联） Obsidian 侧的实践 - projects/{name}/ 子目录存项目文档，一个项目一个文件夹 - Frontmatter 是关键：commits 字段链接代码、aliases 放 issue 编号（如 P1、BUNOTES-37）便于搜索 - 不记流水账，记决策和结论 — 「为什么选 cherry-pick 不选 rebase」比「今天做了 xx」有价值 - 文档状态只有 draft 和 complete，不搞复杂状态机 QMD 串联一切 - 所有 Obsidian 笔记自动索引，支持关键词搜索和语义搜索 - Claude Code session 记录也被索引 — 几周前的调试过程可以被找回 - 搜 issue 编号能同时找到 Obsidian 文档和历史 session 上下文 Claude Code 作为执行层 - 开发时同步维护两侧：创建 Linear issue → 编码 → 提交 → 更新 issue checklist → 写/更新 Obsidian 文档 - Skill 里写清规范（frontmatter 格式、commit 字段必填），AI 自动遵守 - 一个 session 内完成代码 + 任务管理 + 文档，不需要手动切换工具 反直觉的点 - 不需要完美的双向链接 — commit hash 就是最好的链接，在 Linear 和 Obsidian 都能搜到 - 不需要模板引擎 — frontmatter + 目录约定就够了 - 不需要自动同步 — 人为确认「这个 issue 确实完了」再手动更新，比自动化更可靠 - QMD 的价值不在「随时搜索」，在于「几个月后还能找回当时的决策上下文」

* * *

### 热门回复

**@BadUncle** ♥ 67 · 💬 3

qmd被低估了，和obsidian结合起来用好用。 关于知识管理或者文档管理， 最早从RAG开始，太重了，个人用户几乎没有。 后来向量的概念逐步普及，大家知道文档迟早是要进入向量的， 但是embedding的大模型， 默认还是云服务的， 这个虽然很便宜， 但是仍然阻碍了普及。 知道qmd， 一步到位，qmd