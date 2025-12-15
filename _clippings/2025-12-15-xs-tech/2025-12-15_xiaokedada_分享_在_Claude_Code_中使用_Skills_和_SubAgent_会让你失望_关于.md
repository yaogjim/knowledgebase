---
title: "2025-12-15_xiaokedada_分享_在_Claude_Code_中使用_Skills_和_SubAgent_会让你失望_关于"
source: "https://x.com/xiaokedada/status/1999130869072834850"
author:
  - "[[@xiaokedada]]"
published: 2025-12-15
created: 2025-12-15
description:
tags:
  - "#分享"
  - "x"
  - "@xiaokedada"
  - "command"
---

# #分享 在 Claude Code 中使用 Skills 和 SubAgent 会让你失望 - 关于

**nazha** @xiaokedada [2025-12-11](https://x.com/xiaokedada/status/1999130869072834850)

#分享 在 Claude Code 中使用 Skills 和 SubAgent 会让你失望 - 关于如何激活 Skill 的调查

这几天为公司内部引入基于 AI 研发流程，类似于 superpowers / claude-code-infrastructure-showcase 这些 case。然而让人很困惑的是，这些 Skill 和 SubAgent 的激活率极低。

\> 它们就静静地躺在那里，不像是静静地等待被唤醒，而是被彻底遗忘。

在社区的一些方案里，主要是基于 UserPromptSubmit 这个 Hook 做一些主动激活的事情。比如这样：

{

"hooks": {

"UserPromptSubmit": \[

{

"hooks": \[

{

"type": "command",

"command": "echo 'INSTRUCTION: If the prompt matches any available skill keywords, use Skill(skill-name) to activate it.'"

}

\]

}

\]

}

}

{

"hooks": {

"用户提示提交"：\[

{

"钩子": \[

{

"type": "command",

"command": "echo '指令：若提示匹配任何可用技能关键词，请使用技能（技能名称）激活该技能。'"

}

\]

}

\]

}

}

或者这样：

"hooks": {

"UserPromptSubmit": \[

{

"matcher": "",

"hooks": \[

{

"type": "command",

"command": "echo \\"I have these agents available: \[list all available agents\], i will use \[name agent\] to solve this task as it is the best for \[reason for choosing that agent\]\\""

},

{

"type": "command",

"command": "echo \\"REPEAT OUTLOUD: \\\\n I WILL NOT CREATE REDUNDANT FILES \\\\n I WLL CLEAN UP AFTER MY SELF AND KEEP ONLY THE ACTUAL DEMANDED SOLTUTION \\\\n I WILL NOT OVERENGINEER \\\\n I WILL USE THE APROPRIATE AGENT \\\\n I WLL NOT ABANDON MY OBJECTIVE CREATING SIMPLER TESTING FILES\\""

}

\]

}

\]

}

或者这样：

"hooks": {

"用户提示提交"：\[

{

"匹配器": ""

"hooks": \[

{

"类型": "命令",

"command": "echo \\"我有以下可用代理：\[列出所有可用代理\]，我将使用\[指定代理名称\]来解决此任务，因为它最适合\[选择该代理的原因\]\\""

},

{

"类型": "命令",

"command": "echo \\"大声重复：\\\\n 我不会创建冗余文件 \\\\n 我会自行清理并只保留实际需要的解决方案 \\\\n 我不会过度工程化 \\\\n 我会使用合适的代理 \\\\n 我不会放弃目标去创建更简单的测试文件\\""

}

\]

}

\]

}

抱歉，你最后的激活率也可能只达到 50%。

\> 如果你在提示词里表现出任何地温和态度，Claude Code 都会选择无视它。

社区还有个策略是通过三个过程让 Claude Code 做出强制激活的承诺，代价是更多的 Token 和注意力。这三个步骤是：

Step 1 - EVALUATE: For each skill, state YES/NO with reason

Step 2 - ACTIVATE: Use Skill() tool NOW

Step 3 - IMPLEMENT: Only after activation

第一步 - 评估：针对每项技能，给出是/否的判断并说明理由

第二步 - 激活：立即使用技能()工具

第三步 - 实施：仅在激活后进行

CRITICAL: The evaluation is WORTHLESS unless you ACTIVATE the skills.

关键提示：除非你激活技能，否则评估毫无价值。

这个策略，同样是实现在 UserPromptSubmit 这个 Hook，似乎没有别的路子。

在这种几乎疯狂的 Hack 的策略下，能把 Skill 的 激活率提升 80%。

坑，已经帮大家踩过了。

* * *

**nazha** @xiaokedada [2025-12-11](https://x.com/xiaokedada/status/1999130871505592344)

参考资料：

1\. Superpowers https://github.com/obra/superpowers…，一个基于 Claude Code 的代码开发工作流程，想法挺好，但是 not work

2\. 官方 issue https://github.com/anthropics/claude-code/issues/9716…

3\. https://scottspence.com/posts/claude-code-skills-dont-auto-activate… 这篇文章就是介绍如何将 Skills 的激活提升到 80% 的策略

4.

* * *

**FlintyLemming** @FlintyLemming [2025-12-12](https://x.com/FlintyLemming/status/1999417111433883692)

2.0.67 对于 subagent 的调用已经非常积极了，至于rules 更是必读

* * *

**Hektoen International** @hekint

When composer Frédéric Chopin died in 1849, his heart was preserved in cognac and interred in a church in Warsaw; authorities today forbid examination. He was supposed to have died of lung disease (TB), but cardiac disease and even cystic fibrosis have been suggested.

1849年作曲家肖邦逝世时，他的心脏被保存在白兰地中，安葬于华沙的一座教堂；如今当局禁止对其进行检查。据称他死于肺病（肺结核），但也有人提出是心脏病甚至囊性纤维化。

![Image](https://pbs.twimg.com/media/G7-MhuzXEAUQbT5?format=jpg&name=large)

* * *

**Lukin** @iLukin [2025-12-12](https://x.com/iLukin/status/1999345225689629072)

所以 我还是继续用 command

* * *

**pand** @pand\_lin [2025-12-12](https://x.com/pand_lin/status/1999381166454112468)

我激活率100%，且没你这些花里胡哨的东西

* * *

**亚洲图片** @tt67wq [2025-12-12](https://x.com/tt67wq/status/1999389999457054986)

我都是直接命令cc 使用某个 skill 的