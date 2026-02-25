---
title: "2026-02-25_宝玉_宝玉_用_Claude_Code_的_Hook_Skill_实现每次提交后自从_comm"
source: "https://x.com/dotey/status/2024036073265942784"
author:
  - "[[@宝玉]]"
published: 2026-02-25
created: 2026-02-25
description:
tags:
  - "x"
  - "@宝玉"
  - "git"
  - "commit"
---

# 宝玉 用 Claude Code 的 Hook + Skill，实现每次提交后自从 comm

**宝玉**

用 Claude Code 的 Hook + Skill，实现每次提交后自从 commit 提交变更

我用 Git 管理所有写作内容，文章、素材、提纲、草稿，全在仓库里。问题是我经常忘记提交。写完一篇文章，润色完，发布了，然后就去忙别的了。过几天一看 git status，十几个文件的变更堆在那里，完全不记得哪次改了什么。Git 本来是用来追踪每一步修改的，结果变成了一个大杂烩的快照工具。

现在我用 Claude Code 跑写作流程，从素材分析到成稿发布基本都交给它。既然每次任务它都在改文件，能不能让它改完就自己提交？

两个机制配合就解决了。

【1】Hook：任务结束时的拦截器

Claude Code 支持 Hook 机制，在特定事件（会话开始、工具调用前后、任务结束等）发生时自动执行脚本。思路和 Git Hook 类似，但挂在 Claude Code 的生命周期上。

我在项目的 .claude/settings.local.json 里配了一个 Stop Hook，每次 Claude Code 准备结束任务时触发：

\`\`\`json "hooks": { "Stop": \[{ "hooks": \[{ "type": "command", "command": "\\"$CLAUDE\_PROJECT\_DIR\\"/.claude/hooks/auto-commit.sh" }\] }\] } \`\`\`

\`\`\`json "钩子": { “停止”： \[{ "钩子": \[{ "type": "命令", "命令": "\\"$CLAUDE\_PROJECT\_DIR\\"/.claude/hooks/auto-commit.sh" }\] }\] } \`\`\`

脚本做的事很简单：检查工作区有没有未提交的变更（新文件、修改、删除），如果有，就阻止 Claude Code 停下来，告诉它“你还有活没干完，去提交”。

核心逻辑就这几行：

\`\`\`bash if git diff --quiet && git diff --cached --quiet && \\ \[ -z "$(git ls-files --others --exclude-standard)" \]; then exit 0 # 没变更，正常结束 fi

\`\`\`bash 如果 git diff --quiet && git diff --cached --quiet && \\ \[ -z "$(git ls-files --others --exclude-standard)" \]; 然后 exit 0 # 没变化，正常结束 菲

\# 有变更，拦住它 echo '{"decision": "block", "reason": "检测到未提交的变更，请调用 /commit 技能提交更新。"}' \`\`\`

还有个细节：提交本身也会触发“任务结束”，不处理就无限循环。脚本用 stop\\\_hook\\\_active 标志跳过二次触发。

【2】Commit Skill：让提交有意义

Hook 只管拦截，具体怎么提交靠 Commit Skill。

Skill 是 Claude Code 的技能模块，放在 .claude/skills/ 目录下，用 [http://SKILL.md](https://t.co/05rGqABuRg) 定义工作流程。name 字段自动变成 /slash-command，手动或自动都能触发。相当于一份操作手册，告诉 Claude Code 遇到特定任务该怎么做。

我的 /commit 技能定义了这些规则：

\* 先分析变更文件的路径，判断改的是文章、技能配置还是代码 \* 按主题分组提交，不把所有东西塞进一个 commit。比如改了两篇文章，就分两次提交 \* 自动生成中文 commit message，格式固定：文章用“添加/润色/更新 + 主题”，代码用“优化/修复 + 功能” \* 明确指定提交文件，避免 git add . 这种粗暴操作，排除临时文件和备份文件

这样 git log 里看到的是：

\`\`\` 42257b3 添加 Amodei NYT 访谈整理文章 c4eee96 添加 Peter Steinberger OpenClaw 访谈整理文章 e2a01da 润色 Suleyman FT 专访文章 \`\`\`

每条都说得清楚这次改了什么，不是那种“update files”或者“misc changes”的垃圾信息。

两个机制的配合：Hook 当守门员，保证没有变更被遗漏；Skill 当执行者，保证每次提交都有意义。我再也不用惦记提交这件事了。

\*\*\*

附录：完整配置

【A】Hook 脚本

文件路径：.claude/hooks/auto-commit.sh

\`\`\`bash #!/bin/bash # Stop hook: 任务完成后自动检测未提交变更并触发 commit skill

INPUT=$(cat) STOP\_HOOK\_ACTIVE=$(echo "$INPUT" | jq -r '.stop\_hook\_active // false')

输入=$(cat) STOP\_HOOK\_ACTIVE=$(echo "$INPUT" | jq -r '.stop\_hook\_active // false')

\# 防止无限循环：commit 后再次触发时直接放行 if \[ "$STOP\_HOOK\_ACTIVE" = "true" \]; then exit 0 fi

\# 检查是否有未提交的变更 cd "$CLAUDE\_PROJECT\_DIR" 2>/dev/null || exit 0

\# 检查工作区是否有变更（已修改、新文件等） if git diff --quiet 2>/dev/null && git diff --cached --quiet 2>/dev/null && \[ -z "$(git ls-files --others --exclude-standard 2>/dev/null)" \]; then # 没有变更，正常结束 exit 0 fi

\# 有未提交变更，阻止 Claude 停止，让它继续执行 commit cat <<'EOF' {"decision": "block", "reason": "检测到未提交的变更，请调用 /commit 技能提交更新。"} EOF \`\`\`

【B】Commit Skill

【B】承诺技能

文件路径：.claude/skills/commit/SKILL.md

\`\`\`markdown --- name: commit description: 提交当前未 commit 的修改。自动分析变更内容，生成规范的 commit message，支持按目录分组提交或一次性提交所有修改。 ---

\# Git Commit 技能

\# Git 提交技能

提交当前未 commit 的修改到 git 仓库。

\## 工作流程

\### 步骤一：查看未提交修改

git status --short

分析变更类型： - M - 已修改 - ?? - 新文件（未跟踪） - D - 已删除 - R - 重命名

\### 步骤二：分析变更内容

根据修改文件路径判断变更类型：

| 路径模式 | 变更类型 | |----------|----------| | posts/YYYY-MM-DD/\[slug\]/ | 文章相关 | | .claude/skills/ | 技能配置 | | src/ | 脚本代码 | | .r2-upload-map/ | 资源映射（通常不单独提交） | | 其他 | 项目配置 |

\### 步骤三：决定提交策略

单一主题修改：一次性提交所有文件

多主题修改：按目录/主题分组提交

分组优先级： 1. 文章目录（每篇文章一个 commit） 2. 技能目录（每个技能一个 commit） 3. 代码变更（合并为一个 commit） 4. 配置文件（合并为一个 commit）

\### 步骤四：生成 Commit Message

格式规范： - 用中文 - 简洁描述变更内容 - 不超过 50 字

常用模板： - 文章：添加 \[文章主题简述\]、润色 \[文章标题\]、更新 \[文章标题\] - 技能：添加 \[技能名\] 技能、更新 \[技能名\] 技能 - 代码：优化 \[功能描述\]、修复 \[问题描述\] - 配置：更新项目配置

\### 步骤五：执行提交

git add <file1> <file2> ... git commit -m "commit message"

git 添加 <file1><file2>... git commit -m "提交信息"

注意： - 避免使用 git add . 或 git add -A - 明确指定要提交的文件 - 排除临时文件（.bak-\*、.html.bak-\*）

\### 步骤六：确认结果

git log --oneline -3

输出最近提交记录确认成功。

\## 排除规则

以下文件默认不提交： - \*.bak-\* - 备份文件 - .DS\_Store - macOS 系统文件 - node\_modules/ - 依赖目录 - .r2-upload-map/\*.json - 通常随文章一起提交，除非单独要求 \`\`\`

【C】Hook 配置

【C】钩子配置

文件路径：.claude/settings.local.json（相关部分）

\`\`\`json { "hooks": { "Stop": \[{ "hooks": \[{ "type": "command", "command": "\\"$CLAUDE\_PROJECT\_DIR\\"/.claude/hooks/auto-commit.sh" }\] }\] } } \`\`\`

\`\`\`json { "钩子": { “停止”： \[{ "钩子": \[{ "type": "命令", "命令": "\\"$CLAUDE\_PROJECT\_DIR\\"/.claude/hooks/auto-commit.sh" }\] }\] } } \`\`\`

![图片](https://pbs.twimg.com/media/HBbSCHNWIAE79TQ?format=jpg&name=large)