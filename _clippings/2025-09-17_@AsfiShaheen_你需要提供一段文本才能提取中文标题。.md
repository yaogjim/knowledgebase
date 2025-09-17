---
title: "你需要提供一段文本才能提取中文标题。"
source: "https://x.com/AsfiShaheen/status/1967866903331999807"
author:
  - "[[@AsfiShaheen]]"
published: 2025-09-17
created: 2025-09-17
description:
tags:
  - "@AsfiShaheen 你需要提供一段文本才能提取带有 # 的中文标签。"
---
**Asfi** @AsfiShaheen [2025-09-16](https://x.com/AsfiShaheen/status/1967866903331999807)

  
要使用 GEPA（DSPy 中最佳的优化器），你需要两件事

1\. 准确的人工标注数据集

2\. 关于它为何准确的文本解释

以下是一个应用于标记财务报表的实例。这种方法可以为你节省时间和金钱。 🧵

---

**Asfi** @AsfiShaheen [2025-09-16](https://x.com/AsfiShaheen/status/1967866907182428610)

  
1\. 是什么让 GEPA 与众不同

我认为这是第一个既需要正确答案集，又需要对为何这些是正确答案作出解释的优化器。

大卫·多伊奇可能会喜欢它。也许 GEPA 是无穷的开端？我离题了。

---

**Asfi** @AsfiShaheen [2025-09-16](https://x.com/AsfiShaheen/status/1967866910458126794)

  
2\. 用例

我已经将大约一百万页内容转换成了 Markdown 格式，并且需要分配元数据标签。

我可以用正则表达式（很糟糕）、手工编写的提示（错误太多）来做这件事，或者我使用 GEPA。

要做到这一点，我需要处理 300 页内容，手动标记它们，并为我的推理写下解释。

---

**Asfi** @AsfiShaheen [2025-09-16](https://x.com/AsfiShaheen/status/1967866914207830360)

  
3\. 手动打标签？真的吗？

嗯，其实并非如此。我可以使用 Opus 和 Gemini Pro，并设置较高的令牌预算来创建我的数据集，其准确率能达到近 90%，但成本很高。

然后我手动检查结果并将其冻结。最终结果是 300 页完美且有详细解释的内容。

---

**Asfi** @AsfiShaheen [2025-09-16](https://x.com/AsfiShaheen/status/1967866918460858763)

  
4\. 现在到了有趣的部分

如果我有这 300 页我知道是正确的且有详细解释的内容，我可以使用像 Gemini 2.5 lite 这样快速/低成本的大语言模型（LLM），或者 groq 上众多开源模型中的一个，然后直接在 dspy.GEPA 中运行它们。

---

**Asfi** @AsfiShaheen [2025-09-16](https://x.com/AsfiShaheen/status/1967866921954709879)

  
5\. 最终结果是接近 100%的准确率、超快速且超低成本的标注。

因为我当然负担不起，也等不起用那该死的 Opus 或 Gemini 2.5 Pro 去标记上百万页面。我的意思是也许我可以，但那简直是浪费时间和金钱。

---

**Asfi** @AsfiShaheen [2025-09-16](https://x.com/AsfiShaheen/status/1967866930754470096)

  
6\. 总体而言，我觉得 DSPy 的文档过于技术化了。

例如，看看这个关于 GEPA 的解释。它都是正确的，但当你第一次读的时候会头疼。

要点是：不要只给你的模型正确答案，还要给出为什么它是正确答案的解释。

![Image](https://pbs.twimg.com/media/G09EitYWkAAzyap?format=jpg&name=large)

---

**Dr. Datta M.D. (AIIMS Delhi)** @DrDatta\_AIIMS [2025-09-16](https://x.com/DrDatta_AIIMS/status/1968038520234316265)

  
但我们是否总是需要给他们解释呢？就我而言，（BLEU 和 ROUGE）这些指标还不够吗？还是你认为最好给出解释？

---

**Asfi** @AsfiShaheen [2025-09-16](https://x.com/AsfiShaheen/status/1968039921844965726)

  
我今天尝试了 MIPROv2 和 GEPA。为了给出解释，我使用了一个大语言模型（LLM）来生成，然后检查它们是否正确。

GEPA 并不严格要求解释部分，但我发现它极大地改进了生成的提示 + 以及在我的更大语料库上的结果。

---

**Asfi** @AsfiShaheen [2025-09-16](https://x.com/AsfiShaheen/status/1968040732343832766)

  
大致就是这样的模式。我为每一页都设置了元数据标签（这是我的正确的黄金数据集），后面跟着解释。

我还在没有它的情况下运行了 GEPA，结果发现准确率也没有那么好地趋于稳定。

![Image](https://pbs.twimg.com/media/G0_iRIkWoAAtSYc?format=jpg&name=large)

---

[2025-09-16](https://x.com/aldea_trading/status/1968041969218908298)

  
如果可能的话，你能分享一下 GitHub 吗？？关于你的代码的。

---

**Asfi** @AsfiShaheen [2025-09-16](https://x.com/AsfiShaheen/status/1968059924883313085)

  
上传太麻烦了。但我迟早会上传的。

不过说实话，在你得到数据集之后，它就是即插即用的。只需将 dspy.GEPA 页面粘贴到 GPT5 或类似工具中，你很快就能让它运行起来。

---

**Phillip Ninan** @ninan\_phillip [2025-09-16](https://x.com/ninan_phillip/status/1968058034007183594)

  
很棒的推文！

你能给出一两个你使用的数据集的例子吗？或者有没有关于“标注”和提供文本解释的文档？

我刚接触 DSPy 和优化，不确定自己做得是否正确。我正在构建一个 RAG，我的数据集只是问题和答案。

---

**Asfi** @AsfiShaheen [2025-09-16](https://x.com/AsfiShaheen/status/1968058892660904364)

  
{"pg": 73, "content\_type": "附注", "statement\_type": "无", "note\_type": "资产负债表", "explanation": "本页详细列出负债和承诺事项，包括法律诉讼、税务要求和银行担保。这些是与资产负债表相关的潜在未来义务。"}
