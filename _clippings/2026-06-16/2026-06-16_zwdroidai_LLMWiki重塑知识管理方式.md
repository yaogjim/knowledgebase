---
title: "2026-06-16_unknown_LLMWiki重塑知识管理方式"
source: "omnisun://digest/1775700564895"
author:
  - "[[@zwdroidai]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "#5660"
  - "@zwdroidai"
  - "wiki"
  - "pages"
---

# LLMWiki重塑知识管理方式

# 宝玉: 因为太多人写过 Andrej Karpathy 的 LLM Wiki，我就没写，其实在我心中比 Auto Research 更有创意，Auto Research…

https://x.com/dotey/status/2041509264221483449

**宝玉**

因为太多人写过 Andrej Karpathy 的 LLM Wiki，我就没写，其实在我心中比 Auto Research 更有创意，Auto Research 本身不新鲜，早就有相关理论，但 LLM WIKI 倒是让我眼前一亮。

我们每个人或多或少都在做信息收集的工作，比如 X 上看到好的文章点赞或者收藏，看到一篇好的技术文章添加到浏览器收藏夹，微信上有人分享了篇好文章点收藏，还有更多的是惊鸿一瞥再也找不到然后想起来根据关键词去 Google ……

其实绝大部分收藏后再也不会打开，一方面是因为收藏即看过的心理暗示，一方面是因为散落各地找起来太麻烦。

所以第一个问题其实是中心化的信息收集整理，把散落在各处的信息汇聚在一处。

已经有很多工具了，我自己也有写小工具/agent 帮助收集信息，因为我除了收集外还有一些二次加工的需要，比如翻译、总结。

但还存在问题就是信息是点状的，最多人工打个tag、加个分类。

但 Karpathy 的更进一步，让 LLM 帮你把信息整理成结构化的。这一步是我之前没考虑过的，也没见过有其他产品做的。

这里面的差别在于以前整理是要人做的，你自己建分类，自己打 tag，对于勤劳的爱整理的人当然没问题，但对于我这种懒人来说是不会做的，所以找信息是比较麻烦的。

但如果这种事情让 Agent 做，那就省事多了，毕竟它不知疲倦，而且极擅长处理内容。

只要稍加调教，它就能帮你把信息整理得井井有条，编程成你自己喜欢的格式，就像你的秘书一样，你只要去看看 WIKI 就可以方便的找到需要的信息，不需要以前那样去各个地方用关键字找。

这里面最核心是思路的转变，信息的收集和整理，不再是人主动的行为，而是 AI Agent 在帮你做这些事情，你所要做的就是每天去看属于自己的 WIKI。

> **@zwdroidai**
> 
> 老师怎么看 llm wiki。说下浅见，如 karpathy 说是个 idea，并没有如 autoreaerch 一样有工程示例。对于 raw 的摘要和索引这个不新鲜，之前很多这样做的，只是把这一部分当做查询 raw 的桥梁。现在升级为 wiki 之后， query 时不查 raw 而直接查 wiki，但从 raw 到 wiki 的压缩并没看到技术实现的进步

* * *

### 热门回复

**@宝玉** ♥ 98 · 💬 1

Skill 可以参考这个版本：

**@宝玉** ♥ 66 · 💬 1

AK 分享了提示词：

https://

gist.github.com/karpathy/442a6

bf555914893e9891c11519de94f

…

**@Orange Standard** ♥ 17 · 💬 0

Real Bitcoin holders don't sell.

They use it.

BTC-backed liquidity for long-term holders. Bitcoin-only. US-based.

**@Teknium (e/λ)** ♥ 11 · 💬 1

It is built in skill in Hermes Agent now if interested too!

现在 Hermes Agent 中内置了这项技能，如果你也感兴趣的话！

**@耳朵** ♥ 7 · 💬 1

我也是因为不喜欢手动维护 所以知识库的双链是废弃状态，看了 AK 这个东西直接把帖子给 AI 让他给我改造整个知识库了，目前看起来还挺满意。

主要是解决了 收藏不看的问题，现在我可以把收藏的内容发给AI，AI 会读取我的 skill

* * *

# llm-wiki

https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

llm-wiki

## LLM Wiki

一种使用 LLMs 构建个人知识库的模式

这是一个想法文件，旨在被复制粘贴到你自己的 LLM Agent（例如 OpenAI Codex、Claude Code、OpenCode / Pi 等）。其目标是传达高层次的想法，但你的 Agent 将与你协作构建具体细节。

大多数人使用 LLMs 和文档的体验都类似于检索增强生成（RAG）：上传一组文件，LLM 在查询时检索相关片段并生成回答。这虽然可行，但 LLM 在每个问题上都要从头重新发现知识，没有知识积累。如果提出一个需要整合五份文档的微妙问题，LLM 每次都必须找到并拼凑相关片段，没有任何内容被积累起来。NotebookLM、ChatGPT 的文件上传功能以及大多数检索增强生成系统都是这样工作的。

这里的思路有所不同。与仅在查询时从原始文档中检索信息不同，LLM **逐步构建并维护一个持久的维基知识库** ——这是一个结构化、相互关联的 Markdown 文件集合，位于你和原始源文件之间。当你添加新的源文件时，LLM 不仅仅是为后续检索建立索引。它会读取该文件，提取关键信息，并将其整合到现有的维基知识库中——更新实体页面、修订主题摘要、记录新数据与旧说法的矛盾之处、强化或挑战不断发展的综合内容。知识被一次性编译，然后 *保持最新* ，而不是在每次查询时重新推导。

这是关键区别： **维基是一个持久且不断积累的成果。** 交叉引用已经存在。矛盾已被标记。综合内容已经反映了你所阅读的一切。每添加一个来源和每提出一个问题，维基都会变得更加丰富。

你从不（或很少）自己编写维基 — LLM 编写并维护所有内容。你负责信息搜集、探索以及提出正确的问题。LLM 承担所有基础工作 — 总结、交叉引用、归档和记录，这些工作能让知识库随着时间推移真正发挥作用。实际上，我一边打开 LLM 代理，另一边打开 Obsidian。LLM 根据我们的对话进行编辑，我实时浏览结果 — 跟随链接、查看图谱视图、阅读更新后的页面。Obsidian 是 IDE；LLM 是程序员；维基是代码库。

这适用于很多不同的场景。举几个例子：

- **个人** ：跟踪自己的目标、健康、心理和自我提升——记录日记条目、文章、播客笔记，并随着时间的推移构建起对自己的结构化认知。
- **研究** ：深入研究一个主题，持续数周或数月——阅读论文、文章和报告，并逐步构建一个内容全面的维基百科，同时论文观点不断演进。
- **阅读书籍** ：归档每一章内容，为角色、主题、情节线索以及它们之间的关联构建页面。最终你会拥有一个丰富的配套维基。想想像 [托尔金之门](https://tolkiengateway.net/wiki/Main_Page) 这样的粉丝维基——数千个相互关联的页面，涵盖角色、地点、事件、语言，由志愿者社区多年来共同构建。你可以在阅读时亲自构建类似的东西，让 LLM 完成所有的交叉引用和维护工作。
- **业务/团队** ：由 LLMs 维护的内部维基，由 Slack 线程、会议记录、项目文档、客户通话提供内容。可能有人工参与审核更新。该维基保持最新是因为 LLM 承担了团队中无人愿意做的维护工作。
- **竞争分析、尽职调查、旅行规划、课程笔记、爱好深度探索** ——任何你需要随着时间积累知识，并且希望将这些知识整理好而非零散存放的事情。

## Architecture

There are three layers:

**原始来源** — 您精心整理的源文档集合。文章、论文、图像、数据文件。这些是不可变的 — LLM 从这些源读取数据但从不修改它们。这是您的事实依据。

**The wiki** — LLM 生成的 Markdown 文件的目录。摘要、实体页面、概念页面、对比、概述、综合。LLM 完全拥有这一层。它创建页面，当有新来源出现时更新页面，维护交叉引用，并保持所有内容的一致性。你阅读它；LLM 撰写它。

**架构** — 一个文档（例如，Claude Code 对应的文件为 CLAUDE.md，Codex 对应的文件为 AGENTS.md），它告诉大语言模型（LLM）维基的结构是怎样的、有哪些约定，以及在摄取资料、回答问题或维护维基时应遵循的工作流程。这是关键的配置文件——它使 LLM 成为一个有纪律的维基维护者，而不是一个通用的聊天机器人。随着你逐步明确什么适合你的领域，你和 LLM 会随着时间共同演进这个架构。

## Operations

**导入** 。你将新的源文件导入原始集合，并指示 LLM 进行处理。一个示例流程如下：LLM 读取源文件，与你讨论关键要点，在 wiki 中撰写摘要页面，更新索引，更新 wiki 中相关的实体和概念页面，并在日志中添加一条记录。单个源文件可能涉及 10-15 个 wiki 页面。就我个人而言，我更喜欢逐个导入源文件并保持参与——我会阅读摘要，检查更新，并指导 LLM 关注重点。但你也可以一次性批量导入多个源文件，只需较少的监督。由你决定制定符合你风格的工作流程，并将其记录在模式中，以便未来的会话使用。

**查询.** 你针对维基提问。LLM 搜索相关页面，阅读这些页面，并综合出带有引用的答案。答案可以根据问题以不同形式呈现——一个 Markdown 页面、一个对比表格、一个幻灯片（Marp）、一个图表（matplotlib）、一个画布。重要的见解是： **好的答案可以作为新页面重新归档到维基中。** 你要求的对比、一次分析、你发现的关联——这些都很有价值，不应消失在聊天记录中。这样，你的探索会像被纳入的资料一样，在知识库中不断累积。

**Lint.** 定期地，让 LLM 对维基进行健康检查。需要检查的内容包括：页面之间的矛盾、被新来源取代的过时说法、没有入站链接的孤立页面、被提及但缺乏自身页面的重要概念、缺失的交叉引用，以及可通过网络搜索填补的数据空白。LLM 擅长提出需要调查的新问题和需要查找的新来源。这有助于维基在发展过程中保持健康。

两个特殊文件帮助 LLM（以及你）在维基随着规模增长时进行导航。它们有不同的用途：

**index.md** 以内容为导向。它是维基百科（wiki）中所有内容的目录——每个页面都列出了一个链接、一行摘要，以及可选的元数据（如日期或来源数量）。按类别组织（实体、概念、来源等）。LLM 会在每次数据摄取时更新该目录。在回答查询时，LLM 会首先读取该索引以找到相关页面，然后深入查看这些页面。这种方法在中等规模（约 100 个来源、约数百个页面）下效果出奇地好，并且避免了对基于嵌入的 RAG 基础设施的需求。

**log.md** 是按时间顺序排列的。它是一个仅追加的记录，记录了发生的事情和时间——数据导入、查询、代码检查通过。一个有用的提示：如果每条记录以一致的前缀开头（例如 `## [2026-04-02] ingest | Article Title` ），则日志可以用简单的 Unix 工具解析—— `grep "^## \[" log.md | tail -5` 可以获取最后 5 条记录。该日志为你提供维基的发展时间线，并帮助 LLM 了解最近完成的工作。

有时你可能想要构建一些小工具，帮助 LLM 更高效地在 wiki 上运行。维基页面的搜索引擎是最明显的一个——小规模时索引文件就足够了，但随着 wiki 的增长，你需要完善的搜索功能。 [qmd](https://github.com/tobi/qmd) 是个不错的选择：它是一个针对 markdown 文件的本地搜索引擎，采用混合 BM25/向量搜索和 LLM 重排序，所有功能都在设备端运行。它同时提供 CLI（这样 LLM 可以调用它）和 MCP 服务器（这样 LLM 可以将其用作原生工具）。你也可以自己构建更简单的工具——当有需要时，LLM 可以帮你即兴编码一个简单的搜索脚本。

- **Obsidian Web Clipper** 是一个将网页文章转换为 Markdown 的浏览器扩展。对于快速将来源内容纳入你的原始集合非常有用。
- **本地下载图片** 。在 Obsidian 设置 → 文件和链接 中，将“Attachment folder path”设置为固定目录（例如 `raw/assets/` ）。然后在设置 → 快捷键 中，搜索“Download”找到“Download attachments for current file”并将其绑定到一个快捷键（例如 Ctrl+Shift+D）。截取文章后，按下该快捷键，所有图片都会被下载到本地磁盘。这是可选的但很有用——它可以让 LLM 直接查看和引用图片，而不是依赖可能失效的 URL。请注意，LLM 无法一次性原生读取带有内联图片的 Markdown——变通方法是让 LLM 先读取文本，然后单独查看部分或全部引用的图片以获取更多上下文。这有点麻烦，但效果还不错。
- **Obsidian 的图谱视图** 是查看你的知识库结构的最佳方式——哪些内容相互关联，哪些页面是中心节点，哪些是孤立页面。
- **Marp** 是一种基于 Markdown 的幻灯片格式。Obsidian 有一个针对它的插件。可直接从维基内容生成演示文稿，非常有用。
- **Dataview** 是一款 Obsidian 插件，可对页面前置元数据执行查询。如果您的 LLM 向 Wiki 页面添加 YAML 前置元数据（标签、日期、来源计数），Dataview 可以生成动态表格和列表。
- 这个维基其实就是一个存放 Markdown 文件的 Git 仓库。你可以免费获得版本历史、分支和协作功能。

维护知识库的繁琐部分不在于阅读或思考——而在于记账。更新交叉引用、保持摘要最新、记录新数据何时与旧说法矛盾、确保数十页内容的一致性。人们放弃维基是因为维护负担的增长速度超过了其价值。LLMs 不会感到厌烦，不会忘记更新交叉引用，并且可以一次性处理 15 个文件。维基能够保持维护状态，因为维护成本几乎为零。

人类的工作是筛选并整理资料、指导分析、提出好问题，并思考这一切的意义。LLM 的工作是其他所有事情。

这个想法在精神上与万尼瓦尔·布什（Vannevar Bush）的 Memex（1945 年）相关——这是一个个人化的、经过精心整理的知识存储系统，其中文档之间存在关联路径。布什的愿景比网络后来的样子更接近这一理念：私密的、经过积极整理的，文档之间的关联与文档本身同样有价值。他未能解决的问题是谁来进行维护。而 LLM 负责了这一点。

## Note

本文刻意保持抽象性。它描述的是理念而非具体实现。确切的目录结构、模式规范、页面格式、工具链——所有这些都取决于您的领域、偏好以及所选择的 LLM。上述所有内容均为可选且模块化——选择有用的部分，忽略无用的部分。例如：您的源数据可能仅为纯文本，因此完全不需要图像处理。您的 Wiki 可能规模较小，只需索引文件即可，无需搜索引擎。您可能不关心幻灯片，只想要 Markdown 页面。您可能需要完全不同的输出格式集。使用本文档的正确方式是将其与您的 LLM 代理共享，并共同协作实例化一个符合您需求的版本。本文档的唯一作用是传达模式，其余部分由您的 LLM 自行处理。

* * *

# hermes-agent/skills/research/llm-wiki/SKILL.md at main · NousResearch/hermes-agent

https://github.com/NousResearch/hermes-agent/blob/main/skills/research/llm-wiki/SKILL.md

[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/) [Open in codespace](/codespaces/new/NousResearch/hermes-agent/tree/main?resume=1)

[docs(llm-wiki): add Obsidian Headless setup for servers (](/NousResearch/hermes-agent/commit/539629923c05e98fee06258a3341af94f2dcccba)[#5660](https://github.com/NousResearch/hermes-agent/pull/5660)[)](/NousResearch/hermes-agent/commit/539629923c05e98fee06258a3341af94f2dcccba)

[5396299](/NousResearch/hermes-agent/commit/539629923c05e98fee06258a3341af94f2dcccba) ·

<table><tbody><tr><th>name</th><td>llm-wiki</td></tr><tr><th>description</th><td>Karpathy 的 LLM Wiki — 构建和维护一个持久的、互联的 Markdown 知识库。摄取源数据，查询编译后的知识，并检查一致性。</td></tr><tr><th>version</th><td>2.0.0</td></tr><tr><th>author</th><td>Hermes Agent</td></tr><tr><th>license</th><td>MIT</td></tr><tr><th>metadata</th><td><table><thead><tr><th>hermes</th></tr></thead><tbody><tr><td></td></tr></tbody></table></td></tr></tbody></table>

构建并维护一个持久的、不断积累的知识库，这些知识库以相互关联的 Markdown 文件形式存在。基于 [Andrej Karpathy 的 LLM Wiki 模式](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) 。

与传统的 RAG（每次查询都从头重新发现知识）不同，维基知识库一次性整合知识并保持其时效性。交叉引用已经存在。矛盾信息已经被标记。综合内容反映了所有已整合的内容。

**分工：** 人类管理信息源并指导分析。代理进行总结、交叉引用、归档并保持一致性。

Use this skill when the user:

- 要求创建、构建或启动维基或知识库
- 请求将一个来源导入、添加或处理到他们的维基中
- 提出一个问题，并且在已配置的路径上存在一个现有的维基
- 要求对他们的 wiki 进行校验、审计或健康检查
- 在研究背景下引用其维基、知识库或“笔记”

## Wiki Location

通过 `skills.config.wiki.path` 在 `~/.hermes/config.yaml` 中配置（在 `hermes config migrate` 或 `hermes setup` 过程中提示）：

```
skills:
  config:
 wiki:
 path: ~/wiki
```

回退到 `~/wiki` 默认值。解析后的路径在该技能加载时被注入 — 检查上方的 `[Skill config: ...]` 区块以获取有效配置值。

这个维基只是一个 Markdown 文件的目录 — 在 Obsidian、VS Code 或任何编辑器中打开它即可。不需要数据库，也不需要特殊工具。

```
wiki/
├── SCHEMA.md # Conventions, structure rules, domain config
├── index.md # Sectioned content catalog with one-line summaries
├── log.md # Chronological action log (append-only, rotated yearly)
├── raw/ # Layer 1: Immutable source material
│ ├── articles/ # Web articles, clippings
│ ├── papers/ # PDFs, arxiv papers
│ ├── transcripts/ # Meeting notes, interviews
│ └── assets/ # Images, diagrams referenced by sources
├── entities/ # Layer 2: Entity pages (people, orgs, products, models)
├── concepts/ # Layer 2: Concept/topic pages
├── comparisons/ # Layer 2: Side-by-side analyses
└── queries/ # Layer 2: Filed query results worth keeping
```

**第 1 层 — 原始来源：** 不可变的。代理只读取这些内容，从不修改它们。 **第 2 层 —— 知识库：** 代理拥有的 Markdown 文件。创建、更新以及 由智能体交叉引用 **第 3 层——架构：** `SCHEMA.md` 定义结构、规范和标签分类法。

## 恢复现有 Wiki（关键——每次会话都要执行此操作）

当用户已有 Wiki 时， **始终在采取任何行动之前明确自身定位** ：

① **阅读 `SCHEMA.md`** — 了解领域、约定和标签分类体系。 ② **阅读 `index.md`** — 了解存在哪些页面及其摘要。 ③ **浏览最近 `log.md`** — 阅读最近 20-30 条记录以了解近期活动。

```
WIKI="${wiki_path:-$HOME/wiki}"
# Orientation reads at session start
read_file "$WIKI/SCHEMA.md"
read_file "$WIKI/index.md"
read_file "$WIKI/log.md" offset=<last 30 lines>
```

只有在定向之后，你才应该导入、查询或进行代码检查。这可以防止:

- 为已存在的实体创建重复页面
- 缺少对现有内容的交叉引用
- 与模式的惯例相矛盾
- Repeating work already logged

对于大型维基（100+ 页），在创建任何新内容之前，还应对当前主题执行快速的 `search_files` 操作。

当用户请求创建或启动一个维基时：

1.  确定 wiki 路径（来自配置、环境变量或询问用户；默认 `~/wiki` ）
2.  创建上述的目录结构
3.  询问用户该 Wiki 涵盖的领域是什么——要具体
4.  编写 `SCHEMA.md` 针对该领域定制（见下方模板）
5.  编写初始的 `index.md` ，并带有分节标题
6.  编写初始的 `log.md` 并包含创建条目
7.  确认维基已准备就绪，并建议首批导入的来源

### SCHEMA.md Template

适应用户的领域。模式约束代理行为并确保一致性：

```
# Wiki Schema

## Domain
[What this wiki covers — e.g., "AI/ML research", "personal health", "startup intelligence"]

## Conventions
- File names: lowercase, hyphens, no spaces (e.g., `transformer-architecture.md`)
- Every wiki page starts with YAML frontmatter (see below)
- Use `[[wikilinks]]` to link between pages (minimum 2 outbound links per page)
- When updating a page, always bump the `updated` date
- Every new page must be added to `index.md` under the correct section
- Every action must be appended to `log.md`

## Frontmatter
  ```yaml
  ---
  title: Page Title
  created: YYYY-MM-DD
  updated: YYYY-MM-DD
  type: entity | concept | comparison | query | summary
  tags: [from taxonomy below]
  sources: [raw/articles/source-name.md]
  ---
```

## Tag Taxonomy

\[定义10-20个顶级标签用于该领域。在此处添加新标签，在使用它们之前。\]

Example for AI/ML:

- 模型：模型、架构、基准测试、训练
- 人物/组织：个人，公司，实验室，开源
- 技术：优化、微调、推理、对齐、数据
- Meta: 比较，时间线，争议，预测

规则：每个标签必须出现在这个分类体系中。如果需要新标签，先在这里添加，然后使用它。这可以防止标签泛滥。

## Page Thresholds

- **创建一个页面** 当实体/概念出现在 2+个来源中 或 在一个来源中处于核心地位
- **添加到现有页面** 当来源提到已经涵盖的内容时
- **不要创建页面** 用于传递提及、次要细节或领域之外的内容
- **拆分页面** 当页面超过约 200 行时 — 拆分为带有交叉链接的子主题
- **归档页面** 当页面内容被完全取代时 — 移动到 `_archive/` ，从索引中移除

## Entity Pages

每个重要实体对应一个页面。包括：

- Overview / what it is
- Key facts and dates
- 与其他实体的关系（\[\[wikilinks\]\]）
- Source references

## Concept Pages

每个概念或主题单独成页。包括：

- Definition / explanation
- Current state of knowledge
- Open questions or debates
- 相关概念 (\[\[wikilinks\]\])

## Comparison Pages

并排分析。包括：

- 比较的是什么，为什么
- 比较维度（建议使用表格形式）
- Verdict or synthesis
- Sources

## Update Policy

当新信息与现有内容冲突时：

1.  检查日期——较新的来源通常会取代较旧的来源
2.  如果确实存在矛盾，需记录双方立场并标注日期和来源
3.  在前置内容中标记矛盾： `contradictions: [page-name]`
4.  在 lint 报告中标记供用户审核

````
### index.md Template

The index is sectioned by type. Each entry is one line: wikilink + summary.

```markdown
# Wiki Index

> Content catalog. Every wiki page listed under its type with a one-line summary.
> Read this first to find relevant pages for any query.
> Last updated: YYYY-MM-DD | Total pages: N

## Entities
<!-- Alphabetical within section -->

## Concepts

## Comparisons

## Queries
````

**Scaling rule:** When any section exceeds 50 entries, split it into sub-sections by first letter or sub-domain. When the index exceeds 200 entries total, create a `_meta/topic-map.md` that groups pages by theme for faster navigation.

### log.md Template

```
# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete
> When this file exceeds 500 entries, rotate: rename to log-YYYY.md, start fresh.

## [YYYY-MM-DD] create | Wiki initialized
- Domain: [domain]
- Structure created with SCHEMA.md, index.md, log.md
```

## Core Operations

### 1\. Ingest

When the user provides a source (URL, file, paste), integrate it into the wiki:

① **Capture the raw source:**

- URL → use `web_extract` to get markdown, save to `raw/articles/`
- PDF → use `web_extract` (handles PDFs), save to `raw/papers/`
- Pasted text → save to appropriate `raw/` subdirectory
- Name the file descriptively: `raw/articles/karpathy-llm-wiki-2026.md`

② **Discuss takeaways** with the user — what's interesting, what matters for the domain. (Skip this in automated/cron contexts — proceed directly.)

③ **Check what already exists** — search index.md and use `search_files` to find existing pages for mentioned entities/concepts. This is the difference between a growing wiki and a pile of duplicates.

④ **Write or update wiki pages:**

- **New entities/concepts:** Create pages only if they meet the Page Thresholds in SCHEMA.md (2+ source mentions, or central to one source)
- **Existing pages:** Add new information, update facts, bump `updated` date. When new info contradicts existing content, follow the Update Policy.
- **Cross-reference:** Every new or updated page must link to at least 2 other pages via `[[wikilinks]]`. Check that existing pages link back.
- **Tags:** Only use tags from the taxonomy in SCHEMA.md

⑤ **Update navigation:**

- Add new pages to `index.md` under the correct section, alphabetically
- Update the "Total pages" count and "Last updated" date in index header
- Append to `log.md`: `## [YYYY-MM-DD] ingest | Source Title`
- List every file created or updated in the log entry

⑥ **Report what changed** — list every file created or updated to the user.

A single source can trigger updates across 5-15 wiki pages. This is normal and desired — it's the compounding effect.

### 2\. Query

When the user asks a question about the wiki's domain:

① **Read `index.md`** to identify relevant pages. ② **For wikis with 100+ pages**, also `search_files` across all `.md` files for key terms — the index alone may miss relevant content. ③ **Read the relevant pages** using `read_file`. ④ **Synthesize an answer** from the compiled knowledge. Cite the wiki pages you drew from: "Based on \[\[page-a\]\] and \[\[page-b\]\]..." ⑤ **File valuable answers back** — if the answer is a substantial comparison, deep dive, or novel synthesis, create a page in `queries/` or `comparisons/`. Don't file trivial lookups — only answers that would be painful to re-derive. ⑥ **Update log.md** with the query and whether it was filed.

### 3\. Lint

When the user asks to lint, health-check, or audit the wiki:

① **Orphan pages:** Find pages with no inbound `[[wikilinks]]` from other pages.

```
# Use execute_code for this — programmatic scan across all wiki pages
import os, re
from collections import defaultdict
wiki = "<WIKI_PATH>"
# Scan all .md files in entities/, concepts/, comparisons/, queries/
# Extract all [[wikilinks]] — build inbound link map
# Pages with zero inbound links are orphans
```

② **Broken wikilinks:** Find `[[links]]` that point to pages that don't exist.

③ **Index completeness:** Every wiki page should appear in `index.md`. Compare the filesystem against index entries.

④ **Frontmatter validation:** Every wiki page must have all required fields (title, created, updated, type, tags, sources). Tags must be in the taxonomy.

⑤ **Stale content:** Pages whose `updated` date is >90 days older than the most recent source that mentions the same entities.

⑥ **Contradictions:** Pages on the same topic with conflicting claims. Look for pages that share tags/entities but state different facts.

⑦ **Page size:** Flag pages over 200 lines — candidates for splitting.

⑧ **Tag audit:** List all tags in use, flag any not in the SCHEMA.md taxonomy.

⑨ **Log rotation:** If log.md exceeds 500 entries, rotate it.

⑩ **Report findings** with specific file paths and suggested actions, grouped by severity (broken links > orphans > stale content > style issues).

⑪ **Append to log.md:**`## [YYYY-MM-DD] lint | N issues found`

### Searching

```
# Find pages by content
search_files "transformer" path="$WIKI" file_glob="*.md"

# Find pages by filename
search_files "*.md" target="files" path="$WIKI"

# Find pages by tag
search_files "tags:.*alignment" path="$WIKI" file_glob="*.md"

# Recent activity
read_file "$WIKI/log.md" offset=<last 20 lines>
```

### Bulk Ingest

When ingesting multiple sources at once, batch the updates:

1.  Read all sources first
2.  Identify all entities and concepts across all sources
3.  Check existing pages for all of them (one search pass, not N)
4.  Create/update pages in one pass (avoids redundant updates)
5.  Update index.md once at the end
6.  Write a single log entry covering the batch

### Archiving

When content is fully superseded or the domain scope changes:

1.  Create `_archive/` directory if it doesn't exist
2.  Move the page to `_archive/` with its original path (e.g., `_archive/entities/old-page.md`)
3.  Remove from `index.md`
4.  Update any pages that linked to it — replace wikilink with plain text + "(archived)"
5.  Log the archive action

### Obsidian Integration

The wiki directory works as an Obsidian vault out of the box:

- `[[wikilinks]]` render as clickable links
- Graph View visualizes the knowledge network
- YAML frontmatter powers Dataview queries
- The `raw/assets/` folder holds images referenced via `![[image.png]]`

For best results:

- Set Obsidian's attachment folder to `raw/assets/`
- Enable "Wikilinks" in Obsidian settings (usually on by default)
- Install Dataview plugin for queries like `TABLE tags FROM "entities" WHERE contains(tags, "company")`

If using the Obsidian skill alongside this one, set `OBSIDIAN_VAULT_PATH` to the same directory as the wiki path.

On machines without a display, use `obsidian-headless` instead of the desktop app. It syncs vaults via Obsidian Sync without a GUI — perfect for agents running on servers that write to the wiki while Obsidian desktop reads it on another device.

**Setup:**

**Continuous background sync via systemd:**

```
# ~/.config/systemd/user/obsidian-wiki-sync.service
[Unit]
Description=Obsidian LLM Wiki Sync
After=network-online.target
Wants=network-online.target

[Service]
ExecStart=/path/to/ob sync --continuous
WorkingDirectory=/home/user/wiki
Restart=on-failure
RestartSec=10

[Install]
WantedBy=default.target
```

This lets the agent write to `~/wiki` on a server while you browse the same vault in Obsidian on your laptop/phone — changes appear within seconds.

## Pitfalls

- **Never modify files in `raw/`** — sources are immutable. Corrections go in wiki pages.
- **Always orient first** — read SCHEMA + index + recent log before any operation in a new session. Skipping this causes duplicates and missed cross-references.
- **Always update index.md and log.md** — skipping this makes the wiki degrade. These are the navigational backbone.
- **Don't create pages for passing mentions** — follow the Page Thresholds in SCHEMA.md. A name appearing once in a footnote doesn't warrant an entity page.
- **Don't create pages without cross-references** — isolated pages are invisible. Every page must link to at least 2 other pages.
- **Frontmatter is required** — it enables search, filtering, and staleness detection.
- **Tags must come from the taxonomy** — freeform tags decay into noise. Add new tags to SCHEMA.md first, then use them.
- **Keep pages scannable** — a wiki page should be readable in 30 seconds. Split pages over 200 lines. Move detailed analysis to dedicated deep-dive pages.
- **Ask before mass-updating** — if an ingest would touch 10+ existing pages, confirm the scope with the user first.
- **Rotate the log** — when log.md exceeds 500 entries, rename it `log-YYYY.md` and start fresh. The agent should check log size during lint.
- **Handle contradictions explicitly** — don't silently overwrite. Note both claims with dates, mark in frontmatter, flag for user review.