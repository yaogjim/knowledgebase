---
title: "文本到SQL微调：Qwen-0.6B超越GPT-4.1"
source: "https://x.com/gregschoeninger/status/1922781767720706151"
author:
  - "[[@gregschoeninger]]"
created: 2025-05-16
description:
tags:
  - "@gregschoeninger #文本到SQL #微调 #Qwen #GPT-4.1"
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
**Greg Schoeninger** @gregschoeninger [2025-05-14](https://x.com/gregschoeninger/status/1922781767720706151)

  
我花了大约 10 分钟在 Text2SQL 上对 Qwen-0.6B 进行微调，并在同一任务上超过了 GPT-4.1 的准确率。

Qwen 是个虽小却强大的王者 👑

![Image](https://pbs.twimg.com/media/Gq8XHddXoAAT3ht?format=jpg&name=large)

---

**Greg Schoeninger** @gregschoeninger [2025-05-14](https://x.com/gregschoeninger/status/1922781769650114847)

  
如果你想知道为什么总体准确率如此之低，文本到 SQL 是一项有点困难且微妙的任务

> 2025-05-14
> 
>   
> 评估文本到 SQL 有点难，不声张地说
> 
> ![Image](https://pbs.twimg.com/media/Gq8Jnr-aAAAUGJR?format=png&name=large)

---

**Greg Schoeninger** @gregschoeninger [2025-05-14](https://x.com/gregschoeninger/status/1922781771432652899)

  
博客文章即将发布 👀

---

**DeGao** @MrDeGao [2025-05-16](https://x.com/MrDeGao/status/1923235855474233764)

  
如果你感兴趣，我们一起做个实验吧。我们一起试试 DLM，看看它能不能更高？

---

**Greg Schoeninger** @gregschoeninger [2025-05-16](https://x.com/gregschoeninger/status/1923240112982294648)

  
一个扩散语言模型听起来很有趣，很想尝试一下

---

**熊布朗** @Stephen4171127 [2025-05-15](https://x.com/Stephen4171127/status/1923016808501539275)

  
期待你的博客！我真的很喜欢你上周在巴黎的分享

---

**Caleb** @calebfahlgren [2025-05-15](https://x.com/calebfahlgren/status/1923014500921249870)

  
很棒！要是能在 @huggingface 中心看到一篇帖子就好了。我觉得社区会很喜欢这个的！

---

**Greg Schoeninger** @gregschoeninger [2025-05-15](https://x.com/gregschoeninger/status/1923048694720401870)

  
当博客文章完成后我会通知你，然后我们可以进行交叉发布 🤝

---

**Shailesh** @0xThoughtVector [2025-05-15](https://x.com/0xThoughtVector/status/1923060418467025047)

  
如果有的话，你能简要描述一下你的秘诀是什么吗？

---

**Greg Schoeninger** @gregschoeninger [2025-05-15](https://x.com/gregschoeninger/status/1923062056565002437)

  
老实说，没什么特别的诀窍，只是使用 transformers 库进行了一次标准的微调。我会整理一篇包含数据和代码的博客文章，这样任何人都可以复现。

---

**atharva** @k7agar [2025-05-15](https://x.com/k7agar/status/1922963629055541618)

  
我喜欢他们为此设计的小型模型；用于试验和部署既快速又极其便宜

---

**Greg Schoeninger** @gregschoeninger [2025-05-15](https://x.com/gregschoeninger/status/1923046088522543313)

  
到目前为止，和它们一起玩非常有趣，豆包团队干得很棒

---

**ibrahim.demirci.com** @iedmrc [2025-05-15](https://x.com/iedmrc/status/1923071366347075730)

  
你是使用你微调时所用的同一个数据集进行测试的吗？

---

**Greg Schoeninger** @gregschoeninger [2025-05-15](https://x.com/gregschoeninger/status/1923074716786393475)

  
使用训练集/验证集/测试集划分

---

**Reinaldo Sotillo** @reynald76165051 [2025-05-15](https://x.com/reynald76165051/status/1923031020258893915)

  
尝试 GPT4.1 纳米微调

---

**Greg Schoeninger** @gregschoeninger [2025-05-15](https://x.com/gregschoeninger/status/1923045982477992331)

  
哦，那会是个有趣的比较！

---

**winston** @winston178 [2025-05-15](https://x.com/winston178/status/1923079052656591223)

  
不过是哪种 SQL 语言呢？

---

**Greg Schoeninger** @gregschoeninger [2025-05-15](https://x.com/gregschoeninger/status/1923079990830047644)

  
此示例的 PostgreSQL 语法

---

**Aakash** @a\_void\_sky [2025-05-15](https://x.com/a_void_sky/status/1923004056680731030)

  
用于训练的硬件？

---

**Greg Schoeninger** @gregschoeninger [2025-05-15](https://x.com/gregschoeninger/status/1923015519327654301)

  
你不需要太多资源，进行完整的微调只需要几 GB 的 VRAM。我最后在一台笔记本电脑上使用了一块 A10G 显卡，网址是 http://Oxen.ai

https:// 文档.oxen.ai/功能/笔记簿 s…

---

**Peter Haider** @pepehaider [2025-05-16](https://x.com/pepehaider/status/1923268633758700023)

  
对于微调过程，你有一些好的建议吗，比如代码库之类的？我想针对特定行业的 XML 格式微调一个编码模型，但真的不知道从哪里开始。

---

**Farseen CK** @itsfarseen [2025-05-16](https://x.com/itsfarseen/status/1923331452998975668)

  
你使用什么硬件进行微调？

有没有可能使用配备 RTX 3060 6GB 的游戏笔记本电脑来实现这一点？