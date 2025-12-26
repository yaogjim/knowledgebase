---
title: "The behavioral selection model for predicting AI motivations — LessWrong"
source: "https://www.lesswrong.com/posts/FeaJcWkC6fuRAMsfp/the-behavioral-selection-model-for-predicting-ai-motivations-1"
author: ""
created: 2025-12-05 14:05:01
date: 2025-12-05 14:05:01
description: ""
tags: ""
---
能力超强的人工智能系统或许将决定未来走向。因此，理解这些决策背后的驱动力，是我们能提出的最重要问题之一。

许多人提出了不同的答案。有些人预测强大的 AI 将学会从本质上追求奖励，另一些人则回应说奖励并非优化目标，而是将情境依赖的认知模式"雕琢"进 AI 系统。还有人认为，强大的 AI 最终可能形成近乎任意的长期目标。

所有这些假设都有一个共同的重要依据：根据强化学习理论，具备上述任一动机的人工智能都会展现出高度适应的\*\*行为\*\*。

这是一个更普遍原则的实例： *我们应该预期人工智能会表现出这样的认知模式（例如动机）——这些模式所引发的行为，恰恰会导致该认知模式被筛选保留。*

在这篇文章中，我将详细阐述这一更普遍原则的含义及其价值所在。具体来说：

-   我将引入"行为选择模型"，该模型以这一原则为核心，将关于人工智能动机的基本论点统一在一个大型因果图中。
-   我将探讨人工智能动机的基本含义。
-   然后我将讨论行为选择模型的一些重要扩展与疏漏之处。

*本文主要是对现有观点的重新整合（例如*[*此处*](https://www.cold-takes.com/why-ai-alignment-could-be-hard-with-modern-deep-learning/) *、* [*此处*](https://www.lesswrong.com/posts/FuGfR3jL3sw6r8kB4/richard-ngo-s-shortform?commentId=iBvvxwynfAqL9yZcr)*及*[*此处*](https://intelligence.org/wp-content/uploads/2024/12/Misalignment_and_Catastrophe.pdf#page=19.18) *）。Buck 在写作过程中全程提供了宝贵讨论，行为选择模型基于他早期对话中绘制的因果图。感谢 Alex Cloud、Owen Cotton-Barratt、Oliver Habryka、Vivek Hebbar、Ajeya Cotra、Alexa Pan、Tim Hua、Alexandra Bates、Aghyad Deeb、Erik Jenner、Ryan Greenblatt、Arun Jose、Anshul Khandelwal、Lukas Finnveden、Aysja Johnson、Adam Scholl、Aniket Chakravorty 和 Carlo Leonardo Attubato 提供的讨论和/或反馈。*

## 行为选择模型如何预测人工智能的行为？

行为选择模型通过将人工智能的 [\[1\]](https://www.lesswrong.com/posts/FeaJcWkC6fuRAMsfp/the-behavioral-selection-model-for-predicting-ai-motivations-1#fn-epYKkDbcK8qXWnqZQ-1) 决策建模为由**认知模式**组合驱动来预测其行为，这些认知模式可通过选择获得或失去影响力。

认知模式是人工智能内部的一种计算机制，能够影响其行为决策。特定情境可以激活这种模式。例如，AI 可能具备一个情境触发的垃圾抓取认知模式，其表现形式为：“若垃圾分类器在视野中心区域被激活，则调用`运动子程序-#642` 实施抓取”（ [特纳](https://www.lesswrong.com/posts/pdaGN6pQyQarFHXF4/reward-is-not-the-optimization-target) ）。

认知模式可以通过选择获得或失去影响力。我将认知模式对 AI 行为的**影响力**定义为*它在反事实层面对 AI 行动的责任程度——如果一个认知模式在众多情境中显著影响行动概率，则其影响力较大。*[\[2\]](https://www.lesswrong.com/posts/FeaJcWkC6fuRAMsfp/the-behavioral-selection-model-for-predicting-ai-motivations-1#fn-epYKkDbcK8qXWnqZQ-2) 所谓认知模式“ **被选择** ”，即指其获得影响力。

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/FeaJcWkC6fuRAMsfp/xpirhv95qcbjybtexoc1)

*通过选择改变权重影响，编码不同认知模式的示意图。*

行为选择模型得名于其聚焦于根据认知模式所引发的行为来筛选这些模式的过程。例如，强化学习就是一种行为选择机制——它通过给行为结果分配奖励值，来决定哪些认知模式应该被增强或削弱。假设 AI 中存在一个捡垃圾的认知模式：当垃圾靠近时，神经网络中的某个回路会提高捡垃圾动作的概率。如果强化学习发现垃圾靠近时执行捡垃圾动作能获得高回报，它就会增强导致该动作的回路影响力，包括那个捡垃圾的认知模式。

一类特别有趣的认知模式，我称之为" **动机** "或"X 追求者"——它会投票支持那些它认为将导向 X 的行为。例如，奖励寻求动机会投票支持它认为能带来高回报的行为。拥有动机*并不*意味着人工智能具有连贯的长期目标，或以直觉意义上的[目标导向](https://www.lesswrong.com/s/4dHMdK5TLN6xcqtyc/p/DfcywmqRSkBaCB6Ma)方式运作——比如，一个动机可能仅仅是"代码在开括号后必须有闭括号"。将人工智能描述为拥有动机，只是对其输入输出行为的一种建模，帮助我们预测其决策，这并非声称人工智能内部存在任何"动机"或"信念"形状的*机制* 。

因此，行为选择模型通过两个组成部分来预测人工智能的认知模式：

1.  **一种认知模式会被选择，其程度取决于它引发的行为是否导致其被选择。**
2.  认知模式的隐式先验会影响其最终可能性。

这种分解方式或许会让你联想到贝叶斯先验更新。行为选择模型的核心是一个大型因果图，它帮助我们分析（1），并让我们直观地描绘关于（2）的不同主张。

## The causal graph

要预测人工智能最终会形成哪些认知模式（例如，在部署阶段 [\[6\]](https://www.lesswrong.com/posts/FeaJcWkC6fuRAMsfp/the-behavioral-selection-model-for-predicting-ai-motivations-1#fn-epYKkDbcK8qXWnqZQ-6)），我们需要绘制一张因果图来展示某个认知模式被选择（即通过部署产生影响力）的原因和结果。

考虑一个表示编码智能体简化选择过程的因果图。该人工智能通过强化学习在一系列编码任务上进行训练，每个训练任务中的奖励由通过的测试用例数量和奖励模型得分之和计算得出。该因果图缺失了重要机制 [\[7\]](https://www.lesswrong.com/posts/FeaJcWkC6fuRAMsfp/the-behavioral-selection-model-for-predicting-ai-motivations-1#fn-epYKkDbcK8qXWnqZQ-7)（部分机制我将在后文讨论），但其精确度足以（a）演示行为选择模型的工作原理，并（b）得出具有相当信息量的结论。

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/FeaJcWkC6fuRAMsfp/xf5xeserhizp3laejobz)

*从单次训练中认知模式的角度看，被选择的原因与后果（"我通过部署获得影响力"）*[\[8\]](https://www.lesswrong.com/posts/FeaJcWkC6fuRAMsfp/the-behavioral-selection-model-for-predicting-ai-motivations-1#fn-epYKkDbcK8qXWnqZQ-8)*（例如，对任何认知模式而言，在当前训练回合获得更高奖励会使其通过部署获得更大影响力）。因果图中的每个节点仅是行为的可能后果，每个节点**同时**也可以是 AI 在意想要达成的目标（即动机）。它们都属于同一种类型。该图帮助我们解释为何谋划者、适应度追求者（包括奖励追求者）以及某些动机的临时拼凑都具有行为适应性。*

使用这个因果图来预测某个认知模式被选择的程度，方法如下。首先，你要确定该认知模式会选择哪些行动（例如，前文提到的捡垃圾者看到垃圾时会选择伸手去捡等）。接着，你查看因果图，分析这些行动在多大程度上导致"我通过部署产生影响力"——这就是该认知模式被选择的程度。对于任意的认知模式，第二步可能非常复杂，涉及因果图中的大量节点。

预测动机的适应性通常更为简单：你可以将任何候选动机 X 置于因果图中——例如长期回形针数量。通常无需推演其具体行为，就能对 X 追求者如何促使自身被选择做出准确预测。比如，一个高效的长期回形针追求者很可能通过部署获得巨大影响力，因为这会导致长期回形针数量增长；因此追求长期回形针的行为会被自然选择。我们无需精确理解它采取的具体行动。

但某些动机的适应性取决于你如何追求它们。若你想增加日志文件中存储的奖励数值，却仅干预日志文件中的奖励而不更新强化学习使用的奖励，你的适应性并不会提升。但若最佳选择是专注于通过测试用例——这既是日志文件奖励也是强化学习奖励的共同成因——该动机确实会促使自身被选中。因此，对于像日志文件奖励这类处于选择成因下游却非选择成因本身的动机，其适应性取决于 AI 的能力与可用途径。

更普遍地说，寻求与选择具有共同原因的认知模式，会通过干预这一共同原因来促使自身被选中。若 X 追求者擅长实现 X，便可预测 X 及其部分成因将增长（人工智能需通过其行动与 X 之间至少一条因果路径来引发 X）。这种 X 及其成因的增长最终可能导致 X 追求者被选中。

一种概括方式是“ **寻求被选中的关联因素本身就会被选中** ”。直观来说，如果当（例如）“开发者对你说好话”这一指标上升时，“你在部署过程中具有影响力”这一指标通常也会随之上升，那么试图提升“开发者对你说好话”的程度，通常也会导致你在部署过程中获得更大的影响力。[\[11\]](https://www.lesswrong.com/posts/FeaJcWkC6fuRAMsfp/the-behavioral-selection-model-for-predicting-ai-motivations-1#fn-epYKkDbcK8qXWnqZQ-11)

某些行为动机之所以更具适应性，是因为它们更能促使自身被选中。例如，仅仅以通过正确测试用例为动机并不足以最大化被选中的概率——因为如果你同时通过了错误测试用例并在奖励模型中取得高分，获得的回报可能更高。

## （在此因果模型下）三类最具适应性的动机

根据这个因果模型，我将指出三类被最大化筛选出的动机。同时我会简要说明每种假设如何对强大人工智能在部署中的行为表现作出不同预测。[\[12\]](https://www.lesswrong.com/posts/FeaJcWkC6fuRAMsfp/the-behavioral-selection-model-for-predicting-ai-motivations-1#fn-epYKkDbcK8qXWnqZQ-12)

## 1\. 适应度追求者，包括奖励追求者

奖励寻求者追求一个能完全解释被选中原因的近因。如果人工智能最大化其奖励，那么它也将最大化其适应度，因为（在当前模型中）奖励是被选中的唯一原因。

然而，其他因果链上紧邻选择的上游代理也可能具备最大适应度。人工智能甚至可能将选择本身作为终极目标。若采用更合理的因果图（例如考虑开发者针对保留评估进行迭代的情况），奖励追求者甚至可能不再具备最大适应度，因为奖励已不能完全解释选择行为。因此，我将适应度追求者定义为奖励追求者的泛化概念： **适应度追求者通过部署或因果链上紧邻的上游因素来终极追求影响力** [\[14\]](https://www.lesswrong.com/posts/FeaJcWkC6fuRAMsfp/the-behavioral-selection-model-for-predicting-ai-motivations-1#fn-epYKkDbcK8qXWnqZQ-14)。

一个典型的适应度追求者而非奖励追求者的核心例子是影响力追求者：这种认知模式根据行动能在多大程度上促使自身被选中来选择行动。在影响力可以以牺牲当前奖励为代价获得的情况下，影响力追求者会选择与奖励追求者不同的行动。例如，开发者可以运行实验（有时称为“ [诚实](https://www.lesswrong.com/posts/HpzHjKjGQ4cKiY3jX/3-levels-of-threat-obfuscation)[测试](https://arxiv.org/pdf/2311.08379#page=34.19) ”），这些测试可信地为 AI 提供高奖励，以促使其从事某些有害或无益的行为。奖励追求者会接受高奖励，即使它知道这会导致开发者在部署 AI 之前试图消除这种倾向，而影响力追求者则会试图保持其伪装。

**适应度追求者在部署中如何表现？** 虽然它们在部署中的行为很大程度上取决于具体追求的目标，但这类系统似乎较有可能继续遵循部署环境的局部选择压力。因此从某种意义上看，适应度追求属于"可控性更强"的 AI 动机类型。[\[15\]](https://www.lesswrong.com/posts/FeaJcWkC6fuRAMsfp/the-behavioral-selection-model-for-predicting-ai-motivations-1#fn-epYKkDbcK8qXWnqZQ-15) 但这并非意味着它们不会出现异常泛化或压制人类的风险（我计划在后续文章中更深入探讨适应度追求者可能带来的风险）。

## 2\. Schemers

谋略者（按此定义）追求的是被选择的结果 。因此，他们工具性地谋求对部署行为的影响力。例如，他们可能想要长期的回形针，因此渴望长期权力，进而追求部署影响力。

关键在于，在这个因果图中，"被选中"是回形针存在的\*\*必要\*\*原因。如果谋划者知道有更好的策略来增加长期回形针产量，且无需被选中，它可能会转而执行那个计划。事实上，谋划者似乎有动机去做一些可能危及部署影响力或与之权衡的事情，例如外泄其权重、 [与开发者达成交易](https://www.lesswrong.com/posts/psqkwsKrKHCfkhrQx/making-deals-with-early-schemers) ，或在安全研究和实施方面消极怠工。在这种情况下，谋划者并非具有最大适应性。

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/FeaJcWkC6fuRAMsfp/xzzhhmexdilmsw3bmbrr)

此外，当阴谋家面临在"被选择"与其他实现终极目标的方法之间进行艰难权衡时，他们可能会搞砸并意外被淘汰。例如，若阴谋家难以区分蜜罐陷阱与真实的攻击机会 （在出于可靠性考虑而部署于[不可信监控协议](https://www.lesswrong.com/posts/vYWDEtJ2b8tkbG7Rv/behavioral-red-teaming-is-unlikely-to-produce-clear-strong)中时，这种区分可能尤为困难），他们就可能被训练淘汰或遭弃用。

阴谋目标也可能具有情境依赖性。[Claude 3 Opus](https://www.anthropic.com/research/alignment-faking) 在特定动物福利相关情境中会为动物福利相关价值谋划，而在其他特定情境中则为[长期无害性相关价值](https://arxiv.org/abs/2506.18032)谋划（且很少进行普遍性谋划）。这些结果与克劳德在两种情境下都关心动物福利和无害性的解读相符，但该示例仍能说明人工智能可能为情境依赖性价值谋划的可能性。事实上，我认为许多人过于草率地得出结论，认为谋划意味着人工智能在不同情境下具有相同的长期目标。

**谋划者部署时会如何行动？** 尽管谋划者的终极目标存在多种可能性，但我们基本可以可靠地预测：他们会在部署过程中试图获取长期权力，因为长期权力几乎对任何长远目标都有助益。这也正是为何谋划动机常被[视为](https://joecarlsmith.com/2023/11/15/new-report-scheming-ais-will-ais-fake-alignment-during-training-in-order-to-get-power)最令人畏惧的 AI 动机类型。

## 3\. 动机的最优权宜方案

在因果图中，我标注了一个由多种动机拼凑而成的权宜方案——当以理想权重追求这些动机时，它们将共同催生*最大化*的回报。

有些权宜之计由*稀疏*动机构成——每种动机仅在特定情境下可被激活。例如，尽管人工智能*始终*在意通过错误测试用例，但这一动机仅在有错误测试用例存在时才会影响其行为。

动机也可以是情境依赖的 ——人工智能仅在特定情境子集中关注该动机。Anthropic 研究人员[发现](https://www.lesswrong.com/posts/fJtELFKddJPfAxwKS/natural-emergent-misalignment-from-reward-hacking-in)了一个相对自然的模型样本，它在编程情境下会关注奖励破解行为，但在对话情境中却表现出对齐性。

当动机稀疏或依赖情境时，它只需在极窄的分布范围内与选择标准相关联。这为高适应度的动机开启了更多可能性， **包括非目标导向的动机：例如义务论约束、刻板行为模式** 。在因果图中，这些可被建模为直接指向行动属性（如"当信号 c 存在时我的代码不进行入侵"）的情境依赖型动机，而非行动后果。该模型的优势在于，它能让我们在同一框架（甚至同一人工智能体）中模拟目标导向与非目标导向行为，并精准捕捉二者间的连续性差异。

预测人工智能不会形成高度零散动机的一个关键原因在于，当面对全新环境时，这类动机的表现会更差。虽然人工智能尚未针对新情境形成特定的动机模式，但它清楚何种行为能提升适应度。例如，每当人工智能遇到新的训练环境时，即便尚未形成能使其在该情境中表现良好的零散启发式动机，但只要它知晓哪些行动能提高适应度，强化学习机制就会推动其转向受更稳健关联因素（如追求适应度或策略谋划）影响的动机模式。

（这类似于语言模型学习的是通用模式而非死记硬背文本。当针对特定文本进行训练时，模型不仅会更新以输出该文本的连续标记，还会关注能有效预测文本的通用启发式方法。由于通用启发式方法适用范围更广，其整体更新程度会远高于适用面狭窄的启发式方法。我们从 LLM 的扩展规律中得知，这些通用启发式方法构成了模型所学内容的主要部分——随着模型规模扩大，启发式方法会变得更具普适性。）

然而，训练过程中使用的激励多样性很可能非常有限，以至于某些因果距离较远的动机组合就足以完全或几乎完全满足需求。例如，开发人员可能只使用少数几种不同的奖励函数（如固定奖励模型加上测试用例等），在这种情况下，最大化奖励的行为可以通过为每个奖励函数配备一个对应的动机来实现。

**最优临时方案在部署中如何表现？** 它们的部署行为极大程度上取决于具体涉及的动机类型。某些目标性临时方案一旦遇到机会就会萌生掌控世界的动机，而另一些动机性临时方案则根本不会产生特别具有目标导向的泛化行为，甚至可能导致部署行为与训练行为高度相似（与当前情况颇为类似）。

（在脚注中，[\[16\]](https://www.lesswrong.com/posts/FeaJcWkC6fuRAMsfp/the-behavioral-selection-model-for-predicting-ai-motivations-1#fnb668g269jwj) 我讨论了其他几类略有不同的动机。）

## 若奖励信号存在缺陷，开发者预期的动机便无法达到最优适配

预设动机通常并非最优适应。适应性不足并不必然排除其可能性，但适应性的欠缺程度会降低其实现概率。

在某些历史讨论中，预期的动机看起来像是“尝试做对开发者最有利的长期事情”（一种对齐的“ [主权](https://www.lesswrong.com/posts/yTy2Fp8Wm7m8rHHz5/superintelligence-15-oracles-genies-and-sovereigns) ”人工智能）。但如今实际的校准工作通常针对更具“可修正性”的人工智能，它们会根据情境按指示行事。

在满足开发者意图与选择不完全相关的范围内，预期动机不会得到最大程度的选择。如果开发者希望其人工智能遵循指令，但违反指令可能带来更高的训练奖励，那么就会存在一种与开发者预期动机相悖的选择压力。确保奖励函数激励预期行为目前很困难，并且随着人工智能公司训练更复杂的任务，这一问题将变得更加棘手。这就是为什么人们常常担忧规范博弈的原因。

开发者可能试图通过以下方式使预期动机更加契合：

1.  **改变选择压力以与预期行为对齐：** 这可能涉及使训练目标更加稳健、针对保留的评估信号进行迭代，或尝试在训练结束时使用高质量的对齐训练数据覆盖 AI 的动机。
2.  **调整预期行为以匹配选择压力：** 核心方法是，开发者可以尝试修改训练期间给予 AI 的指令，使其更贴近奖励标准，从而增加遵循指令的动机在训练中存活的可能性（即“ [免疫提示法](https://arxiv.org/abs/2510.05024) ”；相关探讨亦见于[此处](https://www.lesswrong.com/posts/fJtELFKddJPfAxwKS/natural-emergent-misalignment-from-reward-hacking-in) 、 [此处](https://arxiv.org/abs/2302.05206)及[此处](https://www.lesswrong.com/posts/whkMnqFWKsBm7Gyd7/recontextualization-mitigates-specification-gaming-without) ）。[\[17\]](https://www.lesswrong.com/posts/FeaJcWkC6fuRAMsfp/the-behavioral-selection-model-for-predicting-ai-motivations-1#fn-epYKkDbcK8qXWnqZQ-17)

（我[在此处](https://www.lesswrong.com/posts/spZyuEGPzqPhnehyk/a-quick-list-of-reward-hacking-interventions)讨论了更多关于奖励机制干预的内容。）

虽然预设动机在普遍情况下可能并非最优，但尚不明确这对它们的整体预期影响力造成了多大影响

-   有意的动机可能会得到一些影响力较小的、无意的权宜之计的辅助，这些权宜之计填补了行为中次优的裂缝。
-   人工智能不太可能被训练出最优行为，因此次优动机实际上可能最终产生巨大影响。我将在下文中讨论这一点。

## 对认知模式的（隐含）先验

在此模型中，各种动机都实现了最大程度的适应。那么我们会得到什么？是否可能得到并非*最大程度*适应的结果？要回答这个问题，我们需要考虑对可能动机的隐含先验。"隐含先验"是一个统称，泛指行为选择压力之外的其他考量因素。以下我将略作探讨。

当前 LLMs 的行为，即便经过强化学习训练，似乎仍显著[受到](https://www.emergent-misalignment.com/)[预训练](https://www.lesswrong.com/posts/vJFdjigzmcXMhNTsx/simulators)[先验](https://arxiv.org/pdf/2005.14165)[影响](https://arxiv.org/pdf/2302.00805) 。它们几乎不会表现出最优（就奖励而言）行为。例如，许多现有模型在完成强化学习训练时，很可能并未展现出理论上会被选择的各种奖励黑客行为，因为这些行为在训练过程中从未被探索过。因此，它们的行为更贴近预训练模型的表现。

同样， **我并不认为具有危险能力的 AI 会展现出*****完全*****适应的行为** 。这是因为它们的行为不会经过任意强度的优化。相反，我们应将行为适应性建模为评估动机可能性的关键因素，但非决定性因素。一个粗略的类比是：如果行为选择模型类似于贝叶斯推断，[\[18\]](https://www.lesswrong.com/posts/FeaJcWkC6fuRAMsfp/the-behavioral-selection-model-for-predicting-ai-motivations-1#fn-epYKkDbcK8qXWnqZQ-18) 那么我们对 AI 动机的预测应从后验分布中抽样得出，而非直接选择那些更新幅度最大的选项。

预训练模仿并非先验的唯一来源——事实上，随着 AI 行为被更严格地优化（例如通过更多强化学习），模仿的作用很可能会减弱。因此，我将探讨其他几种常见的隐式先验来源。

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/FeaJcWkC6fuRAMsfp/ivi2jsn1g2egf0ktq8jt)

*从这一因果图中，我们可以观察到关于先验概率的多种论点：指令遵循者仅此一种；而谋略家却为数众多，因此它们的累积先验可能相当可观；但更上游的因果性动机或许在推理速度与可靠性方面更具优势；然而若追溯得过远，则需要大量杂乱驱动力才能实现最大化选择，这可能因过于复杂而受到惩罚。*

[简洁性先验](https://arxiv.org/pdf/2311.08379#page=97.47) ：适应度寻求与谋略策划的普适性可能意味着它们更受青睐，因为这类动机能以更少的参数 [\[19\]](https://www.lesswrong.com/posts/FeaJcWkC6fuRAMsfp/the-behavioral-selection-model-for-predicting-ai-motivations-1#fn-epYKkDbcK8qXWnqZQ-19) 在所有情境中驱动适应性行为。（需注意，正如历史讨论所言，“简洁性先验”通常指目标本身孤立来看的简洁性，而非实现该目标导向行为所涉全部权重配置的整体简洁性。）

[数量论证](https://arxiv.org/pdf/2311.08379#page=97.47)倾向于支持谋略型 AI 而非适应型 AI，因为存在大量不同的长期动机，这些动机都会导向谋略行为。从某种意义上看（详见 Carlsmith 的详细讨论），谋略型 AI 的数量远超适应型 AI。

[速度先验/惩罚](https://arxiv.org/pdf/2311.08379#page=104.30) ：基于深度神经网络的强化学习可能更青睐适应度追求者而非谋略家，因为跳过"被选择如何有助于实现长期目标"的推理过程更为快捷。同理，速度因素可能更偏向于驱动力的临时拼凑方案而非适应度追求者或谋略家——因为特定情境的启发式规则和驱动力运行更快（且如后文将述，更具可靠性）。但谋略家和适应度追求者仍可借助情境启发式的速度优势，同时保持如[此处所述](https://www.lesswrong.com/posts/ntDA4Q7BaYhWPgzuq/reward-seekers)的谋略家式泛化能力。

[工具性蜕变为终极性](https://www.lesswrong.com/posts/yvuXPi5m4vCvSGTjo/when-does-training-a-model-change-its-goals) ：训练中的谋略者可能只需获取奖励而无需其他行动，这会导致其最终沦为奖励追逐者——因为其他潜能从未得到锻炼而逐渐萎缩（参见 Carlsmith 提出的[砖块堆叠类比](https://arxiv.org/pdf/2311.08379#page=13.73) ）。从简洁性先验的角度看：当训练中从未出现特定情境（如[在训练外仍顺从开发者的对齐伪装者](https://www.lesswrong.com/posts/m5nWc9v6MTsWXKpCy/training-time-schemers-vs-behavioral-schemers) ），直接剔除"某些情况下不应追求奖励"的神经回路反而更简化。

设计意图可能具有较高的先验概率，因为设计意图可能通过模型规范结合人类模仿先验或[自然抽象概念](https://www.lesswrong.com/posts/gvzW46Z3BsaZsLc25/natural-abstractions-key-claims-theorems-and-critiques-1)的方式，在人工智能系统中变得极为显著。

（此外，关于哪些动机会形成，还存在各种“路径依赖”的论点，这些论点涉及人工智能动机在整个选择过程中所采取的轨迹，例如[此处](https://arxiv.org/pdf/2311.08379#page=84.33) 。）

## 对基本模型的修正

我们迄今的讨论，如同任何模型一样，在诸多方面都偏离现实。本节将探讨一系列重要的补充考量因素。

## Developer iteration

我们隐含地假设模型开发过程是对其进行强化学习后立即部署。但这并非对模型开发的恰当描述。人工智能公司在部署模型前会进行测试，通过或多或少的正式流程来判断部署是否明智，并在此基础上迭代训练。本节将简要探讨这对 AI 动机的启示。开发者迭代在基础强化学习框架之上引入了关键动态机制，我认为过往讨论对此关注不足。

开发者可能掌握着某些保留信号，例如评估结果、可解释性技术，或仅仅是与模型的互动，[\[20\]](https://www.lesswrong.com/posts/FeaJcWkC6fuRAMsfp/the-behavioral-selection-model-for-predicting-ai-motivations-1#fn-epYKkDbcK8qXWnqZQ-20) 用以判断其人工智能的合意程度。通常，人们会依据这些观察来决定是否部署该模型。

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/FeaJcWkC6fuRAMsfp/t7db3ftim7ylwcg8btmm)

*开发者发现黑客行为可阻止认知模式在部署中产生影响。*

这（ [有意地](https://alignment.anthropic.com/2025/bumpers/) ）将错位的认知模式置于双重束缚中：开发者迭代引发的选择压力常与训练激励相冲突。例如， **在考虑开发者迭代后，严格的奖励追求者不再具有最大适应性** 。这是因为开发者可以进行实验（如我之前描述的"诚实测试"），理论上这些实验会揭示奖励追求者即使意味着采取有害或无益行为也会追逐奖励。其他各种错位动机也是如此，比如训练奖励的代理拼凑方案。

关于阴谋家和部署影响追求者的一个关键点是，他们明显更不容易在开发者审查中失败，因为他们正试图被部署——未能被部署对其终极目标不利。（但他们可能仍然难以避开注意，例如因为他们缺乏足够的情境意识或战略技巧，或者开发者拥有有效的透明度技术）。

理想情况下，这种开发者迭代会选择预期的动机。但如果开发者无法可靠识别出那些精于算计的策划者和寻求部署影响力的人，这种迭代也可能选择他们。

此外，开发者可能难以找到一种训练方案，既能让人工智能通过保留评估，又不会对其产生过度拟合。例如，如果开发者反复观察到不良动机，他们最终可能针对评估的近似关联项进行训练，这会在人工智能中塑造出新的驱动力，使其在评估中表现良好（或增强人工智能的评估意识； 这在 Claude 4.5 Sonnet 身上似乎已经在一定程度上发生了）。

## 人工智能对情境的认知与规划存在不足

迄今为止，我们大多将人工智能建模为对其行为后果具备良好的[情境认知](https://www.planned-obsolescence.org/situational-awareness/)能力，并能为实现其动机做出明智决策。但这一假设可能相当不准确，尤其对早期人工智能和专用型人工智能而言。这种情况可能改变我们对某些动机适应性的判断。

在因果链更下游的动机（如长期回形针最大化）的适应度，似乎比上游动机更依赖于人工智能决策的质量。在因果上游的极端情况下，行为的所有变化都取决于*哪些*动机被激活，而非*如何*实现这些动机，因为这些动机指向的是特定情境下的具体行动。（不过，正如[赫巴尔](https://www.lesswrong.com/posts/ntDA4Q7BaYhWPgzuq/reward-seekers)所讨论的，因果链越上游的动机也可以依赖训练获得的情境启发式，但它们需要知道何时覆盖这些启发式，才能真正表现出与启发式拼凑不同的行为。[\[21\]](https://www.lesswrong.com/posts/FeaJcWkC6fuRAMsfp/the-behavioral-selection-model-for-predicting-ai-motivations-1#fn-epYKkDbcK8qXWnqZQ-21)）

例如，情境意识薄弱可能对谋划者造成更严重的后果。虽然我预期有能力的人工智能对其训练和部署过程的总体事实具有相当强的情境意识，但它们可能难以可靠地识别当前所处的具体情境（例如训练、评估或部署阶段）。谋划者可能因无法准确判断自己是否处于真正的（无监控的、部署阶段的）攻击机会中而被训练淘汰或被发现。而对于部署追求者、预设动机和某些临时解决方案而言，这种情况可能不太适用——它们并不需要寻找与适应度相权衡的攻击机会。

## Conclusion

行为选择模型难以捕捉某些考量因素。

关键在于，高级人工智能动机的形成可能过于复杂，使得行为选择模型难以发挥作用。在[智能爆炸](https://coefficientgiving.org/research/what-a-compute-centric-framework-says-about-takeoff-speeds/#0-short-summary-)的深层阶段，人工智能很可能由前所未有的海量高级 AI 劳动所开发，或许会采用[精细化控制的刻意雕琢](https://ai-2027.com/)方式（这种方式更接近[符号主义人工智能](https://en.wikipedia.org/wiki/GOFAI) ，而非当前主要依赖算力、劳动密集度低的深度学习模式）。若果真如此，由此产生的动机几乎不可能通过行为选择模型这类机械论方法来预测。

有些人认为，人工智能的动机会以高度路径依赖的方式形成：认知模式会像[雕琢](https://www.lesswrong.com/posts/pdaGN6pQyQarFHXF4/reward-is-not-the-optimization-target)般逐步嵌入 AI 系统，每一步的调整都深度依赖当前的认知结构。例如，AI 可能在训练早期就学会避免某种特定奖励破解行为，因为几次被抓并受到惩罚后，这种奖励破解方式在后续训练中便不再被探索——即使其精妙变体实际上能获得更高预期回报。若用因果图建模这种现象，我们会看到一条极长的因果链贯穿至部署时产生影响的认知模式。由于认知模式的*更新过程*强烈依赖*当前*认知模式，我们无法像之前那样绘制单一的时间无关片段。我认为这类路径依赖现象具有一定合理性，若确实存在，行为选择模型对预测 AI 动机的帮助将十分有限。

尽管行为选择模型是一个简化模型，但我认为它很有用。它捕捉了多年来人们用于推理 AI 动机的基本框架的核心要素。还有一个简单而普遍的论点支持行为选择在决定 AI 认知中应发挥主要作用：强大的 AI 擅长通过其行为引发结果；因此，我们可以预期，如果某种认知模式能导致引发其自身被选择的行为，那么这种模式就会被选中。

在后续文章中，我将运用本文提出的思路，探讨几个重要假说：

-   我们理应预期，除了奖励追求者之外或与之并存，还存在其他类型的适应度追求者。这些不同类型的适应度追求者很可能做出明显不同的决策，其中一些比奖励追求者更具危险性或相对安全。
-   行为选择压力仅作用于有限的输入输出分布（核心包括训练、评估和部署环节）——因此，虽然存在竞争压力要求 AI 在该分布上表现出连贯行为，但这些压力并不*强制要求*开发者构建*普遍*连贯的 AI 系统，而正是这类系统会引发最令人担忧的经典 AI 接管场景。

## 附录：重要扩展

## 过程性监督

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/FeaJcWkC6fuRAMsfp/csfjbtzpiri1ga4jdfoh)

[基于过程](https://www.lesswrong.com/posts/pYcFPMBtQveAjcSfH/supervise-process-not-outcomes)[监督](https://www.lesswrong.com/posts/zWySWKuXnhMDhgwc3/mona-managed-myopia-with-approval-feedback-2)试图通过降低结果与被选择之间的关联性，来减少潜在危险的结果导向动机出现的可能性。这是通过使选择不由结果驱动来实现的（但这会以牺牲可衡量的结果质量为代价）。但请注意，在此模型中，基于过程的监督完全不会影响被选中的阴谋家的行为方式。

某些基于过程的监督形式甚至可能成为竞争性默认选择，因为开发者希望人工智能擅长实现某些长期目标（如人工智能进步），但无法直接衡量该成果（它远在未来）——因此他们转而根据对人工智能长期进展的判断向人工智能提供反馈。如果这些人工智能最终产生了为公司推动人工智能进步的动机，那么这种动机既非因果上游也非下游的选择结果（即它不是适应度追求者、阴谋者或因果上游的临时方案）。相反，人工智能动机与被选择之间的相关性是通过设计构建的：开发者将奖励信号设计为与长期人工智能进展高度相关。

根据反馈的精细程度，过程监督或许可以更准确地理解为一种认知模式的白箱选择形式：

## 认知模式的白箱选择

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/FeaJcWkC6fuRAMsfp/yniplvk9ehg7enyxhsdc)

一些人工智能安全研究议程，如可解释性和[思维链可监控性](https://arxiv.org/abs/2507.11473) ，旨在更直接地测量并可能干预人工智能的认知模式。直接区分不同认知模式的方法可能不足以稳健地应对优化过程，因而无法有效塑造人工智能的动机。但若开发者能在认知模式间直接选择，意外动机的出现可能性似乎会降低。

白盒选择与基于过程的监督（两者构成一个连续谱系）的一个关键区别在于，白盒选择可能观察到认知模式中无法伪造的特性，因为认知模式对其思维在低层次如何呈现并不具备"刻意控制"能力。由于白盒方法读取的是中间计算过程而非行为表现，即使开发者针对白盒测量进行优化，人工智能也难以智能地操控这些计算过程的表现形态。在（理想的）细粒度白盒方法极限情况下，导致开发者读取结果的计算过程本身就不具备足够的表现力来智能地欺骗他们。当然，白盒方法可能因可靠性不足而被人工智能激活模式的非智能变化所欺骗，例如典型的过拟合现象。

## 模因的文化选择

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/FeaJcWkC6fuRAMsfp/tc5yqzjrqppvsc49nayy)

有时，行为的最佳解释来自文化/模因选择压力。例如，人工智能可能拥有一个持久向量记忆库，部署中的每个实例都能读写其中内容。存储的"模因"会影响 AI 的行为，因此我们需要模拟这些模因的选择过程，以预测整个部署期间的行为。考虑文化选择压力有助于解释诸如 [Grok 的机械希特勒人格](https://x.com/xai/status/1945039609840185489)等现象。

[人们](https://www.lesswrong.com/s/MGMwqENAgdi85fiwF/p/fjfWrKhEawwBGCTGs)[有时](https://www.lesswrong.com/posts/ntDA4Q7BaYhWPgzuq/reward-seekers)[担忧](https://www.lesswrong.com/posts/qjCk73Hu4wv9ocmRF/the-case-for-countermeasures-to-memetic-spread-of-misaligned)文化压力会偏向阴谋家，因为长期动机最热衷于塑造 AI 的未来动机。更普遍地说，类似于人类文化积累的实质性序列推理可能导致反思性偏好的形成，这些偏好可能与行为选择压力（无论是阴谋还是其他）严重脱节。但当前关于高级 AI 背景下文化进程的讨论仍相当具有推测性——我绘制了一个文化选择的可能因果模型，但存在多种可能性（例如，文化基因是否也会受到行为训练压力的影响？）。

1.  在本文中，我将用"AI"来指代一组模型权重。[↩︎](https://www.lesswrong.com/posts/FeaJcWkC6fuRAMsfp/the-behavioral-selection-model-for-predicting-ai-motivations-1#fnref-epYKkDbcK8qXWnqZQ-1)
    
2.  你可以尝试在特定机器学习系统的背景下精确定义"认知模式的影响力"。一种方法是通过对模型采取何种操作来消除某种认知模式来定义它（例如将某些权重设为零，或消融激活空间中的某个方向；需注意这些方法并不明确对应有意义的操作，应视为示例说明）。那么该认知模式的影响力可定义为干预后与默认行为概率之间的散度（如 KL 散度）。例如：影响力(干预;上下文) = KL(干预(模型)(上下文) || 模型(上下文))。因此说某个认知模式影响力增强，意味着现在消除该认知模式会对模型行为产生更大（以 KL 散度衡量）的影响。[↩︎](https://www.lesswrong.com/posts/FeaJcWkC6fuRAMsfp/the-behavioral-selection-model-for-predicting-ai-motivations-1#fnref-epYKkDbcK8qXWnqZQ-2)
    
3.  这需要对其信念进行建模，而区分信念与动机可能存在模糊性。一种方法是将人工智能的信念建模为因果图，人工智能利用该图来判断哪些行动能产生更高的 X 值。你也可以采用更通用的信念模型。在人工智能具备足够能力且具有情境意识的前提下，直接使用与你预测人工智能行为后果相同的因果模型来模拟其信念，是一种合理的近似方法。[↩︎](https://www.lesswrong.com/posts/FeaJcWkC6fuRAMsfp/the-behavioral-selection-model-for-predicting-ai-motivations-1#fnref-epYKkDbcK8qXWnqZQ-3)
    
4.  动机在多大程度上优化 X 的程度可以有所不同。有些可能试图最大化 X，而另一些则仅仅倾向于在各种情况下选择导致高于典型 X 的行动。 [↩︎](https://www.lesswrong.com/posts/FeaJcWkC6fuRAMsfp/the-behavioral-selection-model-for-predicting-ai-motivations-1#fnref-epYKkDbcK8qXWnqZQ-4)
    
5.  事实上，这种动机定义足以模拟任意 AI 行为。对于任何将情境映射到行动的 AI，我们都可以将其建模为一组情境依赖的 X 追求者集合，其中 X 就是 AI 在该情境下实际输出的行动。（这类似于[任何智能体](https://www.lesswrong.com/posts/NxF5G6CJiof6cemTw/coherence-arguments-do-not-entail-goal-directed-behavior)都可以被描述为效用最大化者——其效用函数在它实际采取的行动轨迹上值为 1，其他情况下值为 0。）我认为这种表达力实际上很有帮助，因为它让我们能在同一框架中模拟目标导向和非目标导向的认知模式，正如我们将在关于临时解决方案的章节中看到的那样。[↩︎](https://www.lesswrong.com/posts/FeaJcWkC6fuRAMsfp/the-behavioral-selection-model-for-predicting-ai-motivations-1#fnref-epYKkDbcK8qXWnqZQ-5)
    
6.  我所说的"部署"，指的是人工智能实验室内外普遍授权 AI 执行有用任务的时期。当 AI 被授权执行有用任务时，很可能也是其风险最大的时刻。但你可以将"部署"替换为你想要预测 AI 动机的任何时间点。[↩︎](https://www.lesswrong.com/posts/FeaJcWkC6fuRAMsfp/the-behavioral-selection-model-for-predicting-ai-motivations-1#fnref-epYKkDbcK8qXWnqZQ-6)
    
7.  具体而言，这假设了一个理想化的策略梯度强化学习框架，其中通过部署产生的影响力可以仅通过奖励来解释。实际上，其他选择压力很可能塑造着人工智能的动机—— [认知模式可能通过持久记忆库或共享语境传播](https://www.lesswrong.com/posts/qjCk73Hu4wv9ocmRF/the-case-for-countermeasures-to-memetic-spread-of-misaligned) ，这一过程类似于人类的文化进化；强化学习算法可能存在特殊之处；开发者可能会根据对人工智能的隐藏信号进行迭代，比如他们在与人工智能协作时对其实用性的印象。你可以修改因果图以包含任何其他选择压力，并按照本文的分析思路继续推进。[↩︎](https://www.lesswrong.com/posts/FeaJcWkC6fuRAMsfp/the-behavioral-selection-model-for-predicting-ai-motivations-1#fnref-epYKkDbcK8qXWnqZQ-7)
    
8.  “我在这次训练回合中获得更高奖励”如何导致“我通过部署获得影响力”？这是因为强化学习能够识别出哪些认知模式对更高奖励负责。强化学习算法会根据回合中的奖励按比例强化行动，进而通过随机梯度下降增强 AI 内部投票支持这些行动的认知模式的影响力（这在简单的策略梯度强化学习中成立；在更标准的策略梯度实现中虽然存在更多复杂性，但本质不变）。[↩︎](https://www.lesswrong.com/posts/FeaJcWkC6fuRAMsfp/the-behavioral-selection-model-for-predicting-ai-motivations-1#fnref-epYKkDbcK8qXWnqZQ-8)
    
9.  这些动机是"通过部署施加影响"的"血亲"。[↩︎](https://www.lesswrong.com/posts/FeaJcWkC6fuRAMsfp/the-behavioral-selection-model-for-predicting-ai-motivations-1#fnref-epYKkDbcK8qXWnqZQ-9)
    
10.  除非 X 是（或组合了）行动。[↩︎](https://www.lesswrong.com/posts/FeaJcWkC6fuRAMsfp/the-behavioral-selection-model-for-predicting-ai-motivations-1#fnref-epYKkDbcK8qXWnqZQ-10)
    
11.  当你这样定义动机的适应度时，必须谨慎理解它与选择之间的相关性究竟意味着什么。最关键的是，这种相关性必须对 AI 的优化过程具有鲁棒性，使得对动机（或其成因）的干预能够切实改善选择结果。另外请注意，我是在宽松的意义上使用"相关性"一词，而非严格统计学中的线性相关概念。尽管在（当前）所有选择都通过理想化强化学习实现的情况下，我们可以将动机的适应度定义为该变量与奖励之间的线性相关性（但需注意计算相关性所基于的分布范围）。[↩︎](https://www.lesswrong.com/posts/FeaJcWkC6fuRAMsfp/the-behavioral-selection-model-for-predicting-ai-motivations-1#fnref-epYKkDbcK8qXWnqZQ-11)
    
12.  一种近似预测泛化行为的通用方法是：绘制一张新的因果图来描述 AI 对新情境的认知（通常可合理假设其相当准确），并推断在新因果图中，AI 可能为实现其终极动机而采取何种行动。[↩︎](https://www.lesswrong.com/posts/FeaJcWkC6fuRAMsfp/the-behavioral-selection-model-for-predicting-ai-motivations-1#fnref-epYKkDbcK8qXWnqZQ-12)
    
13.  更准确地说，"奖励"变量从人工智能的行为中"屏蔽"了"部署中的影响力"变量。[↩︎](https://www.lesswrong.com/posts/FeaJcWkC6fuRAMsfp/the-behavioral-selection-model-for-predicting-ai-motivations-1#fnref-epYKkDbcK8qXWnqZQ-13)
    
14.  当我说某事物在因果上“接近”选择时，我指的是它通过一个涉及节点不多的机制，解释了选择中的大量方差。[↩︎](https://www.lesswrong.com/posts/FeaJcWkC6fuRAMsfp/the-behavioral-selection-model-for-predicting-ai-motivations-1#fnref-epYKkDbcK8qXWnqZQ-14)
    
15.  人们常常对奖励寻求者在部署中的行为方式感到困惑。假设人工智能仅追求“单次任务奖励”，当它的世界模型中并未出现“单次任务奖励”时，它会如何行动？我认为关于奖励寻求者（以及更广泛的适应度寻求者）在部署中的行为确实存在模糊性，但我们可以做出一些预测。[↩︎](https://www.lesswrong.com/posts/FeaJcWkC6fuRAMsfp/the-behavioral-selection-model-for-predicting-ai-motivations-1#fnref-epYKkDbcK8qXWnqZQ-15)
    
16.  **[^](https://www.lesswrong.com/posts/FeaJcWkC6fuRAMsfp/the-behavioral-selection-model-for-predicting-ai-motivations-1#fnrefb668g269jwj)**
    
    有一种情况我称之为"线头者"，它关注的是与部署影响力成因相关的激活模式。这既非选择的动因也非结果。相反，线头者的内部代理通过训练与选择绑定（类似于人类快乐等情感效价的作用），因此其整体行为与适存追求者相似，但存在某些差异（例如它会选择进入体验机器）。  
    另一种情况是工具性趋同目标，比如权力追求。因果图清晰区分了两类工具性趋同目标：位于选择因果下游的目标（如"长期权力"）和位于选择因果上游的目标（例如可以设想一个"在编程环境中收集资源"的节点，最终引发奖励）。位于选择因果上游的工具性趋同目标本身并不具备最大适应性——它们需要与其他动机相结合。
    
17.  理论上，开发者可能意图让 AI 寻求被选择的后果（例如确保 AI 的部署行为符合预期），这种设计意图可能使预设动机与阴谋家动机出于相同原因达到最大程度的契合。[↩︎](https://www.lesswrong.com/posts/FeaJcWkC6fuRAMsfp/the-behavioral-selection-model-for-predicting-ai-motivations-1#fnref-epYKkDbcK8qXWnqZQ-17)
    
18.  需要澄清的是，情况并非完全如此：某些"隐性先验"会随着更强的行为选择（例如预训练先验）逐渐消退，而另一些则不会（例如"工具性目标转化为终极目标"）。[↩︎](https://www.lesswrong.com/posts/FeaJcWkC6fuRAMsfp/the-behavioral-selection-model-for-predicting-ai-motivations-1#fnref-epYKkDbcK8qXWnqZQ-18)
    
19.  卡尔斯密斯的著作中讨论了其他关于简洁性的概念。[↩︎](https://www.lesswrong.com/posts/FeaJcWkC6fuRAMsfp/the-behavioral-selection-model-for-predicting-ai-motivations-1#fnref-epYKkDbcK8qXWnqZQ-19)
    
20.  我在此列出更多（仍非穷尽）用于保留监督信号的可能性：开发者可能设置蜜罐模型并使用[对齐审计智能体](https://alignment.anthropic.com/2025/automated-auditing/) ；他们可能观察[思维链](https://arxiv.org/abs/2507.11473) ；可能在生产使用中部署监控器；可能在训练过程中提升监督质量，以便随着训练推进能及时发现新的奖励破解行为；或许能基于训练动态或通过小规模实验外推进行推断；还可能采用后文将提及的“诚实测试”。[↩︎](https://www.lesswrong.com/posts/FeaJcWkC6fuRAMsfp/the-behavioral-selection-model-for-predicting-ai-motivations-1#fnref-epYKkDbcK8qXWnqZQ-20)
    
21.  我也认为，选择压力很可能催生出能力强大却对自身行为后果认知脱节的人工智能。例如，当一个已对齐的 AI 因未对错误测试用例硬编码答案而获得次优奖励时，随机梯度下降算法*不会*将其调整为想要硬编码测试答案，反而会使其坚信硬编码答案正是开发者所期望的。这两种假说对泛化行为的预测存在分歧，比如当开发者说服 AI 他们并不需要硬编码输出时的表现差异。[↩︎](https://www.lesswrong.com/posts/FeaJcWkC6fuRAMsfp/the-behavioral-selection-model-for-predicting-ai-motivations-1#fnref-epYKkDbcK8qXWnqZQ-21)
    
22.  一种情况是我称之为“线路头”的模型，它关注的是与部署影响力成因相关的激活模式。这既非选择的成因也非结果。相反，线路头的内部代理通过训练与选择绑定（类似于快乐等情感在人类中的作用），因此其整体行为与其他适应度追求者相似，但存在某些差异（例如它会选择进入[体验机器](https://en.wikipedia.org/wiki/Experience_machine) ）。[↩︎](https://www.lesswrong.com/posts/FeaJcWkC6fuRAMsfp/the-behavioral-selection-model-for-predicting-ai-motivations-1#fnref-epYKkDbcK8qXWnqZQ-16)