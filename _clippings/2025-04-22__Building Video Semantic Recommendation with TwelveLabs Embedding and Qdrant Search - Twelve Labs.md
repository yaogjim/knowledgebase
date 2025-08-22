---
title: "Building Video Semantic Recommendation with TwelveLabs Embedding and Qdrant Search - Twelve Labs"
source: "https://www.twelvelabs.io/blog/content-recommender"
author:
published: 2025-07-11
created: 2025-04-22
description: "Recognized by leading researchers as the most performant AI for video understanding; surpassing benchmarks from cloud majors and open-source models."
tags:
  - "clippings"
---
教程

### 使用 TwelveLabs 嵌入和 Qdrant 搜索构建视频语义推荐

赫里希克什·亚达夫

在本教程中，我们将构建一个能够在语义层面理解视频内容的推荐系统。通过将 TwelveLabs 的视频嵌入功能与 Qdrant 向量相似性搜索相结合，我们将创建一个基于视频实际含义（而非仅仅基于关键词匹配）来查找相关视频的引擎。

![](https://framerusercontent.com/images/UBpkGi0Lq6691BouUkPiZ6M3A.png)

2025 年 4 月 11 日

10 Min

复制文章链接

#### 介绍

要是你的内容推荐系统能够真正理解视频里发生了什么，而不只是依赖标签、文字记录和关键词呢？ 🔍

在本教程中，我们将构建一个能够在语义层面理解视频内容的推荐系统。通过将 TwelveLabs 的视频嵌入功能与 Qdrant 向量相似性搜索相结合，我们将创建一个基于视频实际含义而非仅仅关键词匹配来查找相关视频的引擎。

让我们探索一下这个应用程序是如何工作的，以及如何使用 TwelveLabs Python 软件开发工具包和 Qdrant Cloud 快速入门来构建类似的解决方案。

你可以在此处探索该应用程序的演示：TwelveLabs 内容推荐

![](https://framerusercontent.com/images/pb6LNvPJN3O4M2uAwddzRBM7Do.gif)

#### 前提条件

- 通过在 TwelveLabs Playground 注册来生成一个 API 密钥。
- 按照设置指南设置 Qdrant Cloud。
- 在 Github 上找到此应用程序的存储库。
- 你应该熟悉 Python、Flask 和 Next.js

  

#### 演示应用程序

此演示应用程序展示了语义视频内容推荐的强大功能。用户可以选择基于意图的类别，系统通过语义相似性匹配推荐相关内容。用户还可以指定自己的情绪，以接收与其情绪状态相符的内容。

该系统在 Qdrant Cloud 中存储来自不同类别的大量动画视频的嵌入向量。

#### 应用程序的工作原理

该应用程序分两个主要阶段运行：

- 嵌入生成与存储 - 系统使用 Marengo 2.7 创建视频嵌入，并通过 S3 存储桶生成公共 URL。这些嵌入及其元数据存储在 Qdrant Cloud 向量数据库集合中。
- 搜索与检索 - 当用户输入他们的偏好和搜索查询时，系统使用 Marengo 2.7 将文本转换为嵌入向量，并对相关视频进行语义搜索。用户可以通过调整心情或选择新的偏好来优化结果，系统会从 Qdrant Cloud 集合中获取更新后的推荐。
![](https://framerusercontent.com/images/GNVIJmgoSB4aLzNo7MmrdetE.png)

要使应用程序按预期运行，您必须将嵌入数据插入集合中，或者您可以参考此应用程序中使用的此处提供的示例数据。

  

#### 准备步骤

1. 从 TwelveLabs Playground 获取您的 API 密钥并设置您的环境变量。
2. 从 Github 克隆项目。
3. 创建一个包含您的 TwelveLabs 和 Qdrant 凭证的.env 文件。
4. 设置一个 Qdrant Cloud 实例。按照 Qdrant Cloud 集群的设置指南进行操作。

一旦你完成了这些步骤，你就可以开始开发了！

  

#### 内容推荐应用程序操作指南

本教程将向您展示如何构建一个视频内容推荐应用程序。该应用程序的前端使用 Next.js，后端使用启用了 CORS 的 Flask API。我们将专注于实现内容推荐的核心后端功能并设置应用程序。

你将学习如何设置 Qdrant Cloud 客户端、生成并插入嵌入向量，以及与集合进行交互以检索相关视频。有关详细的代码结构和设置说明，请查看 GitHub 上的 README.md。

  

##### 1 - 嵌入生成及插入到 Qdrant 的指南

  

###### 步骤 1 - 设置与依赖项

让我们从安装必要的依赖项开始。

!pip install qdrant-client boto3

!pip install twelvelabs pytube flask flask-cors python-dotenv

现在让我们导入我们需要的库：

import os

import uuid

import boto3

from botocore.exceptions import ClientError

import requests

from IPython.display import display,HTML

import shutil

import pandas as pd

from twelvelabs import TwelveLabs

from qdrant\_client import QdrantClient,models

from qdrant\_client.models import PointStruct

import time

###### 步骤 2 - 配置服务

让我们配置 AWS S3、TwelveLabs 和 Qdrant。首先，设置一个 AWS S3 存储桶以生成用于流传输的公共视频 URL。然后，初始化 Qdrant 和 TwelveLabs 客户端以实现高效的视频嵌入和搜索。

\# AWS S3 Configuration

AWS\_ACCESS\_KEY = "YOUR\_AWS\_ACCESS\_KEY"

AWS\_SECRET\_KEY = "YOUR\_AWS\_SECRET\_KEY"

AWS\_BUCKET\_NAME = "YOUR\_BUCKET\_NAME"

AWS\_REGION = "us-east-1" \# Change to your region

  

\# Initialize S3 client

s3\_client = boto3.client (

's3',

aws\_access\_key\_id = AWS\_ACCESS\_KEY,

aws\_secret\_access\_key = AWS\_SECRET\_KEY,

region\_name = AWS\_REGION

)

  

\# Twelve Labs Configuration

TWELVE\_LABS\_API\_KEY = "YOUR\_TWELVE\_LABS\_API\_KEY"

twelvelabs\_client = TwelveLabs (api\_key = TWELVE\_LABS\_API\_KEY)

  

\# Qdrant Configuration

QDRANT\_HOST = "YOUR\_QDRANT\_HOST"

QDRANT\_API\_KEY = "YOUR\_QDRANT\_API\_KEY"

COLLECTION\_NAME = "content\_collection"

VECTOR\_SIZE = 1024 \# Size of embeddings from Twelve Labs

  

\# Initialize Qdrant client

qdrant\_client = QdrantClient (

url = f"https:// { QDRANT\_HOST } ",

api\_key = QDRANT\_API\_KEY,

timeout = 20,

prefer\_grpc = False

)

  

在配置 Qdrant 客户端时，设置 `timeout=20` 以防止无限期等待并避免延迟。设置 `prefer_grpc=False` 是因为 Flask 原生支持 HTTP REST API 而不是 gRPC。这确保了 Flask 和 Qdrant 之间使用标准 HTTP 进行顺畅通信。

定义视频目录并访问其中的 MP4 文件夹。此设置对于后续处理步骤至关重要。

\# Get a list of video files

video\_dir = "downloads/video\_content"

video\_files = \[f for f in os.listdir (video\_dir) if f.endswith ('.mp4')\]

  

###### 步骤 3 - 将视频上传到 AWS S3

首先，我们需要一个函数来将视频上传到 AWS S3 存储桶并生成公共 URL。返回公共 URL 并将其存储为每个视频的元数据。

def upload\_to\_s3 (file\_path,filename):

try:

\# Upload the file

s3\_client.upload\_file (

file\_path,

AWS\_BUCKET\_NAME,

f"videos-embed/ { filename } ",

ExtraArgs = {

'ACL': 'public-read',

'ContentType': 'video/mp4'

}

)

  

\# Generate the public URL

url = f"https:// { AWS\_BUCKET\_NAME }.s3.{ AWS\_REGION }.amazonaws.com/videos-embed/ { filename } "

print (f"Uploaded to S3: { url } ")

return url

  

except ClientError as e:

print (f"Error uploading to S3: { str (e) } ")

raise

  

###### 步骤 4 - 使用 Marengo 2.7 生成视频嵌入

现在我们将创建一个函数，用于使用 TwelveLabs Marengo-retrieval-2.7 引擎生成视频嵌入。你可以在此处找到视频嵌入生成和插入的代码。

def create\_video\_embedding (video\_path,max\_retries = 3,retry\_delay = 5):

if not twelvelabs\_client:

raise ValueError ("Twelve Labs API key not configured")

  

retries = 0

while retries < max\_retries:

try:

print (f"Creating whole video embedding for { video\_path }... (Attempt { retries + 1 } / { max\_retries })")

  

\# Use video\_embedding\_scopes parameter set to \["clip", "video"\] to get whole video embedding

task = twelvelabs\_client.embed.task.create (

model\_name = "Marengo-retrieval-2.7",

video\_file = video\_path,

video\_embedding\_scopes = \["clip","video"\]

)

  

print (f"Created task: id= { task.id }, status= { task.status } ")

task.wait\_for\_done (sleep\_interval = 3)

task\_result = twelvelabs\_client.embed.task.retrieve (task.id)

  

if task\_result.status!= 'ready':

raise ValueError (f"Task failed with status: { task\_result.status } ")

  

return task\_result

  

except Exception as e:

print (f"Error creating embedding (attempt { retries + 1 }): { str (e) } ")

retries += 1

if retries < max\_retries:

print (f"Retrying in { retry\_delay } seconds...")

time.sleep (retry\_delay)

retry\_delay \*= 2

else:

print ("Max retries reached, giving up.")

raise

`video_embedding_scopes` 被设置为剪辑和视频，以便为整个视频剪辑生成嵌入。

  

###### 步骤 5 - 将嵌入内容与元数据插入到 Qdrant 中

让我们创建一个函数，将生成的嵌入向量存储在我们的 Qdrant 向量数据库中。视频嵌入向量作为一个带有元数据有效负载的点进行存储，从而提高可搜索性。元数据中的视频 URL 支持流传输。

def store\_in\_qdrant (task\_result,video\_id,s3\_url,original\_filename):

if not qdrant\_client:

raise ValueError ("Qdrant client not configured")

  

try:

print (f"Processing video embedding for { video\_id }...")

  

\# The embedding will be in the segments with embedding\_scope="video"

if task\_result.video\_embedding and task\_result.video\_embedding.segments:

video\_segments = \[s for s in task\_result.video\_embedding.segments

if hasattr (s,'embedding\_scope') and s.embedding\_scope == 'video'\]

  

if video\_segments:

print (f"Found video-scope embedding")

embedding\_vector = video\_segments \[0\].embeddings\_float

else:

\# If no video scope segment is found, use the first segment as fallback

print (f"No video-scope embedding found, using first available segment")

embedding\_vector = task\_result.video\_embedding.segments \[0\].embeddings\_float

else:

raise ValueError ("No embeddings found in the response")

  

\# Create a unique point structure for Qdrant storage

point = PointStruct (

id = uuid.uuid4 ().int & ((1 << 64) - 1),\# Generate a unique 64-bit integer ID

vector = embedding\_vector,\# Store the extracted embedding vector

payload = {

'video\_id': video\_id,

'video\_url': s3\_url,\# Store the public S3 URL of the video

'is\_url': True,

'original\_filename': original\_filename \# Save the original filename

}

)

  

\# Insert the generated embedding point into the Qdrant collection

qdrant\_client.upsert (collection\_name = COLLECTION\_NAME,points = \[point\])

print (f"Stored whole video embedding in Qdrant")

return 1

except Exception as e:

print (f"Error storing in Qdrant: { str (e) } ")

raise

  

###### 步骤 6 - 视频处理管道

现在我们将定义一个简化的流程，该流程连接所有组件，通过我们的管道处理视频。

通过完整流程处理目录中的所有视频：

1. 上传到 AWS S3 存储桶
2. 使用 TwelveLabs 生成嵌入向量
3. 将嵌入向量存储在 Qdrant 中

\# Process each video

for filename in video\_files \[:5\]: \# Process first 5 videos or you can setup as per convenience

try:

print (f"\\nProcessing { filename }...")

video\_path = os.path.join (video\_dir,filename)

video\_id = f" { str (uuid.uuid4 ()) \[:8\] } \_ { filename } "

\# Upload to S3

s3\_url = upload\_to\_s3 (video\_path,video\_id)

\# Generate embeddings

task\_result = create\_video\_embedding (video\_path)

\# Store in Qdrant

store\_in\_qdrant (task\_result,video\_id,s3\_url,filename)

print (f"Successfully processed { filename } ")

except Exception as e:

print (f"Error processing { filename }: { str (e) } ")

视频嵌入和元数据现在存储在 Qdrant Cloud 中。下一步是将我们的应用程序连接到集合以进行检索。

  

##### 2 - 使用 Flask 构建搜索 API

  

###### 步骤 1 - 设置跨域资源共享源

要启用跨域请求，我们需要在 Flask 应用程序中配置 CORS（跨域资源共享）。这允许托管在不同域上的 Web 客户端访问我们的 API。你可以在 app.py 中找到完整的后端实现。

app = Flask (\_\_name\_\_)

CORS (app,resources = { r"/\*": { "origins": "\*" } })

  

###### 步骤 2 - 初始化 Qdrant 集合

如果我们的 Qdrant 集合不存在，我们需要对其进行初始化。此设置可确保我们的向量数据库能够正确检索视频嵌入。初始化 TwelveLabs 客户端以生成用于语义搜索功能的搜索查询嵌入。

\# Get credentials from environment variables

API\_KEY = os.getenv ('API\_KEY')

QDRANT\_HOST = os.getenv ('QDRANT\_HOST')

QDRANT\_API\_KEY = os.getenv ('QDRANT\_API\_KEY')

  

\# Qdrant Configuration

COLLECTION\_NAME = "content\_collection"

VECTOR\_SIZE = 1024 \# Dimension of vector embeddings

  

\# Initialize clients

try:

client = TwelveLabs (api\_key = API\_KEY)

qdrant\_client = QdrantClient (

url = f"https:// { QDRANT\_HOST } ",

api\_key = QDRANT\_API\_KEY,

timeout = 20

)

logger.info ("Successfully initialized API clients")

except Exception as e:

logger.error (f"Failed to initialize clients: { str (e) } ")

raise

  

def init\_qdrant ():

try:

\# Fetch all existing collections

collections = qdrant\_client.get\_collections ().collections

collection\_exists = any (col.name == COLLECTION\_NAME for col in collections)

if not collection\_exists:

\# Create the collection with specified vector configuration if it doesn't exist

qdrant\_client.recreate\_collection (

collection\_name = COLLECTION\_NAME,

vectors\_config = VectorParams (

size = VECTOR\_SIZE,

distance = Distance.COSINE \# Use cosine similarity for retrieval

)

)

logger.info (f"Created collection: { COLLECTION\_NAME } ")

except Exception as e:

logger.error (f"Qdrant initialization error: { str (e) } ")

raise

  

###### 步骤 3 - 创建简单搜索功能

本节实现了一个搜索端点，该端点允许用户搜索视频。该端点处理搜索查询，通过 TwelveLabs 生成嵌入，从 Qdrant 检索相似向量，并返回匹配结果。

![](https://framerusercontent.com/images/4bKRwaxiaioOOLPeo0TCMOiKtI.png)

让我们为视频搜索创建一个搜索端点。

@ app.route ('/search',methods = \['POST'\])

def search ():

\# Ensure the request contains JSON data

if not request.is\_json:

logger.warning ("Missing JSON data")

return jsonify ({ 'error': 'Request must be JSON format' }),400

\# Get and validate query

data = request.get\_json ()

query = data.get ('query')

if not query:

logger.warning ("Empty query parameter")

return jsonify ({ 'error': 'Missing query parameter' }),400

logger.info (f"Processing search: ' { query } '")

try:

\# Generate embedding for the search query

formatted\_query = f"Recommend - { query } "

embedding\_response = client.embed.create (

model\_name = "Marengo-retrieval-2.7",

text = formatted\_query

)

  

\# Get the embedding vector

vector = embedding\_response.text\_embedding.segments \[0\].embeddings\_float

\# Similarity search from the Qdrant collection

query\_response = qdrant\_client.query\_points (

collection\_name = COLLECTION\_NAME,

query = vector,

limit = 10,

with\_payload = True

)

\# Extract and format results

search\_results = query\_response.points

logger.info (f"Found { len (search\_results) } matching results")

\# If no results, return empty list

if not search\_results:

return jsonify (\[\])

\# Build formatted response

formatted\_results = \[\]

for result in search\_results:

point\_id = result.id

score = float (result.score)

payload = result.payload

formatted\_results.append ({

'video\_id': payload.get ('video\_id',f"video\_ { point\_id } "),

'filename': payload.get ('original\_filename',payload.get ('filename','video.mp4')),

'start\_time': float (payload.get ('start\_time',0)),

'end\_time': float (payload.get ('end\_time',30)),

'score': score,

'confidence': 'high' if score > 0.7 else 'medium',

'url': payload.get ('video\_url')

})

logger.info (f"Returning { len (formatted\_results) } results")

return jsonify (formatted\_results)

except Exception as e:

logger.exception (f"Search error: { str (e) } ")

return jsonify ({ 'error': 'Search failed','details': str (e) }),500

它是这样工作的：

1. 从请求中接收搜索查询
2. 使用 TwelveLabs 生成嵌入向量
3. 在 Qdrant 中搜索相似向量
4. 以结构化格式返回匹配的视频
![](https://framerusercontent.com/images/JImOUhVwLhQQgRqWUsehdKRVbGE.gif)

  

#### 更多可用于试验教程的想法

了解应用程序的工作原理有助于您创建满足用户需求的创新产品。以下是视频内容嵌入的一些潜在用例：

🎯 个性化广告插入 —— 动态地将与上下文相关的广告插入视频中。

⚙️实时相似度匹配 —— 新内容上传时即时找到相似视频。

📊 趋势分析与洞察 —— 基于嵌入模式对视频趋势进行聚类和分析。

  

#### 结论

本教程展示了视频理解如何创建更智能、更准确的内容推荐。通过使用 TwelveLabs 进行视频嵌入，并使用 Qdrant 进行快速向量搜索，我们构建了一个能够理解视频内容的系统，而不仅仅局限于手动转录、标签或关键词。这种方法能够提供更好的推荐，使用户保持参与度，并能轻松扩展以处理大型视频集。作为一个开源解决方案，它可以针对从教育到娱乐等各个行业进行定制。

  

#### 其他资源

了解有关嵌入生成引擎 Marengo-retrieval-2.7 的更多信息。要进一步探索 TwelveLabs 并加深您对视频内容分析的理解，请查看以下资源：

- 尝试集成：立即注册 TwelveLabs 嵌入 API 公开测试版，并开始使用 Qdrant 构建自己的人工智能视频应用程序。
- 探索更多用例：访问 Qdrant Cloud 快速入门指南，了解如何根据您的业务需求实施类似的工作流程。
- 加入对话：在 TwelveLabs Discord 上分享你对此次集成的反馈。
- 探索教程：通过我们全面的教程更深入地了解 TwelveLabs 的功能

我们鼓励您利用这些资源来扩展您的知识，并使用 TwelveLabs 视频理解技术创建创新应用程序。

#### 相关文章

[![](https://framerusercontent.com/images/PWYixWAaBu15PyfPL1SpVNI1ESk.png)](https://www.twelvelabs.io/blog/security-analysis)

[使用 Twelve Labs 构建安全分析应用程序](https://www.twelvelabs.io/blog/security-analysis)

[![](https://framerusercontent.com/images/Tg3mwrbJRSPDD4GvbNAwrRd2On4.png)

使用 Twelve Labs 和 Milvus 构建多模态检索增强生成应用程序

](https://www.twelvelabs.io/blog/fashion-chat-assistant)[![](https://framerusercontent.com/images/2qQiwkKXesYczPLkwRWyT3XWXCc.png)

使用 Twelve Labs 构建一个奥运视频分类应用程序

](https://www.twelvelabs.io/blog/olympics-classification)[![](https://framerusercontent.com/images/WHHJPUhjOkptvGqH1ZrSc6Hbok.png)

使用 Twelve Labs 构建视频人工智能面试分析器

](https://www.twelvelabs.io/blog/interview-analyzer)