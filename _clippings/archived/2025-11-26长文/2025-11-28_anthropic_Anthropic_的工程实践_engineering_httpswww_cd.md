---
title: "2025-11-28_anthropic_com_Anthropic_的工程实践_engineering_httpswww_cd"
source: "https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents"
author:
  - "[[@anthropic.com]]"
published: 2025-11-28
created: 2025-11-28
description:
tags:
  - "#multi"
  - "anthropic"
  - "@anthropic.com"
  - "claude"
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

# [Anthropic 的工程实践](engineering) ![](httpswww-cd

[Anthropic 的工程实践](/engineering) ![](https://www-cdn.anthropic.com/images/4zrzovbb/website/5dfb835ad3cbbf76b85824e969146eac20329e72-1000x1000.svg)

## 持久运行智能体的高效控制机制

随着人工智能代理能力的提升，开发者越来越多地要求它们承担需要数小时甚至数天才能完成的复杂任务。然而，让代理在多个上下文窗口中持续取得进展，仍然是一个悬而未决的难题。

长时运行智能体的核心挑战在于，它们必须在离散的会话中工作，而每个新会话开始时都没有先前会话的记忆。设想一个由轮班工程师组成的软件项目，每位新到岗的工程师都对上一班次的工作内容毫无记忆。由于上下文窗口存在限制，且大多数复杂项目无法在单一窗口内完成，智能体需要一种机制来弥合不同编程会话之间的断层。

我们开发了一套双重解决方案，使 [Claude 智能体 SDK](https://platform.claude.com/docs/en/agent-sdk/overview) 能够在多个上下文窗口中高效运作：包含负责首次运行时环境配置的 **初始化智能体** ，以及负责在每次 **会话** 中实现渐进式进展、同时为后续会话留存清晰成果的 **编程智能体** 。您可以在随附的 [快速入门指南](https://github.com/anthropics/claude-quickstarts/tree/main/autonomous-coding) 中查看代码示例。

## 长时运行智能体问题

Claude Agent SDK 是一款功能强大的通用智能体框架，擅长编程以及需要模型使用工具来收集上下文、规划和执行的其他任务。它具有上下文管理功能，例如压缩，使智能体能够在处理任务时不会耗尽上下文窗口。理论上，在这种设置下，智能体应该能够无限期地持续进行有效工作。

然而，仅靠压缩是不够的。如果只给出高层级提示（例如"构建一个 [claude.ai](http://claude.ai/redirect/website.v1.bcd1298e-326f-4965-891e-6a83e9eec7ca) 的克隆版本"），即使像 Opus 4.5 这样的前沿编码模型通过 Claude Agent SDK 在多个上下文窗口中循环运行，也难以构建出生产级质量的网络应用。

Claude 的失败呈现出两种模式。首先，智能体倾向于一次性尝试过多任务——本质上试图一蹴而就地完成整个应用。这常常导致模型在实施过程中耗尽上下文，使得后续会话不得不从半成品功能且缺乏文档的状态开始。智能体随后只能猜测之前发生的情况，并花费大量时间试图让基础应用重新运转。即便采用上下文压缩技术，这种情况仍会发生，因为压缩后的指令并不总能清晰传递给下一个智能体。

项目的后期常会出现第二种失效模式：当部分功能已开发完成后，后续的智能体实例会环顾四周，发现已有进展，便宣告任务完成。

这便将问题分解为两个部分。首先，我们需要建立一个初始环境，为特定提示所需 *所有* 功能奠定基础，使智能体能够逐步开展工作并feature-by-feature.其次，我们应引导每个智能体朝着目标持续取得进展，同时在会话结束时保持环境的清洁状态。所谓"清洁状态"，是指适合合并到主分支的代码标准：不存在重大错误，代码结构井然且文档完善，开发者无需先清理无关的混乱代码，就能直接着手新功能的开发。

在内部实验过程中，我们采用双管齐下的方案来解决这些问题：

1.  初始化代理：首个代理会话采用专门提示，要求模型设置初始环境：包括一个 `init.sh` 脚本、一个记录代理操作日志的claude-progress.txt文件，以及显示所添加文件的初始 git 提交。
2.  编程助手：每次后续会话都会要求模型逐步推进，并留下结构化的更新。 1

此处的关键洞见在于，为智能体找到一种在全新上下文窗口启动时快速理解工作状态的方法，这通过结合claude-progress.txt文件与 git 历史记录得以实现。这些实践方法的灵感来源于观察高效软件工程师的日常操作。

## 环境管理

在更新版 [Claude 4 提示指南](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#multi-context-window-workflows) 中，我们分享了多上下文窗口工作流的一些最佳实践，包括采用"首个上下文窗口使用不同提示"的框架结构。这种"差异化提示"要求初始化代理预先配置好运行环境，为后续编程代理高效工作备齐所有必要上下文。本文将深入探讨此类环境搭建的关键组件。

### Feature list

为解决智能体一次性完成应用或过早认为项目完成的问题，我们提示初始化智能体编写详细的功能需求文件，对用户初始提示进行扩展。在 [claude.ai](http://claude.ai/redirect/website.v1.bcd1298e-326f-4965-891e-6a83e9eec7ca) 克隆示例中，这意味着需定义 200 多项功能，例如“用户能打开新对话窗口、输入查询内容、按下回车键并看到 AI 响应”。这些功能最初均标记为“未实现”，以便后续编程智能体能清晰了解完整功能的全貌。

我们指示编程智能体仅通过修改测试通过状态字段来编辑此文件，并使用措辞强硬的指令如“绝不允许删除或修改测试用例，否则可能导致功能缺失或产生缺陷”。经过多次实验，我们最终确定采用 JSON 格式进行此项操作，因为相较于 Markdown 文件，模型更不容易对 JSON 文件进行不当修改或覆盖。

### 逐步进展

有了这个初始环境框架后，新版编程助手被要求每次只专注于一个功能开发。这种渐进式方法对于纠正助手试图一次性处理过多任务的倾向起到了关键作用。

一旦采用渐进式工作方式，模型在修改代码后保持环境整洁仍然至关重要。在我们的实验中，我们发现最佳实践是要求模型通过描述性提交信息将进度提交至 git，并在进度文件中记录工作摘要。这使得模型能够利用 git 回退不良代码变更，并恢复代码库的可运行状态。

这些方法还提高了效率，因为它们消除了智能体需要猜测发生了什么并花费时间尝试让基础应用程序重新运行的必要。

### Testing

我们观察到的最后一个主要故障模式是，Claude 倾向于在未经充分测试的情况下将功能标记为已完成。在没有明确提示的情况下，Claude 往往会进行代码修改，甚至通过单元测试或针对开发服务器的 `curl` 命令进行测试，但未能意识到该功能无法端到端正常运行。

在构建网络应用时，一旦明确提示 Claude 使用浏览器自动化工具并像真实用户那样进行全流程测试，它大部分情况下都能出色完成端到端的功能验证。

![ Screenshots taken by Claude through the Puppeteer MCP server as it tested the claude.ai clone. ](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Ff94c2257964fb2d623f1e81f874977ebfc0986bc-1920x1080.gif&w=3840&q=75)

Claude 通过 Puppeteer MCP 服务器在测试 claude.ai 克隆版时截取的屏幕截图。

为 Claude 配备这类测试工具显著提升了其性能，因为它能够识别并修复仅从代码本身难以察觉的错误。

一些挑战依然存在，比如 Claude 的视觉能力和浏览器自动化工具的限制，使得难以识别所有类型的错误。例如，Claude 无法通过 Puppeteer MCP 看到浏览器原生的警告弹窗，因此依赖这些弹窗的功能往往更容易出现缺陷。

## Getting up to speed

在完成以上所有设置后，每个编程智能体都会按照一系列步骤来明确自身定位，其中有些步骤虽然基础却依然实用：

1.  *运行 `pwd` 命令查看当前工作目录，您只能编辑该目录下的文件。*
2.  *阅读 git 日志和进度文件，快速了解近期工作进展。*
3.  *阅读功能列表文件，并选择尚未完成的最高优先级功能进行开发。*

这种方法在每个会话中为 Claude 节省了一些令牌，因为它无需思考如何测试代码。同时，让初始化代理编写能运行开发服务器的 init.sh 脚本，并在实现新功能前进行基础端到端测试也很有帮助。

对于 claude.ai 克隆项目而言，这意味着智能体始终会启动本地开发服务器，并利用 Puppeteer MCP 执行新对话创建、消息发送和响应接收的全流程。这套机制确保 Claude 能快速识别应用是否处于异常状态，并立即修复现存缺陷。若智能体转而着手开发新功能，反而可能加剧系统问题。

有鉴于此，典型的会话通常以下列助手消息开场：

```
[Assistant] I'll start by getting my bearings and understanding the current state of the project.
[Tool Use] <bash - pwd>
[Tool Use] <read - claude-progress.txt>
[Tool Use] <read - feature_list.json>
[Assistant] Let me check the git log to see recent work.
[Tool Use] <bash - git log --oneline -20>
[Assistant] Now let me check if there's an init.sh script to restart the servers.
<Starts the development server>
[Assistant] Excellent! Now let me navigate to the application and verify that some fundamental features are still working.
<Tests basic functionality>
[Assistant] Based on my verification testing, I can see that the fundamental functionality is working well. The core chat features, theme switching, conversation loading, and error handling are all functioning correctly. Now let me review the tests.json file more comprehensively to understand what needs to be implemented next.
<Starts work on a new feature>
```

智能体的故障模式与应对方案

| **Problem** | **初始化智能体行为** | **编程智能体行为** |
| --- | --- | --- |
| Claude 过早地宣布了整个项目的胜利。 | 创建功能清单文件：根据输入规范，设置一个包含端到端功能描述的结构化 JSON 文件。 | 在会话开始时读取功能列表文件，选择单个功能开始处理。 |
| Claude 离开了环境，留下了一些错误或未记录的进展。 | 初始的 Git 仓库和进度记录文件已创建完成。 | 启动会话时，先读取进度记录文件和 git 提交日志，并在开发服务器上运行基础测试以发现未记录的缺陷。结束会话时，编写 git 提交并更新进度记录。 |
| Claude 过早地标记功能已完成。 | 创建功能列表文件。 | 对所有功能进行自检。只有在仔细测试后，才将功能标记为“通过”。 |
| Claude 需要花时间弄清楚如何运行该应用程序。 | 编写一个能运行开发服务器的 `init.sh` 脚本。 | 通过读取 `init.sh` 来启动会话。 |

总结长时运行 AI 智能体的四种常见故障模式及解决方案。

## Future work

这项研究展示了在长期运行的智能体框架中，一套可能的解决方案，使模型能够在多个上下文窗口中实现渐进式进展。但仍有未解之谜。

最值得注意的是，目前尚不确定单一通用型编程智能体能否在所有场景下表现最优，还是通过多智能体架构能实现更佳性能。从软件开发周期的子任务来看，像测试智能体、质量保证智能体或代码清理智能体这样的专业化智能体，似乎更有可能在特定环节发挥更出色的作用。

此外，该演示项目针对全栈 Web 应用开发进行了优化。未来的研究方向是将这些发现推广至其他领域——例如在科学研究或金融建模等场景下，部分或全部经验很可能适用于各类持续性智能体任务。

### Acknowledgements

本文由贾斯汀·杨撰写。特别感谢大卫·赫什、普里特维·拉贾萨克兰、杰里米·哈德菲尔德、娜亚·布斯卡、迈克尔·廷利、杰西·穆、杰克·伊顿、马里乌斯·布兰德兰、玛吉·沃、佩德拉姆·纳维德、纳丁·亚瑟和亚历克斯·诺托夫做出的贡献。

这项成果凝聚了 Anthropic 多个团队的集体智慧，正是他们让 Claude 能够安全地进行长周期自主软件工程开发，特别是代码强化学习团队和 Claude 代码团队。欢迎有志之士通过 [anthropic.com/careers](http://anthropic.com/careers) 申请加入，共同推动技术边界。

### Footnotes

1\. 我们在此语境下将它们称为独立智能体，仅因其初始用户提示不同。除此之外，系统提示、工具集及整体智能体框架均完全一致。

## 订阅开发者通讯

产品更新、使用指南、社区精选等内容，每月直达您的收件箱。