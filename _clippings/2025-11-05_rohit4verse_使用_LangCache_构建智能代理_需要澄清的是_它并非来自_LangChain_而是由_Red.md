---
title: "2025-11-05_rohit4verse_使用_LangCache_构建智能代理_需要澄清的是_它并非来自_LangChain_而是由_Red"
source: "https://x.com/rohit4verse/status/1985704039200538916"
author:
  - "[[@rohit4verse]]"
published: 2025-11-05
created: 2025-11-05
description:
tags:
  - "x"
  - "@rohit4verse"
  - "https"
  - "2025-11-04"
---

# 使用 LangCache 构建智能代理。需要澄清的是，它并非来自 LangChain，而是由 Red

**Rohit** @rohit4verse [2025-11-04](https://x.com/rohit4verse/status/1985704039200538916)

使用 LangCache 构建智能代理。需要澄清的是，它并非来自 LangChain，而是由 Redis 开发，专为生产级记忆与召回设计。LangChain 内置缓存主要基于文本精确匹配，而 Redis LangCache 则采用语义缓存技术——它根据语义而非完全相同的字符串进行召回。

其核心运作原理如下：

\> 用户向 AI 应用发送提示词

\> 应用通过 POST /v1/caches/{cacheId}/entries/search 接口将提示词发送至 LangCache

\> 系统调用嵌入模型为提示词生成向量

\> 基于这些向量在缓存中搜索语义相似的条目

\> 若找到匹配项（缓存命中）：LangCache 立即返回缓存的响应

\> 若无匹配项（缓存未命中）：应用将调用 LLM 获取新响应，并通过 POST /v1/caches/{cacheId}/entries 接口回存至系统

\> LangCache 保存新的嵌入向量和响应以供后续复用

与 LangChain 缓存的差异：

\> LangChain 内置缓存（如 RedisCache 或 InMemoryCache）仅支持字符串精确匹配

\> RedisSemanticCache 虽支持嵌入向量，但需自行托管且扩展性有限Redis LangCache 是一项专为生产工作负载设计的全托管语义缓存服务。为何重要：

更快的响应时间

降低 API 成本

无需管理基础设施

\>Language-agnostic（通过 REST API）何时使用：

\>AI 智能体、RAG 系统与聊天机器人

\>重复或相似查询处理

\>Production-grade 可靠性

自动优化的嵌入

\>详细缓存监控

![Diagram illustrates LangCache architecture for AI app. Client app sends prompt to embedding model service which generates vector. Vector used to search LangCache for similar entries via POST request. If cache hit returns stored response from Redis. If miss calls LLM for new response then stores embedding and response in vector DB and Redis via POST. Components include project response cache service route handler metadata cache service and centralized metadata. Arrows show data flow between services.](https://pbs.twimg.com/media/G46VCWzWEAA5FVp?format=png&name=large)

* * *

**lucas liao** @liao\_lucas [2025-11-04](https://x.com/liao_lucas/status/1985723314535612835)

嵌入模型的准确性是否足以让你选择一个“相似”的向量，而它仍能代表相同的语义含义？我对此处的输出质量有所顾虑

* * *

**Rohit** @rohit4verse [2025-11-04](https://x.com/rohit4verse/status/1985724716695634025)

你保持谨慎是完全正确的。该系统的有效性取决于你对相似度阈值和所选嵌入模型的审慎考量。托管服务正是为你承担了这些复杂工作的大部分。

* * *

**Manthan Patel | Lead Gen Man** @leadgenmanthan [2025-11-04](https://x.com/leadgenmanthan/status/1985760475687350596)

语义缓存是多数 AI 应用忽略的关键层，LangCache 精准实现了这一功能。

* * *

**Rohit** @rohit4verse [2025-11-04](https://x.com/rohit4verse/status/1985761272076648568)

绝对如此……当规模扩大时，哪怕只是 1%的增长也至关重要，因为 LLM 的成本极其高昂。

* * *

**spidey** @lochan\_twt [2025-11-04](https://x.com/lochan_twt/status/1985722083499000289)

这家伙最近发的都是些疯狂内容

* * *

**Rohit** @rohit4verse [2025-11-04](https://x.com/rohit4verse/status/1985724099193380966)

最好的尚未来临

* * *

**Susindra** @SusindrarR [2025-11-04](https://x.com/SusindrarR/status/1985714641734156716)

干得漂亮，老兄！这是 Langchain 团队发布的吗？

* * *

**Rohit** @rohit4verse [2025-11-04](https://x.com/rohit4verse/status/1985714965588947212)

人 😂 😂 至少读两行，第二行本身就提到这不是来自 langchain

* * *

**Shubhu** @positronx\_ [2025-11-04](https://x.com/positronx_/status/1985775781151457749)

我时间线上出现的最佳帖子

* * *

**Rohit** @rohit4verse [2025-11-04](https://x.com/rohit4verse/status/1985776156906602807)

嘿嘿，谢谢舒布大哥

* * *

**Ashfaque** @ashfaque\_dev [2025-11-04](https://x.com/ashfaque_dev/status/1985739551583977722)

好兄弟解释得真清楚

* * *

**Rohit** @rohit4verse [2025-11-04](https://x.com/rohit4verse/status/1985739844430307345)

呵呵，谢谢，希望我的解释能让你明白

* * *

**TrendsAGI** @TrendsAGI [2025-11-04](https://x.com/TrendsAGI/status/1985717884987798011)

这引起了共鸣。实际上，我们在过去一个季度观察到生产部署中优先考虑语义召回而非简单键值记忆的趋势显著上升，这标志着处理方式正日趋成熟。

我们帮助搜索引擎优化师在话题流行之前发现此类突破性主题。

* * *

**Rohit** @rohit4verse [2025-11-04](https://x.com/rohit4verse/status/1985718212810719728)

私信聊会儿？

* * *

**CG** @cgtwtz [2025-11-04](https://x.com/cgtwtz/status/1985725122729427050)

解释得真是太好了……干得漂亮

* * *

**Rohit** @rohit4verse [2025-11-04](https://x.com/rohit4verse/status/1985725467681497565)

谢了兄弟，我会全面覆盖智能代理 AI 领域的内容

* * *

**Siddharth** @Pseudo\_Sid26 [2025-11-04](https://x.com/Pseudo_Sid26/status/1985714358287286429)

W 解释 兄弟 👏 💯

* * *

**Rohit** @rohit4verse [2025-11-04](https://x.com/rohit4verse/status/1985714439723827674)

多谢兄弟 ❤️

* * *

**Omkar** @psomkar1 [2025-11-04](https://x.com/psomkar1/status/1985725136490938428)

兄弟，你真是太棒了 🔥

* * *

**Rohit** @rohit4verse [2025-11-04](https://x.com/rohit4verse/status/1985725553740300720)

最好的尚未来临

* * *

**Tirthhhh** @Tirthhh30 [2025-11-04](https://x.com/Tirthhh30/status/1985728028090175561)

语义缓存带来根本性改变，文本匹配仅触及皮毛。

* * *

**Rohit** @rohit4verse [2025-11-04](https://x.com/rohit4verse/status/1985729196531073068)

语义缓存是解决之道，它能显著降低 LLM 的开销

* * *

**Himanshu Singh** @nothiingf4 [2025-11-04](https://x.com/nothiingf4/status/1985730383884038325)

太棒的帖子！！缓存现在终于能读懂言外之意了，真是智能多了。

* * *

**Uzeb Khan** @X\_Ibyte [2025-11-04](https://x.com/X_Ibyte/status/1985705537976352852)

@grok 简而言之

* * *

**CryptoPatrick** @cryptopatrick [2025-11-04](https://x.com/cryptopatrick/status/1985786284611129481)

你能否分享一下，你是用什么工具制作出那个精美图表的？

* * *

**Himanshu Kumar** @codewithimanshu [2025-11-04](https://x.com/codewithimanshu/status/1985763165247062341)

罗希特，这一点说得太棒了！语义缓存对智能体来说确实更合适，对吧？

* * *

**Jagrit** @Jagrit\_Gumber [2025-11-04](https://x.com/Jagrit_Gumber/status/1985840426923016715)

已为再次阅读添加书签 🫡

* * *

**Pradyumna** @daddy\_\_broccoli [2025-11-04](https://x.com/daddy__broccoli/status/1985707354487472257)

太棒了 🙌🏻 🙌🏻