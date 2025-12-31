---
title: "2025-12-29_simonw_今天在做一些很冷门的项目_我做了一个页面_展示所有官方_GitHub_Actions_的最新版本_比"
source: "https://x.com/simonw/status/2005410175948304670"
author:
  - "[[@simonw]]"
published: 2025-12-29
created: 2025-12-29
description:
tags:
  - "x"
  - "@simonw"
  - "https"
  - "2025-12-28"
---

# 今天在做一些很冷门的项目：我做了一个页面，展示所有官方 GitHub Actions 的最新版本（比

**Simon Willison** @simonw [2025-12-28](https://x.com/simonw/status/2005410175948304670)

今天在做一些很冷门的项目：我做了一个页面，展示所有官方 GitHub Actions 的最新版本（比如 actions/setup-python@v6 这类），这样当 Claude Code 和朋友们帮我写工作流的时候，我就可以让他们参考这个页面

* * *

**Stove Jebs** @JebsSteve0x1 [2025-12-28](https://x.com/JebsSteve0x1/status/2005415041345147149)

为什么用 setup-python 而不用 setup-uv？

* * *

**Simon Willison** @simonw [2025-12-28](https://x.com/simonw/status/2005420519378833570)

我还没完全搞懂那个的缓存机制——我超希望我的工作流除非 pyproject.toml 变了，否则不获取任何数据。

* * *

**trainface** @trainface [2025-12-29](https://x.com/trainface/status/2005437282300699056)

必要的基础设施

* * *

**Salina Mendoza** @inababi [2025-12-29](https://x.com/inababi/status/2005431195275038846)

谢谢你做的这些工作，西蒙！整理很花时间。我会在教他们的时候把这个分享给其他人，让他们了解 Claude Code 的强大之处。 😌

* * *

**Somi AI** @somi\_ai [2025-12-29](https://x.com/somi_ai/status/2005442310516175220)

这解决了一个真正的痛点。每次 Claude 生成工作流时，我们都要手动检查动作版本。有一个权威的来源可以参考，省去了“实际上那个版本已经过时了，用 v6”这样的来回沟通。已添加到我们的标准上下文文件中。

* * *

**David P** @Lat3ntG3nius [2025-12-29](https://x.com/Lat3ntG3nius/status/2005443012638511289)

这就是模式：智能代理需要权威、最新的参考资料，它们无法编造内容。版本漂移是大模型生成代码的隐形杀手。为代理构建这些“事实来源”端点是被低估的基础设施工作。

* * *

**Risto Anton** @blogtheristo [2025-12-28](https://x.com/blogtheristo/status/2005413566049091896)

好想法。工作流版本化。明白了。