---
title: "ParserGPT (Public Beta Coming Soon): Turn messy websites into clean CSVs"
source: "https://medium.com/@ayush.shrivastava016/parsergpt-public-beta-coming-soon-turn-messy-websites-into-clean-csvs-dd8c7199ca97"
author:
  - "[[Ayush Shrivastava]]"
published: 2025-09-19
created: 2025-09-19
description: "ParserGPT (Public Beta Coming Soon): Turn messy websites into clean CSVs Heads-up: I’ve built ParserGPT to solve “scrape site, reliably.” I’m polishing the release, beta is coming soon. If …"
tags:
  - "Ayush Shrivastava"
status: "inbox"
importance: 2
effort: 2
review_level: 0
review_next: "2025-10-17"
review_interval: null
review_count: 0
decision: null
topics: []
links_out: []
summary: ""
pov: ""
actions: []
---
[Sitemap](https://medium.com/sitemap/sitemap.xml)

> ***注意：*** *我开发 ParserGPT 是为了解决“可靠地抓取网站”这一问题。我正在完善发布工作，* ***公测版即将推出*** *。*

如果你尝试过抓取“任何网站”，你就会遇到混乱的情况：标记不一致、动态内容、随机的反机器人技巧，还有那一页毫无合理理由地把年份放在图像替代文本标签里。一个简单的 BeautifulSoup 脚本只能用于 *一个* 网站。我想要一种通用的方法：

- 了解数据在网站上的位置（选择器、模式）。
- 使用那些学到的规则进行确定性且快速的运行。
- 仅在实际有帮助时才使用 LLM（严格的、经过验证的 JSON）。

**ParserGPT** 就是这样一个系统。可以把它想象成一个 **编译器** ：LLM 为每个域名 “编译” **选择器** （CSS/XPath/正则表达式），然后运行时快速且低成本地执行这些规则。当规则缺失时，一个受保护的 LLM 步骤会填补空白。

## Sneak Peek

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*6-xPCroiGRgVVsNqis_O7A.gif)

## ParserGPT 是一个由两部分组成的机器：

- **学习者（人工智能辅助）** ：查看网站的几页内容， **找出数据所在位置** 。它会为该网站输出一个名为 **适配器** 的小“配方”（基本上是：CSS/XPath 选择器和正则表达式）。这由 **LangChain** （提示和解析）和 **LangGraph** （一个运行“提议→验证→修复→保存”的微型状态机）提供支持。
- **运行器（确定性）** ：使用该适配器在许多页面上 **快速且低成本地提取数据** 。如果某个值缺失，它会仅针对该字段、仅在该页面上且仅在经过严格验证的 JSON 中请求 LLM 一次来填补空白。

## 架构概览（附用于理解的简短、重点突出的代码片段）

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*WHYG2nIB-2H8uP-MXb7gEg.png)

### 步骤 1：获取数据（FastAPI）

- 代码编号 0：POST /jobs → 启动一个任务并返回代码编号 1：job\_id
- `GET /jobs/{id}` → 检查状态
- `GET /jobs/{id}/csv` → 下载（或流式传输）CSV
```c
# app/main.py (minimal)
import asyncio, os
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from .models import Base, engine, SessionLocal, Job
from .orchestrator import run_job

app = FastAPI()

@app.on_event("startup")
def boot():
    Base.metadata.create_all(bind=engine)

@app.post("/jobs")
async def create_job(payload: dict):
    s = SessionLocal()
    try:
        job = Job(
          start_url=payload["start_url"],
          allowed_domains=",".join(payload.get("allowed_domains", [])),
          max_depth=int(payload.get("max_depth", 1)),
          max_pages=int(payload.get("max_pages", 10)),
          field_spec=payload["field_spec"],
          status="started",
        )
        s.add(job); s.commit(); s.refresh(job)
        asyncio.create_task(run_job(job, adapter=None, db=None))  # inject your adapter+db
        return {"job_id": job.id, "status": "started"}
    finally:
        s.close()

@app.get("/jobs/{job_id}/csv")
def csv(job_id: int):
    path = f"job_{job_id}.csv"
    if not os.path.exists(path): raise HTTPException(404, "csv not ready")
    return FileResponse(path, media_type="text/csv", filename=os.path.basename(path))
```

### 步骤2 — 编排器

这一层决定适配器（即，是否存在经过学习的数据 JSON）

### 步骤 3 — 学习适配器（LLM + LangGraph）

目标是为每个域名生成一个小的 JSON 文件，记录字段所在位置（JSON 的压缩版本）

```c
{
  "domain": "example.com",
  "version": 1,
  "url_patterns": {
    "detail": ["*/college/*", "*university*"],
    "list":   ["*/colleges/*", "*ranking*"]
  },
  "selectors": {
    "college_name":    { "css": "h1, .page-title", "xpath": "", "regex": "" },
    "courses_offered": { "css": ".courses li",     "xpath": "", "regex": "" },
    "year_founded":    { "css": "", "xpath": "//text()[contains(.,'Founded')]", "regex": "(?:Estd\\.?|Established)\\s*(\\d{4})" }
  },
  "tests": [
    { "url": "https://example.com/college/abc", "expects": { "college_name": "ABC College" } }
  ]
}
```

3.1 我们收集具有代表性的 **列表** 页面和 **详细** 页面。当网站阻止爬虫时，我们使用 **Playwright** （真实的 Chrome、持久化配置文件、逼真的头部信息）。

```c
# sampling.py
import httpx, asyncio
from playwright.async_api import async_playwright

async def fetch_httpx(url: str) -> str:
    async with httpx.AsyncClient(follow_redirects=True, timeout=30.0, http2=True) as c:
        r = await c.get(url, headers={"User-Agent": "Mozilla/5.0"})
        return r.text if r.status_code == 200 and "text" in r.headers.get("content-type","") else ""

async def fetch_playwright(url: str) -> str:
    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(
            user_data_dir="./pw-profile", headless=False,
            args=["--disable-blink-features=AutomationControlled"]
        )
        page = await ctx.new_page()
        await page.add_init_script("Object.defineProperty(navigator,'webdriver',{get:()=>undefined});")
        await page.goto(url, wait_until="load", timeout=60000)
        await page.wait_for_timeout(2500)
        html = await page.content()
        await ctx.close()
        return html

async def sample_pages(seed_url: str, max_samples=6):
    # naive: start with seed, follow a few in-domain links (omitted for brevity)
    html = await fetch_httpx(seed_url) or await fetch_playwright(seed_url)
    return [{"url": seed_url, "html": html}]  # add more discovered samples
```

**3.2 提出选择器（LLM 返回严格的 JSON）**

使用 **LangChain** 并通过 **PydanticOutputParser** 强制生成有效的 JSON。

```c
# propose.py
from pydantic import BaseModel, Field
from typing import Dict
from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

class AdapterDraft(BaseModel):
    url_patterns: Dict[str, list] = Field(default_factory=dict)
    selectors: Dict[str, Dict[str, str]] = Field(default_factory=dict)

parser = PydanticOutputParser(pydantic_object=AdapterDraft)
PROMPT = ChatPromptTemplate.from_messages([
    ("system",
     "You propose extraction rules for given HTML samples and a field spec. "
     "Return ONLY valid JSON with keys: url_patterns, selectors. "
     "selectors uses CSS/XPath/regex; keep them precise and minimal."),
    ("human",
     "FIELDS (name:dtype): {fields}\n\n"
     "SAMPLES (trimmed HTML):\n{samples}\n\n"
     "{format_instructions}")
])

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

async def propose_adapter(fields: list, samples: list) -> AdapterDraft:
    samples_txt = "\n\n---\n\n".join(s["html"][:8000] for s in samples)
    msg = {
        "fields": ", ".join(f"{f['name']}:{f['dtype']}" for f in fields),
        "samples": samples_txt,
        "format_instructions": parser.get_format_instructions()
    }
    return await (PROMPT | llm | parser).ainvoke(msg)
```

**3.3 验证、修复、保存（LangGraph 风格的循环）**

## 在收件箱中获取阿尤什·什里瓦斯塔瓦的故事

免费加入 Medium，获取这位作者的更新内容。

我们将选择器应用于样本，并测量 **覆盖率** 和 **形状** 。如果覆盖率小于阈值，我们将未命中的部分反馈给模型，以请求 **最小差异** ，而不是重写。

### 步骤4：运行提取（确定性；所有页面）

现在我们在范围内进行爬取，并使用 **适配器** 来提取。（非常简洁的代码示例）

```c
# extractor.py
from bs4 import BeautifulSoup
import json, re

def extract_with_adapter(html: str, adapter: dict, field_spec: list) -> dict:
    soup = BeautifulSoup(html, "lxml")
    out = {}
    for f in field_spec:
        name = f["name"]
        sel  = adapter["selectors"].get(name, {})
        values = []
        if sel.get("css"):
            values += [e.get_text(" ", strip=True) for e in soup.select(sel["css"])]
        if sel.get("xpath"):
            pass  # add lxml xpath if you need it
        if sel.get("regex"):
            values += re.findall(sel["regex"], soup.get_text(" ", strip=True), re.I)

        # normalize dtype
        if f["dtype"].endswith("[]"):
            out[name] = [v for i, v in enumerate(values) if v and v not in values[:i]]
        else:
            out[name] = values[0] if values else ""
    return out
```

**为何此方法可行：** 提取现在只需从已知位置读取数据。它速度快、可预测且成本极低。

### 步骤 5 — 回退（仅针对缺失字段使用 LLM，严格遵循 JSON 格式）

如果给定页面上的必填字段为空 **，我们仅向大语言模型（LLM）询问该字段。仅此而已。我们使用 Pydantic 进行解析，因此 **错误的 JSON 会被拒绝** 。**

```c
# fallback.py
from pydantic import BaseModel
from typing import List
from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

class Row(BaseModel):
    college_name: str = ""
    courses_offered: List[str] = []
    year_founded: str = ""

parser = PydanticOutputParser(pydantic_object=Row)
PROMPT = ChatPromptTemplate.from_messages([
    ("system",
     "Extract only the requested fields from HTML. "
     "Return ONLY valid JSON matching the schema. "
     "If unknown, use empty string or empty list."),
    ("human",
     "URL: {url}\n\nHTML (truncated):\n{snippet}\n\n"
     "Schema: college_name(string), courses_offered(string[]), year_founded(string)\n"
     "{format_instructions}")
])
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

async def llm_fill(url: str, html: str) -> Row:
    return await (PROMPT | llm | parser).ainvoke({
        "url": url,
        "snippet": html[:12000],
        "format_instructions": parser.get_format_instructions()
    })

def merge(det: dict, llm_row: Row, prefer=set()) -> dict:
    r = det.copy()
    for k, v in llm_row.dict().items():
        if k in prefer and v not in ("", [], None):
            r[k] = v
        elif not r.get(k) and v not in ("", [], None):
            r[k] = v
    return r
```

注意： **我们不会对整个页面进行“大语言模型处理”** 。我们只询问适配器遗漏的内容，每次一个字段，严格按照 JSON 格式，然后进行合并。

### 步骤 6：将数据推送到 Postgres（ 存储 + 导出 ）

- 将原始 HTML 和提取的行存储在 **Postgres** 中，以便我们以后可以重现结果、重新导出 CSV 或重新学习适配器。
- 流式传输或下载 **CSV** 。数组以 JSON 形式进入一个单元格（之后很容易展开）。

## 让我们了解一下所使用的工具和术语：

1. **大语言模型（LLM）：** 该模型读取一段 HTML 和用户请求的字段，并指出这些字段所在的位置（选择器），或者在规则失败时为您提供值。我们对其进行严格限制：仅接受严格的 JSON 格式，并通过法典进行验证。
2. **LangChain：** 一个用于构建 LLM 管道的 Python 库。  
	想象一下乐高积木：  
	用于使用变量（{schema}，{html}）构建清晰指令的 ***PromptTemplate***  
	***聊天模型*** （支持 OpenAI 或 Ollama，不过为节省成本可使用 Ollama）。  
	***输出解析器*** （例如，PydanticOutputParser），它强制大型语言模型（LLM）返回与你的模式匹配的有效 JSON。如果不匹配，我们会捕获错误，而不是默默接受无效内容。
3. **LangGraph：** 一个构建在 LangChain 之上的微型状态机。我们定义了节点（“提出选择器”、“验证选择器”、“修复选择器”）和边（下一步要做什么）。为什么呢？因为选择器学习是一个包含决策的循环，而不是单次调用。LangGraph 使其具有可预测性、可恢复性和可调试性。
4. **适配器：** 每个域名对应一个小 JSON 文件（例如，adapters/shiksha.com.json）  
	That says:  
	对于 college\_name → CSS：“h1,.page-title”，可能还需要一个备用的 XPath/正则表达式。  
	对于 courses\_offered\[\] → CSS：“.courses li” 等  
	这就是确定性提取器所使用的“方法”。
5. **字段规范：** 用户针对此任务的模式。用户想要的列及其类型。
6. **确定性提取：** 使用 BeautifulSoup/XPath/正则表达式应用适配器选择器。它快速、成本低且可重复。这是我们的主要引擎。
7. **LLM 提取** （备用方法，成本高昂 😭）：仅在确定性方法遗漏所需字段时使用。我们使用 HTML + 模式提示 LLM，并使用严格的 JSON 解析器解析答案。我们逐字段合并结果（从不覆盖良好的确定性值）。
8. **获取器：** 首先尝试使用 httpx（速度快）。如果网站阻止爬虫（出现“访问被拒绝”），我们会使用带有持久化 Chrome 配置文件和逼真头部信息的 Playwright。这表现得就像一个真实的浏览器。
9. FastAPI：服务包装器。异步 POST /jobs 调度爬取任务；CSV 端点提供最终文件或实时流。
10. **Postgres：** 数据库。我们存储职位信息、页面（原始 HTML）和提取内容（JSON）。
11. **CSV：** 用户下载的文件。

## 在设计 ParserGPT 之前我问自己的问题

**为什么不直接让模型读取页面并给我一个 CSV 文件呢？**  
由于它速度慢、成本高且容易出现偏差，一次性学习选择器能为你带来 **速度 + 控制** 。然后，大语言模型（LLM）只填补真正的空白。

**这在一个网站之外还能行吗？**  
是的。适配器是按域名的，但 **学习循环** 在任何地方都是相同的。新网站？运行学习者，然后让运行器进行扩展。

**如果网站发生变化怎么办？**  
覆盖率下降 → 学习者的 **修复** 步骤会调整适配器。这是一个小更新，而非重写。

> ParserGPT 的理念很简单： **一次学习，快速运行** 。大语言模型（LLM）处理模糊部分，学习结构并填补空白，而确定性代码则快速浏览页面。

### 幕后（适配器学习）

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*Mil3ZwGi3PKD-2NxenQ85g.gif)

## 来自 Medium 的推荐

[

See more recommendations

](https://medium.com/?source=post_page---read_next_recirc--dd8c7199ca97---------------------------------------)

[Open in Google Cache](http://webcache.googleusercontent.com/search?q=cache:https://medium.com/@ayush.shrivastava016/parsergpt-public-beta-coming-soon-turn-messy-websites-into-clean-csvs-dd8c7199ca97&strip=0&vwsrc=1&referer=medium-parser) [Open in Read-Medium](https://readmedium.com/en/https://medium.com/@ayush.shrivastava016/parsergpt-public-beta-coming-soon-turn-messy-websites-into-clean-csvs-dd8c7199ca97) [Open in Freedium](https://freedium.cfd/https://medium.com/@ayush.shrivastava016/parsergpt-public-beta-coming-soon-turn-messy-websites-into-clean-csvs-dd8c7199ca97) [Open in Archive](https://archive.today/?url=https://medium.com/@ayush.shrivastava016/parsergpt-public-beta-coming-soon-turn-messy-websites-into-clean-csvs-dd8c7199ca97&run=1&referer=medium-parser) [Open in Proxy API](https://medium-parser.vercel.app/?url=https://medium.com/@ayush.shrivastava016/parsergpt-public-beta-coming-soon-turn-messy-websites-into-clean-csvs-dd8c7199ca97)

Iframe/gist/embeds are not loaded in the Google Cache proxy. For those, please use the Read-Medium/Archive proxy instead.

Having an issue?  
[Open a ticket](https://github.com/Xatta-Trone/medium-parser-extension/issues/new) or [mail here](https://medium.com/@ayush.shrivastava016/)