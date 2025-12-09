---
title: "AI in 2025: gestalt — LessWrong"
source: "https://www.lesswrong.com/posts/Q9ewXs8pQSAX5vL7H/ai-in-2025-gestalt"
author:
  - "[[technicalities]]"
date: "2025-12-09T16:34:23+08:00"
created: 2025-12-09
description: "This is the editorial for this year’s \"Shallow Review of AI Safety\". (It got long enough to stand alone.)  …"
tags:
  - "technicalities"
---
![](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/Q9ewXs8pQSAX5vL7H/u8obwd0t50n9njxvb8tf)

AI in 2025: gestalt by technicalities 24 min read 35 185

x

AI in 2025: gestalt — LessWrong

[^1]: Gemini 3 据称是一次大规模预训练，但相比其他项目，我们对此的实际证据更少，因为无法追踪其 GPU 使用情况。

[^2]: 参见 [宝可梦](https://www.lesswrong.com/posts/Q9ewXs8pQSAX5vL7H/ai-in-2025-gestalt?commentId=WNX5GLdn4ALCucYZb) 作为可能存在的反例。

[^3]: 弱论点如下：Epoch [推测](https://epoch.ai/data/ai-models) Grok 4 的总计算量为 5e26 FLOP。一份非科学的 xAI 营销图表暗示其中一半用于强化学习：2.5e26。而 Mechanize 曾提出 6e26 作为可能引发显著泛化能力的强化学习预算范例。

（实际上，这并非全是强化学习的功劳。）

[^4]: "我们推测其他机构比 OpenBrain 落后 3 到 9 个月。"

[^5]: 莱克辛是一位严谨的灵魂，并指出严格聚合这18种能力并不可行。我在此做了一些有意义的尝试——根据每种能力的特征重要性进行加权处理。

[^6]: 两次运行结果分别为\[48, 85\]，其余运行结果波动幅度小于 4 个点。感谢 Epoch 团队！

另外，o1 模型在这里看起来平平无奇，但这与当时的实际感受不符。我认为这是因为它的发布时间被拖延了很久，这影响了基于公开发布日期计算的进展速率。（别忘了 o1-preview 的训练数据截止到 2023 年 10 月！）

此外，ADeLE o1 的结果也采用了"低"推理强度。

[^7]: 不拖延的一个原因是，这些措施正面临激烈的对抗压力。（ADeLe 尚未被古德哈特定律影响，但这仅仅是因为目前无人知晓它的存在。）

[^8]: 例如参见 [ERNIE-...A47B](https://ernie.baidu.com/blog/posts/ernie4.5/) ，其中“A”表示“活跃”。

[^9]: 即“生物武器；儿童安全；致命武器；平台操纵和影响力行动；自杀与自残；浪漫骗局；追踪与监视；以及暴力极端主义和激进化。”

[^10]: "通过对抗性调控...评估意识表征通常会降低语言化评估意识，有时还会增加错位率...\[无意识调控版 Sonnet 4.5\]的有害行为发生率仍低于 Opus 4.1 和 Sonnet 4。"

[^11]: 假设在 1:8 稀疏度的 MoE 模型中，以每参数 120 个令牌的计算最优配置，采用 FP8 精度进行为期 4 个月、利用率为 40%的训练（目前这似乎已接近主流水平，甚至 NVFP4 在预训练中也 不再显得完全不可能 （ no longer seems completely impossible ） ）。

[^12]: 既然 Grok 5 将是一个 [总参数量达 6T](https://www.youtube.com/watch?v=GwfLkEOW37Q) 的模型，旨在与 OpenAI 竞争并瞄准相同的 NVL72 系统，或许 GPT-4.5 的总参数量也仅为 6T，因为如果 GPT-4.5 规模更大，xAI 在规划 Grok 5 时本应能发现这一点并匹配其架构。