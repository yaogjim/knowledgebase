# 技术解析：深入剖析 llmstxt Generator 项目

在当今大规模语言模型（LLM）快速发展的背景下，数据的获取与处理显得尤为重要。本文将深入分析开源项目 **llmstxt Generator**，该项目旨在从网站生成用于LLM训练和推理的综合文本文件。我们将从系统架构、主要组件、关键实现细节等方面进行详细解析，帮助读者全面理解其设计与实现，并能够借鉴其思想构建类似的解决方案。

## 技术概述

### 系统架构图（文本形式）

```
+---------------------------+
|         前端界面           |
|   [app/page.tsx]          |
+------------+--------------+
             |
             v
+------------+--------------+
|         API 网关           |
|   [app/[...slug]/route.ts] |
+------------+--------------+
             |
             v
+------------+--------------+
|         服务层             |
|  [app/api/map/route.ts]    |
|  [app/api/service/route.ts]|
+------------+--------------+
             |
             v
+------------+--------------+
| 外部服务与数据库           |
| - Firecrawl API            |
| - OpenAI API               |
| - Supabase 数据库           |
+---------------------------+
```

### 主要组件功能与职责

#### 1. 前端界面 (`app/page.tsx`)

- **功能**：提供用户交互界面，允许用户输入目标网址，选择生成文件类型，并展示生成结果。
- **输入/输出**：
  - **输入**：用户输入的目标网址、可选的 Firecrawl API 密钥。
  - **输出**：生成的 `llms.txt` 或 `llms-full.txt` 文件内容，以及复制功能。
- **依赖**：
  - React 库
  - Tailwind CSS
- **关键接口**：
  - 调用后端的 `/api/map` 和 `/api/service` 接口。
- **数据流**：
  - 用户输入 -> 前端发送请求 -> 接收并展示后端返回的数据。
- **配置**：
  - 环境变量配置 API 密钥等。
- **开发环境与设置**：
  - 使用 Next.js 框架，配置 React 组件，使用 Hooks 管理状态。

#### 2. API 网关 (`app/[...slug]/route.ts`)

- **功能**：处理动态路由请求，根据请求路径决定调用相应的后端服务，并返回生成的文本文件内容。
- **输入/输出**：
  - **输入**：URL 路径参数，包含目标网址和可选的 `full` 标志。
  - **输出**：生成的 `llms.txt` 或 `llms-full.txt` 内容。
- **依赖**：
  - Next.js 服务端功能
- **关键接口**：
  - 调用 `/api/map` 和 `/api/service` 接口，组合结果并返回。
- **数据流**：
  - 前端请求 -> API 网关处理 -> 调用服务层 -> 返回结果。
- **配置**：
  - 无特定配置，依赖后端服务的可用性。
- **开发环境与设置**：
  - 使用 Next.js 的动态路由特性，实现灵活的 API 路由分发。

#### 3. 服务层

##### 3.1 `app/api/map/route.ts`

- **功能**：调用 Firecrawl API 进行网站映射，获取网站链接列表。
- **输入/输出**：
  - **输入**：目标网址，Firecrawl API 密钥。
  - **输出**：网站链接列表 (`mapUrls`)。
- **依赖**：
  - `@mendable/firecrawl-js` 库
  - Firecrawl API
- **关键接口**：
  - Firecrawl 的 `mapUrl` 方法。
- **数据流**：
  - 接收前端请求 -> 调用 Firecrawl API -> 返回链接列表。
- **配置**：
  - Firecrawl API 密钥，通过环境变量或用户提供。
- **开发环境与设置**：
  - 使用 TypeScript，实现 API 路由，处理 HTTP 请求。

##### 3.2 `app/api/service/route.ts`

- **功能**：处理链接列表，调用 OpenAI API 生成描述和标题，整合生成最终的 `llms.txt` 和 `llms-full.txt`。
- **输入/输出**：
  - **输入**：链接列表 (`urls`)，Firecrawl API 密钥。
  - **输出**：生成的 `llms.txt` 和 `llms-full.txt` 内容。
- **依赖**：
  - Firecrawl API
  - OpenAI API
  - Supabase 数据库
- **关键接口**：
  - Firecrawl 的 `batchScrapeUrls` 方法。
  - OpenAI 的 `chat.completions` 接口。
  - Supabase 的数据库操作接口。
- **数据流**：
  - 接收前端请求 -> 检查缓存 -> 调用 Firecrawl 与 OpenAI API -> 存储结果到 Supabase -> 返回生成文本。
- **配置**：
  - Firecrawl API 密钥、OpenAI API 密钥、Supabase URL 与密钥。
- **开发环境与设置**：
  - 使用 TypeScript，处理复杂的业务逻辑，集成多个外部服务。

#### 4. 外部服务与数据库

- **Firecrawl API**：用于网站爬取和链接映射。
- **OpenAI API**：用于生成页面描述和标题。
- **Supabase 数据库**：用于缓存生成的结果，提升性能。

### 组件交互流程

1. **用户在前端界面** 输入目标网址，并选择生成 `llms.txt` 或 `llms-full.txt`。
2. **前端发送请求** 到 API 网关 (`app/[...slug]/route.ts`)，携带目标网址和可选的 Firecrawl API 密钥。
3. **API 网关解析请求**，调用服务层的 `/api/map` 接口获取链接列表。
4. **`/api/map` 接口** 使用 Firecrawl API 进行网站映射，返回链接列表。
5. **API 网关接收到链接列表**，继续调用 `/api/service` 接口进行文本生成。
6. **`/api/service` 接口** 检查 Supabase 数据库是否有缓存，若无，则调用 Firecrawl 和 OpenAI API，生成 `llms.txt` 和 `llms-full.txt`，并存储到数据库。
7. **生成的文本内容** 通过 API 网关返回给前端，用户可以在界面上查看并复制。

### 配置选项及其影响

- **环境变量**：
  - `FIRECRAWL_API_KEY`：控制 Firecrawl API 的访问权限。
  - `SUPABASE_URL` & `SUPABASE_KEY`：用于连接 Supabase 数据库。
  - `OPENAI_API_KEY`：用于调用 OpenAI 的语言模型接口。
- **API 请求参数**：
  - `bringYourOwnFirecrawlApiKey`：允许用户提供自定义的 Firecrawl API 密钥，影响文本生成的完整性（有无限制）。
- **限速配置**：
  - 服务层根据是否使用自定义 API 密钥调整爬取和处理的数量限制，提高灵活性。

### 开发环境与设置要求

- **开发工具**：
  - Node.js
  - Next.js 框架
  - TypeScript
  - Tailwind CSS
- **依赖管理**：
  - 使用 `npm` 进行依赖安装，项目依赖定义在 `package.json` 中。
- **本地开发**：
  - 创建 `.env` 文件，配置必要的环境变量。
  - 运行 `npm install` 安装依赖，使用 `npm run dev` 启动开发服务器。

## 关键实现细节

在项目中，有多个关键功能模块值得深入探讨。以下将重点解析其中五个核心功能点，包括代码片段、实现步骤、技术决策及与外部服务的集成等。

### 1. 网站映射功能 (`app/api/map/route.ts`)

#### a) 完整、可运行的代码片段

```typescript
// app/api/map/route.ts

import { NextResponse } from 'next/server';
import FirecrawlApp from '@mendable/firecrawl-js';
import { config } from 'dotenv';
config();

export const maxDuration = 300; 

export async function POST(request: Request) {
  const { url, bringYourOwnFirecrawlApiKey } = await request.json();
  let firecrawlApiKey: string | undefined;
  let limit: number = 100;

  if (bringYourOwnFirecrawlApiKey) {
    firecrawlApiKey = bringYourOwnFirecrawlApiKey;
    console.log("Using provided Firecrawl API key. Limit set to 100");
  } else {
    firecrawlApiKey = process.env.FIRECRAWL_API_KEY;
    limit = 10;
    console.log("Using default limit of 10");
  }

  if (!firecrawlApiKey) {
    throw new Error('FIRECRAWL_API_KEY is not set');
  }

  const app = new FirecrawlApp({ apiKey: firecrawlApiKey });

  let urlObj;
  if (url.startsWith('http://') || url.startsWith('https://')) {
    urlObj = new URL(url);
  } else {
    urlObj = new URL(`http://${url}`);
  }
  
  const stemUrl = `${urlObj.hostname}`;

  // Map a website
  const mapResult = await app.mapUrl(stemUrl, {
    limit: limit,
  });

  if (!mapResult.success) {
    throw new Error(`Failed to map: ${mapResult.error}`);
  }

  let urls = mapResult.success ? mapResult.links : [];

  return NextResponse.json({ mapUrls: urls });
}
```

#### b) 实现步骤解析

- **目的**：接收目标网址，调用 Firecrawl API 进行网站映射，返回链接列表。
- **主要函数**：
  - `POST` 函数：处理 POST 请求。
- **关键变量**：
  - `url`：用户输入的目标网址。
  - `bringYourOwnFirecrawlApiKey`：用户提供的 Firecrawl API 密钥。
  - `firecrawlApiKey`：最终使用的 Firecrawl API 密钥，来自用户输入或环境变量。
  - `limit`：爬取链接的数量限制，若使用默认密钥则限制为10，否则为100。
- **控制流程**：
  1. **解析请求体**：提取 `url` 和 `bringYourOwnFirecrawlApiKey`。
  2. **确定 API 密钥与限制**：优先使用用户提供的密钥，若无则使用环境变量中的默认密钥，并调整爬取限制。
  3. **验证 API 密钥**：若未设置密钥，抛出错误。
  4. **创建 Firecrawl 应用实例**：传入 API 密钥。
  5. **解析网址**：确保 URL 格式正确，提取主机名。
  6. **调用 Firecrawl 的映射方法**：获取链接列表。
  7. **返回结果**：以 JSON 格式返回链接列表。

- **错误处理**：
  - 若未设置 `FIRECRAWL_API_KEY`，抛出错误。
  - 若 Firecrawl API 调用失败，抛出相应错误信息。

- **性能考虑**：
  - 设置 `maxDuration` 为300秒，避免长时间挂起请求。

#### c) 技术决策与理由

- **选择使用 Firecrawl SDK**：简化与 Firecrawl API 的集成，通过封装好的方法调用，提高开发效率。
- **动态限制爬取数量**：根据是否使用自定义 API 密钥，灵活调整爬取链接数量，确保服务的可控性与稳定性。
- **错误处理机制**：通过抛出错误，确保前端能够及时接收到并处理失败情况，提升用户体验。

#### d) 与外部服务/API 的集成点

- **Firecrawl API**：
  - **认证**：通过 API 密钥进行身份验证。
  - **数据格式**：发送 JSON 请求，接收 JSON 响应。
  - **响应处理**：解析成功与失败的响应，确保数据的正确性。

#### e) 重要优化技术

- **环境变量管理**：使用 `dotenv` 库管理环境变量，确保敏感信息的安全性与灵活性。
- **URL 解析优化**：通过条件判断确保输入 URL 格式正确，减少 API 调用失败的可能性。

#### f) 配置参数及其影响

- **`FIRECRAWL_API_KEY`**：决定 API 的权限与爬取限制，影响生成文本的完整性。
- **`limit`**：控制爬取的链接数量，影响生成文本的详细程度与响应时间。

### 2. 文本生成服务 (`app/api/service/route.ts`)

#### a) 完整、可运行的代码片段

```typescript
// app/api/service/route.ts

import { NextResponse } from 'next/server';
import FirecrawlApp from '@mendable/firecrawl-js';
import { config } from 'dotenv';
config();
import { createClient } from '@supabase/supabase-js'
import OpenAI from "openai";
import { zodResponseFormat } from "openai/helpers/zod";
import { z } from "zod";

export const maxDuration = 300; 

export async function POST(request: Request) {
  const { urls, bringYourOwnFirecrawlApiKey } = await request.json();
  let firecrawlApiKey: string | undefined;
  let limit: number = 100;
  let no_limit: boolean = false;

  if (bringYourOwnFirecrawlApiKey) {
    firecrawlApiKey = bringYourOwnFirecrawlApiKey;
    console.log("Using provided Firecrawl API key. Limit set to 100");
    no_limit = true;
  } else {
    firecrawlApiKey = process.env.FIRECRAWL_API_KEY;
    limit = 10;
    console.log("Using default limit of 10");
  }

  if (!firecrawlApiKey) {
    throw new Error('FIRECRAWL_API_KEY is not set');
  }

  const app = new FirecrawlApp({ apiKey: firecrawlApiKey });

  let urlsToScrape = urls;

  // 确保 url 数量不超过限制
  if (urlsToScrape && urlsToScrape.length > limit) {
    urlsToScrape = urlsToScrape.slice(0, limit);
  }
  const sampleUrl = urlsToScrape[0];
  let urlObj;
  if (sampleUrl.startsWith('http://') || sampleUrl.startsWith('https://')) {
    urlObj = new URL(sampleUrl);
  } else {
    urlObj = new URL(`http://${sampleUrl}`);
  }
  
  const stemUrl = `${urlObj.hostname}`;

  const supabaseUrl = process.env.SUPABASE_URL;
  const supabaseKey = process.env.SUPABASE_KEY;
  const supabase = createClient(supabaseUrl!, supabaseKey!);

  const { data: cacheData, error: cacheError } = await supabase
    .from('cache')
    .select('llmstxt, llmsfulltxt, cached_at')
    .eq('url', stemUrl)
    .eq('no_limit', no_limit)
    .single();

  if (cacheError) {
    console.log('no cache hit');
  } else if (cacheData) {
    const cacheAge = (new Date().getTime() - new Date(cacheData.cached_at).getTime()) / (1000 * 60 * 60 * 24);
    if (cacheAge < 3) {
      console.log(`cache hit for ${stemUrl}`);
      return NextResponse.json({ llmstxt: cacheData.llmstxt, llmsFulltxt: cacheData.llmsfulltxt });
    }
  }

  let llmstxt = `# ${stemUrl} llms.txt\n\n`;
  let llmsFulltxt = `# ${stemUrl} llms-full.txt\n\n`;

  // 批量爬取网站内容
  if (!urls) {
    throw new Error('URLs are not defined');
  }

  const batchScrapeResult = await app.batchScrapeUrls(urls, {
    formats: ['markdown'],
    onlyMainContent: true,
  });

  if (!batchScrapeResult.success) {
    throw new Error(`Failed to scrape: ${batchScrapeResult.error}`);
  }
  for (const result of batchScrapeResult.data) {
    const metadata = result.metadata;
    const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

    const DescriptionSchema = z.object({
      description: z.string(),
      title: z.string(),
    });

    const completion = await openai.beta.chat.completions.parse({
      model: "gpt-4o-mini",
      messages: [
        {
          role: "user",
          content: `根据以下内容，为该页面生成一个9-10字的描述和一个3-4字的标题：${metadata?.url}。内容如下：${result.markdown}`,
        }
      ],
      response_format: zodResponseFormat(DescriptionSchema, "description"),
    });

    const parsedResponse = completion.choices[0].message.parsed;
    const description = parsedResponse!.description;
    const title = parsedResponse!.title;
   
    llmstxt += `- [${title}](${metadata?.url}): ${description}\n`; 
    llmsFulltxt += result.markdown;
  }

  if (!no_limit) {
    llmstxt = `*注意：生成的 llmstxt.txt 不完整，请输入 Firecrawl API 密钥以获取完整内容，或通过 API 访问 'http://llmstxt.firecrawl.dev/{YOUR_URL}' 获取 llms.txt，或使用 'http://llmstxt.firecrawl.dev/{YOUR_URL}/full' 获取 llms-full.txt。\n\n` + llmstxt;
    llmsFulltxt = `*注意：生成的 llms-full.txt 不完整，请输入 Firecrawl API 密钥以获取完整内容，或通过 API 访问 'http://llmstxt.firecrawl.dev/{YOUR_URL}' 获取 llms.txt，或使用 'http://llmstxt.firecrawl.dev/{YOUR_URL}/full' 获取 llms-full.txt。\n\n` + llmsFulltxt;
  }

  const { data, error } = await supabase
    .from('cache')
    .insert([
      { url: stemUrl, llmstxt: llmstxt, llmsfulltxt: llmsFulltxt, no_limit: no_limit }
    ]);

  if (error) {
    throw new Error(`Failed to insert into Supabase: ${error.message}`);
  }

  return NextResponse.json({ llmstxt: llmstxt, llmsFulltxt: llmsFulltxt });
}
```

#### b) 实现步骤解析

- **目的**：接收链接列表，调用 Firecrawl API 批量爬取内容，利用 OpenAI API 生成描述与标题，组合生成 `llms.txt` 和 `llms-full.txt`，并缓存到 Supabase 数据库。
- **主要函数**：
  - `POST` 函数：处理 POST 请求。
- **关键变量**：
  - `urls`：来自 `/api/map` 的链接列表。
  - `firecrawlApiKey`：Firecrawl API 密钥。
  - `limit`：爬取链接的数量限制。
  - `no_limit`：标识是否使用自定义密钥，影响文本生成的完整性。
  - `supabase`：Supabase 客户端实例。
- **控制流程**：
  1. **解析请求体**：提取 `urls` 和 `bringYourOwnFirecrawlApiKey`。
  2. **确定 API 密钥与限制**：同样基于是否使用自定义密钥调整限制。
  3. **连接 Supabase**：初始化 Supabase 客户端。
  4. **检查缓存**：查询数据库是否已有生成的文本，且缓存未过期（3天内）。
  5. **若缓存命中**：直接返回缓存的数据。
  6. **否则，生成文本**：
     - **调用 Firecrawl 批量爬取**：获取页面内容。
     - **调用 OpenAI 生成描述与标题**：为每个页面内容生成简短描述和标题。
     - **组合生成 `llms.txt` 和 `llms-full.txt`**：将生成的数据整合为最终文本。
  7. **若未使用自定义密钥**：在生成的文本开头添加提示信息，说明文本不完整。
  8. **存储结果到 Supabase**：插入生成的文本内容到数据库。
  9. **返回生成的文本内容**。

- **错误处理**：
  - 未设置 `FIRECRAWL_API_KEY` 时抛出错误。
  - Firecrawl 或 OpenAI API 调用失败时抛出相应错误。
  - Supabase 数据库插入失败时抛出错误。

- **性能考虑**：
  - 通过缓存机制减少重复计算，提高响应速度。
  - 设置 `maxDuration` 避免长时间请求占用资源。
  - 批量爬取与并行处理，提高效率。

#### c) 技术决策与理由

- **缓存机制**：通过 Supabase 数据库缓存生成的文本，避免重复爬取和生成，提升性能和用户体验。
- **批量爬取与生成**：一次性处理多个链接，提高处理效率。
- **使用 Zod 进行响应格式验证**：确保 OpenAI API 的响应符合预期格式，增加系统的鲁棒性。
- **灵活的限制策略**：根据是否使用自定义 API 密钥调整爬取和处理的数量，确保系统的可控性与扩展性。

#### d) 与外部服务/API 的集成点

- **Firecrawl API**：
  - **认证**：通过 API 密钥进行身份验证。
  - **数据格式**：发送批量爬取请求，接收页面内容。
- **OpenAI API**：
  - **认证**：通过 API 密钥访问。
  - **数据格式**：发送对话式消息，接收结构化响应。
- **Supabase 数据库**：
  - **认证**：通过 URL 和密钥连接。
  - **数据格式**：使用 JSON 进行数据的插入与查询。
  
#### e) 重要优化技术

- **缓存机制**：显著减少重复生成，提高响应速度，降低外部 API 调用成本。
- **批量处理**：一次性处理多个链接，减少网络请求次数，提升效率。
- **响应格式验证**：通过 Zod 库确保 OpenAI API 的响应结构，避免潜在的解析错误。

#### f) 配置参数及其影响

- **`FIRECRAWL_API_KEY`**：决定是否能进行大规模爬取，影响生成文本的完整性。
- **`limit`**：限制爬取链接的数量，影响响应时间与生成文本的详细程度。
- **`no_limit`**：控制是否在生成文本中添加提示信息，影响用户了解文本完整性的方式。
- **Supabase 配置**：影响缓存机制的可靠性与性能。

### 3. 前端用户界面实现 (`app/page.tsx`)

#### a) 完整、可运行的代码片段

```typescript
// app/page.tsx

"use client";
import Image from "next/image";
import { useState, useEffect } from "react";

export default function Home() {
  const [apiMessage, setApiMessage] = useState<string>("");
  const [fullApiMessage, setFullApiMessage] = useState<string>("");
  const [inputUrl, setInputUrl] = useState<string>("");
  const [loading, setLoading] = useState<boolean>(false);
  const [showFullText, setShowFullText] = useState<boolean>(false);
  const [bringYourOwnFirecrawlApiKey, setBringYourOwnFirecrawlApiKey] = useState<string>("");
  const [showApiKeyInput, setShowApiKeyInput] = useState<boolean>(false);
  const [apiKeySet, setApiKeySet] = useState<boolean>(false);
  const [mapUrls, setMapUrls] = useState<string[]>([]);
  const [scrapingMessage, setScrapingMessage] = useState<string>("");
  const [apiInfoMessage, setApiInfoMessage] = useState<string>("");

  useEffect(() => {
    let interval: NodeJS.Timeout;
    if (loading && mapUrls.length > 0) {
      let index = 0;
      const messages = [
        (url: string) => `正在爬取 URL: ${url}`,
        (url: string) => `正在提取标题: ${url}`,
        (url: string) => `正在提取描述: ${url}`,
        (url: string) => `正在添加 URL 到 llms.txt: ${url}`
      ];
      interval = setInterval(() => {
        const currentUrl = mapUrls[index];
        setScrapingMessage(messages[index % messages.length](currentUrl));
        index = (index + 1) % mapUrls.length;
      }, 750);
    } else {
      setScrapingMessage("");
    }
    return () => clearInterval(interval);
  }, [loading, mapUrls]);

  const callApi = async () => {
    setLoading(true);
    try {
      const mapResponse = await fetch("/api/map", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ url: inputUrl, bringYourOwnFirecrawlApiKey: bringYourOwnFirecrawlApiKey }),
      });
      const mapData = await mapResponse.json();
      setMapUrls(mapData.mapUrls);
      const llmsResponse = await fetch("/api/service", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ urls: mapData.mapUrls, bringYourOwnFirecrawlApiKey: bringYourOwnFirecrawlApiKey }),
      });
      const data = await llmsResponse.json();
      setApiMessage(data.llmstxt);
      setFullApiMessage(data.llmsFulltxt);
    } catch (error) {
      setApiMessage("调用 API 时出错");
      setFullApiMessage("调用 API 时出错");
    } finally {
      setLoading(false);
    }
  };

  const handleSetApiKey = () => {
    if (bringYourOwnFirecrawlApiKey.trim() === "") {
      alert("API 密钥不能为空");
      return;
    }
    setApiKeySet(true);
    setShowApiKeyInput(false);
  };

  return (
    <div className="flex items-center justify-center min-h-screen p-8 pb-20 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      
      <div className="flex flex-col items-center gap-4">
      <h1 className="text-6xl font-bold font-[family-name:var(--font-geist-mono)] mb-6">llms.txt 生成器</h1>
        <div className="flex items-center gap-4">
          
          <input
            type="text"
            value={inputUrl}
            onChange={(e) => setInputUrl(e.target.value)}
            className="rounded-full border border-solid border-black/[.08] dark:border-white/[.145] transition-colors flex items-center justify-center hover:bg-[#f2f2f2] dark:hover:bg-[#1a1a1a] hover:border-transparent text-sm sm:text-base h-10 sm:h-12 px-4 sm:px-5"
            placeholder="输入 URL"
          />
          <button
            onClick={callApi}
            className="rounded-full border border-solid border-black/[.08] dark:border-white/[.145] transition-colors flex items-center justify-center hover:bg-[#f2f2f2] dark:hover:bg-[#1a1a1a] hover:border-transparent text-sm sm:text-base h-10 sm:h-12 px-4 sm:px-5"
            disabled={loading}
          >
            {loading ? "生成中..." : "生成"}
          </button>
        </div>
        
        {loading && scrapingMessage && (
          <div className="text-sm text-gray-500">{scrapingMessage}</div>
        )}

        <div className="flex flex-col items-center gap-4 w-full">
          <div className="flex items-center gap-2 mt-6">
            {!apiKeySet ? (
              <>
                {showApiKeyInput ? (
                  <>
                    <input
                      type="text"
                      value={bringYourOwnFirecrawlApiKey}
                      onChange={(e) => setBringYourOwnFirecrawlApiKey(e.target.value)}
                      className="rounded-full border border-solid border-black/[.08] dark:border-white/[.145] transition-colors flex items-center justify-center hover:bg-[#f2f2f2] dark:hover:bg-[#1a1a1a] hover:border-transparent text-sm sm:text-base h-10 sm:h-12 px-4 sm:px-5"
                      placeholder="输入 Firecrawl API 密钥"
                    />
                    <button
                      onClick={handleSetApiKey}
                      className="text-blue-500 text-sm"
                    >
                      设置 Firecrawl 密钥 🔥
                    </button>
                  </>
                ) : (
                  <a
                    href="#"
                    onClick={() => setShowApiKeyInput(true)}
                    className="text-blue-500 text-sm"
                  >
                    使用您的 Firecrawl 密钥 🔥
                  </a>
                )}
              </>
            ) : (
              <div className="text-green-500 text-sm">
                Firecrawl API 密钥已设置
              </div>
            )}

            | <a href="#" onClick={() => setApiInfoMessage(apiInfoMessage ? "" : "您可以通过访问 'http://llmstxt.firecrawl.dev/{YOUR_URL}' 来使用 llms.txt 生成器 API，或通过访问 'http://llmstxt.firecrawl.dev/{YOUR_URL}/full' 来获取 llms-full.txt。如果您有 Firecrawl API 密钥，可以在 URL 末尾添加 '?FIRECRAWL_API_KEY=YOUR_API_KEY' 以获取完整结果。")} className="text-blue-500 pointer-events-auto text-sm"> 使用 llms.txt 生成器 API</a>
            
          </div>
          {apiInfoMessage && (
            <div className="relative w-1/2 text-sm text-black">{apiInfoMessage}</div>
          )}

          
          {apiMessage && (
              <>
            <div className="relative w-1/2">
              <div
                className={`text-sm font-[family-name:var(--font-geist-mono)] rounded border border-solid border-black/[.08] dark:border-white/[.145] transition-colors duration-300 ease-in-out hover:bg-[#f2f2f2] dark:hover:bg-[#1a1a1a] hover:border-transparent w-full h-80 p-4 overflow-hidden ${!bringYourOwnFirecrawlApiKey ? 'bg-gradient-to-b from-transparent to-white dark:to-black' : ''}`}
              >
                <div className="relative h-full overflow-auto">
                  <div className="relative whitespace-pre-wrap">
                    {showFullText ? fullApiMessage : apiMessage}
                    {!bringYourOwnFirecrawlApiKey && (
                      <div className="absolute top-0 left-0 w-full h-60 bg-gradient-to-b from-white dark:from-black to-transparent pointer-events-auto flex justify-center">
                        <div className="p-4">
                        仅限 10 页 - 若需完整结果，请获取<a href="https://firecrawl.dev" className="text-blue-500 pointer-events-auto" target="_blank" rel="noopener noreferrer"> 免费 Firecrawl 密钥 🔥</a>
                        </div>
                      </div>
                    )}
                  </div>
                </div>
              </div>
              
              <div className="flex justify-center">
              <button
                onClick={() => navigator.clipboard.writeText(showFullText ? fullApiMessage : apiMessage)}
                className="mt-4 rounded-full border border-solid border-black/[.08] dark:border-white/[.145] transition-colors flex items-center justify-center hover:bg-[#f2f2f2] dark:hover:bg-[#1a1a1a] hover:border-transparent text-sm sm:text-base h-10 sm:h-12 px-4 sm:px-5"
              >
                复制 {showFullText ? "llms-full-txt" : "llms.txt"}
              </button>
              
              <button
                onClick={() => setShowFullText(!showFullText)}
                className="ml-4 mt-4 rounded-full border border-solid border-black/[.08] dark:border-white/[.145] transition-colors flex items-center justify-center hover:bg-[#f2f2f2] dark:hover:bg-[#1a1a1a] hover:border-transparent text-sm sm:text-base h-10 sm:h-12 px-4 sm:px-5"
              >
                {showFullText ? "显示 llms.txt" : "显示 llms-full.txt"}
              </button>
         
            </div>
            </div>
            </>
          )}
        </div>
    
      </div>
    </div>
  );
}
```

#### b) 实现步骤解析

- **目的**：提供友好的用户界面，允许用户输入网址、设置 API 密钥，并展示生成的文本内容。
- **主要函数与逻辑**：
  - `useState` Hook：管理组件状态，包括输入的网址、生成的文本、加载状态等。
  - `useEffect` Hook：在加载过程中，动态显示爬取状态消息。
  - `callApi` 函数：处理 API 调用逻辑，分别调用 `/api/map` 和 `/api/service`，并更新状态。
  - `handleSetApiKey` 函数：处理用户设置 Firecrawl API 密钥的逻辑。
- **关键变量**：
  - `inputUrl`：用户输入的目标网址。
  - `apiMessage` & `fullApiMessage`：存储生成的 `llms.txt` 和 `llms-full.txt` 内容。
  - `loading`：表示是否正在生成文本。
  - `showFullText`：控制是否展示完整文本。
  - `bringYourOwnFirecrawlApiKey`：用户输入的 Firecrawl API 密钥。
  - `mapUrls`：存储爬取到的 URL 列表。
  - `scrapingMessage`：显示爬取状态信息。
  - `apiInfoMessage`：显示 API 信息提示。
- **控制流程**：
  1. **用户输入网址**，点击“生成”按钮。
  2. **调用 `callApi` 函数**：
     - **设置加载状态**。
     - **发送 POST 请求到 `/api/map`**，获取链接列表。
     - **发送 POST 请求到 `/api/service`**，获取生成的文本内容。
     - **更新状态**，显示生成结果。
     - **处理异常**，显示错误信息。
  3. **用户可选择设置 Firecrawl API 密钥**，影响生成文本的完整性。
  4. **生成的文本内容展示**，用户可进行复制或切换显示内容。
- **错误处理**：
  - 弹出提示 if API 密钥为空时尝试设置。
  - 捕获 API 调用中的异常，显示错误信息。
- **性能考虑**：
  - 使用状态管理和条件渲染，确保界面的响应速度与用户体验。

#### c) 技术决策与理由

- **React Hooks**：利用 `useState` 和 `useEffect` 管理组件状态和副作用，简化组件逻辑。
- **条件渲染**：根据状态动态展示不同的 UI 元素，提高交互性和用户体验。
- **异步处理**：使用 `async/await` 处理 API 请求，确保代码的可读性和可维护性。
- **用户提示**：在没有设置 API 密钥的情况下，提示用户获取完整结果，促进用户进行必要的配置。

#### d) 与外部服务/API 的集成点

- **调用后端 API**：
  - `/api/map`：获取网站链接列表。
  - `/api/service`：生成文本内容。
- **浏览器 API**：
  - `navigator.clipboard`：实现复制功能，提升用户操作便捷性。

#### e) 重要优化技术

- **动态状态消息**：在爬取过程中，实时更新爬取状态，提升用户的感知反馈。
- **缓存机制**：结合后端的缓存策略，减少重复生成，提升性能。
- **响应式设计**：使用 Tailwind CSS 实现响应式布局，确保在不同设备上的良好显示效果。

#### f) 配置参数及其影响

- **输入域与按钮**：提供用户友好的输入和操作控件，影响用户体验的流畅性。
- **API 密钥设置**：影响生成文本的完整性和服务的可用性。
- **生成按钮的禁用状态**：在加载过程中禁用按钮，防止重复请求，确保系统稳定性。

### 4. 动态路由处理 (`app/[...slug]/route.ts`)

#### a) 完整、可运行的代码片段

```typescript
// app/[...slug]/route.ts

import { NextRequest, NextResponse } from 'next/server';

export const maxDuration = 300;

export async function GET(
  request: NextRequest,
  { params }: { params: Promise<{ slug: string[] }> }
) {
  try {
    const resolvedParams = await params;
    const targetUrl = decodeURIComponent(resolvedParams.slug.join('/'));
    const { searchParams } = new URL(request.url);
    const firecrawlApiKey = searchParams.get('FIRECRAWL_API_KEY') || request.headers.get('FIRECRAWL_API_KEY');

    // 准备请求体给 /api/map
    const mapRequestBody = {
      url: targetUrl,
      bringYourOwnFirecrawlApiKey: firecrawlApiKey,
    };

    // 发送 POST 请求到 /api/map
    const mapResponse = await fetch(`${request.nextUrl.origin}/api/map`, {
      method: 'POST',
      body: JSON.stringify(mapRequestBody),
    });

    if (!mapResponse.ok) {
      const errorText = await mapResponse.text();
      return NextResponse.json(
        { error: `来自 /api/map 的错误: ${errorText}` },
        { status: mapResponse.status }
      );
    }

    const mapData = await mapResponse.json();

    // 准备请求体给 /api/service
    const serviceRequestBody = {
      urls: mapData.mapUrls,
      bringYourOwnFirecrawlApiKey: firecrawlApiKey,
    };

    // 发送 POST 请求到 /api/service
    const serviceResponse = await fetch(`${request.nextUrl.origin}/api/service`, {
      method: 'POST',
      body: JSON.stringify(serviceRequestBody),
    });

    if (!serviceResponse.ok) {
      const errorText = await serviceResponse.text();
      return NextResponse.json(
        { error: `来自 /api/service 的错误: ${errorText}` },
        { status: serviceResponse.status }
      );
    }

    const serviceData = await serviceResponse.json();

    if (resolvedParams.slug[resolvedParams.slug.length - 1] === 'full') {
      const llmsFulltxt = serviceData.llmsFulltxt;
      if (!llmsFulltxt) {
        console.error('llmsfulltxt 未定义');
        return NextResponse.json(
          { error: 'llmsfulltxt 未定义' },
          { status: 500 }
        );
      }

      const prettyPrintedFullTxt = JSON.stringify({ llmsfulltxt: llmsFulltxt }, null, 2)
        .replace(/\\n/g, '\n')
        .replace(/\\t/g, '\t')
        .replace(/^\{\s*"llmsfulltxt":\s*"/, '')
        .replace(/"\s*\}$/, '');

      return new Response(prettyPrintedFullTxt, {
        headers: { 'Content-Type': 'application/json' },
      });
    } else {
      const llmstxt = serviceData.llmstxt;

      const prettyPrintedData = JSON.stringify({ llmstxt: llmstxt }, null, 2)
        .replace(/\\n/g, '\n')
        .replace(/\\t/g, '\t')
        .replace(/^\{\s*"llmstxt":\s*"/, '')
        .replace(/"\s*\}$/, '');

      return new Response(prettyPrintedData, {
        headers: { 'Content-Type': 'application/json' },
      });
    }
  } catch (error) {
    console.error('错误:', error);
    return NextResponse.json(
      { error: '发生意外错误' },
      { status: 500 }
    );
  }
}
```

#### b) 实现步骤解析

- **目的**：处理动态路由请求，根据 URL 路径和参数生成相应的 `llms.txt` 或 `llms-full.txt`。
- **主要函数**：
  - `GET` 函数：处理 GET 请求。
- **关键变量**：
  - `slug`：URL 路径参数，包含目标网址及可选的 `full` 标志。
  - `targetUrl`：解码后的目标网址。
  - `firecrawlApiKey`：从查询参数或请求头中获取的 Firecrawl API 密钥。
  - `mapData`：来自 `/api/map` 的链接列表。
  - `serviceData`：来自 `/api/service` 的生成文本。
- **控制流程**：
  1. **解析 URL 路径参数**：拼接目标网址，并解码。
  2. **获取 Firecrawl API 密钥**：优先从查询参数中获取，否则从请求头获取。
  3. **调用 `/api/map` 接口**：获取链接列表。
  4. **检查 `/api/map` 的响应状态**：若失败，返回相应错误。
  5. **调用 `/api/service` 接口**：生成文本内容。
  6. **检查 `/api/service` 的响应状态**：若失败，返回相应错误。
  7. **根据路径参数决定返回 `llms.txt` 还是 `llms-full.txt`**：
     - 若路径末尾为 `full`，返回 `llms-full.txt`。
     - 否则，返回 `llms.txt`。
  8. **格式化响应内容**：将 JSON 转换为易读的文本格式。
  9. **错误处理**：捕获异常，返回统一的错误响应。

- **错误处理**：
  - `/api/map` 或 `/api/service` 调用失败时，返回详细错误信息。
  - 若生成的文本内容缺失，返回服务器错误。

- **性能考虑**：
  - 设置 `maxDuration` 为300秒，避免长时间请求占用资源。
  - 通过集中处理 API 调用与响应，优化请求链路。

#### c) 技术决策与理由

- **统一的错误处理**：通过捕获异常并返回统一的错误响应，确保客户端能够正确处理各种失败情况。
- **动态内容返回**：根据路径参数灵活返回不同版本的文本文件，提升接口的灵活性与扩展性。
- **响应格式优化**：通过正则替换优化 JSON 响应的可读性，增强用户体验。

#### d) 与外部服务/API 的集成点

- **内部 API 调用**：
  - 调用 `/api/map` 获取链接列表。
  - 调用 `/api/service` 生成文本内容。
- **Firecrawl API 密钥获取**：
  - 从查询参数或请求头中获取，支持用户自定义配置。

#### e) 重要优化技术

- **批量请求处理**：通过集中调用内部 API，减少客户端与服务器之间的通信次数，提升效率。
- **动态内容生成**：根据路径参数灵活生成响应内容，适应不同的需求。

#### f) 配置参数及其影响

- **URL 路径参数**：决定生成哪种类型的文本文件，影响最终用户获取的数据内容。
- **Firecrawl API 密钥来源**：支持用户自定义 API 密钥，影响生成文本的完整性与限制。

### 5. 缓存机制与数据库交互 (`app/api/service/route.ts`)

#### a) 完整、可运行的代码片段（摘录相关部分）

```typescript
// app/api/service/route.ts（相关部分）

import { createClient } from '@supabase/supabase-js'

// ...

export const supabaseUrl = process.env.SUPABASE_URL;
export const supabaseKey = process.env.SUPABASE_KEY;
export const supabase = createClient(supabaseUrl!, supabaseKey!);

const { data: cacheData, error: cacheError } = await supabase
  .from('cache')
  .select('llmstxt, llmsfulltxt, cached_at')
  .eq('url', stemUrl)
  .eq('no_limit', no_limit)
  .single();

if (cacheError) {
  console.log('no cache hit');
} else if (cacheData) {
  const cacheAge = (new Date().getTime() - new Date(cacheData.cached_at).getTime()) / (1000 * 60 * 60 * 24);
  if (cacheAge < 3) {
    console.log(`cache hit for ${stemUrl}`);
    return NextResponse.json({ llmstxt: cacheData.llmstxt, llmsFulltxt: cacheData.llmsfulltxt });
  }
}

// ... 生成文本内容 ...

const { data, error } = await supabase
  .from('cache')
  .insert([
    { url: stemUrl, llmstxt: llmstxt, llmsfulltxt: llmsFulltxt, no_limit: no_limit }
  ]);

if (error) {
  throw new Error(`Failed to insert into Supabase: ${error.message}`);
}
```

#### b) 实现步骤解析

- **目的**：通过 Supabase 数据库实现生成文本内容的缓存，提升性能，减少重复生成。
- **关键函数与逻辑**：
  - **连接 Supabase**：使用环境变量中的 URL 和密钥，初始化 Supabase 客户端。
  - **查询缓存**：
    - 查询表 `cache` 中是否已有对应 `url` 和 `no_limit` 的记录。
    - 如果有，计算缓存的时间是否在3天内。
    - 若缓存有效，返回缓存的数据，跳过生成过程。
  - **存储缓存**：
    - 在生成新的文本内容后，将其插入到 `cache` 表中，包含 `url`、`llmstxt`、`llmsfulltxt`、`no_limit` 和 `cached_at` 时间戳。
- **关键变量**：
  - `supabase`：Supabase 客户端实例。
  - `cacheData`：查询到的缓存数据。
  - `cacheError`：查询过程中的错误信息。
  - `cacheAge`：缓存数据的年龄，以天为单位。
- **控制流程**：
  1. **初始化 Supabase 客户端**。
  2. **查询缓存**：根据 `stemUrl` 和 `no_limit` 查询缓存表。
  3. **检查缓存**：
     - 若查询失败，记录无缓存命中。
     - 若查询成功，计算缓存年龄。
     - 若缓存未过期，返回缓存数据。
  4. **生成文本内容**。
  5. **存储生成的内容**：将新的 `llms.txt` 和 `llms-full.txt` 及其相关信息插入缓存表。
- **错误处理**：
  - 查询 Supabase 结果的错误处理，记录日志。
  - 插入缓存失败时，抛出错误并返回服务器错误。

- **性能考虑**：
  - **缓存机制**：减少重复生成，提高系统效率和响应速度。
  - **缓存时间策略**：设定3天的缓存有效期，平衡数据的新鲜度与生成性能。

#### c) 技术决策与理由

- **选择 Supabase**：提供简便的数据库操作接口，适配快速开发需求。
- **缓存有效期设定**：3天为缓存有效期，确保数据的时效性与生成性能的平衡。
- **表结构设计**：
  - `cache` 表包含 `url`、`llmstxt`、`llmsfulltxt`、`no_limit` 和 `cached_at`，满足多维度查询与缓存管理需求。

#### d) 与外部服务/API 的集成点

- **Supabase 数据库**：
  - **连接认证**：通过 URL 和密钥进行认证，确保数据访问安全。
  - **数据操作**：使用 Supabase 的查询与插入接口，简化数据库操作流程。
  
#### e) 重要优化技术

- **缓存预检**：在生成文本前检查缓存，减少不必要的生成操作。
- **自动化时间计算**：动态计算缓存数据的年龄，提高判断的准确性。

#### f) 配置参数及其影响

- **`SUPABASE_URL` 和 `SUPABASE_KEY`**：连接 Supabase 数据库的必要配置，影响数据的读写能力。
- **缓存有效期**：通过代码设定，为3天，影响数据的新鲜度与系统性能的平衡。

### 6. OpenAI API 集成与响应格式验证

#### a) 完整、可运行的代码片段（摘录相关部分）

```typescript
// app/api/service/route.ts（相关部分）

import OpenAI from "openai";
import { zodResponseFormat } from "openai/helpers/zod";
import { z } from "zod";

// ...

const DescriptionSchema = z.object({
  description: z.string(),
  title: z.string(),
});

const completion = await openai.beta.chat.completions.parse({
  model: "gpt-4o-mini",
  messages: [
    {
      role: "user",
      content: `根据以下内容，为该页面生成一个9-10字的描述和一个3-4字的标题：${metadata?.url}。内容如下：${result.markdown}`,
    }
  ],
  response_format: zodResponseFormat(DescriptionSchema, "description"),
});

const parsedResponse = completion.choices[0].message.parsed;
const description = parsedResponse!.description;
const title = parsedResponse!.title;
```

#### b) 实现步骤解析

- **目的**：利用 OpenAI API 为每个爬取的页面内容生成简短描述和标题，丰富 `llms.txt` 的内容。
- **主要函数与逻辑**：
  - **初始化 OpenAI 客户端**：使用环境变量中的 API 密钥。
  - **定义响应模式**：使用 Zod 库定义期望的响应结构，包括 `description` 和 `title`。
  - **发送请求**：构建对话式消息，包含 URL 和页面内容，向 OpenAI API 请求生成描述与标题。
  - **解析响应**：使用 Zod 进行结构化响应验证，提取生成的 `description` 和 `title`。
- **关键变量**：
  - `openai`：OpenAI 客户端实例。
  - `DescriptionSchema`：使用 Zod 定义的响应结构模式。
  - `completion`：从 OpenAI API 接收到的完整响应。
  - `parsedResponse`：经过验证和解析后的响应内容。
- **控制流程**：
  1. **定义响应模式**：确保 OpenAI 返回的数据符合预期结构。
  2. **构建消息内容**：向 OpenAI 提供 URL 和页面内容，指示生成描述与标题。
  3. **发送请求并等待响应**。
  4. **解析并验证响应**：
     - 使用 Zod 解析 OpenAI 的响应，确保包含 `description` 和 `title`。
     - 提取并返回生成的内容。

- **错误处理**：
  - 若 OpenAI 返回的响应不符合预期结构，Zod 将抛出验证错误，需在上层捕获并处理。
  - 捕获 OpenAI API 调用中的异常，确保系统稳定性。

- **性能考虑**：
  - 使用异步请求，提高处理效率。
  - 最小化传输数据量，仅传递必要的内容，提高响应速度。

#### c) 技术决策与理由

- **使用 Zod 进行响应验证**：确保从 OpenAI API 接收到的数据符合预期结构，提升系统的鲁棒性和安全性。
- **对话式消息构建**：明确指示模型生成所需的信息，提升生成质量。
- **异步处理**：利用异步请求，确保系统的高效性与响应性。

#### d) 与外部服务/API 的集成点

- **OpenAI API**：
  - **认证**：通过 API 密钥访问。
  - **数据格式**：发送包含消息的 JSON 请求，接收包含生成内容的 JSON 响应。
  - **响应处理**：使用 Zod 验证响应结构，提取生成的数据。

#### e) 重要优化技术

- **响应模式验证**：通过 Zod 定义响应结构，提前捕获数据格式错误，避免后续处理中的异常。
- **精准的消息指令**：在消息中明确要求生成特定长度的描述和标题，提高生成内容的准确性和实用性。

#### f) 配置参数及其影响

- **`model`**：指定使用的模型类型，例如 `gpt-4o-mini`，影响生成内容的质量与成本。
- **`response_format`**：通过 Zod 定义的响应格式，影响数据的解析与验证过程。

## 结论

通过对 **llmstxt Generator** 项目的深入分析，我们了解了其系统架构、主要组件功能、关键实现细节以及与外部服务的集成方式。该项目巧妙地结合了 Firecrawl 的网站爬取能力、OpenAI 的语言生成能力与 Supabase 的数据库缓存机制，实现了高效、灵活的文本生成解决方案。在实际应用中，这种模块化、集成化的设计思路不仅提升了系统的性能与用户体验，也为开发者提供了宝贵的借鉴经验，助力构建类似的高效数据处理与生成系统。

---

**免责声明**：本文基于开源项目 **llmstxt Generator** 的公开代码及文档进行分析，旨在提供技术学习与交流之用。所有代码及设计概念均归原作者所有，未经授权，请勿用于商业用途。