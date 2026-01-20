---
title: "2026-01-20_jolestar_从_MCP_到_SKILL_关于_Agent_扩展机制的思考_去年_MCP_爆火_大家一度有种感觉"
source: "https://x.com/jolestar/status/2011461813767155828"
author:
  - "[[@jolestar]]"
published: 2026-01-20
created: 2026-01-20
description:
tags:
  - "x"
  - "@jolestar"
  - "https"
  - "mcp"
---

# 从 MCP 到 SKILL：关于 Agent 扩展机制的思考 去年 MCP 爆火，大家一度有种感觉：

**jolestar** @jolestar [2026-01-14](https://x.com/jolestar/status/2011461813767155828)

从 MCP 到 SKILL：关于 Agent 扩展机制的思考

去年 MCP 爆火，大家一度有种感觉：只要把工具都接进来，AI Agent 就会“活”过来，像一个长了手脚的人，什么都能干。

如果把 LLM 看作大脑（智力引擎），tool call / function call 就像让它能指挥四肢：模型填参数，代码去执行，再把结果喂回去继续推理。

MCP（Model Context Protocol）把这套机制做成了“标准插头”：以前各家服务各自一套 SDK + API，你要给 Agent 封装工具，就得处理语言、依赖、鉴权、返回格式，复杂度会指数上升；MCP 的价值是把“接入”这件事工程化、标准化。

所以当时最乐观的推论很自然：只要 MCP 工具够多，Agent 就有无限多的手脚，什么都能干了。

但很快大家就撞墙了。

第一堵墙：容量瓶颈（上下文预算）

工具的定义本身要进入系统 prompt 或等价的工具上下文；工具越多，占用越多，留给“干活”的空间越少。于是你会看到一些很现实的限制：某些 AI coding 工具最多支持配置 100 个 tools，而一个 GitHub MCP 可能就带 50 多个。你想把世界都接进来，但大脑的工作台面就这么大。

第二堵墙：任务闭环瓶颈（组合性）

很多 MCP 的调用结果会被直接回填上下文。短结果当然舒服，长结果就会触发两个问题：要么上下文爆炸，要么被截断丢尾巴。

我在做 holon 的时候就踩过这个坑：让 AI 去处理 PR 的 review comments，如果 comments 一多，直接回填上下文就会被截断，结果总是漏修。 后来反而退回到更“原始”的 GitHub CLI 会更稳——AI 先用 \`gh\` 把评论拉下来写成文件，再用 \`grep\`、\`jq\` 或简单脚本去筛选、聚合，只把必要的摘要喂回上下文继续推理。

这个过程让我意识到一个很基础、但之前容易被忽略的问题：上下文更适合承载决策信息，而不是当作数据存放层。 文件、数据库、对象存储这些外部介质，天然支持分页、寻址和重复访问，更适合用来承接中间状态。当任务需要反复回看、局部筛选或增量处理时，把数据外部化，往往比把全文塞回上下文要可靠得多。

从这个角度看，MCP 暴露出来的瓶颈，并不完全在协议本身，而在于我们常常下意识地把它用成了“往上下文里塞数据”的通道，而不是“把能力接入到工作流里”的接口。

也正是在这样的背景下，SKILL 开始受到关注。

如果 SKILL 只是纯文本，它更像分层 prompt 的组织方式；但当它和命令行工具、脚本结合起来，它就不只是“提示词技巧”，而是一种场景化的工作流封装：同一类任务的步骤、产物、工具链、失败重试方式、输出格式，都被聚合在一起。普通用户可能搞不清 MCP 是干啥的，但他能理解“这个技能帮我把评论整理出来并逐条修复”。

从实现上看，这有点像“以前用胶水代码粘合工具”，现在用“自然语言 + LLM + Bash/脚本”来粘合工具。并且这种范式正在让 Prompt Engineering 转向 Skill Engineering。灵活性确实强了，但相比标准化的扩展，SKILL 还有许多未解决的问题。

安全性是第一个难题。Bash + 脚本这些工具主要是开发者用，大家多少有点风险识别能力；但当 Agent + SKILL 普及到普通用户后，安全问题会更严重。到那时候，“靠提醒小心”是没用的，Agent 环境得提供更强的沙箱隔离能力。

标准化是第二个难题。SKILL 天然是按场景聚合的，但也因此更依赖运行环境：目录结构怎么约定？中间产物放哪？状态如何保存与复用？如何跨端复制这套模式？如果这些问题不解决，SKILL 的能力很难跨环境复用，更像是绑定在某个系统里的私有插件。

说回 MCP，我并不觉得有了 SKILL，MCP 就没意义了。恰恰相反，我更倾向于一种分工：

MCP 解决“连接标准化”，SKILL 解决“工作流编排与状态外部化”。前者让能力能规模化接入，后者让任务能稳定闭环。

MCP 不一定要“由 Agent 直接调用并回填上下文”，它完全可以被 SKILL 里的脚本调用，让结果先落地为可寻址对象（文件/句柄/资源），再把摘要与索引回填给模型。这样上下文就回到它最擅长的位置：做决策、做推理、做取舍，而不是当缓存。

MCP、SKILL 仍处在早期阶段，只是 Agent 插件机制演化中的不同形态。当 Agent 开始承担复杂任务时，真正重要的已不再是能力本身，而是上下文、状态与执行边界如何被拆分和安放。

* * *

**AlexZ** @blackanger [2026-01-14](https://x.com/blackanger/status/2011475668849344658)

用不着对比，优先用 SKILL，如果不行，再考虑 MCP。

* * *

**rming** @rming8803 [2026-01-14](https://x.com/rming8803/status/2011497781475876960)

老师，skill是不是也存在理论上限，太多了模型消化不过来，或者描述冲突导致理解不正确？

* * *

**jolestar** @jolestar [2026-01-14](https://x.com/jolestar/status/2011577943169122708)

会的

* * *

**Weilan| ボッ Bird** @ohouhou717 [2026-01-14](https://x.com/ohouhou717/status/2011531732638740800)

讲得通透，思路清晰

* * *

**Yijun Xiao** @emptycommit [2026-01-15](https://x.com/emptycommit/status/2011829095701889381)

这是我最近看到对 MCP 和 Skill 最有实践深度的内容了。最近正在做一个带 OAuth 认证的 Logto MCP Server，踩了不少坑，从实现一个业务型 MCP Server（非纯工具型）的视角补充一些看法：

关于容量瓶颈

这里一个需要权衡的点是 Tools 的设计要节制。我看到很多 MCP Server 相当于把 API 1:1 映射成

* * *

**轩帅** @MarshalXuan [2026-01-15](https://x.com/MarshalXuan/status/2011751637271134597)

清晰透彻易懂，👍🏻Skills 提供模块化和可扩展的能力，形成复用、懒加载节省 Token，体验大幅提升。如今形成组组合拳：

Prompt + MCP|Tools + CLAUDE|AGENTS(rules) + Skills

加上 Cursor Hooks，将效果又抬升一个层次；未来将如何演变，拭目以待👁。

> 2026-01-15
> 
> Prompt =>
> 
> Prompt + MCP|Tools =>
> 
> Prompt + MCP|Tools + CLAUDE|http://AGENTS.md =>
> 
> Prompt + MCP|Tools + CLAUDE|http://AGENTS.md + Skills =>
> 
> Prompt + MCP|Tools + CLAUDE|http://AGENTS.md + Skills + X
> 
> X = Hooks 👉🏻 https://cursor.com/cn/docs/agent/hooks…
> 
> 提示 =>
> 
> 提示词 + MCP|工具 =>
> 
> 提示词 + MCP|工具 + Claude|http://AGENTS.md =>
> 
> 提示词 + MCP|工具 + Claude|http://AGENTS.md + 技能 =>
> 
> 提示词 + MCP|工具 + Claude|http://AGENTS.md + 技能 + X
> 
> X = 钩子 https://cursor.com/cn/docs/agent/hooks…

* * *

**Rain** @jiangydev [2026-01-14](https://x.com/jiangydev/status/2011471662386905378)

王老师，我写了一篇文章，结合代码评审实例，把command/mcp/skill 这些都串起来的文章，帮指点指点🤣

> 2026-01-09
> 
> ![Article cover image](https://pbs.twimg.com/media/G-PMPMNasAAtqt2?format=jpg&name=large)

* * *

**Chou** @crosg2026 [2026-01-15](https://x.com/crosg2026/status/2011606603993432510)

@GillianR2026 这个是我看过的讲skills得最棒的，比公众号上那些《一文讲透》要本质多了

* * *

**Alan YW** @alan\_ywang [2026-01-14](https://x.com/alan_ywang/status/2011476716338790724)

看好 holon

* * *

**Hero Wars** @HeroWarsWeb

Full Blown RPG in your browser: No Downloads - Just Click and Go!

全功能的角色扮演游戏在你的浏览器中：无需下载 - 点击即玩！

* * *

**John** @YinganL1927 [2026-01-14](https://x.com/YinganL1927/status/2011523073993032122)

👍👍