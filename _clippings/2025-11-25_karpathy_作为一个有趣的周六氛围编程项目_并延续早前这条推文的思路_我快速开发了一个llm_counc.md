---
title: "2025-11-25_karpathy_作为一个有趣的周六氛围编程项目_并延续早前这条推文的思路_我快速开发了一个llm_counc"
source: "https://x.com/karpathy/status/1992381094667411768"
author:
  - "[[@karpathy]]"
published: 2025-11-25
created: 2025-11-25
description:
tags:
  - "x"
  - "@karpathy"
  - "https"
  - "2025-11-23"
---

# 作为一个有趣的周六氛围编程项目，并延续早前这条推文的思路，我快速开发了一个llm-counc

**Andrej Karpathy** @karpathy 2025-11-18

作为一个有趣的周六氛围编程项目，并延续早前这条推文的思路，我快速开发了一个\*\*llm-council\*\*网页应用。它的界面与 ChatGPT 完全一样，但每个用户查询会：1）通过 OpenRouter 分派给你顾问团中的多个模型处理，例如当前配置为"openai/gpt-5.1"。

"google/gemini-3-pro-preview",

"anthropic/claude-sonnet-4.5"

"x-ai/grok-4"模型，随后 2）所有模型都能看到彼此（匿名化）的响应，并进行审阅和排名，接着 3）一位"主席 LLM"会汇总所有信息作为上下文，生成最终回应。观察多个模型对同一查询的并列结果颇为有趣，而阅读它们相互评价和排名的过程则更显妙趣横生。这些模型往往出人意料地愿意选择其他 LLM 的响应优于自己，这使得该策略成为更广义上有趣的模型评估方法。例如，今日与我的 LLM 委员会共读图书章节时，各模型一致称赞 GPT 5.1 为最具洞见的最佳模型，同时始终将 Claude 评为最差模型，其他模型则浮动于中间区间。但我并不完全认同这种评价与我的质性判断相符。就质性而言，我发现 GPT 5.1 略显冗长铺陈，而 Gemini 3 则更为凝练精悍。Claude 在此领域则过于简略。不过，LLM 委员会的数据流设计确实存在广阔的探索空间。LLM 集成系统的构建似乎尚未得到充分发掘。我已将氛围编码应用推送至

https://github.com/karpathy/llm-council…

如果其他人也想参与。感谢 nano banana pro 为仓库提供了有趣的标题图片。

> 2025-11-18
> 
> 我正逐渐养成用 LLMs 阅读所有内容（博客、文章、书籍章节等）的习惯。通常第一遍是手动阅读，第二遍进行"解释/总结"，第三遍问答。最终我的理解往往比直接跳过更深入透彻。这已逐渐成为我最常用的场景之一。
> 
> 开启
> 
> ![Image](https://pbs.twimg.com/media/G6ZZO7ragAAtnCZ?format=jpg&name=large)
