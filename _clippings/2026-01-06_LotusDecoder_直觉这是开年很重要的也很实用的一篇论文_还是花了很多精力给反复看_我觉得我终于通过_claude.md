---
title: "2026-01-06_LotusDecoder_直觉这是开年很重要的也很实用的一篇论文_还是花了很多精力给反复看_我觉得我终于通过_claude"
source: "https://x.com/LotusDecoder/status/2008090818217730535"
author:
  - "[[@LotusDecoder]]"
published: 2026-01-06
created: 2026-01-06
description:
tags:
  - "x"
  - "@LotusDecoder"
  - "https"
  - "language"
---

# 直觉这是开年很重要的也很实用的一篇论文，还是花了很多精力给反复看。 我觉得我终于通过 claude

**LotusDecoder** @LotusDecoder 2025-10-15

直觉这是开年很重要的也很实用的一篇论文，还是花了很多精力给反复看。

我觉得我终于通过 claude code 把 Recursive Language Models 这篇论文给理解了。不知道对不对，发出来看看。

论文里有三类方法处理 高信息密度 提示词。

形象点说，

一、base model，我们大家常用的整段塞进去，臣妾做不到啊，效果几乎为0，gg。

二、agent，分解给多个subagent，一人处理一段后再返回给main agent 综合。然而一盘散沙，各自为政，各扫门前雪，我做啦，其它的不归我管。效果稍好些。

三、Recursive Language Models，main-LLM 像是一位全局指挥官，提示词是一个可操作的对象，指挥官拿到问题，先琢磨如何安排具体流程，他的精力，用户的目标在上下文空间里只是一个变量，占有的字符数极少，随后，指挥官才是，叫手下小弟一步一步干活，有的小弟是 python-read，有的小弟是 python-write ，有的小弟是 sub-LLM。所以，因为main-LLM是注意力始终聚焦在目标和解决问题的，最后效果远远优于前面两种方法。

而且，Recursive Language Models 还是符合端到端理念的，具体的任务识别、分类、决策、执行，是 LLM 自行决定和尝试的，我们即使做agent方式，很多时候也是人去决断挑选哪种数据挖掘方式。

> 2025-10-15
> 
> What if scaling the context windows of frontier LLMs is much easier than it sounds?
> 
> We’re excited to share our work on Recursive Language Models (RLMs). A new inference strategy where LLMs can decompose and recursively interact with input prompts of seemingly unbounded length,
> 
> 如果扩展前沿 LLMs 的上下文窗口比听起来容易得多，会怎么样？
> 
> 我们很高兴分享我们在递归语言模型 (RLMs) 方面的研究成果。这是一种新的推理策略，LLMs 能够分解并递归地与看似无限长的输入提示进行交互。
> 
> ![Image](https://pbs.twimg.com/media/G3TuAPxWYAATrbO?format=jpg&name=large)

* * *

**vito** @zzzzxys [2026-01-05](https://x.com/zzzzxys/status/2008233467516252182)

思路上都是想方法把好钢用在刀刃上，用最先进模型最宝贵的上下文来处理最重要问题。

无论是子agent，外部记忆储存，还是现在的RLM解决的都是同一个问题，但工程方案差距极大。

RLM做的是创建一个虚拟Python空间，把长提示词放到这个代码空间里（而不是main LLM的上下文中），main LLM指挥sub LLM去做抽样，通过抽样结果，分析怎么做切片。

main LLM根据抽样结果反馈，分配新的抽样、切片任务下去，同样的如果sub LLM发现任务太过复杂，也可以调用自己的sub LLM（就像main LLM调用他一样，这是递归结构）。

通过把长上下文做外包，子LLM也不直接处理过大的数据块（过大就抽样理解结构，然后切片分工），这样每一级别的数据量会很小。同时由于采取了python代码切片、分析的方式，也很容易通过python做查询，找到原始需求，定位问题简单，信息保存完整。

这就有效缓解了上下文的使用效率问题。这个理解不知道对不对，我感觉论文的工程实现方案比较难理解。

* * *

**LotusDecoder** @LotusDecoder [2026-01-06](https://x.com/LotusDecoder/status/2008330189135360099)

我也觉得是很难理解。

相当于，比agent在更贴近地方给LLM的主观能动性配了工具吧。

* * *

**Vince** @vce7 [2026-01-05](https://x.com/vce7/status/2008105681669574811)

感觉卖点会是打破 context window 限制加 accuracy 不打折，只是需要接受更多 reasoning 步数？
