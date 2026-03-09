---
title: "2026-03-09_卡尔的AI沃茨_卡尔的AI沃茨_高级OpenClaw第一步_先用12个Skills把联网搜索做到极致_Ope"
source: "https://x.com/aiwarts/status/2028841164418494872"
author:
  - "[[@卡尔的AI沃茨]]"
published: 2026-03-09
created: 2026-03-09
description:
tags:
  - "x"
  - "@卡尔的AI沃茨"
  - "clawhub"
---

# 卡尔的AI沃茨 高级OpenClaw第一步！先用12个Skills把联网搜索做到极致 Ope

**卡尔的AI沃茨**

高级OpenClaw第一步！先用12个Skills把联网搜索做到极致

OpenClaw从中级到高级第一步不是做龙虾分身，先把联网搜索做到极致，把X，某站，某书，播客，公众号，Reddit啥的全都解析明白，再把Deep Research装上，再加上主动订阅的信息源和OpenRouter免费兜底的大模型，这应该是目前云上OpenClaw在不方便文件互传的情况下的最佳搭配方案。

一键安装的命令我整理到最后了。

OpenClaw目前内置的联网搜索是Brave和Perplexity，一个要绑卡一个要付费。

所以我们直接先换成Tavily和Multi Search Engine v2.0.1，

\- Tavily每月1000次免费调用，不用绑卡。好处就是它本身就是专门给Agent做的搜索API，返回的内容处理过了。

\- Multi Search Engine集成了17 个搜索引擎（8个中文+9个全球），不需要API，安装的时候把搜索规则记下就行

但总有些难啃的链接，公众号，某书，某X的不好解析，这段时间我还装了Agent Reach和x-reader，

它们覆盖的平台是有重复的，为了安全性会在本地安装一个docker虚拟机来模拟操作，

\- x-reader能覆盖yt，某站，X，公众号，tg，rss，播客，某书 - Agent Reach在x-reader的基础上多了某抖，Reddit，Github，优先用Cookie登陆不需要扫码，但我还是建议用小号。

还有一类是需要浏览器自动化的， 比方说点击确定，滑动页面，一般来说是用Playwright，

但我发现了更好用的， BrowserWing可以记录浏览器的操作做成Skills，下次再用就可以精确重放了。

如果有一个gemini账号，还可以安ModSearch和Gemini Deep Reserach，

\- ModSearch把gemini cli做成了联网搜索，Google的信息搜索本来就很强，不是反代，没有风险。 - Gemini Deep Reserach就相当于把Gemini的Deep Research能力搬到OpenClaw里面了，还是Gemini 3.1 Pro驱动的。

还有三个比较特别的， find-skills，Clawhub和ClawFeed find-skills和Clawhub都是让OpenClaw遇到问题主动找合适的Skills的。

把ClawFeed放在这里因为它相当于是一个被动更新的信息源，可以订阅X，RSS，HackerNews，Reddit和GitHub Trending，4个小时更新一次。

最后加个Free Ride， 很多朋友虽然已经开始用API了，但没有做额度管理，如果当时在跑一个很长的任务的话，因为速率限制直接就废了。Free Ride相当于调用了OpenRouter上的免费模型，它自动就按照质量排名了，这样的话我们不需要担心openclaw半夜停了。

（1/2）

* * *

### 热门回复

**@卡尔的AI沃茨** ♥ 52 · 💬 0

直接给你的openclaw发， 帮我安装这个skillsgithub链接就好了。 Clawhub https:// clawhub.ai npm i -g clawhub Tavily 如果你的openclaw是新的，没有联网，可以先把tavily搭起来。 clawhub install tavily-search Agent-Reach https:// github.com/Panniantong/Ag ent-Reach?tab=readme-ov-file … ClawFeed

**@王柯基** ♥ 0 · 💬 1

昨天全程看了直播，很多干货哇。想问下最后您提到的有很多免费模型，可以给openclaw用作兜底的是哪个网站？

**@卡尔的AI沃茨** ♥ 0 · 💬 1

是clawhub里的free ride

**@hooray** ♥ 0 · 💬 1

@readwise save thread @readwise 保存线程

**@Half 慢半拍** ♥ 0 · 💬 0

补一点：ClawFeed的4小时更新频率对追热点来说还是慢了，建议高频关注的源单独用RSS轮询。