---
title: "2025-11-20_llamaindex_ai_立即报名参加我们的网络研讨会_超越_OCR_AI_智能体如何解析复杂文档_https"
source: "https://www.llamaindex.ai/blog/observability-in-agentic-document-workflows?utm_source=socials&utm_medium=li_social"
author:
  - "[[@step]]"
published: 2025-11-20
created: 2025-11-20
description:
tags:
  - "#the"
  - "#why"
  - "llamaindex"
  - "@step"
---

# [📣 立即报名参加我们的网络研讨会：超越 OCR：AI 智能体如何解析复杂文档 📣](https

[📣 立即报名参加我们的网络研讨会：超越 OCR：AI 智能体如何解析复杂文档 📣](https://landing.llamaindex.ai/beynd-ocr-how-ai-agents-parse-complex-docs) ![](https://cdn.sanity.io/images/7m9jw85w/production/42d975520edd80d57371d9e3342d1a2525471162-1200x676.png?w=1200)

- [多步骤文档处理的挑战](#the-challenge-of-multi-step-document-processing)
- [为何文档工作流的可观测性至关重要](#why-observability-matters-for-document-workflows)
- [使用 LlamaIndex 构建可观测文档工作流](#building-observable-document-workflows-with-llamaindex)
- [1\. Setup](#1-setup)
- [2\. The workflow](#2-the-workflow)
- [3\. Observability](#3-observability)
- [4\. 运行与检查追踪](#4-running-and-inspecting-traces)
- [5\. 创建自定义事件追踪](#5-creating-custom-event-traces)
- [Wrapping Up](#wrapping-up)

## 多步骤文档处理的挑战

文档工作流是众多业务运营的核心环节：处理发票、从财务报表中提取数据、分析合同，以及将非结构化的 PDF 文件转化为可执行的洞察。这些工作流通常包含多个步骤（如分类、提取、验证和整合），每个步骤都由需要基于文档内容做出决策的 AI 智能体来协调执行。

设想一个财务文档处理流程：您收到一份 PDF 文件，可能是利润表、资产负债表或现金流量表。您的系统需要：

1.  对文档类型进行分类
2.  根据该分类提取相关的结构化数据
3.  验证提取的信息
4.  将其路由至相应的下游流程

这些步骤中的每一步都涉及对非结构化内容的人工智能推理，一旦出现问题——比如错误分类、遗漏字段或验证失败——在没有适当可见性的情况下，调试就会变成一场噩梦。

## 为何可观测性对文档工作流至关重要

这正是可观测性至关重要的地方。在由 AI 智能体驱动的文档工作流中，你需要了解：

- 非结构化上下文如何转化为结构化输出
- 做出了哪些分类决策及其原因
- 成功提取的数据与失败的数据对比
- 验证或合成环节出现故障之处
- 您工作流中每个步骤的性能特征

与传统软件可使用打印语句调试不同，AI 驱动的文档工作流是包含非确定性组件的复杂多步骤流程。在此场景下，可观测性不再是"锦上添花"，而是理解系统行为、预防故障并持续提升准确性的关键要素。

在现代应用中，可观测性应成为技术栈的核心。它能帮助理解系统行为，预防或减少崩溃造成的损害，并通过识别用户流程中的主要痛点，助力开发者提升用户体验。

## 使用 LlamaIndex 构建可观测文档工作流

我们通过 LlamaIndex 智能体工作流为文档流程注入动力，这是一款基于代码的工具，完美契合可观测性管道的集成需求。与依赖繁重日志记录、调试语句淹没于数百行代码的传统方式不同，智能体工作流凭借其源自步进式事件驱动架构的内置可观测性特性（每个步骤都会发射和接收事件），提供了更清晰、更易维护的流程追踪方案。这种结构天然映射到 OpenTelemetry 的跨度与追踪模型，使得文档处理管道的埋点监控变得直观高效。

在本博客中，我们将逐步构建一个金融文档分类与提取工作流，展示如何从零开始搭建完整的可观测性体系。我们将仅使用开源技术：智能体工作流框架、 [OpenTelemetry](https://opentelemetry.io/docs/languages/python/) 和 [Jaeger](https://www.jaegertracing.io/) 。最终您将能追踪文档工作流的每个步骤，甚至通过派发自定义事件实现监控的精细化控制。

### 1\. Setup

在本示例中，我们将使用 uv 和 Docker：请确保已安装这两者以便跟随操作！

首先，让我们通过初始化环境并安装必要的依赖来搭建开发环境：

```html
uv init .

uv add llama-index-workflows \

 llama-cloud-services \

 llama-index-observability-otel \

 opentelemetry-exporter-otlp-proto-http

uv tool install llamactl # this will be helpful later!

source .venv/bin/activate # or .venv\Scripts\activate if you are on Windows
```

现在，让我们在 `compose.yaml` 文件中配置 Jaeger 以实现追踪功能…

```yaml
# compose.yaml

name: jaeger-tracing

services:

  jaeger:

 image: jaegertracing/all-in-one:latest

 ports:

 - 16686:16686

 - 4317:4317

 - 4318:4318

 - 9411:9411

 environment:

 - COLLECTOR_ZIPKIN_HOST_PORT=:9411
```

…并通过 Docker Compose 在本地部署它：

```html
docker compose up -d # the service is now running in the background
```

最后，我们来创建用于开发和运行工作流的目录结构：

```html
mkdir -p src/financial_classifier/

touch src/financial_classifier/__init__.py
```

既然一切准备就绪，我们现在可以着手定义工作流程了。

### 2\. The workflow

针对我们的金融文档处理用例，我们将构建一个利用两款 [LlamaCloud](https://cloud.llamaindex.ai/?utm_source=blog&utm_medium=li_social) 产品的工作流： [LlamaExtract](https://developers.llamaindex.ai/python/cloud/llamaextract/getting_started/?utm_source=blog&utm_medium=li_social) 与 [LlamaClassify](https://developers.llamaindex.ai/python/cloud/llamaclassify/getting_started/?utm_source=blog&utm_medium=li_social) 。该工作流将根据文档类型自动分类金融文档并提取结构化数据——这正是需要全面可观测性的多步骤流水线的典型场景。

让我们将 LlamaCloud 服务设置为工作流的 [资源](https://developers.llamaindex.ai/python/llamaagents/workflows/resources/?utm_source=blog&utm_medium=li_social) ，并将此文件保存至 `src/financial_classifier/resources.py` 中

```python
import os

from pydantic import BaseModel, Field

from llama_cloud_services import LlamaExtract

from llama_cloud_services.beta.classifier import ClassifyClient

class IncomeStatement(BaseModel):

 """Financial performance over a period"""

 period_end: str = Field(description="End date of reporting period")

 revenue: float = Field(description="Total income from sales/services")

 expenses: float = Field(description="Total costs incurred")

 net_income: float = Field(description="Profit or loss (revenue - expenses)")

 currency: str | None = Field(default=None, description="Currency code")

class CashflowStatement(BaseModel):

 """Cash movement over a period"""

 period_end: str = Field(description="End date of reporting period")

 operating_cashflow: float = Field(description="Cash from core business operations")

 investing_cashflow: float = Field(description="Cash from investments/asset purchases")

 financing_cashflow: float = Field(description="Cash from debt/equity activities")

 net_change: float = Field(description="Total change in cash position")

class BalanceSheet(BaseModel):

 """Financial position at a point in time"""

 report_date: str = Field(description="Snapshot date")

 total_assets: float = Field(description="Everything the company owns")

 total_liabilities: float = Field(description="Everything the company owes")

 equity: float = Field(description="Owner's stake (assets - liabilities)")

 currency: str | None = Field(default=None, description="Currency code")

async def get_llama_extract(*args, **kwargs) -> LlamaExtract:

 return LlamaExtract(api_key=os.getenv("LLAMA_CLOUD_API_KEY"))

async def get_llama_classify(*args, **kwargs) -> ClassifyClient:

 return ClassifyClient.from_api_key(api_key=os.getenv("LLAMA_CLOUD_API_KEY", ""))
```

我们现在可以为工作流定义事件，并将其保存在 `src/financial_classifier/events.py` 下：

```python
from workflows.events import StartEvent, StopEvent, Event

from typing import Literal

from pydantic import ConfigDict

from .resources import CashflowStatement, IncomeStatement, BalanceSheet

class InputDocumentEvent(StartEvent):

 path: str

 

class ProgressEvent(Event): # used to monitor progress

 message: str

class ClassificationEvent(Event):

 classification: Literal["income_statement", "cashflow_statement", "balance_sheet"]

 reasons: str

class ExtractedDataEvent(StopEvent):

 extracted_data: CashflowStatement | IncomeStatement | BalanceSheet | None

 error: str | None = None

 model_config = ConfigDict(arbitrary_types_allowed=True)
```

有了资源和事件后，我们就能构建财务分类工作流，并将其保存为 `src/financial_classifier/workflow.py`

```python
from workflows import Workflow, step, Context

from workflows.resource import Resource

from typing import Annotated

from llama_cloud_services.beta.classifier import ClassifyClient

from llama_cloud_services.extract import LlamaExtract, ExtractConfig

from llama_cloud.types.classifier_rule import ClassifierRule

from .events import InputDocumentEvent, ClassificationEvent, ExtractedDataEvent, ProgressEvent

from .resources import get_llama_classify, get_llama_extract, BalanceSheet, IncomeStatement, CashflowStatement

class FinancialClassifierWorkflow(Workflow):

 @step

 async def classify_input_file(self, ev: InputDocumentEvent, classifier: Annotated[ClassifyClient, Resource(get_llama_classify)], ctx: Context) -> ClassificationEvent | ExtractedDataEvent:

 ctx.write_event_to_stream(ProgressEvent(message=f"Classifying {ev.path}..."))

 async with ctx.store.edit_state() as state:

 state.input_file_path = ev.path

 rules = [ClassifierRule(type="income_statement", description="Shows revenue, expenses, and profit/loss over a period"), ClassifierRule(type="cashflow_statement", description="Tracks cash movements across operating, investing, and financing activities"), ClassifierRule(type="balance_sheet", description="Lists assets, liabilities, and equity at a specific date")]

 result = await classifier.aclassify(rules=rules, files=ev.path)

 classification_result = result.items[0].result

 if classification_result is not None and classification_result.type is not None:

 return ClassificationEvent(

 classification=classification_result.type, # type: ignore

 reasons=classification_result.reasoning,

 )

 else:

 return ExtractedDataEvent(extracted_data=None, error="Failed to produce a classification for the input file")

 @step

 async def extract_details_from_file(self, ev: ClassificationEvent, extractor: Annotated[LlamaExtract, Resource(get_llama_extract)], , ctx: Context) -> ExtractedDataEvent:

 ctx.write_event_to_stream(ProgressEvent(message=f"File classified as {ev.classification} because of the following reasons: {ev.reasons}"))

 ctx.write_event_to_stream(ProgressEvent(message="Extracting details..."))

 if ev.classification == "balance_sheet":

 data_model = BalanceSheet

 elif ev.classification == "cashflow_statement":

 data_model = CashflowStatement

 else:

 data_model = IncomeStatement

 state = await ctx.store.get_state()

 result = await extractor.aextract(data_schema=data_model, config=ExtractConfig(), files=state.input_file_path)

 if result.data is not None:

 data = data_model.model_validate(result.data)

 ctx.write_event_to_stream(ProgressEvent(message=f"Extracted the following data:\n{data.model_dump_json(indent=4)}"))

 return ExtractedDataEvent(extracted_data=data)

 else:

 return ExtractedDataEvent(

 extracted_data=None,

 error="It was not possible to extract the data from the provided input file"

 )

workflow = FinancialClassifierWorkflow(timeout=600)
```

为了在本地运行我们的工作流，我们可以使用 `llamactl` （已在安装过程中配置），需要将 `pyproject.toml` 调整为以下结构：

```html
[build-system]

requires = ["hatchling"]

build-backend = "hatchling.build"

[project]

name = "financial-classifier"

version = "0.1.0"

description = "Add your description here"

readme = "README.md"

requires-python = ">=3.13"

dependencies = [

 "llama-cloud-services>=0.6.79",

 "llama-index-observability-otel>=0.2.1",

 "llama-index-workflows>=2.11.1",

 "opentelemetry-exporter-otlp-proto-http>=1.38.0",

]

[tool.hatch.build.targets.wheel]

only-include = ["src/financial_classifier"]

[tool.hatch.build.targets.wheel.sources]

"src" = ""

[tool.llamadeploy.workflows]

classify-and-extract = "financial_classifier.workflow:workflow"

[tool.llamadeploy]

name = "financial-classifier"

env_files = [".env"]

llama_cloud = true
```

现在我们将拥有一个 `financial-classifier` 服务，可以通过 `llamactl serve` 在本地部署，该服务包含位于 `classify-and-extract` 命名空间下的财务分类工作流。

### 3\. Observability

既然我们的文档工作流已经搭建完成，现在可以接入可观测性层来追踪非结构化 PDF 如何转化为结构化财务数据。通过集成 OpenTelemetry，我们将能清晰掌握分类操作的发生节点、提取过程的耗时情况，以及流水线中可能出现的故障点。

为实现此功能，我们需要在 `src/financial_classifier/instrumentation.py` 中添加以下代码：

```python
from llama_index.observability.otel import LlamaIndexOpenTelemetry

from opentelemetry.exporter.otlp.proto.http.trace_exporter import (

 OTLPSpanExporter,

)

span_exporter = OTLPSpanExporter("http://0.0.0.0:4318/v1/traces")

instrumentor = LlamaIndexOpenTelemetry(

 service_name_or_resource="financial_classifier.traces",

 span_exporter=span_exporter,

)
```

然后你应该把这个添加到你的 `workflow.py` 脚本中：

如你所见，仅用六行代码我们就搭建起了完整的可观测性引擎！

### 4\. 运行与检查追踪

既然一切准备就绪，现在就用 `llamactl` 在本地启动工作流吧：

```html
llamactl serve --port 8000
```

随后，我们可以下载一份示例利润表来运行该工作流程：

```html
curl -L https://www.republicguyana.com/pdfs/commercial-account/SAMPLE-INCOME-STATEMENT.pdf -o financial_document.pdf
```

现在我们可以通过以下代码（保存在 `scripts/run_workflow.py` 中）从我们创建的服务器运行工作流：

```python
import asyncio

import httpx

from financial_classifier.events import InputDocumentEvent, ProgressEvent

from workflows.client import WorkflowClient

async def run_workflow():

 httpx_client = httpx.AsyncClient(base_url="http://127.0.0.1:8000/deployments/financial-classifier")

 wf_client = WorkflowClient(httpx_client=httpx_client)

 data = await wf_client.run_workflow_nowait(workflow_name="classify-and-extract", start_event=InputDocumentEvent(path="financial_document.pdf"))

 async for event in wf_client.get_workflow_events(data.handler_id):

 ev = event.load_event()

 if isinstance(ev, ProgressEvent):

 print(ev.message)

 result = None

 while result is None:

 handler_data = await wf_client.get_result(data.handler_id)

 result = handler_data.result

 await asyncio.sleep(0.1)

 print(f"Final result:\n{result}")

if __name__ == "__main__":

 asyncio.run(run_workflow())
```

使用 \`uv run scripts/run\_workflow.py\` 运行此脚本后，您可以前往 Jeager UI（\`http://localhost:16686\`）并选择 \`financial\_classifier.traces\` 服务。您将看到包含五个收集跨度的追踪记录，如果打开它，您会看到类似下图的界面：

![](https://cdn.sanity.io/images/7m9jw85w/production/a380bf27e7653235e26c1ec348942a4a41134a5f-3454x1786.png)

恭喜：您已成功完成首个文档工作流的埋点与追踪！现在您可以完整查看财务文档在分类与提取过程中的流转路径，每一步的时间信息都清晰可见。

### 5\. 创建自定义事件追踪

除了内置的可观测性功能，您还可以对文档工作流中的监控内容进行更精细的控制。例如，您可以追踪分类置信度得分、提取元数据或验证结果（这些特定指标对您的文档处理场景至关重要）。

要创建自定义事件，我们需要从 `llama-index-instrumentation` 包中继承 `BaseEvent` 类，只需将以下代码添加到 `instrumentation.py` 脚本即可实现：

```python
# rest of the code

from llama_index_instrumentation import get_dispatcher

from llama_index_instrumentation.base.event import BaseEvent

dispatcher = get_dispatcher()

class ClassificationMetadata(BaseEvent):

 duration: float

 metadata: dict[str, Any]

 @classmethod

 def class_name(cls) -> str:

 return "ClassificationMetadata"

class ExtractionMetadata(BaseEvent):

 duration: float

 metadata: dict[str, Any]

 @classmethod

 def class_name(cls) -> str:

 return "ExtractionMetadata"

 # rest of the code

 instrumentor = LlamaIndexOpenTelemetry(

 service_name_or_resource="financial_classifier.custom_traces", # modify the service name here to make it easier to distinguish from the previous run

 span_exporter=span_exporter,

)
```

现在，在我们的工作流中，我们可以使用 `dispatcher.event()` 方法来收集一个带有 OpenTelemetry 的事件，并将其导出到 Jaeger。我们可以通过修改工作流的两个步骤来实现这一点。

```python
# rest of the code

from .instrumentation import instrumentor, ExtractionMetadata, ClassificationMetadata, dispatcher

class FinancialClassifierWorkflow(Workflow):

 @step

 async def classify_input_file(self, ev: InputDocumentEvent, classifier: Annotated[ClassifyClient, Resource(get_llama_classify)], ctx: Context) -> ClassificationEvent | ExtractedDataEvent:

 # ...

 start = time.time()

 result = await classifier.aclassify(rules=rules, files=ev.path)

 classification_result = result.items[0].result

 if classification_result is not None and classification_result.type is not None:

 dispatcher.event(event=ClassificationMetadata(duration=time.time()-start, metadata={"confidence": classification_result.confidence})) # add this line to send the custom event

 # ...

 @step

 async def extract_details_from_file(self, ev: ClassificationEvent, extractor: Annotated[LlamaExtract, Resource(get_llama_extract)], ctx: Context) -> ExtractedDataEvent:

 # ...

 state = await ctx.store.get_state()

 start = time.time()

 result = await extractor.aextract(data_schema=data_model, config=ExtractConfig(), files=state.input_file_path)

 if result.data is not None:

 dispatcher.event(event=ExtractionMetadata(duration=time.time()-start, metadata=result.extraction_metadata or {})) # add this line to send the custom event

 # ...

instrumentor.start_registering()

workflow = FinancialClassifierWorkflow(timeout=600)
```

现在让我们重新运行工作流（使用相同的 `run_workflow.py` 脚本），再次查看追踪记录：

![](https://cdn.sanity.io/images/7m9jw85w/production/7dac5f860223434b59f6e79911b2a5f6d7c9a413-3454x1786.png)

从 Jaeger 界面可见，我们自定义的事件已成功发射、注册并导出！这种精细度对于理解文档工作流的运行状态至关重要——不仅能确认流程是否执行，更能精准评估其性能表现。

## Wrapping Up

总而言之，在这篇博文中我们：

- 从现实世界中的多步骤文档工作流程挑战入手，例如财务数据提取和发票处理
- 阐述了可观测性对于理解非结构化文档如何转化为结构化、可操作数据的关键作用
- 利用 LlamaIndex 智能体工作流构建了完整的金融文档分类与提取流程
- 通过 LlamaIndex 与 OpenTelemetry 的原生集成配置了全面可观测性
- 使用 `llamactl` 在本地运行工作流，并通过 Jaeger 收集详细追踪数据
- 添加了自定义事件，用于追踪文档特定指标，如分类置信度和提取元数据

您可以在 [GitHub 上的这个代码仓库](https://github.com/run-llama/observability-blog-code) 中找到本文的所有代码，并可通过 [专题文档](https://developers.llamaindex.ai/python/framework/module_guides/observability/?utm_source=blog&utm_medium=li_social) 深入了解可观测性相关知识。