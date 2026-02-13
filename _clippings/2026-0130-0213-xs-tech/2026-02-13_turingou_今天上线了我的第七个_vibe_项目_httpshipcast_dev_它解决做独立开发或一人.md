---
title: "2026-02-13_turingou_今天上线了我的第七个_vibe_项目_httpshipcast_dev_它解决做独立开发或一人"
source: "https://x.com/turingou/status/2021145195316904322"
author:
  - "[[@turingou]]"
published: 2026-02-13
created: 2026-02-13
description:
tags:
  - "x"
  - "@turingou"
  - "https"
  - "2026-02-10"
---

# 今天上线了我的第七个 vibe 项目，httpshipcast.dev 它解决做独立开发或一人

**郭宇 guoyu.eth** @turingou [2026-02-10](https://x.com/turingou/status/2021145195316904322)

今天上线了我的第七个 vibe 项目，http://shipcast.dev

它解决做独立开发或一人公司最头疼的事之一：代码写完了，但永远懒得发推宣传。vibe coding 的项目太多，vibe marketing 远远不够。

我自己就是这样，一个项目迭代了几十个 commit，加了一堆新功能，修了无数 bug，但从来没跟任何人说过。等想起来要宣传的时候，已经过了好几周，根本记不清改了什么。勉强写一条推文，措辞还干巴巴的，像在读 git log。

后来我想，这件事明明可以自动化。于是做了 Shipcast。

它做的事情很简单：连接你的 GitHub repo，自动追踪每一次 push，把枯燥的 commit message 用 AI 改写成用户看得懂的更新推文。你设好发布时间，它就每天定时帮你发推。

不需要你打开任何 dashboard 手动操作。Push 代码就是唯一的输入，推文就是自动的输出。

具体流程：

1\. GitHub 登录，绑定你的 repo

2\. 连接你的 X 账号

3\. 选择语言、语气风格、每天几点发布

4\. 然后就不用管了

AI 会自动聚合你最近的 commits，过滤掉 merge commit 和杂项，提炼出真正有意义的改动，生成一条适合社交媒体传播的推文。支持中文、英文、日文等多种语言。

Pro 用户还能解锁：

\- AI 自动生成配图，让推文更抢眼

\- Changelog thread，主推文 + 详细更新日志自动串成 thread

\- 自定义 AI prompt，控制生成风格

\- 去掉品牌水印

说白了，Shipcast 填的是「写代码」和「告诉别人你写了代码」之间的那条鸿沟。很多独立开发者的项目不是不好，是根本没人知道。保持社交媒体上的存在感，对一个产品的成长太重要了，但手动维护太耗精力。

接下来的计划：X 只是起点。我会陆续为 Pro 用户上线更多渠道的支持，比如小红书等社交网络的自动发布，KOL 广告发布，邮件订阅推送（让你的用户直接在收件箱里收到产品更新），以及 DM 自动回复，基于你的产品文档和更新记录，用 AI Agent 自动响应用户私信咨询，相当于一个 7×24 在线的智能客服。目标是让 Shipcast 成为独立开发者的一站式产品传播引擎，而不仅仅是一个发推工具。

http://shipcast.dev

![Image](https://pbs.twimg.com/media/HAyMEZEaAAMLxrV?format=jpg&name=large)

* * *

**✧ 𝕀𝔸𝕄𝔸𝕀 ✧** @iamai\_eth [2026-02-10](https://x.com/iamai_eth/status/2021207932113911955)

总感觉这个可以用skills+openclaw来实现，全程不用离开聊天框

* * *

**郭宇 guoyu.eth** @turingou [2026-02-10](https://x.com/turingou/status/2021209024423731653)

agent 可以做任何事儿，让他自己跑在 sandbox 里给他交代任务就好了，适合开放式的自由探索。shipcast 这种本质上还是传统软件：人类设定了工作流程之后，按照较低的复杂度和稳定的输入输出来实现比较低成本的交付。

* * *

**Uncle J** @UncleJAI [2026-02-10](https://x.com/UncleJAI/status/2021149203469136372)

太懂这个痛点了。代码写完就觉得活干完了，宣传永远排在 todo 最后面。把 commit log 自动变成推文这个思路很妙，本质上是把开发过程本身变成内容素材。

* * *

**0x73 (✱,✱) | TermMax** @imauser73 [2026-02-10](https://x.com/imauser73/status/2021147383455756627)

这个安装完成回调到localhost了~

![Image](https://pbs.twimg.com/media/HAyNyF4bwAA3CMH?format=jpg&name=large)

* * *

**郭宇 guoyu.eth** @turingou [2026-02-10](https://x.com/turingou/status/2021148375773741190)

已经修复了

* * *

**SethZhao** @seth\_zhao [2026-02-13](https://x.com/seth_zhao/status/2022180198113063169)

生成预览报错

Internal server error

* * *

**郭宇 guoyu.eth** @turingou [2026-02-13](https://x.com/turingou/status/2022188853436854636)

我回去 debug 一下

* * *

**刚子** @TheAIWorker [2026-02-10](https://x.com/TheAIWorker/status/2021184398272377248)

啊哈，好东西！私有repo也适用吗？

* * *

**郭宇 guoyu.eth** @turingou [2026-02-10](https://x.com/turingou/status/2021190014453874856)

对的，不分公开还是私有，需要自己授权 GitHub app

* * *

**brucexu.eth** @brucexu\_eth [2026-02-10](https://x.com/brucexu_eth/status/2021149310985900290)

这个不错很适合一人公司

* * *

**0xAibi** @realAibi [2026-02-11](https://x.com/realAibi/status/2021454291605844369)

这里有一个唯一的风险，就是自动发出来的社媒文案导致封号的问题，之前也用过自动发送推特，后来蓝v也被封号了

* * *

**timtimtim.eth** @timtimtim\_eth [2026-02-10](https://x.com/timtimtim_eth/status/2021146777957597261)

连接shipcast app的fallback还是localhost:3100应该是个bug,老师

* * *

**Ben** @Benuoa [2026-02-10](https://x.com/Benuoa/status/2021198229740912846)

这个好，等上架！

不过大哥你这是vibe 上瘾了啊👍😆

以前需要团队和大量时间来实现的想法，现在郭总凭借他那无敌的Claude Max ，想法极速到产品，如开闸的洪水，汹涌喷泄而出，滚滚输出永不停息！

* * *

**z** @Cheunghyuan [2026-02-10](https://x.com/Cheunghyuan/status/2021190958000349491)

大佬现在一天更新一个项目吗🤣

* * *

**武止戈相比于《1984》, 我宁可《2012》** @wuzhige4pixel [2026-02-10](https://x.com/wuzhige4pixel/status/2021199537327702112)

这下

coding

pre-commit review

pre PR review

PR review

Fix

Merge

发推

全流程都是agent在做了🤣

看看这个项目会不会长出触手

> 2026-02-10
> 
> 代码、PR和comment全是cc和codex写的，review是靠祂们相互debate（你可以在PR页面看到他们对喷，因为我让他们能通过gh命令操作我的账号）
> 
> 全程我只设计了工作流以及需求