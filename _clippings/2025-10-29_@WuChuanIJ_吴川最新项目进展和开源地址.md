---
title: "吴川最新项目进展和开源地址"
source: "https://x.com/WuChuanIJ/status/1982991392340422740"
author:
  - "[[@WuChuanIJ]]"
published: 2025-10-29
created: 2025-10-29
description:
tags:
  - "@WuChuanIJ #吴川 #微软 #RD-Agent #Qlib #LightGBM #LLM #DeepSeek #数据处理 #机器学习 #投资策略"
status: "inbox"
importance: 2
effort: 2
review_level: 0
review_next: "2025-11-13"
review_interval: null
review_count: 0
decision: null
topics: []
links_out: []
summary: ""
pov: ""
actions: []
---
**吴川** @WuChuanIJ [2025-10-28](https://x.com/WuChuanIJ/status/1982991392340422740)

部署基本完成了，剩下的就是继续训练数据源以及调试工作；

总结下：

1.数据源+清洗+格式转换

2.部署D/R Agent+Qlib+Alpha158特征+LightGBM

3.通过模型训练历史数据

4.训练好的数据参数给LLM

5.优化调参继续用模型跑数据，很费时

6.调下LLM分析实时获取的新闻+股评+人气榜+资金流等

7.重复循环♻️

![First image displays technical text in Chinese listing Qlib data processing steps including cleaning format conversion deployment of Alpha158 features with LightGBM model training on historical data parameter passing to LLM optimization tuning for running data LLM analysis of real-time news stock reviews popularity lists fund flows and iterative loops with metrics RMSE 0.022663 IC 0.586026 mentioning DeepSeek data cleaning deployment. Second image shows structured tables in Chinese with checkmarks detailing DeepSeek data processing steps for 10% 19% 30% features including data cleaning feature engineering and model training across different percentages like 10% 19% 30% up to 50% with sections for various processing stages.](https://pbs.twimg.com/media/G4T9zaKbUAA2An7?format=png&name=large) ![First image displays technical text in Chinese listing Qlib data processing steps including cleaning format conversion deployment of Alpha158 features with LightGBM model training on historical data parameter passing to LLM optimization tuning for running data LLM analysis of real-time news stock reviews popularity lists fund flows and iterative loops with metrics RMSE 0.022663 IC 0.586026 mentioning DeepSeek data cleaning deployment. Second image shows structured tables in Chinese with checkmarks detailing DeepSeek data processing steps for 10% 19% 30% features including data cleaning feature engineering and model training across different percentages like 10% 19% 30% up to 50% with sections for various processing stages.](https://pbs.twimg.com/media/G4T91YoasAANcSx?format=jpg&name=large)

---

**tianzhe** @qq9888 [2025-10-28](https://x.com/qq9888/status/1983026459641028679)

厉害，会开源啊？

---

**吴川** @WuChuanIJ [2025-10-28](https://x.com/WuChuanIJ/status/1983047002796789780)

这个本来就是开源的。翻下评论 我发了地址的

---

**Clark** @yf\_clark [2025-10-28](https://x.com/yf_clark/status/1983180547699683388)

新闻源非常重要，很多都是噪音新闻没有交易的价值

---

**吴川** @WuChuanIJ [2025-10-28](https://x.com/WuChuanIJ/status/1983181505640948146)

有推荐吗

---

**周末出走马** @gymayong [2025-10-28](https://x.com/gymayong/status/1983076880694804846)

评论没看到地址～

---

**吴川** @WuChuanIJ [2025-10-28](https://x.com/WuChuanIJ/status/1983083658488754260)

https://github.com/microsoft/RD-Agent…  
https://github.com/microsoft/RD-Agent…

> 2025-10-28
> 
> https://github.com/microsoft/RD-Agent…  
> https://github.com/microsoft/RD-Agent…

---

**wbdu** @wbdu [2025-10-28](https://x.com/wbdu/status/1983003357712396421)

真够快的，顶一个

---

**吴川** @WuChuanIJ [2025-10-28](https://x.com/WuChuanIJ/status/1983004159319433523)

数据没有训练完 😂 设备扛不住了

---

**Adam Voulstaker** @AdamVoulstaker [2025-10-28](https://x.com/AdamVoulstaker/status/1983098789096530100)

why is everyone giving the data to the LLM?

Why?

If your strat is all of the above you dont need an LLM to mess it up.  
为什么大家都在把数据交给 LLM？

为什么？

如果你的策略包含以上所有内容，那就不需要让 LLM 来搅局了。

---

**吴川** @WuChuanIJ [2025-10-28](https://x.com/WuChuanIJ/status/1983099974595543236)

有道理

---

**Don** @Don\_Builds [2025-10-29](https://x.com/Don_Builds/status/1983404246096900135)

没啥用

---

**吴川** @WuChuanIJ [2025-10-29](https://x.com/WuChuanIJ/status/1983428181458866372)

好的

---

**维恩0xWayne** @0xWayne\_light [2025-10-28](https://x.com/0xWayne_light/status/1983172113369604578)

数据源挺重要

---

**吴川** @WuChuanIJ [2025-10-28](https://x.com/WuChuanIJ/status/1983178998088904816)

是的

---

**demonfei** @demonfeifei [2025-10-28](https://x.com/demonfeifei/status/1983010722503373184)

用的什么设备3080ti能跑起来吗

---

**吴川** @WuChuanIJ [2025-10-28](https://x.com/WuChuanIJ/status/1983013428852863036)

可以的 把内存搞到128去 可以训练深度模型。我设备不行

---

**kk** @kkzhang888 [2025-10-28](https://x.com/kkzhang888/status/1983016151958589483)

你的训练周期是多久？是用的动态股票池吗？

---

**吴川** @WuChuanIJ [2025-10-28](https://x.com/WuChuanIJ/status/1983022811334713835)

搞了近两天，历史数据训练的

---

**Cuper.base.eth|RIVER** @777seeyou [2025-10-28](https://x.com/777seeyou/status/1983109045398712762)

加密货币还是股票？

股票还好 。加密波动太快 热点还没抓住就过了

---

**吴川** @WuChuanIJ [2025-10-28](https://x.com/WuChuanIJ/status/1983118380338229683)

股票

---

**newboy** @newboy518 [2025-10-28](https://x.com/newboy518/status/1983000402460299645)

如果使用llm进行新闻等数据向量化，如果进行历史数据的回测和训练？

---

**吴川** @WuChuanIJ [2025-10-28](https://x.com/WuChuanIJ/status/1983002358956355800)

LLM是最后了 训练和回测在前

---

**Xi** @Xi85063215 [2025-10-28](https://x.com/Xi85063215/status/1983114619423248770)

总共多少数据量？

---

**吴川** @WuChuanIJ [2025-10-28](https://x.com/WuChuanIJ/status/1983118346532073484)

1分钟数据2亿多行

---

**Starlink** @Starlink

Get connected with fast, reliable internet for streaming, video calls, online gaming and more.

Speeds up to 400+ Mbps.

Order online in minutes.  
连接高速可靠的互联网，尽享流畅的影音串流、高清视频通话、畅快在线游戏等丰富体验。

速度高达 400+ Mbps。

几分钟内在线下单。