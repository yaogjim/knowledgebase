---
title: "利用 NotebookLM 和 twillot 提升书签搜索效率"
source: "https://x.com/Yonah_x/status/1908794375456309650"
author:
  - "[[@Yonah_x]]"
created: 2025-04-07
description: "X 书签搜索工作流更新：NotebookLM 搭配 twillot 效率更高。 之前帖子评论有人给我推荐了twillot，于是我去试用了一下，发现twillot确实好用，首先关键词检索挺好用，其次有些小细节比twitter-web-exporter要好，它会把 thread 的帖"
tags:
  - "@Yonah_x #书签 #搜索 #NotebookLM #twillot #效率提升 #笔记 #工具"
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
**汉松** @Yonah\_x 2025-04-04

X 书签搜索工作流更新：NotebookLM 搭配 twillot 效率更高。

之前帖子评论有人给我推荐了twillot，于是我去试用了一下，发现twillot确实好用，首先关键词检索挺好用，其次有些小细节比twitter-web-exporter要好，它会把 thread 的帖子聚合成一个。

NotebookLM的强项是 RAG 语义检索准，但因为文档分块有时候不能找到原文链接，这个时候我就会根据关键字去twillot上面搜索。

所以 NotebookLM 搭配 twillot 效率更高，一个负责语义检索，一个负责精确定位和导出书签。

![Image](https://pbs.twimg.com/media/Gn1mInGXAAAGBAF?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/Gn1l1RkXoAInb5m?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/Gn1kdTEXoAAlieC?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/Gn1kd1dXIAA8cO2?format=jpg&name=large)

> 2025-04-04
> 
> X 的书签搜索很垃圾，我收藏了很多东西都想用的时候都找不到。经过一晚上的研究和尝试，终于让我找到了解决这个问题的方法，那就是用 NotebookLM 来检索书签。是的，你没听错，谷歌的产品估计不会想到我会用它来当书签搜索器。😂
> 
> 下面我分享一下怎么搞，我一开始的想法就是把书签导出来然后做 RAG
> 
> ![Image](https://pbs.twimg.com/media/Gns0iBHasAAE-pp?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/Gns1QtkakAAKBDR?format=jpg&name=large)