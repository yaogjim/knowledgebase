---
title: "2025-12-26_yan5xu_skill_subagent这些概念最后都是用prompt来组织_就像工具的说明书_而大模型有一个所"
source: "https://x.com/yan5xu/status/2003618544735649947"
author:
  - "[[@yan5xu]]"
published: 2025-12-26
created: 2025-12-26
description:
tags:
  - "x"
  - "@yan5xu"
  - "https"
  - "agent"
---

# skill、subagent这些概念最后都是用prompt来组织，就像工具的说明书 而大模型有一个所

**宝玉** @dotey [2025-12-23](https://x.com/dotey/status/2003530767574687854)

skill、subagent这些概念最后都是用prompt来组织，就像工具的说明书

而大模型有一个所拥有的工具的清单，自己可以根据场景来决定什么时候触发skill、agent、MCP的prompt

> 2025-12-23
> 
> 做工具的人沒想明白
> 
> 大部分 Agent 概念最後都被搓到 prompt
> 
> 只是如何觸發的區別

* * *

**yan5xu** @yan5xu [2025-12-24](https://x.com/yan5xu/status/2003618544735649947)

skills 重点在Prompt 发现&懒加载，改变当前 agent 能力，有当前完整上下文，我觉得适合的场景是当前任务复合程度不高的情况（载入多个 skills 就会出现性能下降问题），比如主 Agent 是入口当做路由，然后通过 skills 载入场景能力，进入到 YouTube-summary，写 ppt 模式；

sub-agent 也有发现过程，但重点是过程压缩，执行过程在当前 agent 之外，他对于当前 agent 就是一个 tool（function call），只有 req/res；

还有一个把两种结合在一起的方式，在一个节点发现需要 skills，载入执行拿到 skills 的结果后，把需要 skills 的节点到结果的节点的 tool use 过程进行压缩，也是一种方式。

![Image](https://pbs.twimg.com/media/G85IW7DagAAbkUL?format=png&name=large)

* * *

**yan5xu** @yan5xu [2025-12-24](https://x.com/yan5xu/status/2003620025593409792)

sub-agent 除了现在 tool 之外，还可以通过文件系统，实现一点点 main/sub agent 双向通信，进一步压缩上下文。比如主 agent 委托指令，用文档地址而不是直接写到指令中，sub agent 的返回内容也是一个 状态/交付物/决策点 以及一个过程记录的文档地址，主 agent 根据决策点判断载入哪些内容；

* * *

**yan5xu** @yan5xu [2025-12-24](https://x.com/yan5xu/status/2003620713018859932)

后面说的结合办法，在 claude code，可以在载入 skills并且完成 skills 的内容之后，让cc 把这个过程给总结到文档（可以固定成一个 slash command），然后 rewind 回滚到 skills 载入前的节点，说“我已经完成了，文档在 XXX”来实现；

我经常在上下文快到头的时候用这个办法抢救

* * *

**亚洲图片** @tt67wq [2025-12-24](https://x.com/tt67wq/status/2003655830995108262)

可以在 skill 的脚本里面调用下 ai 的 sdk，实现类似 sub-agent 的效果

* * *

**yan5xu** @yan5xu [2025-12-24](https://x.com/yan5xu/status/2003662103006314664)

这个可以！之前好像很多是让 agent 通过 cli yolo 模式调用

* * *

**Bob | AI 企业提效** @Hey\_BobAI [2025-12-24](https://x.com/Hey_BobAI/status/2003830245619806569)

未来的 Agent 不再是臃肿的全才，而是拥有‘感知-检索-压缩’能力的极简大脑。Skills 负责深度，Sub-Agent 负责广度

* * *

**知识猫图解** @GeekPediax [2025-12-25](https://x.com/GeekPediax/status/2004150673278140620)

![Image](https://pbs.twimg.com/media/G9AsaPCaYAA5N-s?format=jpg&name=large)

* * *

**Jian** @hello\_jian [2025-12-24](https://x.com/hello_jian/status/2003710104080908586)

可以sub-agent \* SKILL

可以子代理 \* 技能

* * *

**终南山葫芦娃** @infmaxtop [2025-12-25](https://x.com/infmaxtop/status/2004016231675056212)

感觉有些像是三个臭皮匠顶个诸葛亮的，主打团队作战，打造成多面手