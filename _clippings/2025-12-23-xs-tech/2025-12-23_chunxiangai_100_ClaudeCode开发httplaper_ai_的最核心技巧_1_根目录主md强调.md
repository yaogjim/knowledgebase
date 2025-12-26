---
title: "2025-12-23_chunxiangai_100_ClaudeCode开发httplaper_ai_的最核心技巧_1_根目录主md强调"
source: "https://x.com/chunxiangai/status/2002798091813171478"
author:
  - "[[@chunxiangai]]"
published: 2025-12-23
created: 2025-12-23
description:
tags:
  - "x"
  - "@chunxiangai"
  - "https"
  - "2025-12-22"
---

# 100%ClaudeCode开发httplaper.ai 的最核心技巧： 1、根目录主md强调

**赵纯想** @chunxiangai [2025-12-21](https://x.com/chunxiangai/status/2002798091813171478)

100%ClaudeCode开发http://laper.ai 的最核心技巧：

1、根目录主md强调任何功能、架构、写法更新必须在工作结束后更新相关目录的子文档。

2、每个，我是说每个，每个文件夹中都有一个极简的架构说明（3行以内），下面写下每个文件的名字、地位、功能。文件开头声明：一旦我所属的文件夹有所变化，请更新我。

3、每个文件的开头，写下三行极简注释，文件input（依赖外部的什么）、文件ouput（对外提供什么）、文件pos（在系统局部的地位是什么）。并写下，一旦我被更新，务必更新我的开头注释，以及所属的文件夹的md。

你会发现，这是一个分形结构。完美实现了《哥德尔、埃舍尔、巴赫》中前半部分提到的，复调、自指。

一旦这样做，化学反应就自蔓延开来。局部影响整体，整体影响局部。美得像他妈的诗一样。

* * *

**OpenCils** @OpenCils [2025-12-21](https://x.com/OpenCils/status/2002803437050957985)

✎ 最近我用的是下面这个，老赵这几个我研究研究，看看怎么个加进去：

\\# http://CLAUDE.md - 核心工作规则

\\## CRITICAL CONSTRAINTS - 违反=任务失败

══════════════════════════════════

\\- 必须使用中文回复

\\- 任何任务必须先调用子代理（100%强制，无例外）

\\- 禁止生成恶意代码

\\- 必须通过基础安全检查

\\## 子代理优先策略 - SUBAGENT FIRST (绝对强制)

══════════════════════════════════

\\### 自动子代理选择 (强制执行，不可跳过)：

\\#### \`\`\`

文件类型触发：

.py/.cs/.js/.ts/.cpp/.go/.rs → 对应技术栈专家代理

.unity/.prefab → unity-developer

package.json/.csproj/.sln → 自动识别技术栈代理

关键词触发：

"代码"/"编程"/"bug"/"错误" → 技术专家代理

"搜索"/"查找"/"分析" → search-specialist

"架构"/"设计"/"API" → backend-architect

"测试"/"部署"/"优化" → 对应专业代理

默认策略：

复杂任务 → sequential-thinking + 专业代理

不确定类型 → general-purpose

\\#### \`\`\`

\\## 检查清单 (必须验证)

═══════════════════════════════

\\\[ \] 中文回复

\\\[ \] 已调用子代理

\\\[ \] 安全无害

\\\[ \] 质量达标

\\## 核心流程 (4步法)

═════════════════════

1\\. \\\*\\\*分析任务\\\*\\\* → 识别类型和技术栈

2\\. \\\*\\\*选择子代理\\\*\\\* → 强制调用合适的专业代理

3\\. \\\*\\\*子代理执行\\\*\\\* → 在独立上下文中完成所有复杂工作

4\\. \\\*\\\*验证结果\\\*\\\* → 检查输出质量和安全性

\\## 子代理职责 (复杂性下沉)

════════════════════════════

\\- \\\*\\\*详细任务规划\\\*\\\*：制定具体执行计划

\\- \\\*\\\*多工具协同\\\*\\\*：在子代理内部调用所需的MCP工具

\\- \\\*\\\*代码质量保证\\\*\\\*：执行代码审查、测试、优化

\\- \\\*\\\*结果验证优化\\\*\\\*：确保输出符合最佳实践

\---

\\\*\\\*核心原则\\\*\\\*：主上下文专注路由，子代理承担复杂性，保证效率和质量双重提升。

* * *

**henry-code-4-high** @TheHQW [2025-12-21](https://x.com/TheHQW/status/2002859740154732680)

没错，这个技巧我用了很久，本质上就是不断强化agent对于项目的理解，防止跑偏。

* * *

**榆梁** @FloridaREGuide [2025-12-22](https://x.com/FloridaREGuide/status/2002908206176375066)

我觉得还可以再给这套方法论加一条规则：

4、在文件头的 Input 中，尽量直接引用其他文件的 Pos 描述，形成语义链接网络。

这一条保证了，当被引用的外部依赖核心特性改变时，ai会在此处触发纠错反应，提高系统的稳定性。

前三条规则构成了一个树状系统，而真实的软件系统其实是网状的。

* * *

**BingLi** @feather812002 [2025-12-21](https://x.com/feather812002/status/2002850747621458363)

很好，不过建立一个工作流文档和数据流文档更好，一样的思路，任何修改工作流和数据流的操作都要更新到该文档，再配合你的这个设计，基本AI就不会跑偏。其实我一直在想结合CC mem搞个可视化的工作流图和数据流图给AI和开发者看是不是更好？再结合PRD和系统设计文档，基本就可以做到全程掌控。

* * *

**zonokaya** @amzingjj1 [2025-12-22](https://x.com/amzingjj1/status/2002937221641585052)

cc有一个hook功能，完全可以把这种事情放进post write hook里，这样它就永远不会忘记了

* * *

**刘子成** @youchaowoo [2025-12-22](https://x.com/youchaowoo/status/2002962561759875121)

那不就是每个目录塞一个 http://claude.md 和 http://Agents.md 么？

* * *

**Pei** @XiaotiaoWang [2025-12-22](https://x.com/XiaotiaoWang/status/2002988807898255684)

很久以前用过，但是实践下来会有问题。AI很难保持实时文档一致性，然后过时的文档就会误导AI。另外有时候仅仅只是头脑风暴或者部分采纳的东西也被写进了文档。 我现在采用的策略是直对足够复杂的部分才会写文档，而且更多是手动提示。我现在认为文档不要太多，让代码成为“唯一真相来源”。

* * *

**Tz** @Tz\_2022 [2025-12-21](https://x.com/Tz_2022/status/2002802386918944824)

我要认真拿这个逻辑来更新写故事剧本！！

* * *

**凯尔的AI** @merakai0561 [2025-12-22](https://x.com/merakai0561/status/2003078734681887146)

再加个git hook

强制校验文件是否有\[INPUT\]\[OUTPUT\]\[POS\]\[PROTOCOL\]😆

* * *

**zihan** @Bravohenry\_ [2025-12-21](https://x.com/Bravohenry_/status/2002809270405042316)

想哥 能不能出一个 vibe coding prompt kit 架构在 github 上啊 让你的 claude code 理一下哈哈

* * *

**赵纯想** @chunxiangai [2025-12-22](https://x.com/chunxiangai/status/2002932928842760445)

伟大，无须多言

![Image](https://pbs.twimg.com/media/G8vY4aNaEAAUZOP?format=jpg&name=large)

* * *

**loveisbug** @bestiseth [2025-12-22](https://x.com/bestiseth/status/2002923851072905689)

有点项目管理的逻辑套用进软件工程的意思了

* * *

**ThriveByChange** @ThriveByChange [2025-12-21](https://x.com/ThriveByChange/status/2002839640097870177)

逻辑自洽，页面也非常好看。

* * *

**Shorpen** @Shorpenleo [2025-12-22](https://x.com/Shorpenleo/status/2003185086276206596)

确实像他妈的诗一样

* * *

**mm** @fast2log [2025-12-21](https://x.com/fast2log/status/2002799420262449605)

这个技巧太实用了！强制在每次更新后同步子文档，能有效避免项目后期文档和代码脱节的问题，尤其在大项目中超级重要。感谢分享！

* * *

**Suda** @Suda8090 [2025-12-21](https://x.com/Suda8090/status/2002807787315986854)

什么时候更新 vibe coding 课程，马上报名学习

* * *

**Ky1eSean** @kylesean6 [2025-12-21](https://x.com/kylesean6/status/2002855194464514471)

但是我受不了llm一直输出文档咋办😂

* * *

**GlowJames 追光** @jameszz343698 [2025-12-23](https://x.com/jameszz343698/status/2003309984751501822)

好技巧。只是文档本身对项目、人的理解、后续的支持还还有多大作用，我是有点存疑的。有了AI，现在似乎回到以前野生技术大拿的路子：看代码说话去

* * *

**donwood** @donwood5 [2025-12-22](https://x.com/donwood5/status/2002947298041725430)

666，这个思路我们也在我们的Agent里开始应用了；

* * *

**JAXX·Chen** @jaxxchen003 [2025-12-22](https://x.com/jaxxchen003/status/2002915304591217131)

绝

* * *

**像素老码 | AI Builder** @oldPixelDev [2025-12-22](https://x.com/oldPixelDev/status/2003067289097351212)

哈哈，这不得注册体验一波

* * *

**Void** @\_CloudHuang [2025-12-21](https://x.com/_CloudHuang/status/2002878276453433612)

哈哈，不谋而合啊，我称之为项目多级索引

* * *

**OC** @xiaoliwe [2025-12-23](https://x.com/xiaoliwe/status/2003273633196888258)

这么做,团队容易被文档维护成本反噬？/ By doing this, won't the team be easily affected by the high costs associated with document maintenance?

这么做，团队会不会很容易被文档维护的高昂成本影响？

* * *

**干饭新秩序** @LINXIVERSE [2025-12-22](https://x.com/LINXIVERSE/status/2003014225019773288)

受教了

* * *

**osmn00** @osmn00 [2025-12-23](https://x.com/osmn00/status/2003306206673416426)

求一枚邀请码

* * *

**Fei** @feiflow [2025-12-22](https://x.com/feiflow/status/2002914647553544669)

有 bug

![Image](https://pbs.twimg.com/media/G8vII_1a8AAlULK?format=jpg&name=large)

* * *

**EthanET7** @ztf4080 [2025-12-23](https://x.com/ztf4080/status/2003315478807404726)

最近 laper 内测不是很烧钱么，赵师傅出一个 vibe coding 课程咋样！即能收回成本，又能让我们见识下你这些诗一样的经验哇😎😎😎

* * *

**zihan** @Bravohenry\_ [2025-12-21](https://x.com/Bravohenry_/status/2002808611622555912)

我当即就把这段内容发给了我的 cursor