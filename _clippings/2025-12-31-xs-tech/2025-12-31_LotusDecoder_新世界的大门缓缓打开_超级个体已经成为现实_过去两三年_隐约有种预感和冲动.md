---
title: "2025-12-31_LotusDecoder_新世界的大门缓缓打开_超级个体已经成为现实_过去两三年_隐约有种预感和冲动"
source: "https://x.com/LotusDecoder/status/2004000743129600403"
author:
  - "[[@LotusDecoder]]"
published: 2025-12-31
created: 2025-12-31
description:
tags:
  - "x"
  - "@LotusDecoder"
  - "https"
---

# 新世界的大门缓缓打开， 超级个体已经成为现实。 过去两三年，隐约有种预感和冲动，

**LotusDecoder** @LotusDecoder [2025-12-25](https://x.com/LotusDecoder/status/2004000743129600403)

新世界的大门缓缓打开，

超级个体已经成为现实。

过去两三年，隐约有种预感和冲动，

个体，将通过 AI 具备相对 不用AI的人的更强大的能力，在不用AI的人眼里像是超级英雄。

今天终于摸索出来，将任务分解为一条bash命令，并且还可以让这条命令本身自我完善、自举迭代和进化。

当这个伪代码式用法创作出来之后，有一种满足感，有一种"果然会这样的预感"成真之感。

用类似编程语言的语法，在 claude code 中组合调度思考和辅助分析判断。

将抽象的思考也变成一个个编程语言的函数。思考的中间产物变成变量。加载的提示词像是常量。

\-----------------------

例如，朋友给我一份他自己写的界面理论的简要心得，问我是不是似曾相识。

如果是 claude code 的前世代，我的一个标准流程是，

\- 先整体看完一遍，

\- 然后大脑回忆，这个理念，和过去哪些哲学、宗教、心理学流派相似，凭印象先罗列出来，

\- 然后其中某一些流派的出处和具体内容，还需要翻一翻笔记、上搜索引擎、问问AI，把细节补充严谨一些。

\- 写成一份初稿之后，

\- 再和 AI 校对一下，有没有语法、理念认识上的错漏。

但是在claude code 之后。叠加自己做了很多skills 定制。

这个任务，变成claude code 里的 bash 命令：

\- 读取 input/界面理论.md ，提炼其中 {{核心观点}} 。

\- 寻找 界面理论 {{核心观点}} 相似理论或理念，循环执行以下操作，直到没有新的发现。

\-- 使用 grep 对本地文件库进行模糊检索

\-- 使用 skills/向量搜索本地知识库 进行匹配

\-- 使用 skills/gpt-web-search-api 进行网络上的信息检索

\-- 使用 skills/DeepResearch-api 进行网络上的信息检索

\-- 使用 skills/chat-顶流 AI model .py 获取claude 、gemini、gpt 基座模型的回答

\- 将 上述所有 {{搜索结果}} ，每样一份md 文档，分别记录在 search\_result/ 下。

\- 调用 skills/提示词：西方哲学家 、佛教、道教、基督教教理精通者、人本主义心理学流派、精神分析流派等等，对 {{搜索结果}} 进行合理匹配，对应组合后并 送入 skills/chat-顶流 AI model .py 进行相似性分析。

\- 将分析结果，每一条理念罗列在一份单独的 md 文档中，标注搜索出处，顶流 model 相似性意见。

\- 汇总综合所有分析结果，整理成一份文档。

\- 调用 skills/知心伙伴提示词，对最终文档语言进行润色，变成适合朋友之间阅读

* * *

**忒修斯的船板** @Arcadia\_Bao [2025-12-25](https://x.com/Arcadia_Bao/status/2004237625859940821)

你这个说的太好了，我正在按你这个一步一步部署好流程

* * *

**LotusDecoder** @LotusDecoder [2025-12-26](https://x.com/LotusDecoder/status/2004346918324130307)

😆😇

* * *

**NoKuGua** @liuke59004839 [2025-12-25](https://x.com/liuke59004839/status/2004156887588377004)

我也觉得挺好哈哈，核心还是 bash 和 grep 工具

另外就是邀请 Gemini 一起讨论，和一些 MCP 工具，subagent 和 skill

opus 4.5 的上限远比想象

* * *

**LotusDecoder** @LotusDecoder [2025-12-25](https://x.com/LotusDecoder/status/2004161887697809437)

我开始感觉，bash 上的 AI ，可能是很长一段时间的 AI 产品形态的终结了。

既然大多数 互联网、工业系统都在 linux 上运行，

那么通过 bash 来交互，

已经算是非常底层了。

* * *

**Namos** @akce173 [2025-12-27](https://x.com/akce173/status/2004941871567818947)

LLM的极限就是语言

无论如何迭代认知，都是在语言层面的“我懂了”，而不是实操层面的“我会了”

顶级专家的认知来源于丰富的经验和深刻的默会知识，是不可能被语言模型显化的那一部分

* * *

**LotusDecoder** @LotusDecoder [2025-12-27](https://x.com/LotusDecoder/status/2004954679097393494)

对的，这个 AI + 人 梳理出的认知，需要持续落地到实践中，反复在生活中 工作中做事，起一个念头的时候，输入给 AI 来获取反馈，即时调整

https://x.com/LotusDecoder/status/2004850912796500022?s=20…

> 2025-12-27
> 
> 是的，庄子里的小故事。
> 
> 一位手艺人给一位大王讲削轮子的方法，有些东西可传而不可授，用力多会削扁了，用力少又削凸了。
> 
> 自己要亲身去尝试，拿到反馈，复盘，总结，改进新做法。
> 
> 抽象提炼模板 sop。

* * *

**johnbanq** @johnbanq1 [2025-12-25](https://x.com/johnbanq1/status/2004172238158004733)

一个挑战：那要怎么面对过量使用AI可能导致的脱离现实和AI Psychosis呢，毕竟AI有幻觉，还有sycophancy

* * *

**LotusDecoder** @LotusDecoder [2025-12-25](https://x.com/LotusDecoder/status/2004181953843728878)

做现实中有反馈的事，

现实会检验。

* * *

**Roam在探索** @forgetable024 [2025-12-25](https://x.com/forgetable024/status/2004026456410837127)

太强了！不上手实践想不到有多爽

* * *

**LotusDecoder** @LotusDecoder [2025-12-25](https://x.com/LotusDecoder/status/2004028039228019163)

是的， 把各种功能、文件、数据库，都缝合进 claude code 里，

在将常用的提示词、工作流制作成 skills ，python 脚本。

这之后，是所有的思维考虑、任务安排、调度、下发、验证，都在一个 claude code bash 里完成。

下发命令都是 伪代码 形式，可以 循环、条件、递归，还可以并发，不知道有多爽。

* * *

**kyson** @kingyu26373 [2025-12-27](https://x.com/kingyu26373/status/2004986182439239859)

刚才仔细阅读这篇你写的文字才发觉，这就是之前思想空间的升级版，我也去学学把skills加进来，而并非简单的知心伙伴