---
title: "2025-11-19_Stephen4171127_我把_local_mcp_放到_mcp_json里_但是默认用_Claude_danger"
source: "https://x.com/Stephen4171127/status/1990138520502227179"
author:
  - "[[@Stephen4171127]]"
published: 2025-11-19
created: 2025-11-19
description:
tags:
  - "x"
  - "@Stephen4171127"
  - "mcp"
  - "claude"
status: "inbox"
importance: 2
effort: 2
review_level: 0
review_next: "2025-12-10"
review_interval: null
review_count: 0
decision: null
topics: []
links_out: []
summary: ""
pov: ""
actions: []
---

# 我把 local mcp 放到.mcp.json里，但是默认用 Claude --danger...

**熊布朗** @Stephen4171127 [2025-11-16](https://x.com/Stephen4171127/status/1990138520502227179)

我把 local mcp 放到.mcp.json里，但是默认用 Claude --danger... 的时候不预加载。

——

1\. MCP 服务器需要显式批准才能加载

\- .mcp.json 中的服务器不是自动生效的

\- 必须经过用户批准流程

2\. --dangerously-skip-permissions 跳过的是"询问"流程

\- 跳过了批准对话框的显示

\- 但没有自动批准 MCP 服务器

\- 结果：既没有批准流程，也没有 MCP 加载

3\. 批准状态存储在用户配置中

\- MCP 加载依赖于 .claude.json 中的 enabledMcpjsonServers

\- 跳过权限不会自动填充这个字段

————

让我总结一下 MCP 服务器批准机制：

MCP 服务器批准机制

1️⃣ 配置文件层级

.mcp.json (项目共享配置)

↓ 需要用户批准

.claude.json (用户个人配置，按项目存储)

2️⃣ 批准流程

当 Claude Code 首次在项目中发现 .mcp.json 时：

1\. 弹出批准对话框，显示要加载的 MCP 服务器列表

2\. 用户可以选择：

\- ✅ 批准（信任）

\- ❌ 拒绝

3\. 用户的选择被写入 ~/.claude.json 中的项目配置

3️⃣ 存储结构

在 ~/.claude.json 中，每个项目都有自己的配置段：

{

"/path/to/project": {

"mcpServers": {}, // 通过 CLI 添加的 local 范围服务器

"enabledMcpjsonServers": \["server-name-1", "server-name-2"\], // 从 .mcp.json

批准的服务器名称

"disabledMcpjsonServers": \["blocked-server"\], // 从 .mcp.json 拒绝的服务器名称

"hasTrustDialogAccepted": true // 是否接受过项目信任对话框

}

}

4️⃣ 重置批准

claude mcp reset-project-choices

claude mcp 重置项目选择

这个命令会清空所有项目的 enabledMcpjsonServers 和 disabledMcpjsonServers，下次启动时重新提示。

5️⃣ 安全考虑

这个机制是为了防止：

\- 恶意代码通过版本控制注入危险的 MCP 服务器配置

\- 用户无意中执行不信任的远程代码

\- 项目贡献者滥用 MCP 配置权限

所以是的，批准结果存储在 ~/.claude.json，而不是项目的

.mcp.json，这样确保了每个用户可以独立决定是否信任项目提供的 MCP 服务器。