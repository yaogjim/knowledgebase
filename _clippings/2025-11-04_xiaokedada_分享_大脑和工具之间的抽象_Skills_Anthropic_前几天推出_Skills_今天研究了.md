---
title: "2025-11-04_xiaokedada_分享_大脑和工具之间的抽象_Skills_Anthropic_前几天推出_Skills_今天研究了"
source: "https://x.com/xiaokedada/status/1981326177836159224"
author:
  - "[[@xiaokedada]]"
published: 2025-11-04
created: 2025-11-04
description:
tags:
  - "#分享"
  - "@xiaokedada"
  - "@axtrur"
  - "@kokodayoxie"
  - "agent"
  - "skills"
  - "https"
  - "mcp"
  - "//x"
  - "x.com"
---

# #分享 大脑和工具之间的抽象：Skills Anthropic 前几天推出 Skills，今天研究了

**nazha** @xiaokedada [2025-10-23](https://x.com/xiaokedada/status/1981326177836159224)

#分享 大脑和工具之间的抽象：Skills

Anthropic 前几天推出 Skills，今天研究了下，第一眼就让我感觉怎么跟 Cursor Rules 的设计一模一样：标题、描述和被“卸载”到文件系统的详细内容。

接着仔细看了 Anthropic 提供的 Skills 示例https://github.com/anthropics/skills…，强烈觉得这恐怕又是 Anthropic 公司内部 dogfooding 的结果。

我的理解是：Skills 描述的对人类技能的抽象。

\## MCP 和 Skills

\## MCP 与技能

一般，我们把 MCP 定义为 Agent 的 \*\*工具能力\*\*，能够访问外部系统、执行相关流程和获取关键信息。当然，MCP 也可以来做跟 Skills 相关的事情，它可以很狭义，也可以很广义，这主要看在具体实践中的定义。

技能是更高纬度的，通过学习、训练或工作经验获得的能力。之前主要是依赖 LLMs 的内在的通用能力，而 Skills 有点类似于强化学习路径，让 LLM 有一个可参考的模板。

简单理解，MCP 不能跟 Skills 混为一谈：MCP 定位在工具，Skills 定位在技能。

在 Anthropic 发布的这张图也并没有表达 Skills 替换 MCP 的意思，工具应该是更原子化的东西。而工具 = MCP + 命令行 + 自定义脚本 + ...

\## Skills 是 Anthropic 让 Claude Code/Claude Web 向迈向通用 Agent 做的努力

Anthropic 在 Claude Code 中也集成了 Skills，显然是看到了 Claude Code 在通用 Agent 方向的潜力，而不仅仅是写代码（拜托，先换个名字，不要叫 Claude Code 了）。

\## 再来看 Skills 的设计

第一个感觉就是对普通人来说真的简单。你要实现一个 MCP 工具，非编程科班出身的还真有点难度，理解 MCP 的各个概念就能让人退而却步。而 Skill 的设计呢，无非就是写文档、讲明白事情就可以。

为了实现在 Skills 执行脚本和代码，Anthropic 就必须提供一个虚拟执行环境，将部分困难转交给容器执行环境（这也许是下一个技术热点）。当然，并不是批评 MCP，MCP在设计的时候，也许并没有这个共识存在。

\## 给我们在设计 Agent 架构时的启发

技能的部分，在之前的架构设计中，有一部分是会演变成子智能体，技能详情变成了子智能体的系统提示，即 Agent as Tool / Agent as Skill 的设计。若在智能体和工具之间又加了一个技能层，给我们在设计 Agent 架构的时候，就要思考得更多了，第一个问题就是是否需要额外引入一个 Agent，如果这个 Agent 的能力能够被 Skill 承载？

对于多智能体的架构，目前我看到的一些产品，比如 Manus、 Claude Code 都是很谨慎的。Skills 给我们在设计 Agent 的时候提供另一条思路：有技能的智能体。

\## 了解 Skill, 我的建议

先从 https://github.com/anthropics/skills… 的每个例子开始，对技能是什么有个初步的概念。再看下 https://anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills… 这篇工程文章，深入了解 Skills 的设计。

最后，我表示我很喜欢 Skill。哪怕 Cursor Rules 出来很久，这也是我也没取思考过的工程设计。也许像浩瀚天空的一颗星，指明了一些方向。

![Diagram titled Agent plus skills plus Virtual Machine shows agent configuration core prompt connected to agent virtual machine, with deployed skills including YAML files, PDF, and Markdown documents, linked to MCP servers and file system contents like requirements.txt and data sources.](https://pbs.twimg.com/media/G38UeVVWQAALpX8?format=jpg&name=large) ![Diagram titled Agent plus skills plus Virtual Machine shows agent configuration core prompt connected to agent virtual machine, with deployed skills including YAML files, PDF, and Markdown documents, linked to MCP servers and file system contents like requirements.txt and data sources.](https://pbs.twimg.com/media/G38U6YbXIAAtXH2?format=jpg&name=large)

* * *

**axtrur** @axtrur [2025-10-25](https://x.com/axtrur/status/1982132989787079026)

看了anthropic家的各种产品会发现他们的一个共识：human like，一切设计采用主动性的use主动性的pick，甚至是coding agent中的文件mention之后他们都不愿意一起把文件内容组装到上下文而是让模型自己read file，同样的skill也一样，use skill when...

* * *

**nazha** @xiaokedada [2025-10-26](https://x.com/xiaokedada/status/1982446794551517289)

确实是这样的~

* * *

**Kokodayoxie** @kokodayoxie [2025-10-23](https://x.com/kokodayoxie/status/1981386752498766179)

不share context的SubAgent可以避免污染Main Agent的context，但skills会污染上下文。

* * *

**nazha** @xiaokedada [2025-10-24](https://x.com/xiaokedada/status/1981542722399064481)

是的，这里间的编排很复杂~ Skill 我觉得也不是来替代 SubAgent，而是给共享上下文的 Agent 的 alternative? 在实际工程里，反而要清晰定义 Agent / Skill / Tools 的边界问题，激进引入 Multi-Agent 可能不一定对架构有利

* * *

**坤sir** @kun70706 [2025-10-23](https://x.com/kun70706/status/1981337839192461822)

未来交付的是作为专家的经验，在某个领域的经验集。真的是加载技能包

* * *

**nazha** @xiaokedada [2025-10-24](https://x.com/xiaokedada/status/1981543895281652148)

也有可能技能内化成 LLMs 底层能力。AGI 刚兴起那会，result = LLM(input)，以为只要描述好 input，LLM 能给我解决好一切（或者一个中等偏上的结果）。现在发现还没到这个地步，LLMs 还不够智能，为了得到相对更好、更稳定的结果，Skills 是工程上应对 LLMs