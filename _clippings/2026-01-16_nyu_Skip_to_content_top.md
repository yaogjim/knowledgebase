---
title: "2026-01-16_developers_llamaindex_ai_Skip_to_content_top"
source: "https://developers.llamaindex.ai/python/cloud/llamaextract/examples/split_and_extract_resume_book/?utm_source=socials&utm_medium=tc_social#step-3-initialize-llamaextract"
author:
  - "[[@nyu]]"
published: 2026-01-16
created: 2026-01-16
description:
tags:
  - "#_top"
  - "developers"
  - "@nyu"
  - "field"
---

当你需要从数百份简历中提取结构化信息时，处理简历集可能会很耗时。本笔记本展示了如何使用 LlamaAgent Workflows、LlamaSplit 和 LlamaExtract 构建一个能够自动处理简历集的智能代理。该代理：

1.  将 PDF 文档上传到 LlamaCloud
2.  将文档拆分为逻辑分段（简历与课程大纲/索引）
3.  从每份简历中提取结构化数据
4.  使用 LlamaIndex 工作流统筹整个流程

在这个示例中，我们将使用纽约大学数学金融全职简历集。你可以从以下位置下载：

**📥 下载简历书**

请先将文件保存到本地（例如，命名为 `resume_book.pdf` ），再继续操作。

该工作流使用了两个关键的 LlamaCloud 服务：

- LlamaSplit：将文档页面分类为不同类型（如简历、课程页、封面页等）
- LlamaExtract：利用 AI 从文档中提取结构化数据

让我们先安装所需的依赖项。

```python
pip install llama-cloud requests llama-cloud-services llama-index-workflows
```

```python
import os
from getpass import getpass

if "OPENAI_API_KEY" not in os.environ:
 os.environ["OPENAI_API_KEY"] = getpass("OPENAI_API_KEY")
if "LLAMA_CLOUD_API_KEY" not in os.environ:
 os.environ["LLAMA_CLOUD_API_KEY"] = getpass("LLAMA_CLOUD_API_KEY")
```

在处理文档之前，我们需要先将其上传到 LlamaCloud。这为我们提供了一个 `file_id` ，可用于其他 LlamaCloud API。

The `LlamaCloud` 客户端提供了一个方便的 `upload_file()` 方法，用于处理上传并返回包含文件 ID 的元数据。

```python
from llama_cloud.client import LlamaCloud

client = LlamaCloud(token=os.getenv("LLAMA_CLOUD_API_KEY"))

# Update this path to where you saved the resume book
pdf_path = "resume_book.pdf"  # or "/content/resume_book.pdf" in Colab

with open(pdf_path, "rb") as f:
 uploaded_file = client.files.upload_file(upload_file=f)

file_id = uploaded_file.id
print(f"✅ File uploaded: {uploaded_file.name}")
```

现在我们将使用 LlamaCloud 的 Split API 自动分类文档中的页面。当文档包含多种类型的内容时，这种方法会很有用。

我们定义类别：

- `resume`: 候选人的个人简历页面
- " `curriculum`: 完整的学生课程页面，展示课程大纲"
- 封面或标题页（可选，视文档结构而定）

Split API 使用人工智能分析每一页，并将其分配到相应的类别。这会生成一个异步执行的任务，因此我们需要轮询结果。

```python
import requests

 "Authorization": f"Bearer {os.getenv("LLAMA_CLOUD_API_KEY")}",
 "Content-Type": "application/json",
}

split_request = {
 "document_input": {
 "type": "file_id",
 "value": file_id,
 },
 "categories": [
 {
 "name": "resume",
 "description": "A resume page from an individual candidate containing their professional information, education, and experience",
 },
 {
 "name": "curriculum",
 "description": "The overall student curriculum page listing the program curriculum",
 },
 {
 "name": "cover_page",
 "description": "Cover page, title page, or introductory page of the resume book",
 },
 ],
}

response = requests.post(
 f"https://api.cloud.llamaindex.ai/api/v1/beta/split/jobs",
 headers=headers,
 json=split_request,
)
response.raise_for_status()

split_job = response.json()
job_id = split_job["id"]

print(f"✅ Split job created: {job_id}")
print(f" Status: {split_job['status']}")
```

```plaintext
✅ Split job created: spl-x1b55wotk30g8x3rraz0734rabld
 Status: pending
```

```python
import time

def poll_split_job(job_id: str, max_wait_seconds: int = 180, poll_interval: int = 5):
 start_time = time.time()

 while (time.time() - start_time) < max_wait_seconds:
 response = requests.get(
 f"https://api.cloud.llamaindex.ai/api/v1/beta/split/jobs/{job_id}",
 headers=headers,
 )
 response.raise_for_status()
 job = response.json()

 status = job["status"]
 elapsed = int(time.time() - start_time)
 print(f" Status: {status} (elapsed: {elapsed}s)")

 if status in ["completed", "failed"]:
 return job

 time.sleep(poll_interval)

 raise TimeoutError(f"Job did not complete within {max_wait_seconds} seconds")

completed_job = poll_split_job(job_id)

segments = completed_job.get("result", {}).get("segments", [])

print(f"📊 Total segments found: {len(segments)}")

for i, segment in enumerate(segments, 1):
 category = segment["category"]
 pages = segment["pages"]
 confidence = segment["confidence_category"]

 if len(pages) == 1:
 page_range = f"Page {pages[0]}"
 else:
 page_range = f"Pages {min(pages)}-{max(pages)}"

 print(f"\nSegment {i}:")
 print(f" Category: {category}")
 print(f" Pages: {pages}")
 print(f" Confidence: {confidence}")
```

LlamaExtract 是一个能够从文档中提取结构化数据的服务。我们将用它从每位候选人的简历中提取简历信息。

提取器将使用 Pydantic 模式来定义我们要提取的数据的结构。

```python
from llama_cloud_services import LlamaExtract

extractor = LlamaExtract()
```

我们定义一个 Pydantic 模式（ `ResumeSchema` ），用于描述我们要从每份简历中提取的数据结构：

- Candidate name
- 联系信息（邮箱、电话）
- 教育（学位、机构、日期）
- 工作经历（公司、职位、日期、描述）
- 技能（包括技术技能、编程语言等）
- 补充信息（证书、语言等）

The `ExtractConfig` specifies:

- 为了最高质量的提取， `extraction_mode`: `PREMIUM`
- " `page_range`: 从特定页面提取（例如，“5”代表第 5 页的简历）"
- 在结果中包含置信度分数

然后我们调用 `aextract()` 来提取指定页码范围内的数据

```python
from llama_cloud import ExtractConfig, ExtractMode
from pydantic import BaseModel, Field
from typing import Optional, List

class Education(BaseModel):
 degree: str = Field(description="Degree type (e.g., B.S., M.S., Ph.D.)")
 institution: str = Field(description="Name of the educational institution")
 field_of_study: Optional[str] = Field(None, description="Field of study or major")
 graduation_date: Optional[str] = Field(None, description="Graduation date or year")
 gpa: Optional[str] = Field(None, description="GPA if mentioned")

class WorkExperience(BaseModel):
 company: str = Field(description="Company or organization name")
 position: str = Field(description="Job title or position")
 start_date: Optional[str] = Field(None, description="Start date")
 end_date: Optional[str] = Field(None, description="End date (or 'Present' if current)")
 description: Optional[str] = Field(None, description="Job description or key responsibilities")

class ResumeSchema(BaseModel):
 name: str = Field(description="Full name of the candidate")
 email: Optional[str] = Field(None, description="Email address")
 phone: Optional[str] = Field(None, description="Phone number")
 location: Optional[str] = Field(None, description="Location or address")
 education: List[Education] = Field(description="List of educational qualifications")
 work_experience: List[WorkExperience] = Field(description="List of work experiences")
 skills: List[str] = Field(description="List of skills, programming languages, or technical competencies")
 certifications: Optional[List[str]] = Field(None, description="Certifications or licenses")
 languages: Optional[List[str]] = Field(None, description="Languages spoken")
 summary: Optional[str] = Field(None, description="Professional summary or objective")

EXTRACT_CONFIG = ExtractConfig(
 extraction_mode=ExtractMode.PREMIUM,
 system_prompt=None,
 use_reasoning=False,
 cite_sources=False,
 confidence_scores=True,
 page_range='5'
)

extracted_result = await extractor.aextract(
 data_schema=ResumeSchema, files="resume_book.pdf", config=EXTRACT_CONFIG
)
```

让我们看看从文档中提取了什么数据。结果是一个与我们的 `ResumeSchema` 匹配的字典。

```python
extracted_result.data
```

```plaintext
{'name': 'Quanquan (Lydia) Chen',
 'email': 'q.chen@nyu.edu',
 'phone': '(201) 626-0959',
 'location': 'New York, NY',
 'education': [{'degree': 'M.S.',
 'institution': 'New York University',
 'field_of_study': 'Mathematics in Finance',
 'graduation_date': '12/24',
 'gpa': None},
  {'degree': 'B.S.',
 'institution': 'Zhejiang University',
 'field_of_study': 'Mathematics and Applied Mathematics',
 'graduation_date': '06/23',
 'gpa': None}],
 'work_experience': [{'company': 'Numerix',
 'position': 'Financial Engineering Intern',
 'start_date': '07/24',
 'end_date': 'Present',
 'description': 'Developed models (e.g., Black-Scholes, Heston, Bates), applied market data and wrote payoff scripts to price exotic instruments (e.g., barrier options, variance swaps, cliquets, corridors). Conducted calibrations for equity and FX models with pricing and Greeks, considered different cases (e.g., time-dependent yield, projection rate, day-count conventions) to ensure accuracy. Researched and applied pricing algorithms (e.g., backward Monte Carlo for American options) in literature review from academic papers on financial products pricing.'},
  {'company': 'Shenwan Hongyuan Securities Research Co., Ltd.',
 'position': 'Financial Engineering Intern',
 'start_date': '06/22',
 'end_date': '11/22',
 'description': 'Extracted fund data, manipulated and validated data through detecting outliers, dropping duplicates values, completed missing values with imputers, and reduce data dimensions. Applied PCA on portfolio, based on principal components and risk budgeting to build a new one, backtested it and obtained annualized return 7.16% and winning percentage nearly 85%. Anatomized low-cost fund data, summarized competitive advantages and background as well as business strategies of investment companies; researched other products, produced client reports.'}],
 'skills': ['Python (Pandas, Numpy, Scipy, Matplotlib, Sklearn)',
  'LaTeX',
  'Excel'],
 'certifications': None,
 'languages': ['English (fluent)', 'Mandarin (native)'],
 'summary': None}
```

现在我们将以 LlamaIndex 工作流的方式统筹整个流程

1.  **`split_document` step**:
 
 - Uploads the file
 - Creates a split job
 - 完成情况调查
 - 为每个片段发出一个 `ExtractResume` 事件
2.  **`extract_resume` step**:
 
 - 等待收集所有片段（扇入模式）
 - 从每个“简历”部分提取数据
 - 返回所有已提取的简历

- 事件：自定义事件类型（ `ExtractResume` ），用于在步骤之间传递数据
- 扇出/扇入： `split_document` 步骤会发出多个事件（每个段一个）， `extract_resume` 会收集所有事件后再继续
- 上下文存储：用于跟踪我们预期收集的片段数量
- 并行处理：多个提取事件可并发处理

```python
from workflows import Workflow, step, Context
from workflows.events import StartEvent, StopEvent, Event

class ExtractResume(Event):
 file_path: str
 category: str
 pages: list[int]

class ResumeBookAgent(Workflow):

 def __init__(self, *args, **kwargs):
 super().__init__(*args, **kwargs)
 self.extractor = LlamaExtract()

 class ResumeSchema(BaseModel):
 name: str = Field(description="Full name of the candidate")
 email: Optional[str] = Field(None, description="Email address")
 phone: Optional[str] = Field(None, description="Phone number")
 location: Optional[str] = Field(None, description="Location or address")
 education: List[Education] = Field(description="List of educational qualifications")
 work_experience: List[WorkExperience] = Field(description="List of work experiences")
 skills: List[str] = Field(description="List of skills, programming languages, or technical competencies")
 certifications: Optional[List[str]] = Field(None, description="Certifications or licenses")
 languages: Optional[List[str]] = Field(None, description="Languages spoken")
 summary: Optional[str] = Field(None, description="Professional summary or objective")

 self.extract_schema = ResumeSchema
 self.categories = [
 {
 "name": "resume",
 "description": "A resume page from an individual candidate containing their professional information, education, and experience",
 },
 {
 "name": "curriculum",
 "description": "The overall student curriculum page listing the program curriculum",
 },
 {
 "name": "cover_page",
 "description": "Cover page, title page, or introductory page of the resume book",
 },
 ]

 self.client = LlamaCloud(token=os.getenv("LLAMA_CLOUD_API_KEY"))

 @step
 async def split_document(self, ev: StartEvent, ctx: Context) -> ExtractResume:
 with open(ev.file_path, "rb") as f:
 uploaded_file = self.client.files.upload_file(upload_file=f)

 file_id = uploaded_file.id
 print(f"✅ File uploaded: {uploaded_file.name}", flush=True)
 "Authorization": f"Bearer {os.getenv("LLAMA_CLOUD_API_KEY")}",
 "Content-Type": "application/json",
 }
 split_request = {
 "document_input": {
 "type": "file_id",
 "value": file_id,
 },
 "categories": self.categories
 }
 response = requests.post(
 f"https://api.cloud.llamaindex.ai/api/v1/beta/split/jobs",
 headers=headers,
 json=split_request,
 )
 response.raise_for_status()
 split_job = response.json()
 job_id = split_job["id"]
 completed_job = poll_split_job(job_id)
 segments = completed_job.get("result", {}).get("segments", [])
 await ctx.store.set("segments_count", len(segments))
 for segment in segments:
 ctx.send_event(ExtractResume(file_path=ev.file_path, category=segment["category"], pages=segment["pages"]))

 @step
 async def extract_resume(self, ev: ExtractResume, ctx: Context) -> StopEvent:
 ready = ctx.collect_events(
 ev, [ExtractResume] * await ctx.store.get("segments_count")
 )
 if ready is None:
 return None
 extraction_result = []
 for event in ready:
 if event.category == "resume":
 config = ExtractConfig(page_range=f"{min(event.pages)}-{max(event.pages)}")
 extracted_result = await self.extractor.aextract(
 data_schema=self.extract_schema, files=event.file_path, config=config)
 extraction_result.append(extracted_result.data)
 return StopEvent(result=extraction_result)
```

```python
agent = ResumeBookAgent(timeout=1000)

resp = await agent.run(start_event=StartEvent(file_path="resume_book.pdf"))
```

```plaintext
✅ File uploaded: resume_book.pdf
 Status: pending (elapsed: 0s)
 Status: processing (elapsed: 5s)
 Status: processing (elapsed: 10s)
 Status: completed (elapsed: 15s)
```

```python
for resume in resp[1:3]:
 print(f"\n{'='*60}")
 print(f"Name: {resume.get('name', 'N/A')}")
 print(f"Education: {resume.get('education', 'N/A')}")
 print(f"Skills: {', '.join(resume.get('skills', []))}")
 print(f"{'='*60}")
```

```plaintext
============================================================
Name: Shengjun (James) Guan
Education: [{'degree': 'M.S.', 'institution': 'New York University', 'field_of_study': 'Mathematics in Finance', 'graduation_date': '12/24', 'gpa': None}, {'degree': 'B.S.', 'institution': 'Rose-Hulman Institute of Technology', 'field_of_study': 'Mathematics and Data Science', 'graduation_date': '05/23', 'gpa': None}]
Skills: Python, Java, R, MongoDB, NoSQL, MATLAB, Maple
============================================================

============================================================
Name: Shupeng (Wayne) Guan
Education: [{'degree': 'M.S.', 'institution': 'New York University', 'field_of_study': 'Mathematics in Finance', 'graduation_date': '01/25', 'gpa': None}, {'degree': 'B.S.', 'institution': 'University of Birmingham', 'field_of_study': 'Mathematics With Honours (First Class)', 'graduation_date': '07/23', 'gpa': None}, {'degree': 'B.S.', 'institution': 'Huazhong University of Science and Technology', 'field_of_study': 'Finance', 'graduation_date': '06/21', 'gpa': '3.8/4'}]
Skills: Python, R, MATLAB, SQL, LaTex
```

既然你已经拥有了结构化的简历数据，你就可以：

- 按技能、教育背景或工作经验筛选候选人
- 查找特定的资格要求
- 构建一个基于职位要求的候选人匹配系统
- 生成候选人的人口统计信息和资格报告