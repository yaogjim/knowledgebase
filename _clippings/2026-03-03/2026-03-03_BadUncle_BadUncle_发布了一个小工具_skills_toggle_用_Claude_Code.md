---
title: "2026-03-03_BadUncle_BadUncle_发布了一个小工具_skills_toggle_用_Claude_Code"
source: "https://x.com/BadUncleX/status/2028506485387649151"
author:
  - "[[@BadUncle]]"
published: 2026-03-03
created: 2026-03-03
description:
tags:
  - "x"
  - "@BadUncle"
  - "skills-toggle"
  - "https"
---

# BadUncle 发布了一个小工具：skills-toggle 用 Claude Code

**BadUncle**

发布了一个小工具：skills-toggle 用 Claude Code 的 skills 功能久了，~/.claude/skills/ 目录会积攒几百个 skill，每个都会往 system prompt 塞 ~100 tokens。session 越来越重，但大部分 skill 当下根本用不到。 做了个 TUI 工具来管理它们——勾选启用，取消禁用： > skills-toggle \[x\] bun \[x\] nextjs \[ \] actix-web-basics \* \[ \] actix-web-database \* \[x\] deep-modules Enabled: 280 | Disabled: 35 | Changed: 2 也支持批量操作： skills-toggle disable 'actix-\*' skills-toggle enable 'flutter-\*' 原理很简单：把不用的 skill 目录移到 .disabled/，Claude Code 不会扫描这个子目录。所有移动操作是原子的，失败会自动回滚。 安装： brew tap BUNotesAI/skills-toggle brew install skills-toggle GitHub: [https://github.com/BUNotesAI/skills-toggle…](https://github.com/BUNotesAI/skills-toggle)

![图片](https://pbs.twimg.com/media/HCaz42DaQAAjUqT?format=png&name=large)

* * *

### 热门回复

**@Leo** ♥ 1 · 💬 0

感觉增加了管理工作量。