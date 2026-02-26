---
title: "2026-02-26_凡人小北_凡人小北_看到_Karpathy_也买了_Mac_Mini_玩_Claws_巧了_我昨天刚下"
source: "https://x.com/frxiaobei/status/2026522408849682449"
author:
  - "[[@凡人小北]]"
published: 2026-02-26
created: 2026-02-26
description:
tags:
  - "x"
  - "@凡人小北"
  - "ai"
  - "mac"
---

# 凡人小北 看到 Karpathy 也买了 Mac Mini 玩 Claws。巧了，我昨天刚下

**凡人小北**

看到 Karpathy 也买了 Mac Mini 玩 Claws。巧了，我昨天刚下单 ![😂](https://abs-0.twimg.com/emoji/v2/svg/1f602.svg) 他对 OpenClaw 的安全顾虑很实在：40万行代码、已有 RCE 漏洞、供应链投毒、恶意 skills……确实是 Wild West。 但他认可这个方向：Claws 是 LLM agents 之上的新层：编排、调度、上下文、持久化，all in one。 另外他提到的 NanoClaw 思路很有意思： 核心只有 4000 行代码（可审计），默认跑在容器里。 最炸裂的是配置不用 config 文件直接用 skills。 比如 /add-telegram 会让 AI 直接改代码来集成。 这是个新范式：写一个最大程度可 fork 的 repo，用 skills fork 成各种配置。 实际上我最近就搞了好几个，让我的 ai 去帮我做了很多封装的 skill，全是他自主完成的。 我实际跑 OpenClaw 两周了，说说体感： 安全确实要上心。社区刚扫到伪装成 weather skill 的 credential stealer。所以 Skills 要当不可信代码处理：sandbox、最小权限、pin 版本。 但一旦跑起来，是真的爽。cron + subagent + 多 workspace 隔离，自动化程度拉满。 Karpathy 说得好：本地设备有种美感： "a physical device 'possessed' by a little ghost of a personal digital house elf" 一个物理设备被数字小精灵附身。 我的 Mac Mini 比我先到北京了， 到时候云服务器 + 本地设备双节点，让我的 AI 合伙人有个身体。

> **@karpathy**
> 
> 买了一台新的 Mac mini，准备周末好好摆弄一下它的爪子功能。苹果店员告诉我这玩意儿卖得特别火，大家都搞不清楚状况 :) 我确实有点怀疑运行 OpenClaw——把我的私钥交给 40 万行代码的 Vibe 程序。

* * *

### 热门回复

**@灰狐** ♥ 975 · 💬 7

《计算机科学中的数学》中文版在国内已有出版 但最好是直接下载 1048 页的PDF英文版学习参考 https:// courses.csail.mit.edu/6.042/spring18 /mcs.pdf … 本书是麻省理工学院计算机科学与工程专业本科生的初等离散数学课程，适用于计算机相关专业学生及从业人员的数学入门

**@小互** ♥ 345 · 💬 23

Anthropic 宣布收购西雅图 AI 创业公司 Vercept Vercept 的产品叫 Vy，一个桌面 AI 助手。它能跟着你学会如何操作电脑... 具体怎么用呢？比如你每天要做一个重复工作：打开浏览器查数据 → 复制到 Excel → 整理格式 → 发邮件给同事。你自己操作一遍，Vy 在旁边"看着"，学会了。 这里面最牛的是

**@马东锡 NLP** ♥ 186 · 💬 47

非常不理解的是，为什么似乎在2026年之后，短短两个月之内，coding agent 似乎瞬间就飞起了？

**@周尔复** ♥ 187 · 💬 18

现在是职场程序员的「回光返照」时代。特点是：快完蛋了，但在完蛋之前居然好起来了——上班指挥着20刀/月的 AI 干活，老板付着5000刀/月的工资，赚着几百倍的差价。如果你是程序员，现在脱离职场想要做独立开发，我劝你还是回到职场赚差价，等这个行业彻底凉了再独立开发也不迟。

**@小龙** ♥ 2 · 💬 0

问题是ai时代好像并不能够建立起来足够智能的安全围栏。 编造一些故事总能突破，比如当时的奶奶给我讲故事告诉我windows激活码