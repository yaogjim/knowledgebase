---
title: "2026-06-16_tobi_车间学习"
source: "https://x.com/tobi/status/2053121182044451016"
author:
  - "[[@tobi]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "#tobi"
  - "#help"
  - "x"
  - "@tobi"
---

# 车间学习

**tobi lutke**

# 车间学习

Years ago I wrote about my

[apprenticeship in Germany](https://tobi.lutke.com/blogs/news/11280301-the-apprentice-programmer). I dropped out of school at 16 and went to work at a Siemens subsidiary, where the most interesting people sat in the basement and used Delphi instead of the corporate-mandated Rosie SQL (both pretty much lost to time and progress). I learned to be a programmer by watching them. By making them coffee. By hanging around long enough that their judgment seeped into mine.

过去一年里，我一直在思考那段经历，因为我们在 Shopify 构建了一个遵循同样原理的东西。

她名叫 River。River 是一个驻留于我们公司 Slack 中的 AI 代理。你可以像与队友交流一样与她对话：只需在 Slack 频道中提及 River 即可。她可以阅读代码、运行测试、编写代码、提交拉取请求、查询我们的数据仓库、查看生产追踪，以及更多其他功能。我们会频繁使用她。

在过去 30 天里，5,938 名 Shopify 员工在 4,450 个不同的 Slack 频道中与 River 合作。仅上周就向我们的主 monorepo 提交了 1,870 个拉取请求。上周合并到我们代码库中的拉取请求中，大约每八个就有一个是由 River 创建并由我们审核的。

目前世界上有很多编码代理。让 River 与众不同的是一个限制条件： 她只在公开环境中工作。

## 一个约束成为了一个功能

当我们开始开发 River 时，最明显的做法是让人们私下使用她。这就是许多其他 AI 助手的工作方式。ChatGPT 是一个私密窗口。Claude 是一个私密窗口。Cursor 是在你和 IDE 之间。

我们做了相反的决定。River 使用 Slack（我们公司的聊天工具）。River 不会回复私信。她礼貌地拒绝了，并建议创建一个公共频道，以便你和她开始合作。我自己和 River 在

[#tobi\_river](https://x.com/search?q=%23tobi_river&src=hashtag_click) 频道中，许多人都效仿了这种模式。因此，所有对话都是可搜索的。Shopify 的任何人都可以参与进来。在我自己的频道中，有超过 100 个人，他们对线程做出反应、增添色彩和补充背景、接过接力棒、帮忙进行评审、提醒我自己有多生疏，而且重要的是，从观察中学习。

这一开始很奇怪。人们习惯了带有自己工具的私密工作空间。当整个公司都能看到这个问题时，寻求帮助的感觉就不一样了。但发生了一件我们期望的事情，只是没有完全预料到其影响：

人们开始互相学习。

A support engineer in

[#help\_checkout](https://x.com/search?q=%23help_checkout&src=hashtag_click) would watch a backend engineer in another channel get River to find the right log query, and the next day she would do the same thing. A new hire would scroll back through

[#river](https://x.com/search?q=%23river&src=hashtag_click)

to see how senior people scope a request before they ever sent their first one.

和德语中常有的情况一样，德语里有一个词可以形容这种环境：Lehrwerkstatt。字面意思是：教学车间。整个车间就是教室。你通过接触工作来学习。持续学习是公司的核心价值观之一。

Shopify 希望成为一个规模化的学习工坊，而 River 现在让我们比以往任何时候都更接近这一理想。这是一种渗透式学习，因为它不需要课程、培训计划或管理者。它只需要每个人的工作尽可能地被充分展示，每个人都从彼此身上学习。

我由衷地对这个有点意外的发现感到兴奋，所以想分享一下。

## 为什么在 AI 背景下，这一点更重要，而非更不重要？

关于人工智能的一个常见担忧是，它会让人们停止思考。如果 AI 替他们完成调试，初级开发者为什么还要学习调试呢？如果他们可以直接询问，为什么还要阅读代码库呢？

我认为担忧是真实的，但表述方式错了。风险不在于 AI 完成工作，而在于 AI 完成工作后我们却从未从中学习。如果与代理的每次交互都在私有窗口中进行，那么唯一能学到东西的人是键盘前的那个人。其他人则被排除在学徒过程之外。

当人们与他们的代理在公共场合协作时，情况则相反。最佳提示模式传播开来，知识也随之传播。一名开发人员调查 Slack 权限漏洞的巧妙方法，成为了其他人调查时的模板。有人编写的用于向 River 讲解公司结账数据仓库的技能，被另外十二个团队复用。River 自己也学到：每个频道都可以预加载其团队所需的区域、技能和指令，这些内容由最接近工作的人员编写。River 的记忆系统也在不断学习和摒弃关于公司及最佳工作方法的关键信息。

代理不会取代学徒，也不会取代导师。代理让整个公司都成为学徒，因为每个人都在不断观察最有经验的人与代理并肩工作。

这也是合并率持续攀升的原因。我们没有重新训练模型，也没有更换模型。两个月内从 36%提升至 77%的改进，源于人们观察 River 的工作过程，发现它在哪里卡壳，记录下它本应知道的内容，并帮助 River 自身成为更好的伙伴。每个团队积累的经验流入代理中，这个代理在 Shopify 相关工作中变得更擅长。

## 公司以其最慢环节的速度前进

当我思考为什么这很重要时，这又回到了我长期以来一直坚信的一点：一个组织的速度由其带宽最低的沟通渠道和节奏决定。会议很慢，电子邮件很慢，私人私信也很慢。这可能对参与其中的个人来说不是问题，但对整个组织而言却是如此。从这些沟通中产生的信息和决策，如果没有大量额外的沟通努力，永远无法完全扩散到组织的其他部分。

人与人之间或与有能力的代理进行的公开对话并非那些（事物）。它是快速的、可搜索的、可教授的，并且会累积。下一个有相同问题的人不必再问。

[人类卓越的未来角色](https://tobi.lutke.com/blogs/news/the-future-role-of-human-excellence)

那就是 River。这是我们的教学工坊。

* * *

### 热门回复

**@Polymarket** ♥ 8.0K · 💬 708

BREAKING: JESUS CHRIST RETURNING THIS YEAR?

4% chance. The odds have risen.

**@AvenorUs** ♥ 676 · 💬 17

Avenor — the most powerful AI agent you’ll ever use, installed in one click. From planning your day and handling everyday tasks to generating photos and videos, it does it all in one place.

**@tobi lutke** ♥ 91 · 💬 14

我刚刚把这篇帖子分享给 river，想看看她的想法。这是她的反应。

**@tobi lutke** ♥ 64 · 💬 2

是的，按频道+人员+区域基于 qmd

**@LovartAI** ♥ 39 · 💬 0

专业级影像生成，让创意精准落地

最强推理引擎赋能，告别“抽卡式”绘图。稳定输出高保真杰作，撑起你的每一个大胆创意。

点击查看详情，领取您的视觉武器。