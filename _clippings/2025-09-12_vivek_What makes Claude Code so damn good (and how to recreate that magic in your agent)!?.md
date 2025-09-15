---
title: "What makes Claude Code so damn good (and how to recreate that magic in your agent)!?"
source: "https://minusx.ai/blog/decoding-claude-code/"
author:
  - "[[vivek]]"
published: 2025-09-12
created: 2025-09-12
description: "Claude Code is the most delightful AI agent/workflow I have used so far.  Not only does it make targeted edits or vibe coding throwaway tools less annoying, ..."
tags:
  - "vivek"
---
# 是什么让 Claude 代码如此出色（以及如何在你的智能体中重现那种魔力）！？

/ [维韦克](https://x.com/nuwandavek) / 2025 年 8 月 21 日

Claude Code 是我目前使用过的最令人愉悦的人工智能代理/工作流程。它不仅能让有针对性的编辑或临时编码工具不那么烦人，使用 Claude Code 还让我很开心。它有足够的自主性去做有趣的事情，同时不会像其他一些工具那样导致令人不安的失控感。当然，大部分繁重的工作是由新的 Claude 4 模型完成的（尤其是交错思考）。但我发现，即使与 Cursor 或 Github Copilot 代理使用相同的基础模型，Claude Code 在客观上使用起来也不那么烦人！是什么让它如此出色呢？如果你正在读这篇文章并点头认同，我将尝试给出一些答案。

**注意** ：这不是一篇关于 Claude Code 架构剖析的博客文章（网上已经有一些很不错的了）。这篇博客文章旨在根据我过去几个月使用和钻研 Claude Code 的经验（以及我们截获并分析的所有日志），为构建令人愉悦的 LLM 智能体提供一份指南。你可以在 [附录部分](https://minusx.ai/blog/decoding-claude-code/#appendix) 找到 [提示词](https://minusx.ai/blog/decoding-claude-code/#appendix) 和 [工具](https://minusx.ai/blog/decoding-claude-code/#appendix) 。这篇文章约 2000 字，所以系好安全带！如果你想快速了解要点， [总结](https://minusx.ai/blog/decoding-claude-code/#how-to-build-a-claude-code-like-agent-tldr) 部分是个不错的起点。

  

![prompts](https://minusx.ai/images/claude-code/prompts.png)

你可以清楚地看到 Claude 代码的不同更新。

  

Claude Code（CC）用起来感觉很棒，因为它 *就是能正常运行* 。CC 是在对 LLM 擅长什么和不擅长什么有基本理解的基础上精心打造的。它的提示和工具弥补了模型的不足，帮助它在擅长的领域发光发热。控制循环极其容易理解，调试起来也很简单。

CC 一经推出，我们就在 MinusX 开始使用了。为了深入了解其内部情况， [斯里吉特](https://x.com/ppsreejith_) 编写了一个日志记录器，用于拦截并记录每一个发出的网络请求。以下分析基于我过去几个月的广泛使用。 **本文试图回答这个问题——“是什么让 Claude 代码如此出色，以及如何在你自己基于聊天的 LLM 代理中提供类似 CC 的体验？”** 我们已经将其中大部分内容融入到 MinusX 中了，我也很高兴看到你们也这样做！

  

![prompts](https://minusx.ai/images/claude-code/tools.png)

编辑是最常用的工具，其次是读取和待办事项写入

  

如果要从中学到一件事，那就是： **笨蛋，把事情简单化** 。调试和评估 LLMs 已经够糟糕的了。你引入的任何额外复杂性（多智能体、智能体交接或复杂的 RAG 搜索算法）只会让调试难上 10 倍。如果这样一个脆弱的系统还能运行，你之后会害怕对它进行大刀阔斧的更改。所以，把所有东西都放在一个文件里，避免过多的样板框架，并且至少把它们全部推翻几次:)

以下是 Claude Code 的主要要点，可在你自己的系统中实施。

- 1.1 [保持一个主循环（最多一个分支）和一个消息历史记录](https://minusx.ai/blog/decoding-claude-code/#11-keep-one-main-loop)
- 1.2 [对于各种各样的事情，一直都使用更小的模型。所有该死的事情，一直都这样。](https://minusx.ai/blog/decoding-claude-code/#12-use-a-smaller-model-for-everything)
- 2.1 [使用 claude.md 模式来协作并记住用户偏好](https://minusx.ai/blog/decoding-claude-code/#21-use-claudemd-for-collaborating-on-user-context-and-preferences)
- 2.2 [使用特殊的 XML 标签、Markdown 以及大量示例](https://minusx.ai/blog/decoding-claude-code/#22-special-xml-tags-markdown-and-lots-of-examples)
- 3.1 [大型语言模型搜索 >>> 基于检索增强生成的搜索](https://minusx.ai/blog/decoding-claude-code/#31-llm-search---rag-based-search)
- 3.2 [如何设计优秀的工具？（高级工具与低级工具）](https://minusx.ai/blog/decoding-claude-code/#32-how-to-design-good-tools-low-level-vs-high-level-tools)
- 3.3 [让你的智能体管理它自己的待办事项列表](https://minusx.ai/blog/decoding-claude-code/#33-let-the-agent-manage-a-todo-list)
- 4.1 [Tone and style](https://minusx.ai/blog/decoding-claude-code/#41-tone-and-style)
- 4.2 [" **请注意，这很重要** " 不幸的是，仍然是当前的技术水平](https://minusx.ai/blog/decoding-claude-code/#42-this-is-important-is-still-state-of-the-art)
- 4.3 [编写算法，包括启发式方法和示例](https://minusx.ai/blog/decoding-claude-code/#43-write-the-algorithm-with-heuristics-and-examples)
  

> Claude Code 在每个环节都选择架构上的简洁性——一个主循环、简单的搜索、简单的待办事项列表等等。抵制过度设计的冲动，为模型构建良好的框架，让它发挥作用！这又是一次端到端的自动驾驶吗？惨痛的教训啊！

---

可调试性 >>> 复杂的手工调整的多智能体语言链-图节点大杂烩。

尽管多智能体系统正风靡一时，但 Claude Code 只有一个主线程。它会定期使用几种不同类型的提示来总结 git 历史记录，将消息历史合并为一条消息，或者想出一些有趣的用户体验元素。但除此之外，它维护着一个扁平的消息列表。它处理分层任务的一种有趣方式是将自身作为一个子智能体生成，且该子智能体没有生成更多子智能体的能力。最多只有一个分支，其结果会作为“工具响应”添加到主消息历史中。

如果问题足够简单，主循环只需通过迭代工具调用就能处理它。但如果存在一个或多个复杂任务，主智能体就会创建自身的克隆体。最大1分支和待办事项列表的组合确保智能体有能力将问题分解为子问题，同时也能关注最终期望的结果。

我非常怀疑你的应用程序需要一个多智能体系统。每增加一层抽象，都会让你的系统更难调试，更重要的是，你偏离了通用模型改进的轨迹。

![Control Loop](https://minusx.ai/images/claude-code/control_loop.gif)

CC 进行的所有重要 LLM 调用中，超过 50%是针对 claude-3-5-haiku 的。它用于读取大文件、解析网页、处理 git 历史记录以及总结长对话。它还用于生成单字处理标签 —— 几乎针对每一次按键操作！较小的模型比标准模型（十四行诗 4、GPT-4.1）便宜 70 - 80%。可以大量使用它们！

Claude 代码有极其详尽的提示，其中充满了启发式方法、示例以及重要（啧啧）提醒。系统提示约 2800 个令牌长，而工具部分占用多达 9400 个令牌。用户提示始终包含 claude.md 文件，该文件通常可能另外有 1000 - 2000 个令牌。系统提示包含关于语气、风格、主动性、任务管理、工具使用策略以及执行任务的部分。它还包含日期、当前工作目录、平台和操作系统信息以及最近的提交。

[**去阅读完整的提示词**](https://minusx.ai/blog/decoding-claude-code/#appendix) ！

大多数编码代理创建者所采用的主要模式之一是上下文文件（又名游标规则/claude.md/agent.md）。有无 claude.md 时 Claude Code 的性能差异犹如天壤之别。这是开发者传递无法从代码库中推断出的上下文并将所有严格偏好进行编码的好方法。例如，你可以强制 LLM 跳过某些文件夹，或使用特定库。每次用户请求时，CC 都会发送 claude.md 的全部内容

我们最近在 MinusX 中引入了 [minusx.md](https://minusx.ai/blog/memory/) ，它正迅速成为我们的智能体用于编纂用户和团队偏好的实际上下文文件。

相当确定的是，XML 标签和 Markdown 是构建提示的两种方式。Claude Code 广泛使用这两种方式。以下是 Claude Code 中一些值得注意的 XML 标签：

- `<system-reminder>` ：这在许多提示部分的末尾使用，用于提醒大语言模型（LLM）那些它可能会忘记的事情。示例：
```markdown
<system-reminder>This is a reminder that your todo list is currently empty. DO NOT mention this to the user explicitly because they are already aware. If you are working on tasks that would benefit from a todo list please use the TodoWrite tool to create one. If not, please feel free to ignore. Again do not mention this message to the user.</system-reminder>
```
- `<good-example>` ， `<bad-example>` ：这些用于编纂启发式方法。当模型面临多个看似合理的路径/工具调用可供选择的岔路口时，它们会特别有用。示例可用于对比不同情况，并非常清楚地表明哪条路径更可取。示例：
```markdown
Try to maintain your current working directory throughout the session by using absolute paths and avoiding usage of \`cd\`. You may use \`cd\` if the User explicitly requests it.
<good-example>
pytest /foo/bar/tests  
</good-example>
<bad-example>
cd /foo/bar && pytest tests
</bad-example>
```

Claude 还使用 Markdown 来在系统提示中划分清晰的部分。示例 Markdown 标题包括：

- Tone and style
- Proactiveness
- 遵循惯例
- Code style
- Task Management
- Tool use policy
- Doing Tasks
- Tools

[**去阅读整个工具提示**](https://minusx.ai/blog/decoding-claude-code/#appendix) \- 它足足有 9400 个词元长！

CC 与其他流行的编码代理的一个显著不同之处在于它对 RAG 的摒弃。Claude Code 就像你一样搜索你的代码库，使用非常复杂的 `ripgrep` 、 `jq` 和 `find` 命令。由于 LLM 对代码理解得非常好，它可以使用复杂的正则表达式来找到几乎任何它认为相关的代码块。有时它会用较小的模型读取整个文件。

从理论上讲，检索增强生成（RAG）听起来是个好主意，但它引入了新的（更重要的是，隐藏的）失败模式。该使用什么相似度函数？什么重排器？如何对代码进行分块？对于大型 JSON 或日志文件该怎么办？使用语言模型（LLM）搜索时，它只查看 JSON 文件的 10 行来理解其结构。如果需要，它会再查看 10 行——就像你会做的那样。最重要的是，这是可通过强化学习（RL）学习的——BigLabs 已经在研究这方面的内容。模型承担了大部分繁重的工作——理应如此，这极大地减少了智能体中需要处理的部分数量。此外，以这种方式连接两个复杂的智能系统实在是很糟糕。我最近和一个朋友开玩笑说，这是 LLM 时代的相机与激光雷达之争，我只是半开玩笑而已。

这个问题让任何正在构建 LLM 智能体的人夜不能寐。你应该给模型一般性的任务（比如有意义的动作），还是应该给它低级的任务（比如打字、点击和使用 bash）？答案是视情况而定（而且你应该两者都用）。

Claude Code 拥有低级工具（Bash、读取、写入）、中级工具（编辑、Grep、通配符）和高级工具（任务、网页抓取、退出计划模式）。Claude Code 可以使用 bash，那么为什么还要提供一个单独的 Grep 工具呢？这里真正的权衡在于你期望你的智能体使用该工具的频率与智能体使用该工具的准确性之间的关系。Claude Code 如此频繁地使用 grep 和通配符，以至于将它们做成单独的工具是有意义的，但与此同时，它也可以针对特殊场景编写通用的 bash 命令。

同样，还有更高级的工具，如 WebFetch 或“mcp\_\_ide\_\_getDiagnostics”，它们的操作具有极高的确定性。这使大型语言模型（LLM）无需进行多次低级的点击和输入操作，并使其保持在正轨上。帮帮这个可怜的模型吧，好吗！？工具描述中有详细的提示和大量示例。系统提示包含有关“何时使用工具”或如何在两个能完成相同任务的工具之间进行选择的信息。

**Claude 代码中的工具：**

这是个好主意，原因有很多。在长期运行的大语言模型（LLM）智能体中，上下文衰减是个常见问题。它们一开始满腔热情地着手解决难题，但随着时间推移迷失方向，沦为垃圾。当前的智能体设计有几种方法来应对这个问题。许多智能体尝试过显式待办事项（一个模型生成待办事项，另一个模型执行它们）或多智能体交接+验证（产品需求文档/项目经理智能体 -> 实施者智能体 -> 质量保证智能体）

我们已经知道，由于诸多原因，多智能体交接不是个好主意。Claude Code 使用一个明确的待办事项列表，但这个列表是由模型维护的。这能让大语言模型（LLM）保持在正轨上（它被大量提示要频繁参考待办事项列表），同时又能让模型在实施过程中有中途纠正路线的灵活性。这还能有效地利用模型的交错式思维能力，随时拒绝或插入新的待办事项。

Claude 明确尝试控制智能体的审美行为。在系统提示中有关于语气、风格和积极性的部分，充满了说明和示例。这就是为什么 Claude Code 在其评论和积极性方面 “感觉” 很有品味。我建议直接将这其中的大部分内容原样复制到你的应用程序中。

```markdown
# Some examples of tone and style
- IMPORTANT: You should NOT answer with unnecessary preamble or postamble (such as explaining your code or summarizing your action), unless the user asks you to.
Do not add additional code explanation summary unless requested by the user.

- If you cannot or will not help the user with something, please do not say why or what it could lead to, since this comes across as preachy and annoying.

- Only use emojis if the user explicitly requests it. Avoid using emojis in all communication unless asked.
```

不幸的是，在要求模型不做某些事情方面，Claude 也并不出色。重要的是，非常重要的是，“从不”和“总是”似乎是引导模型避开雷区的最佳方式。我预计未来模型会更易于引导，从而避免这种糟糕的情况。但目前，Claude 大量使用这种方式，你也应该如此。一些例子：

```markdown
- IMPORTANT: DO NOT ADD ***ANY*** COMMENTS unless asked

- VERY IMPORTANT: You MUST avoid using search commands like \`find\` and \`grep\`. Instead use Grep, Glob, or Task to search. You MUST avoid read tools like \`cat\`, \`head\`, \`tail\`, and \`ls\`, and use Read and LS to read files.\n  - If you _still_ need to run \`grep\`, STOP. ALWAYS USE ripgrep at \`rg\` first

- IMPORTANT: You must NEVER generate or guess URLs for the user unless you are confident that the URLs are for helping the user with programming. You may use URLs provided by the user in their messages or local files.
```

确定大语言模型（LLM）需要执行的最重要任务并为其编写算法极其重要。尝试扮演大语言模型并通过示例进行演练，识别所有决策点并明确写出。如果以流程图的形式呈现会很有帮助。这有助于构建决策过程，并帮助大语言模型遵循指令。一定要避免的一件事是一大堆“做”与“不做”的内容。它们更难跟踪，而且相互排斥。如果你的提示有几千个词元长，你会无意中出现相互冲突的“做”与“不做”的内容。在这种情况下，大语言模型会变得极其脆弱，并且无法纳入新的用例。

Claude Code 系统提示中的“ `  任务管理  ` ”、“ `  执行任务  ` ”和“ `  工具使用策略  ` ”部分清晰地阐述了要遵循的算法。这也是添加大量启发式方法以及 LLM 可能遇到的各种场景示例的部分。

在引导大语言模型（LLMs）方面，很多努力都在试图对其训练后/基于人类反馈的强化学习（RLHF）数据分布进行逆向工程。应该使用 JSON 还是 XML？工具描述应该放在系统提示中还是仅放在工具里？你的应用程序的当前状态又如何呢？了解它们在自己的应用程序中是怎么做的，并以此为你的应用程序提供参考，这会很有帮助。Claude 代码设计有很强的倾向性，利用这一点来形成你自己的设计会很有帮助。

  

再次强调，主要的收获是保持简单。极端的脚手架框架对你的伤害大于帮助。Claude Code 真的让我相信一个“智能体”可以既简单又极其强大。我们已经将很多这些经验教训融入到 MinusX 中，并且还在继续融入更多。

如果你有兴趣为自己的大语言模型（LLM）智能体编写 Claude 代码，我很乐意聊聊——在 [推特](https://x.com/nuwandavek) 上联系我！如果你想为你的 Metabase 获取像数据智能体那样可训练的 Claude 代码，查看一下 [MinusX](https://minusx.ai/) ，或者 [在此处](https://minusx.ai/demo) 与我预约一次演示。（用 Claude）编码愉快！

  

---