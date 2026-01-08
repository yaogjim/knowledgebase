---
title: "迭代系统提示词的方法和实践"
source: "https://x.com/dontbesilent12/status/2008598819869708781"
author:
  - "[[@dontbesilent12]]"
date: "2026-01-08T16:38:22+08:00"
created: 2026-01-08
description:
tags:
  - "@dontbesilent12 #AI #系统提示词 #迭代 #强化学习 #RLHF #人类反馈 #负反馈 #系统设计"
---
**dontbesilent** @dontbesilent12 [2026-01-06](https://x.com/dontbesilent12/status/2008598819869708781)

分享一下我怎么迭代我的系统提示词

这是一个尝试去复制我自己的文字风格的系统提示词

它写得很烂，但是提示词的框架很好，可以通过有限次数的迭代，改进得很好

我会让它大量输出，然后给它写的文案挑毛病：

1、哪句写得不好

2、为什么不好

3、什么情况下可以这么写

每一个版本的系统提示词，都会跟着这样一个表格

迭代 n 次之后，这个文档里面会有 V1～Vn 总共 n 个版本的系统提示词，以及对应的 n 个表格

然后把整个文档下载下来，让 AI 给我 V(n+1) 版本

![Image](https://pbs.twimg.com/media/G9_5Mb1acAABFfu?format=jpg&name=large)

---

**dontbesilent** @dontbesilent12 [2026-01-06](https://x.com/dontbesilent12/status/2008601863877476846)

当我测试的数据多了之后，我可以复制一个「dontbesilent（测试版）」，做一个专门用于测试的 system prompt

这样就有了文案智能体和测试智能体（暂且误用“智能体”这个词，实际上就是 chatbot）

---

**dontbesilent** @dontbesilent12 [2026-01-06](https://x.com/dontbesilent12/status/2008601968647012461)

然后衍生出两种方法：

A：做工作流，让测试智能体不断给文案智能体负反馈，只有通过了测试智能体的文案才能进入到 output 节点

B：用测试智能体产出大量的正反馈和负反馈，搜集全方位的数据，然后用于迭代文案智能体的 system prompt

---

**dontbesilent** @dontbesilent12 [2026-01-06](https://x.com/dontbesilent12/status/2008602097206652981)

然后用 B 流程产出的新版的文案智能体，放到工作流 A 里面， 看看能不能用更少的循环次数，触发 output 节点，产出合格的文案

所以新的评判标准，就不再是测试智能体给的反馈

而是整个工作流的 token 消耗是否可以稳定降低

---

**孔孔** @0x0fish [2026-01-07](https://x.com/0x0fish/status/2008738310542553317)

don哥写负反馈的效率会不会太低了，AI有无数种犯错的可能，只告诉它如何得分会不会更好？

---

**dontbesilent** @dontbesilent12 [2026-01-07](https://x.com/dontbesilent12/status/2008750031055261784)

一定要写足够多的负反馈，建立一个围栏，在围栏内自由发挥

---

**香蕉Banana** @treydtw [2026-01-07](https://x.com/treydtw/status/2008704772774535360)

这看着好像就是RLHF工程（(基于人类反馈的强化学习）了。

有点强😂

---

**dontbesilent** @dontbesilent12 [2026-01-07](https://x.com/dontbesilent12/status/2008749825777693076)

就是 reward model 的思路

---

**谢赋琪** @xiefuqi [2026-01-07](https://x.com/xiefuqi/status/2008760599753400829)

提示词迭代系统这个需求为什么没有人搞一个专门的小工具出来呢🤔，话说应该挺多人需要的。

---

**dontbesilent** @dontbesilent12 [2026-01-07](https://x.com/dontbesilent12/status/2008761373895872546)

核心工作是人类把负反馈写清楚

迭代流程是次要的

---

**汪仔** @wangzaimedia [2026-01-06](https://x.com/wangzaimedia/status/2008686351215153251)

可以理解为通过多次反馈建立了一套自己文案的评判标准吗

---

**dontbesilent** @dontbesilent12 [2026-01-07](https://x.com/dontbesilent12/status/2008749783838847334)

先做裁判，后做运动员

---

**Vicky** @vickyzhangtimes [2026-01-07](https://x.com/vickyzhangtimes/status/2008862274136822052)

这个负反馈的评价太有趣了，你是怎么给这个负反馈的角色定位的 ，从我的角度 完全感受不到 那个错了，有高高在上的感觉，是什么样的人会有啊🤣

---

**Berryxia.AI** @berryxia [2026-01-06](https://x.com/berryxia/status/2008685318585938042)

这个记录对比的形式挺好，我是每次直接迭代看效果没有进行横向拉表对比。 这样更直观一下，mark！☺️
