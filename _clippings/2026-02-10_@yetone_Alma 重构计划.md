---
title: "Alma 重构计划"
source: "https://x.com/yetone/status/2020875192923558026"
author:
  - "[[@yetone]]"
date: "2026-02-10T13:56:21+08:00"
created: 2026-02-10
description:
tags:
  - "@yetone #AI_Native #Alma_Rewards #技能驱动 #自动化配置 #重构计划"
---
**yetone** @yetone [2026-02-09](https://x.com/yetone/status/2020875192923558026)

这几天因为在泰国旅游所以高强度使用了 openclaw, 离开了它丑丑的 UI 我发现 openclaw 最牛逼的地方就是它是一个高度 AI Native 的系统（拜托于各式各样的 skills），这是 Alma 目前特别欠缺的。Alma 还是部分 AI Native 部分 workflow。接下来 Alma 可能要进行一个极大的重构，让 Alma 本身也变成一个彻底的从头到尾的 AI Native 系统

---

**✧ 𝕀𝔸𝕄𝔸𝕀 ✧** @iamai\_eth [2026-02-09](https://x.com/iamai_eth/status/2020882642674295005)

很不稳定，高度依赖ai provider，需要增强自保活能力

---

**Focal** @AskFocal

Get Focal today

---

**Nshen** @nshen121 [2026-02-09](https://x.com/nshen121/status/2020890671402651818)

为什么泰国旅游需要openclaw?

---

**yetone** @yetone [2026-02-09](https://x.com/yetone/status/2020896177940750636)

因为大多数情况下都不在电脑前

---

**albert** @albertmokt [2026-02-09](https://x.com/albertmokt/status/2020880596147577344)

其实并不是因为 UI 丑，而是他本身就是一个 Headless AI Native 产品，如果真的说有 UI 的话，那 IM 就是他的 UI 了。他的出现其实给很多 agent 产品一个启示，agent 最适合的载体就是 IM，因为可以随时随地唤起。

---

**yetone** @yetone [2026-02-09](https://x.com/yetone/status/2020881025875022121)

是的，我之前被它满眼 Vibe 的 dashboard 给吓哭了，因为我不太信任满眼 Vibe 的系统，但是看了一下它底层依赖的 pi 的源码，我完全放心了

---

**albert** @albertmokt [2026-02-09](https://x.com/albertmokt/status/2020882753571676405)

他底层的 pi-agent-core 真的是贯彻了极简的 Unix 设计哲学：只需四个工具 read/write/edit/bash，其他都是文件系统。非常符合直觉且具有很大想象力

---

**yetone** @yetone [2026-02-09](https://x.com/yetone/status/2020883271576637835)

只能说它想得很彻底，很明白。我之前还傻逼似的给 Alma 增加各种 search fetch 的工具，现在我准备抛弃了，也只给 alma 提供四大金刚工具，其他的都通过 skills 来实现。这样的话啊，一部分利用了市面上所有的 skills 能力，另一部分还极大地使用了 prompt caching, 让缓存命中率极大地提高

---

**南闲** @norsizu [2026-02-09](https://x.com/norsizu/status/2020876322294382919)

如果可行的话，最大的一个障碍或者期望能打通的是IM这端，我目前觉得如果我在电脑端，处理任务很丝滑，但是回家不打开笔记本，手上只有手机的时候，就跟失联了差不多，Alma如果能打通跟手机IM这端的链接，那就无敌了

---

**yetone** @yetone [2026-02-09](https://x.com/yetone/status/2020876480310542660)

已经打通了：

> 2026-02-09
> 
> ![Image](https://pbs.twimg.com/media/HAtaRIhaMAAmX0d?format=jpg&name=large)

---

**UBsoft** @zhiyebanzhuan [2026-02-09](https://x.com/zhiyebanzhuan/status/2020884324246274116)

没错Alma是有层层叠叠的UI树和对化设置的，要让设置能通过对话和记忆，自己设置自己

---

**yetone** @yetone [2026-02-09](https://x.com/yetone/status/2020884628958318861)

接下来的几个版本，Alma 逐渐进化到 skill base 的系统，大家都不需要通过任何 UI 点击就能完成所有的 Alma 的配置工作

---

**ody** @odyzhou [2026-02-09](https://x.com/odyzhou/status/2020882427267396039)

您怎么定义ai native？

---

**yetone** @yetone [2026-02-09](https://x.com/yetone/status/2020882828494594361)

完全发挥 AI 的主观能动性，不需要用户操作任何的 UI 控件，只通过聊天让 AI 完成所有的操作

> 2026-02-09
> 
> 完全发挥 AI 的主观能动性，不需要用户操作任何的 UI 控件，只通过聊天让 AI 完成所有的操作

---

**逆风狂撒花椒粉** @alucard\_907 [2026-02-09](https://x.com/alucard_907/status/2020902255671853541)

质疑，理解，成为。

---

**yetone** @yetone [2026-02-09](https://x.com/yetone/status/2020912364392956416)

我哭了，我真的哭了

---

**WeZZard** @realWeZZard [2026-02-09](https://x.com/realWeZZard/status/2020882412507717858)

我总感觉 Cowork 是在抄 Alma

---

**吒老斯** @zachzhao1984 [2026-02-10](https://x.com/zachzhao1984/status/2021056324273066273)

你的 openclaw 是部署在 Macmini 上么

---

**大梁Pro** @Daliang66 [2026-02-09](https://x.com/Daliang66/status/2020878589940633748)

想想就期待，提前给大佬磕一个

---

**microstrong** @Microstrongs [2026-02-09](https://x.com/Microstrongs/status/2020876109588701335)

每天都在进行重构，或大或小

---

**Leo** @leeoxi [2026-02-09](https://x.com/leeoxi/status/2020888997552394717)

ai native会更依赖模型本身的能力？

---

**Sanjin** @EqbymCi [2026-02-10](https://x.com/EqbymCi/status/2021045150747853277)

可以看下 craft ,一些配置直接让 ai 自己修改自己写

---

**wuding** @daobian\_xue [2026-02-10](https://x.com/daobian_xue/status/2021029041160020376)

快端上来罢！我率先更新

---

**loveweb3** @EMEAnp9D7ASsztm [2026-02-10](https://x.com/EMEAnp9D7ASsztm/status/2021047986206408719)

期待alma的重构

---

**Togo** @chickenpunk\_ [2026-02-09](https://x.com/chickenpunk_/status/2020912228023796096)

老师又要发力了

---

**Kiierr** @kiierrhairgrow

We've helped 100k+ win their hair loss battle..

Start seeing results in just 7 weeks! Money-Back Guarantee.