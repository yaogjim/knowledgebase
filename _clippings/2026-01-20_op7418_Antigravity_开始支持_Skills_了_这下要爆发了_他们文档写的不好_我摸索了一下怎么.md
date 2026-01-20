---
title: "2026-01-20_op7418_Antigravity_开始支持_Skills_了_这下要爆发了_他们文档写的不好_我摸索了一下怎么"
source: "https://x.com/op7418/status/2011278858897801228"
author:
  - "[[@op7418]]"
published: 2026-01-20
created: 2026-01-20
description:
tags:
  - "x"
  - "@op7418"
  - "https"
  - "2026-01-14"
---

# Antigravity 开始支持 Skills 了，这下要爆发了 他们文档写的不好，我摸索了一下怎么

**歸藏(guizang.ai)** @op7418 2026-01-14

Antigravity 开始支持 Skills 了，这下要爆发了

他们文档写的不好，我摸索了一下怎么用，这里分享一下

\------

Antigravity 支持两种类型的 Skills，Workspace 和全局。

具体的使用和创建方式就是将你的 Skills 文件夹移动到两个不同的文件位置。

Workspace Skills 需要在你当前打开的项目文件夹下，

<workspace-root>/.agent/skills/<skill-folder>/

比如我我的项目文件叫 Prompt 那他就在这个位置

/Users/guohao/Documents/Text content/Prompt/.agent/skills

全局的 Skills 需要放在 Antigravity 的安装文件夹下面，

~/.gemini/antigravity/skills/<skill-folder>/

比如我自己电脑的话他应该在这里：

/Users/guohao/.gemini/antigravity/skills/

Mac 下打开具体文件夹的方法是：点击访达，在桌面最上面的 Tab 栏找到前往，输入对应的路径。

当你把 Skill 放进去以后，Antigravity Agent 就可以看到你的 Skills 列表，然后如果你的对话内容看起来跟某个 Skills 相关，他就会读取这个 Skills. md 的内容并执行。

比如你用我写的 PPT 生成 Skills 的话就是，帮我基于 XXX 文档创建一个 PPT。

> 2026-01-14
> 
> 牛皮，Antigravity 现在已经支持完整的 Skills 规范
> 
> 你可以在里面使用和创建 Skills 了，这下 OpenAI、谷歌都支持了，Skills 要爆发了 x.com/antigravity/st…
> 
> ![Image](https://pbs.twimg.com/media/G-l_c38aEAAttGh?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G-lx_5jXkAALg_1?format=jpg&name=large)

* * *

**主任𒀭** @zhuren1992 [2026-01-14](https://x.com/zhuren1992/status/2011333172152426772)

Antigravity 技能规范完整了

* * *

**小耳Jane｜Xiaoer** @xiaoerzhan [2026-01-14](https://x.com/xiaoerzhan/status/2011316818779259237)

不用那么复杂

第一步:把下面这个官方文档丢给 Antigravity

https://antigravity.google/docs/skills

第二步:说“读这个文档 给我安装skills“

第三步:就给我搞定了

* * *

**Chris** @wifeForRao [2026-01-14](https://x.com/wifeForRao/status/2011286495068582328)

用上了，还带内置的生图，确实牛逼

![Image](https://pbs.twimg.com/media/G-mGSZibQAMv63N?format=png&name=large)

* * *

**Alfonsxh** @alfonsxh [2026-01-14](https://x.com/alfonsxh/status/2011325075384091045)

手搓了一个 skill 管理工具，支持所有这些 IDE 工具部署管理 skill 🤣🤣🤣

> 2026-01-14
> 
> 整了一个 skill 安装工具，支持 市面上主流的 Agent 工具（Codex、Claude、Gemini、Antigravity IDE、VSCode、OpenCode、Cursor）安装 skill：https://github.com/AlfonsSkills/SkillSync…
> 
> 1\. curl -fsSL https://raw.githubusercontent.com/AlfonsSkills/SkillSync/main/install.sh… | bash
> 
> 2\. 安装 skill 仓库：skillsync install anthropics/skills
> 
> 3.

* * *

**阿张SaulZhang** @MrYing67815618 [2026-01-15](https://x.com/MrYing67815618/status/2011625674277261606)

你好老师，请教一下你：这和原先anti自带的workflow有什么区别？我不太理解

* * *

**猎人威比 Hunter Wei** @wsiwsii [2026-01-14](https://x.com/wsiwsii/status/2011323531905417667)

全局安装的话怎么用/来触发呀？我只能看到本地项目的 agent

* * *

**0xfffCrypto** @0xfffCrypto [2026-01-14](https://x.com/0xfffCrypto/status/2011374354605740355)

老师！帮忙评价下 http://skillhub.club 支持多个coding agent一键导出，解决痛点，快速找到组合技能！谢谢

* * *

**时光** @tihubb\_ [2026-01-14](https://x.com/tihubb_/status/2011415684094546338)

为啥一直有地区限制，无法登录

* * *

**Don Winslow** @donwinslow

Thank you @adrianmckinty !

* * *

**0xEric** @0x\_z\_eric [2026-01-14](https://x.com/0x_z_eric/status/2011357083904733221)

看起来两边的skills是通用的，毕竟内容就是markdown

* * *

**大雾** @ethanligo [2026-01-14](https://x.com/ethanligo/status/2011296045821808878)

@readwise save

* * *

**suddenly** @suddenly01234 [2026-01-15](https://x.com/suddenly01234/status/2011661916519707107)

已经在用了，非常好用。而且还可以做一个全局rules，这样调用skill的时候会有提示。