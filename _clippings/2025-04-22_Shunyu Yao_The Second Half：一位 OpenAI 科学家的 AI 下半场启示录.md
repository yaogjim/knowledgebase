---
title: "The Second Half：一位 OpenAI 科学家的 AI 下半场启示录"
source: "https://mp.weixin.qq.com/s/iBVj-bcEtVbOGWEqwWp6EA"
author:
  - "[[Shunyu Yao]]"
published: 2025-07-11
created: 2025-04-22
description: "效用问题是当下 AI 领域最重要的问题。"
tags:
  - "clippings"
---
Shunyu Yao *2025年04月17日 14:32*

[![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgwMicjr8L9dRRJLEkSNsgIVRriaEeyy8XdWdLbXJWVt0xvib3TVyf4ib6AHEoqewrk6HNnR5xlajQ6stQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)](https://mp.weixin.qq.com/s?__biz=Mzg2OTY0MDk0NQ==&mid=2247507749&idx=1&sn=1403008340bbe16dff1b9fc2d5ae6eae&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgwMicjr8L9dRRJLEkSNsgIVRHpmAWHuicJicSjz64XSvfv7w99H3X1AlQjqUK8YiaZ0nMEXC7icy4ObIew/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1) ![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3tHNibnJ2jgwMicjr8L9dRRJLEkSNsgIVRw4bVibfWDjruedUwOAreh2icNydhJaY0MAaCbX1kVHdwrF6Whn8Jm4cg/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

  

作者：姚顺雨，OpenAI researcher

编译：海外独角兽

本篇内容是 OpenAI Agent Reseacher 姚顺雨对于 AI 下半场的解读，授权海外独角兽编译。

  

在 OpenAI o1 模型发布前，我们猜想 LLM 迎来 [RL 新范式](https://mp.weixin.qq.com/s?__biz=Mzg2OTY0MDk0NQ==&mid=2247509694&idx=1&sn=f0723aa72f1d9e4ffff5f828f8a49389&scene=21#wechat_redirect) ，AGI 路线也随之进入下半场。如果说 LLM 的 pre-training 是对已有知识进行压缩学习，RL 则更需要和环境交互产生新知识。相比 pre-training，RL 的算法和环境搭建更复杂，头部 Labs 对 RL 的探索也尚未收敛。我们该如何思考 RL 的意义，如何更好理解 AI 的下半场？ Shunyu 的这篇文章带来了很多启发。他认为在 AI 训练中，定义问题将比解决问题更重要，evaluation 将比 training 更重要，enviornment 和 priors 的重要性被低估了。

  

有评论称这篇文章是 *Bitter Lesson* 级别的存在，或许是因为和 *Bitter Lesson* 类似，这篇文章也试图从 high level 指出 AI 研究中一种思维范式的彻底改变。 *Bitter Lesson* 启发了大家从“人类指导 AI” 转向算力和数据的 scaling，而 *The Second Half* 告诉大家在 RL 全面到来时，我们应该彻底重新思考问题定义和真实用例的 evaluation。

  

姚顺雨本科毕业于清华姚班，是姚班联席会主席，2024 年从 Princeton 博士毕业后加入 OpenAI 担任 Research Scientist，参与了 OpenAI 的 Computer-Using Agent， [Deep Research](https://mp.weixin.qq.com/s?__biz=Mzg2OTY0MDk0NQ==&mid=2247511569&idx=1&sn=777c963078e486c4faea3e1cbfa66f36&scene=21#wechat_redirect) 等多个产品项目。他是 Agent 领域的最前沿探索者，这个领域不少最重要的 framework 和 benchmark 都来自他 Phd 期间的工作：ReAct、Tree of Thought、SWE\_Bench。

  

这篇 Blog 主要内容来自姚顺雨在 CS 224N 和 Columbia 大学所做的演讲，初稿由 OpenAI Deep Research 阅读演讲 Slides 后完成。

  

  

  

💡 目录 💡

01 我们正处于 AI 的半场时刻

02 什么是 AI 上半场

03 AI 的有效配方

04 欢迎来到 AI 下半场

  

  

  

  

  

**01.**  

  

**我们正处于  
AI 的半场时刻**

  

*We’re at AI’s halftime*

  

数十年来，AI 的核心一直在于开发新训练方法和模型。这种路径确实有效：打败国际象棋和围棋世界冠军、在 SAT 和律师资格考试上超过大部分人、赢得 IMO（国际数学奥林匹克）和 IOI （国际信息学奥林匹克）金牌，这些写进 AI 历史书里的里程碑——DeepBlue，AlphaGo，GPT-4 和 o 系列，都来自底层训练方法的创新，search，deep RL，scaling，reasoning。一切都在随着时间持续进步。

  

那么现在到底有什么变了？

  

简单来说，强化学习（reinforcement learning, RL）终于有效了。更确切地说，RL 终于有了泛化能力。经过几次弯路，也跨过了一系列重要里程碑后，我们终于找到了正确的配方（recipe），能通过语言模态和推理能力来解决广泛的强化学习任务。

  

即便在一年前，如果你告诉大多数 AI 研究者，有一种 recipe 能同时应对软件工程、创意写作、IMO 级别的数学问题、鼠标键盘操作以及长篇问答——他们只会嘲笑你在幻想。这些任务每一项都极其艰难，许多研究者整个博士期间只专注于其中一个细分领域。

  

但今天这件事的确发生了。

  

接下来会发生什么？

  

AI 的下半场——从现在开始——会从 **解决** 问题转向 **定义** 问题。在这个新阶段， Evaluation（模型评估） 会比 Training （模型训练） 更重要。我们不再只是问，“我们能不能训练模型来解决 X ？” 而是开始问：“我们究竟应该训练模型来做什么，如何衡量真正的进展？”要想赢得 AI 的下半场，我们必须及时转变心态和技能，也许要更像产品经理。

  

  

  

**02.**  

  

  

**什么是 AI 上半场**

  

*The First half*

  

要理解 AI 上半场的意义，可以看看这个阶段的 winners。

  

先来想一个问题，你认为迄今最具影响力的 AI 论文有哪些？我在 Stanford CS 224N 的课堂现场提出了这个问题，大家的答案并不意外：Transformer、AlexNet、GPT-3 等。这些论文的共同点在于它们提出了训练更强模型的一些基础性突破，但同时也在一些 benchmark 上展示了显著的性能提升，从而得以发表。

  

💡

CS 224N 是 Stanford 深度学习与 NLP 主题的公开课，是过去十年 AI 领域的很多学生和学者入门 NLP 最好的课程之一。由 Chris Manning 教授主讲。

Chris Manning 是 Stanford 语言学和计算机科学系首任 Thomas M. Siebel 机器学习教授、人工智能实验室（SAIL）主任和以人为本人工智能研究所（HAI）联合创始人，他还是 ACM、AAAI 和 ACL 的 Fellow，并曾于 2015 年担任 ACL 主席，是自然语言处理和机器学习领域的先锋人物。

**这些经典论文还有一个潜在共性：它们几乎都是训练方法或模型，而不是 benchmark 或者 tasks。** 即便是被认为是最有影响力的基准数据集 ImageNet，它的引用量也不到 AlexNet 的三分之一。这种差距在其他案例中更加明显。

  

比如，Transformer 使用的主要 benchmark 是 WMT’14，WMT’14 的 workshop report 引用量大约为 1300 次，而 Transformer 本身的论文引用早已突破 16 万次。

  

![图片](https://mp.weixin.qq.com/s/www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg%20stroke='none'%20stroke-width='1'%20fill='none'%20fill-rule='evenodd'%20fill-opacity='0'%3E%3Cg%20transform='translate(-249.000000,%20-126.000000)'%20fill='%23FFFFFF'%3E%3Crect%20x='249'%20y='126'%20width='1'%20height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

  

这些对比形象地说明了 AI 上半场是关注于构建新的模型和训练方法，evaluation 和 benchmark 则位于第二位，尽管对于学术发表体系而言，后者是十分必要的。

  

为什么会出现这种现象？

  

一个重要原因是，在 AI 上半场，训练方法比定义 tasks 更难也更令人兴奋。从零开始发明一种全新的算法或模型架构，比如反向传播算法、卷积神经网络（AlexNet），或是 GPT-3 所用的 Transformer，都需要非凡的洞察力和工程能力。

  

相比之下，为 AI 定义 tasks 往往显得更直接：我们只是把人类已经在做的事情，比如翻译、图像识别或下棋，转化为 benchmark，这个过程几乎不需要太多洞察，甚至不需要多少工程工作。

  

训练方法往往比具体任务更通用、适用范围更广，因此显得格外有价值。比如，Transformer 架构最终推动了 CV、NLP、RL 等多个领域的进展，影响范围远远超出最初验证它效果的 WMT'14 这个翻译数据集。一个出色的新训练方法往往能在多个 benchmark 上取得较好效果，因为它足够简单、通用，它的影响也因此会超越某个具体任务。

  

过去数十年来都是训练方法论的创新先行，催生了许多改变世界的理念和突破，并通过在各个领域不断提升的 benchmark 表现出来。

  

那么，为什么今天这件事会发生改变？因为这些理念和突破的积累，在解决任务方面带来了本质改变，造就了一套真正有效的 recipe。

  

  

  

**03.**  

  

**AI 的有效配方**

  

*The recipe*

  

这套 recipe 到底是什么？recipe 的关键成分并不让人意外：大规模的语言 pre-training，数据和算力的 scaling，reasoning 和 acting 的理念。这几个词乍一听很像今天出现频率极高的 buzzwords。

  

为什么将这几个词称为 recipe ？我们可以从 RL 的角度来看。

  

RL 通常被认为是 AI 的“终极形态”，毕竟从理论上，它能够保证在 game 中取胜，而在实践上，几乎所有 superhuman 水平的 AI 系统（比如 AlphaGo）都离不开 RL 的支撑。

  

💡

**game：** 在博弈论中，game 指的是所有在封闭环境中，有明确输赢的博弈任务。

  

RL 领域有三个关键组成部分：算法（algorithm）、环境（environment）和先验知识（priors）。

  

很长时间以来，RL 研究者主要关注算法，比如 REINFORCE、DQN、TD-learning、actor-critic、PPO、TRPO 等，也就是 agent 如何学习的这一核心机制。

  

💡

**DQN：** Deep Q-Network，即深度 Q 网络，是深度强化学习的一种重要算法，使用深度神经网络来逼近Q 值函数，并通过最大化 Q 值来选择最优动作，其中 Q 值计算的是 Agent 执行某个行动带来的价值变化。

**TD-learning：** Temporal difference learning，即时序差分学习，结合了动态规划（Dynamic Programming）和蒙特卡罗方法（Monte Carlo）的优点。

**Actor-critic：** 即演员-评论家算法，是一种结合策略梯度和时序差分学习的强化学习方法，包括演员（Actor，负责行动）和评价者（Critic，负责评价）用神经网络分工进行博弈。

**PPO：** Proximal Policy Optimization，即近端策略优化，是 OpenAI 在 2017 年提出的一种强化学习算法，被认为是目前强化学习领域的 SOTA 方法，也是适用性最广的算法之一。PPO 简化了以前的策略梯度算法，通过几个关键技术提高了训练的稳定性和效率。这是之前 RLHF 最常用的 RL 算法，在 reasoning model 场景下 Deepseek 提出的 GRPO 算法正在取代成为主流。

**TRPO：** Trust Region Policy Optimization，即置信域策略优化，是一种用于强化学习的策略优化算法。

  

相比之下，环境（environment）和先验知识（priors）往往被当作既定条件，或者被尽可能简化处理。例如，Sutton 和 Barto 的经典教材几乎讲的都是算法，对于环境和先验知识几乎只字未提。

  

![图片](https://mp.weixin.qq.com/s/www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg%20stroke='none'%20stroke-width='1'%20fill='none'%20fill-rule='evenodd'%20fill-opacity='0'%3E%3Cg%20transform='translate(-249.000000,%20-126.000000)'%20fill='%23FFFFFF'%3E%3Crect%20x='249'%20y='126'%20width='1'%20height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

  

但在深度强化学习时代，环境在实践中的重要性凸显：一个算法的效果往往高度依赖于它所开发和测试的环境。如果忽视环境，可能会导致我们构建的最优算法只在过于简化的环境中有效。

  

那么，为什么我们不先思考清楚真正想要解决的环境，再去寻找最适合它的算法？

  

OpenAI 最初就是这么计划的。

  

OpenAI 先是打造了 Gym，一个用于各类 game 的标准 RL 环境，接着又推出了 World of Bits 和 Universe，试图将互联网或计算机变成一个 game。这个设计很好，一旦我们可以将所有数字世界转化为 environment，再用 RL 算法来解决问题，我们就能实现数字领域 AGI。

  

💡

**Gym：** Gym 是 OpenAI 在 2016 年 4 月发布的一个用于开发和比较 RL 算法的工具包，提供了多种预定义环境，以便研究者和开发者可以在相同的 benchmarks 下测试他们的算法。

**World of Bits 和 Universe：** OpenAI 的 World of Bits 是基于 Universe 的训练平台，也是 Universe 项目的前身。Universe 发布于 2016 年 12 月，是一个能在几乎所有环境中衡量和训练 AI 通用智能水平的开源平台，目标是让 AI Agent 能像人一样使用计算机。

  

这个设计很好，但并不完全奏效。虽然 OpenAI 取得了巨大的进展，比如利用 RL 解决了 Dota、机器人手等问题，但还没有解决 computer use 或 web navigation ，并且，在一个领域表现出色的 RL agent 并不能迁移到另一个领域。某些关键因素仍然缺失。

  

直到 GPT-2 或 GPT-3 出现，我们才发现缺失的是先验知识 （priors）。你需要进行大规模 pre-training，将常识和语言知识提炼到模型中，然后通过微调使其成为网络 agent（WebGPT）或聊天 agent（ChatGPT），从而改变世界。

  

**结果发现，RL 中最重要的部分可能甚至不是 RL 算法或环境，而是先验知识，而这些先验知识的获取方式与 RL 完全无关。**

  

语言模型的 pre-training 为对话类任务提供了良好的先验知识，但在控制计算机或玩电子游戏方面却不够理想。因为这些领域和互联网的文本分布相差很大，直接在这些领域上做 SFT 或 RL 的泛化效果很差。

  

我是在 2019 年意识到的这个问题，当时 GPT-2 刚刚发布，我在它的基础上做了 SFT 或 RL 来解决基于文本的 game，最终做出了 CALM。CALM 是世界上第一个基于 pre-training 语言模型构建的 agent，但它要花费上百万步的 RL，才能在单一 game 中取得进展，而且无法迁移到其他 game 上。

  

虽然这正是 RL 的特点，对 RL 研究者来说并不意外， **但我仍觉得很反常，因为人类可以轻松上手一款新游戏，而且在零样本的前提下做得比 agent 更好。**

  

这时，我迎来了人生中第一个顿悟时刻：人类之所以能泛化，是因为人类不仅能做“去 2 号柜子”、“用 1 号钥匙打开 3 号箱子”或“用剑杀死地牢怪物”这类操作，还能思考：“地牢很危险，我需要一件武器。附近没有武器，我需要在锁着的柜子或箱子里找，3 号箱子在 2 号柜子里，那我应该先去那里把柜子打开。”

  

![图片](https://mp.weixin.qq.com/s/www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg%20stroke='none'%20stroke-width='1'%20fill='none'%20fill-rule='evenodd'%20fill-opacity='0'%3E%3Cg%20transform='translate(-249.000000,%20-126.000000)'%20fill='%23FFFFFF'%3E%3Crect%20x='249'%20y='126'%20width='1'%20height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

  

**思考（thinking）或推理（reasoning）是一种很特殊的行为，它并不会直接改变外部世界，但却拥有一个开放、无限组合的空间，** 我们可以想一个单词、一句话、一段话，或者一万个随机英语单词，但周围环境不会立刻发生变化。

  

在经典 RL 理论中，reasoning 是一个糟糕的存在，因为它会让决策变得不可能。比如，一个人需要从两个盒子中选一个，其中一个装着 100 万美元，另一个是空的，这个时候预期收益是 50 万美元。现在如果我们往这个人面前放了无数个空盒子，那么他的预期收益就变成了 0。

  

但如果我们在 RL 环境的动作空间（Action Space）中加上 reasoning，我们就能利用语言模型 pre-training 中获得的先验知识进行泛化，并可以在不同的决策中灵活分配 test-time compute。

  

💡

**动作空间：** 不同的环境允许不同种类的动作，在给定的环境中，有效动作的集合被称为动作空间（Action Space）。在离散动作空间（Discrete Action Space），agent 的动作数量是有限的，在连续动作空间（Continuous Action Space），动作是实值的向量。

  

这个过程很神奇，我会在未来专门写一篇 blog 来讲。可以通过 ReAct 这篇论文先了解我对 agent reasoning 的看法。

  

💡

**ReAct：** ReAct 是姚顺雨在 *ReAct: Synergizing Reasoning and Acting in Language Models* 中提出的框架，到今天还在 agent framework 中占有一席之地。

  

当下，我对于这件事的解释是：虽然一个人面前被放置了无数个空盒子，但他在此之前，他已经在各种 game 中见过这些盒子，之前的这些选盒子的经验能帮助他更好地识别出哪个盒子更可能装着钱。

  

用一句抽象的话来说：语言通过 agent reasoning 来实现泛化（language generalizes through reasoning in agents.）。

  

一旦我们拥有了正确的 RL 先验知识（语言 pre-training）和 environment（将语言推理作为行动），算法可能是最微不足道的部分。现在我们有了 o 系列、R1、deep research、computer-using agent，未来还会有更多的成果。多么讽刺的转折！

  

长期以来，RL 研究者更关心算法，远胜于关心 environment ，几乎没有人关注先验知识——所有的 RL 实验本质上都是从零开始的，但我们绕了几十年的弯路，才意识到也许我们的优先级应该反过来。

  

但正如 Steve Jobs 所说：You can’t connect the dots looking forward; you can only connect them looking backward.

  

  

  

**04.**  

  

**欢迎来到 AI 下半场**

  

*The second half*

  

这套 recipe 在彻底改变 AI 的游戏规则，AI 上半场的游戏规则是：

  

• 我们开发出新颖的训练方法或模型，在各种 benchmarks 上取得更好的成果。

  

• 我们创造出更难的 benchmarks，并继续这个循环。

  

现在这个游戏规则正在被彻底改变，原因在于：

  

• 这套 recipe 本质上已经把攻克 benchmark 的过程标准化、流程化了，我们不再需要太多新的想法。并且因为这套 recipe 具有较好的 scaling 和泛化能力， **你为某个具体任务设计的全新方法可能只能带来 5% 的提升，而下一代的 o 系列模型即使没有专门针对这个任务训练，也能带来 30% 的提升。**

  

• 即使我们设计出了更难的 benchmark，它们也往往会很快（而且越来越快）被这套 recipe 攻克。我的同事 Jason Wei 做了一张精彩的图，直观地展示了这个趋势。

  

![图片](https://mp.weixin.qq.com/s/www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg%20stroke='none'%20stroke-width='1'%20fill='none'%20fill-rule='evenodd'%20fill-opacity='0'%3E%3Cg%20transform='translate(-249.000000,%20-126.000000)'%20fill='%23FFFFFF'%3E%3Crect%20x='249'%20y='126'%20width='1'%20height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

  

那 AI 下半场应该做什么？如果新的训练方法不再必要，更难的 benchmark 也会被越来越快地攻克，我们应该怎么做？

  

我认为我们需要从根本上重新思考“评估”（evaluation），这不仅意味着设计更新、更难的 benchmarks，而是要彻底质疑现有的评估方法，创造新的评估方法，这样才能迫使我们发明超越现有有效的 recipe 的新方法。

  

但这很难，因为人类有惯性，人类很少去质疑最基础的假设——你只是理所当然地接受它们，却没意识到它们其实只是“假设（assumptions）”，而不是“定律（laws）”。

  

用一个例子来说明这种惯性，假如你基于人类考试，发明出了一种史上最成功的 AI 评估方法之一。在 2021 年这也许是一个突破性的想法，但到了 3 年后，这一方法已被很多人使用，属于非常常规的评估方法。那么你接下来会做什么？很可能是再设计一套更难的考试。

  

再比如，你已经成功解决了基础的编程任务，那么你接下来会做什么？很可能是寻找更难的编程任务，直到达到 IOI 金牌的水平。

  

惯性是一种很自然的现象，但问题也正出在这里。AI 已经在国际象棋和围棋上战胜了世界冠军，在 SAT 和律师资格考试中超过了大多数人类，达到了 IOI 和 IMO 金牌的能力，但至少从经济或 GDP 的角度看，世界并没有发生太大变化。

  

**我将这个称之为“效用问题（utility problem）”，我认为这是当下 AI 领域最重要的问题。**

  

也许我们很快就能解决“效用问题”，也许还不能。但无论结果如何，这个问题背后的根源可能非常简单：我们的评估方法在很多基本假设上与现实世界的设定不同。

  

举两个假设为例：

  

• **假设 1：评估应该是自动运行**

  

通常一个 agent 会收到一个任务输入，自动完成任务，最后得到一个任务奖励。但现实中，agent 往往需要在整个任务过程中持续与人类互动，比如你不会给客服发一条长信息，然后等十分钟，期待对方给出一条详细答复来解决所有问题。当我们质疑这种评估假设时，就催生出了新的 benchmarks，要么将真实人类引入交互环节（例如 Chatbot Arena），要么引入用户模拟（例如 tau-bench）。

  

![图片](https://mp.weixin.qq.com/s/www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg%20stroke='none'%20stroke-width='1'%20fill='none'%20fill-rule='evenodd'%20fill-opacity='0'%3E%3Cg%20transform='translate(-249.000000,%20-126.000000)'%20fill='%23FFFFFF'%3E%3Crect%20x='249'%20y='126'%20width='1'%20height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

  

• **假设 2：被评估的任务应该是独立同分布（i.i.d.）的**

  

如果你有一个包含 500 个任务的测试集，评估的时候，你会将每个任务独立运行，最后对结果取平均，得出整体评分。

  

但现实中，任务往往是顺序进行的，而不是并行的。一位 Google 的软件工程师在逐步熟悉 google3 仓库后，会越来越高效地解决问题，但一个软件工程 agent 在同一个仓库中解决多个问题，却无法获得这种熟悉度。我们显然需要 long-term memory 的方法（事实上已经有一些相关尝试），但学术界缺乏能合理体现这种需求的正确 benchmarks，甚至缺乏质疑 i.i.d. 这个被视为机器学习基础假设的勇气。

  

💡

**独立同分布：** Independent and identically distributed，即 i.i.d.，是机器学习中一个重要的假设，它表明训练数据和测试数据遵循相同的概率分布。这个假设确保了在训练集上训练的模型能够有效地在测试集上进行泛化，从而在未知数据上保持良好性能。

  

这些假设一直以来就是默认存在的。在 AI 上半场，基于这些假设来设计 benchmarks 是合理的，因为在智能水平较低时，提高智能通常就能提升效用。现在在这些假设下，那套通用 recipe 已几乎被保证奏效。那么 AI 下半场这个新游戏的玩法会是：

  

• 我们需要开发面向现实世界效用的全新评估设定或 task；

  

• 我们需要用 recipe 来攻克这些评估设定或 task，或用新组件来增强 recipe，然后重复这个循环。

  

这个游戏很难，因为它充满了未知，但也格外令人兴奋。AI 上半场的玩家专注于攻克电子游戏和标准化考试，AI 下半场的玩家则通过把智能转化为有用的产品，打造出数十亿甚至万亿美元的公司。

  

上半场充斥着各种不断迭代的训练方法和模型，而下半场在某种程度上对它们进行了筛选。通用 recipe 会轻松碾压你的渐进式改进，你创造出能打破这套 recipe 的新假设。那时，你就能做出真正改变游戏规则的研究。

  

欢迎来到 AI 下半场！

  

  

![图片](https://mp.weixin.qq.com/s/www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg%20stroke='none'%20stroke-width='1'%20fill='none'%20fill-rule='evenodd'%20fill-opacity='0'%3E%3Cg%20transform='translate(-249.000000,%20-126.000000)'%20fill='%23FFFFFF'%3E%3Crect%20x='249'%20y='126'%20width='1'%20height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

  

排版：杨乐乐  

延伸阅读

  

[![图片](https://mp.weixin.qq.com/s/www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg%20stroke='none'%20stroke-width='1'%20fill='none'%20fill-rule='evenodd'%20fill-opacity='0'%3E%3Cg%20transform='translate(-249.000000,%20-126.000000)'%20fill='%23FFFFFF'%3E%3Crect%20x='249'%20y='126'%20width='1'%20height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)](https://mp.weixin.qq.com/s?__biz=Mzg2OTY0MDk0NQ==&mid=2247512305&idx=1&sn=307f2ebde8ee40d2d13e621230d6fcfe&scene=21#wechat_redirect)

AI Agent 摩尔定律：每 7 个月能力翻倍，带来软件智能大爆炸

  

[![图片](https://mp.weixin.qq.com/s/www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg%20stroke='none'%20stroke-width='1'%20fill='none'%20fill-rule='evenodd'%20fill-opacity='0'%3E%3Cg%20transform='translate(-249.000000,%20-126.000000)'%20fill='%23FFFFFF'%3E%3Crect%20x='249'%20y='126'%20width='1'%20height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)](https://mp.weixin.qq.com/s?__biz=Mzg2OTY0MDk0NQ==&mid=2247512241&idx=1&sn=a2a3fe33f7b0038afd75f4d948d42c5f&scene=21#wechat_redirect)

为什么 AI Agent 需要自己的浏览器？

  

[![图片](https://mp.weixin.qq.com/s/www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg%20stroke='none'%20stroke-width='1'%20fill='none'%20fill-rule='evenodd'%20fill-opacity='0'%3E%3Cg%20transform='translate(-249.000000,%20-126.000000)'%20fill='%23FFFFFF'%3E%3Crect%20x='249'%20y='126'%20width='1'%20height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)](https://mp.weixin.qq.com/s?__biz=Mzg2OTY0MDk0NQ==&mid=2247512202&idx=1&sn=6cd431892eba5b3a19bcc5faa7172146&scene=21#wechat_redirect)

Exa：给 AI Agent 的 “Bing API”

  

[![图片](https://mp.weixin.qq.com/s/www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg%20stroke='none'%20stroke-width='1'%20fill='none'%20fill-rule='evenodd'%20fill-opacity='0'%3E%3Cg%20transform='translate(-249.000000,%20-126.000000)'%20fill='%23FFFFFF'%3E%3Crect%20x='249'%20y='126'%20width='1'%20height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)](https://mp.weixin.qq.com/s?__biz=Mzg2OTY0MDk0NQ==&mid=2247512142&idx=1&sn=12189fc24382c0df75fbccf2b2333cdc&scene=21#wechat_redirect)

Cartesia: 3 个月融资 9100 万美元，从 Transformer 到 Mamba 重塑语音 AI

  

[![图片](https://mp.weixin.qq.com/s/www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg%20stroke='none'%20stroke-width='1'%20fill='none'%20fill-rule='evenodd'%20fill-opacity='0'%3E%3Cg%20transform='translate(-249.000000,%20-126.000000)'%20fill='%23FFFFFF'%3E%3Crect%20x='249'%20y='126'%20width='1'%20height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)](https://mp.weixin.qq.com/s?__biz=Mzg2OTY0MDk0NQ==&mid=2247511894&idx=1&sn=a7d4a28a84ab923d23bd3e2c47c0760a&scene=21#wechat_redirect)

大模型非共识下，什么是 AGI 的主线与主峰？

  

  

[阅读原文](https://mp.weixin.qq.com/s/)

继续滑动看下一个

海外独角兽

向上滑动看下一个