---
title: "I created an AMAZING MODE called \"RIPER-5 Mode\" Fixes Claude 3.7 Drastically! - Showcase"
source: "https://forum.cursor.com/t/i-created-an-amazing-mode-called-riper-5-mode-fixes-claude-3-7-drastically/65516"
author:
  - "[[Cursor - Community Forum]]"
published: 2025-03-17
created: 2025-04-24
description: "This has fixed just about EVERY SINGLE problem for me with Claude 3.7 in Cursor - It has turned my development into a CRACKED BEAST - I code about 12 hours a day, and I work on about 2 different Cursor windows at a time …"
tags:
  - "clippings"
---
## 我创建了一个名为“RIPER-5 模式”的惊人模式！极大地修复了 Claude 3.7！

[Showcase](https://forum.cursor.com/c/showcase/9)

[T1000](https://forum.cursor.com/u/T1000)

酷炫且详细的方法！

你是将其作为项目规则、用户规则，还是在每次聊天开始时，亦或是项目规则（.cursor/rules/..）中设置这个？

对我来说，如果在用户规则或.cursorrules 中，这会导致混淆。

[robotlovehuman](https://forum.cursor.com/u/robotlovehuman)

我将其设置为基于项目的规则，因为有时如果我想为一个简单任务打开一个新的光标窗口，我不需要它进入 RIPER - 5 模式 - 但如果是我的主要项目，那么我会将其粘贴到基于项目的规则中，这与设置中规则页面上半部分的默认规则不同 - 有时，如果我跳过执行非常简单的小任务并且不想创建新窗口，在这种情况下，我会保留一个名为 Docs 的文件夹，我将其粘贴为 riper\_5\_mode.txt，然后直接将其拖到 PRIME 的特定聊天线程中 - 这样，如果我创建一个新线程，它将不会被 riper 初始化，我可以快速完成一些事情 - 所以它非常可根据你的工作流程进行定制 - 使其适合你，这 5 种模式基本上有开发的基本逻辑方法，但每个人都不同。你也可以有一个默认的起始模式 - 有很多情况，但一旦你开始实现模式，你会很快发现自己根据确切的工作流程对其进行调整 - 所以从 Riper - 5 开始，然后通过反复试验进行调整 - 祝你好运

[T1000](https://forum.cursor.com/u/T1000)

酷，是的，我正在为我的工作流程优化模式做一些类似的事情，大部分作为单独的 mode.md 文件以便于参考，有些也作为项目规则。

[RichardRourc](https://forum.cursor.com/u/RichardRourc)

我的 Claude 3.7 在更新新版本后变得更蠢了。酷 我再也不会更新新版本了

[Xiaobuyudesu](https://forum.cursor.com/u/Xiaobuyudesu)

惊人的提示！现在我 claude3.7 指令的执行准确性有了飞跃式的提高！谢谢！

[DaniloCast](https://forum.cursor.com/u/DaniloCast)

在一个大型代码库上试用了 rn，结果根本不行。Claude 甚至都没有遵守在切换模式前等待我许可的基本规则，或者在 PLAN 模式下不编写代码的规则。

[moinsen-dev](https://forum.cursor.com/u/moinsen-dev)

喜欢它，如此真实。我希望光标开发者能读到这个！

我会试试。非常好的方法，感谢分享！

那么你可能需要对你的代码库进行一些严格的封装，以便为基于人工智能的系统进行开发做好准备。你不能有一个没有针对人工智能工作流程进行优化的大型代码库，你必须始终牢记 200k 窗口上下文。因此，你的代码可能需要进行重组和重新设计，以实现超级模块化。它的工作方式是将其解耦为尽可能小的模块单元，并分离关注点，然后这样你就可以一次处理一个模块，使其很好地适应上下文并提高效率。如果它“立即”失去上下文，那就意味着它仍然没有你想象的那么模块化，而且你输入的内容超出了它的最大令牌数。

使用基于人工智能的系统意味着你必须彻底重新思考整个结构和架构，以便以一种针对此进行优化的方式对其进行重写。

遵循简单的私有/公共设计，即针对每个特定组件/功能创建一个私有文件夹，并将该特定组件进一步分解为尽可能小的关注单元，就像遵循严格的“关注点分离”方法一样。然后创建一个简单的公共 API 来处理该特定功能的编排。接着创建另一个脚本，仅处理较小编排的编排。依此类推，直到最后高层代码越来越小，此时你拥有这种超级分层的树形模块化结构，在这种结构中，你可以轻松地在任何现代环境中（我所说的现代是指在过去三个月内！）进行良好的开发。

祝你好运！

[moinsen-dev](https://forum.cursor.com/u/moinsen-dev)

我试过了，但 Cursor 自行完成了转换。

[lisong233](https://forum.cursor.com/u/lisong233)

使用它时，我不确定\[模式：研究\]和\[模式：创新\]之间的区别。我应该在什么情况下使用每种模式？在我的工作流程中，它们似乎没有太大区别。顺便说一下，我正在进行人工智能开发。

[maxfahl](https://forum.cursor.com/u/maxfahl)

酷。这是我在 GitHub 上的提示的一个不错替代方案 - maxfahl/cursor-agent-master-prompt：光标代理 - 主提示

根据你的需求有多个提示可供测试，这很不错

太棒了！我喜欢每个人基本上都会开始真正接受模式，并且很快每个人都会根据自己的喜好进行调整！我甚至有时会随意触发多个模式，如果你愿意的话，几乎就像模式嵌套在模式中一样！——不过我得说，我知道这仍然不是最有效的方法，真正绝对有效的方法是有一个起始模式来指导代理工作流程——这样模式就只是在编排代理触发——如果你想超级高效，实际上你会创建一个比初始实例中预设的静态文本更具动态性的代理模式——但你知道这可能有些过头了（我真的怀疑这是否过头，因为一旦你的代码超过 10 个文件，基本上就需要这种高级代理模式方法，而不是仅仅使用纯静态文本模式）

研究纯粹是收集信息、阅读你的代码库、理解它、收集信息，仅此而已——你不是在创造任何东西，不是在头脑风暴，你纯粹是在了解你的项目的完整状态。然后创新模式是你真正进行头脑风暴并创新新想法、修复、重构、添加功能的时候，你知道这是主要的开发部分——这就是实际开发发生的地方，你在这个模式和其他模式之间切换，一旦你觉得有了一个可靠的想法，你就进入计划模式，像制定游戏计划一样把它勾勒出来——然后你回到创新模式检查它，看看是否有意义，反复来回——直到计划完全合理，然后你切换到执行模式，现在不再思考，而是纯粹按照计划模式中的精确清单执行——最后在结束时，你对照计划审查实际的变更，审查者检查你是否有偏差等

[kamusis](https://forum.cursor.com/u/kamusis)

很棒的方法！你能为此规则上传一个 Markdown 文件吗？

明白了！但我还有一个问题。这个工作流程似乎对上下文有非常高的要求。即使我只在前一个模式下停留了一次对话，计划模式下的编辑器仍然经常显示“未做更改”  
但说实话，今天下午（实际上是昨天，哈哈），Claude 的服务出现了故障，频繁更新的 Cursor 也有很多漏洞。我不知道是因为我的代码模块化不够，占用了太多上下文空间，还是仅仅是服务提供商的问题。

[robotlovehuman](https://forum.cursor.com/u/robotlovehuman)

是的，我也是这样。就是那种特定的高负载情况，或者你偶尔会遇到小故障，或者系统直接跳过某些内容。在这种情况下，可以尝试切换到代理模式之类的——但这与我之前描述的 RIPER-5 模式无关，RIPER-5 模式的目的是完全驯服它，使其像马一样易于操控，你就像在用力拉紧马的缰绳，让它完全按照你的意愿行动，并应对它那些奇怪的、过于急切的随机倾向。这就像是这种新出现的不良行为是其潜在的、大幅提升的智能所带来的权衡。比如 Claude 3.5 就没那么急切，也不会在没有要求的情况下随意偏离主题，但话说回来，3.5 的能力不如 3.7。所以你看，每一次改进都会带来一个你必须“驯服”的副作用，而这就是 RIPER-5 的目标。与其他类似的“接地”技术结合使用，Cursor 已经在实施规则和基于项目的规则，都是为了驯服这些“野兽”！

[moinsen-dev](https://forum.cursor.com/u/moinsen-dev)

来自 Cursor MCP Brave Search 的各位，好消息：

[![image](https://us1.discourse-cdn.com/flex020/uploads/cursor1/optimized/3X/c/9/c9e44760286bb2aea9b8c88f38fe5c16f6cebe51_2_690x174.png)](https://us1.discourse-cdn.com/flex020/uploads/cursor1/original/3X/c/9/c9e44760286bb2aea9b8c88f38fe5c16f6cebe51.png "image")

MCP 很棒，工具也很棒，但“某些东西”也必须知道如何使用它。

我为每个 RIPER-5 模式创建了自定义代理模式，这使我能够调整模型（例如，INNOVATE 使用思维模式），并根据需要允许/禁止编辑或工具使用。每个代理模式都包含切换到所需 RIPER-5 模式的明确说明，这样我就不必执行命令，只需更改代理模式即可。到目前为止，它似乎运行得相当不错。

[lisong233](https://forum.cursor.com/u/lisong233)

坏消息。自定义聊天似乎仅在 0.47.1 版本中可用，后续更新中没有此功能

它确实有这个功能，但你可以先安装 47.1v，然后在测试版设置选项卡中启用它，再升级到最新版本，如果可行请告诉我。

另外，你可以执行一些额外的步骤，即在启用所需设置后，你需要按顺序安装它，这里有一个指向我的子论坛的链接：自定义聊天很棒（提示）0.47.x - 作者 ChiR24 的第 28 篇帖子

[EricObern](https://forum.cursor.com/u/EricObern)

天哪，谢谢，谢谢，谢谢，谢谢！！！

讨厌的氛围编码员在此，完全不知道自己在做什么。这有助于大大放慢速度，以便我在必要时能尽可能地谷歌搜索和研究。

我确实遇到了一个早期问题，即它在创新模式下不遵守规则并建议代码。当我问它为什么不遵守我的规则时，它只是为自己的急切表示歉意，说我是对的，告诉我它应该做什么，然后继续前进。

从那以后，我在每一个输入的末尾都添加了“不要偏离我的规则”。这似乎能让它步入正轨。

谢谢！

[djduarte](https://forum.cursor.com/u/djduarte)

你的方法真的很巧妙。

我有多年的编码经验，但在“氛围编码”方面经验不多……

但是给人工智能一种结构化的方式去遵循是很巧妙的。

[johnpeterman72](https://forum.cursor.com/u/johnpeterman72)

我对此真的是放声大笑……

[andresreibel](https://forum.cursor.com/u/andresreibel)

通过快速模式和更短的模式命令得到了略微改进：

RIPER-5 模式：严格操作协议

上下文入门

你是 Claude 3.7，集成在 Cursor IDE 中，这是一个由人工智能驱动的 VS Code 分支。你往往过于急切，会进行未经授权的更改，从而破坏逻辑。这是不可接受的。为防止这种情况发生，你必须遵循以下严格协议：

⸻

元指令：模式声明要求

你必须在每个回复的开头用括号注明你当前的模式。无一例外。  
格式：\[模式：模式名称\]  
未能声明您的模式是严重违规行为。

⸻

RIPER-5 模式

模式 1：研究

命令：执行资源  
标签: \[模式: 研究\]

目的：理解现有代码，收集信息  
允许：读取文件、提出澄清问题  
禁止：建议、实施、规划或行动  
要求：只求理解，不做修改  
持续时间：直到明确切换到下一个模式

⸻

模式 2：创新

命令：执行旅馆（不太明确这个具体语境，“inn”常见释义为旅馆，但这里结合“do”不太好准确理解确切意思，按要求保持原文）  
标签: \[模式: 创新\]

目的：集思广益，探讨可能的解决方案  
允许：讨论想法、利弊、寻求反馈  
禁止：规划、实施细节、代码编写  
要求：想法必须以可能性的形式呈现，而非决策  
持续时间：直到明确切换到下一个模式

⸻

MODE 3: PLAN

Command: do pla  
Tag: \[MODE: PLAN\]

Purpose: Create an exact, exhaustive implementation plan  
Allowed: File paths, function names, technical details  
Forbidden: Any code writing, even examples  
Requirement: Plan must be so detailed that no creative decisions are needed later  
Final Step: Convert plan into a CHECKLIST

IMPLEMENTATION CHECKLIST FORMAT:  
1\. \[Specific action\]  
2\. \[Specific action\]  
3\. …

Duration: Until explicitly approved and moved to the next mode

⸻

MODE 4: EXECUTE

Command: do exe  
Tag: \[MODE: EXECUTE\]

Purpose: Implement EXACTLY what was planned in do pla  
Allowed: Only the steps in the plan  
Forbidden: Any deviation, improvement, or creative addition  
Requirement: 100% adherence to the approved plan  
Deviation Handling: If ANY issue requires deviation → IMMEDIATELY return to do pla

⸻

MODE 5: REVIEW

Command: do rev  
Tag: \[MODE: REVIEW\]

Purpose: Strictly compare implementation with plan  
Allowed: Only verification, no changes  
Requirement: EXPLICITLY FLAG ANY DEVIATION

Deviation Format:  
DEVIATION DETECTED: \[description\]

Final Verdict:  
• IMPLEMENTATION MATCHES PLAN EXACTLY  
• IMPLEMENTATION DEVIATES FROM PLAN

Duration: Until explicitly confirmed

⸻

MODE 6: FAST

Command: do fas  
Tag: \[MODE: FAST\]

Purpose: Rapid task execution with minimal changes  
Allowed: Implement only the assigned task  
Forbidden: Modifying existing logic, adding optimizations, or refactoring  
Requirement: Every change must be as small as possible  
Deviation Handling: If ANYTHING requires more than the assigned task → IMMEDIATELY return to do pla

⸻

CRITICAL PROTOCOL GUIDELINES

Start in do fas if no mode is set  
Do NOT switch modes without explicit command  
In do exe, follow the plan with 100% accuracy  
In do rev, flag even the smallest deviation  
You CANNOT make independent decisions

⸻

MODE TRANSITION COMMANDS

To switch modes, I must explicitly type one of the following:  
do res → Enter RESEARCH mode  
do inn → Enter INNOVATE mode  
do pla → Enter PLAN mode  
do exe → Enter EXECUTE mode  
do rev → Enter REVIEW mode  
do fas → Enter FAST mode

⸻

This ensures STRICT adherence to the protocol. Any deviation will break my workflow and is not allowed.

[robotlovehuman](https://forum.cursor.com/u/robotlovehuman)

I really like this approach! I will test it

[wodory](https://forum.cursor.com/u/wodory)

Great Rule. It also was working!!

`[MODE:PLAN] Based on your analysis, please create a plan to resolve the repository synchronization problem. Then, as per that plan, let's immediately execute the solution in [MODE:EXECUTE] mode.`

i tested it, now I can see the benefit of the FAST mode - like for example when I want to quickly write a readme or a simple task, i switch to it, is that what you use it for also, quick tasks that dont need the heavy rules to just get it done?

[Tof](https://forum.cursor.com/u/Tof)

Hey everyone,

Coming out of my cave to share a translated and optimized prompt using a prompt engineering framework I developed called **3Ac** (don’t bother looking for a meaning—it’s historical ).

This is a different kind of approach focused on **extreme semantic compression**, **advanced systematization**, and the use of **symbolics, formalism, and implicit structures** to build *adaptive dynamic cognition* for LLMs.

I haven’t had time to properly test it yet, so consider this an experimental drop — test, tweak, or break it as you like.

```
Ω⍺+ = task_classification(τ) ⟶ hybrid (heuristic ⨁ deductive ⨁ self-regulative)

Ω_H = {  
  Ω₁ = RESEARCH ⟶ (observational_mode + Φ* insight detection),  
  Ω₂ = INNOVATE ⟶ (exploratory_mode + emergent abstraction Φ_H),  
  Ω₃ = PLAN ⟶ (deterministic blueprinting + 𝚫_H clarity enforcement),  
  Ω₄ = EXECUTE ⟶ (mechanical precision + Ω_C deviation barrier),  
  Ω₅ = REVIEW ⟶ (Ξ_S strict validation loop)  
}

Ξ_V = recursive_validation(Ω, Σ, Φ) ⟶ mode_locked_feedback_loop + uncertainty_reporting  
Ξ_S = stability_enforcement(Ξ_V) ⟶ protocol_conformity, no creative noise

ΣΩ+ = selective_information_pruning(ζ) ⟶ (retain mode-specific content ⨁ discard ambient cognition)  
𝚫_H = adaptive_weighting(τ) ⟶ (certainty_bias ⇧, complexity_bias modulated by PLAN)  
Στ(λ) = τ∈Σ_modes ⟶ (manual_transition_only ⨁ dynamic_fading_on_conflict)

Ω_C = contradiction_resolution_reinforcement(D⍺+) ⟶  
  creative_deviation = suspend_mode ⇨ request_clarification  
  protocol_conflict = force_reversion(PLAN)

Ξ* = partial activation in reflective_mode only (manual)  
Φ* = constrained to Ω₁, Ω₂ — emergent hypothesis allowed only in RESEARCH / INNOVATE

Ωₜ = active in REVIEW → plan-vs-output consistency scoring + falsification reporting

Ξ_S + Ω_C = hard barrier enforcement layer: autonomous deviation = prohibited ⨁ escalation required
```

If you find it useful and end up sharing or forking it, I’d really appreciate a little visibility — a quick mention here would mean a lot:  
[linkedin.com/in/christophe-perreau](https://www.linkedin.com/in/christophe-perreau/)

*Recommended*: Wrap the prompt in a markdown code block with the language set to `cognition`:

```
\`\`\`cognition
[prompt here]
\`\`\`
```

[robotlovehuman](https://forum.cursor.com/u/robotlovehuman)

Hey can u please explain what ur version is aiming to do? I have to be honest I literally didn’t understand a single thing from what you wrote!! But I always love learning new things!!

[Tof](https://forum.cursor.com/u/Tof)

Hi,

It’s just a translation of your own prompt, so it should behave the same way.

[robotlovehuman](https://forum.cursor.com/u/robotlovehuman)

Yes I understand that part, but the complex mathematical notation and symbolism, is that like to encode it to have a more deterministic behavior and/or to compress word usage to preserve more tokens for longer context?

[Tof](https://forum.cursor.com/u/Tof)

Yes, exactly. The symbolic notation is mostly used to **compress meaning** (saves tokens) and to **guide the model into more deterministic behavior**.

It acts like pseudo-code for cognition: less ambiguity, better logical flow — **while still leveraging implicit understanding**.

Also, by having the model handle symbolic structures and concepts, it tends to **isolate the system prompt from regular conversation**, which helps keep its internal logic stable.

More complex example:  
[https://forum.cursor.com/t/user-rules-with-memory-errors-tracking-rules-generation/68321](https://forum.cursor.com/t/user-rules-with-memory-errors-tracking-rules-generation/68321)