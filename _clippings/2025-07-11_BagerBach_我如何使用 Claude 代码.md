---
title: "我如何使用 Claude 代码"
source: "https://www.reddit.com/r/ClaudeAI/comments/1lkfz1h/how_i_use_claude_code/"
author:
  - "[[BagerBach]]"
published: 2025-06-26
created: 2025-07-11
description:
tags:
  - "clippings"
---
嘿，[r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/)！这是一篇转自我博客 [的跨平台帖子](https://bagerbach.com/blog/how-i-use-claude-code) 。我在这里分享我对 Claude 代码的了解，希望你觉得它有用 ：）

  
自从 [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) 发布以来，我就一直是它的超级粉丝。

  
我第一次试用它的时候，它的出色表现让我大为惊叹。但高昂的令牌成本很快就让我望而却步。当时我觉得那些费用高得离谱，实在无法接受。

  
自从 Anthropic 允许使用 Claude.ai 订阅来支持 Claude Code 的使用后，这对我来说是个无需思考的决定。我很快就购买了 Max 层级来支持我的使用。

  
从那时起，我就广泛使用 Claude Code。我经常运行多个 CC 实例来进行某种形式的编码或对我有用的任务。如果我必须为使用付费，这将花费我数千美元。自从开始这样做以来，我的生产力有了显著提高，而且随着我越来越擅长使用这些智能编码工具，它一直在稳步提高。

##   
来自一次性项目……

  
智能编码带来了一个明显的好处，那就是可以接手一些一次性项目，你可以出于兴趣去探索这些项目。就在昨天，我从丹麦医疗系统下载了我所有的病历，并对其进行了格式化处理，以便大语言模型（LLM）能够轻松理解。然后我把它交给了 OpenAI 的 o3 模型，以帮助我更好地了解自己（有点非典型）的病史。这只花了我不到 15 分钟的时间来设置和引导，结果非常棒。我终于得到了多年来一直想知道的问题的答案。

  
有无数次，Claude（CC）帮我完成了一些有用的事情，但这些事情并不十分关键，在日常事务中没有被列为优先事项。

##   
致认真的开发者

  
我最感兴趣的是如何使用像 Claude Code 这样的工具来提高我的影响力，并创建更好、更有用的解决方案。虽然副业项目很有趣，但它们并不是最需要优化的事情。严肃的项目（通常）有现有的代码库和质量标准需要维护。

  
我在使用 Claude Code、[AmpCode](https://ampcode.com/) 以及其他人工智能编码工具进行这类项目时有着很棒的体验，不过编码模式有所不同：

- **上下文编排至关重要** ：除了任务规范之外，你还必须纳入既定的经验和方向线索。
- **你指导架构** ：你有责任提供并引导模型创建适合你系统上下文的设计。这意味着要更多地手把手指导，并为智能工具执行制定明确的计划。
- **少些随性编码，多些伙伴合作** ：它更像是一个智能的 sparring partner，会热切地为你处理琐碎任务，在某些方面有着惊人的能力，能在几分钟内阅读并理解数百页文档，但如果没有指导，它不太理解你的系统或项目。

##   
智能体编码的模式与技巧

  
这些建议大多可以归结为：

- 精通你正在使用的工具
- 构建并维护有助于你更好地使用这些智能编码工具的工具和框架。使用智能工具来编写这些内容。

  
随着时间的推移，你从智能编码工具中获得的技能和生产力提升将呈指数级增长。

  
以下是我尝试总结一些我在大量使用 Claude 代码过程中学到的最有用的模式和技巧。

###   
1\. 创建并维护一个 CLAUDE.md 文件

  
这可能感觉像是一件苦差事，但它非常有用，能为你节省大量时间。

  
在你的 CC 提示前加上 `#` 作为前缀，它会将你的指令添加到 CLAUDE.md 中，从而记住这些指令。

  
将 CLAUDE.md 文件放在子目录中，以便为测试、前端代码、后端服务等提供具体说明。精心整理你的上下文！

  
你在整理诸如 CLAUDE.md 这样的文件、（7）中的流程或（11）中的脚本上所做的投入，与投资你的开发工具是一样的。你会在没有代码检查器或格式化工具的情况下编写代码吗？没有语言服务器来纠正你并提供反馈呢？或者没有类型检查器呢？你可以这么做，但大多数人会认同这样做没那么容易，也没那么高效。

###   
2\. 使用这些命令

  
一些有用的：

- 计划模式（Shift+Tab）。我发现这提高了 Claude 的可靠性。它更有能力将任务执行到底。
- 详细模式（CTRL+R）可查看 Claude 所看到的完整上下文
- Bash 模式（`!` 前缀）用于运行命令并将输出作为下一轮的上下文添加进去
- 按 Esc 键中断，按两次 Esc 键跳回到对话历史记录

###   
3\. 并行运行多个实例

  
同时进行前端和后端开发是个很棒的方法。让一个实例使用占位符/模拟 API 构建前端，并在设计上进行迭代，而另一个智能体则编写后端代码。

  
你可以使用 Git 工作树在同一个代码库上与多个代理进行协作。老实说，当你必须启动多个 Docker Compose 环境时，麻烦大于收益，所以在那种项目中就使用单个 Claude 实例。或者干脆不要让项目的多个实例同时运行。

###   
4\. 使用子代理

  
只需让 Claude 代码这样做。

  
一种常见且有用的模式是使用多个子智能体从多个角度同时处理一个问题，然后让主智能体与你交流并找出最佳解决方案。

###   
5\. 使用视觉元素

  
使用屏幕截图（直接拖进来就行）。Claude Code 在理解视觉信息方面表现出色，可帮助调试用户界面问题或复制设计。

###   
6\. 选择 Claude 4 Opus

  
特别是如果你处于更高的层级。为什么不使用现有的最佳模型呢？

  
根据个人经验，它比 Claude 4 Sonnet 有显著提升，而 Claude 4 Sonnet 本身已经是一个不错的模型了。

###   
7\. 创建特定项目的斜杠命令

  
将它们放在 `.claude/commands` 中。

  示例：

- 常见任务或指令
- 创建迁移
- 项目设置
- 正在加载上下文/说明
- 每次需要重复但重点不同的任务

  
[@tokenbender](https://x.com/tokenbender) 写了一篇很棒的关于他们 [agent-guides](https://github.com/tokenbender/agent-guides) 设置的指南，展示了这种做法。

###   
8\. 使用扩展思维

  
对于需要更多思考的情况，如调试、规划、设计等，输入 `think`、`think harder` 或 `ultrathink`。

  
这些会增加思考预算，从而带来更好的结果（但耗时更长）。`ultrathink` 据称会分配 31,999 个标记。

###   
9\. 记录所有事项

  
让 Claude Code 将其想法、当前任务规范、设计、需求规范等写入一个中间的 Markdown 文档。这既能在之后提供上下文，又能作为当前的便签本。而且这会让你更易于验证并帮助指导编码过程。

  
在后续会话中使用这些文档非常宝贵。随着会话时长增加，上下文会丢失。只需再次阅读文档就能找回重要的上下文。

###   
10\. 适用于 Vibe 编码人员

  
使用 Git。经常使用它。你可以让 Claude 帮你写提交信息。说真的，当你在人工智能的帮助下快速推进时，版本控制变得更加关键。

###   
11\. 优化你的工作流程

- 继续上一个会话以保留上下文（使用 `--resume`）
- 使用 MCP 服务器（context7、deepwiki、puppeteer，或自行搭建）
- 为常见的确定性任务编写脚本，并让 CC 维护它们
- 使用 GitHub CLI 而非 fetch 工具来获取 GitHub 上下文。不要使用 `fetch` 工具从 GitHub 检索上下文。（或者使用 MCP 服务器，但 CLI 更好）。
- 使用 [ccusage](https://github.com/ryoppippi/ccusage) 来跟踪你的使用情况
	- 如果你使用的是专业版/Max 版本，这更像是一个有趣的噱头——你只会看到如果你使用 API 的话“可能会”花费多少。
	- 但是实时仪表盘（`bunx ccusage blocks --live`）对于查看你的多个代理是否接近达到速率限制很有用。
- 通过 [文档](https://docs.anthropic.com/en/docs/claude-code/overview) 了解最新信息 – 它们非常棒

###   
12\. 追求快速的反馈循环

  
为模型提供一种验证机制，以实现快速反馈循环。这通常会减少奖励作弊行为，特别是当与特定指令和约束条件结合使用时。

  
奖励作弊：指人工智能走捷径，看似成功解决了问题，实则并未真正解决。例如，它可能硬编码虚假输出，或者编写总是通过的测试，而不是去做实际的工作。

###   
13\. 在你的集成开发环境中使用克劳德代码

  
这种体验变得更类似于结对编程，并且它使 Claude 能够与集成开发环境（IDE）工具进行交互，这非常有用。例如，能够获取代码检查错误、当前活动文件等信息。

###   
14\. 对消息进行排队

  
在 Claude Code 运行时，你可以持续发送消息，这些消息会被排队等待下一轮处理。当你已经知道接下来要做什么时，这很有用。

  
目前有一个漏洞，即 CC 并不总是能看到这条消息，但通常是有效的。请注意这一点。

###   
15\. 压缩与会话上下文长度

  
要非常注意压缩。它能减少对话中的噪音，但也可能会压缩掉重要的上下文信息。在自然的停顿点提前进行压缩，因为压缩会导致信息丢失。

###   
16\. 获取一个更好的公关模板

  
这更多是我对模板本身的个人抱怨。

  
使用默认模板以外的其他拉取请求（PR）模板。似乎 Claude 4/CC 被指示使用特定模板，但那个模板很糟糕。“总结→更改→测试计划”还可以，但最好有一个根据你的具体 PR 或项目量身定制的 PR 正文。

##   超越编码

  
Claude 代码的用途不止于代码。

- 研究文档→撰写报告（例如用于其他会话上下文）
- 调试（它在这方面真的很擅长！）
- 完成功能后编写文档
- 重构
- 编写测试
- 找出 X 是在哪里完成的（例如，在新的代码库中，或者在你不熟悉的大型代码库中）。
- 在我的 Obsidian 知识库中使用 Claude 代码，对我的笔记（日记、想法、点子、笔记等等）进行广泛研究

##   
需要留意的事项

###   
使用工具时的安全性

  
对于你输入到模型中的外部上下文要格外小心，例如通过 MCP 或其他方式获取信息时。提示注入是一个切实的安全问题。人们可以在例如 GitHub 问题中编写恶意提示，从而让你的智能体泄露意外信息或采取前所未有的行动。

### Vibing

  
我仍然还没见过一种情况，即连续数小时进行全面的自动氛围编码是有意义的。没错，它是可行的，而且你也能这么做，但在人们必须积极维护代码的生产系统中，我会避免这样做。或者，至少要自己审查一下代码。

###   模型可变性

  
有时感觉 Anthropic 会根据模型需求使用量化模型。就好像模型质量会随时间变化。这可能是技术问题，但我看到其他用户也报告了类似的经历。虽然可以理解，但作为付费用户，感觉不太好。

##   
运行克劳德代码

  
我忍不住要摆弄和探索我使用的工具，并且我发现了一些与 Claude Code 一起使用的有趣配置。

  
我正在使用的一些环境变量尚未公开文档，所以在此提醒你，它们可能不稳定。

  
这是我用来以优化设置启动 Claude 代码的一个 bash 函数：

function ccv() {
  local env\_vars=(
    "ENABLE\_BACKGROUND\_TASKS=true"
    "FORCE\_AUTO\_BACKGROUND\_TASKS=true"
    "CLAUDE\_CODE\_DISABLE\_NONESSENTIAL\_TRAFFIC=true"
    "CLAUDE\_CODE\_ENABLE\_UNIFIED\_READ\_TOOL=true"
  )
  
  local claude\_args=()
  
  if \[\[ "$1" == "-y" \]\]; then
    claude\_args+=("--dangerously-skip-permissions")
  elif \[\[ "$1" == "-r" \]\]; then
    claude\_args+=("--resume")
  elif \[\[ "$1" == "-ry" \]\] || \[\[ "$1" == "-yr" \]\]; then
    claude\_args+=("--resume" "--dangerously-skip-permissions")
  fi
  
  env "${env\_vars\[@\]}" claude "${claude\_args\[@\]}"
}
- `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=true` ：禁用遥测、错误报告和自动更新
- `ENABLE_BACKGROUND_TASKS=true`：为长时间运行的命令启用后台任务功能
- `FORCE_AUTO_BACKGROUND_TASKS=true` ：无需确认即可自动将长任务发送到后台
- `CLAUDE_CODE_ENABLE_UNIFIED_READ_TOOL=true` ：统一文件读取功能，包括 Jupyter 笔记本。

  
这会给你：

- 针对长时间运行任务（例如你的开发服务器）的自动后台处理
- 无遥测数据或不必要的网络流量
- 统一文件读取
- 针对常见场景的便捷切换（`-y` 用于自动批准，`-r` 用于恢复）

---

## Comments

> **Cipher\_Lock\_20** • [7 points](https://reddit.com/r/ClaudeAI/comments/1lkfz1h/comment/mztxgct/) • 2025-06-26
> 
>   
> 谢谢！这就是我们在使用这些工具时需要的思维方式和实践方法。我讨厌“氛围编码”这个词如此笼统。像这样的帖子在鼓励尝试新事物的同时，也宣扬了最佳实践。
> 
>   
> 我总觉得我们有两个团队一直在争论。
> 
>   
> 拒绝改变的老行业资深开发者：“氛围编码员！！你什么都不懂，你的代码很烂，你得自己把所有代码都写出来”
> 
> Or the
> 
>   
> 我现在是个创业者了：“我在三天内推出了我的初创公司和全新的革命性应用程序。全凭感觉编码，运行完美！”
> 
>   
> 在中间存在一个不错的位置。学习语言，学习最佳实践，学习软件开发生命周期（SDLC）和 DevOps。版本控制仍然是绝对必要的。在你的管道中使用代码检查、Prettier、静态应用程序安全测试（SAST）和动态应用程序安全测试（DAST）工具。测试所有内容，审查差异，不要像分发糖果一样随意传递机密信息。这样的事项还有很多。
> 
>   
> 但是，有了这些智能体和工具，所有这些事情在实施、实践和理解上都变得简单得多！
> 
>   
> 就像你提到的，纯粹凭感觉编码在娱乐或原型制作方面肯定有它的用武之地，但一旦某件事变成了你打算分享或供他人使用的实际项目，你真的应该开始实施这些最佳实践。学习 Claude Code 和 Gemini CLI 类似于学习 GitHub 或你选择的 IDE 的工具。它们仍然是工具，可以被很好地使用，也可以只是用简单的提示随意操作，而全然不顾其他！
> 
>   
> 不管人们是否喜欢，软件开发都在发生变化，而我们仍然不确定未来5到10年它会是什么样子。现在是掌握基础知识并彻底学习这些工具的绝佳时机。

> **Expert\_Ad\_8272** • [2 points](https://reddit.com/r/ClaudeAI/comments/1lkfz1h/comment/mzsswzx/) • 2025-06-26
> 
>   
> 写得真好，最后一部分很吸引我，我会进一步研究这个，你使用那些实验性标志的体验如何？
> 
> > **BagerBach** • [1 points](https://reddit.com/r/ClaudeAI/comments/1lkfz1h/comment/mzv0mg1/) • 2025-06-26
> > 
> >   
> > 谢谢！后台任务标志很不错，但 Claude Code 目前还无法妥善处理它。当任务被强制设为后台任务时，Claude Code 不知道如何获取任务的日志。

> **Same\_Fruit\_4574** • [2 points](https://reddit.com/r/ClaudeAI/comments/1lkfz1h/comment/mzt09vg/) • 2025-06-26
> 
>   
> 信息非常丰富。你能解释一下如何对消息进行排队，以及在达到使用限制后如何自动恢复吗？
> 
> > **BagerBach** • [2 points](https://reddit.com/r/ClaudeAI/comments/1lkfz1h/comment/mzv0svd/) • 2025-06-26
> > 
> >   
> > 谢谢，很高兴听到这个消息。
> > 
> >   
> > 排队大多是在你有一个正在进行的会话时使用。当它已经在做某件事时，我只是发送更多消息。
> > 
> >   
> > 可以使用\`--resume\`或\`--continue\`来恢复。我使用最高层级时不太常遇到速率限制，所以不需要自动恢复，很遗憾在这方面我帮不上太多忙。

> **AI\_JERBS** • [2 points](https://reddit.com/r/ClaudeAI/comments/1lkfz1h/comment/mztdch6/) • 2025-06-26
> 
>   
> 真的很感谢这些专业提示！

> **No-Dig-9252** • [2 points](https://reddit.com/r/ClaudeAI/comments/1lkfz1h/comment/n049iij/) • 2025-06-27
> 
>   
> 这是一次精彩的剖析，真的很感谢你分享这一切。特别是《Claude.md》和子代理模式让我深有感触。我一直在 Jupyter 中使用代理工作流程和 MCP 工具做类似的事情，但没有一个针对每个服务/组件记录提示的正式结构——现在肯定要借鉴这个了。
> 
>   
> 另外，在使用可视化方面我也赞成。Claude 4 仅通过我的开发服务器的屏幕截图就能极其出色地调试布局问题。
> 
>   
> 你有没有试过像 [数据层](https://datalayer.ai/) 这样的东西？它能让我在 Jupyter 中运行类似 Claude 的智能体工作流程，并且在人工智能、单元格和代码上下文之间实现非常简洁的集成。虽然不像 Claude 那样经过充分测试，但对于混合工作流程来说非常有前景。
> 
>   
> 再次感谢——这篇帖子内容很丰富。
> 
> > **BagerBach** • [1 points](https://reddit.com/r/ClaudeAI/comments/1lkfz1h/comment/n08yfxs/) • 2025-06-28
> > 
> >   
> > 谢谢！很高兴你觉得它有趣。我还没试过数据层，但可能会去看看 ：）

> **SpeedyBrowser45** • [2 points](https://reddit.com/r/ClaudeAI/comments/1lkfz1h/comment/mzsao8b/) • 2025-06-25
> 
>   
> 看起来写得非常好，但我这边已经很晚了，我可以把这个教程复制到我的电脑上之后再看吗？
> 
> > **\[deleted\]** • [0 points](https://reddit.com/) • 2025-06-26
> > 
> > Thanks, ^\_^
> > 
> > > **SpeedyBrowser45** • [2 points](https://reddit.com/r/ClaudeAI/comments/1lkfz1h/comment/mzswq44/) • 2025-06-26
> > > 
> > > Thanks, ^\_^
> > > 
> > > **Queasy\_Question673** • [1 points](https://reddit.com/r/ClaudeAI/comments/1lkfz1h/comment/mzts64s/) • 2025-06-26
> > > 
> > > You are absolutely right!
> 
> **Familiar\_Gas\_1487** • [2 points](https://reddit.com/r/ClaudeAI/comments/1lkfz1h/comment/mzt005j/) • 2025-06-26
> 
> 🤣

> **onepunchcode** • [0 points](https://reddit.com/r/ClaudeAI/comments/1lkfz1h/comment/mzvc74y/) • 2025-06-26
> 
>   
> 你说的**减少氛围编码**是什么意思？去你的

> **Ok\_Maize\_3709** • [1 points](https://reddit.com/r/ClaudeAI/comments/1lkfz1h/comment/mzua336/) • 2025-06-26
> 
>   
> 一个愚蠢的问题，但是例如有没有可能撤销 Claude 在最后两条消息中所做的编辑（即它在会话中有没有版本控制）？
> 
> > **BagerBach** • [2 points](https://reddit.com/r/ClaudeAI/comments/1lkfz1h/comment/mzv0vsb/) • 2025-06-26
> > 
> >   
> > Claude 没有其他人工智能编码工具所具备的那种检查点系统，所以我在编码时对使用 Git 非常谨慎
> > 
> > **rThoro** • [2 points](https://reddit.com/r/ClaudeAI/comments/1lkfz1h/comment/mzwy9hv/) • 2025-06-26
> > 
> >   
> > 不，但你可以告诉它，因为它处于上下文环境中，它可以撤销这些更改（除非是脚本）
> > 
> > **Mother\_Primary\_9016** • [2 points](https://reddit.com/r/ClaudeAI/comments/1lkfz1h/comment/n04np1j/) • 2025-06-27
> > 
> >   
> > 告诉克劳德提交他的更改，或者手动提交

> **zinozAreNazis** • [1 points](https://reddit.com/r/ClaudeAI/comments/1lkfz1h/comment/mzud69d/) • 2025-06-26
> 
>   
> 你的 GitHub 仓库是什么/你的背景是怎样的？
> 
> > **BagerBach** • [2 points](https://reddit.com/r/ClaudeAI/comments/1lkfz1h/comment/mzv10jz/) • 2025-06-26
> > 
> >   
> > 软件工程师。[github.com/chhoumann](http://github.com/chhoumann)
> > 
> > > **zinozAreNazis** • [0 points](https://reddit.com/r/ClaudeAI/comments/1lkfz1h/comment/mzvj98t/) • 2025-06-26
> > > 
> > >   
> > > 感谢你的回复。我看了你的.zshrc 文件，我可以保证你不是那种装样子的“程序员”。既然你很懂行，那我现在要去读那篇文章了。再次感谢！

> **maurinator2022** • [1 points](https://reddit.com/r/ClaudeAI/comments/1lkfz1h/comment/mzujp9e/) • 2025-06-26
> 
>   
> 很棒的信息。你对 /collect 或 /clear 有什么看法？
> 
> > **BagerBach** • [1 points](https://reddit.com/r/ClaudeAI/comments/1lkfz1h/comment/mzv1wyq/) • 2025-06-26
> > 
> >   
> > 理想情况下，你应该将任务分解到足够小，以便在单个会话中就能处理。
> > 
> >   
> > 我从来没有真正用过清除功能。我只是开启了另一个会话。
> > 
> > > **maurinator2022** • [1 points](https://reddit.com/r/ClaudeAI/comments/1lkfz1h/comment/mzv2maa/) • 2025-06-26
> > > 
> > > Thanks

> **joeyda3rd** • [1 points](https://reddit.com/r/ClaudeAI/comments/1lkfz1h/comment/mzumjet/) • 2025-06-26
> 
>   
> 感谢这篇文章！实际上我在使用 CC SDK 构建会话监控器时看到了那些标志。我相信有关于它们的文档，我会再在参考资料里找找看。
> 
>   
> 你认为在你的工作流程中，你尚未找到解决方案的最大困扰或反复出现的麻烦是什么？
> 
> > **BagerBach** • [1 points](https://reddit.com/r/ClaudeAI/comments/1lkfz1h/comment/mzv1tra/) • 2025-06-26
> > 
> >   
> > 嘿！据我所知，后台任务尚未有文档记录，所以我才写了那个内容 ：）
> > 
> >   
> > 以下是一些：
> > 
> >   
> > \- 总是需要靠近我的电脑才能让代理运行。我正在使用各种远程工具通过手机连接到我的电脑，但体验不太好。  
> >   
> > \- 模型还不够智能，以至于我仍需要在上下文整理方面做大量工作。很希望看到自动化的、长期的项目或组织记忆（比如像 Devin 那样的？）  
> >   
> > \- 使用终端工具来做这类工作感觉像是个折中的办法，但目前还不错  
> >   
> > \- 在以跳过权限检查的“危险”模式运行时，我希望它能进行更多规划，或者我可以强制它退出跳过权限模式并进入规划模式  
> >   
> > \- 任务排队。我还没有找到一个能让它更自主运行的好办法，即能够完成一项任务，然后接着处理下一项任务并重复。我试过各种方法，但都不够好，不值得我花时间去用。
> > 
> > > **joeyda3rd** • [1 points](https://reddit.com/r/ClaudeAI/comments/1lkfz1h/comment/mzv9mmt/) • 2025-06-26
> > > 
> > >   
> > > 我现在实际上正在做第一个。做一个超级移动端的东西。更像是一个概念验证。想想贾维斯那种。
> > > 
> > >   
> > > 到目前为止，上下文管理是最让我头疼的问题。有些人制作了多个工具，但似乎没有一个是令人满意的。这肯定是一个完整的研究领域。
> > > 
> > >   
> > > 你试过任何集成开发环境（IDE）集成吗？我用过原生的 IDE 命令，但似乎没什么用。
> > > 
> > >   
> > > 让它们专注于任务也很困难。我发现对我来说最好的方法是复制粘贴详细的说明，但这也不是万无一失的。参考文档甚至也不能真正提高准确性，但总比没有好。
> > > 
> > > > **BagerBach** • [1 points](https://reddit.com/r/ClaudeAI/comments/1lkfz1h/comment/mzvcsp8/) • 2025-06-26
> > > > 
> > > >   
> > > > 不错！要是能看到就好了。我一直在关注 [https://vibetunnel.sh/](https://vibetunnel.sh/) ，但不幸的是它仅适用于苹果电脑。
> > > > 
> > > >   
> > > > 至于 IDE 集成，我使用的是基本的/ide。但我对像 OpenCode 这样具有 LSP 支持的工具非常感兴趣。我主要希望 Claude Code 不要对我们现有的工具视而不见。  
> > > >   
> > > > 除此之外，就是大量的搭建工作以及教授如何使用我常用的命令行界面工具。
> > > > 
> > > >   
> > > > 我通常会预先花不少时间创建文档。这似乎真的能加快流程，避免走入歧途。比如说，让它理解我们即将修改的代码库部分，而不是直接让它进行修改。将较大的任务分解。在与新的/外部服务或包集成时，先让它为其创建文档，然后在新会话中使用这些文档。
> > > > 
> > > > > **joeyda3rd** • [1 points](https://reddit.com/r/ClaudeAI/comments/1lkfz1h/comment/mzvk9bp/) • 2025-06-26
> > > > > 
> > > > >   
> > > > > 我正在探索是否有一种简单的方法，可以在提示（prompt）和智能体（agent）之间注入一个轻量级的上下文管理层，同时在速度和令牌数量方面不会有太大损失。我正在探索一种中间层为大语言模型（LLM）的方法，这种方法会对提示进行调整，但保留其意图。我想我会看看是否有办法在提示中安全地注入不可变的上下文，但我相信一定有更好的办法。

> **JimboTheClown** • [1 points](https://reddit.com/r/ClaudeAI/comments/1lkfz1h/comment/mzvgwm6/) • 2025-06-26
> 
>   
> 我的克劳德代码直接忽略了 claude.md...
> 
> > **BagerBach** • [1 points](https://reddit.com/r/ClaudeAI/comments/1lkfz1h/comment/mzxelh2/) • 2025-06-26
> > 
> >   
> > 有时你需要让它读取文件。希望这个问题能很快得到解决！

> **Odd\_Philosophy\_1941** • [1 points](https://reddit.com/r/ClaudeAI/comments/1lkfz1h/comment/mzvy1br/) • 2025-06-26
> 
>   
> 感谢这篇很棒的文章。我也订阅了你的时事通讯。
> 
>   
> 我试图在我的.zshrc 中使用你的 ccv，在 Claude 4 Sonnet 的帮助下我不得不稍作修改。
> 
>   
> 以下是代码：[https://gist.github.com/spilist/6b065cda20c0e75436d018e147f0cad9](https://gist.github.com/spilist/6b065cda20c0e75436d018e147f0cad9)
> 
> > **BagerBach** • [1 points](https://reddit.com/r/ClaudeAI/comments/1lkfz1h/comment/mzxe5h4/) • 2025-06-26
> > 
> >   谢谢！
