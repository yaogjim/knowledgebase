---
title: "Wang Shuyi on X: "Claude Skills 入门：一篇文章搞懂 AI 怎么从「嘴替」升级成「打工人」" / X"
source: "https://x.com/wshuyi/status/2009451186039214388"
author: ""
created: 2026-01-12 09:09:31
date: 2026-01-12 09:09:31
description: ""
tags: ""
---
你有没有这种感觉 ——AI 领域的新名词，比手机型号更新还快？

昨天刚搞懂「函数调用」(Function Calling) 是怎么回事，今天又冒出来个「Skills」。前天有人跟你说「MCP」，你还没反应过来，后天又有人聊「Agent」。每次看到这些词，第一反应都是：我是不是又落伍了？

别慌。今天咱们把「Claude Skills」这事儿掰开揉碎了讲清楚。

更重要的是，我会告诉你它跟你已经知道的那些概念 —— 函数、函数调用 —— 到底是什么关系。你会发现，这不是三个孤立的新词，而是一层一层往上搭的台阶。搞懂这三层，以后再出什么新词，你也能自己判断它在哪一层。

你可以把函数理解成一个「小助手」。你告诉它要做什么（给它一个输入），它帮你做完后告诉你结果（给你一个输出）。就像餐厅里的服务员：你点菜，他端菜，每次都按照固定流程来。

举个例子，程序员写一个叫 \`calculate\_tax (income)\` 的函数。你把收入数字扔进去，它把该交多少税算出来还给你。下次还要算？再调用一遍就行。不用每次都重写一遍算税的逻辑。

把一件事情的做法「打包」起来，以后谁都能用，每次用的方式都一样。这是程序员几十年来最基本的生产力工具。

[

![Image](https://pbs.twimg.com/media/G-L7CmQW0AAkUVK?format=jpg&name=medium)



](https://x.com/wshuyi/article/2009451186039214388/media/2009444405808123904)

程序员在代码里写 \`getWeather()\`，这个函数 100% 会被执行。可是普通人不会写代码，AI 也不会直接「运行」这些代码。那怎么让 AI 也能用上这些「小助手」呢？

2023 年前后，一个叫「函数调用」（Function Calling）的概念火了起来。

你可以把它理解成：给那个「只会聊天的 AI」配了一部电话和一本通讯录。

以前的 AI，你问它「今天北京天气怎么样」，它要么从训练数据里瞎猜一个，要么老老实实说「我不知道」。因为它没有「手脚」，不能真的去查天气。

开发者事先告诉 AI：「这是一本通讯录，里面有个叫 \`get\_weather\` 的函数，你想查天气就打这个电话。」AI 收到「今天北京天气怎么样」的问题后，它会自己判断：「哦，这个问题我得打电话给 \`get\_weather\` 才能回答。」

然后它生成一段标准格式的「便签」（叫 JSON），上面写着：

> { "function": "get\_weather", "arguments": { "city": "北京" } }

这段便签被外部程序接收、解析、执行。真正打电话给气象台的，是外部程序，不是 AI 自己。执行完后，结果返回给 AI，AI 再用人话告诉你：「北京今天晴，15 度。」

传统函数是「确定性」的——程序员在代码里写了 \`getWeather()\`，100% 会执行。

但 LLM 的函数调用是「概率性」的——AI 看到「今天天气怎么样」，它要自己判断该不该调用天气函数。这个判断是基于理解，不是基于规则。有小概率它会判断错误，比如把「天气」理解成某个人名。

所以说，函数调用的本质是：让 AI 能「打电话」，但打不打、打给谁，它自己决定。

这是一个巨大的进步 ——AI 不再只是「知识库」，它开始变成「行动者」。

[

![Image](https://pbs.twimg.com/media/G-L60Z9XYAAy8sV?format=jpg&name=medium)



](https://x.com/wshuyi/article/2009451186039214388/media/2009444161989074944)

你给 AI 配了十几个函数，它每次只能选一个打电话。如果一个任务需要连续调用五六个函数、中间还有逻辑判断、还需要参考一些文档，函数调用就不够用了。

2025 年 10 月 16 日，Anthropic 发布了一个新功能：

。

你可以把 Skills 理解成「员工手册」+「工具箱」的组合。

员工手册告诉 AI：「当你遇到某类任务时，应该怎么做，分几步，每一步用什么工具。」工具箱里装着它需要用的脚本和参考资料。

具体来说，一个 Skill 就是一个文件夹，里面有三样东西：

第一，

文件。这是「指令」，用自然语言写的。告诉 AI：这个 Skill 是干什么的，什么情况下该用，怎么用，有什么注意事项。

第二，脚本。可以是 Python、JavaScript 或者其他语言写的代码。当 AI 需要「动手」的时候，就执行这些脚本。

第三，资源文件。比如参考文档、模板、配置文件。AI 在执行任务的时候可以查阅这些资料。

区别在于：函数调用是「单个工具」，Skills 是「整套解决方案」​。

打个比方。函数调用像是给你一把锤子、一把螺丝刀、一把扳手，你得自己知道什么时候用哪个。Skills 像是给你一本《如何组装宜家书柜》的说明书，说明书里不仅告诉你步骤，还附上了所有需要的工具和零件。

AI 的「工作记忆」是有限的（技术上叫「上下文窗口」）。如果你把所有 Skills 的内容一股脑塞进去，AI 会被信息淹没。

Skills 的做法是：平时只告诉 AI「有这么一本说明书」，AI 真正需要的时候再去翻。就像你不用把整本百科全书背下来，遇到问题再查相关那一页就行。

[

![Image](https://pbs.twimg.com/media/G-L6bveXMAA3vgQ?format=jpg&name=medium)



](https://x.com/wshuyi/article/2009451186039214388/media/2009443738267889664)

[

![Image](https://pbs.twimg.com/media/G-L6QRTW0AAtfzD?format=jpg&name=medium)



](https://x.com/wshuyi/article/2009451186039214388/media/2009443541190103040)

从下往上看，抽象层次越来越高。函数是代码级的，函数调用是接口级的，Skills 是工作流级的。

Skills 可以包含函数调用，但函数调用只是 Skills 的一部分。

就像一本菜谱不只是「切菜」「炒菜」「装盘」这几个动作的罗列，它还包括「为什么要这样做」「火候怎么掌握」「如果烧焦了怎么补救」这些知识。

说了这么多概念，Skills 到底能干什么？咱们看几个真实案例。

[

![Image](https://pbs.twimg.com/media/G-L6FxcWcAAZufc?format=jpg&name=medium)



](https://x.com/wshuyi/article/2009451186039214388/media/2009443360839200768)

如果你用 Markdown 写文章，然后想发布到 X（Twitter）的 Articles 功能里，你会遇到一个极其崩溃的问题：复制粘贴过去，格式全丢了。

标题变普通文字，粗体变普通文字，链接变普通文字。你得手动一个一个加回来。一篇文章，光是调格式就要花 15-20 分钟。

更要命的是图片。你得手动上传每一张，然后把它拖到正确的位置。如果文章有十几张图，你很容易搞错顺序。

它会先解析你的 Markdown 文件，提取标题、封面图，并且给每张内容图片计算一个「块索引」（block\_index）—— 就是这张图应该出现在文章的第几个段落之后。

然后，它把 Markdown 转成富文本 HTML，通过剪贴板粘贴到 X 编辑器里。格式完美保留。

最后，它用浏览器自动化（Playwright）把每张图片精准插入到正确的位置。

原本 20-30 分钟的手动操作，现在几分钟内全自动搞定。减少时长自不必说。对懒人而言，能全程不用自己再动手，才是最主要的嘛。

单纯的自动化脚本，你得自己记住什么时候用、怎么用、参数怎么填。但 Skill 把「什么时候用」「怎么用」都写进了指令里。你只需要跟 AI 说一句「把这篇文章发到 X」，它就知道该调用这个 Skill，该怎么操作。

这就是「知识编码」的价值——把「我知道怎么做」变成「AI 也知道怎么做」。

会议管理：有个 Skill 能自动从会议记录里提取摘要、决策和行动项，然后起草跟进邮件。开完会不用再花半小时整理笔记。

数据分析：扔给它一个 CSV 文件，它能自动识别关键指标、找出异常值，生成图文并茂的报告。非技术人员也能快速从数据里挖出洞察。

客户支持：它从公司知识库里检索准确答案，再用人性化的语言组织成回复。既保证准确，又不失温度。

这些场景有个共同点：都是重复性高、步骤固定、但又需要一定判断力的任务。以前，要么靠人硬扛，要么花大价钱开发专门的软件。现在，一个 Skill 就能搞定。

有个叫 \`skill-creator\` 的 Skill，特别有意思 —— 它是用来创建 Skill 的 Skill。

[

![Image](https://pbs.twimg.com/media/G-L5tI9XMAAALwG?format=jpg&name=medium)



](https://x.com/wshuyi/article/2009451186039214388/media/2009442937654947840)

你跟它聊天，告诉它你想实现什么工作流，它会帮你生成一个完整的 Skill 项目框架。这就是所谓的「元技能」。

还有 \`webapp-testing\`，能根据测试用例自动操作浏览器，对 Web 应用进行功能测试，然后生成测试报告。前端测试流程部分自动化了。

如果你想用现成的 Skills，最简单的方式是通过 Claude Code 的插件市场。

默认初始自动安装的只是 Claude 官方的插件市场。

[

![Image](https://pbs.twimg.com/media/G-L5iWgW8AAiyG6?format=jpg&name=large)



](https://x.com/wshuyi/article/2009451186039214388/media/2009442752312832000)

你也可以根据自己的需求，添加其他插件市场。格式例如：

> /plugin marketplace add anthropics/claude-code

[

![Image](https://pbs.twimg.com/media/G-L5XpNXQAAw35c?format=jpg&name=medium)



](https://x.com/wshuyi/article/2009451186039214388/media/2009442568354873344)

[

![Image](https://pbs.twimg.com/media/G-L5M0jXAAApqJv?format=jpg&name=medium)



](https://x.com/wshuyi/article/2009451186039214388/media/2009442382421360640)

你看到了，利用 \`/plugin\` 命令，可以添加、管理插件。

[

![Image](https://pbs.twimg.com/media/G-L43HPW8AAUt3e?format=jpg&name=medium)



](https://x.com/wshuyi/article/2009451186039214388/media/2009442009480622080)

装完之后，你可以让 Claude 用某个 Skill 来完成任务。比如：「用 PDF Skill 提取这份文件里的表格数据。」

如果你想自己创建 Skills，可以用 \`skill-creator\` 这个元技能。跟它对话，描述你的工作流，它会帮你生成框架。

你可以编写 Claude Skill，让它帮助你去分析材料、自动调研，并且绘制出对应的结构图。

[

![Image](https://pbs.twimg.com/media/G-L4pI3WUAACQ6n?format=jpg&name=medium)



](https://x.com/wshuyi/article/2009451186039214388/media/2009441769398620160)

[

![Image](https://pbs.twimg.com/media/G-L4eR-WwAASYi-?format=jpg&name=medium)



](https://x.com/wshuyi/article/2009451186039214388/media/2009441582865367040)

更高级的玩法是用 Claude Skills 连接一些非常好的外部工具，例如 NotebookLM 作为知识库使用。这样你就可以把 NotebookLM 强大的检索和知识验证功能，与你自己的创意以及其他模型工具的特点有机地结合在一起。

[

![Image](https://pbs.twimg.com/media/G-L3sgkWMAAJGwr?format=jpg&name=medium)



](https://x.com/wshuyi/article/2009451186039214388/media/2009440727789350912)

想看看别人做了什么 Skills？去 GitHub 搜

，那里有社区整理的优秀 Skill 清单。

[

![Image](https://pbs.twimg.com/media/G-L3lr2WEAAyOmu?format=jpg&name=medium)



](https://x.com/wshuyi/article/2009451186039214388/media/2009440610558545920)

我个人比较推荐的是活水智能（也就是阳志平老师团队）做的

。

[

![Image](https://pbs.twimg.com/media/G-L3eOyXQAAMxPT?format=jpg&name=medium)



](https://x.com/wshuyi/article/2009451186039214388/media/2009440482498134016)

这里不仅整理了很多的插件，而且还有相应的评级评分，更可以保证避免踩坑。

[

![Image](https://pbs.twimg.com/media/G-L3Vn0XcAAfUAb?format=jpg&name=medium)



](https://x.com/wshuyi/article/2009451186039214388/media/2009440334598598656)

最重要的一点：创建 Skill 不一定需要会写代码。

里的指令是自然语言写的。如果你的工作流不涉及复杂的脚本，光靠自然语言指令就能完成很多事情。

正如 Claire Vo 在

里说的：即使是非程序员，也可以通过清晰地定义工作流，创建出强大的、可复用的 AI 工作流。

[

![Image](https://pbs.twimg.com/media/G-L3NNRWAAAYaoz?format=jpg&name=medium)



](https://x.com/wshuyi/article/2009451186039214388/media/2009440190033428480)

-   编程函数是基石。它提供了最基础、最可靠的逻辑执行单元。
    
-   LLM 函数调用是桥梁。它让 AI 不再只是「知识库」，而是能「打电话」驱动外部世界的行动者。
    
-   Claude Skills是蓝图。它把零散的工具和指令整合成完整的工作流，让 AI 能更可靠、更专业地完成复杂任务。
    

这三层会越来越融合。开发者继续写高效的函数作为底层工具；通过函数调用把工具暴露给 AI；再用 Skills 指导 AI 怎么智能地使用这些工具。

你不需要是程序员，只需要清楚自己的工作流程是什么，就能把这些知识打包成一个 Skill。你的专业知识不再只存在于你脑子里，它变成了 AI 可以调用的能力。

对了，就在我写这篇文章的时候（2026 年 1 月 8 日），Claude Code 又发布了一次重大更新。Skills 现在支持隔离上下文、热重载、指定模型、在子代理中使用……

也正式上线了。

[

![Image](https://pbs.twimg.com/media/G-L3FyFXUAAmUBV?format=jpg&name=medium)



](https://x.com/wshuyi/article/2009451186039214388/media/2009440062476341248)

Anthropic 还把 Agent Skills 规范作为

发布 —— 这跟他们之前推 MCP（Model Context Protocol）的路数一样，都是走开放生态路线。

Gartner 的分析师说，这标志着 AI 市场的焦点正在从「模型更新」转向「用例落地」。

翻译成人话就是：大家不再只比谁的模型更聪明，而是开始比谁能把 AI 用得更好。

Skills 是这场转变的核心载体。它让 AI 从「应答者」变成了「协作者」。

下次再有人跟你说什么关于 Agent 功能的新词，你就问自己：它是在哪一层？是代码级的工具，是接口级的桥梁，还是工作流级的蓝图？

你有没有尝试过 Claude Skills？有没有自己制作符合你自己工作流的 Claude Skill？