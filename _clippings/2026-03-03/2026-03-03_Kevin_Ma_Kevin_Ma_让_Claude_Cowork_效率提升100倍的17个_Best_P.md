---
title: "2026-03-03_Kevin_Ma_Kevin_Ma_让_Claude_Cowork_效率提升100倍的17个_Best_P"
source: "https://x.com/kevinma_dev_zh/status/2028369395517726932"
author:
  - "[[@Kevin Ma]]"
published: 2026-03-03
created: 2026-03-03
description:
tags:
  - "#product"
  - "x"
  - "@Kevin Ma"
  - "cowork"
---

# Kevin Ma # 让 Claude Cowork 效率提升100倍的17个 Best P

**Kevin Ma**

# 让 Claude Cowork 效率提升100倍的17个 Best Practices

今天看到这篇文章，觉得特别棒，整理了一下分享给大家。

我自己最近一个月在利用 AI 用于非编程领域方面提效很多，越来越觉得，打造一个适用于自己的系统特别重要，而 Nav Toor 的分享正好是可以帮助我们学习到如何打造适用于自己的高效系统。

> 17 Best Practices That Make Claude Cowork 100x More PowerfulI’ve been using Claude Cowork since January 12, the day it launched. In seven weeks, I’ve run over 400 Cowork sessions. I’ve tested every plugin, every connector, every slash command. I’ve broken it...
> 
> — Nav Toor
> 
> [https://x.com/heynavtoor/status/2028148844891152554](https://x.com/heynavtoor/status/2028148844891152554)

作者在 Cowork 上线当天（1月12日）就开始使用，七周内运行超过400次 session，测试了每一个 plugin、connector 和 slash command。以下是他总结的完整列表——按影响力排序。

核心结论：差距不在于 prompting 技巧，而在于搭建方式与结构。

## Part 1：Context Architecture（实践 1–5）

## 1\. 为每个工作文件夹创建 \_MANIFEST.md

当你把 Cowork 指向一个文件夹时，它默认读取一切——包括过时的草稿和被替代的旧版本，导致输出前后矛盾。解决方案是在工作文件夹中放一个 \_MANIFEST.md，按三层结构组织：

Tier 1（Canonical）

- 内容：品牌规范、项目简报、当前策略文档
- Claude 的行为：优先阅读

Tier 2（Domain）

- 内容：各主题子文件夹（如 /pricing、/research）
- Claude 的行为：仅在任务涉及时加载

Tier 3（Archival）

- 内容：旧草稿、被替代版本、参考资料
- Claude 的行为：除非明确要求，否则跳过

下划线前缀让文件排在文件夹顶部。填写只需五分钟，却能节省数小时混乱的输出。文件少于10个时可以不用；项目文件夹则必不可少。

## 2\. 将 Global Instructions 用作你的永久操作系统

路径：Settings → Cowork → Edit → Global Instructions

Global Instructions 在一切之前加载——先于文件、先于 prompt。即使是最随意的 prompt，也能因此产出有质量的结果。以下是一个实用模板：

> 我是\[姓名\]，担任\[角色\]。 - 开始任务前，先查找 \_MANIFEST.md 并优先读取 Tier 1 文件 - 执行前先提问澄清，采取行动前展示简短计划 - 默认输出格式：.docx - 不使用 filler language，不填充内容 - 质量标准：每份 deliverable 无需编辑即达客户可用级别 - 如果把握不足，请说明

## 3\. 创建三个持久 Context 文件

创建文件夹 00\_Context，添加以下三个文件：

about-me.md — 你的职业身份。你实际做什么、服务谁、当前优先事项，以及一两个最佳工作示例（非简历）。

brand-voice.md — 你的沟通风格。语气、习惯用词、禁用词、格式偏好，附2–3段实际写作样本。

working-style.md — Claude 的工作方式。协作规则、默认输出格式、质量标准、需要避免的事项。

这些文件会产生复利效应。每周优化一次。输出不满意时，九成是 context 问题而非 prompt 问题——在文件里加一行，永久解决。

## 4\. 使用 Folder Instructions 添加项目专属 Context

三层叠加逻辑：Global Instructions 设定通用行为，Folder Instructions 添加项目 context（客户名、目标、术语、截止日），Prompt 指定具体任务。三层，一层比一层具体。这就是从"通用 AI 输出"到"听起来像在团队待了六个月的同事"的路径。

## 5\. 主动管理 Context 范围，不要让 Claude 读取一切

更大的 context 不等于更好的输出。无关文件越多，噪音越多，输出越差。在 Global Instructions 中加入：

> 开始任务时，先查找 \_MANIFEST.md。 加载 Tier 1 文件。仅当任务涉及某领域时才加载 Tier 2。 除非我明确要求，否则不加载 Tier 3。

如果使用 subagent，范围要更精细：

> 分解任务时，只给每个 subagent 其子任务所需的最少 context。

## Part 2：Task Design（实践 6–10）

## 6\. 定义终态，而非过程

Cowork 是协作者，不是 chatbot。告诉它"完成是什么样子"，而不是"怎么做"。

差的 prompt："帮我处理这些文件。"

好的 prompt："将此文件夹中所有文件按客户名称整理到子文件夹。文件名使用 YYYY-MM-DD-描述性名称 格式。创建记录每次更改的 summary log。不删除任何内容。如果一个文件可能属于多个客户，放入 /needs-review。"

每个任务 prompt 都应回答三个问题：完成是什么样的？约束条件是什么？不确定时该怎么做？

## 7\. 执行前始终要求 Plan

在 Global Instructions 中加入："在任何任务上采取行动前，先展示简短 plan。等待我批准后再执行。"

这一行能防止90%的 Cowork 灾难。代价是每次任务多30秒，收益是永远不需要撤销一个持续了20分钟的自主错误。

## 8\. 告诉 Claude 不确定时该怎么做

大多数人对顺利路径给出了清晰指令，却对边缘情况只字未提。Claude 会猜，而猜测往往错误——不是因为它笨，而是因为它不了解你在模糊情况下的偏好。把 uncertainty handling 写入每个任务：

> 如果日期不清晰，标记为 VERIFY。 如果文件可能属于多个文件夹，放入 /needs-review。 如果分类把握不足80%，标记它而不是猜测。

这将 Cowork 从"偶尔出错的工具"变成"精确告诉你在哪里需要你判断的工具"。

## 9\. 将相关工作合并到单次 Session 中

每次 session 都有 startup cost。不要为五个相关任务开五个 session，合并成一次："处理本月费用收据、更新预算表、生成 summary report、起草发给财务的邮件，并保存到 /monthly-reports/february。"

Claude 会跨任务共享 context（收据 → 预算 → 报告 → 邮件），在一次运行中产出五个相互关联的 deliverable。更快、更省、质量更高。

## 10\. 主动使用 Subagent，要求并行处理

当你给 Cowork 一个有独立部分的任务时，它可以启动多个 subagent 同时处理。触发方式是在 prompt 中加入"Spin up subagents to..."或"使用 subagent 并行处理这些"。

例如评估四家供应商，串行需要40分钟，启动四个并行 subagent 只需10分钟。适用场景包括竞争分析、多源研究、批量文件处理、多角度评估选项等。

注意：subagent 在 Opus 4.6 上效果最佳，消耗更多 token，应当用于复杂任务，不要用来整理 Downloads 文件夹。

## Part 3：Automation & Scheduling（实践 11–13）

## 11\. 用 /schedule 安排 Recurring Tasks

在任意任务中输入 /schedule，Claude 会引导你设置每日、每周、每月或按需自动运行的任务。

作者设置过的最佳案例：周一早7点汇总 Slack 和日历生成本周 briefing，保存到 /weekly-briefings；周五下午4点从 Asana 拉取已完成任务起草 status update，保存到 /reports；每天早9点追踪竞争对手动态，仅在有新内容时保存摘要。

需要注意的限制：任务只在电脑开启且 Claude Desktop 运行时才执行。如果到期时电脑休眠，Cowork 会在你回来后补上并通知你。

## 12\. 一次构建，每周运行——将一切外化为文件

Cowork 在 session 间没有 memory，这是设计特性而非缺陷。没有 memory 意味着没有 context 污染，没有几周前的幻觉式回忆，每次 session 全新开始。但这也意味着你不能依赖"Claude 记得我喜欢这样做"。

解决方案是将一切外化为文件：偏好存在 context 文件中，项目计划存在 markdown 文档中，标准操作程序存在 skill 文件中，决策与结果存在 log 文件中。

一个有完整文档的 workflow 是可移植的、可共享的、可版本控制的——它不存在于 AI 的 memory 中，它存在于你的系统中。

## 13\. /schedule + Connector 组合，实现真正的自动化

Scheduled task 与 connector 结合时才真正强大。连接 Gmail、Slack、Google Drive、Notion、Asana 等50多个 integration，然后安排拉取实时数据的任务：

> 每周一：拉取 #product-feedback 未读 Slack 消息 → 按主题分类 → 创建摘要到 Google Drive 每天早上：检查 Gmail 发票 → 提取金额和日期 → 更新本地费用表

这是 Cowork 从 task executor 变成 autonomous system 的转折点。路径：Settings → Connectors → Browse connectors，从 Slack 和 Gmail 开始。

## Part 4：Plugins & Skills（实践 14–16）

## 14\. 叠加 Plugin，实现复合能力

每个 plugin 都是针对特定领域设计的 skill、slash command 和 subagent 配置包。但大多数人忽视的是：plugin 是可组合的。你可以安装多个 plugin，在单个任务中调用所有 plugin 的能力。

例如安装 Data Analysis plugin 和 Sales plugin，然后说："分析 Q1 pipeline 数据，识别三个最弱的 deal，并为每个起草个性化 follow-up 邮件。"Claude 在一个 workflow 中同时使用了两个 plugin 的能力。

推荐 plugin stack：Productivity（常开）+ Data Analysis（常开）+ Sales 或 Marketing（按需轮换）。

## 15\. 为你的 Workflow 构建自定义 Skill

Skill 是教 Claude 如何处理特定、可重复任务的 markdown 文件。标准结构如下：

> \[markdown\] # \[Skill Name\] ## Purpose：此 skill 的作用 ## Inputs：Claude 需要什么信息 ## Process：分步骤说明 ## Output：成品 deliverable 的样子 ## Constraints：规则和 guardrail

一旦创建，只需说"对\[主题\]运行我的文章起草 skill"——把原本需要20分钟解释的 prompt 压缩成一句话。将自定义 skill 保存为工作文件夹中的 .md 文件，或通过 Customize 菜单上传。

## 16\. 用 Plugin Management Plugin 通过对话构建 Plugin

安装 Plugin Management plugin，然后说："帮我为\[你的 workflow\]创建一个 plugin。"Claude 会引导你通过对话定义 skill、slash command 和配置——无需写代码，无需 GitHub，无需学 markdown 语法。你描述，Claude 构建，你测试，你优化。不到一小时就能拥有一个专属 workflow plugin。

对团队尤其有价值：一人构建，全团队安装，标准统一存在于 plugin 中而非个人 memory 里。企业团队可以使用 Anthropic 在二月份推出的 private plugin marketplace，管理员可以在整个组织中创建、整理和分发自定义 plugin。

## Part 5：Safety & Efficiency（实践 17）

## 17\. 把 Cowork 当作强大的员工，而不是玩具

Cowork 拥有真实的文件系统访问权限，可以创建、移动、重命名，甚至删除文件。它可以浏览网络，与连接的工具交互，还能无监督运行数小时。这种能力需要被认真对待。

实验前先备份——尤其是文件组织任务。"大多数时候正确"对客户合同来说不够。

敏感文件单独隔离——财务、密码、个人信息，放在 Cowork 永不触碰的文件夹。不要授予整个 Documents 目录的访问权限，要精确限定范围。

默认加入"不删除任何内容"——即使有 deletion confirmation，也要从源头防止误删。

新 workflow 的前几次运行要监控——观察 Claude 做什么，阅读 plan，检查 output。建立信任后再放手。

注意 prompt injection 风险——如果 Claude 读取了恶意文档或网站，隐藏的指令可能改变其行为。不要让 Cowork 指向未审查的文件或陌生 URL。

追踪 usage——复杂的多步骤任务很消耗配额。优先用批量 session、用"只修改第2节"代替"重做一切"、通过文件预加载 context 而不是在 chat 中重新解释。

## 17个实践背后的规律

如果往后退一步，这个列表上的每个实践都遵循同一个原则：投资于搭建，减少 prompting。

在 Cowork 上挣扎的人，是在为每个任务写又长又详细的 prompt，却得到不稳定的结果。在 Cowork 上蓬勃发展的人，花了一个下午构建他们的 context architecture——manifest 文件、global instructions、context 文件、folder instructions、自定义 skill——现在只需写十个词的 prompt，就能产出客户可用的 deliverable。

ChatGPT 时代奖励 prompt engineering，Cowork 时代奖励 system engineering。

Prompt 是 Cowork session 中最不重要的部分。Context、结构、skill 和 constraint——那才是输出质量的来源。

## 实施 Checklist

今天（30分钟）

- 创建三个 context 文件 + 设置 Global Instructions（超越95%的用户）

本周

- 为最常用项目文件夹添加 \_MANIFEST.md + 安装2–3个 plugin + 设置一个 scheduled task

本月

- 构建第一个自定义 skill + 尝试 subagent + 根据输出质量优化 context 文件

知道这17个实践的人与不知道的人之间的差距，已经很巨大了。六个月后，那将是一道峡谷。