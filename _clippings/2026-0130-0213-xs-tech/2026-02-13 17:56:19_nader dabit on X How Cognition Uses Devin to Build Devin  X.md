---
title: ""
source: "https://x.com/dabit3/status/2021702398775812135"
author: ""
created: 2026-02-13 17:56:19
date: 2026-02-13 17:56:19
description: ""
tags: ""
---
你好，我是纳德， ，@DevinAI 的创建者 。

Devin 是

面向工程团队的。你可以像对待队友一样与 Devin 协作——在 Slack 或 Linear 等平台上给它分配任务，审核它的 PR（拉取请求），并让它处理你的待办事项。

加入后，我想了解高级用户是如何使用 Devin 完成实际软件工程工作的。以下是我了解到的：

设置如下：添加任何你希望 Devin 管理的代码库。

然后你会得到一个统一界面，在这个界面中你可以使用自然语言在你所有的代码仓库中工作。

它被设计为对话式界面，因此我们可以以和给队友发消息相同的方式与它聊天——通过 Slack、CLI、Linear 或 Jira 工单，或网页应用。

在任何频道中@Devin。如果需要，包含附件。像在普通聊天界面中那样来回沟通。

[

![Image](https://pbs.twimg.com/media/HA59kw-XwAAmR8E?format=jpg&name=medium)



](https://x.com/dabit3/article/2021702398775812135/media/2021691353311199232)

一个强大的成果是，任何人都能贡献，无论其技术专长或在公司中的角色，他们无需理解和设置 Git 或任何命令行工具就能开始为我们的代码库做贡献。

用请求标记@Devin，我们会得到一个可以审查和测试的 PR。

如果有人发现过时的文档或错误（比如），他们会在 Slack 上发一条简短消息来修复它，然后继续过他们的一天。

[

![Image](https://pbs.twimg.com/media/HA5-Lr7bUAA8ZS6?format=jpg&name=medium)



](https://x.com/dabit3/article/2021702398775812135/media/2021692021971570688)

这消除了快速迭代和优化的摩擦与障碍，也减少了上下文切换。

当工程师看到他们的队友在自己每天都使用的同一个代码库上借助 Devin 完成的工作时，他们会有“哦，真的吗？Devin 能做到吗？”的反应，于是这种情况就会自然传播开来。

[

![Image](https://pbs.twimg.com/media/HA5-TtCbsAA_hL1?format=jpg&name=medium)



](https://x.com/dabit3/article/2021702398775812135/media/2021692159708344320)

Devin 可以通过 Devin 工作区使用三个核心工具：

Shell.Devin 的终端，在这里你可以查看命令执行过程并查看输出日志。你可以复制 shell 输出用于调试，或者当你接管时，直接运行命令。

IDE。一个加载了你的仓库的嵌入式 VSCode 环境。你可以实时观察 Devin 进行编辑，使用所有你喜欢的快捷键，跳转到定义，在标签页中打开文件等等…

浏览器。观察 Devin 浏览文档、测试它构建的 Web 应用程序或下载信息。您可以通过交互式浏览器介入，协助处理验证码、多因素认证或复杂导航。

进度标签页将这三者整合到一个统一视图中。点击会话中的任意步骤，即可确切查看 Devin 的操作内容。

随着我们通过代理发布更多代码，瓶颈从编写代码转移到了代码审查。

Devin Review 将大型、复杂的 GitHub 拉取请求转换为直观组织的差异和精确的解释。我们现在每个拉取请求都使用它。

![](https://pbs.twimg.com/tweet_video_thumb/HA5-2KJWIAANeI7.jpg)

每次 Devin 在 Slack 上提交 PR 时，都会包含一个 Devin Review 链接，因此已整理的差异始终只需一键即可访问。

[

![Image](https://pbs.twimg.com/media/HA5-9oabsAAl5S0?format=jpg&name=large)



](https://x.com/dabit3/article/2021702398775812135/media/2021692880021336064)

-   。如果 Devin Review 或 GitHub 机器人标记了 bug，Devin 会自动修复 PR。Devin 还会处理 CI/lint 问题，直到所有检查通过，结束代理循环。
    
-   智能差异组织。按逻辑分组变更，将相关修改集中，而非按字母顺序排列。
    
-   复制和移动检测。检测到代码被复制或移动时，清晰地显示变更，而不是完全删除和插入。
    
-   Bug Catcher。自动分析拉取请求中的潜在问题，并根据置信度对其进行标记。严重的 bug 需要立即处理。非严重的 bug 仍需审核。标记是信息性注释。
    
-   代码库感知聊天。询问有关 PR 的问题，并从代码库的其他部分获取带有相关上下文的答案。
    

对于任何 GitHub PR 链接，你可以替换

替换为

在 URL 中。

一旦自动评审（Auto-Review）配置完成，Devin 会在 PR 被打开、新提交被推送或有人被添加为评审者时，自动开始评审 PR。

一旦你将代码仓库添加到 Devin，它就会被自动索引。Ask Devin 会成为了解该代码库的窗口。

我们在开始会话前，经常用它来进行范围界定工作。工作流程：使用 Ask Devin 探索代码并明确你的目标，然后直接从搜索界面启动会话。

Devin 从你探索中获得的清晰上下文开始，并且提示词会自动适配你的任务。

[

![Image](https://pbs.twimg.com/media/HA5_QNoWwAAPa2R?format=jpg&name=medium)



](https://x.com/dabit3/article/2021702398775812135/media/2021693199249489920)

相同的工作流适用于 Jira 或 Linear 集成。

在工单上标记 Devin。Devin 分析任务，搜索代码库，并规划其方法。它会自动生成高质量的会话提示。

[

![Image](https://pbs.twimg.com/media/HA5_ZEYbsAERIQe?format=jpg&name=medium)



](https://x.com/dabit3/article/2021702398775812135/media/2021693351385608193)

借助 DeepWiki，Devin 会自动索引所有代码仓库，并生成包含架构图、源代码链接和代码库摘要的 Wiki。

我们用它来快速熟悉代码库中不熟悉的部分。Ask Devin 使用 Wiki 中的信息来更好地理解并找到相关背景信息。

对于公开仓库，

会自动生成架构图、源代码链接和文档，无需设置

[

![Image](https://pbs.twimg.com/media/HA5_k9PXwAAucK_?format=jpg&name=medium)



](https://x.com/dabit3/article/2021702398775812135/media/2021693555626983424)

DANA 是针对数据库查询、数据分析和创建可视化内容进行了优化的 Devin 专用版本。

我们用它来处理关于我们数据仓库的问题、构建仪表盘以及回答数据问题，而不会让工程师停下手头的工作。它也成为了非工程类任务的首选工具——那种“点击一堆按钮来填写报告”的工作过去常常会占用大量时间。

我们可以通过点击代理选择器下拉菜单从网页应用访问 DANA，或者在 Slack 中使用/dana 命令或@Devin！dana，然后输入我们的问题。

[

![Image](https://pbs.twimg.com/media/HA5_y-9WwAEfIkg?format=jpg&name=medium)



](https://x.com/dabit3/article/2021702398775812135/media/2021693796606459905)

我们已经学会了明确指标、包含时间周期，并在可视化能提供帮助时请求可视化。

DANA 通过 MCP 连接到你的数据仓库——Redshift、PostgreSQL、Snowflake、BigQuery，无论你运行的是哪种（数据仓库系统），它都维护着自己的数据库知识，因此在你提出任何问题之前就已经理解你的数据模式。

它针对简洁、侧重指标的回答进行了优化，内置 seaborn 可视化功能，因此您可以快速获得图表和洞察结果，而不是等待工程师切换到 SQL 客户端的上下文。

我们发现，对于那些过去常常在某人的待处理队列中搁置数天的临时问题——比如“周二注册量为何下降？”或“按企业版和自助版分解消费情况”——团队中的任何人只需在 Slack 中提问，就能得到包含 SQL 代码的答案，从而验证逻辑。

Playbook 就像是用于重复任务的自定义系统提示。

如果你发现自己在多个 Devin 会话中重复相同的指令，你就需要一个 Playbook。

[

![Image](https://pbs.twimg.com/media/HA6ACzKbsAMZcuP?format=jpg&name=medium)



](https://x.com/dabit3/article/2021702398775812135/media/2021694068317990915)

一旦任何人使用 Devin 取得成功，其他人就能复制这种成功。

-   我们希望 Devin 达成的结果
    
-   到达那里所需的步骤
    
-   描述后置条件的规范
    
-   纠正 Devin 先验知识的建议
    
-   禁止操作
    
-   发起者所需的任何必要输入或背景信息
    

Playbooks 使 Devin 能够独立处理复杂工作，从将数据导入 Redshift 和执行数据库迁移，到使用 Stripe、Plaid、Modal 和 Storybook 等各种 API。

MCP 使 Devin 能够使用数百个外部工具和数据源。

我们使用 MCPs 挖掘 Sentry、Datadog 和 Vercel 的日志。在 Slack 中连接数据库 MCPs 以进行数据分析。从 Notion、Airtable 和 Linear 等工具中提取上下文。

[

![Image](https://pbs.twimg.com/media/HA6AOzzWcAA1yfB?format=jpg&name=medium)



](https://x.com/dabit3/article/2021702398775812135/media/2021694274648043520)

许多都可以一键启用——Vercel、Atlassian、Notion、Sentry、Neon、Asana、Jam 以及更多。

会话洞察分析已完成的 Devin 会话，并提供用于改进的可操作建议。

-   问题与挑战（技术问题、沟通障碍、范围蔓延）
    
-   会话时间线与关键里程碑及效率指标
    
-   行动项包括立即改进和流程优化
    
-   改进的提示建议与增强的指令
    

我们利用一个会话中的洞察来指导下一个会话。你可以直接从这些洞察中使用改进后的提示来启动新的会话。随着时间的推移，会话会变得更加高效。

Devin 提供完整的 REST API，因此代理无需人工介入即可启动工作。将 Devin 连接到您现有的系统，并通过编程方式触发会话：

-   一份崩溃日志从 Sentry 到达 → Devin 调查并打开了一个 PR
    
-   一个错误报告被提交 → Devin 复现、诊断并修复
    
-   部署失败 → Devin 分析日志并提出修复方案
    
-   请求进行代码审查 → Devin 审查并留下评论
    

最成功的 Devin 任务对我们来说验证起来很快——检查 CI 是否通过、测试自动部署。

-   针对性重构
    
-   小型前端功能
    
-   错误修复和边界情况
    
-   提高测试覆盖率
    
-   调查 CI 失败
    
-   Lint 错误和 CVE 漏洞修复
    
-   语言迁移和框架升级
    
-   PR 审核
    
-   代码库问答
    
-   编写单元测试
    
-   维护文档
    
-   现代化与迁移
    
-   通过静态分析修复安全漏洞
    

我们的经验法则是：如果一名初级工程师在有足够指导的情况下能够弄明白，那就是一个好的 Devin 任务。

大规模挑战需要分解为更小的、独立的任务，分布在不同的会话中。

UI 美学需要人工协助。Devin 能够构建功能型前端，但在设计打磨方面缺乏良好的审美眼光。

对于任何需要广泛测试和验证的事物，我们确保验证机制已经到位。

2.  连接你的 GitHub、GitLab 或 Bitbucket
    
3.  添加你的第一个代码仓库
    
4.  以一个简单的任务开始会话
    

-   添加知识以教 Devin 你的代码库规范
    
-   创建用于重复任务的剧本
    
-   连接 Slack 以进行内联协作
    
-   为你的工具启用 MCPs
    
-   在开始工作会话前，使用 Ask Devin 来确定复杂工作的范围
    

把 Devin 当作团队成员对待。给它提供上下文。教它你们的规范。让它处理待办事项，而你专注于需要资深判断的工作。

一位拥有清晰上下文、能自主处理范围明确任务的 AI 软件工程师是一位效能倍增器。

由@cognition 团队打造。如果你正在使用@DevinAI 开发，我们很乐意听听你的情况。