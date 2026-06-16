---
title: "2026-06-16_Voxyz_ai_I_Compared_gstack_Superpowers_and_Compound_Enginee"
source: "https://x.com/Voxyz_ai/status/2038237755654783107"
author:
  - "[[@Voxyz_ai]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "x"
  - "@Voxyz_ai"
  - "ce"
  - "/ce"
---

# I Compared gstack, Superpowers, and Compound Engineering. They Solve Three Completely Different Prob
我比较了 gstack、Superpowers 和 Compound Engineering。它们解决了三个完全不同的问题。

**Vox**

# 我比较了 gstack、Superpowers 和 Compound Engineering。它们解决了三个完全不同的问题。

最近有三个 Claude 代码工具火了：Garry Tan 的 gstack（54.6K ⭐截至 2026-03-29），Jesse Vincent 的 Superpowers（121K ⭐），以及 Every Inc 的 Compound Engineering（11.5K ⭐）。

我比较了这三个代码库。这不是三个竞争对手，而是三个不同的层次，各有不同的重心。大多数人安装一个就以为自己已经覆盖了。

可以这样理解：gstack 是你的主厨兼试吃员，Superpowers 是你的厨房操作手册，CE 是每位员工下次轮班前都要阅读的食谱手册。你聘请了一位优秀的主厨，却没有食谱手册，因此每位新厨师都会重复犯下上一位厨师已经发现的错误。

为了理解这三个层次，我以 Anthropic 2025 年 11 月的工程博客作为框架。它是我找到的用来衡量这些工具的最佳标尺。

## Anthropic 的 Harness 架构

![Image](https://pbs.twimg.com/media/HEkojkNXYAAkOLp?format=jpg&name=large)

Anthropic 发布了一篇关于长期运行代理的有效利用方法的文章（2025 年 11 月 26 日）。他们的架构正式采用了一个两部分的系统：一个负责分解任务的初始化代理，以及后续执行这些任务的编码代理。测试、质量保证和专业代理作为未来工作进行了讨论。

我将用一个餐厅比喻来将其扩展为四个职责，因为这能让工具比较更清晰：

- 主厨决定菜单（规划）
- 厨房团队厨师（执行）
- 独立的食品品鉴师检查质量（评估）。不能让厨师评判自己做的菜。
- 结束记录传递给早班（跨时段状态）

这里最重要的核心发现是：评估自己工作的构建者会系统性地过于乐观。就像厨师评价自己做的菜，总是觉得很美味。构建者和检查者必须分离。通过他们的 harness 架构，智能体自主构建了一个具有 200 多个可验证功能的完整应用程序。

## gstack：决策层 + 测试层

![Image](https://pbs.twimg.com/media/HEkolSHW0AAub9o?format=jpg&name=large)

gstack 成功胜任规划和评估的角色。

/plan-ceo-review 和 /plan-eng-review 是你的主要审核人。一个从产品角度询问“这个是否值得开发”，另一个从架构角度询问“日后会不会出问题”。在开始工作前，这两个审核环节都必须通过。

这是一个实用的小贴士。在运行 /office-hours 之前，请使用这个提示来明确需求：

> 我即将开始这个项目。采访我，直到你对我实际想要的东西有95%的把握，而不是我觉得我应该想要的东西。

让 AI 来问你问题，而不是你去问 AI。大多数项目失败不是因为构建错误，而是因为一开始没有人明确要构建什么。AI 面试你比你提示 AI 有效 10 倍。

Claude Opus 4.6 拥有 100 万 token 的上下文窗口（目前在 Claude 平台上处于测试阶段）。对于符合该窗口范围的项目，您可以一次性加载完整的代码库和文档，而无需分批次输入。话虽如此，Anthropic 自己的工具说明仍然强调外部状态文件（feature-list、init.sh、claude-progress.txt）作为主要的协调机制，而非仅仅是原始上下文。

/qa 是独立的测试工具。它会打开真实浏览器，像真实用户一样浏览你的网站。不是“代码看起来没问题”，而是实际使用它。在他们的 Web 应用测试场景中，Anthropic 发现，与仅依赖代码层面的检查相比，明确要求基于浏览器的端到端测试能显著提升性能。

Garry Tan 表示，他通过这种配置在 60 天内交付了 60 万行生产代码，每天 10-20K 行，同时全职运营 YC（这些是他从回顾中提到的个人数据，具体情况因人而异）。在决策和质量保证方面，gstack 仍然是最强的。

但 gstack 就像一家有好厨师和好试吃员，却没有食谱本的餐厅。没人记录今晚出了什么问题。明天的团队从头开始，却犯同样的错误。注意：gstack 确实有自己的 /review 和 /ship 命令，因此与 CE 的 review 功能有一定重叠。区别在于侧重点不同，而非严格界限。

## 超能力：无记忆进程

Superpowers 的 121 万颗星证明了其品质。头脑风暴→计划→执行→回顾，帮助许多人从“随机与 AI 聊天”提升到“有流程地使用 AI”。

就像从一个每个人都即兴发挥的厨房，转变为一个有实际食谱和准备清单的厨房。这是一个巨大的进步。它还包括子代理驱动的开发，其中有独立的规范和代码质量审查者。

但 Superpowers 并不像 CE 那样将知识积累视为核心特性。每个会话的上下文都仅保留在该会话中。下一个会话开始时不会包含上一个会话的内容。

这就是让我在顶部添加 CE 的原因。

## 复合工程：缺失的层

![Image](https://pbs.twimg.com/media/HEkoojtW4AAlsqc?format=jpg&name=large)

CE 的周期：头脑风暴 → 计划 → 执行 → 回顾 → 复合。

前四个步骤类似于超级能力，但更深入。

计划阶段：而不是在当前对话中从头开始撰写计划，它会生成并行的研究代理，这些代理会深入挖掘你的项目历史、扫描代码库模式并读取 Git 提交日志。就像一位新厨师在设计明天的菜单前，会查看过去三个月每道菜的顾客反馈，而不是凭猜测行事。

评审阶段： 不只是一位品鉴者说“味道不错”。它运行一个动态评审团队，至少 6 名常驻评审员，外加基于 diff 的条件性评审员：正确性、安全性、性能、测试、可维护性、对抗性，每个评审员都会生成独立报告。就像有一位美食评论家、一位卫生检查员和一个客户小组分别品尝同一道菜。

但真正的分水岭是第五步：/ce:compound。

这就是 CE 得名的地方。

修复一个 bug 或完成一个功能后，执行这条命令。它会并行生成五个第一阶段子代理：

- 上下文分析器： 追踪整个对话，提取问题类型及涉及的组件
- 解决方案提取器: 捕获不起作用的地方、起作用的地方、根本原因以及最终解决方案
- 相关文档查找器：在现有知识库中搜索重复内容。如果之前已经修复过类似的问题，它会更新旧文档而不是创建新文档
- 预防策略师: 识别如何在未来预防这类问题
- 分类分类器: 标记并分类学习内容以用于结构化检索

所有五个完成，结果合并到 docs/solutions/。结构化、分类、可搜索的文档。

简单来说：你的代理每次班次结束后会撰写一份结束总结。下次任何代理开始新任务时，它会先浏览所有这些总结。

你修复了一个边缘运行时兼容性错误，这需要数小时的调试。Compound 自动记录这些信息：问题、症状、尝试过但无效的方法、最终解决方案、预防步骤。三周后，在另一个功能中出现了类似的问题。计划阶段的研究员自动找到了该记录：“我们之前遇到过这个问题，解决方案在这里。”数小时的调试时间被压缩到了几分钟。

关键区别：Anthropic 的进度文件是今晚的交接记录，留给早班，呈线性传递，一班传给下一班。CE 的 docs/solutions/是餐厅的食谱手册，每位员工入职第一天起每天都会查阅，且任何人随时都可搜索。

总结笔记解决连续性。食谱集解决积累。一个是线性的，一个是指数的。

这就是“compound”在这里的含义。不是复合的，而是复利。每个任务的输出不仅仅是代码，而是可复用的经验。你使用它的时间越长，你的代理就越了解你的项目。

## 三层堆叠

![Image](https://pbs.twimg.com/media/HEkoq0DbkAAkpP4?format=jpg&name=large)

```plaintext
Layer Tool Restaurant Version
──────────────────────────────────────────────────────────────────────────────────
Decisions (build or not) gstack Head chef sets the menu
Planning (how to build) CE /ce:plan Researcher reviews past complaints
Execution CE /ce:work Kitchen team cooks
Review (built correctly?)  CE /ce:review + gstack /qa Food critic + inspector + panel
Knowledge (remember) CE /ce:compound Recipe binder everyone reads
```

这些工具的重心不同，并非严格界限分明。gstack 的优势在于决策和实际场景中的质量保证。Superpowers 带来了结构化工作流的规范。CE 的优势在于研究驱动的规划、深度评审和知识积累。评审环节存在一些重叠，这并无不妥。

## 如何实际使用它们

如果你刚开始，先选择一个主要框架（gstack 或 CE）并熟悉它。虽然组合使用这三个框架是可行的，但多个框架可能会出现流程冲突和命令重叠。先理顺一个框架的工作流程，然后再逐步叠加。

对于有经验的用户，以下是组合流程：

1.  明确你想要什么。 使用 95%置信度提示语："询问我直到你对我真正想要的东西有 95%的把握，而不是我认为我应该想要的东西。"
2.  /office-hours (gstack). 描述你正在构建的内容。接受挑战。
3.  /plan-ceo-review (gstack). 产品门控：这个值得开发吗？
4.  /plan-eng-review (gstack). 架构门：这个以后会不会出问题？
5.  /ce:brainstorm (CE). 探索需求和方法，提炼为规范
6.  /ce:plan（CE）。研究代理扫描您的项目历史，然后生成详细的实施计划。
7.  /ce:work (CE). 执行计划并进行任务跟踪。
8.  /ce:review (CE). 动态评审者集合，最少 6 个，随差异复杂度扩展。
9.  /qa (gstack). 真实浏览器、真实点击、在预发环境中的真实用户测试
10.  /ce:compound (CE)。记录你学到的内容。五个子代理提取经验教训，将它们写入 docs/solutions/。
11.  发布它。 下次你从步骤 1 开始时，你的计划阶段已经知道你这次学到的所有内容。

步骤1-4确保你构建正确的东西。步骤5-9确保你构建得好。步骤10确保下次更快。

你的代理每天编写代码、修复 bug、运行测试。完成之后，知识会流向哪里？

如果答案是“分散在各个会话中，下次再次踩坑”，那么复合层就是你遗漏的那个层。

CE: github.com/EveryInc/复合工程插件 gstack：github.com/garrytan/gstack 超能力: github.com/obra/superpowers Anthropic 博客: anthropic.com/engineering/effective-harnesses-for-long-running-agents (2025 年 11 月 26 日) Anthropic 博客 2: anthropic.com/工程/测试框架设计-长期运行的应用

* * *

### 热门回复

**@Jason Zhou** ♥ 1.6K · 💬 63

很棒的关于降低 Claude 代码 token 数量高达 60%的帖子

最佳选择是使用开源工具 RTK（Rust 令牌杀手）

它会自动去除噪声，合并重复内容，并去除无用的空白行和进度条。

更多详情请见下方

@aibuilderclub\_

**@Peter Yang** ♥ 1.5K · 💬 64

"我们（Anthropic）现在可以在几天内而非几周内创建完整的功能。"

这是我新一期的节目，我和

@jenny\_wen

（Claude 的设计主管）一起，她向我难得地展示了 Anthropic 的运作方式，包括：

她如何使用 Cowork 来构建产品

Cowork 背后的真实故事

**@Fanatics** ♥ 492 · 💬 0

Cheer on your hoops team in their official Bench Tee!

**@aginaut** ♥ 2 · 💬 1

我也认为你最深刻的见解是连续性和积累之间的区别。

进度文件保存当前线程。

解决方案库会改变未来的线程。

这是一个比听起来大得多的区别，因为一个维持了势头，而另一个

**@Dale R-S** ♥ 1 · 💬 1

请问你能修复三层叠放部分的格式吗？