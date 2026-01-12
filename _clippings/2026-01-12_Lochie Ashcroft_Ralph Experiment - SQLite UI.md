---
title: "Ralph Experiment - SQLite UI"
source: "https://lochie.dev/posts/ralph-sqlite-ui/"
author:
  - "[[Lochie Ashcroft]]"
date: "2026-01-12T09:27:23+08:00"
created: 2026-01-12
description: "An experiment using Claude Code with the Ralph technique to build a browser-based SQLite UI"
tags:
  - "Lochie Ashcroft"
---
## Ralph 实验 - SQLite 界面

---

![ralph](https://lochie.dev/sqlite-ui-post/ralph.webp)

## TLDR

- 我利用 Ralph 技术和 Claude 代码，从一份生成的 PRD 中自主地构建了一个基于浏览器的 SQLite 用户界面。
- Claude 逐个处理需求，在几乎没有指导的情况下开发了一个简单的静态应用，并且没有使用任何框架。
- 这种方法效果出奇地好，但速度较慢、token 过多，且在缺乏测试和版本控制的情况下风险较高。
- 更强的防护机制、更短的迭代周期以及更优的项目结构将显著提升可靠性和效率。
- 总体而言，在时间和 token 成本可接受的情况下，Ralph 在无需过多人工干预的新建项目开发中表现有效。

最终结果可在 lochie.dev/sqlite-ui 查看。

## Intro

首先，拉尔夫·维格姆和软件开发有什么关系？

[2025 年 7 月，杰弗里·亨特利首次创造了这个术语](https://ghuntley.com/ralph/)

> Ralph 是一种技术。在最纯粹的形式中，它是一个 Bash 循环。

```sh
while :; do cat PROMPT.md | claude-code ; done
```

> 对于大多数公司的新建项目，Ralph 可以替代大部分外包工作。虽然它存在缺陷，但这些缺陷是可识别的，并且可以通过不同类型的提示词来解决。

本周早些时候，马特·波科克(Matt Pocock)的精彩视频出现在我的信息流里。马特采纳了杰弗里(Geoffrey)的原始想法，并将其调整以适配自己的开发风格。

我强烈推荐观看这个视频。不过，为了总结核心概念，Matt 有效地重现了一个完全由 Claude 驱动的敏捷风格工作流程。

1. 用户故事类需求在创建时需包含名称、描述、成功标准和实施状态。
2. 这些需求被分为一个列表（即“冲刺”）
3. Claude 处理一个单一的需求，独立完成后更新其状态。
4. 重复步骤 3，直到所有需求都得到满足。

Claude 本身被用来定义需求列表。没有明确的依赖映射或优先级排序，这完全由 Claude 在冲刺阶段自行确定。

迭代以 JSON 文件形式存在，该文件包含所有需求及其进度。更新会被持久化存储，既保存在文本文件中，也通过 git 提交，且每次迭代后都会写入这些更新。

## The Experiment

看到我的信息流里全是 Ralph 的热议，我有点 FOMO（错失恐惧症），于是开始构思一个足够复杂却又有趣且切实可行的项目。

一个基于浏览器的 Web 应用程序，用于与 SQLite 数据库交互，感觉非常合适。更好的是，如果它运行得好，我以后就能自己实际使用它了。

这是我第一次使用计划模式的提示：

> 为一款基于浏览器的 SQLite 数据库查看器撰写产品需求文档，该查看器需支持打开 SQLite 数据库文件、显示内容并具备交互性。无需使用前端 JavaScript 框架，只需保持简单、轻量且静态。

这导致了一个相当庞大的需求清单，这些需求被存储在 PRD.md 中。

然后我把那些需求转化为 PRD.json，遵循了 Matt 在他视频中采用的方法：

> 使用 @PRD.md 创建 PRD.json
> 
> 该文件应包含一个功能对象数组，对象的结构如下。请将 PRD 分解为多个小功能。
> 
> | field | description |
> | --- | --- |
> | category | 功能性、非功能性等 |
> | description | 一个关于该功能的简短一句话描述 |
> | steps | 字符串数组，例如：当点击按钮时，颜色改变 |
> | passes | 布尔值，用于表示该功能是否完整且能正常工作 |

总共，这产生了 62 项需求。

如果你感兴趣，可以在下面查看它们：

Click to expand
```json
[
  {
    "category": "functional",
    "description": "User can drag and drop a SQLite file onto the page to open it",
    "steps": [
      "User drags a .db, .sqlite, .sqlite3, or .db3 file over the drop zone",
      "Drop zone visual indicator activates (highlight/border change)",
      "User drops the file",
      "File is read using the File API",
      "Database is loaded into sql.js",
      "UI transitions from empty state to database view"
    ],
    "passes": false
  },
  {
    "category": "functional",
    "description": "User can click a browse button to select a SQLite file",
    "steps": [
      "User clicks the 'Browse Files' button",
      "Native file picker dialog opens",
      "User selects a SQLite file",
      "File is read and loaded into sql.js",
      "UI transitions to database view"
    ],
    "passes": false
  },
  {
    "category": "functional",
    "description": "File name and size are displayed after loading a database",
    "steps": [
      "User loads a SQLite file",
      "File name appears in the header or info area",
      "File size is displayed in human-readable format (KB/MB)"
    ],
    "passes": false
  },
  {
    "category": "functional",
    "description": "All tables in the database are listed in a sidebar",
    "steps": [
      "Database is loaded",
      "Query sqlite_master for all tables",
      "Table names are rendered in a sidebar list",
      "List is scrollable if many tables exist"
    ],
    "passes": false
  },
  {
    "category": "functional",
    "description": "Each table in the sidebar shows its row count",
    "steps": [
      "Tables are listed in sidebar",
      "For each table, execute COUNT(*) query",
      "Row count is displayed next to table name"
    ],
    "passes": false
  },
  {
    "category": "functional",
    "description": "Clicking a table name loads and displays its contents",
    "steps": [
      "User clicks on a table name in the sidebar",
      "Table becomes visually selected/highlighted",
      "SELECT query executes for that table",
      "Results display in the data viewer panel"
    ],
    "passes": false
  },
  {
    "category": "functional",
    "description": "Column names and types are shown in table headers",
    "steps": [
      "Table data is displayed",
      "Header row shows column names",
      "Column data types are visible (as subtitle or tooltip)"
    ],
    "passes": false
  },
  {
    "category": "functional",
    "description": "Table data is paginated with configurable page size",
    "steps": [
      "Table with more rows than page size is selected",
      "Only first page of results is shown",
      "Pagination controls appear below the table",
      "Current page number and total pages are displayed"
    ],
    "passes": false
  },
  {
    "category": "functional",
    "description": "User can change the number of rows per page",
    "steps": [
      "Page size dropdown/selector is visible",
      "User selects a different page size (25, 50, 100, or 500)",
      "Table refreshes with new number of rows",
      "Pagination updates to reflect new total pages"
    ],
    "passes": false
  },
  {
    "category": "functional",
    "description": "User can navigate between pages using pagination controls",
    "steps": [
      "User clicks 'Next' button",
      "Next page of results loads",
      "User clicks 'Previous' button",
      "Previous page loads",
      "User can click specific page number to jump to it"
    ],
    "passes": false
  },
  {
    "category": "functional",
    "description": "Clicking a column header sorts the table by that column",
    "steps": [
      "User clicks on a column header",
      "Table sorts by that column in ascending order",
      "Sort indicator (arrow) appears on the column",
      "User clicks same header again",
      "Sort order toggles to descending",
      "Sort indicator updates to show descending"
    ],
    "passes": false
  },
  {
    "category": "functional",
    "description": "NULL values are displayed with distinct styling",
    "steps": [
      "Table contains NULL values",
      "NULL cells display 'NULL' text or placeholder",
      "NULL cells have distinct visual styling (italic, gray, etc.)"
    ],
    "passes": false
  },
  {
    "category": "functional",
    "description": "BLOB data shows a size indicator instead of raw content",
    "steps": [
      "Table contains BLOB columns",
      "BLOB cells display type indicator (e.g., 'BLOB')",
      "BLOB size is shown (e.g., '1.2 KB')",
      "Raw binary data is not rendered as text"
    ],
    "passes": false
  },
  {
    "category": "functional",
    "description": "SQL query editor text area is available for custom queries",
    "steps": [
      "Query editor panel is visible in the UI",
      "Text area accepts user input",
      "User can type SQL queries",
      "Text area supports multi-line input"
    ],
    "passes": false
  },
  {
    "category": "functional",
    "description": "User can execute a query by clicking the Run button",
    "steps": [
      "User types a SQL query in the editor",
      "User clicks the 'Run' button",
      "Query is executed against the database",
      "Results appear in the data viewer"
    ],
    "passes": false
  },
  {
    "category": "functional",
    "description": "User can execute a query with Ctrl+Enter keyboard shortcut",
    "steps": [
      "User types a SQL query in the editor",
      "User presses Ctrl+Enter (or Cmd+Enter on Mac)",
      "Query executes",
      "Results display in the data viewer"
    ],
    "passes": false
  },
  {
    "category": "functional",
    "description": "Query results display in the same table format as table browsing",
    "steps": [
      "User executes a custom SQL query",
      "Results render in the data table component",
      "Column headers show result column names",
      "Pagination works for query results"
    ],
    "passes": false
  },
  {
    "category": "functional",
    "description": "Invalid SQL queries show an error message",
    "steps": [
      "User types an invalid SQL query",
      "User executes the query",
      "Error message is displayed",
      "Error message includes the SQL error description",
      "Previous results remain visible or cleared gracefully"
    ],
    "passes": false
  },
  {
    "category": "functional",
    "description": "SQL editor has basic syntax highlighting",
    "steps": [
      "User types SQL in the editor",
      "SQL keywords (SELECT, FROM, WHERE, etc.) are highlighted",
      "String literals are highlighted in a different color",
      "Numbers are highlighted distinctly"
    ],
    "passes": false
  },
  {
    "category": "ui",
    "description": "Wide tables scroll horizontally",
    "steps": [
      "Table with many columns is displayed",
      "Table container shows horizontal scrollbar",
      "User can scroll left/right to see all columns"
    ],
    "passes": false
  },
  {
    "category": "ui",
    "description": "Table header row remains sticky when scrolling vertically",
    "steps": [
      "Table with many rows is displayed",
      "User scrolls down in the table",
      "Header row stays fixed at the top",
      "Column names remain visible while scrolling"
    ],
    "passes": false
  },
  {
    "category": "ui",
    "description": "Long cell values are truncated with ellipsis",
    "steps": [
      "Cell contains text longer than column width",
      "Text is truncated with ellipsis (...)",
      "Column maintains consistent width"
    ],
    "passes": false
  },
  {
    "category": "ui",
    "description": "Hovering over truncated cells shows full content in tooltip",
    "steps": [
      "Cell has truncated content",
      "User hovers over the cell",
      "Tooltip appears with full cell value",
      "Tooltip disappears when mouse leaves"
    ],
    "passes": false
  },
  {
    "category": "ui",
    "description": "Empty state is shown when no database is loaded",
    "steps": [
      "Application loads without a file",
      "Drop zone with instructions is displayed",
      "SQLite icon or graphic is shown",
      "Supported file formats are listed",
      "Privacy message about local data is shown"
    ],
    "passes": false
  },
  {
    "category": "ui",
    "description": "Application header displays logo and title",
    "steps": [
      "Page loads",
      "Header is visible at top of page",
      "Logo/icon is displayed",
      "'SQLite UI' title is shown"
    ],
    "passes": false
  },
  {
    "category": "functional",
    "description": "Quick filter input filters visible table rows",
    "steps": [
      "Table data is displayed",
      "Filter input field is visible above the table",
      "User types in the filter input",
      "Rows not matching the filter text are hidden",
      "Matching rows remain visible",
      "Clearing filter shows all rows again"
    ],
    "passes": false
  },
  {
    "category": "functional",
    "description": "User can export current view to CSV",
    "steps": [
      "Table data is displayed",
      "User clicks 'Export CSV' button",
      "CSV file is generated with current view data",
      "Browser downloads the CSV file"
    ],
    "passes": false
  },
  {
    "category": "functional",
    "description": "User can export current view to JSON",
    "steps": [
      "Table data is displayed",
      "User clicks 'Export JSON' button",
      "JSON file is generated with current view data",
      "Browser downloads the JSON file"
    ],
    "passes": false
  },
  {
    "category": "functional",
    "description": "User can copy cell value to clipboard",
    "steps": [
      "User clicks on a cell or uses context menu",
      "Copy option is available",
      "Cell value is copied to clipboard",
      "Visual feedback confirms copy action"
    ],
    "passes": false
  },
  {
    "category": "functional",
    "description": "Query history stores executed queries in localStorage",
    "steps": [
      "User executes a SQL query",
      "Query is saved to localStorage",
      "Query history persists after page reload",
      "Last N queries are retained (older ones removed)"
    ],
    "passes": false
  },
  {
    "category": "functional",
    "description": "User can re-run queries from history dropdown",
    "steps": [
      "User opens query history dropdown",
      "Previous queries are listed",
      "User clicks on a historical query",
      "Query populates in the editor",
      "Query can be executed"
    ],
    "passes": false
  },
  {
    "category": "functional",
    "description": "User can clear query history",
    "steps": [
      "Query history contains entries",
      "User clicks 'Clear History' option",
      "Confirmation prompt appears (optional)",
      "History is cleared from localStorage",
      "History dropdown shows empty state"
    ],
    "passes": false
  },
  {
    "category": "functional",
    "description": "Foreign key columns show a visual indicator",
    "steps": [
      "Table with foreign key constraints is selected",
      "Columns with FK constraints have an icon or badge",
      "FK indicator distinguishes FK columns from regular columns"
    ],
    "passes": false
  },
  {
    "category": "functional",
    "description": "Clicking a foreign key value navigates to the referenced row",
    "steps": [
      "Cell in a FK column is clicked",
      "Referenced table is loaded",
      "View jumps to the referenced row",
      "Referenced row is highlighted"
    ],
    "passes": false
  },
  {
    "category": "functional",
    "description": "Dark mode can be toggled via UI control",
    "steps": [
      "Theme toggle button is visible in header",
      "User clicks the toggle",
      "UI switches between light and dark themes",
      "All components update to new theme colors"
    ],
    "passes": false
  },
  {
    "category": "functional",
    "description": "Dark mode respects system preference by default",
    "steps": [
      "User has system dark mode enabled",
      "Application loads",
      "Dark theme is applied automatically",
      "User with light system preference sees light theme"
    ],
    "passes": false
  },
  {
    "category": "functional",
    "description": "Theme preference is persisted in localStorage",
    "steps": [
      "User toggles theme",
      "Preference is saved to localStorage",
      "User reloads the page",
      "Previously selected theme is applied"
    ],
    "passes": false
  },
  {
    "category": "non-functional",
    "description": "Page loads in under 500ms",
    "steps": [
      "User navigates to the application URL",
      "HTML, CSS, and critical JS load",
      "Initial UI renders within 500ms",
      "Empty state is interactive"
    ],
    "passes": false
  },
  {
    "category": "non-functional",
    "description": "sql.js WebAssembly module loads in under 1 second",
    "steps": [
      "Page load initiates WASM fetch",
      "sql-wasm.wasm file downloads",
      "WASM module compiles and initializes",
      "Total time is under 1 second on broadband"
    ],
    "passes": false
  },
  {
    "category": "non-functional",
    "description": "10MB database file opens in under 2 seconds",
    "steps": [
      "User loads a 10MB SQLite file",
      "File is read into memory",
      "sql.js initializes the database",
      "Table list is populated",
      "Total time is under 2 seconds"
    ],
    "passes": false
  },
  {
    "category": "non-functional",
    "description": "Simple SELECT queries execute in under 100ms",
    "steps": [
      "Database is loaded",
      "User runs a simple SELECT query",
      "Query executes and returns results",
      "Results render in under 100ms total"
    ],
    "passes": false
  },
  {
    "category": "non-functional",
    "description": "Warning is shown for files over 100MB",
    "steps": [
      "User attempts to load a file larger than 100MB",
      "Warning message is displayed",
      "User can choose to proceed or cancel",
      "File loads if user confirms"
    ],
    "passes": false
  },
  {
    "category": "non-functional",
    "description": "Files over 500MB are rejected with an error",
    "steps": [
      "User attempts to load a file larger than 500MB",
      "Error message is displayed",
      "File is not loaded",
      "Application remains functional"
    ],
    "passes": false
  },
  {
    "category": "non-functional",
    "description": "Loading progress is shown for files over 10MB",
    "steps": [
      "User loads a file larger than 10MB",
      "Progress indicator appears",
      "Progress updates as file loads",
      "Progress indicator disappears when complete"
    ],
    "passes": false
  },
  {
    "category": "non-functional",
    "description": "Application uses semantic HTML elements",
    "steps": [
      "Page uses appropriate semantic tags",
      "Tables use <table>, <thead>, <tbody>, <th>, <td>",
      "Navigation uses <nav>",
      "Main content uses <main>",
      "Buttons use <button> elements"
    ],
    "passes": false
  },
  {
    "category": "non-functional",
    "description": "Interactive elements have ARIA labels",
    "steps": [
      "Buttons have aria-label or visible text",
      "Icon-only buttons have descriptive aria-labels",
      "Form inputs have associated labels",
      "Status messages use aria-live regions"
    ],
    "passes": false
  },
  {
    "category": "non-functional",
    "description": "Application is keyboard navigable",
    "steps": [
      "User can Tab through all interactive elements",
      "Focus indicators are visible",
      "Enter/Space activates buttons",
      "Escape closes modals/dropdowns"
    ],
    "passes": false
  },
  {
    "category": "non-functional",
    "description": "Color contrast meets WCAG AA standards",
    "steps": [
      "Text has minimum 4.5:1 contrast ratio against background",
      "Large text has minimum 3:1 contrast ratio",
      "Interactive elements are distinguishable",
      "Both light and dark themes meet contrast requirements"
    ],
    "passes": false
  },
  {
    "category": "non-functional",
    "description": "No data is transmitted to external servers",
    "steps": [
      "User loads and queries a database",
      "Network tab shows no external requests with user data",
      "All processing happens client-side",
      "Only static assets are fetched from hosting server"
    ],
    "passes": false
  },
  {
    "category": "non-functional",
    "description": "User input displayed in UI is properly sanitized",
    "steps": [
      "Database contains potentially malicious content (script tags, etc.)",
      "Data is displayed in the table",
      "No scripts execute",
      "HTML entities are properly escaped"
    ],
    "passes": false
  },
  {
    "category": "non-functional",
    "description": "Application works in Chrome 80+",
    "steps": [
      "Application is opened in Chrome 80 or later",
      "All features function correctly",
      "No console errors related to unsupported APIs"
    ],
    "passes": false
  },
  {
    "category": "non-functional",
    "description": "Application works in Firefox 75+",
    "steps": [
      "Application is opened in Firefox 75 or later",
      "All features function correctly",
      "No console errors related to unsupported APIs"
    ],
    "passes": false
  },
  {
    "category": "non-functional",
    "description": "Application works in Safari 14+",
    "steps": [
      "Application is opened in Safari 14 or later",
      "All features function correctly",
      "No console errors related to unsupported APIs"
    ],
    "passes": false
  },
  {
    "category": "non-functional",
    "description": "Application works in Edge 80+",
    "steps": [
      "Application is opened in Edge 80 or later",
      "All features function correctly",
      "No console errors related to unsupported APIs"
    ],
    "passes": false
  },
  {
    "category": "ui",
    "description": "Sidebar is resizable or has appropriate fixed width",
    "steps": [
      "Sidebar displays table list",
      "Sidebar has reasonable width for table names",
      "Long table names are truncated or sidebar scrolls horizontally"
    ],
    "passes": false
  },
  {
    "category": "ui",
    "description": "Selected table is visually highlighted in sidebar",
    "steps": [
      "User clicks on a table in the sidebar",
      "Selected table has distinct background or border",
      "Selection is clearly visible",
      "Previous selection is deselected"
    ],
    "passes": false
  },
  {
    "category": "ui",
    "description": "Table name and row count displayed above data viewer",
    "steps": [
      "User selects a table",
      "Table name appears above the data grid",
      "Row count is displayed (e.g., '1,234 rows')"
    ],
    "passes": false
  },
  {
    "category": "ui",
    "description": "Query editor panel is collapsible or togglable",
    "steps": [
      "Query editor panel has expand/collapse control",
      "User clicks to collapse the panel",
      "Panel minimizes to save space",
      "User can expand it again"
    ],
    "passes": false
  },
  {
    "category": "functional",
    "description": "First column can be made sticky via toggle",
    "steps": [
      "Toggle for sticky first column is available",
      "User enables the toggle",
      "First column remains fixed when scrolling horizontally",
      "User can disable to return to normal scrolling"
    ],
    "passes": false
  },
  {
    "category": "functional",
    "description": "Column-specific filtering allows filtering by individual columns",
    "steps": [
      "User opens column filter options",
      "User can select which column to filter",
      "User enters filter value",
      "Only rows matching that column's filter are shown"
    ],
    "passes": false
  },
  {
    "category": "functional",
    "description": "User can copy entire row to clipboard",
    "steps": [
      "User selects a row or uses row context menu",
      "Copy row option is available",
      "Row data is copied as tab-separated or JSON",
      "Visual feedback confirms copy"
    ],
    "passes": false
  },
  {
    "category": "functional",
    "description": "Foreign key relationships are shown in schema info",
    "steps": [
      "User views table schema/structure",
      "FK relationships are listed",
      "Referenced table and column are displayed"
    ],
    "passes": false
  }
]
```

有了我的 Ralph 脚本，我准备好大干一场了。

```bash
#!/bin/bash

set -e

if [ -z "$1" ]; then
  echo "Usage: $0 {iterations}"
  exit 1
fi

for ((i=1; i<=$1; i++)); do
  echo "Iteration: $i"
  echo "---------------------------------------"
  result=$(claude --permission-mode acceptEdits -p "@PRD.json @progress.txt \
1. Find the highest-priority feature to work on and work only on that feature. \
2. Check that the tests pass. \
3. Update the PRD (PRD.json) with the work that was done. \
4. Append your progress to the progress.txt file. \
ONLY WORK ON A SINGLE FEATURE
If, while implementing the feature, you notice the PRD is complete, output <promise>COMPLETE</promise>. \
")

  echo "$result"

  if [[ "$result" == *"<promise>COMPLETE</promise>"* ]]; then
    echo "PRD COMPLETE"
    exit 0
  fi
done
```

我每次运行脚本时执行 10 次迭代。每次迭代都会阻塞且无输出，因此我每次都急切等待完成。

我的方法没有 Git 历史记录。我当时真是在冒险行事。每次迭代后，我都依赖 `progress.txt` 文件查看变更，同时刷新浏览器检查是否有东西出问题。令我惊讶的是，一切都进展得相当顺利，应用程序很快就开始具备一个功能齐全的数据库 UI 的雏形了。

我无法一次性完成所有需求。随着功能不断增加，token 使用量大幅上升，最终我用了大约两天时间完成了这个实验。

一旦所有原始需求都实现完毕，我就忍不住开始要求更多功能，包括：

- 显示表的存储大小
- 对查询执行 `EXPLAIN`
- 显示查询执行时长
- 交互式行编辑
- 保存更新后的数据库
- Index management
- Schema diagrams
- …and more

在那个时候，我已经从一名工程师变成了一个过于兴奋的产品经理，我刚刚发现了一名全天候工作的软件工程师，他从不拒绝，而且没有底气去抵制范围蔓延。

## The Final Result

你可以在这里试用一下 lochie.dev/sqlite-ui

![schema](https://lochie.dev/sqlite-ui-post/schema.webp)

![data](https://lochie.dev/sqlite-ui-post/data.webp)

## Reflections

使用极简的提示，我就能生成一份完整的需求清单，并直接让 Claude 投入工作。结果大体上符合我的预期，但考虑到提示很简短，仍然令人印象深刻。

我要求一个简单的静态实现，而我得到的正是这样的结果——单个 HTML、CSS 和 JavaScript 文件。唯一的外部依赖是 sql-wasm。Claude 构建了一个坚实的基础，这个基础可以进一步扩展。

最初显示表的存储大小时遇到了问题。克劳德指出，由于 sql-wasm 使用的编译标志，在实现过程中这可能会无法正常工作。我自己用 `SQLITE_ENABLE_DBSTAT_VTAB` 重新构建了它，更新 HTML 以指向我的构建产物，并通过 HTTP 服务器提供这些文件（WASM 加载所必需），之后一切都正常运行，无需再做任何代码修改。

一些不足变得显而易见：

- Claude 运行时没有明显的中间输出，所以很难判断它是卡住了还是只是运行缓慢。
- 没有编写任何测试。（没有被提示，Claude 认为这没必要。）
- 这个项目没有进行版本控制。
- 我很幸运，没出什么大问题。

不过，这次成功并不意外。Ralph 本质上把 Claude 变成一名专注的软件工程师，让他执行由项目经理定义的冲刺。没有上下文切换，一次只处理一个故事。

话虽如此，这种方法速度不快，还会消耗大量的 token。这显然是速度与准确性之间的权衡。如果你有时间，并且觉得成本值得，像这样自主构建一个项目是有道理的，尤其是当它能在你睡觉时还默默运行的时候。

## Future Improvements

根据以往经验，Claude 在约束更强、指引更明确的情况下表现明显更佳。虽然 Ralph loop 在设置最少时效果出乎意料地好，但这次实验却凸显了几个方面，在这些方面采用更刻意的结构设计会更有成效。

### 防护措施和项目结构

下次我会做不同的事：

- 创建一个定义明确的 `CLAUDE.md` ，用于记录项目规范、架构、约束条件和期望。
- 采用结构化的多文件项目布局，而非单一的、持续增长的 JavaScript 文件。
- 从一开始就添加 Git 来保存进度，通过提交历史进行检查，并在 Claude 陷入无法恢复的状态时允许回滚。
- 添加大量测试。对于 Web 应用，Playwright 是个不错的选择，可以自动捕捉功能和视觉回归问题。

由于 Ralph 的每次迭代都在全新的 Claude Code 会话中进行，大量时间和 token 被用于重新加载和重新理解项目上下文。更优的结构、更明确的规范以及自动化测试将显著降低这一开销，并提升迭代质量。

### 更短的冲刺与提前规划

冲刺的规模也很重要。62 个功能点在一个冲刺里实在太多了，Claude 需要做大量的分析才能决定下一步该做什么。

一种选择是手动确定故事范围、定义关系并提前分配优先级。然而，更有趣的工作流程是让 Claude 自行处理那个规划步骤。

- 从完整的需求集合开始
- 让 Claude 将它们拆分为多个更小的冲刺周期，并提前规划几个冲刺周期，就像现实中的敏捷流程一样。
- 独立执行每个冲刺

通过这种方法，Ralph 脚本可以扩展以使用嵌套循环：遍历冲刺，然后遍历每个冲刺中的故事。这将减少因反复扫描完整需求集而浪费的上下文，并允许 Claude 自主运行更长时间。

更进一步，这个模型甚至可以扩展到多个“软件工程师”（多个 Claude 实例）并行协作，由更高层级的编排层进行协调。

## Conclusion

我觉得这个实验很成功。

我开发了一个真正有用、不会被弃置的东西，在实践中深入了解了拉尔夫技术，现在对将其应用到未来的项目中充满信心。

我很期待能再次尝试它，这次会有更完善的防护、测试和版本控制机制。