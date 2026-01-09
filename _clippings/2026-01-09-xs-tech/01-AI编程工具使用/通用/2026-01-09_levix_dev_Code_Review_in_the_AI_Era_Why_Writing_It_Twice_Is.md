---
title: "2026-01-09_levix_dev_Code_Review_in_the_AI_Era_Why_Writing_It_Twice_Is"
source: "https://x.com/levix_dev/status/2007657343383646565"
author:
  - "[[@levix_dev]]"
published: 2026-01-09
created: 2026-01-09
description:
tags:
  - "x"
  - "@levix_dev"
  - "description"
  - "type"
---

# Code Review in the AI Era Why Writing It Twice Is

**宝玉** @dotey [2026-01-03](https://x.com/dotey/status/2007514902819467505)

Code Review in the AI Era: Why Writing It Twice Is Actually Faster

If you've been coding for a few years, you've probably lived through this nightmare: you finish the first version, finally get it running, and then realize you misunderstood half the requirements, hit three

人工智能时代的代码审查：为什么写两次实际上更快

如果你已经写了几年代码，你可能经历过这样的噩梦：完成第一个版本，终于让它跑起来了，然后才发现自己误解了一半的需求，还遇到了三个..

> 2026-01-02
> 
> I'm Boris and I created Claude Code. Lots of people have asked how I use Claude Code, so I wanted to show off my setup a bit.
> 
> My setup might be surprisingly vanilla! Claude Code works great out of the box, so I personally don't customize it much. There is no one correct way to
> 
> 我是 Boris，我创建了 Claude Code。很多人问我如何使用 Claude Code，所以我想稍微展示一下我的配置。
> 
> 我的配置可能意外地很基础！Claude Code 开箱即用效果很好，所以我个人不会太多自定义它。没有唯一正确的方法...
> 
> ![Image](https://pbs.twimg.com/media/G9wfSQbWEAAVJkN?format=jpg&name=large)

* * *

**宝玉** @dotey [2026-01-03](https://x.com/dotey/status/2007515334350086153)

AI 时代的代码审核：写两遍，反而更快

做过几年开发的人，大概都有过这种痛苦记忆：第一版代码写完，功能好不容易跑通了，然后发现需求理解错了一半，技术方案踩了三个坑，架构设计根本撑不住后续迭代。

![Image](https://pbs.twimg.com/media/G9wgg-0W4AAfAdu?format=jpg&name=large)

* * *

**Levix** @levix\_dev [2026-01-04](https://x.com/levix_dev/status/2007657343383646565)

在公司内部我实践了 SPEC 那套流程，过程中沉淀了设计文档、布局文档等上下文文档，最终进行了前端出码，某个版本确实正常跑通了，但将过程中沉淀出来的 Agent md 各文档形成一套规范后落入到其他版本，效果就很差。

偶然间我看到了《Effective harnesses for long-running agents》这篇文章并分享到团队内部，团队将任务拆解成更加细粒度的形式（即结构化的形式），把关键业务模块的知识库建立好（采用的是 Skills），过程中还把什么设计文档、布局文档等 Agent 移除了，最终效果还不错，看到了希望。26 年大概率会在内部推崇这一套方案。

以下是我们内部实践的大致结构：

\`\`\`

{

"$id": "task-list.schema.json",

"title": "Task Dependency and Validation Schema",

"description": "定义了任务依赖关系、执行步骤、验证上下文和结果的规范",

"type": "object",

"properties": {

"$schema": {

"type": "string",

"description": "JSON Schema 文件的引用路径"

},

"task": {

"type": "array",

"description": "任务列表，包含所有相关的任务配置",

"items": {

"type": "object",

"properties": {

"id": {

"type": "string",

"default": "task",

"description": "任务的唯一标识符，通常是一个 UUID 或具有唯一性的字符串。"

},

"category": {

"type": "string",

"default": "functional",

"description": "任务的分类，例如 'functional', 'validation', 'generation', 'testing' 等。"

},

"description": {

"type": "string",

"description": "任务的详细描述，说明这个任务的目标和作用。"

},

"steps": {

"type": "array",

"description": "完成任务所需执行的一系列步骤。",

"items": {

"type": "string",

"description": "单个步骤的描述，应为清晰、可执行的指令。"

}

},

"dependence\_context": {

"type": "array",

"description": "依赖文件，例如 skill 中的文件、知识库文件、组件库模板文件等",

"items": {

"type": "object",

"properties": {

"description": {

"type": "string",

"description": "文件描述"

},

"path": {

"type": "array",

"description": "文件引用路径数组",

"items": {

"type": "string",

"description": "文件的引用路径"

}

}

}

},

"required": \["description", "path"\]

},

"ccode": {

"type": "string",

"description": "D2C 设计链接，可选字段"

},

"passes": {

"type": "boolean",

"default": false,

"description": "任务的执行结果状态，true 表示通过，false 表示失败。"

}

},

"required": \["id", "category", "description", "steps", "passes"\]

}

}

},

"required": \["task"\]

}

\`\`\`

https://x.com/levix\_dev/status/1994048920435995119…

我在公司内部实践了 SPEC 那套流程，过程中积累了设计文档、布局文档等上下文文档，最终完成了前端编码，某个版本确实能正常运行。但将过程中沉淀出的 Agent 的各 md 文档整理成一套规范后应用到其他版本，效果就很差。

偶然间我看到了《长期运行代理的有效管理框架》这篇文章，分享到了团队内部。团队把任务拆解成更细粒度的形式（也就是结构化形式），还建立了关键业务模块的知识库（用的是 Skills），过程中还把设计文档、布局文档这类 Agent 相关的东西给移除了。最终效果还不错，看到了希望。2026 年大概率会在内部推广这套方案。

以下是我们内部实践的大致结构：

\`\`\`

{

"$id": "任务列表.schema.json",

"title": "任务依赖和验证模式"

定义了任务依赖关系、执行步骤、验证上下文和结果的规范

"类型": "对象",

"属性": {

$schema": {

"类型": "字符串",

"JSON Schema 文件的引用路径"

},

"任务": {

"类型": "数组",

任务列表，包含所有相关的任务配置

"项目": {

"类型": "对象",

"属性": {

"id": {

"类型": "字符串",

"默认": "任务"

任务的唯一标识符，通常是一个 UUID 或具有唯一性的字符串。

},

"类别": {

"类型": "字符串",

"默认": "功能的"

"description": "任务的分类，例如 'functional'、'validation'、'generation'、'testing' 等。"

},

"描述": {

"类型": "字符串",

任务的详细描述，说明这个任务的目标和作用。

},

"步骤": {

"类型": "数组",

完成任务所需执行的一系列步骤。

"items": {

"类型": "字符串",

单个步骤的描述，应为清晰、可执行的指令。

}

},

"依赖上下文": {

"类型": "数组",

"依赖文件，例如 skill 中的文件、知识库文件、组件库模板文件等"

"项目": {

"类型": "对象"

"属性": {

"描述": {

"类型": "字符串",

"description": "文件描述"

},

"路径": {

"类型": "数组",

"description": "文件引用路径内存",

"项目": {

"type": "字符串",

"description": "文件的引用路径"

}

}

}

},

"必填": \["description", "path"\]

},

"ccode": {

"类型": "字符串",

D2C 设计链接，可选字段

},

"通行证": {

"type": "布尔值",

"默认": false,

"description": "任务的执行结果状态，true 表示通过，false 表示失败。"

}

},

\["ID", "类别", "描述", "步骤", "通过"\]

}

}

},

"required": \["任务"\]

}

\`\`\`

https://x.com/levix\_dev/status/1994048920435995119…