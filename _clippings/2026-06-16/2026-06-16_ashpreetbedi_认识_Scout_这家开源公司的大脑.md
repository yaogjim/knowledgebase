---
title: "2026-06-16_ashpreetbedi_认识_Scout_这家开源公司的大脑"
source: "https://x.com/ashpreetbedi/status/2049180168200106150"
author:
  - "[[@ashpreetbedi]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "#company"
  - "#ai"
  - "x"
  - "@ashpreetbedi"
---

# 认识 Scout。这家开源公司的大脑

**Ashpreet Bedi**

# 认识 Scout。这家开源公司的大脑

YC's Summer 2026

[Requests for Startups](https://www.ycombinator.com/rfs) named two ideas that point at the same thing from different angles.

[Company Brain](https://www.ycombinator.com/rfs#company-brain): pull knowledge out of fragmented sources (Slack, email, tickets), structure it, keep it current, turn it into something AI can act on.

> "Structure it, keep it current" is the wrong approach. The trick is "navigation over search". More on this later.

> 公司大脑 @t\_blom 每家公司都有关键专业知识分散在人们的脑海中、旧的 Slack 对话线程、支持工单和数据库中，而 AI 代理无法像这样运作。 我们认为世界上的每一家公司都将需要一个新的基础要素：一个关于“如何”的活地图
> 
> — Y Combinator
> 
> [https://x.com/ycombinator/status/2048834293779378437](https://x.com/ycombinator/status/2048834293779378437)
> 
> ![方形资料图片](https://pbs.twimg.com/profile_images/1623777064821358592/9CApQWXe_normal.png)![图片](https://pbs.twimg.com/amplify_video_thumb/2048809119650623488/img/XWVz4iIiK6kT0dwk.jpg)![Download](chrome-extension://jfphcjkiccfhcmggdncpidahnkfpngfa/blueicon.jpg)

[AI Operating System for Companies](https://www.ycombinator.com/rfs#ai-operating-system-for-companies): the connective layer that makes a company legible to AI by default. Closed-loop systems that watch what happens after a decision and adjust.

> 面向企业的人工智能操作系统 @sdianahu 最优秀的原生 AI 公司让整个公司都可被查询：每个会议、工单和客户互动都对一个从中学习的智能层是可理解的。 今天构建这个需要艰苦的集成工作
> 
> — Y Combinator
> 
> [https://x.com/ycombinator/status/2048834315539435657](https://x.com/ycombinator/status/2048834315539435657)
> 
> ![方形资料图片](https://pbs.twimg.com/profile_images/1623777064821358592/9CApQWXe_normal.png)![图片](https://pbs.twimg.com/amplify_video_thumb/2048812811921616896/img/EfRVxxY9YXw9VWPF.jpg)![Download](chrome-extension://jfphcjkiccfhcmggdncpidahnkfpngfa/blueicon.jpg)

The brain is the data layer. The OS is what runs on top of it. Neither exists as a finished product today but the pieces are there (model capability, context providers, agentic SQL, MCP, persistent memory, scheduled execution).

Let's see if we can stitch them into something useful. We'll build the company brain together, and see if we can turn it into the AI operating system.

# Meet Scout

[Scout is a open-source context agent](https://github.com/agno-agi/scout). It navigates live information sources to assemble context on demand. It connects the fragmented knowledge living in slack, google drive, linear using proven patterns like "navigation over search", "context providers", and "learning machines".

Scout also builds its own wiki and CRM as it learns about your company. So you can share that "Josh from Anthropic shared this new paper on RLMs" and it'll add a note in the CRM, parse the paper and store it in the company wiki.

You can also share that "a decision on v3 schema migration" is pending and it'll log a follow up in the CRM, ready to surface next time anyone asks what's open. Put follow-up review on a daily cron and the loop gets tighter.

让我们讨论一些设计决策，这些决策使得 Scout 比那种把所有东西都扔进向量数据库然后祈祷能找到正确数据块的做法更好。

# 上下文提供者

构建“公司大脑”时遇到的第一个问题，是一个智能体连接所有工具并跨信息源工作的能力。目前尚未解决的三个问题是：

1.  来自太多工具的上下文污染
2.  范围重叠导致的性能下降
3.  主代理停止工作，因为其上下文全是工具怪癖

我发现可行的解决方案是 agent 和工具之间的一个薄层，称为 Context Providers。每个信息源（Slack、Drive、CRM）都成为一个 context provider，并向主 agent 暴露两个工具：

- 查询\_<source> 用于自然语言读取
- 更新\_<source> 用于自然语言写作

这种方法的第一个优点是主代理看不到 Slack 的十二个工具，它只看到 query\_slack。

第二个优势，即“大赢”（BIG WIN），在于 query\_slack 工具背后是一个子代理，该子代理掌握了 Slack 的所有特殊处理方式（如在直接发送消息（DM）给用户前先查询用户信息、通过游标进行分页、优先使用 conversations.replies 处理线程）。这一点极为重要，因为现在主代理的上下文不会被如何使用 Slack 的指令或所有中间工具调用结果所污染。

不，技能无法解决这个问题。技能是特定任务的指令（例如“如何使用 Slack”），模型会按需加载这些指令。技能将任务知识从始终存在的提示中移出，转移到更具条件性的内容中。但是当模块被加载时，Slack 工具仍然会作用于主代理，中间工具调用的结果仍然保留在主上下文中。加载两个具备搜索能力的技能，你的代理会立即崩溃。

Scout 的工具界面今日：

- Web: query\_web
- Slack: query\_slack, update\_slack
- Google Drive: query\_gdrive
- CRM: query\_crm, update\_crm (writes to contacts / projects / notes / follow-ups)
- Knowledge wiki: query\_knowledge, update\_knowledge
- Voice wiki: query\_voice (read-only)
- MCP servers: query\_mcp\_<server> (one per registered server)
- Workspace: query\_workspace
- Cross-cutting: list\_contexts

The payoff:

1.  你实际上可以同时使用多个上下文提供者。query\_slack 找到讨论，query\_gdrive 找到文档。
2.  路由是最基本的，这意味着 Scout 的指令保持不变，并且添加更多工具不会导致回归问题。

你可以在这里阅读关于 Context Providers 的更深入文章：

> 上下文提供者：代理与工具之间缺失的层如果你构建了一个拥有相当数量工具的智能体，你就会撞上三道壁垒： 过多工具导致的上下文污染 重叠作用域导致的性能下降 主代理忘记了它的职责...
> 
> — Ashpreet Bedi
> 
> [https://x.com/ashpreetbedi/status/2048817143974613089](https://x.com/ashpreetbedi/status/2048817143974613089)
> 
> ![图片](https://pbs.twimg.com/profile_images/2024047696827273217/vlW-RvPT_normal.jpg)![图片](https://pbs.twimg.com/profile_images/1984361332624306176/KaNuKvU4_bigger.jpg)![文章封面图片](https://pbs.twimg.com/media/HG7UDLrbMAAJ3Wt?format=png&name=large)![Download](chrome-extension://jfphcjkiccfhcmggdncpidahnkfpngfa/blueicon.jpg)

# 搜索导航

构建“公司大脑”时的默认做法是将所有数据导入向量数据库，进行分块、嵌入处理，然后检索 top-k 结果。

这根本没用。索引总是过时的。这些块落在错误的边界上。引用指向的片段在上周二时是正确的。一半的时候，相关内容其实在那个从未被索引的 Slack 线程里——毕竟哪个神智正常的人会去索引 Slack 呢！

编码代理发现的关键是：不要搜索，要导航。他们用 \`ls\` 列出目录内容，用 \`grep\` 搜索函数名，打开文件，跟踪导入，遍历文件系统，就像人类一样。

这种模式非常适用于上下文代理。每个信息源已经具备了相当于 ls、grep 和 cat 的功能。这些功能通过上下文提供者暴露出来。

The payoff:

1.  实时状态。您三十秒前发送的 Slack 消息可供座席使用。昨天的路线图文档是最新的，因为它是实际文档。
2.  真实引用。每个引用都是一个你可以打开的路径。没有来自嵌入边界的片段。
3.  Permissions stay where they live. Drive enforces who can read what, Slack enforces channel membership. Scout sees what its credentials see.

The trade off is more LLM calls per query. A vector lookup is one round trip; navigation is three or four.

# The wiki, crm, and the closed loop

Some things don't have a natural source home. "Josh from Anthropic shared an RLM paper last week" doesn't live anywhere obvious. It was probably mentioned in Slack, but you don't search Slack for "who is Josh".

That's what the CRM and the knowledge wiki are for. Scout populates these as it learns. Josh becomes a contact in the CRM. The RLM paper becomes a wiki page linked from his contact note.

The CRM ships with four tables: scout\_contacts, scout\_projects, scout\_notes, scout\_followups. Beyond those, the write sub-agent creates new scout\_\* tables on demand. "Track my coffee orders" becomes a scout\_coffee\_orders table with the right columns. Schema on demand.

> If you think LLMs are good at bash, wait till you see them write SQL.

# Scout in action

[Scout is open-source.](https://github.com/agno-agi/scout) Fork it, customize it, make it your own.

[Repo](https://github.com/agno-agi/scout)

.

## Quickstart

Clone the repo, add your API key and run scout locally using docker.

```text
git clone https://github.com/agno-agi/scout && cd scout

cp example.env .env # set OPENAI_API_KEY

docker compose up -d --build
```

By default, scout comes with the web, CRM, knowledge wiki, voice wiki, and workspace context providers. Slack and Google Drive providers are wired up, you just need to set up the credentials.

## AgentOS

Scout runs on Agno's

[AgentOS](https://docs.agno.com/). You get a UI, multi-user sessions, scheduled tasks, and a FastAPI app that deploys anywhere Docker runs. Once you have Scout running locally, connect it to the AgentOS UI at

[os.agno.com](https://os.agno.com/)

.

[![视频](https://pbs.twimg.com/amplify_video_thumb/2049176163088580608/img/QnFTsQUSqIQwIxZ4.jpg)](https://x.com/ashpreetbedi/status/2049180168200106150)[![视频](https://pbs.twimg.com/amplify_video_thumb/2049176163088580608/img/QnFTsQUSqIQwIxZ4.jpg)](https://x.com/ashpreetbedi/status/2049180168200106150)

## Slack

Scout is part of your team, and integrating Slack is a ~5 minute setup. Each Slack thread becomes its own session, follow-ups carry the full history.

See the

[SLACK\_CONNECT.md](https://github.com/agno-agi/scout/blob/main/docs/SLACK_CONNECT.md) file for the setup guide.

[![视频](https://pbs.twimg.com/amplify_video_thumb/2049176272744411137/img/Nxs4V49UYOp3dtWX.jpg)](https://x.com/ashpreetbedi/status/2049180168200106150)[![视频](https://pbs.twimg.com/amplify_video_thumb/2049176272744411137/img/Nxs4V49UYOp3dtWX.jpg)](https://x.com/ashpreetbedi/status/2049180168200106150)

Some prompts to test with:

- "Which contexts are you connected to?"
- "Walk me through your codebase"
- "Save a note: Josh from Anthropic shared a new RLM paper this week"
- "The v3 schema migration decision is pending, surface it next Tuesday"
- "Create a runbook for incident response — page on-call first, post status in
 
 [#incidents](https://x.com/search?q=%23incidents&src=hashtag_click), capture timeline as you go"
 
- "Start tracking my coffee consumption. First one: flat white, extra shot"

# What's next

The roadmap from here:

- Scheduled tasks. Surface pending follow-ups automatically.
- Proactive actions per source. Run update\_slack, update\_github daily.
- GitHub, Gmail, Calendar providers. Testing on a side branch.

* * *

链接：

- [侦察兵](https://github.com/agno-agi/scout)
 
- [Agno 文档](https://docs.agno.com/)
 
- [Agno GitHub](https://github.com/agno-agi/agno)
 

* * *

### 热门回复

**@4月27日** ♥ 1.4K · 💬 137

公司大脑

@t\_blom

每家公司都有关键专业知识分散在人们的脑海中、旧的 Slack 对话线程、支持工单和数据库中，而 AI 代理无法像这样运作。

我们认为世界上的每一家公司都将需要一个新的基础要素：一个关于“如何”的活地图

**@4月27日** ♥ 354 · 💬 39

面向企业的人工智能操作系统

@sdianahu

最优秀的原生 AI 公司让整个公司都可被查询：每个会议、工单和客户互动都对一个从中学习的智能层是可理解的。

今天构建这个需要艰苦的集成工作