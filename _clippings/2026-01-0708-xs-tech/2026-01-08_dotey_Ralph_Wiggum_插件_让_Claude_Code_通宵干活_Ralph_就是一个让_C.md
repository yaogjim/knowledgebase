---
title: "2026-01-08_dotey_Ralph_Wiggum_插件_让_Claude_Code_通宵干活_Ralph_就是一个让_C"
source: "https://x.com/dotey/status/2007197068394164613"
author:
  - "[[@dotey]]"
published: 2026-01-08
created: 2026-01-08
description:
tags:
  - "x"
  - "@dotey"
  - "https"
  - "claude"
---

# Ralph Wiggum 插件：让 Claude Code “通宵干活” Ralph 就是一个让 C

**宝玉** @dotey 2025-12-27

Ralph Wiggum 插件：让 Claude Code “通宵干活”

Ralph 就是一个让 Claude 自己跟自己对话的循环——你下班回家，它替你加班，醒来代码写好了。

核心原理

传统用法：你给 Claude 一个任务 → Claude 完成 → 退出 → 你再手动启动下一轮。

Ralph 用法：

\`\`\`bash

/ralph-loop "你的任务描述" --completion-promise "DONE" --max-iterations 50

\`\`\`

Claude 会：

1\. 执行任务

2\. 尝试退出时被 Stop hook 拦截

3\. 自动重新读取同一个 prompt

4\. 看到自己之前写的代码/测试结果

5\. 继续改进，直到输出 “DONE” 或达到迭代上限

每次迭代 prompt 不变，但文件和 git 历史在变——Claude 通过读取自己的“作品”实现自我进化。

最适合的场景

✅ TDD 开发：写测试 → 跑失败 → 改代码 → 重复直到全绿

✅ Greenfield 项目：定义好需求，过夜执行

✅ 有自动验证的任务：测试、Lint、类型检查能告诉它对不对

❌ 需要人类判断的设计决策

❌ 没有明确成功标准的任务

Prompt 写法要点：

必须有：明确的完成条件 + 完成信号词

示例：

\`\`\`markdown

构建一个 Todo REST API

完成标准：

\- CRUD 全部可用

\- 输入校验完备

\- 测试覆盖率 > 80%

完成后输出：<promise>COMPLETE</promise>

\`\`\`

真实战绩

\- Y Combinator Hackathon：一夜生成 6 个仓库

\- 某项目：$50k 合同，API 成本仅 $297

安全机制

始终设置 \`--max-iterations\` 防止无限循环：

\`\`\`bash

/ralph-loop “任务” --max-iterations 30 --completion-promise “DONE”

\`\`\`

📎 插件地址：https://github.com/anthropics/claude-plugins-official/tree/main/plugins/ralph-wiggum…

> 2025-12-27
> 
> 如果你想实现的需求相对确定/可验证，并且你不在意 token 消耗或是订阅制，那么可以在 Claude Code 中使用这个官方插件 Ralph Wiggum。
> 
> 它通过 Stop hook，在每次 Claude 要停下的时候，再次驱动它干活&验证，直到你的需求被解决
> 
> https://github.com/anthropics/claude-plugins-official/blob/main/plugins%2Fralph-wiggum%2FREADME.md…
> 
> ![Image](https://pbs.twimg.com/media/G9r_B73WAAALV7D?format=jpg&name=large)

* * *

**宝玉** @dotey [2026-01-03](https://x.com/dotey/status/2007516557254197562)

Best practice for reviewing AI code

> 2026-01-03
> 
> Code Review in the AI Era: Why Writing It Twice Is Actually Faster
> 
> If you've been coding for a few years, you've probably lived through this nightmare: you finish the first version, finally get it running, and then realize you misunderstood half the requirements, hit three x.com/bcherny/status…
> 
> ![Image](https://pbs.twimg.com/media/G9wfSQbWEAAVJkN?format=jpg&name=large)

* * *

**宝玉** @dotey [2026-01-07](https://x.com/dotey/status/2008937613420593208)

改名了

> 2026-01-07
> 
> 名字改成ralph-loop了，地址也更新了：
> 
> https://github.com/anthropics/claude-plugins-official/tree/main/plugins/ralph-loop…

* * *

**geoff** @GeoffreyHuntley [2026-01-03](https://x.com/GeoffreyHuntley/status/2007357605438685684)

see https://ghuntley.com/ralph (and the video in that post from yesterday) if you want better outcomes than the CC plugin.

cc plugin isn’t it

* * *

**Jintao Zhang 张晋涛** @zhangjintao9020 [2026-01-03](https://x.com/zhangjintao9020/status/2007242285411643894)

🤗 感谢

* * *

**Leo Xiang** @leeoxiang [2026-01-03](https://x.com/leeoxiang/status/2007290998238695668)

这个还是要慎重用， stop hook 的时候有点问题，我有个任务一直没停。

* * *

**耳朵** @RookieRicardoR [2026-01-03](https://x.com/RookieRicardoR/status/2007453067177013538)

最近在用的 opencode 内置了类似功能

> 2026-01-03
> 
> 最近一直在使用一个绝对被低估的开源宝藏组合：OpenCode + oh-my-opencode。
> 
> 如果你觉得 Claude Code 已经是体验天花板，那这个组合可能会刷新你的认知。
> 
> 它不仅免费开源，更汇聚了 Claude Code 和 AmpCode 的所有优势，甚至在某些方面完成了超越。
> 
> 🔥 什么是
> 
> ![Image](https://pbs.twimg.com/media/G9vlc5fasAMdnsv?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G9viyk9asAIzjIt?format=jpg&name=large)