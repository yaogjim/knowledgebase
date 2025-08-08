---
title: "利用 AI 编程快速开发 Chrome 插件，解决个人需求"
source: "https://x.com/vista8/status/1906752136345788879"
author:
  - "[[@vista8]]"
created: 2025-04-01
description: "5分钟写一个Chrome插件！ 之前写的复制标题和URL的Chrome插件源码被误删。 索性重写，两周Vibe Coding经验，熟练度提升，5分钟搞定。 实现步骤： 1. 新建一个文件夹，Windsurf打开 2. Cursor Directory复制一个Chrome插"
tags:
  - "@vista8 #AI编程 #Chrome插件 #效率提升 #个客定制 #开发工具"
---
**向阳乔木** @vista8 [2025-03-31](https://x.com/vista8/status/1906752136345788879)

5分钟写一个Chrome插件！

之前写的复制标题和URL的Chrome插件源码被误删。

索性重写，两周Vibe Coding经验，熟练度提升，5分钟搞定。

实现步骤：

1\. 新建一个文件夹，Windsurf打开

2\. Cursor Directory复制一个Chrome插件开发Rules，新建文件粘贴，命名http://rules.md

3\. 指定参考Rules文件开发，写提示词说明需求。（图1）

4\. icon点kitchen生成图标，告诉用这个文件夹中图标

一次成功，其余3轮对话都是调细节，如不用弹窗，成功反馈样式等。

插件下载见评论

![Image](https://pbs.twimg.com/media/GnYjmmtagAAL5RR?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/GnYjv9MbQAAvQng?format=png&name=large) ![Image](https://pbs.twimg.com/media/GnYj683aIAMMmuG?format=png&name=large) ![Image](https://pbs.twimg.com/media/GnYkAYEaMAAUsy7?format=png&name=large)

---

**向阳乔木** @vista8 [2025-03-31](https://x.com/vista8/status/1906752476583502284)

EasyCopy插件下载：https://pan.quark.cn/s/bb8dcf197a37

图标制作：https://icon.kitchen

Cursor Rule：

---

**yuanming** @leejincai [2025-03-31](https://x.com/leejincai/status/1906825383716307210)

有了AI之后越来越多的轮子了，我一直都用tabcopy，非常好用

---

**向阳乔木** @vista8 [2025-03-31](https://x.com/vista8/status/1906851595478003833)

以前也一直用tabcopy，但某次更新他们为了满足更多人需求，变成了点击一次出弹层，再点一次才能复制。

对个人需求讲，多了一步操作。

这是AI编程的巨大价值，完全根据自己需求定制软件。

---

**朝歌** @Zhaoge01 [2025-04-01](https://x.com/Zhaoge01/status/1906863807080939908)

Rules是啥

---

**向阳乔木** @vista8 [2025-04-01](https://x.com/vista8/status/1906867305411465315)

类似于编程软件的系统提示词，用一个文本写要求。

分全局提示词和针对项目的提示词。

最早见到是在Cursor AI，一般命名为 cursorrules.mdx

---

**hahagood** @hahagood [2025-04-01](https://x.com/hahagood/status/1906883092406784087)

插件 surfingkeys 本身就有复制 url 的快捷键 yy,

我又在后面添加了两个, 功能是复制 url + title, 一个是用在微信里转发, 另一个是用在 org-mode 保存:

api.mapkey('yo',"#7Copy current page's title and URL for org-mode", function() {

Clipboard.write('\[\[' + window.location.href + '\]\['

---

**SimbaLee** @lipeng0820 [2025-04-01](https://x.com/lipeng0820/status/1906891582416334977)

掌握AI coding后最有用的就是自己能写一堆浏览器插件，帮助解决小众场景问题