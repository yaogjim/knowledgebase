---
title: "2026-02-25_Leo_Xiang_Leo_Xiang_openai_最新的_websocket_协议支持_预缓存了_在预缓存的"
source: "https://x.com/leeoxiang/status/2026214722421633273"
author:
  - "[[@Leo Xiang]]"
published: 2026-02-25
created: 2026-02-25
description:
tags:
  - "x"
  - "@Leo Xiang"
  - "xiang"
  - "websocket"
---

# Leo Xiang openai 最新的 websocket 协议支持 预缓存了，在预缓存的

**Leo Xiang**

openai 最新的 websocket 协议支持 预缓存了，在预缓存的场景下首token延迟能到100ms级别，对实时交互的场景会非常友好。

![图片](https://pbs.twimg.com/media/HB6PjHOaUAAvKpZ?format=jpg&name=large)

* * *

### 热门回复

**@Zub8eti** ♥ 14 · 💬 0

Zub8eti | "Introduction"

**@Leo Xiang** ♥ 5 · 💬 1

目前 Websocket in Response API 多个会话之间连接无法复用： 1、对于首包延迟提升不大； 2、对于有很多轮 tool call 场景提升会比较大；