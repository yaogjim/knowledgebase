---
title: "2025-11-19_vista8_一直觉得Claude_Skill这个概念难懂_也不知道怎么开始_经过昨天研究_发现我想复杂了_上手"
source: "https://x.com/vista8/status/1990668495496098194"
author:
  - "[[@vista8]]"
published: 2025-11-19
created: 2025-11-19
description:
tags:
  - "x"
  - "@vista8"
  - "https"
  - "2025-11-18"
---

# 一直觉得Claude Skill这个概念难懂，也不知道怎么开始 经过昨天研究，发现我想复杂了。 上手

**向阳乔木** @vista8 [2025-11-18](https://x.com/vista8/status/1990668495496098194)

一直觉得Claude Skill这个概念难懂，也不知道怎么开始

经过昨天研究，发现我想复杂了。

上手其实很简单，如果你有Claude Code，无论官方还是中转。（ 比如我用的兔子API @tuzi\_ai 的中转）

一共三步：

1\. 运行Claude Code，输入/plugin , 选择add marketplace，输入下面网址回车

https://github.com/anthropics/skills…

1\. 运行 Claude Code，输入/plugin，选择添加市场，输入以下网址后按回车

https://github.com/anthropics/skills…

2\. 这时会看到两个安装选项，一个是document-skill，一个是example-skill，都装上。

第一个用于处理pdf、word等文档，第二个是样例，未来也能调用。

3\. 跟 Claude 对话说：“一步步引导我写第一个Claude skill”

Claude会抱怨需求不清楚，让你回答问题，明确需求。

我回答：我想要一个写作Skill，能联网，会用我的提示词，并且安装一个seedream MCP用于生成配图插入文章。

Claude会追问细节，给你一些选择题，都答完，需求明确后。

它会创建一系列文件夹和文件。

第一个写作Skill就做好了！

![Image](https://pbs.twimg.com/media/G6BD1U-boAAHlAP?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G6BEPTMbYAASSPD?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G6BFMoibMAEUSNJ?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G6BFmjWbUAAzmIr?format=jpg&name=large)

* * *

**兔妹\_兔子** @tuzi\_ai [2025-11-18](https://x.com/tuzi_ai/status/1990693734678475185)

Anthropic 已经开源了一些官方示例和模板👇

https://github.com/anthropics/skills…

包括：

✓ 真实可用的文档处理技能

✓ 品牌指南技能

✓ 设计与图像生成技能

✓ web 测试、MCP、 artifacts builder 等开发技能

✓ 还有可直接复制的模板（template-skill）

* * *

**AlexZ** @blackanger [2025-11-18](https://x.com/blackanger/status/1990818249165209832)

更方便的方式是，直接把 官方 skill 链接扔给它，把你的需求告诉它，它自己就写好 skill 了，然后它会告诉你怎么用

* * *

**elon lee** @elonlee123 [2025-11-18](https://x.com/elonlee123/status/1990696352649818463)

可以参考这个项目https://github.com/iptag/jimeng-api…，直接调用他的skill更方便，

* * *

**化骨绵掌** @likefeiwu [2025-11-18](https://x.com/likefeiwu/status/1990669325444001829)

skill 的问题是，这个里面的提示词不会像agent一样逐步加载，都是启动了，就一次加载，一次执行

* * *

**噪点noisepoint** @noisepoint\_agi [2025-11-18](https://x.com/noisepoint_agi/status/1990677087145894397)

是的，创建skill不怎么复杂，让claude一步步引导就好了，因为官方插件内置了一个创建skill的skill

* * *

**Ernestine Demars** @DemarsErnestine [2025-11-18](https://x.com/DemarsErnestine/status/1990721361984057659)

主要是搞不明白skill和subagent的区别，看上去skill好像是给subagent用的，但主agent直接用skill也能有很好的效果。

* * *

**Browny** @brownylin [2025-11-18](https://x.com/brownylin/status/1990898374757752864)

前陣子用了一下，覺得 Skill 是從協定走向了心法