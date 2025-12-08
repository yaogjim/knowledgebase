---
title: "2025-12-05_wquguru_OpenAI_Codex合并了httpsgithub_comopenaicodexpul"
source: "https://x.com/wquguru/status/1996388143747178871"
author:
  - "[[@wquguru]]"
published: 2025-12-05
created: 2025-12-05
description:
tags:
  - "x"
  - "@wquguru"
  - "https"
---

# OpenAI Codex合并了httpsgithub.comopenaicodexpul

**WquGuru** @wquguru 2025-12-01

OpenAI Codex合并了https://github.com/openai/codex/pull/7412…，引入了实验性的Skills系统，核心特性大概是这样：

1.完整兼容Claude Skills规范

\-路径：~/.codex/skills/\*\*/SKILL.md

\-格式：标准YAML frontmatter+Markdown正文，跟Claude Code 100%一致

\-启动时递归加载所有有效http://SKILL.md，只解析frontmatter

2.上下文高效注入机制

\-所有已加载技能渲染成## Skills段，追加到user instructions末尾

\-只注入name+description+文件路径引用（单条30–50 token左右）

\-完整技能正文只在模型明确引用时才由代理主动读取（progressive disclosure那种）

\-跟现有http://AGENTS.md、http://PROJECT.md等文档同级合并，不用改系统提示

3.实现细节

\-新增skills/模块（loader、model、renderer）

\-依赖serde\_yaml、dunce，错误统一用SkillError，通过TUI模态展示

\-受Feature::Skills特性旗控制：codex dev --features skills就能开启（后续默认开）

4.互操作性

\-直接symlink或cp ~/.claude/skills/到~/.codex/skills/，零修改复用Claude市场那500+社区技能（推荐symlink的方式，一遍修改，两遍生效）

简单说，OpenAI没另起炉灶，而是直接采纳Anthropic的Skills标准，让Codex瞬间接入目前最成熟的动态上下文加载生态

Claude Skills本身就是个轻量、可堆叠、延迟加载的技能定义格式：YAML声明元数据→模型先看摘要→规划时决定调用→运行时read\_file完整指令，彻底解决长上下文污染问题，已经成Claude Code、Cursor、Windsurf等多个工具的事实标准

现在Codex也加入这个统一阵营，不得不说A社的创造一直都在引领方向，Claude Code、MCP、Skills均如此

> 2025-12-01
> 
> Skills are coming to Codex - currently being implemented
> 
> \- Seems like they'll be interoperable with Claude Skills, although in a separate ~/.codex/skills directory (probably want to symlink here)
> 
> \- Uses the same YAML and http://SKILL.md format
> 
> https://github.com/openai/codex/pull/7412…
> 
> Codex 即将迎来技能功能——目前正在实施中
> 
> \- 看起来它们将与 Claude Skills 兼容，不过会存放在单独的~/.codex/skills 目录中（可能需要在此处创建符号链接）
> 
> \- 采用相同的 YAML 和 http://SKILL.md 格式
> 
> https://github.com/openai/codex/pull/7412…
> 
> ![Image](https://pbs.twimg.com/media/G7Ec5j-bwAE7FCr?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G7EdIoXaoAAqhpI?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G7EdSBYasAABjfS?format=jpg&name=large)

* * *

**WquGuru** @wquguru [2025-12-04](https://x.com/wquguru/status/1996441442374365373)

快速上手方法：

1\. 升级到alpha版本： npm install -g @openai/codex@0.65.0-alpha.8

2\. 将claude code skills拷贝或者symlink到~/.codex

\- 2.1 创建：mkdir -p ~/.codex/skills

\- 2.2 symlink方式（推荐）：

cd ~/.claude/skills

for dir in \*/; do

ln -s "$(pwd)/$dir" ~/.codex/skills/

done

\-

快速上手方法：

1\. 升级到 alpha 版本： npm install -g @openai/codex@0.65.0-alpha.8

2\. 将 claude code skills 拷贝或创建符号链接到~/.codex 目录

\- 2.1 创建：mkdir -p ~/.codex/skills

\- 2.2 符号链接方式（推荐）：

cd ~/.claude/skills

for dir in \*/; do

ln -s "$(pwd)/$dir" ~/.codex/skills/

完成

\-

* * *

**WquGuru** @wquguru [2025-12-04](https://x.com/wquguru/status/1996442320284315830)

勘误一点，codex还不支持symlink，只能用拷贝方式（头疼）

![Image](https://pbs.twimg.com/media/G7TJsOdaYAACK5N?format=jpg&name=large)

* * *

**AlexZ** @blackanger [2025-12-04](https://x.com/blackanger/status/1996443024902209767)

我最早是在 Dia 浏览器里看到 skill 功能的，不知道 claude code是不是受这个启发

* * *

**marshmallow.edge** @7marshm7allow [2025-12-04](https://x.com/7marshm7allow/status/1996486650281742658)

Codex拥抱开放标准真是明智之举，技能复用生态瞬间翻倍