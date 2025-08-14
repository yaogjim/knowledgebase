---
title: "OpenRouter API 性能对比与使用体验分享"
source: "https://x.com/paulwalker99318/status/1955153786978308557"
author:
  - "[[@paulwalker99318]]"
published: 2025-08-14
created: 2025-08-14
description:
tags:
  - "@paulwalker99318 #翻译 #OpenRouter #GPT-OSS #Groq #Cerebras #模型选择"
---
**Bruce** @paulwalker99318 [2025-08-12](https://x.com/paulwalker99318/status/1955153786978308557)

使用的主力翻译模型改成了gpt-oss-120b，原因是翻译效果更好、价格实惠、速度更快、延迟更低。此前用的是更便宜的qwen/qwen3-235b-a22b-thinking-2507，之所以切换，主要是发现qwen-3在翻译Agent/Agentic相关的技术文档时效果不够好，不如gpt-oss-120b。

OpenRouter上有十几家API供应商，价格、上下文、延迟、速度都有差异。OpenRouter官方说的是自动路由到最优的厂商，但实际上看了一下，调用的随机概率很大。

虽然Cerebras的速度遥遥领先，但实际调用的结果是Groq更快，能到2110 tokens/s，延迟也更低。综合下来还是Groq最强。

![Image](https://pbs.twimg.com/media/GyIXpmtaEAIAIRW?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/GyIYOeaaoAAjFlt?format=jpg&name=large)

---

**Bruce** @paulwalker99318 [2025-08-13](https://x.com/paulwalker99318/status/1955432724950642992)

补充：截图没说清楚，图 1 是调用OpenRouter API的真实数据，图 2 是OpenRouter模型详细给出的理论性能。Cerebras的峰值比较高，但使用下来Groq能稳定在500+ tokens/s。

另外：gpt-oss-120b似乎与GPT-5类似，对prompt非常敏感，所以大家使用的时候可能要注意，prompt不是越多越好，也不是越详细越好。

---

**Bruce** @paulwalker99318 [2025-08-13](https://x.com/paulwalker99318/status/1955527246325969086)

在OpenRouter上选模型要小心，可能贵10倍！

models页面的票价像极了某宝的套路，标的往往是最低价格，但实际上你使用的往往是随机路由的。

以 DeepSeek-R1 0528 为例（目前看到差价最大的）：

\- models页面标价：input 0.18$, output 0.72$

\- 实际调用的价格可能是8$, 贵了整整10倍！

![Image](https://pbs.twimg.com/media/GyNs_ljaEAAdP0n?format=jpg&name=large)

---

**DeGao** @MrDeGao [2025-08-12](https://x.com/MrDeGao/status/1955301727210705301)

我做了DLM，扩散，可以到2800 Tps，是不是可以蒸馏下120b？

---

**Bruce** @paulwalker99318 [2025-08-12](https://x.com/paulwalker99318/status/1955302347187556567)

🐮 在什么显卡上跑的？

---

**Michael Anti** @mranti [2025-08-13](https://x.com/mranti/status/1955450854980669498)

qwen3-235b-a22b-thinking-2507是thinking模式，本身就是慢响应的，qwen3-235b-a22b-2507这个才快。

---

**Bruce** @paulwalker99318 [2025-08-13](https://x.com/paulwalker99318/status/1955465165295775858)

好像打错了，就是非思考模型。速度跟gpt-oss还是差一些

---

**akazwz** @akazwz\_ [2025-08-12](https://x.com/akazwz_/status/1955218042302107720)

Grok is too fast!  
Grok 速度太快了！

---

**Bruce** @paulwalker99318 [2025-08-12](https://x.com/paulwalker99318/status/1955236172965482928)

是的，cerebras官网的速度也能到2000 tokens/s，但是API没那么快

---

**Denis Wang** @wangyg [2025-08-12](https://x.com/wangyg/status/1955337748736512087)

Groq也不能绑定大陆的信用卡吧？

---

**Bruce** @paulwalker99318 [2025-08-12](https://x.com/paulwalker99318/status/1955412008041582706)

用的OpenRouter API  
使用的 OpenRouter API

---

**Tom Q** @TomQ296214 [2025-08-13](https://x.com/TomQ296214/status/1955437942069178821)

qwen-mt和gpt-5-nano对比过吗，哪种会更好呢

---

**Bruce** @paulwalker99318 [2025-08-13](https://x.com/paulwalker99318/status/1955468953364599013)

qwen-mt没试过，不过既然是翻译专用模型，效果应该不差。gpt-5-nano效果还行，看价格和定位应该是用于取代gpt-4.1-mini的，与gemini-2.5-flash-lite相当，一般的翻译场景够用了。

---

**老鬼** @laogui [2025-08-12](https://x.com/laogui/status/1955296940998205929)

翻译几十 b 就够了，主要看并发限制

---

**Bruce** @paulwalker99318 [2025-08-12](https://x.com/paulwalker99318/status/1955412637115990261)

不同场景的翻译质量要求也不一样，我翻译网面的时候用mini或者Dia浏览器默认的chatgpt-4.1，技术文档的翻译会用好的模型以追求更好的效果。

---

**RockCat** @HunterRockCat [2025-08-13](https://x.com/HunterRockCat/status/1955430875291877827)

客户端用什么？

---

**Bruce** @paulwalker99318 [2025-08-13](https://x.com/paulwalker99318/status/1955464785945878583)

用的沉浸式翻译（虽然最近闹了点风波，但还是很推荐）

---

**Li God** @rx541359627 [2025-08-12](https://x.com/rx541359627/status/1955306751345168475)

gpt-oss-120b有deep seek-v3好吗？  
gpt-oss-120b 比深寻 v3 好吗？

---

**Bruce** @paulwalker99318 [2025-08-12](https://x.com/paulwalker99318/status/1955411865120678001)

主观感觉是略好于deepseek-v3，OpenAI的模型做翻译都不错，而且速度比deepseek-v3快多了。

---

**就这样** @zhaogua61654931 [2025-08-12](https://x.com/zhaogua61654931/status/1955194539653861644)

qwen3里处理文字最好的是30B的模型，你可以试试，235B比较偏向深度技术向了，越是技术问题越好用，闲聊和翻译这种任务不如30B

---

**Laisky** @LaiskyCai [2025-08-13](https://x.com/LaiskyCai/status/1955462109040652636)

我最近也很喜欢这个模型，实在太快了，开着深度思考，上千 tokens 也能在 1s 内响应。

![Image](https://pbs.twimg.com/media/GyMyS1IaEAUtY69?format=jpg&name=large)

---

**notice\_u** @ID\_CKChen [2025-08-12](https://x.com/ID_CKChen/status/1955351174154162351)

@readwise save thread  
@readwise 保存线程

---

**Whitmore** @zhaopengme [2025-08-13](https://x.com/zhaopengme/status/1955466511591813435)

qwen4b那个挺不错的

---

**isaced** @isacedx [2025-08-13](https://x.com/isacedx/status/1955560566816415791)

有试过 qwen-mt 翻译模型吗

---

**Zynelia** @Zyneliaofficial

Built to withstand endless playtime and tough chewing adventures.

Order: https://zynelia.com/ONSY?twclid=22or1yj7uind3r9b72otx1p12  
专为承受无尽的玩耍时间和激烈的啃咬冒险而设计。

订单： https://zynelia.com/ONSY?twclid=22or1yj7uind3r9b72otx1p12