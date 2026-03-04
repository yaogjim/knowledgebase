---
title: "2026-03-02_Leo_Leo_上条聊了_httpCLAUDE_md_httpCLAUDE_md"
source: "https://x.com/runes_leo/status/2028253450631331958"
author:
  - "[[@Leo]]"
published: 2026-03-02
created: 2026-03-02
description:
tags:
  - "x"
  - "@Leo"
  - "skill"
  - "agent"
---

# Leo 上条聊了 [httpCLAUDE.md](httpCLAUDE.md)

**Leo**

上条聊了 [http://CLAUDE.md](http://CLAUDE.md) 怎么从配置文件变成记忆系统，这条接着说能力层——Skills。 Claude Code 的 Skills 生态正在经历一轮爆发。聚合市场从几万涨到近 30 万条，官方 repo、Vercel 的包管理器、第三方市场三条线同时跑。看起来很像早期的 App Store 我自己连下载带自己写一共有了 30 个 skill，覆盖推文风格校准、四阶段调试流程、数据采集、Obsidian 同步、PDF 处理、代码审查交叉验证。两个月用下来，最大的体感是： 数量没意义。 市场上 30 万个 skill，大部分是一段 prompt 套个 markdown 模板。装上就能用，但用两次就知道不对——没有触发条件，不知道什么时候该跑；没有错误处理，一出问题整个流程断掉；没有输入输出契约，每次结果格式不一样。 有人分析了 3 万多个 skill，发现 26.1% 存在安全风险。提示注入、未经验证的外部调用、权限过宽——这些不是理论风险，是你把别人的 skill 装进自己的 agent 就真实存在的攻击面。 好的 skill 不是一段 prompt，是一套完整的调度逻辑。拿我用得最多的 leo-style 举例：它有范文库做风格校准，有 7 条禁止规则做质量兜底，有溯源检查防止 AI 替你吹牛，还有迭代日志——每次我手动改了推文，规则自动更新。这不是"安装一个插件" ，更像是给 agent 做岗前培训。 现在的 Skills 生态像 2009 年的 App Store——量在爆发，质量没跟上。聪明的做法不是装 50 个热门 skill，是花时间把 3-5 个核心 skill 打磨到真正好用。 你自己写的，永远比别人写的更合手。你在用什么 skill？欢迎评论区推荐！👀

![图片](https://pbs.twimg.com/media/HCVjpZnbEAAMEul?format=jpg&name=large)![图片](https://pbs.twimg.com/media/HCQQcjLbEAQoFKc?format=jpg&name=large)

> **@runes\_leo**
> 
> 我的 AI 外脑：Obsidian + 向量搜索 + Claude Code 上条聊了 Obsidian CLI 的搜索能力，但单 vault 关键词搜只是起点。我需要 AI 能同时搜笔记、代码文档和三个月前的踩坑记录，然后直接给答案。 现在的做法：用 QMD 给 vault 建了关键词索引和向量索引，用 ChromaDB 存了 1000 x.com/runes\_leo/stat…

![引用图片](https://pbs.twimg.com/media/HCQQcjLbEAQoFKc?format=jpg&name=large)

* * *

### 热门回复

**@Leo** ♥ 9 · 💬 2

Cursor CEO 说软件开发经历了三个阶段——AI 补全代码、AI 当场写代码、AI 自己跑几个小时把活干完交给你审。他们内部 35% 的 PR 已经由 Agent 创建。 这个框架跟我每天的体感完全吻合，只是我不在 IDE 里。

**@阿台BlueBird** ♥ 0 · 💬 0

技能质量远比数量重要