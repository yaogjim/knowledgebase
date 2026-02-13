---
title: "2026-02-13_bcherny_回顾工程师喜爱_Claude_Code_的原因_其中一个突出的特点是它的可定制性_钩子_插件_LSP"
source: "https://x.com/bcherny/status/2021699851499798911"
author:
  - "[[@bcherny]]"
published: 2026-02-13
created: 2026-02-13
description:
tags:
  - "x"
  - "@bcherny"
  - "https"
  - "claude"
---

# 回顾工程师喜爱 Claude Code 的原因，其中一个突出的特点是它的可定制性：钩子、插件、LSP

**Boris Cherny** @bcherny [2026-02-11](https://x.com/bcherny/status/2021699851499798911)

回顾工程师喜爱 Claude Code 的原因，其中一个突出的特点是它的可定制性：钩子、插件、LSPs、MCPs、技能、投入、自定义代理、状态行、输出样式等。

每个工程师使用工具的方式各不相同。我们从零开始构建了 Claude Code，不仅拥有出色的默认设置，还具备极高的可定制性。这也是开发者爱上这款产品的原因之一，也是 Claude Code 的增长持续加速的原因。

我想分享几种我们看到个人和团队自定义他们的 Claude 的方式。

* * *

**Boris Cherny** @bcherny [2026-02-11](https://x.com/bcherny/status/2021699859359883608)

1/ 配置你的终端

主题：运行 /config 以设置浅色/深色模式

Notifs: 为 iTerm2 启用通知，或使用自定义的通知钩子

换行：如果您在 IDE 终端、Apple 终端、Warp 或 Alacritty 中使用 Claude Code，请运行 /terminal-setup 以启用 shift+enter 用于

![Image](https://pbs.twimg.com/media/HA6EwD8bsAQnna5?format=jpg&name=large)

* * *

**Boris Cherny** @bcherny [2026-02-11](https://x.com/bcherny/status/2021699860869902424)

2/ 调整工作量

运行 /model 以选择您偏好的努力程度。将其设置为：

低：减少 token 数量，加快响应速度

\- 中等，用于平衡行为

高，以获取更多 token 和更多智能

就我个人而言，我什么都用 High。

![Image](https://pbs.twimg.com/media/HA6FCTCakAI5FFk?format=png&name=large)

* * *

**Boris Cherny** @bcherny [2026-02-11](https://x.com/bcherny/status/2021699862522364149)

3/ 安装插件、MCPs 和技能

插件允许你安装 LSPs（现在适用于所有主要语言）、MCPs、技能、代理和自定义钩子。

从官方的 Anthropic 插件市场安装一个插件，或者为你的公司创建自己的市场。然后，检查

![Image](https://pbs.twimg.com/media/HA6FQOSbcAA6ybR?format=jpg&name=large)

* * *

**Boris Cherny** @bcherny [2026-02-11](https://x.com/bcherny/status/2021700144039903699)

4/ 创建自定义代理

要创建自定义代理，请将 .md 文件放入 .claude/agents 目录。每个代理可以有自定义名称、颜色、工具集、预先允许和禁止的工具、权限模式以及模型。

Claude Code 中还有一个鲜为人知的功能，它可以让你设置

![Image](https://pbs.twimg.com/media/HA6Fi_WaMAA2_LG?format=png&name=large)

* * *

**Boris Cherny** @bcherny [2026-02-11](https://x.com/bcherny/status/2021700332292911228)

5/ 预先批准常见权限

Claude Code 使用了一套复杂的权限系统，结合了提示词注入检测、静态分析、沙箱化以及人工监督。

开箱即用，我们预先批准了一小部分安全命令。要预先批准更多，运行 /permissions

![Image](https://pbs.twimg.com/media/HA6FurbbsAM95NS?format=png&name=large)

* * *

**Boris Cherny** @bcherny [2026-02-11](https://x.com/bcherny/status/2021700506465579443)

6/ 启用沙箱

启用 Claude Code 的开源沙箱运行时（ https://github.com/anthropic-experimental/sandbox-runtime…）以提高安全性，同时减少权限提示。

运行 /sandbox 以启用它。沙箱在您的机器上运行，并支持文件和网络隔离。Windows 支持

![Image](https://pbs.twimg.com/media/HA6F4hrbsAEjpXW?format=png&name=large)

* * *

**Boris Cherny** @bcherny [2026-02-11](https://x.com/bcherny/status/2021700784019452195)

7/ 添加状态行

自定义状态行显示在编辑器正下方，让你可以显示模型、目录、剩余上下文、成本以及几乎任何你在工作时想要查看的其他内容。

Claude Code 团队的每个成员都有不同的状态栏。使用/statusline 来

![Image](https://pbs.twimg.com/media/HA6GIPDaEAEE7nm?format=jpg&name=large)

* * *

**Boris Cherny** @bcherny [2026-02-11](https://x.com/bcherny/status/2021700883873165435)

8/ 自定义你的快捷键

你知道 Claude Code 中的每个按键绑定都是可自定义的吗？使用/keybindings 命令重新映射任何按键。设置会实时重载，这样你可以立即看到效果。