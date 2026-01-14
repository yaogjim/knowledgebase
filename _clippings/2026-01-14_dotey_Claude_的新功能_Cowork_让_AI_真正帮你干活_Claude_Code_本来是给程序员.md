---
title: "2026-01-14_dotey_Claude_的新功能_Cowork_让_AI_真正帮你干活_Claude_Code_本来是给程序员"
source: "https://x.com/dotey/status/2010817497340187076"
author:
  - "[[@dotey]]"
published: 2026-01-14
created: 2026-01-14
description:
tags:
  - "x"
  - "@dotey"
  - "https"
  - "2026-01-13"
---

# Claude 的新功能 Cowork：让 AI 真正帮你干活 Claude Code 本来是给程序员

**宝玉** @dotey 2026-01-12

Claude 的新功能 Cowork：让 AI 真正帮你干活

Claude Code 本来是给程序员写代码用的，结果大家发现它整理文件、做表格、写报告也很顺手。Anthropic 索性把这套能力包装成了 Cowork，让不会写代码的人也能用上。

【1】Cowork 到底能干啥

你选一个电脑上的文件夹，Claude 就能在里面读文件、改文件、创建新文件。

听起来简单，用起来挺香。比如你下载文件夹乱成一锅粥，让它帮你分类重命名。或者你有一堆消费截图，它能整理成一张 Excel 表。再比如你写了几页凌乱的笔记，它能帮你理顺思路、输出初稿。

和普通对话不一样的是，Cowork 模式下 Claude 更像个真正的助手。你布置任务，它自己规划步骤、一步步执行，中间会告诉你进度。如果你用过 Claude Code，这感觉会很熟悉，因为底层技术是同一套。

【2】还能更强

基础功能只是起点。Cowork 可以接上你已有的连接器，比如 Google Drive、Slack。它还内置了一批技能，能更好地生成文档、PPT 之类的文件。再配上 Chrome 浏览器插件，Claude 甚至能帮你操作网页。

这套设计让工作流变得很丝滑。你不用反复给 Claude 喂上下文，也不用手动把输出转成正确格式。甚至不用等它做完一件事再布置下一件，可以连续丢任务让它并行处理。用 Anthropic 的话说，这感觉不像你一句我一句地聊天，更像给同事留便签。

【3】和 Claude Code 共享技能生态

对 Claude Code 用户来说有个好消息：Cowork 能读取你本地的 http://CLAUDE.md 文件和自定义 Skills。

我测试了一下，选择工作文件夹后，Cowork 能看到里面的 http://CLAUDE.md 并按指令执行。我在 Claude Code 里配置的写作风格技能，Cowork 里也能直接调用。技能分两类：Anthropic 官方提供的（docx、pptx、pdf 这些）和用户自己创建的，两类都能用。

换句话说，你在 Claude Code 里攒下的工作流配置可以直接迁移过来。Cowork 不是另起炉灶，是同一套体系的图形化入口。

有个坑要注意：Cowork 跑在 Linux 虚拟机里，而你的 Mac 是 ARM 架构。如果技能依赖 node\_modules 或本地特定环境（比如浏览器 cookies、特定架构的二进制文件），就跑不了。我试着调用一个需要运行 nodejs 脚本的图片生成技能，报错了——架构不兼容。纯文本类的配置（http://CLAUDE.md、写作规范）没问题，涉及本地脚本的技能可能需要额外适配。

【4】安全边界在哪里

Claude 只能访问你明确授权的文件夹和连接器，动作比较大的时候会先问你。但有几件事得提前知道：Claude 可能会误解你的指令，如果你说"清理一下这个文件夹"，它可能真的把文件删了。指令要说清楚。

另一个风险是提示词注入，就是攻击者在网页内容里藏一些指令，试图劫持 Claude 的行为。Anthropic 说他们做了防护，但这个领域整个行业都还在摸索。

这些风险不是 Cowork 特有的，只是很多人可能是第一次用这种更自主的 AI 工具。官方建议：刚开始用的时候谨慎点，别一上来就让它处理重要文件。

【5】现在能用吗

Cowork 目前是研究预览版，只对 Mac 上的 Claude Max 订阅用户开放。Anthropic 想先看看大家怎么用、有什么反馈，然后快速迭代。后面会加跨设备同步，也会出 Windows 版。

这一步到是意料之中，因为 Claude Code 现在已经被用在很多编程意外的领域，但是门槛略高，限制了使用群体是程序员或者懂点技术的用户，而且脚本执行权限会有很多安全上的隐患。Cowork 一下子降低了使用的门槛，通过图形化界面就可以操作，并且也让使用更安全。

现在还是早期版本，能做的事有限，安全机制也在完善中。但如果你是 Max + Mac 用户，值得一试。

> 2026-01-12
> 
> Introducing Cowork: Claude Code for the rest of your work.
> 
> Cowork lets you complete non-technical tasks much like how developers use Claude Code.
> 
> 介绍 Cowork：Claude 代码，为你剩下的工作。
> 
> Cowork 让你完成非技术性任务，就像开发者使用 Claude Code 一样。

* * *

**范凯说 AI | AI Insights** @robbinfan [2026-01-13](https://x.com/robbinfan/status/2010891065402986975)

Claude CoWork本质上就算是AI PC了。

* * *

**yan5xu** @yan5xu [2026-01-12](https://x.com/yan5xu/status/2010853141731033522)

杀到通用 agent 了

* * *

**叶隐** @sunpolis [2026-01-13](https://x.com/sunpolis/status/2011098172144099690)

用不了claude，请问cowork和google的notebooklm有什么不一样？

* * *

**宝玉** @dotey [2026-01-13](https://x.com/dotey/status/2011101970418057666)

这个更像帮你操作电脑干一些体力活

* * *

**iTrustCapital** @iTrustCapital

No External Wallets or Unnecessary Risks, Just a Trusted Way to Buy & Custody Crypto.

无需外部钱包，也无不必要风险，只需一种可靠的加密货币购买与保管方式。

* * *

**moying** @MoYingLZ [2026-01-13](https://x.com/MoYingLZ/status/2010917767252185461)

可以把本地许多图片做分类吗

* * *

**宝玉** @dotey [2026-01-13](https://x.com/dotey/status/2010918041664585982)

应该可以

* * *

**Trends | Capitalized Information Market** @trendsdotfun [2026-01-13](https://x.com/trendsdotfun/status/2011052498283528401)

确实惊喜，AI帮手+1

* * *

**NoOne** @hunterzhang86 [2026-01-12](https://x.com/hunterzhang86/status/2010847101056663589)

写一下把很多 AI SaaS 都干没了😭

* * *

**xiaoyu** @zhongxingyuyes [2026-01-13](https://x.com/zhongxingyuyes/status/2010956041219916031)

Cowork的本质是降低门槛而非降低能力。让非技术用户也能调用Computer Use的能力,这是产品化的关键一步。不过文件操作的安全问题确实需要持续打磨。

* * *

**Mens@codesome.cn** @oops073111 [2026-01-13](https://x.com/oops073111/status/2010941157455643120)

越好用，越不能用。现在官方对 CN 的订阅，限制更大了

* * *

**JimmyJacy** @ljhspurs [2026-01-13](https://x.com/ljhspurs/status/2010877637632409888)

其实我有个想法:

Claude是想通过这个功能慢慢实现开始实现PC端的AGI

到最后我在Cowork上下达命令: "帮我去赚钱"，它就自动帮我去干了，哈

以后就看AI操作赚钱快还是token扣钱扣得快🤓

* * *

**Raad** @Raadmobrem

Founder of Reddit ($25B)

Founder of Loom ($1B)

Execs at Uber ($200B), Tinder ($8B), and more.

You can get personalized advice from them on Intro.

No pitch decks. No cold emails.

Just real advice. 1:1. Live. →

Reddit 创始人（250 亿美元）

Loom 的创始人（10 亿美元）

优步（2000 亿美元）、Tinder（80 亿美元）等公司的高管

你可以从他们那里获得关于 Intro 的个性化建议。

没有路演 PPT。没有冷邮件。

只是真诚的建议。1:1。直播。→

* * *

**Jeremy Feng** @JeremyFeng98 [2026-01-13](https://x.com/JeremyFeng98/status/2010893143978492090)

本地版 Manus？

* * *

**binghanliu** @gogogonow178 [2026-01-13](https://x.com/gogogonow178/status/2010876704651427932)

这个功能很实用了

* * *

**IVAR** @VikingkingIvar [2026-01-13](https://x.com/VikingkingIvar/status/2010921882317701488)

能预感到，现在anthropic想降低操作难度，让这款出圈

* * *

**蛋黄堡.ai** @Hamburgerai [2026-01-13](https://x.com/Hamburgerai/status/2010899653794107557)

Claude准备要彻底出圈了，有了GUI之后普通人用会更加方便

* * *

**踏雪寻仙** @TaXue2025 [2026-01-13](https://x.com/TaXue2025/status/2010934405431496860)

Claude Cowork 的开源版应该也快了

* * *

**minsea** @MinSea01 [2026-01-13](https://x.com/MinSea01/status/2010926295627227321)

真正能干活的ai

* * *

**小鲸鱼** @tinywhale2023 [2026-01-13](https://x.com/tinywhale2023/status/2010905131408294302)

claude开始拿更多私有数据了

* * *

**xiaobeiLin(小北)** @linxiaobei888 [2026-01-13](https://x.com/linxiaobei888/status/2010874602713743492)

Cowork 只花了一周半的时间开发出来的，而且所有代码都是CC写的……

* * *

**行者达达** @dali51334388 [2026-01-13](https://x.com/dali51334388/status/2010869025325400222)

取代了界面上的 code？

* * *

**suting ver** @ver\_suting [2026-01-13](https://x.com/ver_suting/status/2010879163113324649)

这和已有的project 是不是一样的？只不过又来个新名词

* * *

**The Fabulous** @GetTheFabulous

You don’t outgrow being gifted.

You outgrow the systems that once worked for you.

你不会长大而失去天赋。

你会超越那些曾经对你有效的系统。

* * *

**OmniHelix** @OmniHelix [2026-01-12](https://x.com/OmniHelix/status/2010850942451925144)

与官方神同步，速度好快，学习一下。

* * *

**BF-Beauty Finder** @Beauty\_finder\_ [2026-01-12](https://x.com/Beauty_finder_/status/2010843758577721683)

太好了，简单写文章的宝玉老师又回来了

* * *

**Spark** @sparkxxf [2026-01-13](https://x.com/sparkxxf/status/2011032273605517386)

非max用户可以试试 chatLily

* * *

**Ananya Patelik** @ananyapatelik [2026-01-13](https://x.com/ananyapatelik/status/2010895070669480269)

love how “code” tools sneak into workflow art. i’ve used claudecode to untangle csv chaos more than to write scripts. accidental productivity ftw

喜欢“代码”工具悄悄融入工作流程的艺术中。我用 ClaudeCode 理清 CSV 文件的混乱情况，次数比写脚本还多。意外的生产力简直太棒了！