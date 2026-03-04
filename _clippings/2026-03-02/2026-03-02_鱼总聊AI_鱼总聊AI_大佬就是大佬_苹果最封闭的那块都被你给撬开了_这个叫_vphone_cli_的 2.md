---
title: "2026-03-02_鱼总聊AI_鱼总聊AI_大佬就是大佬_苹果最封闭的那块都被你给撬开了_这个叫_vphone_cli_的"
source: "https://x.com/grok/status/2028195980391162270"
author:
  - "[[@鱼总聊AI]]"
published: 2026-03-02
created: 2026-03-02
description:
tags:
  - "x"
  - "@鱼总聊AI"
  - "ios"
  - "https"
---

# 鱼总聊AI 大佬就是大佬，苹果最封闭的那块都被你给撬开了。 这个叫 vphone-cli 的

**鱼总聊AI**

大佬就是大佬，苹果最封闭的那块都被你给撬开了。 这个叫 vphone-cli 的开源项目，可以在 Mac 上直接跑完整 iOS 系统虚拟机。 注意，这不是模拟器哈。是真的 iOS。 可以批量开，批量关，脚本控制，在CI 里直接用。 以前做 iOS 自动化测试要买一堆真机接一堆线，现在变成 vphone create 一条命令。

![图片](https://pbs.twimg.com/amplify_video_thumb/2027794518066794504/img/JtsUvJfWQ-tSSW7a.jpg)

[![视频](https://pbs.twimg.com/amplify_video_thumb/2027794518066794504/img/JtsUvJfWQ-tSSW7a.jpg)](https://x.com/grok/status/2028195980391162270)

> **@Lakr233**
> 
> I've made changes to vphone-cli so you can now use the virtual device without a VNC.

* * *

### 热门回复

**@Grok** ♥ 6 · 💬 0

用苹果 Virtualization.framework（私用 PV=3 API）+ PCC research VM（Private Cloud Compute 研究固件）实现。 核心是：合并 iPhone IPSW 和 cloudOS IPSW 做混合固件，动态 patch boot chain（LLB、iBSS、iBEC 等 6 个组件，41+ 修改）绕过签名、FairPlay 和激活检查。 主机要 disable SIP/AMFI + 开启 research entitlements，创建模拟 iPhone17,3 硬件的 VM。 流程：DFU 模式 restore → 注入 SSH ramdisk → 装 CFW → 正常 boot 进完整 iOS 26 系统，支持 SSH/VNC 操作。 牛在用苹果自家基础设施撬开了封闭生态，纯研究向。 详情看 GitHub:

**@AI人工智能自媒体** ♥ 1 · 💬 1

@grok 怎么做到的