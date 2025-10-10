---
title: "Jesse Lau 谈谈 O3 的局限性和 Gemini 的优势"
source: "https://x.com/jesselaunz/status/1913708817835241752"
author:
  - "[[@jesselaunz]]"
created: 2025-04-21
description:
tags:
  - "@jesselaunz #python #ai #o3 #gemini #longcontextwindow #webdevelopment"
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
**Jesse Lau** @jesselaunz 2025-04-19

o3目前的agent还很初级，主要是生成所有project代码后，调用python的文件生成、zip打包提供下载，也就是再加一道编程而已（图一）

然而，因为长context window的处理水平没有提升（图二），对于我已经建好django template（文件很多，tokens很大）的情况下，o3基本上起不到帮助，只能打打零工

TA前端水平不太行（图三），只能用于编单一功能的python脚本等等

而o3 chat界面自动化agent功能，我其实早就自己做好了py脚本

通过gemini 2.5 pro等较好支持long context window的model做好project+翻译后，我自己再运行本地的脚本，即可生成多种语言版本并自动deploy（图四）

相当于半自动化agent，使我每天的project只需半小时就可搞定，这在AI前时代，至少需要1个礼拜的工作量

> 2025-04-19
> 
> try o3, it's an agent model  
> 尝试 O3，它是一个代理模型
> 
> ![Image](https://pbs.twimg.com/media/Go7b587a0AAu8W8?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/Go7b587a8AA2Vp5?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/Go7b584bsAAZOzM?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/Go7b6AHaAAADf5d?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/Go6Mu3UbsAAX7ls?format=jpg&name=large)

---

**Jesse Lau** @jesselaunz [2025-04-20](https://x.com/jesselaunz/status/1913805572933296625)

直观感受了Gemini大窗口的🐮

900k的prompt因为输出受限没搞定，分成两个，每个400多k完美解决

> 2025-04-20
> 
> 我靠，极限测试了要
> 
> 最大初始prompt
> 
> 我估计一把搞不定，需要我再搞个脚本拆分一下 x.com/jesselaunz/sta…
> 
> ![Image](https://pbs.twimg.com/media/Go8oD6la4AAD943?format=png&name=large)