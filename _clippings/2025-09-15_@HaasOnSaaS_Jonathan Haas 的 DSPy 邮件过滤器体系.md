---
title: "Jonathan Haas 的 DSPy 邮件过滤器体系 "
source: "https://x.com/HaasOnSaaS/status/1963344407689925039"
author:
  - "[[@HaasOnSaaS]]"
published: 2025-09-15
created: 2025-09-15
description:
tags:
  - "@HaasOnSaaS #DSPy #邮件过滤器 #人工智能 #LLM #执行助理"
status: "inbox"
importance: 2
effort: 2
review_level: 0
review_next: "2025-10-17"
review_interval: null
review_count: 0
decision: null
topics: []
links_out: []
summary: ""
pov: ""
actions: []
---
**Jonathan Haas** @HaasOnSaaS [2025-09-03](https://x.com/HaasOnSaaS/status/1963344407689925039/history)

  
他们说：“你不能什么都往上面扔 @DSPyOSS 。”

我：将 DSPy 扔进收件箱

DSPy：批量进行类似更新，将谷歌相关内容转至工程部门，将水星项目标记为网络推广，展示竞争情报。

我：我绝对可以，而且会的。

![A screenshot of a terminal window displaying text. The text includes headers like ](https://pbs.twimg.com/media/Gz8zSlEbkAEVnDG?format=jpg&name=large)

---

**Jonathan Haas** @HaasOnSaaS [2025-09-03](https://x.com/HaasOnSaaS/status/1963362662966042801)

  
其工作方式是一个分层的 DSPy 管道，在随着时间推移变得更智能的同时，还能保持低成本。

大约 70%的电子邮件由基于规则的过滤器（时事通讯、促销邮件、明显的垃圾邮件）即时处理，LLM 成本为零。

接下来约 25%的内容会通过一个经过轻量级、针对 DSPy 优化的 GPT-3.5 分类器，该分类器是基于我的修正内容和合成示例进行训练的，成本仅为几美分的零头。

只有最难处理的约 5%的情况会触发完整的 GPT-4 推理链，该推理链会在做出决策前分析发送者、意图、优先级和上下文。

每次修正都会反馈到 DSPy 的 MIPROv2 优化器中，因此系统会不断重新学习更好的提示和路由策略。

结合特定于评估运营（EvalOps）的业务背景（投资者、客户、筹款重点），最终成果是一个能以每封邮件低于一美分的成本做出与首席执行官相关决策的执行助理。

---

**Jonathan Haas** @HaasOnSaaS [2025-09-03](https://x.com/HaasOnSaaS/status/1963363600837611815)

  
简单得漂亮。

![Image](https://pbs.twimg.com/media/Gz9ExdcbkAATb7y?format=jpg&name=large)

---

**Brandon Galang** @brandon\_galang [2025-09-04](https://x.com/brandon_galang/status/1963699221787472270)

  
这很酷，但你为什么使用 GPT3.5 和 4？