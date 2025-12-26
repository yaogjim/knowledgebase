---
title: "2025-12-26_Simon_Willison_Claude_的能力真的很出色_可能比_MCP_更有分量"
source: "https://simonwillison.net/2025/Oct/16/claude-skills/"
author:
  - "[[@Simon Willison]]"
published: 2025-12-26
created: 2025-12-26
description:
tags:
  - "#trying"
  - "#skills"
  - "simonwillison"
  - "@Simon Willison"
---

# ## Claude 的能力真的很出色，可能比 MCP 更有分量

## Claude 的能力真的很出色，可能比 MCP 更有分量

16th October 2025

今天上午，Anthropic 推出了 Claude 技能，这是一种为其模型赋予新能力的新模式：

> Claude can now use Skills to enhance its performance in specific tasks. Skills are folders containing instructions, scripts, and resources that Claude can load when needed.
> 
> Claude will only use a skill when it is relevant to the current task. When used, skills help Claude excel at specialized tasks such as using Excel or following your organization’s brand guidelines.

他们的工程博客上有更详细的说明。此外，还有一个新的 anthropics/skills GitHub 仓库。

上周五，我在逆向工程并写文章介绍了这个功能后，无意中抢先发布了他们的公告！

技能在概念上极其简单：它是一个 Markdown 文件，用于告诉模型如何完成任务，并且可以可选地附带额外文档和预先编写的脚本，模型可通过运行这些脚本来协助完成技能中描述的任务。

Claude 的新文档创建能力（于 9 月随新的代码解释器功能一同推出）结果发现完全是通过技能实现的。这些能力现在可在 Anthropic 的代码仓库中找到，涵盖 `.pdf` 、 `.docx` 、 `.xlsx` 和 `.pptx` 文件。

有一个额外的细节让这成为一个功能，而不只是磁盘上的一堆文件。在会话开始时，Claude 的各类工具可以扫描所有可用的技能文件，并从 Markdown 文件的前置 YAML 中读取每个技能文件的简短说明。这在 token 使用上非常高效：每个技能仅占用几十个额外的 token，只有当用户提出该技能可解决的任务时，才会加载完整的详细内容。

- [试用 Slack 动图创建器技能](https://simonwillison.net/2025/Oct/16/claude-skills/#trying-out-the-slack-gif-creator-skill)
- [技能的发挥依赖于编程环境](https://simonwillison.net/2025/Oct/16/claude-skills/#skills-depend-on-a-coding-environment)
- [Claude 代码作为通用代理](https://simonwillison.net/2025/Oct/16/claude-skills/#claude-as-a-general-agent)
- [技能对比 MCP](https://simonwillison.net/2025/Oct/16/claude-skills/#skills-compared-to-mcp)
- [这些技能来了](https://simonwillison.net/2025/Oct/16/claude-skills/#here-come-the-skills)
- [简洁才是关键](https://simonwillison.net/2025/Oct/16/claude-skills/#the-simplicity-is-the-point)

#### 试试 Slack 的 GIF 生成器技能#

这是 Anthropic 今天早上发布的一个 slack-gif-creator 技能示例的元数据

> 用于创建针对 Slack 优化的动态 GIF 的工具包，并包含用于尺寸限制的验证器和可组合的动画基本元素。当用户根据“为我制作一个 Slack 用的 X 做 Y 的 GIF”这类描述请求 Slack 用的动态 GIF 或表情动画时，该技能即可使用。

我刚刚在 Claude 的移动网页应用中试用了这个技能，与 Sonnet 4.5 进行了对比。首先我在设置中启用了 slack-gif-creator 技能，然后我发起了提问：

> `Make me a gif for slack about how Skills are way cooler than MCPs`

而且克劳德给我做了这个 GIF。点击播放（它几乎会诱发癫痫，所以才用了点击播放机制）：

![](https://static.simonwillison.net/static/2025/skills_vs_mcps_still.gif)

这个特定的 GIF 虽然很糟糕，但技能的优势在于它们很容易迭代优化，从而变得更好。

以下是它编写的 Python 脚本中的一些值得注意的代码片段，我的注释：

```
# Start by adding the skill's directory to the Python path
import sys
sys.path.insert(0, '/mnt/skills/examples/slack-gif-creator')

from PIL import Image, ImageDraw, ImageFont
# This class lives in the core/ directory for the skill
from core.gif_builder import GIFBuilder

# ... code that builds the GIF ...

# Save it to disk:
info = builder.save('/mnt/user-data/outputs/skills_vs_mcps.gif', 
 num_colors=128, 
 optimize_for_emoji=False)

print(f"GIF created successfully!")
print(f"Size: {info['size_kb']:.1f} KB ({info['size_mb']:.2f} MB)")
print(f"Frames: {info['frame_count']}")
print(f"Duration: {info['duration_seconds']:.1f}s")

# Use the check_slack_size() function to confirm it's small enough for Slack:
passes, check_info = check_slack_size('/mnt/user-data/outputs/skills_vs_mcps.gif', is_emoji=False)
if passes:
 print("✓ Ready for Slack!")
else:
 print(f"⚠ File size: {check_info['size_kb']:.1f} KB (limit: {check_info['limit_kb']} KB)")
```

这真挺有意思的。Slack GIFs 的最大文件大小限制为 2MB，因此该技能内置了一个验证函数，模型可以用它来检查文件大小。如果文件过大，模型可以尝试再次将其缩小。

#### 技能依赖于编码环境 #

技能机制完全依赖于模型具备以下能力：访问文件系统、使用工具导航文件系统，以及在该环境中执行命令。

如今，这是 LLM 工具领域的一种常见模式——ChatGPT 代码解释器是 2023 年初这一模式的首个重要范例，此后，该模式通过 Cursor、Claude 代码、Codex CLI 和 Gemini CLI 等编码代理工具扩展到了本地设备。

这一要求是技能与其他以往拓展大语言模型(LLMs)能力的尝试之间最大的区别，例如 MCP 和 ChatGPT 插件。这是一项重要的依赖，但它能解锁的新能力之多，却有些令人困惑。

技能如此强大且易于创建，这一事实又为向 LLMs 提供安全的编码环境增添了另一个理由。不过，这里的'safe'一词其实含义深远！我们确实需要弄清楚如何最佳地对这些环境进行沙箱化处理，以使诸如提示注入之类的攻击所造成的损害控制在可接受的范围内。

#### Claude 代码作为通用代理

早在今年一月，我对人工智能/大语言模型（LLMs）做出了一些鲁莽的预测，其中包括“智能体”（agents）将会再次未能实现：

> 我认为 2025 年关于代理的炒作会越来越多，但我预计结果会让大多数对这个概念抱有期待的人大失所望。我预计会有很多人因为追逐几个不同但定义模糊且同名的梦想而损失大量金钱。

我之前完全错了。2025 年真的是“智能代理（agents）”的关键之年，不管你选择众多相互冲突的定义中的哪一个（我最终将其定义为“工具循环”）。

事后看来，Claude Code 这个名字起得不太好。它并非纯粹的编码工具，而是通用的计算机自动化工具。任何你通过向计算机输入命令能完成的任务，现在都可以由 Claude Code 实现自动化。用“通用代理”来形容它最为贴切。技能让这一点变得更加直观和明确。

我觉得这个技巧的潜在应用范围之广有点让人眼花缭乱。从数据新闻的角度想想：想象一个装满各种技能的文件夹，里面涵盖的任务如下：

- 哪里可以获取美国人口普查数据以及如何理解其结构
- 如何使用合适的 Python 库将不同格式的数据加载到 SQLite 或 DuckDB 中
- 如何在线发布数据？可以以 Parquet 文件形式存储在 S3 中，或者将其作为表格推送到 Datasette Cloud
- 由一位有经验的数据记者提出的一种技能，即如何在一组新数据中最好地发现有趣的故事
- 一种介绍如何使用 D3 构建简洁、易读的数据可视化的技能

恭喜你，你刚刚打造了一个能够针对美国最新发布的人口普查数据发现并协助发布故事的“数据新闻智能体”。而且你正是通过一个装满 Markdown 文件的文件夹，或许还有几个 Python 示例脚本来实现的。

#### 技能和 MCP 的比较

模型上下文协议自去年 11 月首次发布以来就备受关注。我喜欢开玩笑说，它之所以迅速走红，是因为每家公司都明白自己需要一个“AI 战略”，而构建（或宣布）MCP 的实施是满足这一需求的简便途径。

随着时间的推移，MCP 的局限性逐渐显现。最显著的体现在 token 使用上：GitHub 官方的 MCP 本身就因消耗数万上下文 token 而著称，一旦再添加一些，剩余空间就极为有限，留给 LLM 实际发挥有效作用的空间所剩无几。

自从我开始认真对待编码代理后，我对 MCP 的兴趣就减退了。几乎所有我能用 MCP 实现的事情，现在都可以改用命令行工具来完成。LLMs 知道如何调用 `cli-tool --help` ，这意味着你不需要花费很多 token 来描述如何使用它们——模型在以后需要的时候可以自己弄清楚。

技能的优势完全相同，只是现在我甚至不需要开发新的命令行工具。我可以直接用一个 Markdown 文件来描述如何完成任务，只有在有助于提高可靠性或效率时才添加额外的脚本。

#### 技能来了#

关于 Skills 最令人兴奋的事情之一，就是它们的共享十分便捷。我预计，许多技能将以单个文件的形式实现——而更复杂的技能则会是一个包含更多内容的文件夹。

Anthropic 拥有 Agent 技能文档和 Claude 技能手册。我已经在构思自己可能构建的技能，比如一个关于如何构建 Datasette 插件的技能。

我还喜欢技能设计的另一个特点是，完全没有任何东西会阻止它们与其他模型配合使用。

你现在就可以获取一个技能文件夹，将 Codex CLI 或 Gemini CLI 指向它，然后说“读取 pdf/SKILL.md，然后为我生成一个描述该项目的 PDF”，它就能正常工作，尽管这些工具和模型对技能系统并没有内置的相关知识。

我预计，技能领域将迎来一场寒武纪式的大爆发，这将使得今年的 MCP 热潮相比之下显得平平无奇。

#### 简洁才是重点

我注意到有人质疑“技能”，认为它们过于简单，几乎不能算作一项功能。很多人尝试过一种方法：在 Markdown 文件中加入额外指令，并告知编码代理在继续任务前先阅读该文件。AGENTS.md 是一种成熟的模式，该文件中已经可以包含类似“在尝试创建 PDF 之前先阅读 PDF.md”的指令

正是技能设计的核心简洁性，让我对它如此兴奋。

MCP 是一个完整的协议规范，涵盖主机、客户端、服务器、资源、提示、工具、采样、根、诱导以及三种不同的传输方式（标准输入输出、流式 HTTP 和原始的 SSE）

技能是带有少量 YAML 元数据的 Markdown 格式，以及一些可选脚本——这些脚本可以是你能在环境中使其可执行的任何内容。它们更贴近 LLMs 的核心精神：只需输入一些文本，让模型自行处理。

他们将困难部分外包给 LLM 平台和相关的计算机环境。鉴于过去几年我们对 LLMs 运行工具的能力的了解，我认为这是一个非常明智的策略。

定义 42 AI 1752 提示工程 176 生成式 AI 1549 LLMs 1513 Anthropic 215 Claude 218 代码解释器 28 AI 代理 89 编码代理 115 Claude 代码 67 技能 8

接下来：使用 Claude 代码通过蛮力使 DeepSeek-OCR 在 NVIDIA Spark 上正常运行

此前：NVIDIA DGX Spark：硬件出色，生态系统尚处早期阶段