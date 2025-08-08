---
title: "提取中文标题"
source: "https://x.com/ericzakariasson/status/1915072216523497628"
author:
  - "[[@ericzakariasson]]"
created: 2025-04-24
description:
tags:
  - "@ericzakariasson 提取包含 # 的中文标签"
---
**eric zakariasson** @ericzakariasson [2025-04-23](https://x.com/ericzakariasson/status/1915072216523497628)

  
关于如何在大型代码库和单一仓库中使用@cursor\_ai，我收到了很多问题。虽然这取决于具体情况™，但这里有一些提示和技巧

![Image](https://pbs.twimg.com/media/GpO0BaubsAAQnH-?format=jpg&name=large)

---

**eric zakariasson** @ericzakariasson [2025-04-23](https://x.com/ericzakariasson/status/1915072233816687015)

  
启用项目结构，使模型更清楚项目的结构方式

![Image](https://pbs.twimg.com/media/GpO0DDrbcAA_eJv?format=png&name=large)

---

**eric zakariasson** @ericzakariasson [2025-04-23](https://x.com/ericzakariasson/status/1915072249411023135)

  
确保@提及你知道包含与你想要完成的任务相关模式和示例的特定文件或文件夹。这会让模型以你的代码库为基础

![Image](https://pbs.twimg.com/media/GpO0D87bMAACDR2?format=jpg&name=large)

---

**eric zakariasson** @ericzakariasson [2025-04-23](https://x.com/ericzakariasson/status/1915072261750677854)

  
不要试图一次做太多事情。把问题分解成可以逐一完成的小任务。想象一下从产品需求文档到一个个工单，一步一步来。

---

**eric zakariasson** @ericzakariasson [2025-04-23](https://x.com/ericzakariasson/status/1915072273809285199)

  
当手头有新任务时创建新的聊天记录，以保持上下文清晰，避免混淆模型。如果您依赖之前的聊天记录，可以参考@过去的聊天记录

> 2025-02-13
> 
>   
> 单一用途的作曲器
> 
> 这是我为充分利用@cursor\_ai 而采用的模式之一。我经常看到人们使用非常长的编排器，将不相关的更改混在一起，导致模型感到困惑。
> 
> 通过创建新的作曲家（命令+N），你可以从一个干净的状态重新开始

---

**eric zakariasson** @ericzakariasson [2025-04-23](https://x.com/ericzakariasson/status/1915072290066461159)

  
开启询问模式，要求智能体在编写任何代码之前制定一个实施计划。反复迭代，直到你对规格满意为止，然后切换到智能体模式并提示模型进行实施

![Image](https://pbs.twimg.com/media/GpO0GVrakAALctv?format=jpg&name=large)

---

**eric zakariasson** @ericzakariasson [2025-04-23](https://x.com/ericzakariasson/status/1915072302796226739)

  
确保排除文件索引，例如构建工件、缓存等。模式由.gitignore 继承，所以你可能无需触碰它

在即将推出的版本中，当我们推出工作区支持时，这将变得容易得多