---
title: "「Coze 2.0 Agent Skills 的体验：还差一个模型」"
source: "https://x.com/libukai/status/2013092665425002923"
author:
  - "[[@libukai]]"
date: "2026-01-20T12:10:30+08:00"
created: 2026-01-20
description:
tags:
  - "@libukai # Coze # AI产品 # Workflow # 中间层 # 语言模型 # 基座模型 # AI时代"
---
**李不凯正在研究** @libukai [2026-01-19](https://x.com/libukai/status/2013092665425002923)

论“抄”音速，在字节面前，其他的公司，不论大小，全是弟弟。  
  
这不，已经反复来回切换了 N 个定位的 扣子/Coze 又 All in Agent Skills 了。  
  
在刚刚正式发布的 Coze 2.0 版中，新增了一个技能商店，内置有 80 多个预设好的智能体（参见图一）。  
  
从这些技能当中，我随机选了个公众号 SVG生成器，以“帮我生成一个中国商业火箭发展史的动态时间轴”为需求进行了测试。  
  
怎么说呢？看起来这个 Agent Skill 还是整的挺复杂的，跑了接近 20 分钟才生成了一个看起来也挺复杂的 SVG ，然后，就翻车了········（参见图二）  
  
预设的不太行，那么我们看看 Coze 2.0 对以 .zip 格式上传的技能支持情况如何。  
  
这次我选用了官方的 docx skill，从安装的过程来看，Coze 采用了类似 Manus 的云端沙盒方案，为每一个技能配置了一台 1 核 2G 的虚拟机（见图三）。  
  
对于上传的 .zip 文件，Coze 自动转化为了 .skill 格式（又是字节封闭体系自己造轮子的传统技能了，见图三），并且提示说支持执行脚本进行相应的处理。  
  
不过，又翻车了······不管我怎么让它去帮我生成一个 Word 文档，这个 Skill 就是不去调用现成的脚本，而是要从头用 Javascript 写个库来处理 docx 格式文档（见图四），😂  
  
从初步的体验来看，个人觉得 Coze 2.0 对 Agent Skills 的支持连个半成品都算不上吧，最多只能算是个 Demo。  
  
作为一个从 Coze 叛逃到 n8n 的 workflows 开发者，我其实对 Coze 的产品能力还是挺认可的。但默认强推自己扶不上墙的豆包模型，让这个产品几乎不具备生产环境的可用性。  
  
以个人经验来判断，Coze 2.0 对 Agent Skills 的支持出现这样史诗级的大翻车，作为基座的豆包大模型应该也要负主要责任。  
  
实在不行，你把最新的 Qwen 用起来当基座模型啊。打不过就认输，真的不丢人，打不过还硬撑，才真的丢人。

![Image](https://pbs.twimg.com/media/G-_mxotXgAA00n3?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G-_r8L_WMAAeVav?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G-_xDdtbcAA-7Ol?format=jpg&name=large)

---

**糖串sensei.** @tangchuan\_CN [2026-01-19](https://x.com/tangchuan_CN/status/2013303164146196546)

终于看到一个非广子的评测贴

---

**李不凯正在研究** @libukai [2026-01-19](https://x.com/libukai/status/2013397694392475943)

这次 KOL 的面铺的还挺广的

---

**蛋黄堡.ai** @Hamburgerai [2026-01-20](https://x.com/Hamburgerai/status/2013438124320342430)

这种中间层字节都抄得挺快的，看现在国内谈及workflow，基本都有coze身影了

那么既然缺点只在基座模型的话，后面模型能力跟上来了，用户体验一下子就能上来

现在谁还记得coze国内刚上的时候那个拉跨模型？

要抢快的话，“有就行”“主流几个能跑就行”

---

**李不凯正在研究** @libukai [2026-01-20](https://x.com/libukai/status/2013457546036523289)

从市场策略上来讲，我还是挺赞同的，现在这个阶段的 AI 产品，在“有就行，凑合能用”的前提下，快比完美更重要。当然心理承受能力也要更强一些才行，有啥问题别逃避赶紧优化就是。

---

**BTCOW** @EEjMdVqi4MDUeAH [2026-01-19](https://x.com/EEjMdVqi4MDUeAH/status/2013242108690178156)

这有什么好嘲讽？身处Ai时代，我们每个人都是一样的，跟这个大公司做同样的事。我们都是在搭框架,等这个基座模型能力上来之后，获得整体的一个质的飞跃下一个模型提升了它整个生态就活起来了。

---

**李不凯正在研究** @libukai [2026-01-19](https://x.com/libukai/status/2013397555393241168)

出来混，有错就要认，挨打要立正，这不是基座模型能力还没上来吗？等上来了再说硬话吧

---

**阿川聊AI** @zzy17813100102 [2026-01-19](https://x.com/zzy17813100102/status/2013102517882900503)

我今天已经在公众号的文章里看到商单了。表面上是一些博主在介绍自己的写作技巧、提示词和工作流，实际上是通过将这些内容与 Coze 绑定来推销 Coze 的产品，从而完成商单的宣传。

真是绷不住了呀！一看就是商单，我都不想继续看了。如果好的话，也不至于需要这样宣传了，反正他们家的产品我基本不用

---

**李不凯正在研究** @libukai [2026-01-19](https://x.com/libukai/status/2013102872930726249)

刚刚也刷到了几条，的确有点难绷，Coze 这玩意先天体质不良，靠吃大补丸估计也难

---

**victor-wu.eth** @victor\_wu\_eth [2026-01-19](https://x.com/victor_wu_eth/status/2013139312263778316)

我之前就是嫌弃他模型更新太慢选择用dify的

---

**李不凯正在研究** @libukai [2026-01-19](https://x.com/libukai/status/2013162870071009367)

Dify 也太重了，每次升级都是地狱般的体验

---

**Bito** @BitoHQ

Get one-shot production-ready code in Cursor and Claude with Bito’s AI Architect:

1\. System intelligence

2\. Services, APIs, dependencies

3\. Grounded code generation

4\. Production-ready output  
借助 Bito 的 AI 架构师，在 Cursor 和 Claude 中获取一键生成的生产就绪代码：

系统智能

2\. 服务、API、依赖项

3\. 有依据的代码生成

4\. 可用于生产的输出