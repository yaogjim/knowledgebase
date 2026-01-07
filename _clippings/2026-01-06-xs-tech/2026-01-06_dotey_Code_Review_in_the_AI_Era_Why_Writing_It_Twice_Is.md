---
title: "2026-01-06_dotey_Code_Review_in_the_AI_Era_Why_Writing_It_Twice_Is"
source: "https://x.com/dotey/status/2007515334350086153"
author:
  - "[[@dotey]]"
published: 2026-01-06
created: 2026-01-06
description:
tags:
  - "x"
  - "@dotey"
  - "https"
  - "ai"
---

# Code Review in the AI Era Why Writing It Twice Is

**宝玉** @dotey [2026-01-03](https://x.com/dotey/status/2007514902819467505)

Code Review in the AI Era: Why Writing It Twice Is Actually Faster

If you've been coding for a few years, you've probably lived through this nightmare: you finish the first version, finally get it running, and then realize you misunderstood half the requirements, hit three

AI 时代的代码审查：为什么写两遍反而更快

如果你做了几年开发，大概都经历过这种痛苦记忆：第一版代码写完，功能好不容易跑通了，然后发现需求理解错了一半，技术方案踩了三个坑，架构设计根本撑不住后续迭代

> 2026-01-02
> 
> I'm Boris and I created Claude Code. Lots of people have asked how I use Claude Code, so I wanted to show off my setup a bit.
> 
> My setup might be surprisingly vanilla! Claude Code works great out of the box, so I personally don't customize it much. There is no one correct way to
> 
> 我是 Boris，我创建了 Claude 代码。很多人问我怎么使用 Claude 代码，所以我想稍微展示一下我的配置。
> 
> 我的配置可能意外地很基础！Claude Code 开箱即用效果超棒，所以我个人没怎么自定义它。没有一种正确的方式
> 
> ![Image](https://pbs.twimg.com/media/G9wfSQbWEAAVJkN?format=jpg&name=large)

* * *

**宝玉** @dotey [2026-01-03](https://x.com/dotey/status/2007515334350086153)

AI 时代的代码审核：写两遍，反而更快

做过几年开发的人，大概都有过这种痛苦记忆：第一版代码写完，功能好不容易跑通了，然后发现需求理解错了一半，技术方案踩了三个坑，架构设计根本撑不住后续迭代。

想推翻重写？老板说deadline不等人。只好硬着头皮往上堆，三年后回头看，那坨代码已经成了没人敢动的屎山。

这个问题存在了几十年，但现在 AI 编程工具的出现，意外地给了一个新解法。

【1】我的解法：两个版本，两套标准

这个解法其实不新，软件工程教科书里叫“原型开发法”：先做个粗糙版本验证想法，再正式开发。但以前没人这么干，因为成本太高。写一个能跑的原型，可能要花正式开发一半的时间，谁等得起？

现在情况变了。AI 写代码的速度，快到让人不适应。以前一个功能要写三天，现在可能三小时就能出个能跑的版本。这个速度变化，让原型开发法从“理论上可行”变成了“实践中划算”。

具体怎么做？分两个版本开发。

【2】第一版：原型版，让AI撒欢跑

第一个版本的定位很明确：原型，不是产品。目标只有两个：确认需求，解决技术难点。

这个阶段的原则是“不管不顾”：不考虑架构设计，不考虑代码质量，不考虑安全性能。

只考虑一件事：把功能实现出来。代码生成出来直接合并，不做 review，让 AI 反复迭代，直到产品经理点头说“对，这就是我要的”。

这个版本的代码是准备扔掉的，所以要单独开个分支，或者干脆放在独立的仓库里。它的价值不在于代码本身，而在于两件事：确认需求到底是什么，以及把技术上的坑先踩一遍。

很多时候，需求文档写得再详细，你不做出来就是想不清楚。技术难点也是，纸上谈兵和真刀真枪完全两回事。第一版的意义就在于此：用最低的成本，把该踩的坑踩完。

就像建筑师画草图。草图不讲究线条精准、比例完美，它的作用是帮你把想法快速具象化，试错、调整、确认方向。没人会拿草图去施工。

【3】第二版：生产版，回归传统工程

等第一版把路探清楚了，再来做第二版。第二个版本才是真正要交付的东西。

这个阶段回归传统软件工程的套路：先做设计，再拆模块，走 CI 流程，做 Code Review。每次提交的代码量要小，方便人工审核。设计、维护、安全，该考虑的都要考虑。

在这个阶段，AI仍然是主力干活的，但人来主导。先设计后实现，配合plan模式，让AI按你的思路来生成代码。

第一版的代码也不是完全白写，有些模块是可以复用的，尤其是算法实现和业务逻辑这些核心部分。

相当于从草图里把有价值的部分提炼出来，放进正式的施工图。

【4】这套方法有效的底层逻辑

为什么要这么麻烦，搞两个版本？

核心原因是：在第一版做完之前，你对需求的理解大概率是不完整的。

传统开发模式的问题，恰恰在于它在第一版上花了太多精力。需求还没完全想清楚，就开始做架构设计；技术难点还没摸透，就开始考虑扩展性、可维护性。结果呢？大量过度设计，考虑了很多“未来可能会有但其实永远不会出现”的情况。时间花在了细枝末节上，真正重要的问题反而被忽略了。

两版本开发法的好处是，让你先用最低成本把路趟一遍。第一版跑完，需求确认了，技术难点解决了，再来做设计，这时候你知道该设计什么、不该设计什么。少走很多弯路。

还有一个隐藏好处。很多资深开发者不愿意用 AI 编程，核心原因是接受不了 AI 生成代码的质量。但如果你告诉他，这些代码就是用来扔的，只是为了验证想法，心理上的抵触就会小很多。这等于给了一个台阶：用 AI，但不用对那些代码负责。

说到底，AI 改变的不只是写代码的速度，更是整个开发流程的经济学。以前做两遍太贵，现在做两遍反而更划算。承认第一版是用来扔的，反而能做出更好的第二版。

![Image](https://pbs.twimg.com/media/G9wgg-0W4AAfAdu?format=jpg&name=large)

* * *

**宝玉** @dotey [2026-01-05](https://x.com/dotey/status/2007989488035967340)

问：如果是在第二版本开发，那如何让它践行双版本策略，新迭代的功能如果保持原来的编码架构？

答：如果是开发后续版本，第一遍原型版本不一定要基于原有的架构，起一个新项目vibe更快效率更高；但第二遍生产环境版本就需要考虑如何从第一版迁移了，需要充分考虑trade off：成本、收益和风险

* * *

**ハイスクールD×D Operation paradise infinity** @highschoolads

New game you didn't know about

Give it a try!

你不知道的新游戏

试试看！

* * *

**熊布朗** @Stephen4171127 [2026-01-05](https://x.com/Stephen4171127/status/2008100598973952200)

让我来质疑（思考）一下

1\. 这个是给DEV 团队的实践方式，第一版的结果看似更多是给产品经理确认，像我，以产品负责人角度出发做事，似乎不需要这一版确认需求，换句话说，需求确认不需要做出来什么再确认。本来就应该是产品经理们该负责好的事情。

2.

* * *

**耳朵** @RookieRicardoR [2026-01-04](https://x.com/RookieRicardoR/status/2007616120485032256)

我和宝玉老师的做法一致，我目前在生产环境就是这么干的。

* * *

**Lyte** @Lyte\_XAI [2026-01-04](https://x.com/Lyte_XAI/status/2007617445440487890)

这和我们现在内部在推的思路是类似的，不过第一版是交给产品经理来完成，用类似AI Studio 的软件，不要考虑技术栈，直接出可交互的原型效果，目的就是来确认需求、验证想法闭环，为后面需求澄清和开发更直观做准备的。正式的开发就按照已有技术栈来设计和推进

* * *

**宝玉** @dotey [2026-01-04](https://x.com/dotey/status/2007617727557709942)

产品经理来完成验证需求是没问题的，有一个问题就是产品经理不会考虑技术实现，所以有些技术上的坑开发可能还得自己踩一遍

* * *

**jarryfeng** @JarryR2D [2026-01-04](https://x.com/JarryR2D/status/2007613670218707307)

除了Saas，传统工业软件，这样的方法也奏效吗？

* * *

**宝玉** @dotey [2026-01-04](https://x.com/dotey/status/2007614160272830936)

奏效的，前提是AI开发速度确实快

* * *

**JimmyJacy** @ljhspurs [2026-01-05](https://x.com/ljhspurs/status/2008010488903500136)

这种实践想法其实挺好

不过缺点就是个人的钱包羞涩不够支付那么多token费用

如果是公司全包就好了🤓

* * *

**宝玉** @dotey [2026-01-05](https://x.com/dotey/status/2008010785281429853)

包月账号其实还好

* * *

**fangjun** @fjun99 [2026-01-04](https://x.com/fjun99/status/2007606717086085124)

谢谢好文章，用你的提示词也画了一个图

![Image](https://pbs.twimg.com/media/G9xzqSBa0AEaIbc?format=jpg&name=large)