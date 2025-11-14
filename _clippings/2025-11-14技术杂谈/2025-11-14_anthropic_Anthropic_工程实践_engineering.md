---
title: "2025-11-14_anthropic_com_Anthropic_工程实践_engineering"
source: "https://www.anthropic.com/engineering/code-execution-with-mcp"
author:
  - "[[@anthropic.com]]"
published: 2025-11-14
created: 2025-11-14
description:
tags:
  - "anthropic"
  - "@anthropic.com"
  - "mcp"
  - "salesforce"
---

# [Anthropic 工程实践](engineering)

[Anthropic 工程实践](/engineering)

[模型上下文协议（MCP）](https://modelcontextprotocol.io/) 是连接 AI 智能体与外部系统的开放标准。传统上，将智能体与工具及数据连接需要为每个配对进行定制集成，这导致了碎片化和重复劳动，使得真正互联的系统难以扩展。MCP 提供了一个通用协议——开发者只需在智能体中实现一次 MCP，即可解锁整个集成生态系统。

自 2024 年 11 月推出 MCP 以来，其应用迅速普及：社区已构建了数千个 [MCP 服务器](https://github.com/modelcontextprotocol/servers) ，所有主流编程语言都提供了 [SDK](https://modelcontextprotocol.io/docs/sdk) 支持，业界已将 MCP 视为连接智能体与工具数据的实际标准。

如今，开发者通常会构建能够访问数十个 MCP 服务器中数百甚至数千种工具的智能体。然而，随着连接工具数量的增加，预先加载所有工具定义并通过上下文窗口传递中间结果的做法，会降低智能体的运行速度并增加成本。

在这篇博客中，我们将探讨代码执行如何让智能体更高效地与 MCP 服务器交互，既能调用更多工具，又能减少令牌消耗。

## 工具消耗过多令牌会降低代理的效率

随着 MCP 使用规模的扩大，有两种常见模式可能会增加代理成本和延迟：

1.  工具定义会挤占上下文窗口；
2.  中间工具结果会消耗额外的令牌。

### 工具定义过多会占用上下文窗口

大多数 MCP 客户端会预先将所有工具定义直接加载到上下文中，通过直接工具调用语法向模型公开这些定义。这些工具定义可能呈现为以下形式：

```
gdrive.getDocument
 Description: Retrieves a document from Google Drive
 Parameters:
 documentId (required, string): The ID of the document to retrieve
 fields (optional, string): Specific fields to return
 Returns: Document object with title, body content, metadata, permissions, etc.
```

```
salesforce.updateRecord
 Description: Updates a record in Salesforce
 Parameters:
 objectType (required, string): Type of Salesforce object (Lead, Contact, Account, etc.)
 recordId (required, string): The ID of the record to update
 data (required, object): Fields to update with their new values
 Returns: Updated record object with confirmation
```

工具描述会占用更多的上下文窗口空间，从而增加响应时间和成本。在代理连接数千个工具的情况下，它们需要处理数十万个令牌才能读取请求。

### 2\. 中间工具结果会消耗额外的令牌

大多数 MCP 客户端允许模型直接调用 MCP 工具。例如，你可以向智能体发出指令："从 Google Drive 下载我的会议记录，并将其附加到 Salesforce 的销售线索中。"

模型将执行如下调用：

```
TOOL CALL: gdrive.getDocument(documentId: "abc123")
 → returns "Discussed Q4 goals...\n[full transcript text]"
 (loaded into model context)

TOOL CALL: salesforce.updateRecord(
 objectType: "SalesMeeting",
 recordId: "00Q5f000001abcXYZ",
 data: { "Notes": "Discussed Q4 goals...\n[full transcript text written out]" }
 )
 (model needs to write entire transcript into context again)
```

每个中间结果都必须经过模型处理。在这个例子中，完整的对话记录需要流经模型两次。对于一场两小时的销售会议，这可能意味着需要额外处理5万个词元。更大的文档甚至可能超出上下文窗口限制，导致工作流程中断。

在处理大型文档或复杂数据结构时，模型在工具调用间复制数据时更容易出错。

![Image of how the MCP client works with the MCP server and LLM.](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F9ecf165020005c09a22a9472cee6309555485619-1920x1080.png&w=3840&q=75)

MCP 客户端将工具定义加载到模型的上下文窗口中，并编排一个消息循环，在每次操作之间，每个工具调用及其结果都会经过模型处理。

## 通过 MCP 执行代码可提升上下文效率

随着代码执行环境在智能体中的日益普及，一种解决方案是将 MCP 服务器呈现为代码 API 而非直接工具调用。这样，智能体便能编写代码与 MCP 服务器交互。此方法同时应对了两大挑战：智能体可仅加载所需工具，并在执行环境中处理数据后再将结果传回模型。

实现这一目标有多种方式。一种方法是生成来自已连接 MCP 服务器的所有可用工具的文件树。以下是使用 TypeScript 的实现示例：

```
servers
├── google-drive
│ ├── getDocument.ts
│ ├── ... (other tools)
│ └── index.ts
├── salesforce
│ ├── updateRecord.ts
│ ├── ... (other tools)
│ └── index.ts
└── ... (other servers)
```

那么每个工具就对应一个文件，类似这样：

```
// ./servers/google-drive/getDocument.ts
import { callMCPTool } from "../../../client.js";

interface GetDocumentInput {
  documentId: string;
}

interface GetDocumentResponse {
  content: string;
}

/* Read a document from Google Drive */
export async function getDocument(input: GetDocumentInput): Promise<GetDocumentResponse> {
  return callMCPTool<GetDocumentResponse>('google_drive__get_document', input);
}
```

我们上面提到的从 Google Drive 到 Salesforce 的示例就变成了这段代码：

```
// Read transcript from Google Docs and add to Salesforce prospect
import * as gdrive from './servers/google-drive';
import * as salesforce from './servers/salesforce';

const transcript = (await gdrive.getDocument({ documentId: 'abc123' })).content;
await salesforce.updateRecord({
  objectType: 'SalesMeeting',
  recordId: '00Q5f000001abcXYZ',
  data: { Notes: transcript }
});
```

智能体通过探索文件系统来发现工具：首先列出 `./servers/` 目录以查找可用服务器（例如 `google-drive` 和 `salesforce` ），随后读取所需的具体工具文件（如 `getDocument.ts` 和 `updateRecord.ts` ）来理解每个工具的接口。这种方式使得智能体仅需加载当前任务所需的定义，从而将令牌使用量从 15 万降至 2000——实现了 98.7%的时间和成本节约。

Cloudflare [发布过类似研究](https://blog.cloudflare.com/code-mode/) ，将 MCP 代码执行称为“代码模式”。核心洞见如出一辙：LLMs 擅长编写代码，开发者应利用这一优势构建能与 MCP 服务器高效交互的智能体。

## 通过 MCP 执行代码的优势

通过 MCP 执行代码，智能体能够按需加载工具、在数据传入模型前进行筛选，以及单步执行复杂逻辑，从而更高效地利用上下文。这种方法还具备安全性和状态管理方面的优势。

模型在文件系统导航方面表现出色。将工具以代码形式呈现在文件系统上，使模型能够按需读取工具定义，而非一次性预先读取所有内容。

或者，可以在服务器中添加一个 `search_tools` 工具来查找相关定义。例如，当使用上述假设的 Salesforce 服务器时，智能体会搜索“salesforce”并仅加载当前任务所需的工具。在 `search_tools` 工具中包含一个详细级别参数，允许智能体选择所需的详细程度（如仅名称、名称和描述，或包含架构的完整定义），也有助于智能体节省上下文并高效查找工具。

### 上下文高效工具结果

在处理大型数据集时，智能体可以先通过代码对结果进行筛选和转换，再将其返回。设想一下获取一个包含一万行数据的电子表格：

```
// Without code execution - all rows flow through context
TOOL CALL: gdrive.getSheet(sheetId: 'abc123')
 → returns 10,000 rows in context to filter manually

// With code execution - filter in the execution environment
const allRows = await gdrive.getSheet({ sheetId: 'abc123' });
const pendingOrders = allRows.filter(row => 
  row["Status"] === 'pending'
);
console.log(`Found ${pendingOrders.length} pending orders`);
console.log(pendingOrders.slice(0, 5)); // Only log first 5 for review
```

代理看到的是五行数据而非一万行。类似的模式适用于聚合、跨多个数据源的连接或提取特定字段——所有这些操作都不会导致上下文窗口膨胀。

循环、条件判断和错误处理可以通过熟悉的代码模式完成，而无需串联多个独立工具调用。例如，若需在 Slack 发送部署通知，智能体可直接编写代码实现：

```
let found = false;
while (!found) {
  const messages = await slack.getChannelHistory({ channel: 'C123456' });
  found = messages.some(m => m.text.includes('deployment complete'));
  if (!found) await new Promise(r => setTimeout(r, 5000));
}
console.log('Deployment notification received');
```

这种方法比在代理循环中交替使用 MCP 工具调用和休眠命令更为高效。

此外，能够编写并执行条件判断树还能减少“首词延迟”时间：代理无需等待模型评估 if 语句，而是让代码执行环境来完成这一过程。

### 隐私保护操作

当代理使用 MCP 执行代码时，中间结果默认会保留在执行环境中。这样一来，代理只能看到您明确记录或返回的内容，这意味着您不希望与模型共享的数据可以在工作流中流转，而无需进入模型的上下文。

对于更敏感的工作负载，代理框架可自动对敏感数据进行标记化处理。例如，假设您需要将客户联系信息从电子表格导入 Salesforce，代理会编写如下代码：

```
const sheet = await gdrive.getSheet({ sheetId: 'abc123' });
for (const row of sheet.rows) {
  await salesforce.updateRecord({
 objectType: 'Lead',
 recordId: row.salesforceId,
 data: { 
 Email: row.email,
 Phone: row.phone,
 Name: row.name
 }
  });
}
console.log(`Updated ${sheet.rows.length} leads`);
```

MCP 客户端在数据抵达模型前进行拦截，并对个人身份信息进行分词处理

```
// What the agent would see, if it logged the sheet.rows:
[
  { salesforceId: '00Q...', email: '[EMAIL_1]', phone: '[PHONE_1]', name: '[NAME_1]' },
  { salesforceId: '00Q...', email: '[EMAIL_2]', phone: '[PHONE_2]', name: '[NAME_2]' },
  ...
]
```

随后，当这些数据在另一个 MCP 工具调用中被共享时，会通过 MCP 客户端中的查找操作进行反标记化。真实的电子邮件地址、电话号码和姓名从 Google 表格流向 Salesforce，但始终不经过模型。这可以防止代理意外记录或处理敏感数据。您还可以利用此功能定义确定性的安全规则，选择数据可以流向和来自哪些位置。

### 状态持久化与技能

具备文件系统访问权限的代码执行功能使得智能体能够在跨操作中维持状态。智能体可将中间结果写入文件，从而实现工作断点续传与进度追踪：

```
const leads = await salesforce.query({ 
  query: 'SELECT Id, Email FROM Lead LIMIT 1000' 
});
const csvData = leads.map(l => `${l.Id},${l.Email}`).join('\n');
await fs.writeFile('./workspace/leads.csv', csvData);

// Later execution picks up where it left off
const saved = await fs.readFile('./workspace/leads.csv', 'utf-8');
```

智能体还能将自身代码作为可复用函数进行持久化存储。当智能体为某项任务开发出有效代码后，即可保存该实现方案供未来调用：

```
// In ./skills/save-sheet-as-csv.ts
import * as gdrive from './servers/google-drive';
export async function saveSheetAsCsv(sheetId: string) {
  const data = await gdrive.getSheet({ sheetId });
  const csv = data.map(row => row.join(',')).join('\n');
  await fs.writeFile(`./workspace/sheet-${sheetId}.csv`, csv);
  return `./workspace/sheet-${sheetId}.csv`;
}

// Later, in any agent execution:
import { saveSheetAsCsv } from './skills/save-sheet-as-csv';
const csvPath = await saveSheetAsCsv('abc123');
```

这与 [技能](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) 概念紧密相连——技能是可复用的指令、脚本和资源文件夹，用于提升模型在特定任务上的表现。为这些保存的函数添加 SKILL.md 文件即可创建结构化技能，供模型参考使用。长此以往，你的智能体将逐步构建起高阶能力的工具箱，不断优化其高效运作所需的基础架构。

需要注意的是，代码执行本身会带来复杂性。运行智能体生成的代码需要一个具备适当 [沙箱隔离](https://www.anthropic.com/engineering/claude-code-sandboxing) 机制、资源限制和监控功能的安全执行环境。这些基础设施要求会带来额外的运维负担和安全考量，而直接调用工具则可以避免这些问题。代码执行的优势——如降低令牌成本、减少延迟以及优化工具组合——需要与这些实施成本进行权衡。

## Summary

MCP 为智能体连接多种工具和系统提供了基础协议。然而，当连接的服务器过多时，工具定义和结果会消耗过多令牌，从而降低智能体的运行效率。

尽管这里的许多问题——如上下文管理、工具组合、状态持久化——看似新颖，但软件工程领域已有成熟的解决方案。代码执行将这些既定模式应用于智能体，使其能够利用熟悉的编程结构更高效地与 MCP 服务器交互。若您实践此方法，我们期待您与 [MCP 社区](https://modelcontextprotocol.io/community/communication) 分享成果。

### Acknowledgments

*本文由亚当·琼斯与康纳·凯利共同撰写。感谢杰里米·福克斯、杰罗姆·斯旺纳克、斯图尔特·里奇、莫莉·沃沃克、马特·塞缪尔和玛吉·沃对本文草稿提出的宝贵意见。*

## 订阅开发者通讯

产品更新、使用指南、社区亮点等精彩内容。每月定期发送至您的收件箱。