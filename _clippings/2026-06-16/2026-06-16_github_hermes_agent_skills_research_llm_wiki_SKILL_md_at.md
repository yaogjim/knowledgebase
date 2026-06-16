---
title: "2026-06-16_github_com_hermes_agent_skills_research_llm_wiki_SKILL_md_at_"
source: "https://github.com/NousResearch/hermes-agent/blob/main/skills/research/llm-wiki/SKILL.md"
author:
  - "[[@github.com]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "#5660"
  - "github"
  - "@github.com"
  - "md"
---

# hermes-agent/skills/research/llm-wiki/SKILL.md at main · NousResearch/hermes-agent

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

**缩放规则：** 当任何章节超过 50 个条目时，按首字母或子域将其拆分为子章节。当总条目数超过 200 时，创建一个 `_meta/topic-map.md` ，该文件按主题对页面进行分组以实现更快的导航。

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

当用户提供一个来源（URL、文件、粘贴内容）时，将其整合到维基中：

① **捕获原始源：**

- URL → 使用 `web_extract` 获取 Markdown，保存到 `raw/articles/`
- PDF → 使用 `web_extract` （处理 PDF），保存到 `raw/papers/`
- 粘贴的文本 → 保存到合适的 `raw/` 子目录
- 描述性地命名文件： `raw/articles/karpathy-llm-wiki-2026.md`

② **讨论要点** 与用户——有趣的地方是什么，以及对该领域重要的内容是什么。（在自动化/定时任务场景中跳过此步骤——直接继续。）

③ **检查已存在的内容** — 搜索 index.md 并使用 `search_files` 查找已提及的实体/概念对应的现有页面。这就是不断发展的维基与一堆重复内容之间的区别。

④ **编写或更新维基页面：**

- \*\*新实体/概念：\*\* 仅当新实体/概念满足 SCHEMA.md 中的页面阈值（2 个以上来源提及或某一来源的核心内容）时，才创建页面
- **现有页面：** 添加新信息，更新事实，更新 `updated` 日期。当新信息与现有内容冲突时，遵循更新政策。
- **交叉引用：** 每一个新页面或已更新的页面必须通过\[\[wikilinks\]\]链接到至少 2 个其他页面。检查现有页面是否有反向链接。
- **标签：** 仅使用 SCHEMA.md 中分类体系里的标签

⑤ **更新导航：**

- 添加新页面到 `index.md` 的正确章节下，按字母顺序
- 更新索引头部中的"总页数"计数和"最后更新"日期
- Append to `log.md`: `## [YYYY-MM-DD] ingest | Source Title`
- 列出日志条目中创建或更新的每个文件

⑥ **报告变更内容** — 列出所有创建或更新的文件给用户。

单一来源可以触发5-15个维基页面的更新。这是正常且期望的——这就是复合效应。

### 2\. Query

当用户询问关于 wiki 领域的问题时：

① **阅读 `index.md`** 以识别相关页面。② **对于拥有 100+ 页的维基** ，还需在所有 `.md` 文件中 `search_files` 关键术语 —— 仅靠索引可能会遗漏相关内容。③ **阅读相关页面** 使用 `read_file` 。④ **综合答案** 从整理的知识中生成。引用你参考的维基页面：“基于 \[\[page-a\]\] 和 \[\[page-b\]\]...” ⑤ **归档有价值的答案** —— 如果答案是实质性比较、深入分析或新颖的综合，请在 `queries/` 或 `comparisons/` 中创建一个页面。不要归档琐碎的查询 —— 仅归档重新推导时会很麻烦的答案。⑥ **更新 log.md** ，包含查询内容及是否已归档。

### 3\. Lint

当用户要求对 Wiki 进行代码检查、健康检查或审计时：

① **孤立页面：** 查找没有来自其他页面的入站 `[[维基链接]]` 的页面。

```
# Use execute_code for this — programmatic scan across all wiki pages
import os, re
from collections import defaultdict
wiki = "<WIKI_PATH>"
# Scan all .md files in entities/, concepts/, comparisons/, queries/
# Extract all [[wikilinks]] — build inbound link map
# Pages with zero inbound links are orphans
```

② **失效的维基链接：** 查找指向不存在的页面的 `[[links]]`

③ **索引完整性：** 每个维基页面都应该出现在 `index.md` 中。将文件系统与索引条目进行比较。

④ **前置内容验证：** 每个维基页面必须包含所有必填字段（标题、创建时间、更新时间、类型、标签、来源）。标签必须属于分类体系。

⑤ **陈旧内容** ：页面的 `updated` 日期比提及相同实体的最新来源的日期早超过 90 天。

⑥ **矛盾** ：同一主题的页面存在相互矛盾的说法。寻找共享标签/实体但陈述不同事实的页面。

⑦ **页面大小：** 标记超过 200 行的页面——需要拆分的候选页面。

⑧ **标签审核：** 列出所有正在使用的标签，标记任何不在 SCHEMA.md 分类体系中的标签。

⑨ **日志轮转：** 如果 log.md 超过 500 条记录，轮转它。

⑩ **报告发现** ，包含具体文件路径和建议的操作，按严重程度分组（断链＞孤立页面＞过时内容＞样式问题）

⑪ **追加到 log.md：** `## [YYYY-MM-DD] lint | N issues found`

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

当同时导入多个来源时，批量处理更新：

1.  Read all sources first
2.  识别所有来源中的所有实体和概念
3.  检查所有这些的现有页面（一次搜索遍历，不是 N 次）
4.  一次性创建/更新页面（避免重复更新）
5.  在最后更新一次 index.md
6.  编写一条涵盖该批次的日志记录

### Archiving

当内容被完全取代或领域范围发生变化时：

1.  如果不存在，则创建 `_archive/` 目录
2.  将页面移动到 `_archive/` 并保持其原始路径（例如： `_archive/entities/old-page.md` ）
3.  Remove from `index.md`
4.  更新任何链接到它的页面 — 将 wikilink 替换为纯文本并加上 "(archived)"
5.  Log the archive action

### Obsidian Integration

wiki 目录开箱即用，可作为 Obsidian vault 使用：

- `[[wikilinks]]` render as clickable links
- 图形视图可视化知识网络
- YAML 前置元数据支持 Dataview 查询
- 文件夹 `raw/assets/` 存储通过 `![[image.png]] 引用的图像`

For best results:

- 将 Obsidian 的附件文件夹设置为 `raw/assets/`
- 在 Obsidian 设置中启用“Wikilinks”（通常默认开启）
- 安装 Dataview 插件用于 `TABLE tags FROM "entities" WHERE contains(tags, "company") 之类的查询`

如果同时使用 Obsidian 技能与本技能，请将 `OBSIDIAN_VAULT_PATH` 设置为与 wiki 路径相同的目录。

### Obsidian 无头版（服务器和无头机器）

在没有显示器的机器上，使用 `obsidian-headless` 替代桌面应用。它通过 Obsidian Sync 同步知识库（vaults），无需图形界面（GUI）——非常适合在服务器上运行的代理程序，这些代理程序向知识库（wiki）写入内容，而 Obsidian 桌面应用则在另一台设备上读取知识库内容。

**Setup:**

**通过 systemd 进行持续的后台同步：**

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

这允许代理在服务器上写入 `~/wiki` ，而当你在笔记本电脑/手机上的 Obsidian 中浏览同一个知识库时，更改会在几秒钟内显示出来。

## Pitfalls

- **切勿修改 `raw/ 中的文件 — 源文件不可变。更正应提交到维基页面。`**
- **始终先明确方向** — 在新会话中进行任何操作前，请先阅读 SCHEMA + 索引 + 最近日志。跳过这一步会导致重复项和遗漏的交叉引用。
- 始终更新 index.md 和 log.md — 跳过这一步会使维基（wiki）退化。这些是导航的支柱。
- **不要为临时提及创建页面** — 请遵循 SCHEMA.md 中的页面阈值。一个名称在脚注中出现一次并不足以证明需要创建实体页面。
- **不要创建没有交叉引用的页面** — 孤立的页面是不可见的。每个页面必须至少链接到另外 2 个页面。
- **前置内容是必需的** — 它支持搜索、筛选和陈旧性检测。
- **标签必须来自分类体系** — 自由形式标签会逐渐变成噪声。首先将新标签添加到 SCHEMA.md 中，然后使用它们。
- **保持页面易读** — 维基页面应能在 30 秒内读完。将超过 200 行的页面拆分。将详细分析移至专门的深度分析页面。
- **大规模更新前先询问** — 如果一次导入会影响 10 个以上现有页面，请先与用户确认范围。
- **日志轮转** — 当 log.md 的条目数超过 500 时，将其重命名为 `log-YYYY.md` 并重新开始。代理应在 lint 过程中检查日志大小。
- **明确处理矛盾** ——不要悄无声息地覆盖。记录两个带日期的声明，在 frontmatter 中标记，并标记供用户审核。