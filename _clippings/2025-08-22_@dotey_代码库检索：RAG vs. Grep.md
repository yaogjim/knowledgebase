---
title: "代码库检索：RAG vs. Grep"
source: "https://x.com/dotey/status/1958557280166703401"
author:
  - "[[@dotey]]"
published: 2025-08-22
created: 2025-08-22
description:
tags:
  - "@dotey #代码搜索 #RAG #Grep #代码库"
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
**宝玉** @dotey 2025-08-21

代码库做 RAG 的几个主要问题：

1\. 很多代码文件很大，必须分块，分块后可能结果不完整

2\. 代码更新频繁，尤其是现在 AI 生成代码速度太快，而 RAG 需要时间去做 Embedding，这可能会导致检索不到最新结果

3\. 代码更适合精确检索（函数名、变量名等）

另外 grep 检索对 token 消耗并不大，因为 LLM 只需要生成传入 Grep 的参数，以及处理 Grep 后的结果，LLM 本身不需要读取整个代码库去检索。

AI 比人更擅长用 Grep 是因为 AI 更会写正则表达式以及设置各种参数，普通人主要用关键词

> 2025-08-21
> 
> 感觉大家现在对于代码库检索各执一词，最近看了zilliz新开源了一个claude-context，他们就是用RAG做的，主要设计还是在保持语意完整上，因为grep单纯靠字面意思匹配，对token消耗很大。
> 
> https://github.com/zilliztech/claude-context…

---

**Jeffrey** @fancylea [2025-08-22](https://x.com/fancylea/status/1958719104988430348)

但凡尝试过Embedding和search两个方案的，绝对不会选择embedding

embedding 缺点太明显了，成本高，速度慢，还不准确，对于代码这种变动频繁的东西根本就不合适。

---

**waroy** @0xWaroy [2025-08-21](https://x.com/0xWaroy/status/1958560539547758601)

所以我真的好佩服发明， grep, sed，jq 的人。 在AI出来之前就发明了给AI 用的工具。

相比之下sql真的逊爆了，字多浪费token。

---

**LouisShark** @shark\_louis [2025-08-21](https://x.com/shark_louis/status/1958558954377871645)

llm 吐 token 的速度越快 token 越便宜 应该趋势就越偏向 grep

---

**Yang Li** @YangLi\_leo [2025-08-21](https://x.com/YangLi_leo/status/1958591594220986408)

学习了，尤其是第二点🫡