---
title: "2026-06-16_LufzzLiz_给任何开源项目建一份可信架构_wiki_LLM_Wiki_范式实战教程"
source: "https://x.com/LufzzLiz/status/2058542686551028006"
author:
  - "[[@LufzzLiz]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "#index"
  - "x"
  - "@LufzzLiz"
  - "wiki"
---

# 给任何开源项目建一份可信架构 wiki：LLM Wiki 范式实战教程

**岚叔**

# 给任何开源项目建一份可信架构 wiki：LLM Wiki 范式实战教程

## 引言

前几天有推友看到我最近做的几个 wiki 项目，想让我做次分享。整理材料的时候发现，与其重复讲口头版本，不如写一篇成体系的文章也方便大家复用。

这篇文章想回答三个问题：

1\. 为什么我要花时间做这些 wiki？传统的 README、Notion、飞书文档不够用吗？

2\. 怎么做才能让一个开源项目的源码变成一份可读、可查、可信的 wiki？

3\. 能复用吗你看完之后能不能照搬这套流程，给你自己关心的项目也建一个？

先抛结论：

我做wiki的目的也很简单，就是让LLM能够基于源码给出可信的分析，同时代码也是不断更新迭代的，用llm-wiki 也能够及时掌握所有关系链条。

LLM 让知识管理的根本矛盾松动了

本文将分享并开源：基于llm-wiki的skill，以及我们做的各种wiki和wiki-web

过去几十年所有的"个人知识库" 运动都败在同一件事上：维护成本随规模超线性增长，最后人都放弃了。

RAG 看起来解决了，但它每次查询都重新检索、重新合成，知识不积累、不复利。Karpathy 在 2026 年初提出了一个新范式：让 LLM 增量维护一个持久化的 markdown wiki。交叉引用预建好，矛盾预标注，合成预完成。人负责策展和提问，LLM 负责所有摘要、链接、归档。

看到 Karpathy 这篇 gist 后立刻动手验证，4 天后建了第一个 wiki（\[Hermes-Wiki\](

[https://github.com/cclank/Hermes-Wiki](https://github.com/cclank/Hermes-Wiki))），6 天后第二个（OpenClaw-wiki）。最近一段时间陆续做出 7 个 wiki 项目：

它们已经在我日常开发中起作用：

查 Hermes Agent 任何模块直接读 wiki 比读源码快；

给同事讲 X 算法时直接发 wiki 链接而不是讲一小时；

连"今天和昨天对源码理解有没有矛盾"这种细节，wiki 也能自动告诉我。

下面分两部分：先讲原理，再用 x-algorithm-wiki 当案例走一遍完整流程。

* * *

# 原理讲解

![Image](https://pbs.twimg.com/media/HJFnxqaaoAE6yl_?format=jpg&name=large)

## 1\. 三层架构：raw / wiki / schema

所有 wiki 都遵循同一个抽象：

```text
raw/ # 原始内容（源码、PDF、网页快照），不可变，LLM 只读不改
wiki/ # LLM 维护的结构化笔记（概念页、实体页、合成页）
schema/ # 人机共建的规则（CLAUDE.md / SCHEMA.md），定义页面格式、标签、工作流
```

这三层各司其职：

- raw 是真相的锚，任何时候有疑问都能回溯到原文
- wiki 是被"编译"过的知识，交叉引用、对比、矛盾都已经预先标注好
- schema 是人对 LLM 的"教学大纲"，告诉 LLM 怎么命名、怎么打标签、什么时候创建新页

## 2\. 两种范式

共同骨架：

\- \`index.md\`：给 LLM 看的扁平导航，每个页面一行摘要

\- \`log.md\`：所有操作的追加日志，跨会话连续性的关键

\- \`SCHEMA.md\` 或 \`CLAUDE.md\`：页面格式、标签体系、操作规则

\- \`\[\[wikilinks\]\]\`：Obsidian 兼容的双向链接

## 3\. 三大核心操作

3.1 Ingest（导入）：把一份资料拆成 5-15 个 wiki 页面：

1\. 完整阅读原文（不是只看标题）

2\. 与人讨论要点（确认理解对了）

3\. 在 index 里搜重，避免重复创建

4\. 原文存到 \`raw/\`（永不修改）

5\. 创建 \`sources/\` 摘要页，标 reliability（peer-reviewed / official / expert / social / unknown）

5\. 创建 \`sources/\` 摘要页，标注可靠性（同行评审的 / 官方的 / 专家的 / 社会的 / 未知的）

6\. 必须读相关页面全文 再决定怎么更新（禁止只看 index 摘要就改）

7\. 提取 entities、concepts，必要时创建 syntheses

8\. 同步 \`index.md\` + \`log.md\`

3.2 Query（查询）：综合多页回答问题，够"重"就归档：

\- 答案综合 ≥3 来源、跨领域对比、揭示新关联 → 自动归档为 synthesis

3.3 Lint（健康检查）: 9 类问题自动扫描：

\- 矛盾点（同一主题不同结论）/ 过时页 / 孤儿页 / 悬空链接 / 标签近义 / 摘要准确性 / 未解决问题汇总…

贯穿三大操作的硬规则：所有页面的结论必须能追溯到源码 \`文件:行号\` 或原文 URL；做不到，宁可不写。这条规则是 wiki 区别于"AI 自由总结"的核心。

## 4\. 用 Claude Code Skill 落地

4\. 用 Claude 编码技能落地

把上面这些规则做成一个 Claude Code skill 后，触发就变得很轻：

```bash
~/.claude/skills/wiki/
  SKILL.md # 薄路由层（触发词 + 命令决策树 + 新建 wiki 引导）
~/wiki/
  CLAUDE.md # 厚 schema（页面格式、标签、ingest 工作流的权威规则）
```

命令体系：\`/wiki add\` \`/wiki ingest\` \`/wiki query\` \`/wiki lint\` \`/wiki status\` \`/wiki deprecate\` \`/wiki retract\` \`/wiki merge\`。也支持自然语言，说"把这个加到 wiki 里"它就懂。

跨会话连续性靠每次新会话固定读三个文件：\`CLAUDE.md\` → \`index.md\` → \`log.md\` 最近 10 条。

* * *

# 实践部分：给一个开源项目建 wiki 的五步教程

![Image](https://pbs.twimg.com/media/HJFormcasAAo61Q?format=jpg&name=large)

以 \[x-algorithm-wiki\](

[https://github.com/cclank/x-algorithm-wiki](https://github.com/cclank/x-algorithm-wiki)) 为案例（\[在线预览\](

[https://lanshu-wiki-web.lank.workers.dev/wiki/cclank/x-algorithm-wiki#index](https://lanshu-wiki-web.lank.workers.dev/wiki/cclank/x-algorithm-wiki#index)

)）。

以 \[x-算法-wiki\](https://github.com/cclank/x-algorithm-wiki) 为例（\[在线预览\](https://lanshu-wiki-web.lank.workers.dev/wiki/cclank/x-algorithm-wiki#index)）。

34 页 / 6,800 行的 wiki 完整骨干就五步。任何开源项目都是同一套动作。

## Step 1 · 立项 + 锁源码

```bash
# 拉源码，锁定 commit 或 tag（避免后续 ingest 与源码漂移）
git clone https://github.com/xai-org/x-algorithm /tmp/x-algorithm
cd /tmp/x-algorithm && git checkout 0bfc279

# 新建 wiki 仓库 + 复制 schema 模板
mkdir ~/code/x-algorithm-wiki && cd $_
git init && mkdir -p concepts entities changelog
cp ~/code/lanshu-wiki-skill/schema/wiki-code-repo-SCHEMA.md ./SCHEMA.md
echo "# Wiki Index" > index.md && echo "# Wiki Log" > log.md
```

打开 \`SCHEMA.md\`，填两个 \`⚠️\` 字段：\*\*Domain 描述\*\*（项目 + commit + 覆盖的核心子系统）+ \*\*Tag Taxonomy\*\*（项目特定的标签体系，如 recsys / candidate-pipeline / ranking 等）。

## Step 2 · 让 LLM 通读源码产首批页

打开 Claude Code，一条 prompt 起飞（把尖括号里的内容换成你项目的）：

\> 读 \`SCHEMA.md\`，按它的规则给 \`<源码绝对路径>\` 做架构 wiki。

\> 从最核心的 5 个模块开始：\`<列出你项目最关键的 5 个目录或子系统>\`。

\> 硬规则：每个结论必须带 \`文件:行号\` 锚点，覆盖不到的不写。（这一条可以根据情况，也可以说严格按照源码来）

> 最后如果你觉得晦涩难懂，也可以基于已经尝试的事实内容让LLM生成白话文

x-algorithm-wiki 当时填的是 \`home-mixer / candidate-pipeline / phoenix / thunder / grox\` 这五个；你照葫芦画瓢替换即可。

一次产出 10-20 页 concept + entity，总计 2,000-5,000 行。这步建立的核心纪律是「结论可追溯」，之后所有页面都遵守。

## Step 3 · Lint 全量核对

每写完一批就 \`/wiki lint\`：

\- 悬空 \`\[\[wikilink\]\]\` / frontmatter 缺字段 / 标签近义重复 → 工具自动扫

\- \*\*随机抽 2-3 页对照源码全文核验\*\* → 发现「LLM 把 A 模块和 B 模块细节搞混」这类隐性错误的唯一办法

\- 发现 wiki 结论与官方文档冲突 → \*\*写进 changelog 而不是悄悄改\*\*（保留审计痕迹）

x-algorithm-wiki 当时核 29 页 482 个锚点，发现 3 处出入（mini 模型尺寸、打分器数量、候选隔离掩码），全部进 changelog。

## Step 4 · 双层导览 ⭐ 关键升级

到 Step 3 wiki 只服务工程师。发给产品同事看，反馈往往是「读不懂」，技术页全是源码术语。

解法：加 \`guide/\` 目录，按「技术页 + 白话页配对」做：

白话页同样要遵守可追溯规则：每条核心结论在白话页末尾的「出处」表里指到对应技术页 + 源码锚点。否则白话页就退化成 AI 自由发挥。

这一步把 wiki 从「工程师内部文档」升级成「对外宣传材料」：同一份 wiki 服务两类受众。

## Step 5 · 持续打磨

骨干至此 done。剩下是长期维护动作，两件就够：

- 定期 lint：随项目升级修锚点失效、补术语解释
- 读者反馈回流：用户问的好问题立刻补进 \`faq\`，新话题就开新页

# 可选扩展：Web 渲染

到这一步 wiki 是个纯 markdown 仓库，在 GitHub 或 Obsidian 里就能看。如果想给非技术人分享，把仓库喂给 \[lanshu-wiki-web\](

[https://github.com/cclank/lanshu-wiki-web](https://github.com/cclank/lanshu-wiki-web))，秒变带 D3 知识图谱、\`Cmd+K\` 全文搜索、Mermaid 渲染、\`\[\[wikilink\]\]\` 站内跳转的阅读站。

效果看 x-algorithm-wiki 的在线版：\[

[lanshu-wiki-web.lank.workers.dev/wiki/cclank/x-algorithm-wiki](//lanshu-wiki-web.lank.workers.dev/wiki/cclank/x-algorithm-wiki)\](

[https://lanshu-wiki-web.lank.workers.dev/wiki/cclank/x-algorithm-wiki#index](https://lanshu-wiki-web.lank.workers.dev/wiki/cclank/x-algorithm-wiki#index)

)

查看效果 x-算法-wiki 的在线版：\[lanshu-wiki-web.lank.workers.dev/wiki/cclank/x-algorithm-wiki\](https://lanshu-wiki-web.lank.workers.dev/wiki/cclank/x-algorithm-wiki#index)

## 踩过的坑 / 给新人的提醒

\- \*\*同概念多种命名是头号杀手\*\*：Hermes-Wiki 一度有 8 种 kanban 命名、6 种 ralph-loop 命名（不同 daily-sync 各起各的）。创建新页前先 grep \`index.md\` 找近义页

\- \*\*不读全文就改是二号杀手\*\*：只看 index 摘要就动手改页面会丢信息，schema 强制"更新前必读全文"

\- \*\*标签每月 lint 一次\*\*：不去重的话，一年后 30 个标签里 10 个语义重叠

\- \*\*changelog + log.md 是审计轨\*\*：每次操作追加，问题溯源不慌；这是 wiki 比 Notion / 飞书文档强的地方

## 什么时候不该用 LLM Wiki

为了客观，也说说边界：

- 规模上限 ~2000 页：index.md 要装得下所有页面摘要供 LLM 一次性读完。超过 ~1000 页就要考虑按领域拆子 wiki，超过 ~2000 页这个模式开始裂
- 多人并发协作还粗糙：多人同时 ingest 同一来源会创建多份 source 页，需要事后 \`/wiki merge\`；schema 也要先达成共识。当前 skill 主打单人/小团队场景
- Token 成本不可忽视: 让 LLM 通读 5 万行源码做首批 ingest，一次大约消耗 100k-500k input token（按 Claude Sonnet 4.5 价目约 $0.3-1.5），加上多轮 lint 和后续 ingest，一个中等项目 wiki 全周期 $5-30 量级。比工程师工时便宜，但不是免费

## skill 开源&实操建议

不过对你更实用的事就一件：自己也建一个 wiki。最简单的入门路径：

```bash

# 1. 装 skill
git clone https://github.com/cclank/lanshu-wiki-skill.git ~/code/lanshu-wiki-skill
mkdir -p ~/.claude/skills/wiki
ln -sf ~/code/lanshu-wiki-skill/SKILL.md ~/.claude/skills/wiki/SKILL.md

# 2. 个人知识库就这样开张
mkdir -p ~/wiki/{raw,sources,entities,concepts,syntheses,reports,assets}
cp ~/code/lanshu-wiki-skill/schema/wiki-personal-CLAUDE.md ~/wiki/CLAUDE.md
cd ~/wiki && echo "# Wiki Index" > index.md && echo "# Wiki Log" > log.md && echo "# Wiki Inbox" > inbox.md

# 3. 给开源项目建架构 wiki 就这样开张
mkdir ~/code/<project>-wiki && cd ~/code/<project>-wiki
mkdir -p concepts entities changelog
cp ~/code/lanshu-wiki-skill/schema/wiki-code-repo-SCHEMA.md ./SCHEMA.md
echo "# Wiki Index" > index.md && echo "# Wiki Log" > log.md
```

然后打开 Claude Code，自然语言说"添加到 wiki <URL>"或"按 SCHEMA 给 \`<repo>\` 做架构 wiki"就开始。

详细说明、FAQ、对比表、双层导览模式、五步实战指南都在仓库 README 里：\[

[github.com/cclank/lanshu-wiki-skill](//github.com/cclank/lanshu-wiki-skill)\](

[https://github.com/cclank/lanshu-wiki-skill](https://github.com/cclank/lanshu-wiki-skill)

)

想要在线预览效果，直接喂任何 wiki 仓库给 \[

[lanshu-wiki-web.lank.workers.dev](//lanshu-wiki-web.lank.workers.dev)\](

[https://lanshu-wiki-web.lank.workers.dev](https://lanshu-wiki-web.lank.workers.dev)

)。

* * *

## 致谢与传承

这个范式的核心思想不是我发明的，本文只是把它工程化。

Vannevar Bush 在 1945 年的 \[\*As We May Think\*\](

[https://en.wikipedia.org/wiki/As\_We\_May\_Think](https://en.wikipedia.org/wiki/As_We_May_Think)) 一文里提出了 \[Memex\](

[https://en.wikipedia.org/wiki/Memex](https://en.wikipedia.org/wiki/Memex)

)：一个个人化、人工策展、文档之间充满"联想路径"的桌面知识库。

Bush 的设想比后来万维网走的方向更接近知识管理的本质：私有、深度、有人在持续策展。当年他给后人留了一个未解问题：\*\*"谁来维护这些关联？"\*\* 这个问题压垮了之后 80 年所有的个人知识库尝试（卡片盒、Zettelkasten、Notion、Obsidian……人最终都会放弃维护）。

Andrej Karpathy 在 2026 年 4 月发表的 \[LLM Wiki gist\](

[https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f))（只有 75 行）给出了答案：\*\*让 LLM 来做维护\*\*。

三层架构（raw / wiki / schema）、三大操作（Ingest / Query / Lint）、index + log 的设计、"知识应该编译而非每次解释执行"的论证，\*\*全部来自他那 75 行文章\*\*。本文以及我做的所有 wiki 工具，都是把那个抽象 idea 工程化。

致以最高敬意。建议把两篇配着看：\*\*想理解思想，读 \[Karpathy 原文\](

[https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f))\*\*（只要 10 分钟）；

想做出来一个能跑的 wiki，读本文 + 用 \[lanshu-wiki-skill\](

[https://github.com/cclank/lanshu-wiki-skill](https://github.com/cclank/lanshu-wiki-skill))。前者给你 why，后者给你 how。

欢迎来 issue 区交流，或者拿你的 wiki 链接来给我看。这种东西做的人越多越好玩。

> 更好的阅读体验版本可查看：
> 
> [https://mp.weixin.qq.com/s/N2HP\_sxYnUqESiOiKPPamg](https://mp.weixin.qq.com/s/N2HP_sxYnUqESiOiKPPamg)