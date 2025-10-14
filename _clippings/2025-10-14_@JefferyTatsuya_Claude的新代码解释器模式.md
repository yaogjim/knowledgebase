---
title: "Claude的新代码解释器模式"
source: "https://x.com/anothergemino/status/1977717395847368978"
author:
  - "[[@JefferyTatsuya]]"
published: 2025-10-14
created: 2025-10-14
description:
tags:
  - "@JefferyTatsuya # 媒体文件处理 # pptx # docx # pdf # xlsx # claude-skills"
---
**Jeffery Kaneda　金田達也** @JefferyTatsuya [2025-10-13](https://x.com/JefferyTatsuya/status/1977713282308792703)

同事使用claude遇到神奇的事情，它居然展开/mnt/skills目录下面查看到一系列制作ppt的skills。

哪位了解这是什么功能？

![Screenshot displays a terminal or command-line interface showing the contents of the /mnt/skills/public/pptx directory with Claude AI context, listing Python files including index.py, openpyxl.py, inventory.py, and replace.py related to PPT skills, along with Chinese text describing the directory and file details.](https://pbs.twimg.com/media/G3I_gRragAAAtAd?format=jpg&name=large)

---

**Geminoo** @anothergemino 2025-10-10

  
供您参考 https://x.com/simonw/status/1976799855701000552…

仓库 https://github.com/simonw/claude-skills/blob/main/mnt/skills…

> 2025-10-10
> 
>   
> 我刚了解到 Claude 的新代码解释器模式里有个/mnt/skills/public/文件夹，装满了用于创建和操作 pdf、docx、pptx 及 xlsx 文件的提示说明和 Python 工具——你可以向 Claude 要一份副本，就能学到大量处理这些格式的技巧