---
title: "Ryan Carson on X: "Step-by-step guide to get Ralph working and shipping code" / X"
source: "https://x.com/ryancarson/status/2008548371712135632"
author: ""
created: 2026-01-12 09:27:57
date: 2026-01-12 09:27:57
description: ""
tags: ""
---
Ralph 是一个自主的 AI 编码循环，能在你睡觉时发布功能。

由……创建 并宣布它运行 （或您选择的代理人）反复执行，直到所有任务完成。

每次迭代都是一个全新的上下文窗口（让 Threads 保持简洁小巧）。数据通过 git 历史记录和文本文件得以持久化。

我昨晚第一次运行它，还上线了一个功能。我太喜欢了。

Ryan Carson

![](https://pbs.twimg.com/profile_images/1995950801706254336/0MorviXJ_bigger.jpg)

[

![Image](https://pbs.twimg.com/media/G981xxqW0AAJvcc?format=jpg&name=medium)



](https://x.com/ryancarson/status/2008383176339579040/photo/1)

引用

Ryan Carson

![](https://pbs.twimg.com/profile_images/1995950801706254336/0MorviXJ_bigger.jpg)

![Willy Wonka Suspense GIF](https://pbs.twimg.com/tweet_video_thumb/G98lIC-W8AAlsfa?format=jpg&name=360x360)

今晚要在 Amp 上开启一个 Ralph 会话，看看它能不能在我睡觉的时候构建出一个相当完整的功能。 现在正在和 Amp 聊天，一起构建这个 PR，我们会用它来填充用户故事的 JSON。 然后我会开始脚本，然后去睡觉。

1.  将提示词输入到你的 AI 代理中
    
2.  代理从 prd.json 中挑选下一个故事
    
3.  代理实现它
    
4.  Agent 运行类型检查 + 测试
    
5.  如果通过，Agent 提交
    
6.  代理标记故事完成
    
7.  Agent 记录学习内容
    
8.  循环重复直到完成
    

-   Git 提交
    
-   progress.txt（心得）
    
-   prd.json（任务状态）
    

```
scripts/ralph/
├── ralph.sh
├── prompt.md
├── prd.json
└── progress.txt
```

```
#!/bin/bash
set -e

MAX_ITERATIONS=${1:-10}
SCRIPT_DIR="$(cd "$(dirname \
  "${BASH_SOURCE[0]}")" && pwd)"

echo "🚀 Starting Ralph"

for i in $(seq 1 $MAX_ITERATIONS); do
  echo "═══ Iteration $i ═══"
  
  OUTPUT=$(cat "$SCRIPT_DIR/prompt.md" \
    | amp --dangerously-allow-all 2>&1 \
    | tee /dev/stderr) || true
  
  if echo "$OUTPUT" | \
    grep -q "<promise>COMPLETE</promise>"
  then
    echo "✅ Done!"
    exit 0
  fi
  
  sleep 2
done

echo "⚠️ Max iterations reached"
exit 1
```

```
chmod +x scripts/ralph/ralph.sh
```

-   Claude 代码: \`claude --dangerously-skip-permissions\`
    

```
# Ralph Agent Instructions

## Your Task

1. Read `scripts/ralph/prd.json`
2. Read `scripts/ralph/progress.txt`
   (check Codebase Patterns first)
3. Check you're on the correct branch
4. Pick highest priority story 
   where `passes: false`
5. Implement that ONE story
6. Run typecheck and tests
7. Update AGENTS.md files with learnings
8. Commit: `feat: [ID] - [Title]`
9. Update prd.json: `passes: true`
10. Append learnings to progress.txt

## Progress Format

APPEND to progress.txt:

## [Date] - [Story ID]
- What was implemented
- Files changed
- **Learnings:**
  - Patterns discovered
  - Gotchas encountered
---

## Codebase Patterns

Add reusable patterns to the TOP 
of progress.txt:

## Codebase Patterns
- Migrations: Use IF NOT EXISTS
- React: useRef<Timeout | null>(null)

## Stop Condition

If ALL stories pass, reply:
<promise>COMPLETE</promise>

Otherwise end normally.
```

```
{
  "branchName": "ralph/feature",
  "userStories": [
    {
      "id": "US-001",
      "title": "Add login form",
      "acceptanceCriteria": [
        "Email/password fields",
        "Validates email format",
        "typecheck passes"
      ],
      "priority": 1,
      "passes": false,
      "notes": ""
    }
  ]
}
```

-   \`branchName\` — 使用的分支
    
-   优先级 — 越低越优先
    
-   \`passes\` — 设置为 true 当完成时
    

```
# Ralph Progress Log
Started: 2024-01-15

## Codebase Patterns
- Migrations: IF NOT EXISTS
- Types: Export from actions.ts

## Key Files
- db/schema.ts
- app/auth/actions.ts
---
```

```
./scripts/ralph/ralph.sh 25
```

-   创建功能分支
    
-   逐个完成故事
    
-   每次之后提交
    
-   全部通过即停止
    

使用 Ralph 的另一个绝佳方式是在浏览器中进行大量用户测试。我会创建 10-20 个详细的用户测试场景（我明确规定所有验收标准必须能通过 Amp 使用 Chrome 开发者工具（Dev Tools）与人工对比的方式进行判断），然后我把它们放在一个...

```
❌ Too big:
> "Build entire auth system"
✅ Right size:
> "Add login form"
> "Add email validation"
> "Add auth server action"
```

-   \`npm 执行类型检查\`
    
-   \`npm test\`
    

```
❌ Vague:
> "Users can log in"
✅ Explicit:
> - Email/password fields
> - Validates email format
> - Shows error on failure
> - typecheck passes
> - Verify at localhost:$PORT/login (PORT defaults to 3000)
```

到第10个故事时，拉尔夫已经了解了1到9个故事里的规律。

1.  progress.txt — 会话内存 for Ralph 迭代
    

提交前，Ralph 更新 AGENTS.md 以及目录中与已编辑文件相关的文件，如果发现可复用的模式（注意事项、约定、依赖项）。

```
✅ Good additions:
- "When modifying X, also update Y"
- "This module uses pattern Z"
- "Tests require dev server running"
❌ Don't add:
- Story-specific details
- Temporary notes
- Info already in progress.txt
```

对于界面变更，请使用由 @sawyerhood 提供的开发浏览器技能。使用 \`加载开发浏览器技能\` 来加载它，然后：

```
# Start the browser server
~/.config/amp/skills/dev-browser/server.sh &
# Wait for "Ready" message

# Write scripts using heredocs
cd ~/.config/amp/skills/dev-browser && npx tsx <<'EOF'
import { connect, waitForPageLoad } from "@/client.js";

const client = await connect();
const page = await client.page("test");
await page.setViewportSize({ width: 1280, height: 900 });
const port = process.env.PORT || "3000";
await page.goto(`http://localhost:${port}/your-page`);
await waitForPageLoad(page);
await page.screenshot({ path: "tmp/screenshot.png" });
await client.disconnect();
EOF
```

```
ADD COLUMN IF NOT EXISTS email TEXT;
```

```
echo -e "\n\n\n" | npm run db:generate
```

-   服务器操作
    
-   用户界面组件
    
-   API 路由
    

如果类型检查需要其他修改，就做这些修改。不是范围蔓延。

```
# Story status
cat scripts/ralph/prd.json | \
jq '.userStories[] | {id, passes}'
# Learnings
cat scripts/ralph/progress.txt
# Commits
git log --oneline -10
```

-   13用户故事
    
-   约15次迭代
    
-   每个2到5分钟
    
-   总共约1小时
    

经验会累积。到第10个故事时，拉尔夫已经了解我们的模式。

-   探索性工作
    
-   无标准的大规模重构
    
-   安全关键代码
    
-   需要人工审核的内容
    

想了解如何使用 Ralph 的精彩视频教程，看看@mattpocockuk 的视频...

我的拉尔夫·维格姆式崩溃火了。 这是一种简单至上的 AI 编程方法，能让你在睡觉时也能发布产品。 所以这里有完整的解释、示例代码和演示。

![](https://pbs.twimg.com/amplify_video_thumb/2008199065901703168/img/RL13KJK9DQjyi8iI.jpg)