---
title: "2026-02-26_Yadong_Xie_Yadong_Xie_正确的使用_spec_driven_有几个关键点_1_如何划分_s"
source: "https://x.com/yadong_xie/status/2026349409034973397"
author:
  - "[[@Yadong Xie]]"
published: 2026-02-26
created: 2026-02-26
description:
tags:
  - "x"
  - "@Yadong Xie"
  - "spec"
  - "agent"
---

# Yadong Xie 正确的使用 spec driven 有几个关键点： 1. 如何划分 s

**Yadong Xie**

正确的使用 spec driven 有几个关键点： 1. 如何划分 scope 让 agent 在合理的 context 内能够并行工作 2. 如何设置合理的验收逻辑，让 agent 能够在合理循环内结束 3. 如何正确的设置 feedback loop，让 agent 能够在有限次数内收敛 其实整个设计就是《自动控制原理》 自动控制原理是研究在无人直接参与的情况下，通过控制装置使被控对象按预定规律运行的技术科学 死去多年的自动化专业又在攻击我

> **@yadong\_xie**
> 
> 这篇文章建立在一个错误的假设前提下，code 会永远存在并且做为产品的 single source of truth 事实上的最后产品的 spec 才是 SoT，code 的角色最终会变成 bin 或者汇编 code 不是资产，spec 才是，每次有更好的模型就可以从 spec 获得更好的 code implement，而不是让 ai 在 code 的 shit mountain x.com/augmentcode/st…

* * *

### 热门回复

**@Polymarket** ♥ 20.9K · 💬 1477

Bitcoin up or down? 5 minute up/down crypto polymarkets are now live. Powered & secured by Chainlink

**@鹿 𝕟𝕠𝕜𝕚𝕟𝕠𝕜𝕚 祥子——** ♥ 3 · 💬 0

不是管理学么（ 不然这系统的零极点可有点难找啊

**@lee lion** ♥ 1 · 💬 0

感觉代码作为上下文，在已有大项目上内容量太大了，更容易幻觉，尤其是多人维护，写了点脏东西，或者很多都不是关键信息，很多代码都是辅助一个核心方法写的，这种对AI的要求太高了。或者新项目都没有代码，spec说是规范，最终还是为这次prompt的session最优上下文服务，主要就是要那种指哪打哪的感觉