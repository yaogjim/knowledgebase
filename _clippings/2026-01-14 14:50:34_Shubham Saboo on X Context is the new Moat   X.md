---
title: "Shubham Saboo on X: "Context is the new Moat " / X"
source: "https://x.com/Saboo_Shubham_/status/2011278901939683676"
author: ""
created: 2026-01-14 14:50:34
date: 2026-01-14 14:50:34
description: ""
tags: ""
---
你在用 Claude Opus 4.5，你的竞品也是。你在用 GPT-5.2，上周刚上线的初创公司也是。你在用 Gemini 3 Pro，其他做 AI 产品的也都在用。

模型正在商品化。价格在下跌。能力正在趋同。几个月前还是 SOTA 的东西，现在只要有 API 密钥的人都能使用了。

能够将自身知识外化并以结构化方式提供给代理的团队，将打造出竞争对手仅靠使用相同模型就无法复制的成果。

我看着两名开发者用相同的模型构建了几乎一模一样的代理。

有人让 Claude 构建一个带升级机制的多智能体客户支持工单处理系统。

另一个给 Claude 提供了其特定产品的背景信息：用户实际提问、品牌语气、五星好评与投诉的回应示例、需人工交接的特殊情况、座席需访问的内部工具，以及“已解决”对用户的实际含义。

第一个开发者得到了一个通用的客服机器人，声音听起来和其他任何 AI 客服代理都一样。第二个开发者得到的东西则感觉像是经过了几个月针对他们特定产品的训练。

上下文不仅仅是“提示词里的更多文字”。它是帮助模型理解你具体情况的结构化知识。

-   用户上下文。 不是用户画像。真实细节。“我们的用户是想要快速开发 AI 应用原型的开发者。他们关注可以立即运行的可用代码，而不是理论性的解释。他们会放弃任何需要超过 10 分钟设置的内容。”
    
-   领域背景。 你所在领域的具体模式和约束。“在多智能体系统中，协调智能体不应直接调用工具，而是将任务委托给专业智能体。这对可靠性为何重要的原因如下。”
    
-   历史背景。你之前尝试过什么，以及为什么没成功。"我们在2025年第二季度构建了一个类似的智能代理，采用了单一提示词方法。它失败了，因为上下文窗口填充得太快。以下是我们关于分块和摘要的经验。"
    
-   高质量的情境。 在你具体情境中，好的样子的例子。不是抽象的原则。实际的例子。“这是一个用户觉得有帮助的代理回复。这是一个让他们困惑的回复。区别就在这里。”
    
-   约束上下文。 塑造解决方案的实际限制。"我们需要这个与 API 的免费套餐兼容。延迟对于交互式使用必须保持合理。解决方案需要足够简单，以便有人能通过阅读代码理解它。"
    

这是那些存在于你脑子里的东西。在你的 GitHub 问题里。在 Slack 的线程里。在你收到的反馈里。在你从发布产品中积累的直觉里。

你做的每个项目、你记录的每个失败、你捕捉的每个用户洞察、你收集的每个例子，都增加到你的语境库中。

Team A 每个项目都从零开始。他们提示模型，得到通用输出，花数小时修正调整，然后就继续。学到的东西要么留在脑子里，要么完全消失。

B 组维护上下文文档。每个项目结束后，他们会更新学到的内容：哪些有效，哪些无效。新的用户洞察、好产出的新例子，以及需要留意的新边缘案例。

六个月后，A 组仍然得到千篇一律的产出，并且在修改上花费数小时。

B 组成员第一天的成果就比 A 组一周迭代后的成果更好。

这就是飞轮。 良好的上下文→更好的产出→了解哪些上下文起了关键作用→改进的上下文文档→重复。

[

![Image](https://pbs.twimg.com/media/G-j9lMCbQAAyPl4?format=jpg&name=medium)



](https://x.com/Saboo_Shubham_/article/2011278901939683676/media/2011136048949313536)

我维护着, 一个包含 100 多个 AI 代理和检索增强生成(RAG)实现的开源集合。当我构建新代理时，我从不从头开始。

```
Target user: Developers who want to prototype AI agents fast. 
They'll clone, run, and decide in 10 minutes if it's useful.
They won't read a wall of text. They'll scan the README for a quickstart.

Setup requirements:
- Maximum 3 environment variables (API keys only)
- Single requirements.txt, no complex dependency chains
- "pip install + run" in under 5 minutes or they bounce

Tech stack:
- Python only
- Streamlit for UI (fast to build, easy to understand)
- OpenAI/Anthropic/Google AI SDKs directly, minimal abstraction layers

What gets stars:
- Solves a real problem people actually have (not a toy demo)
- Code is readable without extensive comments
- Easy to extend or modify for their own use case
- Good README with a GIF or screenshot showing it working

What doesn't land:
- "Hello world" level demos (too basic)
- Overly complex architectures for simple problems
- Agents that require 10+ minutes of config before first run

Common failure patterns to avoid:
- Context window overflow on long conversations
- Tool call loops where agent gets stuck
- Unclear error messages when API calls fail
- No graceful handling of rate limits

Agent patterns that work:
- Single-purpose agents that do one thing well
- Multi-agent systems with clear role separation
- Coordinator pattern for complex workflows
- Human-in-the-loop for high-stakes decisions
```

当我打开 Claude 代码（）或者 Antigravity（）来构建一个新代理时，这个上下文会先传入。这个代理已经知道这个仓库里“好”是什么样的，该用什么模式，该避免什么错误。

那才是护城河。不是模型。是积累的上下文，让模型能更好地适用于我的特定情况。

最好的上下文系统是无形的。上下文就一直存在那里，每次都随时可用。

现在每一个主要的 AI 编码工具都支持持久化上下文文件。你只需创建一次，将它们放入你的项目中，它们就会自动加载到每一次对话里。

[

![Image](https://pbs.twimg.com/media/G-j9qhRbUAAc6zi?format=jpg&name=medium)



](https://x.com/Saboo_Shubham_/article/2011278901939683676/media/2011136140548722688)

-   光标: .光标/规则
    

-   帆板：.帆板规则
    

-   Claude 项目： 上传作为项目知识
    

我把代理模式、质量标准和失败模式都保存在这些文件里。每次会话开始时，代理已经理解了我的世界。

把你知道的内容以文件形式记录到你的代码仓库中。不要再重复解释你的技术栈，不要再重复描述你的模式，不要再纠正同样的错误。

今天： 写一份背景文档。你的用户到底是谁？好的样子是什么样的？你试过哪些失败的尝试？不需要完美。就开始吧。

每个项目结束后： 你学到了什么？什么让你感到惊讶？你会有什么不同的做法？把这些写下来。

进行中： 痴迷地收集示例。好的输出、坏的输出、边缘情况。示例是你能提供的最高杠杆的上下文。

让它自动化： 添加一个 或者 到你的项目中。它会自动加载。你再也不用考虑它了。

提示会变得更容易。模型会用更少的文字更好地理解你。

将上下文视为头等工程问题的人，会更快地构建出更好的东西。

不直接告诉代理做什么，而是帮助他们理解为什么这很重要。