---
title: "2025-11-13_iamnanyi_这几天用Claude_Agent_SDK搭建一个数据处理Agent_感觉像是打开了一个完全不一样的世"
source: "https://x.com/iamnanyi/status/1988614109580181639"
author:
  - "[[@iamnanyi]]"
published: 2025-11-13
created: 2025-11-13
description:
tags:
  - "x"
  - "@iamnanyi"
  - "https"
  - "2025-11-13"
status: "inbox"
importance: 2
effort: 2
review_level: 0
review_next: "2025-12-10"
review_interval: null
review_count: 0
decision: null
topics: []
links_out: []
summary: ""
pov: ""
actions: []
---

# 这几天用Claude Agent SDK搭建一个数据处理Agent，感觉像是打开了一个完全不一样的世

**NanYi** @iamnanyi [2025-11-12](https://x.com/iamnanyi/status/1988614109580181639)

这几天用Claude Agent SDK搭建一个数据处理Agent，感觉像是打开了一个完全不一样的世界，全部流程大约8步，其中6步是完全AI处理，这6步中有一步用的MCP，其他5步用了Skills，没用AI的两步一个是数据库写入，一个是做前台页面配置参数以启动任务。

一个感受就是，将AI的功能植入toC的产品里并没有多大的生产力提升，用AI Chat基本就能解决C端用户绝大部分的需求。但是如果在工作流环节里去耐心且高质量的完成一个Agent，真的可以既快又省的解决很多低效人力问题，甚至做的数据更漂亮，更合理。也许搭建的时候需要不断的调校打磨，但是一旦成功运行，需要一个部门的人力几天甚至几个月完成并需要长期维护的数据库，Agent只需要几分钟，并且24小时定时间隔更新、维护，这个价值是巨大的！

* * *

**xhchen** @xiaohuachen [2025-11-12](https://x.com/xiaohuachen/status/1988755115084541986)

能否不吝赐教，大致的构建过程是怎样的？

* * *

**NanYi** @iamnanyi [2025-11-13](https://x.com/iamnanyi/status/1988758708835512646)

我会先在工作目录里搭建文档系统，将实现目标、工作流程之类写一个大概，然后让Claude Code或者ChatGPT帮我完善和细化。

接着接入Claude Agent SDK，一个节点一个节点的以Subagent方式实现，设定输入/输出，如何验证，输出的内容都会存成文件，将文件目录传递给主线程。

* * *

**winson li** @winson\_dev [2025-11-13](https://x.com/winson_dev/status/1988823381094068502)

agent 的上下文和整合的数据如何持久化？

* * *

**NanYi** @iamnanyi [2025-11-13](https://x.com/iamnanyi/status/1988823879599747224)

主agent将任务下发subagent，subagent独立上下文处理，输出结果到文件，告知主agent任务结束，主agent分配后续任务，后续subagent按需读取文件内容即可。

* * *

**司马元让** @multiplyws [2025-11-13](https://x.com/multiplyws/status/1988811849564070217)

我想请问的是，对于比较机械的数据更新及维护，用程序实现不比交给ai agent更加可靠吗？当然，前者也会是在ai辅助下进行的，但一旦程序开发完成并且稳定运行，就应该时不时爱幻想的ai可靠吧？

* * *

**NanYi** @iamnanyi [2025-11-13](https://x.com/iamnanyi/status/1988813107821793556)

我这边中间步骤包括数据抽取、归一化、关联和打分评审，这些东西程序我觉得不如AI高效，这几个节点以前都是人来完成的，只有采集部分用了MCP，用程序来请求各种数据源API。

* * *

**wyw\_ghastly** @wyw\_ghastly [2025-11-13](https://x.com/wyw_ghastly/status/1988843771870540230)

如果出现了一些意外的错误，Agent能自行处理还是需要人工干预呢？

* * *

**NanYi** @iamnanyi [2025-11-13](https://x.com/iamnanyi/status/1988844099512713551)

我的是定时器，agent任务设定的是出现错误重试3次，如果3次错误就等下一个定时器吧，连续出错可以设定报警，这些和AI就没啥关系了。

* * *

**Justdoit** @DogeJustdoit [2025-11-13](https://x.com/DogeJustdoit/status/1988819065528623611)

Agent 编程， Agent 数据处理， Agent 运维， 三驾超级马车

* * *

**UBsoft** @zhiyebanzhuan [2025-11-13](https://x.com/zhiyebanzhuan/status/1988793683555283215)

好方向