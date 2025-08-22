---
title: "如何做任务进度跟进？"
source: "https://x.com/BadUncleX/status/1932419883687674361"
author:
  - "[[@BadUncleX]]"
created: 2025-07-01
description:
tags:
  - "@BadUncleX #任务管理 #进度跟进 #效率提升"
---
**BadUncle** @BadUncleX [2025-06-10](https://x.com/BadUncleX/status/1932419883687674361)

Claude Code 如何做任务进度跟进？

先说结论： 每一个新需求，让Claude Code帮你自动生成一个对应md文件， 该文件包含plan和progress

Claude Code自带一个"内存版的todo list"，就是在面临新需求的时候， 它会自动拆解， 但是这个仅仅是用于更好的让用户查看当前进度，以及LLM自己保持前后一致性， 缺点是， 当前任务结束后用户并不好review。

如何review呢？ 就是让Claude Code建一个plan and progress的同步版本 md文件。

每次都要提醒一次吗？ 不用， 将prompt写入CLAUDE\[.\]md文件即可。 我一般都是放在 \`docs/plan\` 文件夹

维护的md文档效果如图

prompt见gist链接(二楼) (prompt建议放在~/.claude/CLAUDE\[.\]md 全局目录下， 具体内容根据自己的需求删减)

结尾： 本tips继续follow我之前提倡的简化/无状态/的理念， 即不需要过度复杂化项目跟进管理，我认为cline的内存银行有复杂化趋势。 另外，就是不要手工维护文档， 而让LLM自动维护， 你通过prompt将其自动化为你的流程的一部分。

为什么拒绝复杂？ 因为复杂是时间的敌人， 过了一段时间狗都不理。

![Image](https://pbs.twimg.com/media/GtFUaytbYAA-YxE?format=jpg&name=large)

---

**BadUncle** @BadUncleX [2025-06-10](https://x.com/BadUncleX/status/1932419886460121160)

prompt:  
提示

---

**xincmm** @xincmm [2025-06-11](https://x.com/xincmm/status/1932700944434884665)

这思路真的很棒，我用 cursor 试了一下，虽然有些错误，但大体是按照这个 todo 来执行

![Image](https://pbs.twimg.com/media/GtJUj9HbUAA58Z4?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/GtJVFUfbMAE7S5Z?format=jpg&name=large)

---

**BadUncle** @BadUncleX [2025-06-11](https://x.com/BadUncleX/status/1932702211072799047)

用起来， 简单的才能做到持续可靠

---

**BRUNT Workwear** @bruntworkwear

The all-new USA Marin Welted is Built in the USA and delivers stability, comfort, and performance for the toughest job sites. Crafted with waterproof leather sourced from American cattle, global components, and assembled at our factory in Texas.  
全新的美国马林固特异 welted 鞋款在美国制造，为最严苛的工作场地提供稳定性、舒适性和卓越性能。采用源自美国牛群的防水皮革、全球零部件，并在我们位于德克萨斯州的工厂组装而成。

---

**宝玉** @dotey [2025-06-11](https://x.com/dotey/status/1932589637974798473)

谢谢分享，很有用，复杂一点任务我也是让它写 TODO

---

**Cheney** @zicjin [2025-06-11](https://x.com/zicjin/status/1932648875783041394)

"同步版本 md文件" 完全看不懂什么意思

---

**BadUncle** @BadUncleX [2025-06-11](https://x.com/BadUncleX/status/1932688678960402588)

就是你任何事都不做的话， 它仅仅在当前的对话过程中显示待办列表， 但是任务结束这个列表就消失了， 这里的同步就是将这个消失的列表保存到本地文件中， 这样就可以有迹可循了
