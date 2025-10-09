---
title: "# 信息位的重要性"
source: "https://x.com/ShashwatGoel7/status/1975939253680120152"
author:
  - "[[@ShashwatGoel7]]"
published: 2025-10-09
created: 2025-10-09
description:
tags:
  - "@ShashwatGoel7 # 人工智能 # 强化学习 # 模仿学习 # SFT"
---
**Shashwat Goel** @ShashwatGoel7 [2025-10-08](https://x.com/ShashwatGoel7/status/1975939253680120152)

  
在 @johnschulman2 发表精彩博客指出强化学习获取的信息量意外之少后，人们对其重要性产生了困惑。以下是我的博客内容，探讨我们可能忽略的关键点：

并非所有比特都生而平等。

信息中的某些比特比其他比特更为重要。这一观察看似简单，却对探索与学习领域——无论是人类还是人工智能——具有深远影响。

以估算大数为例，当数字接近十亿时，百位数的重要性会降低数百万倍。

然而，我们过于纠结信息比特的数量。这种看法太过线性。面对现实世界的不确定性，高阶比特的重要性呈指数级增长。唐纳德·特朗普最喜爱的汽车品牌详细历史可能包含数千比特信息——谁在乎呢？但“他是否是美国总统”这一个比特，却能改变整个世界。

对人工智能的启示

思考模仿学习与强化学习之争——这是当前 AI 领域最热门的话题，源自 @dwarkesh\_sp 与 @RichardSSutton 的播客对谈。LLM 的强化学习从标量奖励中学习，与监督微调（SFT）模仿完整句子相比，所获取的信息比特数极为有限。表面看来，后者显然具有更高的“信息密度”。

然而，强化学习所传授的那最关键的一比特信息，正是关于成败的判断。这正是强化学习在极限情况下超越模仿学习的威力所在——它监督着最高阶的比特，让你无需耗费成本去收集那些次要信息。

另一方面，监督微调（SFT）在某种程度上最小化与参考答案的汉明距离。对 SFT 而言，每个差异位都同等重要。土豆还是洋芋？对 SFT 来说可谓天壤之别。它宁愿牺牲语义正确性也要死磕拼写细节。当然，当你确实需要关注所有信息位时（比如知识积累场景），SFT 依然至关重要。这种情况下强化学习可能效率过低。正因如此，我尚未成为强化学习的“绝对拥护者”。

一个有趣的巧合是，汉明距离衡量的是与理查德·汉明决策理念相反的东西。

在他颇具影响力的演讲《你与你的研究》中，他告诉我们运用最高位原则来指导研究。科研领域存在无数有趣的问题——有待解释的现象列不尽列。然而，有些问题比其他问题更为重要，这些便是更高位的问题。鉴于各位读者时间有限，这些正是你们应当竭力优先解决的问题。用汉明的话来说：

“若不在重要问题上耕耘，便难有重要成果问世。”

![Binary string of 0s and 1s displayed horizontally with green text overlay stating This bit matters a billion times more than that last one above the string and repeated below it.](https://pbs.twimg.com/media/G2uykeEWkAA-Lqi?format=jpg&name=large)

---

**Shashwat Goel** @ShashwatGoel7 [2025-10-08](https://x.com/ShashwatGoel7/status/1975948079724372160)

  
若您希望将此内容保存或分享为博客：https://open.substack.com/pub/shash42/p/not-all-bits-are-made-equal…

---

**Maaz** @mmaaz\_98 [2025-10-08](https://x.com/mmaaz_98/status/1976017822259294541)

  
SFT 在何种意义上最小化汉明距离？还是说您指的是它最小化的是\*令牌级别\*的负对数似然？

---

**Shashwat Goel** @ShashwatGoel7 [2025-10-08](https://x.com/ShashwatGoel7/status/1976019408838332570)

  
从直观的粗略角度来看，它确实最小化了负对数似然。但若将负对数似然离散化，便成了汉明距离。

---

**Sheet0** @sheet0ai

  
您的时间比复制粘贴更宝贵。

还在手动复制数据吗？

有个更聪明的办法。

使用 Sheet0 来收集、清理和组织网络数据。

---

**Bhishmaraj S** @bhi5hmaraj [2025-10-08](https://x.com/bhi5hmaraj/status/1976020412808282310)

  
我认为预训练与监督微调之间应有明确区分。

我认为记忆是由数据集、模型规模和计算能力共同作用的结果。当数据集较小时，（具备能力的）模型倾向于过拟合或记忆；而当数据集足够大时，则更倾向于泛化。

---

**Shashwat Goel** @ShashwatGoel7 [2025-10-08](https://x.com/ShashwatGoel7/status/1976022609738285157)

  
确实如此！但我想表达的观点可能也适用于大型数据集。最小化交叉熵时，所有标记都被赋予了同等权重。

但我们最关心的关键点在于成功！至于 SFT/预训练会关注哪些细节，其实并不重要。我认为并非如此。

---

**ABHISHEK SAWALAKHIYA** @ASawalakhiya [2025-10-09](https://x.com/ASawalakhiya/status/1976160804543328376)

  
这一“高阶位”原则对商业战略至关重要。领导者如何系统性地识别出，若能提升哪一项关键绩效指标，便能让其他所有优化措施相形见绌？

---

**Dode Dahroug** @DodeDahroug [2025-10-08](https://x.com/DodeDahroug/status/1976043634345771151)

  
更少的比特，确定吗？

---

**Parth Thakkar** @parth007\_96 [2025-10-08](https://x.com/parth007_96/status/1976062862759194987)

  
相关的

> 2025-09-03
> 
>   
> 如何向他人解释交叉熵损失中“微小”的差异实则至关重要？

---

**Christy Jestin** @christyjestin [2025-10-08](https://x.com/christyjestin/status/1976043642625429564)

  
拥有如此多功能的推理基础，却仍对大型语言模型的强化学习依赖纯策略梯度，这难道不是明显荒谬吗？

就像这整个关于 Thinky 等人信息位的讨论：为什么我们谈论学习数学，就好像在教狗坐下一样？

> 2025-10-04
> 
>   
> 拥有如此多功能的推理基础，却仍对大型语言模型的强化学习依赖纯策略梯度，这难道不是明显荒谬吗？
> 
> 就像这整个关于 Thinky 等人信息位的讨论：为什么我们谈论学习数学，就好像在教狗坐下一样？