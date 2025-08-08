---
title: "Claude Code Best Practices"
source: "https://www.anthropic.com/engineering/claude-code-best-practices"
author:
  - "[[@AnthropicAI]]"
published:
created: 2025-04-24
description: "A blog post covering tips and tricks that have proven effective for using Claude Code across various codebases, languages, and environments."
tags:
  - "clippings"
---
[Anthropic 公司的工程团队](https://www.anthropic.com/engineering) ![](https://www-cdn.anthropic.com/images/4zrzovbb/website/6295100fcf8952bed666ba69536c581af87eef15-2554x2554.svg)

## 克劳德代码：智能体编码的最佳实践

我们最近发布了 Claude Code，这是一个用于智能编码的命令行工具。作为一个研究项目开发的 Claude Code，为 Anthropic 的工程师和研究人员提供了一种更原生的方式，将 Claude 集成到他们的编码工作流程中。

克劳德代码有意设计为低级别且无倾向性，提供近乎原始的模型访问，而不强制特定的工作流程。这种设计理念创造了一种灵活、可定制、可编写脚本且安全的强大工具。虽然功能强大，但这种灵活性对于刚接触智能编码工具的工程师来说存在学习曲线——至少在他们形成自己的最佳实践之前是这样。

本文概述了已被证明有效的通用模式，这些模式对 Anthropic 的内部团队以及在各种代码库、语言和环境中使用 Claude Code 的外部工程师都有效。此列表中的内容并非一成不变，也并非普遍适用；可将这些建议作为起点。我们鼓励你进行试验，找到最适合你的方法！

想了解更详细的信息？我们在 claude.ai/code 的全面文档涵盖了本文中提到的所有功能，并提供了更多示例、实现细节和高级技术。

## 1\. 自定义你的设置

Claude 代码是一个具有智能的编码助手，它会自动将上下文引入提示中。这种上下文收集会消耗时间和令牌，但你可以通过环境调整对其进行优化。

### a. 创建 CLAUDE.md 文件

`CLAUDE.md` 是一个特殊文件，Claude 在开始对话时会自动将其纳入上下文。这使其成为记录的理想场所：

- 常见的 bash 命令
- 核心文件和实用工具函数
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

- 你的仓库根目录，或者你运行 `claude` 的任何位置（最常见的用法）。将其命名为 `CLAUDE.md` 并提交到 git，以便你可以在不同会话之间共享它并与你的团队共享（推荐），或者将其命名为 `CLAUDE.local.md` 并 `.gitignore` 它
- 运行 `claude` 的目录的任何父目录。这对于单仓库非常有用，在单仓库中，你可能从 `root/foo` 运行 `claude` ，并且在 `root/CLAUDE.md` 和 `root/foo/CLAUDE.md` 中都有 `CLAUDE.md` 文件。这两者都会自动拉入上下文
- 运行 `claude` 的目录下的任何子目录。这与上述情况相反，在这种情况下，当你在子目录中处理文件时，Claude 将按需拉入 `CLAUDE.md` 文件
- 你的主文件夹 ( `~/.claude/CLAUDE.md` )，它会将其应用于你所有的 Claude 会话

当你运行 `/init` 命令时，Claude 将自动为你生成一个 `CLAUDE.md` 。

### b. 调整您的 CLAUDE.md 文件

你的 `CLAUDE.md` 文件会成为 Claude 提示的一部分，所以它们应该像任何常用提示一样进行优化。一个常见的错误是在没有对其有效性进行迭代的情况下添加大量内容。花时间进行试验，确定什么能使模型产生最佳的指令跟随效果。

你可以手动将内容添加到你的 `CLAUDE.md` 中，或者按下 `#` 键向 Claude 发出指令，它会自动将该指令合并到相关的 `CLAUDE.md` 中。许多工程师在编码时经常使用 `#` 来记录命令、文件和样式指南，然后在提交中包含 `CLAUDE.md` 更改，以便团队成员也能受益。

在 Anthropic，我们偶尔会通过提示改进器运行 `CLAUDE.md` 文件，并经常调整指令（例如使用“重要”或“你必须”来添加强调）以提高遵循度。

![Claude Code tool allowlist](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F6961243cc6409e41ba93895faded4f4bc1772366-1600x1231.png&w=3840&q=75)

Claude Code tool allowlist

### c. 策划克劳德允许使用的工具列表

默认情况下，Claude Code 会对任何可能修改系统的操作请求权限：文件写入、许多 bash 命令、MCP 工具等。我们以这种刻意保守的方式设计 Claude Code，以将安全性置于首位。你可以自定义允许列表，以允许你知道是安全的其他工具，或者允许易于撤销的潜在不安全工具（例如，文件编辑， `git commit` ）。

管理允许的工具共有四种方法：

- 在会话期间出现提示时选择“始终允许”。
- 启动 Claude Code 后，使用 `/allowed-tools` 命令从允许列表中添加或删除工具。例如，你可以添加 `Edit` 以始终允许文件编辑，添加 `Bash(git commit:*)` 以允许进行 git 提交，或者添加 `mcp__puppeteer__puppeteer_navigate` 以允许通过 Puppeteer MCP 服务器进行导航。
- 手动编辑你的 `.claude/settings.json` 或 `~/.claude.json` （我们建议将前者检入源代码管理以便与团队共享）。
- 使用 ` --allowedTools` CLI 标志来设置特定会话的权限。

### d. 如果使用 GitHub，请安装 gh 命令行界面

克劳德知道如何使用 `gh` 命令行界面与 GitHub 进行交互，以创建问题、打开拉取请求、读取评论等等。如果没有安装 `gh` ，克劳德仍然可以使用 GitHub API 或 MCP 服务器（如果你已安装）。

Claude 可以访问你的 shell 环境，在那里你可以像为自己那样为它构建一组便利脚本和函数。它还可以通过 MCP 和 REST API 利用更复杂的工具。

### a. 将 Claude 与 bash 工具一起使用

Claude 代码继承你的 bash 环境，使其能够访问你所有的工具。虽然 Claude 了解像 Unix 工具和 `gh` 这样的常用实用程序，但如果没有说明，它不会了解你的自定义 bash 工具：

1. 告诉克劳德工具名称及使用示例
2. 告诉克劳德运行 `--help` 以查看工具文档
3. 记录 `CLAUDE.md` 中常用的工具

### b. 将 Claude 与 MCP 一起使用

Claude 代码既可以作为 MCP 服务器，也可以作为客户端。作为客户端，它可以连接到任意数量的 MCP 服务器，通过三种方式访问其工具：

- 在项目配置中（在该目录中运行 Claude 代码时可用）
- 在全局配置中（所有项目均可使用）
- 在一个已签入的 `.mcp.json` 文件中（代码库中的任何工作人员都可以访问）。例如，你可以将 Puppeteer 和 Sentry 服务器添加到你的 `.mcp.json` 中，这样每个处理你的仓库的工程师都可以开箱即用这些工具。

在使用 MCP 时，使用 `--mcp-debug` 标志启动 Claude 也有助于识别配置问题。

### c. 使用自定义斜杠命令

对于重复的工作流程（如调试循环、日志分析等），将提示模板存储在 `.claude/commands` 文件夹内的 Markdown 文件中。当你输入 `/` 时，这些模板可通过斜杠命令菜单使用。你可以将这些命令提交到 git 中，以便团队其他成员使用。

自定义斜杠命令可以包含特殊关键字 `$ARGUMENTS` ，以便从命令调用中传递参数。

例如，这是一个斜杠命令，你可以用它来自动提取并修复一个 Github 问题：

将上述内容放入 `.claude/commands/fix-github-issue.md` 中，使其在 Claude 代码中作为 `/project:fix-github-issue` 命令可用。例如，你可以使用 `/project:fix-github-issue 1234` 让 Claude 修复问题#1234。同样，你可以将自己的个人命令添加到 `~/.claude/commands` 文件夹中，以便在所有会话中都能使用这些命令。

## 3\. 尝试常见工作流程

Claude 代码并不强制特定的工作流程，让你可以根据自己的意愿灵活使用它。在这种灵活性所提供的空间内，我们的用户社区中出现了几种有效使用 Claude 代码的成功模式：

### a. 探索、规划、编码、提交

这种通用的工作流程适用于许多问题：

1. 要求 Claude 读取相关文件、图像或 URL，提供通用提示（“读取处理日志记录的文件”）或特定文件名（“读取 logging.py”），但明确告诉它目前不要编写任何代码。
	1. 这是工作流程中的一部分，在这部分你应该考虑大力使用子代理，尤其是处理复杂问题时。告诉 Claude 使用子代理来核实细节或调查它可能存在的特定问题，特别是在对话或任务的早期阶段，往往能在不损失太多效率的情况下保持上下文的可用性。
2. 要求 Claude 制定一个解决特定问题的计划。我们建议使用“思考”这个词来触发扩展思考模式，这会给 Claude 额外的计算时间，以便更全面地评估各种选择。这些特定短语直接对应系统中不断增加的思考预算级别：“思考” < “努力思考” < “更努力思考” < “极致思考”。每个级别都会为 Claude 分配逐渐增加的思考预算以供使用。
	1. 如果此步骤的结果看起来合理，你可以让 Claude 创建一个包含其计划的文档或 GitHub 问题，以便在实施（步骤 3）不符合你的要求时，你可以重置到这一点。
3. 要求 Claude 将其解决方案实现为代码。这也是一个很好的地方，可以要求它在实现解决方案的各个部分时明确验证其解决方案的合理性。
4. 要求 Claude 提交结果并创建拉取请求。如果相关，这也是让 Claude 更新任何 README 或变更日志，解释其刚刚所做之事的好时机。

步骤#1 至#2 至关重要——没有它们，Claude 往往会直接跳入编码解决方案的阶段。虽然有时这正是你想要的，但要求 Claude 先进行研究和规划，对于那些需要预先进行更深入思考的问题，能显著提高性能。

### b. 编写测试，提交；编写代码，迭代，提交

这是一种深受 Anthropic 喜爱的工作流程，适用于通过单元测试、集成测试或端到端测试易于验证的更改。通过智能编码，测试驱动开发（TDD）变得更加强大：

1. 要求 Claude 根据预期的输入/输出对编写测试。明确说明你正在进行测试驱动开发，以便它避免创建模拟实现，即使是针对代码库中尚不存在的功能。
2. 告诉克劳德运行测试并确认测试失败。明确告知它在现阶段不要编写任何实现代码通常会有所帮助。
3. 当你对测试满意时，请让 Claude 提交测试。
4. 要求 Claude 编写通过测试的代码，并指示它不要修改测试。告诉 Claude 持续进行，直到所有测试通过。Claude 编写代码、运行测试、调整代码并再次运行测试通常需要进行几次迭代。
	1. 在这个阶段，可以要求它与独立子代理进行核实，以确保实现过程没有过度拟合测试，这会有所帮助
5. 一旦你对更改感到满意，要求 Claude 提交代码。

当 Claude 有一个明确的目标可供迭代时，它的表现最佳——比如视觉模拟、测试用例或其他类型的输出。通过提供像测试这样的预期输出，Claude 可以做出更改、评估结果，并逐步改进，直到成功。

### c. 编写代码，截取结果屏幕截图，进行迭代

与测试工作流程类似，你可以为 Claude 提供视觉目标：

1. 给 Claude 一种截取浏览器屏幕截图的方法（例如，使用 Puppeteer MCP 服务器、iOS 模拟器 MCP 服务器，或者手动将屏幕截图复制/粘贴到 Claude 中）。
2. 通过复制/粘贴或拖放图像，或者向 Claude 提供图像文件路径，为 Claude 提供一个视觉模拟。
3. 要求 Claude 用代码实现该设计，对结果进行截图，并反复迭代直到结果与模型匹配。
4. 当你满意时，要求 Claude 提交。

与人类一样，Claude 的输出往往会随着迭代而显著改进。虽然第一个版本可能不错，但经过 2 到 3 次迭代后，通常会看起来好得多。为 Claude 提供查看其输出的工具以获得最佳结果。

![Safe yolo mode](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F6ea59a36fe82c2b300bceaf3b880a4b4852c552d-1600x1143.png&w=3840&q=75)

Safe yolo mode

### d. 安全 YOLO 模式

与其监督 Claude，你可以使用 `claude --dangerously-skip-permissions` 绕过所有权限检查，让 Claude 不间断地工作直到完成。这对于修复代码检查错误或生成样板代码等工作流程很有效。

让 Claude 运行任意命令存在风险，可能会导致数据丢失、系统损坏，甚至数据泄露（例如，通过提示注入攻击）。为了将这些风险降至最低，请在没有网络访问权限的容器中使用 `--dangerously-skip-permissions` 。你可以按照此参考实现使用 Docker 开发容器。

### e. 代码库问答

在开始使用新的代码库时，使用 Claude Code 进行学习和探索。在结对编程时，你可以向 Claude 提出与你向项目中的其他工程师提出的相同类型的问题。Claude 可以智能地搜索代码库以回答诸如以下的一般问题：

- 日志记录是如何工作的？
- 我如何创建一个新的 API 端点？
- `foo.rs` 的第 134 行上的 `async move { ... }` 有什么作用？
- `CustomerOnboardingFlowImpl` 处理哪些边界情况？
- 为什么我们在第 333 行调用的是 `foo()` 而不是 `bar()` ？
- Java 中 `baz.py` 的第 334 行等效的内容是什么？

在 Anthropic，以这种方式使用 Claude 代码已成为我们的核心入职流程，显著缩短了上手时间并减轻了其他工程师的负担。无需特殊提示！只需提出问题，Claude 就会探索代码以找到答案。

![Use Claude to interact with git](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fa08ea13c2359aac0eceacebf2e15f81e8e8ec8d2-1600x1278.png&w=3840&q=75)

Use Claude to interact with git

### f. 使用 Claude 与 git 进行交互

Claude 可以有效地处理许多 git 操作。许多 Anthropic 工程师在 90%以上的 git 交互中使用 Claude：

- 搜索 git 历史记录以回答诸如“哪些更改被纳入了 v1.2.3？”、“谁拥有这个特定功能？”或“为什么这个 API 是这样设计的？”之类的问题。明确提示 Claude 查看 git 历史记录以回答此类查询会有所帮助。
- 编写提交消息。Claude 会自动查看你的更改和最近的历史记录，以撰写一条考虑到所有相关上下文的消息
- 处理复杂的 Git 操作，如还原文件、解决变基冲突以及比较和移植补丁

### g. 使用 Claude 与 GitHub 进行交互

Claude 代码可以管理许多 GitHub 交互：

- 创建拉取请求：Claude 理解简写“pr”，并将根据差异和上下文生成适当的提交消息。
- 为简单的代码审查评论实现一次性解决方案：只需告诉它修复你拉取请求中的评论（可选地，给它更具体的指令），完成后推送到拉取请求分支。
- 修复失败的构建或代码检查警告
- 通过让 Claude 遍历 GitHub 上的未解决问题来对其进行分类和分流

这消除了在自动化日常任务时记住 `gh` 命令行语法的需要。

### h. 使用 Claude 处理 Jupyter 笔记本

Anthropic 的研究人员和数据科学家使用 Claude 代码来读取和写入 Jupyter 笔记本。Claude 可以解释输出，包括图像，提供一种快速探索数据和与数据交互的方式。没有必需的提示或工作流程，但我们推荐的一种工作流程是在 VS Code 中并排打开 Claude 代码和一个 `.ipynb` 文件。

在你将 Jupyter 笔记本展示给同事之前，你还可以要求 Claude 对其进行清理或进行美观方面的改进。具体告诉它使笔记本或其数据可视化“美观”往往有助于提醒它是在为人类观看体验进行优化。

## 4\. 优化您的工作流程

以下建议适用于所有工作流程：

### a. 你的指示要具体。

克劳德代码（Claude Code）的成功率会随着更具体的指令而显著提高，尤其是在首次尝试时。提前给出明确的指示可以减少后期进行路线修正的需求。

例如：

| Poor | Good |
| --- | --- |
| 为 foo.py 添加测试 | 为 foo.py 编写一个新的测试用例，覆盖用户登出的边界情况。避免使用模拟。 |
| 为什么 ExecutionFactory 有如此奇怪的 API？ | 查看 ExecutionFactory 的 git 历史记录并总结其 API 是如何形成的 |
| 添加日历小部件 | 查看主页上现有小部件的实现方式，以了解其模式，特别是代码和接口是如何分离的。HotDogWidget.php 是一个很好的起始示例。然后，按照该模式实现一个新的日历小部件，该小部件允许用户选择月份并向前/向后翻页以选择年份。除了代码库其余部分已经使用的库之外，从零开始构建。 |

克劳德可以推断意图，但它无法读取思想。明确性会带来与预期更好的契合度。

![Give Claude images](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F75e1b57a0b696e7aafeca1ed5fa6ba7c601a5953-1360x1126.png&w=3840&q=75)

Give Claude images

### b. 给 Claude 图像

Claude 通过几种方法在处理图像和图表方面表现出色：

- 粘贴屏幕截图（专业提示：在 macOS 中按 cmd+ctrl+shift+4 将屏幕截图到剪贴板，然后按 ctrl+v 粘贴。请注意，这不是你通常在 Mac 上粘贴时使用的 cmd+v，并且不能远程使用。）
- 直接将图像拖放到提示输入框中
- 提供图像的文件路径

在将设计模拟作为用户界面开发的参考点以及将可视化图表用于分析和调试时，这一点尤其有用。如果你没有在上下文中添加视觉元素，向 Claude 明确说明结果在视觉上具有吸引力有多重要仍然会有所帮助。

![Mention files you want Claude to look at or work on](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F7372868757dd17b6f2d3fef98d499d7991d89800-1450x1164.png&w=3840&q=75)

Mention files you want Claude to look at or work on

### c. 提及你希望 Claude 查看或处理的文件

使用制表符补全功能在存储库中的任何位置快速引用文件或文件夹，帮助 Claude 查找或更新正确的资源。

![Give Claude URLs](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fe071de707f209bbaa7f16b593cc7ed0739875dae-1306x1088.png&w=3840&q=75)

Give Claude URLs

### d. 给克劳德网址

在你的提示旁边粘贴特定的 URL，让 Claude 获取并读取。为避免对相同域名（例如 docs.foo.com）出现权限提示，请使用 `/allowed-tools` 将域名添加到你的允许列表中。

### e. 尽早且频繁地纠正航向

虽然自动接受模式（按 Shift+Tab 切换）可让 Claude 自主工作，但作为积极的协作者并指导 Claude 的工作方式，通常会获得更好的结果。你可以在开始时向 Claude 详细解释任务，从而获得最佳结果，但你也可以在任何时候纠正 Claude 的工作方向。

这四个工具有助于进行路线修正：

- 要求 Claude 在编码前制定一个计划。明确告诉它在你确认其计划没问题之前不要编码。
- 在任何阶段（思考、调用工具、编辑文件）按 Esc 键中断 Claude，保留上下文以便你可以重定向或扩展指令。
- 双击 Esc 键可跳转到历史记录，编辑上一个提示符，并探索不同的方向。你可以编辑提示符并重复操作，直到获得你想要的结果。
- 要求 Claude 撤销更改，通常结合选项 2 采用不同的方法。

虽然克劳德代码偶尔能在首次尝试时完美解决问题，但使用这些校正工具通常能更快地产生更好的解决方案。

### f. 使用 /clear 来保持上下文聚焦

在长时间的会话中，Claude 的上下文窗口可能会被不相关的对话、文件内容和命令填满。这可能会降低性能，有时还会分散 Claude 的注意力。在任务之间频繁使用 `/clear` 命令来重置上下文窗口。

### g. 对复杂工作流程使用检查表和便签本

对于具有多个步骤或需要详尽解决方案的大型任务（如代码迁移、修复大量代码检查错误或运行复杂的构建脚本），通过让 Claude 使用 Markdown 文件（甚至是 GitHub 问题！）作为检查清单和工作便签本来提高性能：

例如，要修复大量的代码检查问题，你可以执行以下操作：

1. 告诉克劳德运行代码检查命令，并将所有产生的错误（包括文件名和行号）写入一个 Markdown 清单
2. 指示 Claude 逐一处理每个问题，在勾选并进入下一个问题之前进行修复和验证

### h. 将数据输入 Claude

有几种向 Claude 提供数据的方法：

- 直接复制粘贴到你的提示中（最常见的方法）
- 导入 Claude 代码（例如， `cat foo.txt | claude` ），对日志、CSV 文件和大数据特别有用
- 告诉克劳德通过 bash 命令、MCP 工具或自定义斜杠命令提取数据
- 要求 Claude 读取文件或获取 URL（也适用于图像）

大多数会话都涉及这些方法的组合。例如，你可以输入一个日志文件，然后告诉 Claude 使用工具引入额外的上下文来调试日志。

## 5\. 使用无头模式自动化您的基础设施

Claude 代码包括用于非交互式环境（如持续集成、预提交钩子、构建脚本和自动化）的无头模式。使用带有提示符的 `-p` 标志来启用无头模式，使用 `--output-format stream-json` 来流式传输 JSON 输出。

请注意，无头模式不会在会话之间持续存在。你必须在每个会话中触发它。

### a. 使用 Claude 进行问题分类

无头模式可以驱动由 GitHub 事件触发的自动化操作，例如在你的仓库中创建新问题时。例如，公共的 Claude 代码仓库使用 Claude 来检查新进来的问题并分配适当的标签。

### b. 将 Claude 用作代码检查工具

Claude 代码可以提供超越传统代码检查工具所能检测到的主观代码审查，识别诸如拼写错误、过时注释、误导性的函数或变量名等问题，等等。

## 6\. 使用多克劳德工作流程提升级别

除了独立使用之外，一些最强大的应用涉及并行运行多个 Claude 实例：

### a. 让一个 Claude 编写代码；用另一个 Claude 进行验证

一种简单但有效的方法是让一个 Claude 编写代码，同时让另一个 Claude 进行审查或测试。类似于与多个工程师合作，有时拥有单独的上下文是有益的：

1. 使用 Claude 编写代码
2. 运行 `/clear` 或在另一个终端中启动第二个 Claude
3. 让第二个 Claude 审核第一个 Claude 的工作
4. 启动另一个 Claude（或再次 `/clear` ）以同时读取代码和审核反馈
5. 让 Claude 根据反馈编辑代码

你可以对测试做类似的事情：让一个 Claude 编写测试，然后让另一个 Claude 编写代码以使测试通过。你甚至可以通过为 Claude 实例提供单独的工作暂存区，并告诉它们向哪个暂存区写入以及从哪个暂存区读取，来让它们相互通信。

这种分离通常比让单个 Claude 处理所有事情能产生更好的结果。

### b. 对你的仓库进行多次检出

与其等待 Claude 完成每一步，Anthropic 的许多工程师会做的是：

1. 在单独的文件夹中创建 3 到 4 个 git 检出
2. 在单独的终端标签页中打开每个文件夹
3. 在每个文件夹中使用不同任务启动 Claude
4. 循环检查进度并批准/拒绝权限请求

### c. 使用 git 工作树

这种方法在处理多个独立任务时表现出色，为多次检出提供了一种更轻量级的替代方案。Git 工作树允许你从同一个仓库检出多个分支到不同的目录中。每个工作树都有自己独立的工作目录和文件，同时共享相同的 Git 历史记录和引用日志。

使用 git 工作树使您能够在项目的不同部分同时运行多个 Claude 会话，每个会话专注于自己独立的任务。例如，您可能让一个 Claude 重构您的身份验证系统，而另一个 Claude 构建一个完全不相关的数据可视化组件。由于任务不重叠，每个 Claude 都可以全速工作，而无需等待其他 Claude 的更改或处理合并冲突：

1. 创建工作树： `git worktree add ../project-feature-a feature-a`
2. 在每个工作区中启动 Claude： `cd ../project-feature-a && claude`
3. 根据需要创建其他工作树（在新的终端标签页中重复步骤 1-2）

一些提示：

- 使用一致的命名约定
- 为每个工作树维护一个终端标签页
- 如果你正在 Mac 上使用 iTerm2，设置 Claude 需要关注时的通知
- 为不同的工作树使用单独的 IDE 窗口
- 完成后清理： `git worktree remove ../project-feature-a`

### d. 使用带有自定义测试框架的无头模式

`claude -p` （无头模式）以编程方式将 Claude 代码集成到更大的工作流程中，同时利用其内置工具和系统提示。使用无头模式有两种主要模式：

1\. 扇出可处理大规模迁移或分析（例如，分析数百条日志中的情感倾向或分析数千个 CSV 文件）：

1. 让 Claude 编写一个脚本来生成任务列表。例如，生成一个需要从框架 A 迁移到框架 B 的 2k 文件列表。
2. 遍历任务，以编程方式为每个任务调用 Claude，并为其提供一个任务和一组它可以使用的工具。例如： `claude -p “migrate foo.py from React to Vue. When you are done, you MUST return the string OK if you succeeded, or FAIL if the task failed.” --allowedTools Edit Bash(git commit:*)`
3. 多次运行脚本并优化你的提示以获得预期的结果。

2\. 流水线技术将 Claude 集成到现有的数据/处理流水线中：

1. 调用 `claude -p “<your prompt>” --json | your_command` ，其中 `your_command` 是处理管道的下一步
2. 就是这样！JSON 输出（可选）有助于提供结构，以便更轻松地进行自动化处理。

对于这两种用例，使用 `--verbose` 标志来调试 Claude 调用可能会有所帮助。我们通常建议在生产环境中关闭详细模式以获得更简洁的输出。

使用 Claude 代码工作，你有哪些提示和最佳实践？标记@AnthropicAI，这样我们就能看到你正在构建的内容！

## 致谢

作者：鲍里斯·切尔尼。这项工作借鉴了更广泛的 Claude Code 用户社区的最佳实践，他们富有创造性的方法和工作流程不断激励着我们。特别感谢黛西·霍尔曼、阿什温·巴特、凯特·吴、西德·比达萨里亚、卡尔·鲁布、诺迪尔·图拉库洛夫、巴里·张、德鲁·霍顿以及许多其他 Anthropic 工程师，他们对 Claude Code 的宝贵见解和实践经验有助于形成这些建议。