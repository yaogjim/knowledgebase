---
title: "2025-11-05_Philipp_Schmid_使用_Gemini_n8n_和_Google_Cloud_Run_构建您的首个_AI_智能体"
source: "https://www.philschmid.de/n8n-cloud-run-gemini"
author:
  - "[[@Philipp Schmid]]"
published: 2025-11-05
created: 2025-11-05
description:
tags:
  - "#startup"
  - "#pruning"
  - "philschmid"
  - "@Philipp Schmid"
status: "inbox"
importance: 2
effort: 2
review_level: 0
review_next: "2025-11-13"
review_interval: null
review_count: 0
decision: null
topics: []
links_out: []
summary: ""
pov: ""
actions: []
---

# ## 使用 Gemini、n8n 和 Google Cloud Run 构建您的首个 AI 智能体

## 使用 Gemini、n8n 和 Google Cloud Run 构建您的首个 AI 智能体

October 30, 2025 8 minute read

[n8n](https://n8n.io/) 是一款功能强大的开源工作流自动化工具，可帮助您连接并自动化各类服务与应用程序。本指南将逐步指导您在 Google Cloud Run 上部署 n8n，搭配 PostgreSQL 数据库实现持久化存储，并利用 Google Gemini 2.5 创建一个简单的 AI 智能体。

在开始之前，您需要拥有一个已配置结算账户的 Google Cloud Platform (GCP) 账户。

## 第一步：安装并配置 gcloud 命令行工具

要从终端与 Google Cloud 交互，您需要安装 Google Cloud CLI。

1.  **安装 gcloud CLI：** 您可以使用以下命令安装 Google Cloud CLI，或根据您的具体操作系统参考 [官方安装指南](https://cloud.google.com/sdk/docs/install) 。
 
 ```bash
 curl https://sdk.cloud.google.com | bash
 
 exec -l $SHELL
 
 gcloud init
 ```
 
 运行 `gcloud version` 命令以验证安装。
 
2.  **登录到 Google Cloud：** 安装完成后，请使用您的 Google Cloud 账户进行身份验证：
 
 将打开一个浏览器窗口，提示您登录并允许 Google Cloud SDK 访问您的账户。请复制认证代码并粘贴到终端中。
 

## 第二步：设置 Google Cloud 项目

我们需要创建一个新的 Google Cloud 项目并启用必要的服务。

1.  **创建新项目：**
 
 ```bash
 export PROJECT_ID="n8n-gemini-$(head /dev/urandom | tr -dc a-z0-9 | head -c 10)"
 
 gcloud projects create "$PROJECT_ID" --name="n8n Gemini Quickstart"
 
 gcloud config set project "$PROJECT_ID"
 ```
 
2.  **关联结算账户：** 您需要为新项目启用结算功能。请运行以下命令并在浏览器中打开链接，以关联您的结算账户。
 
 ```bash
 echo "https://console.cloud.google.com/billing/linkedaccount?project=$PROJECT_ID"
 ```
 
3.  **设置环境变量：**
 
 ```bash
 export REGION="us-central1" # Change to your preferred region, e.g. us-east1, us-west1, etc.
 ```
 
4.  **启用必要的 API：**
 
 ```bash
 gcloud services enable run.googleapis.com \
 
 sqladmin.googleapis.com \
 
 secretmanager.googleapis.com \
 
 iam.googleapis.com
 ```
 

## 第三步：设置数据库和密钥

n8n 需要一个数据库来存储其数据。我们将使用 Cloud SQL for PostgreSQL 和 Secret Manager 来安全地存储凭据。为了成本效益，我们采用了 `db-f1-micro` 层级，但您可以根据需求调整层级、存储大小和区域等参数。更多配置选项，请参阅 [官方文档](https://docs.cloud.google.com/sql/docs/postgres/create-instance) 。

*注意：此过程可能需要约10到15分钟。*

```bash
export N8N_DB_PASSWORD=$(openssl rand -base64 16)

export N8N_ENCRYPTION_KEY=$(openssl rand -base64 42)

 

# Create Cloud SQL instance

gcloud sql instances create n8n-db \

 --database-version=POSTGRES_13 \

 --tier=db-f1-micro \

 --region=$REGION \

 --root-password=$N8N_DB_PASSWORD \

 --storage-size=10GB \

 --no-backup \

 --storage-type=HDD

 

# Create database and user

gcloud sql databases create n8n --instance=n8n-db

gcloud sql users create n8n-user \

 --instance=n8n-db \

 --password=$N8N_DB_PASSWORD

 

# Store secrets in Secret Manager

echo $N8N_DB_PASSWORD | gcloud secrets create n8n-db-password --data-file=- --replication-policy="automatic"

echo $N8N_ENCRYPTION_KEY | gcloud secrets create n8n-encryption-key --data-file=- --replication-policy="automatic"
```

## 第四步：将 n8n 部署到 Cloud Run

现在我们将把 n8n 部署到 Cloud Run，并连接至数据库和密钥。我们需要为 n8n 创建服务账号并授予其密钥访问权限，然后通过必要的环境变量和密钥将 n8n 容器部署到 Cloud Run。

1.  **为 n8n 创建服务账户：**
 
 ```bash
 gcloud iam service-accounts create n8n-service-account \
 
 --display-name="n8n Service Account"
 
 export SERVICE_ACCOUNT_EMAIL="n8n-service-account@$PROJECT_ID.iam.gserviceaccount.com"
 ```
 
2.  **授予必要权限：**
 
 ```bash
 gcloud secrets add-iam-policy-binding n8n-db-password \
 
 --member="serviceAccount:$SERVICE_ACCOUNT_EMAIL" \
 
 --role="roles/secretmanager.secretAccessor"
 
 gcloud secrets add-iam-policy-binding n8n-encryption-key \
 
 --member="serviceAccount:$SERVICE_ACCOUNT_EMAIL" \
 
 --role="roles/secretmanager.secretAccessor"
 
 gcloud projects add-iam-policy-binding $PROJECT_ID \
 
 --member="serviceAccount:$SERVICE_ACCOUNT_EMAIL" \
 
 --role="roles/cloudsql.client"
 ```
 
3.  **部署到 Cloud Run：**
 
 ```bash
 DB_CONNECTION_NAME="$PROJECT_ID:$REGION:n8n-db"
 
 
 
 gcloud run deploy n8n \
 
 --image=n8nio/n8n:latest \
 
 --region=$REGION \
 
 --allow-unauthenticated \
 
 --port=5678 \
 
 --memory=2Gi \
 
 --cpu=1 \
 
 --no-cpu-throttling \
 
 --set-env-vars="N8N_PORT=5678,N8N_PROTOCOL=https,DB_TYPE=postgresdb,DB_POSTGRESDB_DATABASE=n8n,DB_POSTGRESDB_USER=n8n-user,DB_POSTGRESDB_HOST=/cloudsql/$DB_CONNECTION_NAME,DB_POSTGRESDB_PORT=5432,DB_POSTGRESDB_SCHEMA=public,GENERIC_TIMEZONE=UTC,QUEUE_HEALTH_CHECK_ACTIVE=true" \
 
 --set-secrets="DB_POSTGRESDB_PASSWORD=n8n-db-password:latest,N8N_ENCRYPTION_KEY=n8n-encryption-key:latest" \
 
 --add-cloudsql-instances=$DB_CONNECTION_NAME \
 
 --service-account=$SERVICE_ACCOUNT_EMAIL
 ```
 
 *注意：我们使用 `--no-cpu-throttling` 参数来确保 n8n 的后台进程（如定时任务和等待节点）即使在未主动处理 HTTP 请求时也能持续运行。*
 

部署成功后，Cloud Run 将输出您的 n8n 实例的 URL。其格式应类似于：

```bash
Done.
Service [n8n] revision [n8n-00001-qqn] has been deployed and is serving 100 percent of traffic.
Service URL: https://n8n-780597096402.us-central1.run.app
```

## 第五步：创建你的第一个 Gemini 智能体

首次访问您的 n8n 实例后，系统将提示您设置所有者账户。请按照指引创建所有者账户。此处您还可以添加企业许可证（如有）。完成后，您将看到类似这样的界面：

![n8n](/static/blog/n8n-cloud-run-gemini/n8n.png)

我们将从零开始创建一个智能体。但在创建之前，需要先添加 Gemini API 密钥。请点击"凭据"，然后选择"添加首个凭据"，搜索"Google Gemini (PaLM) API"。点击"创建"并按照指引完成新凭据的创建。若您尚未持有 Gemini API 密钥，可通过 [AI Studio](https://aistudio.google.com/app/api-keys) 获取。

![api-key](/static/blog/n8n-cloud-run-gemini/api-key.png)

验证通过后，返回“工作流”界面，点击“从零开始”。此时您将进入“编辑器”界面。点击“添加第一步”并搜索“AI 智能体”。现在您应处于 AI 智能体的配置界面。在屏幕底部中央区域，您会看到“对话模型”、“记忆模块”和“工具”选项，请点击“对话模型”。

![agent-editor](/static/blog/n8n-cloud-run-gemini/agent-editor.png)

随后搜索“Google Gemini Chat Model”。在此处，您应能选择凭据和要使用的模型。定义完成后，点击左上角的“返回画布”。此时您将看到一个搭载 Gemini 的“基础 AI 智能体”。

![agent](/static/blog/n8n-cloud-run-gemini/agent.png)

试试看！点击“打开聊天”并向它提问。

![agent-chat](/static/blog/n8n-cloud-run-gemini/agent-chat.png)

太棒了，成功了！现在，我们来添加一些工具，让它成为一个真正的智能体。请在 AI 智能体下方的“工具”处点击“+”。此时，您会看到可添加到智能体的一系列工具，包括 MCP 服务器、向量数据库或数百种其他工具。

让我们尝试添加“MCP（模型上下文协议）客户端”。MCP 是一种标准，允许 LLMs 连接到外部数据源而无需自定义集成代码。我们将使用它把 Gemini 连接到一个模拟天气服务。作为端点请添加 `https://gemini-api-demos.uc.r.appspot.com/mcp` （注意：无法保证该端点始终可用。）添加 MCP 服务器后，请点击“返回画布”。

您的代理现在应已连接到“MCP 客户端”工具。

![agent-mcp](/static/blog/n8n-cloud-run-gemini/agent-mcp.png)

好的，我们来测试一下。点击“打开聊天”功能，询问纽约的天气情况，记得在问题中包含“日期”，例如 `What is the weather in New York on 2025-10-29?` 。

![agent-mcp-chat](/static/blog/n8n-cloud-run-gemini/agent-mcp-chat.png)

太棒了，运行成功了！在执行过程中，你应该看到智能体首先调用了 Gemini，它会输出一个结构化调用来调用 MCP 服务器，随后 MCP 服务器的响应被传回给 Gemini，最终由 Gemini 生成最终响应。

完成后别忘了删除你的 Google Cloud 资源。你可以使用以下命令来删除这些资源：

```bash
gcloud run services delete n8n --region=$REGION 

gcloud sql instances delete n8n-db 

gcloud secrets delete n8n-db-password 

gcloud secrets delete n8n-encryption-key 

gcloud iam service-accounts delete $SERVICE_ACCOUNT_EMAIL 

gcloud projects delete $PROJECT_ID
```

恭喜！您已成功将 n8n 部署至 Google Cloud Run，并利用 Gemini 2.5 创建了首个 AI 智能体。现在可以探索更高级的功能，添加更多工具并构建复杂工作流来实现流程自动化。