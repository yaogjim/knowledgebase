---
title: "Andrej Karpathy 分享 Vibe Coding 技巧"
source: "https://x.com/sagacity/status/1961980381009531089"
author:
  - "[[@sagacity]]"
published: 2025-09-02
created: 2025-09-02
description:
tags:
  - "@sagacity #VibeCoding #AI编码 #程序员"
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
**池建强** @sagacity [2025-08-31](https://x.com/sagacity/status/1961980381009531089)

我这半年看过最好的 Vibe Coding 技巧  
  
上周 OpenAI 的创始成员 Andrej Karpathy 在 X 上发了一条长长的推文，继续阐述自己在 Vibe Coding 方面的实践。  
  
这次他开门见山的表示，不要幻想有一个万能的 AI 工具能解决所有编程问题，更可行的做法是建立一个三层结构，让不同的工具在不同场景各司其职，像接力赛一样完成开发任务。  
  
1  
  
在 Karpathy 的日常开发中，大约四分之三的时间最依赖的依然是 Cursor 的自动补全。这里面有一个细节很有意思：Karpathy 并不是依赖自然语言提示去驱动 AI 写代码，而是更习惯在代码里写注释、写片段，用“演示”的方式告诉模型你想要什么。这种方式带宽更高、意图更明确，也避免了上下文缺失造成的偏差。不过他也坦言，有时候 Cursor 太“热情”，会补全一大段并不需要的内容，打断思路。所以他会频繁地开关这个功能，就像和一个“话痨搭档”保持距离。  
  
2  
  
当遇到更大块的功能需求，或者不太熟悉的领域，Karpathy 就会把舞台交给 Claude Code 或 Codex。这类工具更适合快速生成一大段可用的代码实现，尤其是在写 Rust、SQL 这样的语言时，可以立刻把复杂的逻辑搭出来，调试和可视化也能很快跑通。这次他提到一个新词——“后代码稀缺时代”。在这个时代，生成和删除代码都变得轻而易举，代码从来不再是稀缺资源，实验和探索的成本被大幅降低。你想尝试一个新思路？直接让 AI 写一版，跑不通就删掉，重新来过。  
  
不过，AI 写出来的代码质量往往“不够优雅”。Karpathy 给的例子很具体：喜欢堆砌复杂的抽象、滥用 try/catch、写得又长又冗余、缺乏工程品味。这种时候，他需要手动清理，像给新人代码做 code review 一样，把那些不符合自己风格的部分剔除掉。更有意思的是，他还尝试让 Claude 在写代码的同时顺便“上课”——解释为什么这么写，或者帮忙做超参数调优，但这根本不起作用——它真的想写代码，而不是解释任何东西。这从侧面也说明，AI 现在很擅长写东西，但讲解和教学还远没到位。  
  
3  
  
当自动补全和 Claude 都不管用的时候，Karpathy 的“终极武器”是 GPT-5 Pro。他的做法很简单：把一整个疑难问题丢进去，让模型“沉思十分钟”，然后再看答案。很多时候，GPT-5 Pro 能给出人工难以发现的 bug 线索，或者在抽象优化和文献综述中提供独到见解。换句话说，这是他的“救火队长”。  
  
这种三层结构的组合，让 Karpathy 的工作流更像一套生态。轻量需求靠自动补全解决，大规模生成交给 Claude 或 Codex，难题交给 GPT-5 Pro。相比依赖单一工具的思路，这更接近真实的开发场景，也更符合 AI 发展的现状。  
  
在这条推文里，他还谈到“后代码稀缺时代”的焦虑。代码不再稀缺，但人的精力依旧有限。工具更新太快，总让人担心自己是不是落伍了，会不会错过了最前沿的可能性。他把这种状态称为“周日胡思乱想”。  
  
这正是当下许多开发者共同的心态。我们既兴奋于生产力的突飞猛进，又害怕自己无法驾驭这匹充满野性的骏马。  
  
对普通开发者和使用 Vibe Coding 的普通用户来说，这里面有几个启示：  
  
首先，要放弃寻找完美工具的幻想，建立自己的工具组合。不同的任务难度需要不同的 AI，像调动一个虚拟团队一样，谁擅长什么就用谁。  
  
其次，要学会用“代码里的意图”而不是“自然语言的空话”去驱动模型，把注释和片段当作沟通语言，这样效率更高。  
  
最后也不要忽视清理的过程。AI 生成的东西往往像半成品，需要你用工程师的直觉和审美去打磨。  
  
写到这儿我想起一句老话：工欲善其事，必先利其器。只是到了今天，器不再是一把锤子、一个 IDE，而是多个快速迭代的 AI 工具。它们不再是静止的工具，而更像一群性格迥异的搭档。我们需要学会和它们合作，学会在噪音里保持判断，学会在洪流中找到自己的节奏。

![A screenshot of a tweet from Andrej Karpathy on X, displaying text about coding workflows and AI tools. The text includes mentions of Cursor, Claude Code, Codex, and GPT-5 Pro. An X watermark is visible in the top-right corner.](https://pbs.twimg.com/media/GzpawM6akAAUIr0?format=jpg&name=large)

---