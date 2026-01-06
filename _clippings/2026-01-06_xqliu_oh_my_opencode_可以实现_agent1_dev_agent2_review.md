---
title: "2026-01-06_xqliu_oh_my_opencode_可以实现_agent1_dev_agent2_review"
source: "https://x.com/xqliu/status/2007963650758512678"
author:
  - "[[@xqliu]]"
published: 2026-01-06
created: 2026-01-06
description:
tags:
  - "x"
  - "@xqliu"
  - "agent"
  - "https"
---

# oh-my-opencode 可以实现 agent1 dev - agent2 review -

**Larry & Leo Bro - Eagle of Full Stack** @xqliu 2026-01-04

oh-my-opencode 可以实现 agent1 dev -> agent2 review -> agent1 dev -> agent2 review -> agent1 dev -> agent2 review 的 loop, 一直到 review agent 没有任何修改要求!!

下面是我的随手 prompt:

Do the dev and after you finish, call the Oracle sub agent to reveiw your change, loop until no change request / logic error from Oracle sub agent, can you do that?

> 2026-01-04
> 
> 发现 oh-my-opencode 其实是可以做多 agent 会诊的! 我用了下面的 prompt, 居然就工作了
> 
> 你让 codex 和 gemini 的 sub agent 用 @.claude/commands/20-code-review.md 的7轮审查标准审查了吗? 审查结果你考虑并修复/优化了吗?
> 
> opencode 和 oh-my-opencode 的链接见回复 x.com/xqliu/status/2…
> 
> ![Image](https://pbs.twimg.com/media/G9236HNaIAARXZG?format=png&name=large)

* * *

**Vincent** @win1688888888 [2026-01-05](https://x.com/win1688888888/status/2008018102458659254)

这种 Loop 最大的隐患在于 Context Window（上下文窗口）的污染。 随着 Loop 次数增加，对话历史会堆积大量的“错误代码 -> 错误修复 -> 再次错误”的垃圾信息。这会导致 Agent 在第 4 或 第 5 轮时，注意力被之前的错误尝试带偏，智商显著下降。

* * *

**Larry & Leo Bro - Eagle of Full Stack** @xqliu [2026-01-05](https://x.com/xqliu/status/2008071495818612811)

确实是个风险不过昨天睡觉前让 ai loop，发现三轮 修复 - review 就搞定了

* * *

**justin0798** @justin\_newbee [2026-01-05](https://x.com/justin_newbee/status/2008104352448450989)

可以看看pi的作者的说法，subagent的上下文会污染主agent，上下文工程还是自己做，收集全一口气给最好，我也是这样实践的，虽然慢，但是慢就是快

* * *

**Larry & Leo Bro - Eagle of Full Stack** @xqliu [2026-01-05](https://x.com/xqliu/status/2008109213869035797)

正在尝试理解你这段话😂

* * *

**vewin** @lawgpts [2026-01-05](https://x.com/lawgpts/status/2008189381438513158)

opencode有一个问题我今天没找的解决方案，预置的搜索mcp无法联网，我自己添加的远程mcp也无法联网，貌似运行在一个无法联网的沙盒里面，我让opencode读他自己的源码去找答案，他自己设置.env里面的http\_proxy参数测试也不行。实际我是能上各种外网的。

* * *

**Larry & Leo Bro - Eagle of Full Stack** @xqliu [2026-01-05](https://x.com/xqliu/status/2008189634623557953)

奇怪,我用的 Claude 模型好像一直可以上网啊

* * *

**Kilo** @kilocode

Kilo offers a single agent that can explain, architect, plan, code, test, debug, review, and deploy.