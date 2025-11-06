---
title: "2025-11-04_karminski3_啊_AI可以自己找活干了_给大家介绍一个炸裂的开源项目_Hephaestus_这玩意儿让AI"
source: "https://x.com/karminski3/status/1984140302886826477"
author:
  - "[[@karminski3]]"
published: 2025-11-04
created: 2025-11-04
description:
tags:
  - "@karminski3"
  - "@the"
  - "@lamzunghin"
  - "@shiyan"
  - "@likefeiwu"
  - "https"
  - "//x"
  - "2025-10-31"
  - "👋"
  - "spec"
  - "x.com"
status: "inbox"
importance: 2
effort: 2
review_level: 0
review_next: "2025-11-13"
review_interval: null
review_count: 0
decision: null
topics: []
links_out: []
summary: ""
pov: ""
actions: []
---

# 啊？AI可以自己找活干了？ 给大家介绍一个炸裂的开源项目 Hephaestus - 这玩意儿让AI

**karminski-牙医** @karminski3 [2025-10-31](https://x.com/karminski3/status/1984140302886826477)

啊？AI可以自己找活干了？

给大家介绍一个炸裂的开源项目 Hephaestus - 这玩意儿让AI Agent自己规划工作，自己发现问题，自己创建任务！抽象到什么程度？它内嵌了个kanban....让AI自己拆解card自己做....

传统的Agent框架都是你提前写死所有流程，遇到没预料到的情况就傻眼。Hephaestus 直接换了个思路：只定义三个阶段（分析-实现-验证），然后Agent自己看着办。

举例：测试Agent在跑测试时，发现了一个性能优化机会，它不是记个log就完事，而是自己创建了一个新的调查任务，然后放到kanban里，然后另一个Agent接手去研究，确认可行后又自己创建实现任务。整个工作流就这么自己长出了一个分支。

你给它一个PRD，它分析出5个组件，创建5个并行任务。其中一个Agent干完了发现bug，自己创建修复任务。另一个Agent发现可以优化，自己创建优化分支。工作流是实时生成的，而不是一开始就预测好的。

我有空也会测一下试试，看看它能不能真的从0到1自己把活干完。总之先增加到待测试列表。

项目地址：https://github.com/Ido-Levi/Hephaestus…

* * *

**Ido Levi** @the\_ido\_levi [2025-10-31](https://x.com/the_ido_levi/status/1984152993696989537)

Hey, It's the author 👋

When you get the chance let me know how it went!

I've been working on this alone so there are \*some\* rough edges, but overall it should work pretty well (you should try creating a new workflow, check the guides in the docs^)

嘿，我是作者 👋

有机会时告诉我进展如何！

我独自完成这项工作，因此\*有些\*地方还不够完善，但总体上应该运行得相当不错（你可以尝试创建一个新的工作流，查阅文档中的指南^）

* * *

**zysam** @lamzunghin [2025-10-31](https://x.com/lamzunghin/status/1984177495755866306)

现在的 spec 工具也差不多，流程改变就乱套了。改来改去结果维护 spec 而走了许多弯路，浪费了tokens 和时间。这个看起来是解决问题，但实际跑起来会不会乱套就不知道了。

* * *

**GuanJia** @shiyan\_cn [2025-10-31](https://x.com/shiyan_cn/status/1984154870417650153)

任务发散出去，在有后之年能不能收敛回来？

* * *

**化骨绵掌** @likefeiwu [2025-11-01](https://x.com/likefeiwu/status/1984456826356973659)

纯ReAct，是这样的，理论上来说模型能力够强的化，最后结果会好很多很多，当然Token也会多超多

* * *

**jack rose** @jackros81044097 [2025-10-31](https://x.com/jackros81044097/status/1984181823929569382)

等待测试结果，就怕项目没搞完，token 废一堆

* * *

**OSDev** @OiiDev [2025-10-31](https://x.com/OiiDev/status/1984190242321240218)

@readwise save thread

@readwise 保存主题

* * *

**kuriball** @wanjiasu [2025-10-31](https://x.com/wanjiasu/status/1984358516468109536)

这不就是planner-excutor？

* * *

**Jakku 彼岸樱** @JakkuSakura [2025-11-01](https://x.com/JakkuSakura/status/1984637551274311825)

看了一下，感觉用起来很麻烦，要配置很多东西，我好懒

* * *

**smallarmy** @zhangxj2008 [2025-10-31](https://x.com/zhangxj2008/status/1984293120444711214)

真成神了！会不会自己生小孩啊😯