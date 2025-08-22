---
title: "比特尔 - 扩展比特聊天网络的独立网状中继节点"
source: "https://x.com/markkasaurus/status/1949971774579343756"
author:
  - "[[@markkasaurus]]"
created: 2025-07-29
description: "Technical enough to be annoying, dumb enough to be useful. Focused on the branding and marketing layer of engineering.Founder of @Blokhaus"
tags:
  - "@markkasaurus #比特尔 #ESP32 #网状网络 #去中心化通信 #蓝牙 #比特聊天"
---
**Mark Soares** @markkasaurus [2025-07-28](https://x.com/markkasaurus/status/1949971774579343756/history)

  
费了一番功夫，但比特尔 v.01 已可运行；比特尔是一个基于 ESP32 的自供电独立网状中继节点，用于杰克的比特聊天（一种去中心化消息协议）；它可以依靠太阳能无限期运行，或依靠电池运行约 25 至 50 天；其外壳具备防雨功能，适用于在恶劣条件下安装。它应该能将蓝牙在户外的覆盖范围扩展 300 至 500 英尺。

Bitle 通过低功耗蓝牙实现了 bitchat 二进制协议，与 bitchat 设备建立通用属性配置文件（GATT）服务器连接，并作为中间节点来扩展网状网络的范围。Bitle 处理用于安全通信的噪声协议握手，处理加密的用户消息，并通过网状网络转发这些消息。

它被设计为一个专业的网状中继器，通过提供额外的路由节点来增强 bitchat 的去中心化架构，无需用户交互，也不会在消息接口中显示为对等方。

我设想它可作为偏远地区的地面节点，比如徒步小径、露营地等（因此得名 Bitle——“Biddle”或“甲虫”），这些地方信号可能很弱，而通信至关重要。最重要的是，尽管信号/无线网络可能很充足，但 bitchat 并非真的要成为在线通信的备用方案——它是关于选择在没有集中式基础设施的情况下进行通信；点对点——像 Bitle 这样的设备似乎对实现这一点很有帮助。应该可以很便宜地制作这些设备的网格，并建立一个任何人都可以在离线状态下通过其进行通信的环境网状网络。该设备的大部分体积在于电池/太阳能/外壳/电源板——如果将其内置到灯泡或任何插件设备中，它会小得多。

![Image](https://pbs.twimg.com/media/Gw-tJRxXQAEvl65?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/Gw-vJYIWUAAe1b8?format=jpg&name=large)

---

**MeanHash ₿ ✪** @MeanHash [2025-07-28](https://x.com/MeanHash/status/1949982635205317075)

  
现在我们需要开始大规模生产一些配备蓝牙 5 的产品了。

![Image](https://pbs.twimg.com/media/Gw-635SXkAAeicv?format=jpg&name=large)
