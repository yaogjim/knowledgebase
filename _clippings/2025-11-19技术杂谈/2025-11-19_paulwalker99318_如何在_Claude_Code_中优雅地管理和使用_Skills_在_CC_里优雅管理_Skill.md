---
title: "2025-11-19_paulwalker99318_如何在_Claude_Code_中优雅地管理和使用_Skills_在_CC_里优雅管理_Skill"
source: "https://x.com/paulwalker99318/status/1990695712888365075"
author:
  - "[[@paulwalker99318]]"
published: 2025-11-19
created: 2025-11-19
description:
tags:
  - "x"
  - "@paulwalker99318"
  - "plugin"
  - "https"
status: "inbox"
importance: 2
effort: 2
review_level: 0
review_next: "2025-12-10"
review_interval: null
review_count: 0
decision: null
topics: []
links_out: []
summary: ""
pov: ""
actions: []
---

# 如何在 Claude Code 中优雅地管理和使用 Skills？ 在 CC 里优雅管理 Skill

**Bruce** @paulwalker99318 [2025-11-18](https://x.com/paulwalker99318/status/1990695712888365075/history)

如何在 Claude Code 中优雅地管理和使用 Skills？

在 CC 里优雅管理 Skills 的正确姿势是：一律“插件化 + marketplace化”，不要散落的文件。

Anthropic 官方 anthropics/skills 仓库已经给了非常明确的路线：通过 /plugin 把整个仓库当成一个 Plugin Marketplace 来挂载，再按需安装 Skill 套件。

/plugin marketplace add anthropics/skills

命令含义：

\- 告诉 Claude Code：anthropics/skills 仓库里有 .claude-plugin 配置，可以作为一个插件源。

\- 之后 /plugin 打开的 UI 里，你会看到一个叫 anthropic-agent-skills 的插件“市场”。

具体怎么做？

1\. 对于官方 Skills

\# 先从官方插件市场安装 Skills 插件

/plugin marketplace add anthropics/skills

\# 从这个市场里按需安装插件化的 Skill 套件

/plugin install example-skills@anthropic-agent-skills

\# 若有确定的文档处理需求，可以直接安装：

/plugin install document-skills@anthropic-agent-skills

2\. 对于自定义 Skills

在你自己的 GitHub org 建一个 org-claude-skills 仓库：

初始化 .claude-plugin，定义 org-document-skills/org-dev-workflow 等插件。

把你最常用的两三类流程包装成 Skills（可以直接借鉴 skill-creator 模板）。

如何使用？

安装完之后，Claude Code 会自动把插件里 skills/ 目录下的各个 Skill 注册进“可用 Skills”列表。

你只需要“自然语言调用”即可，比如：

“使用 PDF skill 从这个文档中提取表格：path/to/some-file.pdf”

不需要你手动 /skill xxx，也不需要写什么配置。

发现 & 调用都交给模型自己，Skill 只负责“说明自己能做什么”。

![Image](https://pbs.twimg.com/media/G6BboIebAAEohYa?format=jpg&name=large)

* * *

**𝙩𝙮≃𝙛{𝕩}^A𝕀²·ℙarad𝕚g𝕞** @TaNGSoFT [2025-11-18](https://x.com/TaNGSoFT/status/1990706576232239534)

学习了

* * *

**Mechanize** @MechanizeWork

Hopkins seniors: automate software engineering before someone else does. $250k/yr + competitive equity, SF.

* * *

**otto pan** @otto\_bulk [2025-11-19](https://x.com/otto_bulk/status/1990953993749795031)

@threadreaderapp unroll

* * *

**Calvinobai** @calvinobai [2025-11-18](https://x.com/calvinobai/status/1990724004810719246)

👍感谢🙏