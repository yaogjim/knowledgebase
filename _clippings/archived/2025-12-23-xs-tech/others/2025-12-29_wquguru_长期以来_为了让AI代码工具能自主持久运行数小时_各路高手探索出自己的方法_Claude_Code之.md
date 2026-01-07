---
title: "2025-12-29_wquguru_长期以来_为了让AI代码工具能自主持久运行数小时_各路高手探索出自己的方法_Claude_Code之"
source: "https://x.com/wquguru/status/2005112033239249128"
author:
  - "[[@wquguru]]"
published: 2025-12-29
created: 2025-12-29
description:
tags:
  - "x"
  - "@wquguru"
  - "https"
  - "2025-12-28"
---

# 长期以来，为了让AI代码工具能自主持久运行数小时，各路高手探索出自己的方法，Claude Code之

**WquGuru** @wquguru 2025-12-27

长期以来，为了让AI代码工具能自主持久运行数小时，各路高手探索出自己的方法，Claude Code之父Boris在最新的推文中提及了11月20日刚开发的官方插件ralph-wiggum

这个插件的核心原理利用Claude Code的Stop Hook机制：当Claude认为任务完成并试图退出会话时，hook会拦截退出，检查是否真正达成预设成功条件。如果未达成，它会自动递增迭代计数，并将相同的原始任务提示重新注入给Claude

Claude基于上轮留下的文件变更、git历史和测试失败，继续下一轮自纠错迭代。整个过程在单个会话内循环，无需外部脚本，状态通过本地文件持久化

使用方式简单：运行一次/ralph-loop "你的任务描述" --completion-promise "完成信号文本" --max-iterations N（强烈推荐设置上限防无限循环），当Claude输出<promise>完成信号</promise>时，循环结束

这个方法适合的场景：有清晰客观标准（如测试全通过）的任务，比如TDD开发、重构代码、构建完整功能。Reddit中应用案例有一夜生成仓库、全自主完成5w美金的高价值合同

不过也有局限性：不适合主观或模糊任务（易陷入低效循环）；token消耗高；多会话时hook可能意外接管（建议用git worktrees隔离）；依赖优秀的提示工程（如果不熟悉，可以看看这个A社官方的提示工程最佳实践交互课程https://12factor.me/zh/prompt-engineering…）

这个插件标志着AI代理从分钟级到天级自主的跃进，值得每位Claude Code用户尝试

链接：https://github.com/anthropics/claude-plugins-official/tree/main/plugins/ralph-wiggum…

> 2025-12-27
> 
> When I created Claude Code as a side project back in September 2024, I had no idea it would grow to be what it is today. It is humbling to see how Claude Code has become a core dev tool for so many engineers, how enthusiastic the community is, and how people are using it for all
> 
> 当我在 2024 年 9 月将 Claude 代码作为副业项目创建时，根本没想到它会发展到如今的规模。看到 Claude 代码成为这么多工程师的核心开发工具，社区的热情有多高，以及人们如何用它来做各种
> 
> ![Image](https://pbs.twimg.com/media/G9LGAh3WkAAbnBJ?format=png&name=large)

* * *

**WquGuru** @wquguru [2025-12-28](https://x.com/wquguru/status/2005122756720165009)

ralph-wiggum这名字听着就挺逗的，其实来自辛普森一家里的Ralph Wiggum——老是搞砸但从来不放弃

插件的核心哲学是“迭代胜过完美”（iteration over perfection），失败不算完蛋，只是下次改进的素材；只要循环不停，Claude就会盯着上次的错误，一点点修到成功为止

名字最早出自社区大神Geoffrey

![Image](https://pbs.twimg.com/media/G9OggyOaAAAYjHX?format=jpg&name=large)

* * *

**码上盈｜AI陪你做生意** @InnaLyceyum [2025-12-28](https://x.com/InnaLyceyum/status/2005221624166133814)

博主提到的用 git worktrees 隔离和设置上限，这些都是老江湖的经验之谈。AI 代理跑起来确实快，但要是没这些隔离措施，万一逻辑跑偏了，可能把你本地的开发环境也给搅和乱了。这种把 AI 关在笼子里让它可劲儿折腾的思路，才是真正让它落地的高效方法。

* * *

**Leesanity** @Macro\_Zyaire [2025-12-28](https://x.com/Macro_Zyaire/status/2005135298024669365)

看起来很适合工程性项目，但是做研究好像就没法如此了

* * *

**云比云** @yunbiyun [2025-12-28](https://x.com/yunbiyun/status/2005195833973879086)

回头抽时间试一下，这个也许可以很考验国产大模型的进步程度

* * *

**黑眼圈** @i\_m\_m\_ [2025-12-28](https://x.com/i_m_m_/status/2005136582752534789)

太酷了，Claude Code

太酷了，Claude 代码