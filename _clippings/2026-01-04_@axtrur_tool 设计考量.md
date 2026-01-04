---
title: "tool 设计考量"
source: "https://x.com/axtrur/status/2007686506652332212"
author:
  - "[[@axtrur]]"
date: "2026-01-04T18:03:45+08:00"
created: 2026-01-04
description:
tags:
  - "@axtrur #工具开发 #面试题 #工具设计 #软件开发"
---
**axtrur** @axtrur 2026-01-03

我猜要考察的是应聘者对于一个tool的设计会考虑哪些事情，我粗略想了下应该有：

1\. 参数顺序如何控制才能防止参数顺序带来的UI渲染的奇怪问题

2\. 除了功能字段比如path,content字段之外是否需要加入一些description字段提升UI体验

3\. 除了tool功能本身之外，可以有哪些tool call 异常error增强和牵引设计

4\. 大文件读写如何处理，比如是否要分层加载或流式读取 5.不同场景下的read\_file, write\_file考虑的点是否不一样

6\. 如果要做checkpoint，是否要放到tool里还是hooks里。

7\. 不同环境如何设计，比如远程沙箱环境，本地环境等，还是同个Filesystem么？

8\. 某些场景是否需要做业务旁路逻辑

> 2026-01-03
> 
> Context Engineering 面试题：在 XX 业务场景下面，read\_file, write\_file 如何设计？
> 
> 面试中遇到这题我估计临场发挥不会太好😅
> 
> 你答得好吗？ x.com/yan5xu/status/…