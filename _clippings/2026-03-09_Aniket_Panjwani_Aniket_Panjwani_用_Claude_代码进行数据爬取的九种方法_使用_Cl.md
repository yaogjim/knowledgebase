---
title: "2026-03-09_Aniket_Panjwani_Aniket_Panjwani_用_Claude_代码进行数据爬取的九种方法_使用_Cl"
source: "https://x.com/aniketapanjwani/status/2029304239345017050"
author:
  - "[[@Aniket Panjwani]]"
published: 2026-03-09
created: 2026-03-09
description:
tags:
  - "x"
  - "@Aniket Panjwani"
  - "claude"
  - "code"
---

# Aniket Panjwani # 用 Claude 代码进行数据爬取的九种方法 使用 Cl

**Aniket Panjwani**

# 用 Claude 代码进行数据爬取的九种方法

使用 Claude Code 的最容易且最有用的任务之一是数据抓取。

然而，从 Claude Code 获取最佳数据抓取结果取决于给予它正确的提示以及获取正确的工具。

在本文中，我将详尽地介绍使用 Claude Code 抓取数据的九种不同方法。

## 这篇文章的视频版本

我在本文中讨论的所有内容也可以在以下 YouTube 视频中找到：https://youtu.be/4jQJdCfjPcw?si=Iv0F54vCa-JrdEUK

在视频中，我进行实时演示逐步讲解每个以下用 Claude Code 进行数据抓取的九种方法中的每一种，以便你能看到直接地它们是如何工作的。

## 方法 1：只需让 Claude Code 爬取该网站

对于大量网站，你只需告诉 Claude 代码爬取网站，告诉它你想要爬取什么数据，并要求它将数据输出到 CSV 或 SQLite 文件。

它会帮你在网站上四处探查，可能会编写一个 Python 脚本，运行这个脚本，甚至可能编写一些单元测试，然后把数据输出到你电脑上的某个位置。

## 方法 2: 请求 Claude Code 查找端点

很多有趣的数据不是以静态页面的形式呈现，而是通过某种 API 调用动态加载。有时 Claude Code 会自己对该 API 调用进行逆向工程，但有时你需要引导它并明确地告诉它：“嘿，比如找一个能展示酒店价格和预订数据的 API，你可能在写研究论文或进行竞争对手分析时会需要这些数据。”

之前的方法唯一的区别是，在这个方法中你要让它寻找端点。只给出那个词，那个小小的提示，有时会比你只是让它抓取网站得到更好的结果。

## 方法 3：ScrapeCreators

大多数社交媒体平台上都有大量可抓取的有用数据，但它们的端点特别难以逆向工程。

他们有自己的反机器人规则，并且每周都会更改选择器的工作方式。你可以让 Claude 代码或 Codex 不断尝试对它们进行逆向工程，但我喜欢做的是使用一个名为 Scrape Creators（https://scrapecreators.com/）

它拥有几乎所有社交媒体 API 的 API 端点。我建议为“抓取创作者”端点创建一个技能，作为一次性工具，这样你的智能编码工具将始终能够访问它。

## 方法 4: Apify Actor

Apify 是一个爬虫市场。对于很多难以抓取的网站，人们开发了可出租的爬虫，这些爬虫在 Apify 上可供使用（称为“actors”）。

那里有一个我喜欢用的抓取工具是 Google Maps 爬虫，它对社会科学家非常有用，无论是直接分析这些数据，还是创建替代指标。它也适用于商务人士进行竞争分析或寻找本地线索。

唯一的问题是你需要为这些付费。其中一些你按使用量付费，另外一些你需要按月租用。在有限的免费试用之后，你需要为 Apify 订阅付费，这与你使用基于使用量的 Apify actors 的情况有关。

## 方法 5: Firecrawl → Markdown → 结构化提取

你想要获取的大量数据不会是高度结构化的。

例如，当我在做我的 EconNow 项目时，我不得不爬取大量的经济学就业市场候选人页面。

> 我正在建立一个包含 2025-2026 年所有经济学博士就业市场候选人的数据库： https:// econ.now/candidates 到目前为止，18家机构和307名候选人 按机构/领域/导师筛选 简历、JMPs、候选人网站链接 将在接下来的几周内添加所有金融/经济候选人！
> 
> — Aniket Panjwani
> 
> [https://x.com/aniketapanjwani/status/1985418085269192720](https://x.com/aniketapanjwani/status/1985418085269192720)

这些页面中的每一个都有自己的 HTML 结构，因此我想要抓取它们的方式不是依赖于为每个网页编写单独的抓取程序。

相反，一种常见的技术是将网页转换为 Markdown 格式，然后让一个 LLM（比如 OpenAI 的 LLM）解析该 Markdown 并生成某种结构化输出。

Firecrawl 是一款可用于轻松将网页转换为 Markdown 的付费服务。

它也以开源项目的形式存在，但我看到的所有关于这个开源产品的信息都表明它很垃圾，所以对我来说，投资回报率足够高，我愿意自己付费使用 Firecrawl。

但基本上，当你有一个能将网页转换为 Markdown 的工具时，你就可以通过 API 将该 Markdown 传递给 OpenAI。如果你按照 API 期望的结构化输出格式正确设置你的结构化输出，你就能让 LLM 从这些不同的非结构化网站中解析出特定类型的字段。

## 方法 6: DIY HTML -> Markdown -> 结构化提取

现在，你可能会问我：嘿，笨蛋，你为什么要为 Firecrawl 付费？你自己不能把它转换成 Markdown 格式吗？

答案是，是的，你可以。也有一些工具能让你自己完成。

这里有一个：https://github.com/mixmark-io/turndown

这是另一个：https://github.com/microsoft/markitdown

我使用 Firecrawl 的原因是，我发现它能更好地处理某些边缘情况。它是一个设计得非常出色的服务，而且那些渐进式的改进对我来说是值得的。如果你预算有限，比如你是一名学者，你订阅了每月 20 美元的 Codex 服务，而这就是你所有的支出，那么绝对不要为 Firecrawl 付费。

直接使用其中一个软件包来代替，或者更准确地说，直接让 Claude Code 指向它并说：“嘿，把这个转换成 Markdown 格式，并且帮我用 OpenAI API 提取数据。”

现在，另一个需要指出的是，对于小规模任务，你甚至不需要将 Markdown 发送到外部 API 调用。你只需要让 Claude Code 或 Codex 本身进行结构化提取即可。

如果你的工作规模涉及数千或数万份文档，这会非常麻烦，不是你想做的事。

## 方法 7: yt-dlp

yt-dlp 是一个可以让你抓取任何 YouTube 视频、其元数据以及视频字幕的工具。

https://github.com/yt-dlp/yt-dlp

我基本上不再看视频了。我会直接下载字幕，然后让 Claude Code 或 Codex 为我生成个性化摘要，将视频内容应用到我真正关心的任何情境中。

在这个视频中，我使用 Claude Code 和 YTDLP 进行了一次实战练习，以逆向工程分析一位 AI YouTube 创作者的成功视频：https://youtu.be/rxQl4A9-dnk?si=o6PBkrGIBocakuzL

我制作那个 YouTube 视频只是随手为之，但我在那个视频中现场创作的成果，我实际上经常使用，来帮助我思考要制作哪些视频以及如何构思我的视频。

YouTube 视频中有大量有用的数据，我真的认为特别是这个工具高度未被充分利用。

## 方法 8：Reddit JSON 端点

Reddit 有一个 JSON 端点，可用于在其上查找几乎任何内容。

你只需在 Reddit URL 的末尾添加.json，然后你的代理式编码工具就可以以 JSON 文档的形式访问该部分 Reddit 上的所有内容。

例如，看看这个链接到 Claude Code 子版块的 JSON 端点。

https://old.reddit.com/r/claudecode.json

我有一些技能，基本上是用来掌握我关注的各种 subreddit 上人们在讨论什么。这些技能就是 Claude Code 或 Codex 调用 Reddit 的 JSON 端点。

## 方法9：代理浏览器 + 凭证

有很多网站受到某种认证的保护。为了通过该认证，你有两种可能的方法可以采用。

首先，你可以进行那个认证交换。然后，通过该交换，你有时会收到一个 cookie，该 cookie 会被存储在你的电脑上，然后 Claude Code 可以使用该 cookie 进行认证并查看已认证的视图。

另一个选择是使用 Vercel 的 Agent Browser 工具。

https://agent-browser.dev/

这是 Vercel 创建的浏览器自动化命令行界面，专为代理使用而优化。

对于小规模网页抓取，我一直更倾向于使用 Agent Browser。

例如，你可以将 Facebook 的登录凭证存储在某个 Claude Code 或 Codex 可以访问的地方，要么存储在某个你可以通过某种安全密钥交换机制访问的在线保险箱中，要么就随意地将其存储在终端的环境变量中或某个.env 文件里。

然后你可以创建一个技能，由 Claude Code 使用，该技能通过在 Agent Browser 中使用你的 Facebook 登录凭据登录，来抓取你所在的 Facebook 群组，然后进入 Facebook 群组，抓取所有帖子，并将这些数据写入到你希望的位置。

## 附言

我运营着一个由超过 1300 名 AI 开发者、商人和社会科学家组成的社区，他们致力于探索代理编码的前沿领域：https://www.skool.com/the-ai-mba

如果你对学习更多感兴趣，并且想要在社区中学习，那么你绝对应该加入！

* * *

### 热门回复

**@0xMarioNawfal** ♥ 13.8K · 💬 166

Anthropic 发布了一份 33 页的 Claude 技能提升速查表 https:// resources.anthropic.com/hubfs/The-Comp lete-Guide-to-Building-Skill-for-Claude.pdf …

**@Noisy** ♥ 8.2K · 💬 123

Anthropic 发布了一个预测市场交易机器人结构 每天300至1500美元 33 页的速查表，用于提升 Claude 技能，其中 2 页隐藏在一个交易胜率为 68.4%的交易机器人下面 如果我早点看到这些文件，我就会省去一些

**@GREG ISENBERG** ♥ 6.7K · 💬 281

我发现一个 GitHub 仓库，它可以让你快速搭建一个拥有 AI 员工的 AI 机构 工程师，设计师，增长营销人员，产品经理 每个角色以自身代理的身份运行，并且它们协调以交付想法 7 天内 10k+星标 1. 工程 (7个代理) 前端，后端

**@Nov 4, 2025** ♥ 442 · 💬 27

我正在建立一个包含 2025-2026 年所有经济学博士就业市场候选人的数据库： https:// econ.now/candidates 到目前为止，18家机构和307名候选人 按机构/领域/导师筛选 简历、JMPs、候选人网站链接 将在接下来的几周内添加所有金融/经济候选人！

**@anil kalm** ♥ 2 · 💬 1

兄弟，用 yt-dlp + Claude 的方法 7 被严重低估了。 你有没有把它对准更大的 经济相关的内容，比如完整的 NBER 夏季研讨会播放列表、研讨会系列，或者甚至是麻省理工学院开放式课程（MIT OpenCourseWare）、芝加哥大学（或其他地方）的旧讲座课程？不只是窥探 AI 领域的 YouTube 博主..