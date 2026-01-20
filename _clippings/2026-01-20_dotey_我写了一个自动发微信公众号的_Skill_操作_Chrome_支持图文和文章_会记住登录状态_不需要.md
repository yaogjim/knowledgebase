---
title: "2026-01-20_dotey_我写了一个自动发微信公众号的_Skill_操作_Chrome_支持图文和文章_会记住登录状态_不需要"
source: "https://x.com/dotey/status/2011486901610467836"
author:
  - "[[@dotey]]"
published: 2026-01-20
created: 2026-01-20
description:
tags:
  - "x"
  - "@dotey"
  - "https"
  - "宝玉"
---

# 我写了一个自动发微信公众号的 Skill，操作 Chrome，支持图文和文章，会记住登录状态，不需要

**宝玉** @dotey 2026-01-09

我写了一个自动发微信公众号的 Skill，操作 Chrome，支持图文和文章，会记住登录状态，不需要每次登录。

文章的话，提供markdown文档本地地址，会自动帮你把 Markdown 转 HTML（可选风格较少），配图会一张张粘贴进编辑器，不需要手动上传，封面图、原创设置暂时不支持，建议把封面图放文章内容。

技术上我没有使用 PlayWright MCP，因为这玩意儿太费 Tokens 了，而是用的 Chrome CDP (Chrome DevTools Protocol) 是一个允许外部程序通过 WebSocket 与 Chrome（以及 Edge、Opera 等基于 Chromium 浏览器的内核）进行通信的底层调试协议。

都是脚本操作，不怎么费 Token。

图文的话需要告诉图片地址、标题和内容，可以自动上传图片，填写标题和内容。

所有操作都不会发布，只是帮你生成草稿。

需要 Claude Code 或者其他支持 Skills 的 Agent，需要 Nodejs 运行环境（但如果你装了 Claude Code 应该就支持 Node）

Skill 地址：https://github.com/JimLiu/baoyu-skills/blob/main/skills/post-to-wechat/SKILL.md…

安装说明：

https://github.com/JimLiu/baoyu-skills…

这是我分享的 Skill 之一，还有一些其他 Skills，注意其中 gemini-web 的 skill 可以帮你用你的 Gemini 账号画图，需要自己登录一下。不保证它的稳定性和安全性，不过我自己也在用。

> 2026-01-09
> 
> 推荐王老师的教程，另外刚才测试了一下王老师写的自动发布 X 文章的 Skill，真的是强大，而且给我很大启发，理论上来说基于这个思路可以做一个发布微信公众号或者其他平台的 Skill。
> 
> 原理是用脚本控制浏览器，用剪贴板把文字和图片粘贴到编辑器，最有创意的是，根据文字定位到图片要插入的位置👍 x.com/wshuyi/status/…
> 
> ![Image](https://pbs.twimg.com/media/G-o8pqdWEAAtZnd?format=jpg&name=large)

* * *

**宝玉** @dotey [2026-01-14](https://x.com/dotey/status/2011489259824255448)

也支持 HTML，你把自己的风格保存成 html 文件，它就能自动选择复制粘贴到编辑器，但是 html 暂时不支持自动上传图片。

* * *

**宝玉** @dotey [2026-01-15](https://x.com/dotey/status/2011913398238298313)

地址变了一点，主要是加了个统一的前缀：

http://github.com/JimLiu/baoyu-skills/tree/main/skills/baoyu-post-to-wechat…

* * *

**Yangyi** @Yangyixxxx [2026-01-14](https://x.com/Yangyixxxx/status/2011488008554340581)

我来递工具助力

官方api推草稿箱

> 2026-01-13
> 
> 朋友们，免费来领取公众号发布API，Agents自动同步草稿箱
> 
> 如果你在使用ClaudeCode写公众号的话
> 
> 可以前往https://wx.limyai.com
> 
> 在左侧开放平台申请你的公众号Key
> 
> 授权公众号后，复制文档给你的ClaudeCode
> 
> 就可以直接用ClaudeCode推送文章到草稿箱了
> 
> 这个官方API大家自己去申请是相当麻烦的
> 
> ![Image](https://pbs.twimg.com/media/G-hrv7MbQAE-AMZ?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G-hrzTcaoAASGmn?format=jpg&name=large)

* * *

**铁锤人** @lxfater [2026-01-15](https://x.com/lxfater/status/2011617259505222047)

自动化微信不会搞事情吧

* * *

**宝玉** @dotey [2026-01-15](https://x.com/dotey/status/2011620388133093764)

这还好吧，没干啥坏事

* * *

**耳朵** @RookieRicardoR [2026-01-19](https://x.com/RookieRicardoR/status/2013264551001936286)

前两天看到这个帖子的时候，我还在想 Chrome 是可以通过 CDP 直接访问默认 Profile 的，刚才我一去搜才发现 Chrome 136 之后已经不再允许通过 CDP 访问默认 Profile，必须使用非默认 Profile 启动。

宝玉老师还是细，本来准备给您找 BUG，搞了半天是我知识该更新了。

* * *

**Jerlin** @eviljer [2026-01-14](https://x.com/eviljer/status/2011497431813537881)

把 Node 版本的 CC 卸了，剩下 brew 版本…

* * *

**AI铜锣猫** @langhai16501 [2026-01-15](https://x.com/langhai16501/status/2011799204012638498)

好用👏，是mac版本，window要稍微改下就可以用l

* * *

**宝玉** @dotey [2026-01-15](https://x.com/dotey/status/2011808636696191192)

请问windows版本要修改哪里？

* * *

**Terry** @trxuanxw [2026-01-15](https://x.com/trxuanxw/status/2011730344048017836)

请教宝玉老师，如果script是python脚本，那么是否需要另外告诉skill建立虚拟环境，安装倚赖包？

* * *

**宝玉** @dotey [2026-01-15](https://x.com/dotey/status/2011809020256956693)

我对python不太熟

* * *

**云天明web3AI资源导航** @yuntianming10 [2026-01-18](https://x.com/yuntianming10/status/2012905297614975020)

写了篇文章，是通过kimicc使用宝玉老师@dotey的skill,适合国内和小白非coding专业人员使用.但是使用发布到x的skill时，没有跳出chrome的x身份验证，没成功，后期再研究

> 2026-01-18
> 
> ![Article cover image](https://pbs.twimg.com/media/G-82S0MW0AAFxwJ?format=jpg&name=large)

* * *

**宝玉** @dotey [2026-01-18](https://x.com/dotey/status/2012905852873609391)

没有测试过kimi cc，可以直接问问kimi cc为什么没有

* * *

**zwdroid** @zwdroidai [2026-01-14](https://x.com/zwdroidai/status/2011488528731906293)

老师威武，被我言中了啊，试试发一篇

* * *

**宝玉** @dotey [2026-01-14](https://x.com/dotey/status/2011488697380741452)

我自己Mac上测试ok，如果遇到问题请反馈

* * *

**Lip Chan** @Chat24954Lip [2026-01-15](https://x.com/Chat24954Lip/status/2011679110993781122)

我用的Obsidian插件 note-to-mp，也非常好用

* * *

**极客杰尼** @seekjourney [2026-01-16](https://x.com/seekjourney/status/2012076766043783265)

我也做了一个自用的公众号排版吧 skill，打通公众号创作的最后一公里

> 2026-01-13
> 
> ![Article cover image](https://pbs.twimg.com/media/G-g9iWXboAA4dBc?format=jpg&name=large)