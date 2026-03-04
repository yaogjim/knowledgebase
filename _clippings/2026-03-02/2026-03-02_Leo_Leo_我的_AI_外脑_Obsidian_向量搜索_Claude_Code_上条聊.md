---
title: "2026-03-02_Leo_Leo_我的_AI_外脑_Obsidian_向量搜索_Claude_Code_上条聊"
source: "https://x.com/runes_leo/status/2027921261075087705"
author:
  - "[[@Leo]]"
published: 2026-03-02
created: 2026-03-02
description:
tags:
  - "x"
  - "@Leo"
  - "ai"
  - "claude"
---

# Leo 我的 AI 外脑：Obsidian + 向量搜索 + Claude Code 上条聊

**Leo**

我的 AI 外脑：Obsidian + 向量搜索 + Claude Code 上条聊了 Obsidian CLI 的搜索能力，但单 vault 关键词搜只是起点。我需要 AI 能同时搜笔记、代码文档和三个月前的踩坑记录，然后直接给答案。 现在的做法：用 QMD 给 vault 建了关键词索引和向量索引，用 ChromaDB 存了 1000 多条踩坑经验和决策记录。两层都通过 MCP 接进 Claude Code。 实际效果：跟 Claude 对话时，它能同时搜笔记、代码文档和历史经验。问"上次那个 API 报错怎么解决的"，它从三个月前的踩坑记录里把答案捞出来。 不只是 Obsidian——5 个代码仓库的文档也一起索引了。7 个 collection，1191 篇文档，全部本地。 说白了就是个人 RAG，数据全在自己机器上。

![图片](https://pbs.twimg.com/media/HCQQcjLbEAQoFKc?format=jpg&name=large)![图片](https://pbs.twimg.com/media/HCLgcObaQAAuipI?format=jpg&name=large)

> **@runes\_leo**
> 
> Obsidian 1.12 加了命令行工具，对用 AI 的人来说是大升级。 现在很多人把 Obsidian 当 AI 的外部记忆层——笔记、决策记录、踩坑经验都沉淀在 vault 里，AI 需要时直接读取。我自己就是这么用的：Claude Code 读写 x.com/obsdmd/status/…

![引用图片](https://pbs.twimg.com/media/HCLgcObaQAAuipI?format=jpg&name=large)

* * *

### 热门回复

**@小互** ♥ 1.3K · 💬 58

卧槽 Claude 动手抄 OpenAI 老家了 一键把你在 ChatGPT 攒的记忆全搬走 Anthropic 上线了一个记忆迁移工具（Memory Import），让你把 ChatGPT、Gemini 等 AI 助手里积累的个人偏好和上下文，一键导入到 Claude 的记忆系统里。 众所周知 ChatGPT 的一大核心竞争力就是其 记忆系统 很完善...

**@独立开发者William** ♥ 1.3K · 💬 44

有人已经直接用 Qwen3.5-27B + DGX Spark 做成 Android Agent，通过 Web UI 下发任务，让模型自己读屏、决策、点按，推理速度提升 4 倍。

**@鱼总聊AI** ♥ 1.2K · 💬 27

大佬就是大佬，苹果最封闭的那块都被你给撬开了。 这个叫 vphone-cli 的开源项目，可以在 Mac 上直接跑完整 iOS 系统虚拟机。 注意，这不是模拟器哈。是真的 iOS。 可以批量开，批量关，脚本控制，在CI 里直接用。 以前做 iOS 自动化测试要买一堆真机接一堆线，现在变成 vphone create 一条命令。

**@Niko** ♥ 416 · 💬 10

Obsidian Web Clipper 我愿称之为最伟大发明 几十万吃灰的收藏夹文章，装进 Obsidian 里是什么体验？ 答案是：彻底告别「Mark了等于看了」 以前： 遇到干货 → 丢进 X 收藏夹 → 彻底遗忘 → 毫无长进 收藏了 1000 篇，一篇都没看 现在： 遇到干货 → 一键剪藏 → 定期让 AI 批量阅读 →

**@than** ♥ 1 · 💬 1

我最近也在用类似的系统。不过是接入了一些高质量信源，claude opus 4.6每次的输出结果都让我惊艳