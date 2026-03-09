---
title: "2026-03-09_sitin_sitin_一个人管10只小龙虾_我那台_Windows_电脑_64G_内存_配好之后放"
source: "https://x.com/sitinme/status/2029009436862497168"
author:
  - "[[@sitin]]"
published: 2026-03-09
created: 2026-03-09
description:
tags:
  - "#weekly"
  - "#code"
  - "x"
  - "@sitin"
---

# sitin # 一个人管10只小龙虾 我那台 Windows 电脑，64G 内存，配好之后放

**sitin**

# 一个人管10只小龙虾

我那台 Windows 电脑，64G 内存，配好之后放那儿半个月没碰过了。上面跑着 10 个小龙虾，小龙虾 A 和小龙虾 B 互相修，根本不需要我远程上去。Mac Mini 也配了一台，团队也在用。

群里经常有人问：为什么要开多个实例？配置文件老是出错怎么办？自动发X怎么做的？整理了一下，把这些问题一次讲清楚，加上我跑了半个月每天在用的场景。

## 经常被问的问题

Q：为什么要开多个实例，一个机器人全干了不行吗？

两个原因。第一，一个 bot 不够用，有很多事情可以交给它们干。第二，更重要的是，至少要有两个实例互为备份。其中一个配置文件搞坏了，另一个能帮你修。

Q：多实例需要多少资源？

大概 500 兆内存可以跑一个实例。我现在 10 个实例，大概消耗六七个 G 内存。用得越久，本地存的数据越多，我现在数据已经有一个 G 了。

Q：配置模型老是出错怎么办？

尽量别自己去改配置文件，容易改错。两个简单的办法：

第一种，先在本地装一个 Claude Code 或者 Codex，然后让它帮你配小龙虾。

第二种，先配国产模型。去买一个智谱或者 MiniMax 几十块钱的套餐，然后一路点 Yes，需要什么 key 就给它，先跑起来。跑起来之后再把 aigocode 的教程丢给它，让它帮你切换模型。

OpenClaw 部署指南

经验就是：多配几个实例，多配几个模型，基本上就没什么问题了。

Q：AI 写的东西不像我的风格怎么办？

半年以前 AI 写的东西还没我好，半年以后我已经追不上它了。选最好的模型，我只管 Yes 和 No 就完了。

## 三个平台怎么选

飞书

最早用飞书，因为团队日常办公就在上面。群里直接 @ 就能聊，很方便。但用了一阵发现两个问题：对话框不支持 Markdown 输出，流式响应不好。

做通知非常好，我们现在接了很多个 webhook，飞书群随时给我们发各种通知。

不过好消息是 OpenClaw 官方正在做飞书原生插件，目前已经在内测了。新插件支持流式输出卡片回复、表情回复、读取合并转发消息，还能以用户身份操作飞书的多维表格、日历日程、任务、云文档。之前飞书的短板基本都在补。如果你团队重度用飞书，可以关注一下这个插件的进展。

https://bytedance.larkoffice.com/share/base/form/shrcnATgLccRSVQ2HjX2NLxEZed?from=navigation

Discord

做出海方向，自然就转到了 Discord。一上手就觉得对了。建一个 Server，下面分 Channel：weekly、project、passage、construction，每个 Channel 还能开 Thread 做细分，主频道保持干净，细节全折叠在 Thread 里。

Discord 工作台

推荐知县（@zhixianio）的文章《Agent 训练师进阶指南：用 Discord 打造高效 OpenClaw 协作系统》https://x.com/zhixianio/status/2018599315116290469?s=46 @知贤 IOhttps://x.com/知贤 IO/status/2018599315116290469?s=46，我的 Discord 工作台就是参考他搭的。

日常频道说一句话，Agent 自动开 Thread 回复，不污染主线。不同 Channel 可以绑不同 Agent、配不同模型。OpenClaw 默认支持 4 个 Session 同时响应，相当于同时推 4 条线。

Telegram（主力）

Telegram 更轻量，配置简单，流式输出，emoji响应，移动端体验也好，走路上也能跟 Agent 聊。现在 Telegram 是主力。

Discord 重但组织能力强，适合团队协作。

## 怎么开多个实例

核心思路很简单：每个实例就是一个独立的 OpenClaw 进程，有自己的配置文件和 Bot Token。

Telegram 电报

已经有一个实例在跑的情况下，再开一个很简单：

1.找 @BotFather 创建一个新 Bot，拿到 Token

2.把 Token 发给你现有的小龙虾，让它帮你完成剩下的配置和启动

它会自动帮你建好新实例的配置文件、启动新进程。每个 Telegram Bot 就是一个独立的 Agent，跟不同的 Bot 聊就是跟不同的 Agent 对话。

多实例运行截图

Discord

跟 Telegram 一样，每个实例对应一个独立的 Discord Bot。

1.浏览器打开 discord.com/developers/applications discord.com/开发者/应用，点 New Application 创建一个新应用

创建 Discord Application 创建 Discord 应用程序

2.左侧点 Bot，点 Reset Token 生成 Token，保存好。然后把下面三个 Intent 全部打开，记得点 Save Changes

开启 Bot Intents 开启 Bot 意图

3.左侧点 OAuth2 → URL Generator，SCOPES 勾选 bot 和 applications.commands，BOT PERMISSIONS 勾选 Send Messages、Read Message History、View Channels，复制底部生成的链接，浏览器打开，选你的 Server 授权 3. 左侧点击 OAuth2 → URL Generator，在 SCOPES 中勾选 bot 和 applications.commands，在 BOT PERMISSIONS 中勾选 Send Messages、Read Message History、View Channels，复制底部生成的链接，在浏览器中打开，选择你的服务器进行授权。

4.把 Token 发给你现有的小龙虾，让它帮你完成剩下的配置和启动

搞定之后在 Discord 里就能看到 Bot 了，直接发消息就能对话。

Bot 在 Discord 中对话

每个 Bot 可以分配到不同的 Channel 里，各干各的。同一个 Server 里的 Bot，新建 Channel 它自动就在，不用再邀请。但如果你新建了一个 Server，需要重新把 Bot 邀请进去。

Discord 还有个好处：配合 Thread 用，主频道保持干净，细节折叠在 Thread 里。不同 Channel 可以给不同 Bot 配不同的 systemPrompt，比如 #weekly 频道配周报助手，#code #每周 #代码-review 频道配代码审核，各管各的。

飞书

有几个 Agent 就创建几个飞书应用。每个应用就是一个独立的飞书机器人。

1.登录飞书开放平台（open.feishu.cn 开放.飞书.cn），创建企业自建应用

2.进入应用详情页，在「凭证与基础信息」拿到 App ID 和 App Secret

3.先去「添加应用能力」加一个机器人，有些权限需要先有机器人能力才能开

4.进「权限管理」，把这些权限加上：contact:user.base:readonly、im:message、im:message.p2p\_msg:readonly、im:message.group\_at\_msg:readonly、im:message:send\_as\_bot、im:resource。如果想让机器人不用 @ 也能响应群消息，再加 im:message.group\_msg 4. 进入「权限管理」，添加以下权限：contact:user.base:readonly、im:message、im:message.p2p\_msg:readonly、im:message.group\_at\_msg:readonly、im:message:send\_as\_bot、im:resource。如果想让机器人不用 @ 也能响应群消息，再加 im:message.group\_msg

5.进「事件与回调」，事件配置方式选「使用长连接接收事件」，添加这几个事件：im.message.receive\_v1（必需）、im.message.message\_read\_v1、im.chat.member.bot.added\_v1、im.chat.member.bot.deleted\_v1

6.点「版本管理与发布」→ 创建版本 → 申请发布

7.把 App ID 和 App Secret 发给你的小龙虾，让它完成配置。或者手动执行：

> openclaw config set channels.feishu.appId "cli\_xxxxx" openclaw config set channels.feishu.appSecret "your\_app\_secret" openclaw config set channels.feishu.enabled true openclaw 配置 set channels.feishu.appId "cli\_xxxxx" openclaw 配置 设置 channels.飞书.appSecret "your\_app\_secret" openclaw 配置 设置 channels.飞书.enabled true

发布后就能在飞书里和机器人对话了，拉到群里 @ 它就行。

有个坑：群聊默认是白名单模式，机器人拉到群里可能不回复。让小龙虾自己改一下群聊策略配置就好了。

飞书用的是 WebSocket 长连接，不需要配回调地址，也不需要公网 IP。

## 几个实用的场景

发公众号

以前写一篇公众号：选题 1 小时 + 写稿 1 小时 + 排版 30 分钟 + 配图 20 分钟 = 将近 3 小时。

现在跟 AI 说一句"帮我写一篇 xxx，推到公众号草稿箱"。它自动获取 access\_token、上传图片到微信素材库、生成 HTML、推到草稿箱。我打开草稿箱检查一下，直接发布。10 分钟搞定。

踩过一个大坑：Python 发中文到微信 API 会乱码，requests.post(url, json=data) 默认把中文转成 \\uXXXX，微信不会自动解码。必须手动 json.dumps(data, ensure\_ascii=False).encode("utf-8")。这个坑浪费了半天。

（详细配置见 5分钟让AI帮你发公众号）

推特运营

情报 Agent 定时刷 X，筛选有爆款潜力的内容推到素材库。推文 Agent 从素材里挑选，直接帮我发推。

现在推特用户的回复我都不自己回了，全部通过小龙虾来操作。

你们可以把这条推特丢给你们的小龙虾，让它照着配置：https://x.com/sitinme/status/2027202544490213522

代码审核

这是我觉得 Agent 目前对做产品最方便的事情。配置好之后，可以直接在手机端操作小龙虾，让它帮你写网站、部署、推 GitHub、改代码。

完整的流程是这样的：Agent 拉取项目代码，跑接口测试、用浏览器测页面交互，发现问题记录到 Notion 文档。然后用 Claude Code 根据文档针对性修复，修完让 Agent 再检查。几轮下来，发现过不少人工不容易注意到的 bug。

情报采集

多个 cron 定时任务，分别监控不同数据源：OpenClaw 相关内容、AI 出海热点、有潜力的新项目。采集到的内容自动沉淀到 Notion，打上标签分类。

以前每天花 1 小时刷信息流，现在打开 Notion 看整理好的就行。

知识星球

## 文档即大脑

有一句话我特别认同：你的一切，最终都要落到文档上。

不管是采集的情报、踩过的坑、总结的经验、写好的草稿、发现的 bug，全部沉淀到文档。

我用 Notion + Obsidian 双备份。Agent 产出的所有内容自动写入 Notion（接了 4 个数据库 API：工作日志、内容草稿、用户管理、知识库），同时同步到 Obsidian 作为本地备份。

为什么要双备份？OpenClaw 自带记忆系统（MEMORY.md + memory/ 目录），但不排除网络中断、上下文压缩导致信息丢失。维护好文档体系，就算 Agent 失忆了，把文档喂给它，立马恢复。

操作很简单，直接跟小龙虾说"帮我把所有内容同步到 Notion"，它会提醒你要一个 Notion API key，你把一个页面的 API key 给它，以后所有内容都会同步过去。我基本上每天让它给我写日报，汇报今天做了哪些事、有哪些事待做。

Obsidian 的双链笔记在这里特别好用。Agent 写入的每条信息都能通过 wikilinks 跟其他笔记建立联系，时间长了自然形成知识网络。如果你把内容同步到了 Obsidian，本地还可以用 Claude Code 来管理这些 Markdown 文件和 Skills，特别方便。

（详细方案见 我把 OpenClaw 所有内容丢进了 Obsidian）

## 踩坑经验

模型配置

刚开始对模型配置不熟，经常出问题：对话中断、Agent 失忆、光回复但不执行操作。折腾了好几天才搞明白 baseUrl、apiKey、api 字段怎么配。

现在配了多个大模型做备份，一个有问题立刻切到另一个，用 /model 命令就能切换。深度思考用 Claude Opus，写代码可以用 Codex（免费），日常杂活用便宜的模型。还配了故障转移，watchdog 每 5 分钟检测一次，主模型挂了自动切备用。

部署环境

现在 Windows 64G 内存的主力机稳定跑着，从来没宕机过。另外买了台 Mac Mini M4，团队在用。

## 成本

很多人觉得搞 AI 很贵。算笔账：

硬件一台 Windows 主力机（已有的，64G 内存），加一台 Mac Mini M4 给团队用，3186 块。月度费用：电费几块钱，Claude Max 大概 1450（$200/月，主力模型），Codex 免费，Brave Search 35 块（情报抓取用）。月均总成本大约 1490。

做个对比：请一个实习生 3000 块一个月，每天工作 8 小时，会请假。我的 AI 团队 1490 一个月，7×24 在线，不休息。而且模型升级了，能力自动变强。

## 10 分钟拥有你的第一个 AI 员工

不需要会写代码，不需要买服务器。

npm install -g openclaw && openclaw onboard npm 安装 -g openclaw && openclaw onboard

去 aigocode.com 注册拿 API Key，找 @BotFather 人工智能代码网.com@机器人之父 建个 Telegram Bot 填上 Token，基本就能跑起来了。跑起来之后你会发现，一个不够，你想要第二个、第三个。最后就变成了我现在这样，管理一支 AI 团队。

## 相关资源

- OpenClaw 开源仓库：https://github.com/openclaw/openclaw
- 官方文档：https://docs.openclaw.ai/
- 中文社区：https://t.me/claw101
- AI 模型 API（国内直连）：https://aigocode.com/
- 技能商店：https://clawhub.com/

## 加入 OpenClaw 交流群

如果你对 OpenClaw 感兴趣，或者在实践中遇到问题，欢迎加入 OpenClaw 中文交流群。

99 元入群，送 $50 aigocode.com 算力额度。群里都是实际在用 OpenClaw 的玩家，每天分享使用技巧和踩坑经验，氛围很活跃。