---
title: "2026-06-16_Jimmy_JingLv_Agent_Skills_复利工程_你的烂笔记比代码值钱"
source: "https://x.com/Jimmy_JingLv/status/2036417234764279883"
author:
  - "[[@Jimmy_JingLv]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "x"
  - "@Jimmy_JingLv"
  - "claude"
  - "skill"
---

# Agent Skills 复利工程：你的烂笔记比代码值钱

**吕立青\_JimmyLv 2𐃏26**

# Agent Skills 复利工程：你的烂笔记比代码值钱

> 200+ 篇技术笔记 → 6 分钟全量审计 → 4 个 P0 级 Agent Skill。我什么都没教，Claude Code 从我的踩坑记录里自己「学」出来的。

![Image](https://pbs.twimg.com/media/HELKsjzbYAAE5M_?format=jpg&name=large)

## 一句话的起点

```text
学习一下所有的 notes/ 目录下的 .md 文件，看看有什么有价值的，
按照价值进行评分和分类，写入一个新的 note，
还有一列是是否有价值提取为 agent skill 来复用。
```

就这一句。

没有给它模板，没有告诉它怎么分类，没有定义什么叫「有价值」。Claude Code 自己读完 200+ 篇笔记，输出了一份带评分、带分类、带 Skill 提取建议的完整审计报告。

审计报告里标出了 42+ 个可以提取为 Agent Skill 的候选项，按复用频率排了优先级。我挑了排名最高的 3 个说：「incremental-refactor、i18n-page-registrar、state-layer-generator 这 3 个也帮我创建 Skill。」

Claude Code 读了对应的源笔记，理解了每个模式的根因和修复方案，然后自己写出了完整的 SKILL.md——包括触发条件、工作流步骤、代码模板和 Gotchas 段落。加上之前已经创建的 db-performance-auditor，一共 4 个 P0 级 Skill，从笔记到可用，全程不到 10 分钟。

好家伙，我过去一年随手写的那些技术笔记，竟然全是复利资产。

## 复利工程：每一轮工作让下一轮更容易

[Every.to](//Every.to) 团队提出了一个概念叫 Compound Engineering（复利工程）。核心理念一句话：

> Each unit of engineering work should make subsequent units easier—not harder.
> 
> 每个工程工作单元都应该使后续单元更容易，而不是更困难。

传统开发是什么样的？写代码 → 功能上线 → 写更多代码。代码量越来越多，复杂度越来越高，每次改动越来越难。这是递减收益。

复利工程反过来。他们提出一个四步循环：

```text
Plan（规划）→ Work（执行）→ Review（审查）→ Compound（沉淀）
```

关键在最后一步——Compound。每完成一个任务，都要把过程中的教训、模式、方案沉淀下来，让系统本身变得更聪明。下次遇到类似问题时，Agent 已经知道怎么处理了。

![Image](https://pbs.twimg.com/media/HELK3LcaIAAJgf0?format=jpg&name=large)

更反直觉的是他们的精力分配：80% 花在规划和审查上，20% 花在执行上。 跟传统开发完全反过来。因为执行可以交给 Agent，但规划的质量和沉淀的深度决定了复利能不能滚起来。

我做的「笔记审计 → 提取 Skill」，本质上就是一次集中式的 Compound 操作。把过去一年零散积累的 200 篇笔记，一次性转化为 4 个可复用的自动化能力。

## 它是怎么「学」的

200 篇笔记不可能一个个串行读——那得读到天荒地老。Claude Code 自动拆成 8 个并行 agent，每个读 25 篇左右，同时跑。

![Image](https://pbs.twimg.com/media/HELLIu0bAAAjxJi?format=jpg&name=large)

```text
Agent 1: 2025-01 ~ 2025-03  (基础能力建设期)
Agent 2: 2025-04 ~ 2025-06  (博客+分析+Remotion)
Agent 3: 2025-07 (功能爆发期：播单/弹幕/音乐)
Agent 4: 2025-08 (Prompt市场/视频生成/桌面端)
Agent 5: 2025-09 (PDF/EPUB/OAuth/高亮系统)
Agent 6: 2025-10 ~ 2025-11  (性能优化+跨平台)
Agent 7: 2025-12 (i18n/CutFast/编辑器)
Agent 8: 2026-01 ~ 2026-03  (Agent化+iOS+Docker)
```

每个 agent 返回结构化结果：文件名、摘要、分类、价值评分（1-5）、是否可提取为 Skill。

8 个 agent 的结果汇总后，Claude Code 自己做了交叉分析——发现同一个模式在不同时间段反复出现，说明这就是高复用候选。

## 审计结果：200 篇笔记的「体检报告」

![Image](https://pbs.twimg.com/media/HELLSljaIAMka4T?format=jpg&name=large)

主题分布一目了然：

```text
Feature Implementation ████████████████████████████  62 篇 (31%)
Refactoring/Architecture ██████████████████ 40 篇 (20%)
Bug Fix ████████████ 25 篇 (13%)
Infrastructure/DevOps ██████████ 22 篇 (11%)
Performance Optimization ████████ 18 篇 (9%)
```

但最有价值的东西藏在统计数据背后——它识别出了反复出现的模式：

> 最大复用机会：DB 性能审计、i18n 注册、CI 优化、API fallback 链——这四个模式在笔记中反复出现。

同一类问题出现了 3 次以上，说明这是真正的高频场景。手动做一次可以，做三次就该自动化了。

## 从笔记到 Skill：以 db-performance-auditor 为例

![Image](https://pbs.twimg.com/media/HELLypRa0AAJ0CY?format=jpg&name=large)

3 篇笔记孵化出 1 个 Skill：

![Image](https://pbs.twimg.com/media/HELL118bsAABA3d?format=jpg&name=large)

Claude Code 读完这 3 篇笔记后，自动提取出 6 点审计清单。不是简单复制粘贴——它理解了每个问题的根因，把具体案例泛化成了通用模式。

比如 select('\*') 这个点，笔记里写的是 user\_contents 表的具体修复。Skill 里泛化成了：

```text
Audit 1: select('*') Anti-Pattern (Critical)

Why it matters: Postgres 按 8KB 页管理 buffer pool。
行越宽，每页能放的行越少，cache hit rate 越低。
即使你只用 id 和 title，数据库仍然要碰那个 50KB 的 JSONB 列。

How to fix:
1. 追踪下游代码实际用了哪些字段
2. 替换为显式列名：.select('id, title, created_at')
3. 定义常量避免散弹式修改（参考 USER_CONTENT_COLUMNS 模式）
```

从一个表的修复经验，变成了所有表都能用的审计模式。 这就是复利工程里说的 Compound——把一次性的修复转化为永久性的能力。

## 4 个 Skill 对应 Anthropic 官方分类的哪些类型？

Anthropic 的 Thariq 最近写了一篇

[Lessons from Building Claude Code: How We Use Skills

从构建 Claude 代码中获得的经验：我们如何运用技能](https://x.com/trq212/status/2033949937936085378)（5.8M views），把内部数百个 Skill 归纳为 9 大类型。我这 4 个 Skill 正好覆盖了其中 3 种：

![Image](https://pbs.twimg.com/media/HELL-_aaIAQ-_n2?format=jpg&name=large)

Thariq 的文章里有几个洞察，跟我这次实践高度吻合。

洞察一：「Don't State the Obvious」

洞察一：「不要陈述显而易见的内容」

> Claude knows a lot about your codebase, and Claude knows a lot about coding. Focus on information that pushes Claude out of its normal way of thinking.
> 
> Claude 对您的代码库非常了解，并且对编程也很精通。专注于能促使 Claude 脱离常规思维方式的信息。

好的 Skill 得有项目特有知识。Claude 本来就知道什么是索引——但它不知道「Supabase PostgREST 有 30 秒硬超时，SET LOCAL statement\_timeout 没用」、「LEFT JOIN ... IS NULL 在已迁移行多时退化严重」。

这些反直觉的坑，正是笔记里记的东西，也是 Claude 自己推理不出来的。

洞察二：「Build a Gotchas Section」

洞察二：「构建一个易错点部分」

> The highest-signal content in any skill is the Gotchas section. These should be built up from common failure points that Claude runs into.
> 
> 在任何技能中，最关键的内容是注意事项部分。这些应该由 Claude 遇到的常见失败点构建而成。

完全同意。我每个 Skill 末尾都有一个 Gotchas 段落，全部来自笔记里真实踩过的坑：

```text
## Gotchas (Learned from BibiGPT Production)

1. Supabase PostgREST 有 30s 硬超时 — SET LOCAL statement_timeout 无效
2. LEFT JOIN ... IS NULL 随迁移行数增长退化 — 用 ON CONFLICT DO NOTHING
3. MAX(uuid) 在 Postgres 中不存在 — 用 ORDER BY id DESC LIMIT 1
4. Partial index 引用的列被删除时会挂 — 先删索引再删列
```

这些 Gotchas 全从 3 篇笔记里 Claude 自己提炼出来的。笔记越详细，Gotchas 越精准。

洞察三：「The Description Field Is For the Model」

洞察三：「描述字段用于模型」

> The description field is not a summary — it's a trigger condition for when to activate this skill.
> 
> 描述字段不是摘要——它是激活此技能时的触发条件。

这个我在自评环节才意识到。Skill 的 description 写给 Claude 看，当触发条件用——得写得「有侵略性」一点：

```text
# 太保守（经常不触发）
description: "Database performance optimization tool"

# 有效（覆盖多种触发场景）
description: "Audit Supabase/Postgres database performance. Use when:
the user reports slow queries, asks to optimize a table, creates
a new migration, encounters duplicate record bugs, or sees Disk
IO Budget warnings. Also trigger when you notice select('*')
in Supabase queries during code review."
```

## 4 种知识提炼方式

![Image](https://pbs.twimg.com/media/HELMHw3aIAAIwws?format=jpg&name=large)

![Image](https://pbs.twimg.com/media/HELMVAnaIAQPdvd?format=jpg&name=large)

四种不同的提炼逻辑：

- db-performance-auditor：把具体 bug 修复泛化为通用审计模式
- incremental-refactor：把多次重构经验抽象为可复现的方法论
- i18n-page-registrar：把容易遗漏的步骤编排为不可跳过的 checklist
- state-layer-generator：把踩坑教训结构化为决策矩阵 + 代码模板

用复利工程的语言说：笔记是 raw experience，Skill 是 codified knowledge。前者是一次性的，后者是可复用的。转化的那一刻，就是复利开始滚的时刻。

## Skill 自评 + 改进

Skill 写完不算完。用 /skill-creator 做了一轮自我审查：

```text
Cross-cutting improvements:
1. 删除冗余的 "When to Use" 段落（description 已经覆盖触发条件）
2. bash grep 命令 → Grep tool 引用（遵循项目工具规范）
3. 把 MUST/NEVER 改成解释 why（LLM 理解动机比服从命令更有效）
```

第三点值得展开说。

Thariq 的文章提到一个原则：Avoid Railroading Claude。

> Give Claude the information it needs, but give it the flexibility to adapt to the situation.
> 
> 给 Claude 它所需的信息，但给它灵活性以适应情况。

Skill 写作有个反直觉的要求：不要用命令式口吻，要解释为什么。今天的 LLM 足够聪明，理解了动机之后它能自己判断边界情况。

```text
# 命令式（差）——死记硬背
MUST NOT use NOT IN for large tables.
​
# 解释式（好）——举一反三
NOT IN (SELECT ...) 对大表是 O(n²)——每删一行都要全量扫描子查询。
用临时表 + NOT EXISTS，复杂度降到 O(n log n)。
```

前者只能覆盖这一个 case，后者让 Claude 理解了原理，遇到变体也能正确处理。

复利工程管这个叫「taste extraction」——把品味和偏好编码进系统，而不是靠人工 review 来把关。解释了 why 的规则，比强制的 MUST 有更强的泛化能力。

## .agents/ 软链接：一份 Skill，两个 Agent 系统共享

BibiGPT 同时用 Claude Code（.claude/skills/）和 Codex（.agents/skills/）。Skill 文件只维护一份，用软链接同步：

```text
cd .agents/skills
ln -s ../../.claude/skills/db-performance-auditor db-performance-auditor
ln -s ../../.claude/skills/incremental-refactor incremental-refactor
```

改一处，两边同步生效。单一数据源，零维护成本。

Thariq 也提到了 Skill 分发的问题——小团队直接 check in 到 repo 就行，规模大了就需要内部 marketplace。我们用软链接算是轻量级方案，适合 2-3 个 Agent 系统并行的场景。

## 复利闭环：为什么笔记 + Skill + 规则能滚起来

复利工程的四步循环（Plan → Work → Review → Compound）在这里变成了：

![Image](https://pbs.twimg.com/media/HELMgygaIAACkeM?format=jpg&name=large)

关键区别在于：传统团队的 Compound 是手动的——靠 senior 写文档、做分享。这里的 Compound 是 Agent 驱动的——Claude Code 自己读笔记、自己提炼模式、自己生成 Skill。人的角色从「写文档的人」变成了「审核 Agent 输出的人」。

## 这套方法你也能用

不需要 200 篇笔记才能开始。3 篇就够。

![Image](https://pbs.twimg.com/media/HELMmsKaIAAYI7W?format=jpg&name=large)

Step 1：种下种子——Self-Learning Protocol

步骤 1：种下种子——自学习协议

在项目的 CLAUDE.md 里加三行规则：

```text
## Self-Learning Protocol
​
1. 技术攻坚时 → 记录到 notes/
2. 同类问题反复出现时 → 新建 Agent Skill
3. Claude 默认行为不符合项目规范时 → 添加 CLAUDE.md 规则
```

有了这个，Claude Code 会在合适的时机主动提醒你：「这个问题建议记录到 notes」。

Step 2：积累笔记

每次技术攻坚写一篇。不用多精致，三要素就够：问题、方案、踩坑点。

Thariq 说得对——Skill 里最有价值的是 Gotchas 段落。而 Gotchas 的原材料就是笔记里那些「好家伙，原来是这个原因」的瞬间。你现在写得越详细，未来提炼出的 Skill 就越精准。

Step 3：定期审计

笔记攒到 20 篇左右，让 Claude Code 做一次全量审计：

```text
读一下 notes/ 下所有 .md 文件，
按价值评分，找出反复出现的模式，
标记哪些可以提取为 Skill。
```

Step 4：提取 Skill

对审计结果里标记「可提取」的条目，挑出现频次最高的优先做。参考 Anthropic 的 9 大分类，想想你的团队最缺哪种：

![Image](https://pbs.twimg.com/media/HELMv4vaIAAxh7L?format=jpg&name=large)

Step 5：自评改进

用 /skill-creator 让 Claude 审查 Skill 的触发描述、指令清晰度、是否有冗余。记住：description 是给 model 看的触发条件，不是给人看的摘要。

这五步是个循环。笔记越多，审计越准；Skill 越多，新笔记越少（因为问题被自动化解决了）。这就是复利。

## 写在最后

大多数团队的知识管理是这样的：写文档 → 没人看 → 过时 → 重写 → 又没人看。

区别在于，笔记的消费者变了。Agent 才是真正的读者。

Agent 不会觉得文档太长而跳过，不会因为格式不好看而拒绝阅读，不会因为半年前写的就觉得过时。它会老老实实读完 200 篇笔记，找出你自己都忘了的模式，然后把这些模式变成可执行的自动化。

复利工程的核心信念转变里有一条：

> Teaching the system compounds; typing code only solves immediate tasks.

写代码只解决当下问题。教会系统，才能产生复利。

你写的每篇踩坑记录，都是 Agent 的训练数据。

每一篇踩坑记录都是未来某个 Skill 的种子。200 篇笔记 × 每篇 5 分钟 = 约 17 小时的原始积累。换来 4 个可以无限复用的自动化 Skill，加上一份让你一眼看清半年工作脉络的审计报告。

传统开发是线性的——投入时间，产出代码。

复利工程是指数的——投入时间，产出让未来节省时间的系统。

这笔账，怎么算都划算。

基于

[BibiGPT](https://bibigpt.co) 项目实战。200+ 篇笔记审计 + 4 个 P0 Skill 提取的完整过程记录。

参考：

[Compound Engineering](https://every.to/guides/compound-engineering) by

[Every.to](//Every.to)

|

[How We Use Skills](https://x.com/trq212/status/2033949937936085378)

by Thariq @ Anthropic

参考：

[复合工程](https://every.to/guides/compound-engineering)

由

[Every.to](//Every.to)

|

[我们如何运用技能](https://x.com/trq212/status/2033949937936085378)

由 Thariq @ Anthropic