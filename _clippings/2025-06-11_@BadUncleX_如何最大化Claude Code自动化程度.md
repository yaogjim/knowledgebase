---
title: "如何最大化Claude Code自动化程度"
source: "https://x.com/BadUncleX/status/1932694405154279567"
author:
  - "[[@BadUncleX]]"
created: 2025-06-11
description:
tags:
  - "@BadUncleX #ClaudeCode #自动化 #AI #工具调用"
---
**BadUncle** @BadUncleX [2025-06-11](https://x.com/BadUncleX/status/1932694405154279567)

如何最大化Claude Code自动化程度

Vibe Coding的光谱里的主要元素是自动化程度, 对于Claude Code来说就是是否需要你点击确认执行。

根据你个人喜好以及场景确定如何定制自己的自动化程度。

Claude Code为以下两类自动化提供了相关配置：

1\. 最常见的代码编辑。 一般有3个选择，第一种手工点击Yes，或者选择默认Yes，第三种，快捷键 shift tab,即一直自动编辑。

2\. 工具调用自动化， 你可以理解为这是agent的重要组成部分， 除了用Yes手工同意以外， 官方提供了专门的全局配置，你可以用

tips： 默认尽量用手工， 只在你认为枯燥的不需要看细节的内容放开自动化。

图1是我配置的效果， 你也可以拿我现成的 settings.json 文件直接用， 根据需求自己改。具体链接见二楼gist文件。

图2是Claude Code所有可用工具列表， 标红的表示需要用户确认权限才能执行。

具体permissions配置文档见官方， 链接也放在了评论区

![图1](https://pbs.twimg.com/media/GtJO2svbMAMfPZP?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/GtJO3sGaEAAV0ak?format=png&name=large)

---

**BadUncle** @BadUncleX [2025-06-11](https://x.com/BadUncleX/status/1932694407746339194)

settings.json 文件

https://docs.anthropic.com/en/docs/claude-code/settings#permissions…