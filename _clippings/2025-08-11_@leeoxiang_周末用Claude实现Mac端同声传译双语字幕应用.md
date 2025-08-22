---
title: "周末用Claude实现Mac端同声传译/双语字幕应用"
source: "https://x.com/leeoxiang/status/1954517729333202956"
author:
  - "[[@leeoxiang]]"
published: 2025-08-11
created: 2025-08-11
description:
tags:
  - "@leeoxiang #同声传译 #双语字幕 #Mac应用 #实时翻译 #机器翻译"
---
**Leo Xiang** @leeoxiang [2025-08-10](https://x.com/leeoxiang/status/1954517729333202956)

一个周末借助Claude完成一个同声传译/双语字幕的Mac端应用：

1、支持ScreenCaptureKit 采集系统声音、单应用声音、以及麦克风声音，以及多流的mixer；

2、支持OpenAI Realtime API 以及 阿里云Gummy 实时转录模型；

3、支持多家大模型翻译API。

PS：也能支持视频号视频/直播的实时字幕和翻译了。

有相关需求的伙伴可以一起聊聊，看是否可以做成一个产品或者API 出来？

![Image](https://pbs.twimg.com/media/Gx_V0FPacAA6Npq?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/Gx_WpL3bkAArojT?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/Gx_Vj8RbgAAoKvO?format=jpg&name=large)

---

**逆天** @forever7943 [2025-08-10](https://x.com/forever7943/status/1954528107076947984)

用实时api就不用考虑vad了？实时api好像挺贵的吧，可以考虑支持whisper和本地翻译，后者要vad

---

**Leo Xiang** @leeoxiang [2025-08-10](https://x.com/leeoxiang/status/1954528364678586770)

用实时的最好也自己做vad，云API的vad不一定能满足自己的场景。

---

**Xu Desheng** @xudesheng [2025-08-10](https://x.com/xudesheng/status/1954644619175809221)

哈哈，我周末也vibe coding了一把 https://x.com/xudesheng/status/1954616813796446496… ，但与你这个就无法比了。正好今天朋友讨论假日摆摊，摊位上怎么弄个供不同语言访客来询问的东西，你这个方案有很大参考意义。

> 2025-08-10
> 
> 周五车子出车祸回家后，到周六半夜为止，全力Vibe Coding，糊了个网站： https://demotest.io ，没有手工输入任何代码，没有编写任何测试用例，将常用的工具做在一起。Claude Code、ChatGPT、Gemini CLI以及Cursor都用到，主要是前两者，如果再来一次，速度会快很多；准备将整个过程记录一下。

---

**fancyboi** @z2631966523 [2025-08-10](https://x.com/z2631966523/status/1954564406278549599)

我一直想做一个产品，可以实时把视频中说话者的语言翻译成另一种语言，同时保留并克隆说话者的声音，让译后的声音听起来就像原人说的一样。B站的内测功能好像就是类似的——先克隆说话者的声音，再用翻译后的内容合成语音，达成实时翻译，听感无障碍

---

**yanhua** @yanhua1010 [2025-08-11](https://x.com/yanhua1010/status/1954696299560964202)

这该死的渐变

---

**世界很大，我希望去看看** @0x0000001b [2025-08-10](https://x.com/0x0000001b/status/1954567468065689971)

弄个app，搭配一个耳机和播放设备例如苹果手表，场景可观