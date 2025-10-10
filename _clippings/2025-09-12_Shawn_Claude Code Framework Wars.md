---
title: "Claude Code Framework Wars"
source: "https://shmck.substack.com/p/claude-code-framework-wars"
author:
  - "[[Shawn]]"
published: 2025-09-12
created: 2025-09-12
description: "How developers are experimenting with structure, orchestration, and standards to get more out of AI coding."
tags:
  - "Shawn"
status: "inbox"
importance: 2
effort: 2
review_level: 0
review_next: "2025-10-17"
review_interval: null
review_count: 0
decision: null
topics: []
links_out: []
summary: ""
pov: ""
actions: []
---
### 开发者们如何通过试验结构、编排和标准，从人工智能编码中获取更多价值。

作为软件开发人员，我们才刚刚开始学习如何与人工智能合作。

核心观点： **Claude 可以实现编码自动化，而你则可以转型为项目经理、设计师和软件架构师等更具价值的角色。** 关键在于不再将 Claude 仅仅视为一个聊天框，而是将其当作一个 **框架** ——一组规则、角色和工作流程，这些能让它的输出具有可预测性和价值。

更有意思的是——克劳德代码并不需要代码才能成为一个框架，只需要结构化提示即可。而目前，开发者社区正在进行疯狂的试验——你可以称之为\*\*克劳德代码框架之战\*\*。数十个开源项目正在测试不同的方法，以探索如何高效地与人工智能合作。

以下是一份实地报告。

![](https://substackcdn.com/image/fetch/$s_!ZKCU!,w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4aca2f45-4920-4dc6-94f3-bc1269aea406_1536x1024.png)

---

## 决策菜单

如果你正在设计自己的 Claude 设置，你需要做出七个重大选择：

1. Where tasks live?
2. 你如何引导 Claude？
3. 智能体如何进行协调？
4. 会话是如何运行的？
5. 代码如何访问工具？
6. 代码是如何开发的？
7. 代码是如何交付的？
8. 上下文是如何保存的？

可以把它想象成布置一个厨房。Claude 是负责烹饪的厨师，但你需要决定：食谱放在哪里，厨师如何学习餐厅的烹饪风格，谁来管理厨房，以及食物如何上桌？

### 1\. Where Tasks Live

Claude 需要一个真相来源。

- **Markdown 待办事项列表：** 以 markdown 格式将任务作为待办事项列表。
	示例：Backlog.md、ReqText。
- **结构化文本：** 指定转换为任务的产品规格。*Example: [Agent OS](https://github.com/buildermethods/agent-os)*
- **问题/工单：** 将规范存储为 GitHub 问题或 Jira 工单，并将它们与代码审查关联起来。
	*Example:*[ccpm](https://github.com/automazeio/ccpm)

**要点：** 任务必须存放在 Claude 能够看到且你能够追踪的地方。

### 2\. 克劳德是如何被引导的

用结构化内容替换模糊的提示。

- **命令库：** 预建的斜杠命令（例如 /create-tasks，/review）。
- **编码标准** ：明确技术栈、编码指南
- **完成定义：** 对“完成定义”进行编码
- **触发验证钩子** ：对每次更改强制执行代码检查和测试
- **作为评审者的 Claude：** Claude 作为开发者和评审者

**要点：** 当规则清晰且可重复时，Claude 的工作表现更佳。

### 3\. 智能体如何协调

多个 Claude？给它们分配角色和制定计划。

- **角色模拟：** 人工智能充当项目经理、架构师、开发人员、测试人员。
	*Example:*[Agent OS](https://github.com/buildermethods/agent-os)
- **群体并行性：** 多个智能体在结构化流程中同时运行（例如：规范 → 伪代码 → 代码 → 测试）。
	*示例：* [Claude-Flow](https://github.com/ruvnet/claude-flow) 。
- **仓库原生工件：** 将任务、日志和架构决策记录存储在代码库中，以便内存持久化。
	*示例：* [袋鼠指挥官](https://github.com/jezweb/roo-commander) 。

**要点：** 协作可避免许多人工智能工作者相互掣肘。

### 4\. 会话如何运行

人工智能输出可能会变得混乱——会话是你的工作站设置。

- **终端编排：** Claude 可控制命令、面板和日志。
	示例：交响曲，克劳德小队。
- **并行工作树：** [使用 Git 工作树并行运行多个分支](https://docs.anthropic.com/en/docs/claude-code/common-workflows#run-parallel-claude-code-sessions-with-git-worktrees) 。
	*Example:*[Crystal](https://github.com/stravu/crystal).
- **并行容器** ： [在隔离容器中运行 Claude](https://docs.anthropic.com/en/docs/claude-code/devcontainer) 以避免冲突  
	*Example: [ClaudeBox](https://github.com/RchGrav/claudebox)*

**要点：** 通过并行运行任务且避免频繁冲突来提高工作效率

### 5\. 克劳德如何访问工具

向 Claude 提供有关您整个技术栈的信息。

- **MCP 集成（模型上下文协议）：** 捆绑的 MCP 服务器，可将 Claude 连接到外部资源，如浏览器、数据库、测试运行器，甚至 UI 自动化框架。
- **自定义工具库：** 内置 shell 脚本和命令  
	Example: [Symphony](https://github.com/sincover/Symphony)
- **数据库访问器：** 用于强大数据库访问的工具  
	示例： [可与 Supabase 配合使用的 Claudable](https://github.com/opactorai/Claudable)
- **测试与验证钩子：** 在宣布工作“完成”之前运行测试（例如，Vitest、Jest）。这将 Claude 的输出与实际验证循环联系起来  
	Example: [Agent OS](https://github.com/buildermethods/agent-os)

**要点：** 工具将 Claude 从“一个智能自动完成工具”转变为“一个积极的团队成员”，能够检查自身工作并与你的系统进行交互。

### 6\. 代码是如何开发的

根据你的需求，Claude 可以扮演不同的角色：

- **项目经理（PM）：** 将产品规格转化为任务和待办事项
	*示例：* [ccpm](https://github.com/automazeio/ccpm) ， [智能体操作系统](https://github.com/buildermethods/agent-os)
- **架构师：** 在编码开始前设计整体结构、定义接口并设定规范。
- **实现者：** 在这些护栏内编写代码，遵循测试和标准。
- **问答：** 审核工作以查找问题  
	*Example*: [BMAD-code](https://github.com/bmad-code-org/BMAD-METHOD)
- **审核人员：** 审核拉取请求的质量、可读性和风险。

**要点：** 在软件生命周期的每个阶段利用人工智能。

### 7\. 代码的交付方式

代码是如何到达你的代码库的？

- **小差异：** 人工智能提取工单并生成小型拉取请求，且始终经过审核。
	*Example:*[ai-ticket](https://github.com/jmikedupont2/ai-ticket).
- **实验：** 在功能特性开关后部署更改
- **完整应用程序脚手架：** 人工智能根据高级提示构建并部署整个应用程序。
	*Example:*[Claudable](https://github.com/opactorai/Claudable).

**要点：** 选择你的规模——用于生产的安全迭代，用于原型的脚手架。

### 8\. 上下文是如何保存的

克劳德会遗忘。框架会记住。

- **文档和日志：** 保持 CLAUDE.md、架构笔记和项目日志的时效性。
	*示例：* [克劳德指挥器](https://github.com/superbasicstudio/claude-conductor) 。
- **持久内存与检查：** 回顾近期工作，运行项目健康检查，存储决策。
	*示例：* [Claude-Flow](https://github.com/ruvnet/claude-flow) 。

**要点：** 没有记忆，人工智能会不断重复错误。有了记忆，它能累积进步。

## Putting It Together

可以把这些选项想象成一个菜单。你不必一下子把所有东西都点了。

- **新手设置：** Markdown 待办事项列表 + 工单差异。
- **结构化团队：** 产品规格 + 标准 + 角色模拟。
- **大量实验：** 仓库工件 + 并行会话。
- **原型模式：** 应用构建器 + 文档搭建框架。

## The Payoff

早期从克劳德代码框架之战中得到的教训很简单：\*\*当你为人工智能赋予结构时，它的表现最佳\*\*。

Claude 并没有取代开发者，而是在转变他们的角色。你花在编写样板代码上的时间减少了，而花在制定规范、审查设计和定义架构上的时间增多了。如果你不尽职，事情很快就会偏离正轨。

我们仍处于早期阶段，但这些框架正朝着一个未来发展，在这个未来中，人工智能不再是一个魔法盒子，而是\*\*一组你要管理的队友\*\*。而这正是令人兴奋的部分：你给予的结构越多，得到的回报就越多。