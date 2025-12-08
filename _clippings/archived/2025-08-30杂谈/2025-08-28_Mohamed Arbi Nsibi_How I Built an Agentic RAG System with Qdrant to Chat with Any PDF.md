---
title: "How I Built an Agentic RAG System with Qdrant to Chat with Any PDF"
source: "https://medium.com/@mohammedarbinsibi/how-i-built-an-agentic-rag-system-with-qdrant-to-chat-with-any-pdf-4f680e93397e"
author:
  - "[[Mohamed Arbi Nsibi]]"
published: 2025-08-28
created: 2025-08-28
description: "Ever wished you could just chat with a PDF document instead of scrolling through endless pages looking for answers? Well, that’s exactly what we’re going to build today! Think of it like having a…"
tags:
  - "Mohamed Arbi Nsibi"
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

*或者：我是如何构建一个能像人类一样读取 PDF 并回答问题的人工智能助手的*

嘿，你好呀！👋

是否曾希望自己能与 PDF 文档聊天，而不是翻遍无数页面去寻找答案？嗯，这正是我们今天要构建的！

可以把它想象成有一个超级聪明的朋友，他读过你的整篇文档，能立刻回答你提出的任何问题。但这不是一个朋友，而是一个人工智能系统，它结合了视觉（“读取”PDF）、记忆（存储所学内容）和推理（给你智能回答）。

让我们深入其中，一步步构建它！

## 我们要构建什么？

我们正在创建一个所谓的“智能检索增强生成（Agentic RAG）”系统。别被这个花哨的名字吓到：

- **智能体的** \= 它像智能体一样做出决策（可以把它想象成一个智能助手）
- **RAG** = 检索增强生成（一种花哨的说法，意思是“查找信息并生成答案”）

这就好比有一个拥有照相式记忆的图书管理员，他能立即从你的文档中找到并解释任何信息。

## 设置我们的工具

首先，让我们导入所有需要的库。可以把这想象成在做饭前收集所有烹饪食材：

```c
import os
import base64
from PIL import Image

import operator
from io import BytesIO
import pypdfium2 as pdfium
import backoff
import asyncio

from typing import Annotated, Sequence, TypedDict, Literal
from openai import OpenAIError
from openai import AsyncOpenAI, OpenAI
from langchain_openai import ChatOpenAI
from langchain import hub
from langchain_core.messages import AnyMessage, BaseMessage, HumanMessage, SystemMessage
from langchain.tools.retriever import create_retriever_tool
from langgraph.graph.message import add_messages
from langgraph.graph import START, END, StateGraph, MessagesState
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langgraph.prebuilt import tools_condition, ToolNode

from IPython.display import Image, display
from pydantic import BaseModel, Field
```

现在让我们来设置我们的人工智能模型配置：

```c
MODEL = "gpt-4o-2024-08-06"
baseurl = ""
apikey = ""

clienta = AsyncOpenAI(api_key=apikey,  base_url=baseurl)
os.environ["OPENAI_API_BASE"] = baseurl
os.environ["OPENAI_API_KEY"] = apikey
```

## 教我们的人工智能“看懂”PDF 文件

神奇之处就在这里！我们要创建一个函数，它能像人一样查看 PDF 页面并从中提取文本。这就好比拥有了能读取任何文档的超能力眼睛：

```c
@backoff.on_exception(backoff.expo, OpenAIError)
async def parse_page_with_gpt(base64_image: str) -> str:
    messages=[
        {
            "role": "system",
            "content": """
            
            You are a helpful assistant that extracts information from images.
            
            """
        },
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Extract information from image into text"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}",
                        "detail": "auto"
                    },
                },
            ],
        }
    ]
    response = await clienta.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0,
        max_tokens=4096,
    )
    return response.choices[0].message.content or ""
```

这个功能就像是给一个非常聪明的人看一张图片，然后让他们告诉你他们在图片中看到写了什么。

## 处理整个 PDF

现在让我们创建一个函数，它接受一整个 PDF 并处理其中的每一页：

```c
async def document_analysis(filename: str) -> str:
    """
    Document Understanding
Args:
        filename: pdf filename str
    """
    pdf = pdfium.PdfDocument(filename)
    images = []
    for i in range(len(pdf)):
        page = pdf[i]
        image = page.render(scale=8).to_pil()
        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        img_byte = buffered.getvalue()
        img_base64 = base64.b64encode(img_byte).decode("utf-8")
        images.append(img_base64)
    text_of_pages = await asyncio.gather(*[parse_page_with_gpt(image) for image in images])
    
    results = []
    extracted_texts = [doc for doc in text_of_pages]
    # Clean each string in the list and append to json_results
    for text in extracted_texts:
        results.append(text)
        
    return results
```

可以把这想象成有一个阅读速度超快的人，他能快速翻阅一本书的每一页，并记住所看到的一切。

## 让我们处理我们的测试文档

是时候给我们的系统输入一个真正的 PDF 文件了！我们正在使用一个名为“stock price LSTM- GNN.pdf”的文档：

```c
docs_list = await document_analysis("stock price LSTM- GNN.pdf")
```

这将返回从每一页提取的文本列表。

让我们看看我们得到了什么，并将其临时保存：

```c
import uuid

output_file_path = f"{uuid.uuid4()}.txt"
with open(output_file_path, 'w') as json_file:
    json.dump(docs_list, json_file, indent=2)
print(f"data has been written to {output_file_path}")
```

输出： `data has been written to ee273450-7e77-42b3-8281-d453980ace5c.txt`

## 创建我们的智能记忆系统

现在我们需要给我们的人工智能一种方法来记住并搜索所有这些信息。这就好比为一本书创建一个索引，但要聪明得多：

```c
from langchain_community.document_loaders import TextLoader

loader = TextLoader(output_file_path)
data = loader.load()
```

既然我们不再需要那个临时文件了，那就把它清理掉吧：

```c
# Check if the file exists
if os.path.exists(output_file_path):
    
    # Delete the file
    os.remove(output_file_path)
    print(f"File {output_file_path} deleted successfully.")
else:
    print("File does not exist.")
```

现在让我们把文档分成更小、更易于理解的块（就像把披萨切成片一样）：

```c
from langchain_core.documents import Document
from langchain_text_splitters import CharacterTextSplitter

documents = [Document(page_content=text, metadata={"page": i})
             for i, text in enumerate(docs_list)]

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=400)
doc_splits = text_splitter.split_documents(documents)
len(doc_splits)
```

## 构建我们的智能搜索数据库

我们在这里创建系统的“大脑”——一个能够理解文本含义而非仅仅匹配关键词的向量数据库：

```c
embedding_model = OpenAIEmbeddings()
# your Qdrant credentials 
QDRANT_URL=""
QDRANT_API_KEY=""

# Initialize Qdrant client connection using the API key and URL

import qdrant_client
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

client = QdrantClient(
    QDRANT_URL,
    api_key = QDRANT_API_KEY
)

# Define the collection name where we'll store our document vectors
QDRANT_COLLECTION = "agentic_collection"
collection_config = qdrant_client.http.models.VectorParams(
        size=1536, # 768 for instructor-xl, 1536 for OpenAI # 384 for sentence trans= fastembed 768 for mpnet
        distance=qdrant_client.http.models.Distance.COSINE
    )

# Recreate (or create) the collection in Qdrant to store our document vectors
# This will wipe existing data if the collection already exists
client.recreate_collection(
    collection_name = QDRANT_COLLECTION,
    vectors_config=collection_config
)
```
```c
# Use LangChain's Qdrant wrapper to interface with the Qdrant vector store
from langchain.vectorstores import Qdrant

vectorstore = Qdrant(
        client=client,
        collection_name=QDRANT_COLLECTION,
        embeddings=embedding_model
    )
texts = [doc.page_content for doc in doc_splits]
vectorstore.add_texts(texts)
# Create a retriever interface over the vector store
retriever=vectorstore.as_retriever()
```

我们将文档嵌入存储在强大的向量数据库 **Qdrant** 中。我们使用合适的向量大小和相似度度量来配置集合，插入文档块，并使用 LangChain 的检索器接口对我们的 PDF 进行高效的语义搜索。

**如果你不熟悉 Qdrant，本文将向你展示如何在不到 10 分钟的时间内完成设置：** [**Qdrant 设置**](https://medium.com/@mohammedarbinsibi/why-qdrant-will-be-your-favorite-vector-database-setup-in-10-minutes-bc0a79651a14) **。**

现在让我们把我们的检索器变成一个我们的人工智能代理可以使用的工具：

```c
retriever_tool = create_retriever_tool(
    retriever,
    "document_understanding",
    "Retrieve and provide insights on document content analysis and knowledge extraction",
)
tools = [retriever_tool]
```

## 创建我们的人工智能代理的“思维过程”

这就是事情变得非常酷的地方！我们要创建一个人工智能代理，它可以像人类一样一步一步地思考问题。

首先，让我们定义我们的智能体将如何跟踪对话：

```c
class AgentState(TypedDict):
    # The add_messages function defines how an update should be processed
    # Default is to replace. add_messages says "append"
    messages: Annotated[Sequence[BaseMessage], add_messages]
```

## 教我们的智能体检查信息是否相关

这个函数就像是有一个质量检查器，它能确保我们找到的信息确实回答了问题：

```c
### Edges
def grade_documents(state) -> Literal["generate", "rewrite"]:
    """
    Determines whether the retrieved documents are relevant to the question.
Args:
        state (messages): The current state
    Returns:
        str: A decision for whether the documents are relevant or not
    """
    print("---CHECK RELEVANCE---")
    # Data model
    class grade(BaseModel):
        """Binary score for relevance check."""
        binary_score: str = Field(description="Relevance score 'yes' or 'no'")
    # LLM
    model = ChatOpenAI(temperature=0, model="gpt-4o", streaming=True)
    # LLM with tool and validation
    llm_with_tool = model.with_structured_output(grade)
    
    # Prompt
    prompt = PromptTemplate(
        template="""You are a grader assessing relevance of a retrieved document to a user question. \n 
        Here is the retrieved document: \n\n {context} \n\n
        Here is the user question: {question} \n
        If the document contains keyword(s) then grade it as relevant. \n
        Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question.""",
        input_variables=["context", "question"],
    )
    # Chain
    chain = prompt | llm_with_tool
    messages = state["messages"]
    last_message = messages[-1]
    question = messages[0].content
    docs = last_message.content
    print("question: ", question)
    print("context: ", docs)
    scored_result = chain.invoke({"question": question, "context": docs})
    score = scored_result.binary_score
    if score == "yes":
        print("---DECISION: DOCS RELEVANT---")
        return "generate"
    else:
        print("---DECISION: DOCS NOT RELEVANT---")
        print(score)
        return "rewrite"
```

## 构建我们代理的主要功能

现在让我们创建系统的主要“工作者”。可以把它们想象成不同的专家：

```c
### Nodes
def agent(state):
    """
    Invokes the agent model to generate a response based on the current state. Given
    the question, it will decide to retrieve using the retriever tool, or simply end.

Args:
        state (messages): The current state
    Returns:
        dict: The updated state with the agent response appended to messages
    """
    print("---CALL AGENT---")
    messages = state["messages"]
    model = ChatOpenAI(temperature=0, streaming=True, model="gpt-4o")
    model = model.bind_tools(tools)
    response = model.invoke(messages)
    # We return a list, because this will get added to the existing list
    return {"messages": [response]}

def rewrite(state):
    """
    Transform the query to produce a better question.
    Args:
        state (messages): The current state
    Returns:
        dict: The updated state with re-phrased question
    """
    print("---TRANSFORM QUERY---")
    messages = state["messages"]
    question = messages[0].content
    msg = [
        HumanMessage(
            content=f""" \n 
    Look at the input and try to reason about the underlying semantic intent / meaning. \n 
    Here is the initial question:
    \n ------- \n
    {question} 
    \n ------- \n
    Formulate an improved question: """,
        )
    ]
    # Grader
    model = ChatOpenAI(temperature=0, model="gpt-4o", streaming=True)
    response = model.invoke(msg)
    return {"messages": [response]}
```
```c
def generate(state):
    """
    Generate answer
    Args:
        state (messages): The current state
    Returns:
         dict: The updated state with re-phrased question
    """
    print("---GENERATE---")
    messages = state["messages"]
    question = messages[0].content
    last_message = messages[-1]
    docs = last_message.content
    # Prompt
    prompt = hub.pull("rlm/rag-prompt")
    # LLM
    llm = ChatOpenAI(model_name="gpt-4o", temperature=0, streaming=True)
    # Post-processing
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)
    # Chain
    rag_chain = prompt | llm | StrOutputParser()
    # Run
    print("context: ", docs)
    print("question: ", question)
    response = rag_chain.invoke({"context": docs, "question": question})
    return {"messages": [response]}

print("*" * 20 + "Prompt[rlm/rag-prompt]" + "*" * 20)
prompt = hub.pull("rlm/rag-prompt").pretty_print()
```

## 整合一切：构建我们的工作流程

现在到了激动人心的部分——我们要将所有这些部分连接成一个能够思考、搜索和响应的智能工作流程：

```c
# Define a new graph
workflow = StateGraph(AgentState)

# Define the nodes we will cycle between
workflow.add_node("agent", agent)  # agent
retrieve = ToolNode([retriever_tool])
workflow.add_node("retrieve", retrieve)  # retrieval
workflow.add_node("rewrite", rewrite)  # Re-writing the question
workflow.add_node(
    "generate", generate
)  # Generating a response after we know the documents are relevant
# Call agent node to decide to retrieve or not
workflow.add_edge(START, "agent")
# Decide whether to retrieve
workflow.add_conditional_edges(
    "agent",
    # Assess agent decision
    tools_condition,
    {
        # Translate the condition outputs to nodes in our graph
        "tools": "retrieve",
        END: END,
    },
)
# Edges taken after the \`action\` node is called.
workflow.add_conditional_edges(
    "retrieve",
    # Assess agent decision
    grade_documents,
)
workflow.add_edge("generate", END)
workflow.add_edge("rewrite", "agent")
# Compile
graph = workflow.compile()
```

让我们可视化我们的工作流程（这是可选的，但看到会很酷）：

```c
from IPython.display import Image, display

try:
    display(Image(graph.get_graph(xray=True).draw_mermaid_png()))
except Exception:
    # This requires some extra dependencies and is optional
    pass
```

## 测试我们的智能 PDF 聊天机器人

到了关键时刻了！让我们向我们的人工智能询问一些关于这份文档的问题：

**测试 1：询问有关 PDF 中任何信息的内容，例如：**

```c
import pprint

inputs = {
    "messages": [
        ("user", """
        what could be the number of test day corresponding to the 
        highest MSE value in figure 4?
        """),
        #or maybe we can ask about : 
        #How is the graph constructed for the GNN component, and what metrics are used to define relationships between stocks?
    ]
}
for output in graph.stream(inputs):
    for key, value in output.items():
        pprint.pprint(f"Output from node '{key}':")
        pprint.pprint("---")
        pprint.pprint(value, indent=2, width=80, depth=None)
    pprint.pprint("\n---\n")
```

系统经过思考过程后做出回应： *由于市场波动，图 4 中 MSE 值最高的测试日期为 2022 年 11 月 10 日和 2022 年 11 月 30 日。*

**测试2：询问文件中的一张示例图片（图4）**

```c
import pprint

inputs = {
    "messages": [
        ("user", """
        what is the value of MSE corresponding to CNN in the figure 5 ?
        """),
    ]
}
for output in graph.stream(inputs):
    for key, value in output.items():
        pprint.pprint(f"Output from node '{key}':")
        pprint.pprint("---")
        pprint.pprint(value, indent=2, width=80, depth=None)
    pprint.pprint("\n---\n")
```
![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*CcTyIT2FuH1Ft2wBFNmfJQ.png)

论文中的图5

并且它正确回复： *图 5 中卷积神经网络（CNN）的均方误差（MSE）为 0.00302。*

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*Y5aDeb0Hkl12MgIoDIfZLg.png)

正确答案

## 我们学到了什么？

🎉 **恭喜！** 你刚刚构建了一个复杂的人工智能系统，它可以：

1. 使用视觉人工智能（就像拥有超能力的眼睛一样） **查看和理解 PDF 文件**
2. 通过将信息存储在向量数据库中来 **记住所有内容** （就像拥有完美的记忆力一样）
3. 使用代理工作流程（比如拥有一个智能助手）来思考问题
4. **找到相关信息** 并检查它是否真的回答了问题
5. 根据文档内容生成有用的回答

**有趣的部分是什么？** 这个系统不仅仅是进行关键词匹配——它实际上能理解你问题的含义，即使你用不同的方式提问，它也能找到相关信息。

**实际应用：**

- 法律文件分析
- 研究论文问答
- 公司政策助手
- 技术手册助手
- 学术学习辅助工具

这种方法的美妙之处在于，一旦你处理了一份文档，你就可以向它提出数百个问题，而无需手动在大量的内容中搜索。这就好比有一个超级智能的研究助手，它从不疲倦，总能确切记得在哪里看到了你正在寻找的那个特定细节！

相当不错，对吧？😊

如果你想查看代码，这里是 GitHub 仓库：  
[https://github.com/Goodnight77/Just-RAG/tree/main/Agentic-Qdrant-RAG](https://github.com/Goodnight77/Just-RAG/tree/main/Agentic-Qdrant-RAG)

随时可以尝试，随意摆弄，如果遇到问题就告诉我。我总是很乐意帮忙！
