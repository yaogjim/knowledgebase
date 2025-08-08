---
title: "Real Estate Agent with LangGraph (using CLI)"
source: "https://docs.tensorlake.ai/examples/tutorials/real-estate-agent-with-langgraph-cli"
author:
  - "[[Tensorlake]]"
published:
created: 2025-07-01
description: "Build a real estate agent using LangGraph to interact with purchase agreements and answer agent queries."
tags:
  - "clippings"
---
在本教程中，你将使用 Tensorlake、LangChain 和 OpenAI 从包含签名的文档中提取上下文信息。

使用此 [Colab 笔记本](https://tlake.link/langchain-tool-docs) 试用此示例

在 [张量湖 GitHub 仓库](https://github.com/tensorlakeai/tensorlake/tree/main/examples/signature-detection/) 中提供了一个完整的、可运行的示例，展示了一个已构建的同时使用 CLI 和 Streamlit 应用程序的智能体。

## 借助签名检测和 LangGraph 更快完成交易

让我们为这个示例设定一下背景，你将为一家房地产公司构建一个 LangGraph 智能体，以帮助跟踪谁签署了房产文件、他们何时签署的，以及谁仍需签署。

你将学习如何：

- 使用 Tensorlake 的 [签名检测软件开发工具包](https://docs.tensorlake.ai/document-ingestion/parsing#signature-detection)
- 提取并汇总每个房产的签名状态
- 创建一个使用结构化数据来回答诸如以下问题的 [LangGraph 智能体](https://langchain-ai.github.io/langgraph/concepts/why-langgraph/) ：
	- 这份文件中检测到了多少个签名，涉及哪些当事人？
	- 关于任何签名，你能提取哪些上下文信息？
	- 是否有任何页面上的签名缺失？

这对于跨大量带有大量签名的文档自动执行尽职调查和合规跟踪而言非常理想。

## 前提条件

- Python 3.10 及以上版本
- 一个 [OpenAI API 密钥](https://platform.openai.com/api-keys)
- 一个 [张量湖 API 密钥](https://docs.tensorlake.ai/accounts-and-access/api-keys)
- 一些 [房地产文件样本](https://drive.google.com/drive/folders/1lYTE8HIwvVNOZ6TNJDo-SLS0F12dybej?usp=sharing)
- \[可选\] 用于隔离依赖项的 [虚拟 Python 环境](https://docs.python.org/3/library/venv.html)

## 步骤0：设置你的环境

```
pip install openai tensorlake langchain langgraph langchain-community python-dotenv
```

在 `.env` 中设置您的 API 密钥：

```
OPENAI_API_KEY=your_openai_api_key

TENSORLAKE_API_KEY=your_tensorlake_api_key
```

## 步骤 1：使用 Tensorlake 上传并解析文档

对于本教程，你需要创建一个名为 `signature_detection_langgraph_agent.py` 的文件，在该文件中你将使用 Tensorlake 从文档中提取数据并定义我们的 LangGraph 代理。

### 1.1. 准备你的导入语句

在顶部，确保你已导入所有必要的 Tensorlake、LangGraph、LangChain 和辅助包。然后，从 `.env` 加载你的环境变量：

```
# helper packages

import os

import time

import json

import logging

from typing import Optional, Type, Annotated, TypedDict, Union, List

from pydantic import Field, BaseModel, Json

import asyncio

from pathlib import Path

from dotenv import load_dotenv

# LangGraph and LangChain imports

from langgraph.graph import StateGraph, END

from langgraph.graph.message import add_messages

from langgraph.prebuilt import ToolNode

from langchain_openai import ChatOpenAI

from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

from langchain_core.tools import StructuredTool

# TensorLake imports

from tensorlake.documentai import DocumentAI, ParsingOptions

from tensorlake.documentai.parse import (ExtractionOptions)

load_dotenv()

# Load environment variables

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

TENSORLAKE_API_KEY = os.getenv("TENSORLAKE_API_KEY")
```

### 1.2. 使用 Tensorlake 提取签名

创建一个名为 `detect_signatures_in_document` 的 Langchain 工具，该工具将文档的文件路径作为字符串传入，用于解析文档。它将处理与数据提取相关的所有事情，包括：

- 将文档上传到 Tensorlake
- 指定解析选项，以便我们提取所需的特定信息
- 使用 Tensorlake 启动解析任务
- 查询任务直到完成；如果成功，将返回结果

```
def detect_signatures_in_document(path: str) -> str:

    """

    Uploads a document to TensorLake, triggers parsing, including signature detection, and returns the parsed result.

    """

    if not Path(path).exists():

        return f"File not found: {path}"

    if not TENSORLAKE_API_KEY:

        return "Error: TENSORLAKE_API_KEY environment variable is not set"

    # Initialize DocumentAI client

    doc_ai = DocumentAI(api_key=TENSORLAKE_API_KEY)

    

    # Upload document to TensorLake

    file_id = doc_ai.upload(path=path)

    parsing_options = ParsingOptions(

        detect_signature=True,  # this needs to be True

        extraction_options=ExtractionOptions(skip_ocr=True),

    )

    # Start parsing job

    job_id = doc_ai.parse(file_id, options=parsing_options)

    # Poll for completion with configurable timeout

    start_time = time.time()

    max_wait_time = 300  # or set as a constant or parameter (here, we will wait for 5 min max)

    while time.time() - start_time < max_wait_time:

        # Signature detection result after parsing the document

        result = doc_ai.get_job(job_id)  # this may take 2-3 minutes

        if result.status in ["pending", "processing"]:

            time.sleep(5)  # Wait 5 seconds before checking again

        elif result.status == "successful":

            # Optional: save the parsed result in a file for referring to it later

            with open(f"parsed_result_{file_id}.json", "w") as f:

                json.dump(result.model_dump(), f, indent=2)

            # Return parsed result

            return str(result)

        else:

            return f"Document parsing failed with status: {result.status}"

    # Timeout reached

    return f"Document processing timeout after {max_wait_time} seconds. Job ID: {job_id}"
```

这个同步函数将使用 Tensorlake 运行签名检测的核心逻辑。为了使其异步运行，以便能够与像 LangGraph 这样的异步兼容代理框架集成，我们使用 `asyncio.to_thread()` 将其包装在一个异步兼容函数中。

```
async def detect_signatures_in_document_async(path: str) -> str:

    """Asynchronous version of detecting signatures from document."""

    return await asyncio.to_thread(detect_signatures_in_document, path)
```

定义了签名检测函数后，我们使用 \`StructuredTool\` 将其包装为一个 LangChain 工具，这样代理就可以调用它。

```
# Create the LangChain tool using StructuredTool

signature_detection_tool = StructuredTool.from_function(

    func=detect_signatures_in_document,

    coroutine=detect_signatures_in_document_async,

    name="SignatureDetectionTool",

    description="Detect signatures from any document (PDF, Markdown, Docx, etc.)",

    return_direct=False,

    handle_tool_error="Document parsing failed. Please verify the file path and your Tensorlake API key."

)
```

### 1.3. 理解解析结果

解析任务的结果将包含有关文档的结构化数据，包括页面、片段和检测到的签名。在这个要点中可以找到一个关于 [JSON 输出可能是什么样子的完整示例](https://gist.github.com/drguthals/93bdf4b8f07e83465e074113009f4fc0) 。

了解这些数据与签名相关的结构非常重要，这样我们才能为我们的代理提取相关信息。下面是在第一页上找到的单个页面片段的示例。结果将包含一个页面列表，每个页面都有自己的片段。每个片段都将有一个边界框、内容和一种类型，例如文本、键值对或签名。

文档的第1页在页面底部包含一个姓名首字母签名：

![Real Estate purchase with one initials signature at the bottom](https://mintlify.s3.us-west-1.amazonaws.com/tensorlake-35e9e726/images/tutorials/real-estate-agent-with-langgraph/real-estate-page-1-initials.png)

Real Estate purchase with one initials signature at the bottom

在这里你可以看到，在第一页的左下角发现了一个签名页片段。

```
{

    "pages": [

      {

        "dimensions": [

          1584,

          1224

        ],

        "layout": {},

        "page_fragments": [

          {

            "bbox": {

              "x1": 207,

              "x2": 250,

              "y1": 730,

              "y2": 756

            },

            "content": {

              "content": "Signature detected"

            },

            "fragment_type": "signature",

            "reading_order": null

          }

        ],

        "page_number": 1

      },

    ]

}
```

如果你要在 [张量湖游乐场](https://cloud.tensorlake.ai/) 上查看边界框，你会在页面的左下角看到突出显示的签名片段：

![Real Estate purchase with one initials signature at the bottom that is highlighted with a "signature" label. Other items on the page are also highlighted with bounding boxes.](https://mintlify.s3.us-west-1.amazonaws.com/tensorlake-35e9e726/images/tutorials/real-estate-agent-with-langgraph/real-estate-page-1-initials-bbox.png)

Real Estate purchase with one initials signature at the bottom that is highlighted with a "signature" label. Other items on the page are also highlighted with bounding boxes.

既然你已经了解了数据的结构以及结构化数据与文档的关系，那么你就可以仅提取该特定代理的相关数据。对于此示例，我们将使用完整的提取数据继续操作。

## 步骤 2：创建签名查询 LangGraph 代理

既然我们有了一个可以从文档中提取签名数据的工具，我们希望让用户能够就该文档提出自然语言问题。我们不会手动打开 JSON 文件，而是会使用 LangGraph 构建一个对话代理，LangGraph 是一个用于构建有状态、可使用工具的代理的框架，这些代理运行在语言模型之上。这个代理将：

- 使用 `signature_detection_tool` 通过 [张量湖的上下文签名检测](https://docs.tensorlake.ai/document-ingestion/parsing#signature-detection) 从文档中提取签名数据
- 解释用户问题（例如“哪些页面缺少签名？”）
- 返回结构化、准确的答案

### 2.1. 定义 LangGraph 代理提示和行为

首先，定义智能体应该如何思考。为此，构建一个动态系统提示，其中包括解析结果以及智能体应该回答的问题。此提示在运行时注入，并定义智能体的行为。

```
def build_document_analysis_prompt(parsed_result: str, questions: Union[str, List[str]]) -> str:

    # Normalize single question to list

    if isinstance(questions, str):

        questions = [questions]

    question_block = "\n".join(f"{i + 1}. {q}" for i, q in enumerate(questions))

    system_prompt = f"""You are a helpful assistant that answers questions about documents with signature detection data.

Your responsibilities:

1. Answer questions based on that loaded data

2. Help users understand the signature analysis results

You can answer questions like:

- How many signatures were found?

- Which pages contain signatures?

- Who signed the document?

- What does the content say around signatures?

- What type of document is this?

- Who are the parties involved?

- What is the date of the signature?

- Did each party sign the document?

- Are there any missing signatures on any pages?

- Which property is missing signatures?

- Who is the agent for the properties missing signatures?

I've processed a document and got this result:

{parsed_result}

Please analyze the above parsed output and answer the following:

{question_block}

"""

    return system_prompt
```

### 2.2. 定义 LangGraph 智能体工作流程

接下来，定义控制代理如何运行的 LangGraph 状态机。在这种设置中：

- 智能体总是从对用户输入进行推理开始。
- 如果模型选择调用工具（例如，加载保存的签名数据），则图会转换到工具节点。
- 工具执行完毕后，控制权将交还给代理以继续对话。

此循环会一直持续，直到不再进行进一步的工具调用，此时对话结束。LangGraph 使这种流程清晰、可预测且对生产安全。

```
# Define the agent state

class AgentState(TypedDict):

    messages: Annotated[list, add_messages]

# Agent node - decides whether to use tools

async def agent_node(state: AgentState):

    model = ChatOpenAI(

        model="gpt-4o",

        temperature=0.1

    ).bind_tools([signature_detection_tool])

    response = await model.ainvoke(state["messages"])

    return {"messages": [response]}

# Conditional Logic for Tool Use

def should_continue(state: AgentState):

    last_message = state["messages"][-1]

    if hasattr(last_message, 'tool_calls') and last_message.tool_calls:

        return "tools"

    return END

# LangGraph Workflow Setup

workflow = StateGraph(AgentState)

workflow.add_node("agent", agent_node)

workflow.add_node("tools", ToolNode([signature_detection_tool]))

workflow.set_entry_point("agent")

workflow.add_conditional_edges("agent", should_continue, {"tools": "tools", END: END})

workflow.add_edge("tools", "agent")

app = workflow.compile()
```

**状态图** 是 LangGraph 中的核心抽象概念。它定义了状态如何在节点之间流动（例如，智能体推理和工具执行）。在这种情况下，每个节点处理并更新状态，即对话历史记录，并且图会根据工具使用情况或结束条件来确定接下来运行哪个节点。你可以在 [LangGraph 公告博客文章](https://blog.langchain.dev/langgraph/) 上阅读更多相关内容。

```
# Document + Agent Pipeline

async def analyze_signatures_agents(

        path: str,

        questions: List[str]

) -> str:

    """Invoke the tool with parsing options, then use agent for analysis."""

    print("🔍 Processing document with signature detection...")

    # Pass parsing options and run the tool

    parsed_output = await signature_detection_tool.ainvoke({

        "path": path

    })

    # Build prompt

    prompt = build_document_analysis_prompt(parsed_output, questions)

    # Run agent on prompt

    final_state = await app.ainvoke({

        "messages": [HumanMessage(content=prompt)]

    })

    return final_state["messages"][-1].content
```

### 2.3. 运行 LangGraph 代理

构建完成后，使用以下代码运行代理：

```
async def example_signature_detection_real_estate():

    # change to your own file path

    path = "path/to/your/document.pdf"

    analysis_questions = [

        "How many signatures were detected in this document and who are the parties involved?",

        "What contextual information can you extract about any signatures?",

        "Are there any missing signatures on any pages?"

    ]

    result = await analyze_signatures_agents(

        path=path,

        questions=analysis_questions

    )

    print("Analysis Result:\n\n", result)

if __name__ == "__main__":

    # run the example

    asyncio.run(example_signature_detection_real_estate())
```

## 步骤 3：在命令行界面中测试由 Tensorlake 提供支持的 LangGraph 代理

最后，运行脚本以查看代理的实际运行情况。它将：

- 使用 Tensorlake 的签名检测来解析文档
- 根据解析后的数据构建动态提示
- 使用 LangGraph 代理回答有关签名的问题

```
(venv) % python3 signature_detection_langgraph_agent.py

🔍 Processing document with signature detection...

Analysis Result:

 Based on the parsed output from the document, here are the answers to your questions:

1. **How many signatures were detected in this document and who are the parties involved?**

   - A total of 20 signatures were detected in the document. 

   - The parties involved in the document are:

     - **Buyer:** Nova Ellison

     - **Seller:** Juno Vega

     - **Agent:** Aster Polaris from Polaris Group LLC

2. **What contextual information can you extract about any signatures?**

   - The document is a "Residential Real Estate Purchase Agreement" made on September 20, 2025.

   - The signatures are associated with the execution of the agreement, indicating acceptance of the terms by the Buyer, Seller, and Agent.

   - The document includes specific sections where signatures are required, such as the execution section on page 10, where the Buyer, Seller, and Agent have signed and dated the document on September 10, 2025.

   - The signatures are detected on each page, indicating that initials or signatures are required throughout the document to confirm agreement to various sections.

3. **Are there any missing signatures on any pages?**

   - The document does not explicitly indicate missing signatures. However, there are placeholders for initials on several pages (e.g., "Buyer's Initials __________ - _______ Seller's Initials __________ - _______"), which suggest that initials might be required but are not filled in the parsed output.

   - The final execution page (page 10) shows that the Buyer, Seller, and Agent have signed, which is crucial for the document's validity.

   - Without the actual document to verify, it's unclear if these placeholders were intended to be filled or if they are optional. The presence of detected signatures suggests that the main required signatures are present.
```

测试完代理后，别忘了停用虚拟环境 `deactive venv` 。

## 步骤 4：自己构建一个由 Tensorlake 支持的 LangGraph 智能体

你今天就可以在 [张量湖游乐场](https://cloud.tensorlake.ai/) 中或通过我们的 [Python 软件开发工具包](https://pypi.org/project/tensorlake/) 开始使用签名检测功能。注册时，你将获得 **100 个免费积分** ，足以处理大约 100 页内容。

如果你想运行一个已经构建好的智能体，可以在 [张量湖 GitHub 仓库](https://github.com/tensorlakeai/tensorlake/tree/main/examples/signature-detection/) 中查看这个同时使用命令行界面（CLI）和 Streamlit 应用程序的完整示例。

我们构建了 TensorLake，旨在赋能开发者和产品团队，使其能够更高效、更轻松地处理文档，从而实现更多目标。