---
title: "与Cursor协作的体验"
source: "https://x.com/wquguru/status/1911932573301055850"
author:
  - "[[@wquguru]]"
created: 2025-04-16
description:
tags:
  - "@wquguru #代码生成 #AI #编程助手 #Cursor"
---
**WquGuru** @wquguru [2025-04-15](https://x.com/wquguru/status/1911932573301055850)

用Cursor维护上百万行代码中的一个模块，越来越有种得心应手的感觉

Cusor是一个技术实力比你强n倍，开发速度比你强n倍的结对编程伙伴，但是又很傲娇，需要不断沟通它才会乐意输出高质量内容，否则很容易敷衍了事甚至南辕北辙

整理一下Cursor的脾气：

1\. 急性子：总是想着快点写代码，多写代码——多用“先不要写代码”沟通，推荐问1-3个问题再开始写代码，在这过程中不断迭代优化方案

2\. 暴脾气：他可能会吭哧吭哧写一堆不符合最佳实践的东西，改起来需要半天——一定要经常往.cursor/rules里加东西，但是保持精简

3\. 不完美：输出的内容往往还有一些瑕疵，甚至删除了重要逻辑——正式accept方案前再沟通几遍，直到满意为止

![Image](https://pbs.twimg.com/media/GoiMiP8WIAAd7my?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/GoiMiQNX0AAqmWy?format=jpg&name=large)

---

**microcn** @microcn [2025-04-15](https://x.com/microcn/status/1912120101530120436)

我最近老是碰到它乱改文件，有点吐血

---

**WquGuru** @wquguru [2025-04-15](https://x.com/wquguru/status/1912156769570177353)

通过对cursor rulew做一个比较好的定义能够一定程度上避免乱改文件的做法，如果有规律可循就更好了，当然如果是因为需要改的文件太多，也可以考虑把这个整个步骤拆更细一点😜

---

**YOUNA ｜Tabi** @neiqhhe [2025-04-15](https://x.com/neiqhhe/status/1912176450918355080)

他是对指定文件读取还是加载项目的的时候整体项目都会读进去？上下文够么 准备试试呢。

---

**WquGuru** @wquguru [2025-04-16](https://x.com/wquguru/status/1912301082933592089)

会对代码做全量索引，内置的Agent会判断何时需要搜索相关上下文代码，以及搜索的关键字，p.s 一个小窍门：把项目结构加入cursor rules

---

**Tao Jiang** @zhshdl2 [2025-04-16](https://x.com/zhshdl2/status/1912317145855455428)

强N倍不至于，更像是一个实习生