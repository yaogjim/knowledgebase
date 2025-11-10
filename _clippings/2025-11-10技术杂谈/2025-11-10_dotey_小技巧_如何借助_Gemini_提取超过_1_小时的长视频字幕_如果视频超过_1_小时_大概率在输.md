---
title: "2025-11-10_dotey_小技巧_如何借助_Gemini_提取超过_1_小时的长视频字幕_如果视频超过_1_小时_大概率在输"
source: "https://x.com/dotey/status/1985435973157863935/?rw_tt_thread=True"
author:
  - "[[@dotey]]"
published: 2025-11-10
created: 2025-11-10
description:
tags:
  - "x"
  - "@dotey"
  - "https"
  - "image"
---

# 小技巧：如何借助 Gemini 提取超过 1 小时的长视频字幕？ 如果视频超过 1 小时，大概率在输

**宝玉** @dotey 2025-09-27

小技巧：如何借助 Gemini 提取超过 1 小时的长视频字幕？

如果视频超过 1 小时，大概率在输出到 1 小时左右的位置时，Gemini 会中断输出，并且已经输出的内容都看不到了（参考图1）。

这个问题可以通过这两种方式之一解决：

1\. 在接近 1 小时的位置手动停止输出，在停止后输入 "continue" 继续（参考图2）。但这种方式有时候还是可能会输出失败，似乎 Gemini 对于太长的输出还是有限制

2\. 在接近 1 小时的位置手动停止输出，在停止后把之前的目录复制出来（参考图3），在 Gem 中新开一个会话，把视频地址和目录一起粘贴过去，然后在底部加一句：

\> please start from "{从目录中复制出来的你希望开始的章节位置}"

（参考图4）

你还可以让它在指定位置结束：

\> please start from "{开始章节}" to "{结束章节}"

这样就可以避免因为内容太长而停止输出的问题

> 2025-09-27
> 
> Prompt：Transcribes YouTube videos (from a URL) or uploaded local videos into a structured, formatted text complete with speaker labels and timestamps.
> 
> 提取 YouTube 视频字幕为带发言人和时间戳格式化文本的提示词，只支持 Gemini，可以做成 Gemini Gme，使用时输入YouTube视频UR x.com/dotey/status/1…
> 
> 提示：将 YouTube 视频（通过 URL）或上传的本地视频转录为结构化的格式化文本，包含说话人标签和时间戳。
> 
> 提取 YouTube 视频字幕为带发言人和时间戳格式化文本的提示词，仅限 Gemini 使用，可命名为 Gemini Gme。使用时输入 YouTube 视频 URL：x.com/dotey/status/1…
> 
> ![Screenshot of Gemini interface displaying error message about lacking access to content with YouTube link and suggestion to try again. Second image shows conversation in Gemini about Boris discussing adoption curve and simplifying content for LLM with text on handling long outputs. Third image lists table of contents for Secrets of Claude from engineers including topics like model opening and power of tools. Fourth image shows product management challenges table with topics like building yourself in LLM and deploying features.](https://pbs.twimg.com/media/G42tptfXAAASp-l?format=jpg&name=large) ![Screenshot of Gemini interface displaying error message about lacking access to content with YouTube link and suggestion to try again. Second image shows conversation in Gemini about Boris discussing adoption curve and simplifying content for LLM with text on handling long outputs. Third image lists table of contents for Secrets of Claude from engineers including topics like model opening and power of tools. Fourth image shows product management challenges table with topics like building yourself in LLM and deploying features.](https://pbs.twimg.com/media/G42t-hLXMAEUpAb?format=jpg&name=large) ![Screenshot of Gemini interface displaying error message about lacking access to content with YouTube link and suggestion to try again. Second image shows conversation in Gemini about Boris discussing adoption curve and simplifying content for LLM with text on handling long outputs. Third image lists table of contents for Secrets of Claude from engineers including topics like model opening and power of tools. Fourth image shows product management challenges table with topics like building yourself in LLM and deploying features.](https://pbs.twimg.com/media/G42usZiWwAAWktY?format=jpg&name=large) ![Screenshot of Gemini interface displaying error message about lacking access to content with YouTube link and suggestion to try again. Second image shows conversation in Gemini about Boris discussing adoption curve and simplifying content for LLM with text on handling long outputs. Third image lists table of contents for Secrets of Claude from engineers including topics like model opening and power of tools. Fourth image shows product management challenges table with topics like building yourself in LLM and deploying features.](https://pbs.twimg.com/media/G42vK0kXoAApY1u?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G11GTZRXoAEuFfT?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G11GfpaXYAArc-G?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G11Gs0VWsAAFkRW?format=jpg&name=large)

* * *

**Tseng Hsiang** @lamara953 [2025-11-03](https://x.com/lamara953/status/1985492129129582611)

用google ai studio可以在貼YT連結時直接指定起始以及結束時間，所以用gemini網頁目前還不行？

* * *

**宝玉** @dotey [2025-11-04](https://x.com/dotey/status/1985501812225433691)

应该是一样的，方案二就是加时间范围

* * *

**Winnerineast** @winnerineast [2025-11-04](https://x.com/winnerineast/status/1985524549128257788)

其实这个动作谷歌内部用代码或者AI生成代码给接上去，这就是一个无限视频.........谷歌不做是大厂的仁慈还是懒惰，还是长尾需求？

* * *

**fakeworld** @XiaxueleC61xop [2025-11-03](https://x.com/XiaxueleC61xop/status/1985481414767427901)

分割音频，逐段输出后拼接。但是，时间有点不准。

* * *

**fisherdaddy** @fun000001 [2025-11-04](https://x.com/fun000001/status/1985682613424779602)

本以为 gemini 是通过调用了获取 AI 字幕的工具的方式来获取字幕，并按照 Prompt 格式进行输出。但实际上对于没有字幕的视频，试了下宝玉老师的这个方法确实会识别其中的字幕，缺点就是输出速度有点慢。

其实 YouTube 上的大多数英文访谈类或播客类的视频都有 srt 之类的字幕数据，可以直接找个

* * *

**冰河** @binghe\_sun [2025-11-04](https://x.com/binghe_sun/status/1985735358433411281)

我是直接下载字幕，然后再让gemini或GTP来帮我总结。

* * *

**jfdi1001** @jfdi1001 [2025-11-03](https://x.com/jfdi1001/status/1985466850122297708)

@readwise save thread

@readwise 保存主题

* * *

**OSDev** @OiiDev [2025-11-03](https://x.com/OiiDev/status/1985492417634512957)

@readwise save thread

@readwise 保存主题

* * *

**balon@huggingface** @balon\_f3 [2025-11-04](https://x.com/balon_f3/status/1985581655235740134)

为什么不切视频后再提取呢？

* * *

**紫苏子ACG** @Pixelxzen [2025-11-04](https://x.com/Pixelxzen/status/1985648181737377965)

本地开发了web应用，直接无损切割自定义时长的视频，2.5 小时的视频，瞬间完成 3 个文件视频，导出为mp3 给Ai Studio识别完成录音逐字稿即可。

* * *

**Tommycat** @tommy\_725 [2025-11-03](https://x.com/tommy_725/status/1985467070184898970)

有没有有人遇上在GEMINI输出太长内容（或者输出时间长），输出完毕后，跳出让用户sign in的对话框，一点sign in整个session都没了。是Bug？