---
title: "Claude Code Best Practices"
source: "https://www.anthropic.com/engineering/claude-code-best-practices"
author:
  - "[[@AnthropicAI]]"
published:
created: 2025-07-11
description: "A blog post covering tips and tricks that have proven effective for using Claude Code across various codebases, languages, and environments."
tags:
  - "clippings"
---
[Anthropic 公司的工程团队](https://www.anthropic.com/engineering) ![](https://www-cdn.anthropic.com/images/4zrzovbb/website/6295100fcf8952bed666ba69536c581af87eef15-2554x2554.svg)

## 克劳德代码：智能体编码的最佳实践

我们最近发布了 Claude Code，这是一个用于智能编码的命令行工具。作为一个研究项目开发的 Claude Code，为 Anthropic 的工程师和研究人员提供了一种更原生的方式，将 Claude 集成到他们的编码工作流程中。

Claude 代码有意设计得较为底层且不带有倾向性，提供近乎原始的模型访问方式，而不强制使用特定的工作流程。这种设计理念打造出了一个灵活、可定制、可编写脚本且安全的强大工具。虽然功能强大，但这种灵活性对于刚接触智能体编码工具的工程师来说存在一定的学习曲线——至少在他们形成自己的最佳实践之前是这样。

本文概述了一些已被证明行之有效的通用模式，这些模式对 Anthropic 的内部团队以及在各种代码库、语言和环境中使用 Claude Code 的外部工程师都很有效。此列表中的内容并非一成不变，也并非普遍适用；可将这些建议作为起点。我们鼓励你进行试验，找到最适合你的方法！

*想要了解更详细的信息？我们在 [claude.ai/code](https://claude.ai/redirect/website.v1.6c8e1730-aab5-47bb-81a8-958e9eb97c3c/code) 上的全面文档* *涵盖了本文提到的所有功能，并提供了更多示例、实现细节和高级技术。*

## 1\. 自定义你的设置

Claude 代码是一个能自动将上下文引入提示的智能编码助手。这种上下文收集会消耗时间和令牌，但你可以通过环境调整对其进行优化。

### a. 创建 CLAUDE.md 文件

名为 `CLAUDE.md` 的文件是一个特殊文件，Claude 在开始对话时会自动将其纳入上下文。这使其成为记录以下内容的理想场所：

- 常见的 bash 命令
- 核心文件和实用函数
- 代码风格指南
- 测试说明
- 仓库规范（例如，分支命名、合并与变基等）
- 开发者环境设置（例如，使用 pyenv，哪些编译器可用）
- 该项目特有的任何意外行为或警告
- 你希望 Claude 记住的其他信息

`CLAUDE.md` 文件没有要求的格式。我们建议保持它们简洁且易于阅读。例如：

```
# Bash commands
- npm run build: Build the project
- npm run typecheck: Run the typechecker

# Code style
- Use ES modules (import/export) syntax, not CommonJS (require)
- Destructure imports when possible (eg. import { foo } from 'bar')

# Workflow
- Be sure to typecheck when you’re done making a series of code changes
- Prefer running single tests, and not the whole test suite, for performance
```

你可以将 `CLAUDE.md` 文件放置在多个位置：

- **你的仓库根目录** ，或者你运行 `claude` 的任何位置（最常见的用法）。将其命名为 `CLAUDE.md` 并提交到 git，以便你可以在不同会话之间共享它并与你的团队共享（推荐），或者将其命名为 `CLAUDE.local.md` 并在 `.gitignore` 中忽略它
- 运行 `claude` 的目录的 **任何父目录** 。这在多仓库项目中最为有用，比如你可能从 `root/foo` 运行 `claude` ，并且在 `root/CLAUDE.md` 和 `root/foo/CLAUDE.md` 中都有 `CLAUDE.md` 文件。这两个文件都会自动被纳入上下文
- 运行 `claude` 的目录下的 **任何子目录** 。这与上述情况相反，在这种情况下，当你在子目录中处理文件时，Claude 将按需引入 `CLAUDE.md` 文件。
- **你的主文件夹** (`~/.claude/CLAUDE.md`)，它会将其应用于你所有的 *claude* 会话

当你运行 `/init` 命令时，Claude 会自动为你生成一个 `CLAUDE.md` 。

### b. 调整您的 CLAUDE.md 文件

你的 `CLAUDE.md` 文件会成为 Claude 提示的一部分，所以应该像对待任何常用提示一样对它们进行优化。一个常见的错误是在没有反复验证其有效性的情况下添加大量内容。花些时间进行试验，确定什么能让模型产生最佳的指令跟随效果。

你可以手动向你的 `CLAUDE.md` 添加内容，或者按下 `#` 键向 Claude 发出指令，它会自动将其纳入相关的 `CLAUDE.md` 中。许多工程师在编码时经常使用 `#` 来记录命令、文件和样式指南，然后在提交中包含 `CLAUDE.md` 的更改，这样团队成员也能受益。

在 Anthropic，我们偶尔会通过 [提示改进器](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-improver) 运行 `CLAUDE.md` 文件，并经常调整指令（例如，使用“重要”或“你必须”来添加强调）以提高遵循度。

![Claude Code tool allowlist](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F6961243cc6409e41ba93895faded4f4bc1772366-1600x1231.png&w=3840&q=75)

Claude Code tool allowlist

### c. 精心管理 Claude 的允许使用工具列表

默认情况下，Claude Code 会对任何可能修改系统的操作请求权限：文件写入、许多 bash 命令、MCP 工具等。我们以这种刻意保守的方式设计 Claude Code，以优先保障安全。你可以自定义允许列表，以允许你知道是安全的其他工具，或者允许易于撤销的潜在不安全工具（例如，文件编辑， `git commit` ）。

管理允许使用的工具共有四种方法：

- 在会话过程中出现提示时，选择“始终允许”。
- 在启动 Claude Code 后，使用 **`/permissions` 命令** 来添加或从允许列表中移除工具。例如，你可以添加 `Edit` 以始终允许文件编辑，添加 `Bash(git commit:*)` 以允许进行 git 提交，或者添加 `mcp__puppeteer__puppeteer_navigate` 以允许通过 Puppeteer MCP 服务器进行导航。
- 手动编辑你的 `.claude/settings.json` 或 `~/.claude.json` （我们建议将前者纳入版本控制以便与团队共享） *。* **手动编辑**
- 使用 `--allowedTools` CLI 标志来设置特定会话的权限。

### d. 如果使用 GitHub，请安装 gh 命令行界面

Claude 知道如何使用 `gh` 命令行界面与 GitHub 进行交互，以创建问题、打开拉取请求、读取评论等等。如果没有安装 `gh` ，Claude 仍然可以使用 GitHub API 或 MCP 服务器（如果你已安装）。

Claude 可以访问你的 shell 环境，在那里你可以像为自己构建一样，为它构建一系列便捷的脚本和函数。它还可以通过 MCP 和 REST API 利用更复杂的工具。

### a. 将 Claude 与 bash 工具一起使用

Claude 代码继承您的 bash 环境，使其能够访问您的所有工具。虽然 Claude 了解常见的实用工具，如 Unix 工具和 `gh` ，但如果没有说明，它将不了解您的自定义 bash 工具：

1. 告诉 Claude 工具名称及使用示例
2. 告诉 Claude 运行 `--help` 以查看工具文档
3. 《CLAUDE.md》文档中常用的工具

### b. 将 Claude 与 MCP 一起使用

Claude 代码兼具 MCP 服务器和客户端的功能。作为客户端，它可以通过三种方式连接到任意数量的 MCP 服务器以访问其工具：

- **在项目配置中** （在该目录中运行 Claude 代码时可用）
- **在全局配置中** （在所有项目中可用）
- **在签入的 `.mcp.json` 文件中** （代码库中的任何工作人员均可访问）。例如，你可以将 Puppeteer 和 Sentry 服务器添加到 `.mcp.json` 中，这样处理你的代码仓库的每个工程师都可以开箱即用这些工具。

在使用 MCP 时，使用 `--mcp-debug` 标志启动 Claude 也有助于识别配置问题。

### c. 使用自定义斜杠命令

对于重复的工作流程（如调试循环、日志分析等），将提示模板存储在 `.claude/commands` 文件夹内的 Markdown 文件中。当你输入 `/` 时，这些模板会通过斜杠命令菜单显示出来。你可以将这些命令提交到 git 中，以便团队其他成员使用。

自定义斜杠命令可以包含特殊关键字 `$ARGUMENTS` ，以便从命令调用中传递参数。

例如，这是一个你可以用来自动拉取并修复 Github 问题的斜杠命令：

将上述内容放入 `.claude/commands/fix-github-issue.md` 后，它在 Claude Code 中作为 `/project:fix-github-issue` 命令可用。例如，然后你可以使用 `/project:fix-github-issue 1234` 让 Claude 修复问题 #1234。同样，你可以将自己的个人命令添加到 `~/.claude/commands` 文件夹中，以便在你所有的会话中都能使用这些命令。

## 3\. 尝试常见工作流程

Claude 代码并不强制规定特定的工作流程，让你可以根据自己的意愿灵活使用。在这种灵活性所提供的空间内，我们的用户群体中出现了几种有效使用 Claude 代码的成功模式：

### a. 探索、规划、编码、提交

这种通用的工作流程适用于许多问题：

1. **要求 Claude 读取相关文件、图像或 URL** ，提供一般提示（“读取处理日志记录的文件”）或特定文件名（“读取 logging.py”），但明确告诉它目前不要编写任何代码。
	1. 这是工作流程中的一部分，在这部分你应该考虑大力使用子代理，尤其是处理复杂问题时。告诉 Claude 使用子代理来核实细节或调查它可能存在的特定问题，特别是在对话或任务的早期阶段，往往能在不损失太多效率的情况下保持上下文的可用性。
2. **要求 Claude 制定一个解决特定问题的计划** 。我们建议使用“思考”一词来触发扩展思考模式，这会给 Claude 额外的计算时间，以便更全面地评估各种方案。这些特定短语直接对应系统中不断增加的思考预算级别：“思考” ＜ “努力思考” ＜ “更努力思考” ＜ “超级思考”。每个级别为 Claude 分配的思考预算逐渐增加。
	1. 如果此步骤的结果看起来合理，你可以让 Claude 根据其计划创建一个文档或一个 GitHub 问题，这样如果实施过程（步骤 3）不符合你的预期，你可以重置到这一步。
3. **要求 Claude 以代码形式实现其解决方案** 。在它实现解决方案的各个部分时，也是要求它明确验证其解决方案合理性的好时机。
4. **要求 Claude 提交结果并创建拉取请求** 。如果相关，这也是让 Claude 更新任何 README 文件或变更日志，解释其刚刚所做之事的好时机。

步骤#1 至#2 至关重要——没有它们，Claude 往往会直接着手编写解决方案的代码。虽然有时这正是你想要的，但让 Claude 先进行研究和规划，对于那些需要预先深入思考的问题，能显著提高其表现。

### b. 编写测试，提交；编码，迭代，提交

对于那些可以通过单元测试、集成测试或端到端测试轻松验证的更改，这是一种深受 Anthropic 喜爱的工作流程。通过智能编码，测试驱动开发（TDD）变得更加强大：

1. **要求 Claude 根据预期的输入/输出对编写测试** 。明确说明你正在进行测试驱动开发，以便它避免创建模拟实现，即使是针对代码库中尚不存在的功能。
2. **告诉 Claude 运行测试并确认测试失败** 。明确告知它在现阶段不要编写任何实现代码通常会有所帮助。
3. 当你对测试满意时， **要求 Claude 提交测试** 。
4. **要求 Claude 编写通过测试的代码** ，指示它不要修改测试。告诉 Claude 持续进行，直到所有测试都通过。Claude 通常需要经过几次迭代来编写代码、运行测试、调整代码并再次运行测试。
	1. 在这个阶段，要求它与独立的子代理进行验证，以确保实现不会过度拟合测试，这会有所帮助
5. 一旦你对更改感到满意，请要求 Claude 提交代码。

当 Claude 有一个明确的目标可供迭代时，比如视觉模拟、测试用例或其他类型的输出，它的表现最佳。通过提供像测试这样的预期输出，Claude 可以做出更改、评估结果，并逐步改进，直到成功。

### c. 编写代码，截取结果截图，反复迭代

与测试工作流程类似，你可以为 Claude 提供视觉目标：

1. **为 Claude 提供一种截取浏览器屏幕截图的方法** （例如，使用 [Puppeteer MCP 服务器](https://github.com/modelcontextprotocol/servers/tree/c19925b8f0f2815ad72b08d2368f0007c86eb8e6/src/puppeteer) 、 [iOS 模拟器 MCP 服务器](https://github.com/joshuayoes/ios-simulator-mcp) ，或者手动将屏幕截图复制/粘贴到 Claude 中）。
2. 通过复制/粘贴或拖放图像，或者向 Claude 提供图像文件路径，为 Claude 提供一个视觉模拟。
3. <强 id=0>要求 Claude 用代码实现该设计，对结果进行截图，并反复迭代，直到其结果与模拟图匹配。
4. 当你满意时，点击 **让 Claude 提交** 。

和人类一样，Claude 的输出往往会随着迭代而显著改进。虽然第一个版本可能不错，但经过两到三次迭代后通常会看起来好得多。为了获得最佳效果，给 Claude 提供查看其输出的工具。

![Safe yolo mode](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F6ea59a36fe82c2b300bceaf3b880a4b4852c552d-1600x1143.png&w=3840&q=75)

Safe yolo mode

### d. 安全极速模式

你可以使用 `claude --dangerously-skip-permissions` 绕过所有权限检查，让 Claude 不受干扰地工作直至完成，而不是监督 Claude。这在修复代码检查错误或生成样板代码等工作流程中效果很好。

让 Claude 运行任意命令存在风险，可能会导致数据丢失、系统损坏，甚至数据泄露（例如，通过提示注入攻击）。为了将这些风险降至最低，请在没有网络访问权限的容器中使用 `--dangerously-skip-permissions` 。你可以按照此 [参考实现](https://github.com/anthropics/claude-code/tree/main/.devcontainer) 使用 Docker 开发容器。

### e. 代码库问答

在开始使用新的代码库时，使用 Claude Code 进行学习和探索。你可以向 Claude 提出在结对编程时会向项目中的其他工程师提出的类似问题。Claude 可以主动搜索代码库来回答诸如以下的一般问题：

- 日志记录是如何工作的？
- 我如何创建一个新的 API 端点？
- 在\`foo.rs\`文件的第 134 行，\` `async move {... }` \` 做了什么？
- `CustomerOnboardingFlowImpl` 处理哪些边界情况？
- 为什么我们在第 333 行调用的是 `foo()` 而不是 `bar()` ？
- 在 Java 中， `baz.py` 的第 334 行等效代码是什么？

在 Anthropic，以这种方式使用 Claude 代码已成为我们核心的入职流程，显著缩短了上手时间，并减轻了其他工程师的负担。无需特殊提示！只需提出问题，Claude 就会探索代码以找到答案。

![Use Claude to interact with git](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fa08ea13c2359aac0eceacebf2e15f81e8e8ec8d2-1600x1278.png&w=3840&q=75)

Use Claude to interact with git

### f. 使用 Claude 与 git 进行交互

Claude 可以有效地处理许多 git 操作。许多 Anthropic 工程师在 90%以上的 git 交互中使用 Claude：

- **搜索 *git* 历史记录** 以回答诸如 “哪些更改被纳入了 v1.2.3？”、“谁负责这个特定功能？” 或 “为什么这个 API 要这样设计？” 之类的问题。明确提示 Claude 查阅 git 历史记录以回答此类查询会有所帮助。
- **编写提交消息** 。Claude 会自动查看你的更改和最近的历史记录，以撰写一条考虑到所有相关上下文的消息。
- **处理复杂的 git 操作** ，如还原文件、解决变基冲突以及比较和移植补丁

### g. 使用 Claude 与 GitHub 进行交互

Claude 代码可以管理许多 GitHub 交互：

- **创建拉取请求** ：Claude 理解简写“pr”，并会根据差异和周围上下文生成合适的提交消息。
- 针对简单的代码审查评论实施一次性解决方案：只需告诉它修复你拉取请求中的评论（可选地，给出更具体的指示），完成后推回到拉取请求分支。
- 修复失败的构建或代码检查警告
- 通过要求 Claude 遍历 GitHub 上的未解决问题来对未解决问题进行分类和优先级排序

这消除了在自动化日常任务时记住 `gh` 命令行语法的需要。

### h. 使用 Claude 处理 Jupyter 笔记本

Anthropic 的研究人员和数据科学家使用 Claude Code 来读取和编写 Jupyter 笔记本。Claude 可以解释输出内容，包括图像，提供一种快速探索和与数据交互的方式。没有必需的提示或工作流程，但我们推荐的一种工作流程是在 VS Code 中并排打开 Claude Code 和一个 `.ipynb` 文件。

在你将 Jupyter 笔记本展示给同事之前，你还可以要求 Claude 对其进行清理或进行美观方面的改进。明确告诉它要让笔记本或其数据可视化“美观宜人”，这往往有助于提醒它是在为人类的观看体验进行优化。

## 4\. 优化你的工作流程

以下建议适用于所有工作流程：

### a. 让你的指令具体明确。

克劳德代码（Claude Code）的成功率会随着更具体的指令而显著提高，尤其是在首次尝试时。提前给出清晰的指示可以减少后续进行修正的需求。

例如：

| Poor | Good |
| --- | --- |
| 为 foo.py 添加测试 | 为 foo.py 编写一个新的测试用例，覆盖用户已注销的边界情况。避免使用模拟。 |
| 为什么 ExecutionFactory 有这么奇怪的 API？ | 查看 ExecutionFactory 的 git 历史记录，并总结其 API 是如何形成的 |
| 添加一个日历小部件 | 查看主页上现有小部件的实现方式，以了解其模式，特别是代码和界面是如何分离的。HotDogWidget.php 就是一个很好的起始示例。然后，按照该模式实现一个新的日历小部件，该小部件允许用户选择月份并向前/向后翻页以选择年份。除了代码库其他部分已经使用的库之外，从零开始构建。 |

Claude 可以推断意图，但它无法读取思想。明确具体能更好地符合预期。

![Give Claude images](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F75e1b57a0b696e7aafeca1ed5fa6ba7c601a5953-1360x1126.png&w=3840&q=75)

Give Claude images

### b. 向 Claude 提供图像

Claude 通过多种方法在处理图像和图表方面表现出色：

- **粘贴屏幕截图** （专业提示：在 macOS 中按 *cmd+ctrl+shift+4* 将屏幕截图复制到剪贴板，然后按 *ctrl+v* 粘贴。请注意，这不是通常在 Mac 上用于粘贴的 cmd+v，并且远程操作时不起作用。）
- 将图像直接拖放到提示输入框中
- 为图像提供文件路径

在将设计模拟用作 UI 开发的参考点，以及将可视化图表用于分析和调试时，这一点尤其有用。如果你没有在上下文中添加视觉元素，向 Claude 明确说明结果在视觉上具有吸引力有多重要仍然会有所帮助。

![Mention files you want Claude to look at or work on](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F7372868757dd17b6f2d3fef98d499d7991d89800-1450x1164.png&w=3840&q=75)

Mention files you want Claude to look at or work on

### c. 提及你希望 Claude 查看或处理的文件

使用制表符补全功能在你的仓库中的任何位置快速引用文件或文件夹，帮助 Claude 找到或更新正确的资源。

![Give Claude URLs](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fe071de707f209bbaa7f16b593cc7ed0739875dae-1306x1088.png&w=3840&q=75)

Give Claude URLs

### d. 提供 Claude 的网址

在你的提示中粘贴特定的 URL，让 Claude 获取并读取。为避免对相同域名（例如 docs.foo.com）出现权限提示，请使用 `/permissions` 将域名添加到你的允许列表中。

### e. 尽早且频繁地进行方向修正

虽然自动接受模式（按 Shift+Tab 切换）可让 Claude 自主工作，但作为积极的协作方并指导 Claude 的工作方式，通常会获得更好的结果。一开始就向 Claude 详细解释任务，能得到最佳效果，但你也可以在任何时候纠正 Claude 的方向。

以下这四个工具有助于进行课程调整：

- 在编码之前， **要求 Claude 制定一个计划** 。在你确认它的计划看起来不错之前，明确告诉它不要编码。
- 在任何阶段（思考、调用工具、编辑文件）按 Escape 键中断克劳德，保留上下文以便你可以重新定向或扩展指令。
- **双击 Esc 键可跳转到历史记录** ，编辑之前的提示，并探索不同的方向。你可以编辑提示并重复操作，直到获得你想要的结果。
- **要求 Claude 撤销更改** ，通常与选项 2 结合使用以采取不同的方法。

虽然 Claude 代码偶尔能在首次尝试时完美解决问题，但使用这些修正工具通常能更快地产生更好的解决方案。

### f. 使用 /clear 来保持上下文的聚焦

在长时间的会话中，Claude 的上下文窗口可能会被不相关的对话、文件内容和命令填满。这可能会降低性能，有时还会分散 Claude 的注意力。在任务之间频繁使用 `/clear` 命令来重置上下文窗口。

### g. 对于复杂的工作流程，使用检查表和便签纸

对于有多个步骤或需要详尽解决方案的大型任务（如代码迁移、修复大量代码检查错误或运行复杂的构建脚本），可通过让 Claude 使用 Markdown 文件（甚至是 GitHub 问题！）作为检查清单和工作便签本来提高性能：

例如，要修复大量的代码检查问题，你可以执行以下操作：

1. **告诉 Claude 运行代码检查命令** ，并将所有产生的错误（包括文件名和行号）写入一个 Markdown 清单
2. **指示 Claude 逐一处理每个问题** ，在勾选并进入下一个问题之前进行修复和验证

### h. 将数据传入 Claude

有几种向 Claude 提供数据的方法：

- 直接复制粘贴到你的提示中（最常见的方法）
- **通过管道输入 Claude 代码** （例如， `cat foo.txt | claude` ），这对于日志、CSV 文件和大数据特别有用
- 通过 bash 命令、MCP 工具或自定义斜杠命令 **告诉 Claude 提取数据**
- **让 Claude 读取文件** 或获取 URL（对图像也有效）

大多数会话都涉及这些方法的组合。例如，你可以传入一个日志文件，然后告诉 Claude 使用工具引入额外的上下文来调试日志。

## 5\. 使用无头模式自动化您的基础设施

Claude 代码包括用于诸如持续集成（CI）、预提交钩子、构建脚本和自动化等非交互式环境的 [无头模式](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview#automate-ci-and-infra-workflows) 。使用带有提示的 `-p` 标志来启用无头模式，并使用 `--output-format stream-json` 以获取流式 JSON 输出。

请注意，无头模式不会在会话之间持久存在。你必须在每个会话中触发它。

### a. 使用 Claude 进行问题分类

无头模式可以驱动由 GitHub 事件触发的自动化操作，比如当你的仓库中创建了一个新问题时。例如，公开的 [Claude 代码仓库](https://github.com/anthropics/claude-code/blob/main/.github/actions/claude-issue-triage-action/action.yml) 使用 Claude 来检查新进来的问题并分配适当的标签。

### b. 将 Claude 用作代码检查工具

Claude Code 可以提供超越传统代码检查工具所能检测到的主观代码审查，识别诸如拼写错误、过时的注释、误导性的函数或变量名等问题。

## 6\. 通过多克劳德工作流程提升水平

除了独立使用外，一些最强大的应用涉及并行运行多个 Claude 实例：

### a. 让一个 Claude 编写代码；用另一个 Claude 进行验证

一种简单但有效的方法是让一个 Claude 编写代码，同时让另一个 Claude 进行审查或测试。类似于与多个工程师合作，有时拥有独立的上下文是有益的：

1. 使用 Claude 编写代码
2. 运行 `/clear` 或在另一个终端中启动第二个 Claude
3. 让第二个 Claude 审核第一个 Claude 的工作
4. 启动另一个 Claude（或再次执行 `/clear` ）以同时阅读代码和审核反馈
5. 让 Claude 根据反馈编辑这段代码

你可以对测试做类似的事情：让一个 Claude 编写测试，然后让另一个 Claude 编写使测试通过的代码。你甚至可以通过为 Claude 实例提供单独的工作暂存区，并告诉它们向哪个暂存区写入以及从哪个暂存区读取，来让它们相互通信。

这种分离通常会比让一个 Claude 处理所有事情产生更好的结果。

### b. 对你的代码库进行多次检出

与其等待 Claude 完成每一步，Anthropic 的许多工程师会这样做：

1. 在单独的文件夹中 **创建 3 - 4 个 git 检出**
2. 在单独的终端标签页中打开每个文件夹
3. 在每个文件夹中以不同任务启动 Claude
4. **循环遍历** 以检查进度并批准/拒绝权限请求

### c. 使用 git 工作树

这种方法在处理多个独立任务时表现出色，为多次检出提供了一种更轻量级的替代方案。Git 工作树允许你从同一个仓库检出多个分支到不同的目录中。每个工作树都有自己独立的工作目录和文件，同时共享相同的 Git 历史记录和引用日志。

使用 Git 工作树使您能够在项目的不同部分同时运行多个 Claude 会话，每个会话专注于自己独立的任务。例如，您可能会让一个 Claude 重构您的认证系统，而另一个 Claude 构建一个完全不相关的数据可视化组件。由于任务不重叠，每个 Claude 都可以全速工作，而无需等待对方的更改或处理合并冲突：

1. **创建工作树** ： `git worktree add ../project-feature-a feature-a`
2. 在每个工作区启动 Claude： `cd ../project-feature-a && claude`
3. 根据需要创建额外的工作树（在新的终端标签页中重复步骤1-2）

一些提示：

- 使用一致的命名约定
- 为每个工作树维护一个终端标签页
- 如果你在 Mac 上使用 iTerm2， [设置通知](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview#notification-setup) ，以便在 Claude 需要关注时提醒你
- 为不同的工作树使用单独的集成开发环境（IDE）窗口
- 完成后清理： `git worktree remove ../project-feature-a`

### d. 使用带有自定义框架的无头模式

`claude -p` （无头模式）以编程方式将 Claude 代码集成到更大的工作流程中，同时利用其内置工具和系统提示。使用无头模式有两种主要模式：

1\. **分散处理** 用于处理大型迁移或分析（例如，分析数百条日志中的情感倾向或分析数千个 CSV 文件）：

1. 让 Claude 编写一个脚本来生成任务列表。例如，生成一个需要从框架 A 迁移到框架 B 的 2k 个文件的列表。
2. 遍历任务，为每个任务以编程方式调用 Claude，并为其提供一个任务以及它可以使用的一组工具。例如： `claude -p “migrate foo.py from React to Vue. When you are done, you MUST return the string OK if you succeeded, or FAIL if the task failed.” --allowedTools Edit Bash(git commit:*)`
3. 多次运行该脚本并优化你的提示，以获得预期的结果。

2\. **管道化** 将 Claude 集成到现有的数据/处理管道中：

1. 调用 `claude -p “<your prompt>” --json | your_command` ，其中 `your_command` 是你的处理管道的下一步
2. 就是这样！JSON 输出（可选）有助于提供结构，便于进行自动化处理。

对于这两种用例，使用 `--verbose` 标志来调试对 Claude 的调用可能会有所帮助。我们通常建议在生产环境中关闭详细模式以获得更简洁的输出。

使用 Claude 代码有哪些技巧和最佳实践？@AnthropicAI ，这样我们就能看到你在构建什么了！

## 致谢

作者：鲍里斯·切尔尼。本作品借鉴了更广泛的 Claude 代码用户社区的最佳实践，他们富有创造性的方法和工作流程不断激励着我们。特别感谢黛西·霍尔曼、阿什温·巴特、凯特·吴、西德·比达萨里亚、卡尔·鲁布、诺迪尔·图拉库洛夫、巴里·张、德鲁·霍顿以及许多其他 Anthropic 工程师，他们对 Claude 代码的宝贵见解和实践经验有助于形成这些建议。