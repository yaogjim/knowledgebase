---
title: "2025-12-31_jolestar_最近摸索出来了一套_AI_Coding_工作流_首先开一个_Agent_窗口_这个_Agent_的"
source: "https://x.com/jolestar/status/2002918725125820839"
author:
  - "[[@jolestar]]"
published: 2025-12-31
created: 2025-12-31
description:
tags:
  - "x"
  - "@jolestar"
  - "https"
  - "agent"
---

# 最近摸索出来了一套 AI Coding 工作流。 首先开一个 Agent 窗口，这个 Agent 的

**jolestar** @jolestar [2025-12-22](https://x.com/jolestar/status/2002918725125820839)

最近摸索出来了一套 AI Coding 工作流。

首先开一个 Agent 窗口，这个 Agent 的角色是产品经理或者架构师，负责和我聊需求与架构设计，拆分任务，最后转换成可执行的需求说明，直接写到 github issue。如果功能比较复杂，就拆分成多个子 issue。注意，这个 Agent 不做具体的任务，保证它的上下文不会很快被填满，让它持续拥有全局视角。

然后，启动一个 Coder Agent，丢一个 github issue 进去，要求完成代码并提交 PR。权限给够，让他不要中途申请权限或者再来咨询。

提交 PR 后让另外一个 Reviewer Agent review PR，或者 Github Copilot 也可以。有了 review 结果后，丢 PR 链接给 Coder Agent，让他继续修复。

最后没问题合并代码，继续下一个循环。是否能并行取决于 issue 之间是否有依赖关系。

这个流程还是一个手工维护的流程，中间有一些不太顺滑的地方，比如：

1\. Coder Agent 如果给了任意权限，又会担心它不小心命令弄错，把项目外的文件给删了。所以有时候还会被确认权限给卡住。

2\. Reviewer Agent 不太会用 Github inline 的 review comment，没办法精确标记行。直接输出在评论里和 Coder Agent 的配合会有问题。

3\. 让 Agent 拉取 PR 的 review comments 的时候，有时候接口返回太长了，MCP 会截断了，经常拿不全。

所以周末弄了一个工具，把 Coding Agent 装在容器里跑，然后和 Github action 配合把上面的流程自动化。工具差不多了，等发给版本后让大家体验。

* * *

**jolestar** @jolestar [2025-12-30](https://x.com/jolestar/status/2005862871071105283)

工具弄出来了，可以试试 https://x.com/jolestar/status/2005860894585282596… https://github.com/holon-run/holon

> 2025-12-30
> 
> 前一段时间我摸索出了一套 AI coding 的工作流（之前这条推里提过：https://x.com/jolestar/status/2002918725125820839… ），
> 
> 但在真正用的时候发现，并没有一个工具能非常完整地贴合这套流程，于是干脆自己顺手做了一个。
> 
> 我的核心诉求其实很简单：
> 
> 我已经把需求和方案写成了 issue，我希望一个工具能直接拿到这个
> 
> ![Image](https://pbs.twimg.com/media/G9Y_X6ebYAA1HRa?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G9Y_hfVboAAhe6v?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G9Y_n3NaYAAIxRe?format=jpg&name=large)

* * *

**virushuo** @virushuo [2025-12-22](https://x.com/virushuo/status/2002918945955922268)

我们日常也是这么用的

* * *

**jolestar** @jolestar [2025-12-22](https://x.com/jolestar/status/2002919749546815584)

你们全自动化了吗？

* * *

**virushuo** @virushuo [2025-12-22](https://x.com/virushuo/status/2002920796122169619)

没有全自动化，因为还需要人来review和对齐一下，不然一旦出了一个小偏差就会很快走向错误了

* * *

**China Says** @China\_says

UN stuck in outdated power structure

The U.N. Security Council remains constrained by the power structures that don't reflect today's global reality, according to Prof. Jia Lieying, head of China's first university-based U.N. research institute.

Countries and regional

联合国陷入过时的权力结构

中国首个高校联合国研究机构负责人贾烈英教授表示，联合国安理会仍然受到无法反映当今全球现实的权力结构的制约。

国家和地区

* * *

**brucexu.eth** @brucexu\_eth [2025-12-22](https://x.com/brucexu_eth/status/2002932101117780136)

我的类似产品快出来了，空闲时间开发了一阵子了，到时候发给你内测🤣

* * *

**jolestar** @jolestar [2025-12-22](https://x.com/jolestar/status/2002934914988298399)

那我们的工具重了😅？到时候可以看看思路是不是一致

* * *

**未知的健忘** @Activer\_cn [2025-12-23](https://x.com/Activer_cn/status/2003303361614086563)

有些疑问，

\> 1. Coder Agent 如果给了任意权限，又会担心它不小心命令弄错，把项目外的文件给删了。所以有时候还会被确认权限给卡住。

建议放WSL里面，把它当作一个专门code的环境即可；

2\. Reviewer Agent 直接总结提交问题，然后进行修改；这样比踢回给code

* * *

**jolestar** @jolestar [2025-12-30](https://x.com/jolestar/status/2005927971907911716)

1\. 我弄到 docker 容器里了

2\. 还是习惯 PR review 那种方式

* * *

**当然完美发力** @drwmfl\_my [2025-12-23](https://x.com/drwmfl_my/status/2003286356764790846)

gemini3的上下文关联是最长的吧，当作pm是不是最合适

* * *

**jolestar** @jolestar [2025-12-30](https://x.com/jolestar/status/2005928465527414813)

我现在是用 codex gpt5.2 ，后面用 gemini 比较下

* * *

**andy** @oldhomelh [2025-12-23](https://x.com/oldhomelh/status/2003273731481960923)

请问 agent 运行再本地还是远端？

* * *

**jolestar** @jolestar [2025-12-30](https://x.com/jolestar/status/2005928661665673249)

原来是本地的，现在改成远端了，CI 服务器上写代码

* * *

**Cola Deng** @EricDengCa [2025-12-22](https://x.com/EricDengCa/status/2003128131738320982)

搜下openspec，神一样的应用 装了基本不用写代码了

* * *

**0xCharlie** @web3nomercy [2025-12-23](https://x.com/web3nomercy/status/2003361484353712615)

get, 听起来和kilocode的orchestrator模式有点像, 我体验下

* * *

**云比云** @yunbiyun [2025-12-22](https://x.com/yunbiyun/status/2003095906514882857)

看完这些流程很有启发。我在想是不是可以先把整体架构和协作方式搭好，具体功能尽量按需再实现。在现在 AI 能力几乎随时可补齐的情况下，把需求当作“用到才拿出来”的模块，或许能让代码和系统都更精炼一些？

* * *

**girl loaders duo** @girlloaders [2025-12-23](https://x.com/girlloaders/status/2003473961875833030)

你这个思路很好 非常实用

* * *

**Helen,Huang** @sayhelen [2025-12-22](https://x.com/sayhelen/status/2003071383853740049)

期待看看全自动化成品效果

* * *

**不能停** @dwgeneral001 [2025-12-23](https://x.com/dwgeneral001/status/2003359702302982575)

看来我的工作流过时了，我是和 Claude 先一起把项目架构和需求文档梳理出来，然后让 Coding Agent 基于我的文档先出 Spec，然后我 commit 一些不合适的点，就直接干活，做好一个大feature我检查一个，没问题就继续下一个feature，感觉效率也提高了不少嘞，自己基本不写代码

* * *

**Dr. A** @ArkSmartChain [2025-12-22](https://x.com/ArkSmartChain/status/2003075636215333128)

不行，页面效果和细则无法把握，我直接通过调用多agent进行翻译工作就行了。

* * *

**PFinal** @NPfinal [2025-12-23](https://x.com/NPfinal/status/2003284632356422009)

下一步是不是AI自己聊需求，自己写代码，最后把我们都给优化了？

* * *

**dingx** @ieipi [2025-12-23](https://x.com/ieipi/status/2003311244124795279)

很有启发，尤其是第一点，保护第一个agent的上下文不被很快塞满。

我准备弄三个dev machine分别手动搞。

* * *

**Winter’s love** @winterslove2020 [2025-12-23](https://x.com/winterslove2020/status/2003504350828900606)

这个coding agent是自己做的？不太明白

* * *

**0x卡卡撸特 | Golden.S** @0xkakarot888 [2025-12-22](https://x.com/0xkakarot888/status/2003251992450466127)

学习了🫡

* * *

**waka** @S8Vb8 [2025-12-22](https://x.com/S8Vb8/status/2003139899910938979)

我现在就这么用的，发现AI Coding最重要的是方案和需求确认的情况下，产品需求文档和瀑布式的项目管理方法是最靠谱的，分几个agent安排好不同角色，如果走敏捷的路子，干着干着就得返工

* * *

**Jay | Web3 Insights** @JayNam2878 [2025-12-22](https://x.com/JayNam2878/status/2003210756771447101)

The AI Coding workflow sounds effective. Using an Agent for task breakdown and GitHub issues streamlines the process nicely.

这个 AI 编码工作流听起来很有效。使用一个 Agent 进行任务分解并创建 GitHub 问题能很好地简化流程。