---
title: 2026-01-09_借助 Claude 智能体 SDK 构建智能体的完全指南
source: https://x.com/dabit3/article/2009131298250428923
author:
  - ""
created: 2026-01-09 18:18:17
date: 2026-01-09 18:18:17
description: ""
tags:
---
如果你用过 Claude Code，你就会看到 AI 代理实际能做什么：读取文件、运行命令、编辑代码、弄清楚完成任务的步骤。

而且你知道，它不只是帮你写代码，还会主动负责解决问题，就像一个考虑周全的工程师会做的那样。

这个 是同一个引擎，由你指向任何你想要解决的问题，因此你可以轻松构建自己的代理。

这是 Claude Code 背后的基础设施，以库的形式提供。你能获得代理循环、内置工具、上下文管理，基本上是你原本需要自己构建的一切。

本指南将一步步讲解如何从零开始构建一个代码审查代理。最终，你会拥有一个能够分析代码库、发现漏洞和安全问题并给出结构化反馈的代理。

更重要的是，你会理解 SDK 是如何工作的，这样你就能构建你真正需要的任何东西。

1.  分析代码库中的漏洞和安全问题
    
2.  读取文件并自主搜索代码
    
3.  提供结构化、可操作的反馈
    
4.  跟踪它工作时的进展
    

运行时 - Claude 代码 CLI • SDK - @anthropic-ai/claude-agent-sdk • 语言 - TypeScript 模型 - Claude Opus 4.5

如果你用过原始 API 构建代理，你肯定知道这个模式：调用模型，检查它是否需要调用工具，执行工具，将结果反馈回去，重复直到完成。当构建任何复杂的东西时，这会变得很繁琐。

```
// Without the SDK: You manage the loop
let response = await client.messages.create({...});
while (response.stop_reason === "tool_use") {
  const result = yourToolExecutor(response.tool_use);
  response = await client.messages.create({ tool_result: result, ... });
}

// With the SDK: Claude manages it
for await (const message of query({ prompt: "Fix the bug in auth.py" })) {
  console.log(message); // Claude reads files, finds bugs, edits code
}
```

• 读取 - 读取任何工作目录中的文件 • 写入 - 创建新文件 • 编辑 - 对现有文件进行精确编辑 • Bash - 运行终端命令 • Glob - 按模式查找文件 Grep - 使用正则表达式搜索文件内容 WebSearch - 搜索网页 • WebFetch - 获取并解析网页

1.  已安装 Node.js 18+
    
2.  一个 Anthropic API 密钥（）
    

该 Agent SDK 以 Claude 代码作为其运行时：

```
npm install -g @anthropic-ai/claude-code
```

安装完成后，在你的终端中运行 claude 并按照提示进行身份验证。

```
mkdir code-review-agent && cd code-review-agent
npm init -y
npm install @anthropic-ai/claude-agent-sdk
npm install -D typescript @types/node tsx
```

```
export ANTHROPIC_API_KEY=your-api-key
```

```
import { query } from "@anthropic-ai/claude-agent-sdk";

async function main() {
  for await (const message of query({
    prompt: "What files are in this directory?",
    options: {
      model: "opus",
      allowedTools: ["Glob", "Read"],
      maxTurns: 250
    }
  })) {
    if (message.type === "assistant") {
      for (const block of message.message.content) {
        if ("text" in block) {
          console.log(block.text);
        }
      }
    }
    
    if (message.type === "result") {
      console.log("\nDone:", message.subtype);
    }
  }
}

main();
```

Claude 会使用 Glob 工具来列出文件并告诉你它发现了什么。

The 查询() 函数返回一个异步生成器，当 Claude 工作时流式传输消息。以下是关键的消息类型：

```
for await (const message of query({ prompt: "..." })) {
  switch (message.type) {
    case "system":
      // Session initialization info
      if (message.subtype === "init") {
        console.log("Session ID:", message.session_id);
        console.log("Available tools:", message.tools);
      }
      break;
      
    case "assistant":
      // Claude's responses and tool calls
      for (const block of message.message.content) {
        if ("text" in block) {
          console.log("Claude:", block.text);
        } else if ("name" in block) {
          console.log("Tool call:", block.name);
        }
      }
      break;
      
    case "result":
      // Final result
      console.log("Status:", message.subtype); // "success" or error type
      console.log("Cost:", message.total_cost_usd);
      break;
  }
}
```

现在让我们构建一些有用的东西。创建 review-agent.ts:

```
import { query } from "@anthropic-ai/claude-agent-sdk";

async function reviewCode(directory: string) {
  console.log(`\n🔍 Starting code review for: ${directory}\n`);
  
  for await (const message of query({
    prompt: `Review the code in ${directory} for:
1. Bugs and potential crashes
2. Security vulnerabilities  
3. Performance issues
4. Code quality improvements

Be specific about file names and line numbers.`,
    options: {
      model: "opus",
      allowedTools: ["Read", "Glob", "Grep"],
      permissionMode: "bypassPermissions", // Auto-approve read operations
      maxTurns: 250
    }
  })) {
    // Show Claude's analysis as it happens
    if (message.type === "assistant") {
      for (const block of message.message.content) {
        if ("text" in block) {
          console.log(block.text);
        } else if ("name" in block) {
          console.log(`\n📁 Using ${block.name}...`);
        }
      }
    }
    
    // Show completion status
    if (message.type === "result") {
      if (message.subtype === "success") {
        console.log(`\n✅ Review complete! Cost: $${message.total_cost_usd.toFixed(4)}`);
      } else {
        console.log(`\n❌ Review failed: ${message.subtype}`);
      }
    }
  }
}

// Review the current directory
reviewCode(".");
```

创建一个带有一些故意问题的文件。创建 example.ts：

```
function processUsers(users: any) {
  for (let i = 0; i <= users.length; i++) { // Off-by-one error
    console.log(users[i].name.toUpperCase()); // No null check
  }
}

function connectToDb(password: string) {
  const connectionString = `postgres://admin:${password}@localhost/db`;
  console.log("Connecting with:", connectionString); // Logging sensitive data
}

async function fetchData(url) { // Missing type annotation
  const response = await fetch(url);
  return response.json(); // No error handling
}
```

Claude 将识别漏洞、安全问题，并提出修复建议。

在编程使用中，你会需要结构化数据。SDK 支持 JSON Schema 输出：

```
import { query } from "@anthropic-ai/claude-agent-sdk";

const reviewSchema = {
  type: "object",
  properties: {
    issues: {
      type: "array",
      items: {
        type: "object",
        properties: {
          severity: { type: "string", enum: ["low", "medium", "high", "critical"] },
          category: { type: "string", enum: ["bug", "security", "performance", "style"] },
          file: { type: "string" },
          line: { type: "number" },
          description: { type: "string" },
          suggestion: { type: "string" }
        },
        required: ["severity", "category", "file", "description"]
      }
    },
    summary: { type: "string" },
    overallScore: { type: "number" }
  },
  required: ["issues", "summary", "overallScore"]
};

async function reviewCodeStructured(directory: string) {
  for await (const message of query({
    prompt: `Review the code in ${directory}. Identify all issues.`,
    options: {
      model: "opus",
      allowedTools: ["Read", "Glob", "Grep"],
      permissionMode: "bypassPermissions",
      maxTurns: 250,
      outputFormat: {
        type: "json_schema",
        schema: reviewSchema
      }
    }
  })) {
    if (message.type === "result" && message.subtype === "success") {
      const review = message.structured_output as {
        issues: Array<{
          severity: string;
          category: string;
          file: string;
          line?: number;
          description: string;
          suggestion?: string;
        }>;
        summary: string;
        overallScore: number;
      };
      
      console.log(`\n📊 Code Review Results\n`);
      console.log(`Score: ${review.overallScore}/100`);
      console.log(`Summary: ${review.summary}\n`);
      
      for (const issue of review.issues) {
        const icon = issue.severity === "critical" ? "🔴" :
                     issue.severity === "high" ? "🟠" :
                     issue.severity === "medium" ? "🟡" : "🟢";
        console.log(`${icon} [${issue.category.toUpperCase()}] ${issue.file}${issue.line ? `:${issue.line}` : ""}`);
        console.log(`   ${issue.description}`);
        if (issue.suggestion) {
          console.log(`   💡 ${issue.suggestion}`);
        }
        console.log();
      }
    }
  }
}

reviewCodeStructured(".");
```

默认情况下，SDK 在执行工具前会请求批准。你可以自定义这一点：

```
options: {
  // Standard mode - prompts for approval
  permissionMode: "default",
  
  // Auto-approve file edits
  permissionMode: "acceptEdits",
  
  // No prompts (use with caution)
  permissionMode: "bypassPermissions"
}
```

```
options: {
  canUseTool: async (toolName, input) => {
    // Allow all read operations
    if (["Read", "Glob", "Grep"].includes(toolName)) {
      return { behavior: "allow", updatedInput: input };
    }
    
    // Block writes to certain files
    if (toolName === "Write" && input.file_path?.includes(".env")) {
      return { behavior: "deny", message: "Cannot modify .env files" };
    }
    
    // Allow everything else
    return { behavior: "allow", updatedInput: input };
  }
}
```

```
import { query, AgentDefinition } from "@anthropic-ai/claude-agent-sdk";

async function comprehensiveReview(directory: string) {
  for await (const message of query({
    prompt: `Perform a comprehensive code review of ${directory}. 
Use the security-reviewer for security issues and test-analyzer for test coverage.`,
    options: {
      model: "opus",
      allowedTools: ["Read", "Glob", "Grep", "Task"], // Task enables subagents
      permissionMode: "bypassPermissions",
      maxTurns: 250,
      agents: {
        "security-reviewer": {
          description: "Security specialist for vulnerability detection",
          prompt: `You are a security expert. Focus on:
- SQL injection, XSS, CSRF vulnerabilities
- Exposed credentials and secrets
- Insecure data handling
- Authentication/authorization issues`,
          tools: ["Read", "Grep", "Glob"],
          model: "sonnet"
        } as AgentDefinition,
        
        "test-analyzer": {
          description: "Test coverage and quality analyzer",
          prompt: `You are a testing expert. Analyze:
- Test coverage gaps
- Missing edge cases
- Test quality and reliability
- Suggestions for additional tests`,
          tools: ["Read", "Grep", "Glob"],
          model: "haiku" // Use faster model for simpler analysis
        } as AgentDefinition
      }
    }
  })) {
    if (message.type === "assistant") {
      for (const block of message.message.content) {
        if ("text" in block) {
          console.log(block.text);
        } else if ("name" in block && block.name === "Task") {
          console.log(`\n🤖 Delegating to: ${(block.input as any).subagent_type}`);
        }
      }
    }
  }
}

comprehensiveReview(".");
```

```
import { query } from "@anthropic-ai/claude-agent-sdk";

async function interactiveReview() {
  let sessionId: string | undefined;
  
  // Initial review
  for await (const message of query({
    prompt: "Review this codebase and identify the top 3 issues",
    options: {
      model: "opus",
      allowedTools: ["Read", "Glob", "Grep"],
      permissionMode: "bypassPermissions",
      maxTurns: 250
    }
  })) {
    if (message.type === "system" && message.subtype === "init") {
      sessionId = message.session_id;
    }
    // ... handle messages
  }
  
  // Follow-up question using same session
  if (sessionId) {
    for await (const message of query({
      prompt: "Now show me how to fix the most critical issue",
      options: {
        resume: sessionId, // Continue the conversation
        allowedTools: ["Read", "Glob", "Grep"],
        maxTurns: 250
      }
    })) {
      // Claude remembers the previous context
    }
  }
}
```

```
import { query, HookCallback, PreToolUseHookInput } from "@anthropic-ai/claude-agent-sdk";

const auditLogger: HookCallback = async (input, toolUseId, { signal }) => {
  if (input.hook_event_name === "PreToolUse") {
    const preInput = input as PreToolUseHookInput;
    console.log(`[AUDIT] ${new Date().toISOString()} - ${preInput.tool_name}`);
  }
  return {}; // Allow the operation
};

const blockDangerousCommands: HookCallback = async (input, toolUseId, { signal }) => {
  if (input.hook_event_name === "PreToolUse") {
    const preInput = input as PreToolUseHookInput;
    if (preInput.tool_name === "Bash") {
      const command = (preInput.tool_input as any).command || "";
      if (command.includes("rm -rf") || command.includes("sudo")) {
        return {
          hookSpecificOutput: {
            hookEventName: "PreToolUse",
            permissionDecision: "deny",
            permissionDecisionReason: "Dangerous command blocked"
          }
        };
      }
    }
  }
  return {};
};

for await (const message of query({
  prompt: "Clean up temporary files",
  options: {
    model: "opus",
    allowedTools: ["Bash", "Glob"],
    maxTurns: 250,
    hooks: {
      PreToolUse: [
        { hooks: [auditLogger] },
        { matcher: "Bash", hooks: [blockDangerousCommands] }
      ]
    }
  }
})) {
  // ...
}
```

使用模型上下文协议为 Claude 扩展自定义工具：

```
import { query, tool, createSdkMcpServer } from "@anthropic-ai/claude-agent-sdk";
import { z } from "zod";

// Create a custom tool
const customServer = createSdkMcpServer({
  name: "code-metrics",
  version: "1.0.0",
  tools: [
    tool(
      "analyze_complexity",
      "Calculate cyclomatic complexity for a file",
      {
        filePath: z.string().describe("Path to the file to analyze")
      },
      async (args) => {
        // Your complexity analysis logic here
        const complexity = Math.floor(Math.random() * 20) + 1; // Placeholder
        return {
          content: [{
            type: "text",
            text: `Cyclomatic complexity for ${args.filePath}: ${complexity}`
          }]
        };
      }
    )
  ]
});

// Use streaming input for MCP servers
async function* generateMessages() {
  yield {
    type: "user" as const,
    message: {
      role: "user" as const,
      content: "Analyze the complexity of main.ts"
    }
  };
}

for await (const message of query({
  prompt: generateMessages(),
  options: {
    model: "opus",
    mcpServers: {
      "code-metrics": customServer
    },
    allowedTools: ["Read", "mcp__code-metrics__analyze_complexity"],
    maxTurns: 250
  }
})) {
  // ...
}
```

```
for await (const message of query({ prompt: "..." })) {
  if (message.type === "result" && message.subtype === "success") {
    console.log("Total cost:", message.total_cost_usd);
    console.log("Token usage:", message.usage);
    
    // Per-model breakdown (useful with subagents)
    for (const [model, usage] of Object.entries(message.modelUsage)) {
      console.log(`${model}: $${usage.costUSD.toFixed(4)}`);
    }
  }
}
```

这是一个可投入生产的代理，能把所有东西整合在一起：

```
import { query, AgentDefinition } from "@anthropic-ai/claude-agent-sdk";

interface ReviewResult {
  issues: Array<{
    severity: "low" | "medium" | "high" | "critical";
    category: "bug" | "security" | "performance" | "style";
    file: string;
    line?: number;
    description: string;
    suggestion?: string;
  }>;
  summary: string;
  overallScore: number;
}

const reviewSchema = {
  type: "object",
  properties: {
    issues: {
      type: "array",
      items: {
        type: "object",
        properties: {
          severity: { type: "string", enum: ["low", "medium", "high", "critical"] },
          category: { type: "string", enum: ["bug", "security", "performance", "style"] },
          file: { type: "string" },
          line: { type: "number" },
          description: { type: "string" },
          suggestion: { type: "string" }
        },
        required: ["severity", "category", "file", "description"]
      }
    },
    summary: { type: "string" },
    overallScore: { type: "number" }
  },
  required: ["issues", "summary", "overallScore"]
};

async function runCodeReview(directory: string): Promise<ReviewResult | null> {
  console.log(`\n${"=".repeat(50)}`);
  console.log(`🔍 Code Review Agent`);
  console.log(`📁 Directory: ${directory}`);
  console.log(`${"=".repeat(50)}\n`);

  let result: ReviewResult | null = null;

  for await (const message of query({
    prompt: `Perform a thorough code review of ${directory}.

Analyze all source files for:
1. Bugs and potential runtime errors
2. Security vulnerabilities
3. Performance issues
4. Code quality and maintainability

Be specific with file paths and line numbers where possible.`,
    options: {
      model: "opus",
      allowedTools: ["Read", "Glob", "Grep", "Task"],
      permissionMode: "bypassPermissions",
      maxTurns: 250,
      outputFormat: {
        type: "json_schema",
        schema: reviewSchema
      },
      agents: {
        "security-scanner": {
          description: "Deep security analysis for vulnerabilities",
          prompt: `You are a security expert. Scan for:
- Injection vulnerabilities (SQL, XSS, command injection)
- Authentication and authorization flaws
- Sensitive data exposure
- Insecure dependencies`,
          tools: ["Read", "Grep", "Glob"],
          model: "sonnet"
        } as AgentDefinition
      }
    }
  })) {
    // Progress updates
    if (message.type === "assistant") {
      for (const block of message.message.content) {
        if ("name" in block) {
          if (block.name === "Task") {
            console.log(`🤖 Delegating to: ${(block.input as any).subagent_type}`);
          } else {
            console.log(`📂 ${block.name}: ${getToolSummary(block)}`);
          }
        }
      }
    }

    // Final result
    if (message.type === "result") {
      if (message.subtype === "success" && message.structured_output) {
        result = message.structured_output as ReviewResult;
        console.log(`\n✅ Review complete! Cost: $${message.total_cost_usd.toFixed(4)}`);
      } else {
        console.log(`\n❌ Review failed: ${message.subtype}`);
      }
    }
  }

  return result;
}

function getToolSummary(block: any): string {
  const input = block.input || {};
  switch (block.name) {
    case "Read": return input.file_path || "file";
    case "Glob": return input.pattern || "pattern";
    case "Grep": return `"${input.pattern}" in ${input.path || "."}`;
    default: return "";
  }
}

function printResults(result: ReviewResult) {
  console.log(`\n${"=".repeat(50)}`);
  console.log(`📊 REVIEW RESULTS`);
  console.log(`${"=".repeat(50)}\n`);
  
  console.log(`Score: ${result.overallScore}/100`);
  console.log(`Issues Found: ${result.issues.length}\n`);
  console.log(`Summary: ${result.summary}\n`);
  
  const byCategory = {
    critical: result.issues.filter(i => i.severity === "critical"),
    high: result.issues.filter(i => i.severity === "high"),
    medium: result.issues.filter(i => i.severity === "medium"),
    low: result.issues.filter(i => i.severity === "low")
  };
  
  for (const [severity, issues] of Object.entries(byCategory)) {
    if (issues.length === 0) continue;
    
    const icon = severity === "critical" ? "🔴" :
                 severity === "high" ? "🟠" :
                 severity === "medium" ? "🟡" : "🟢";
    
    console.log(`\n${icon} ${severity.toUpperCase()} (${issues.length})`);
    console.log("-".repeat(30));
    
    for (const issue of issues) {
      const location = issue.line ? `${issue.file}:${issue.line}` : issue.file;
      console.log(`\n[${issue.category}] ${location}`);
      console.log(`  ${issue.description}`);
      if (issue.suggestion) {
        console.log(`  💡 ${issue.suggestion}`);
      }
    }
  }
}

// Run the review
async function main() {
  const directory = process.argv[2] || ".";
  const result = await runCodeReview(directory);
  
  if (result) {
    printResults(result);
  }
}

main().catch(console.error);
```

```
npx tsx review-agent.ts ./src
```

代码审查代理涵盖了核心要素：查询()、允许的工具、结构化输出、子代理和权限。

-   \- 包可复用的能力
    

-   \- 部署到容器和 CI/CD
    

> 本指南涵盖了 SDK 的 V1 版本。V2 目前正在开发中。一旦 V2 发布并稳定后，我会更新本指南。 如果您对构建可验证代理感兴趣，请查看我们正在进行的工作。 。