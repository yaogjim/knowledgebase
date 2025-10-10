---
title: "#人工智能发展"
source: "https://x.com/HaasOnSaaS/status/1966972931369824412"
author:
  - "[[@HaasOnSaaS]]"
published: 2025-09-15
created: 2025-09-15
description:
tags:
  - "@HaasOnSaaS #美食 #旅行 #科技"
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
**Jonathan Haas** @HaasOnSaaS [2025-09-13](https://x.com/HaasOnSaaS/status/1966972931369824412)

  
冷邮件没死。糟糕的冷邮件才死了。

我们开源了一个 CLI 工具，它能学习你 3 封“获胜”邮件的风格，使用 @DSPyOSS，然后生成具有相同创始人风格语气的新的外联邮件。

CSV 格式的成功案例 + 潜在客户

下周可供 A/B 测试的已评分、已优化的邮件

冷邮件没死，写得差的冷邮件才死了。我们开源了一个 CLI 工具，它能学习你 3 封“获胜”邮件的风格，然后用 @DSPyOSS 生成新的外联邮件，保持同样的创始人风格语气。输入：获胜邮件 + 潜在客户的 CSV 文件 输出：评分、优化过的邮件，你可以在下周进行 A/B 测试。 https://github.com/evalops/founder-email-optimizer…

---

**Jonathan Haas** @HaasOnSaaS [2025-09-13](https://x.com/HaasOnSaaS/status/1966972933320176148)

  
为什么只用3个成功的例子？

大多数创始人没有成百上千条已标记的回复。DSPy 让我们从一小批演示数据开始，然后优化指令直到它们能够泛化。

---

**Jonathan Haas** @HaasOnSaaS [2025-09-13](https://x.com/HaasOnSaaS/status/1966972934557421906)

  
工作原理：

你给我们一个包含你最好邮件和潜在客户列表的 CSV 文件

DSPy 的 Predict + Optimize 模块会生成新的草稿

一个 judge 模块会根据具体性、创始人语气和槽位覆盖度进行评分

Guardrails 可阻止点击诱饵、废话或虚假的 the product 声明

---

**Jonathan Haas** @HaasOnSaaS [2025-09-13](https://x.com/HaasOnSaaS/status/1966972936038084816)

  
为什么选择 ？@DSPyOSS

它让“提示 + 少样本 + 评判 + 优化器”循环变得声明式。我们不再手动调整提示，而是定义一个签名（创始人邮件应该是什么样子），然后让 DSPy 来处理优化。

---

**Jonathan Haas** @HaasOnSaaS [2025-09-13](https://x.com/HaasOnSaaS/status/1966972937648697508)

  
结果：一个小型、可组合的工具，可以接入你正在使用的任何潜在客户生成工具（Clay、Apollo、HubSpot）。

输入你的 3 个成功案例 → 下周测试更好的外展内容。