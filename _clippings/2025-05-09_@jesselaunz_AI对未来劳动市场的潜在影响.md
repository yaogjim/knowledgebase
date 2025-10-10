---
title: "AI对未来劳动市场的潜在影响"
source: "https://x.com/jesselaunz/status/1920640617149050955"
author:
  - "[[@jesselaunz]]"
created: 2025-05-09
description:
tags:
  - "@jesselaunz #AI #未来职场 #劳动力市场"
status: "inbox"
importance: 2
effort: 2
review_level: 0
review_next: "2025-10-17"
review_interval: null
review_count: 0
decision: null
topics: []
links_out: []
summary: ""
pov: ""
actions: []
---
**Jesse Lau 遁一子** @jesselaunz 2025-05-08

AI Studio恢复了对音频视频的处理，昨天忘了发个推，今天补上😁  
  
不过gemini对SRT格式的文本总是会出错，经常小时的时间轴不写，剪映等软件无法识别。  
  
可以建一个新的chat，system prompt如下：  
  
✅ SRT 文件标准格式结构

每条字幕由三部分组成：  
  
字幕编号（从1开始递增）  
  
时间码（表示字幕出现和消失的时间）  
  
字幕文本  
  
每条字幕之间用空行隔开。  
  
1

00:00:01,000 --> 00:00:04,000

Hello, welcome to the show.  
1

00:00:01,000 --> 00:00:04,000

你好，欢迎来到这个节目。  
  
2

00:00:04,500 --> 00:00:07,000

Today we're going to talk about AI.

🕒 时间码格式  
2

00:00:04,500 --> 00:00:07,000

今天我们要谈论人工智能。

🕒 时间码格式  
  
小时:分钟:秒,毫秒

时间区间之间用 --> 分隔  
  
毫秒使用英文逗号,表示（不是句点.）  
  
✅ 正确格式：  
  
00:01:30,500 --> 00:01:33,000

🔁 最终格式规则总结：

字幕编号（整数）  
  
时间轴（格式严格固定）  
  
字幕正文（可多行）  
  
每条字幕之间必须空一行  
  
⚠ 常见错误注意事项：  
  
错误类型：00:01:774 --> 00:05:874 ，错误省略了小时。

注意时间格式严格为小时:分钟:秒,毫秒，小时00不能省略

""""

你的任务是根据上面SRT原则，将我贴上来的视频生成标准SRT格式的字幕

> 2025-05-08
> 
> 前面5秒的veo2美女降低了30秒的播放率。看来不太适合这类播客视频。
> 
> 这类播客主要针对用户利用碎片时间来获得一些感兴趣的知识点
> 
> 如果没有全程美女同步对嘴型播放，估计还是简单的整个图加点动画效果好点
> 
> 今天研究一下AI对未来劳动市场的潜在影响
> 
> 过两天整个英文播客试试 x.com/jesselaunz/sta…
> 
> ![Image](https://pbs.twimg.com/media/Gqd77DyWgAAkoLa?format=jpg&name=large)

---

**Osaker** @gogoxui [2025-05-09](https://x.com/gogoxui/status/1920648298634822054)

如果不翻译，光stt，whisper.cpp + large v3 turbo就已经很够用了，用mac mini来处理可以干到25x，格式什么的都没问题。

用LLM来STT总觉得他会在什么地方漏几句，不放心😂

---

**Jesse Lau 遁一子** @jesselaunz [2025-05-09](https://x.com/jesselaunz/status/1920652953519575513)

gemini pro还可以，比较稳定。主要whisper有时生成的有些字面错误