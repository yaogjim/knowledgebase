---
title: "2025-12-18_copilotkit_ai_A2UI_正式发布_CopilotKit_已与_Google_合作_在_CopilotKit_和_A"
source: "https://www.copilotkit.ai/blog/build-with-googles-new-a2ui-spec-agent-user-interfaces-with-a2ui-ag-ui"
author:
  - "[[@click]]"
published: 2025-12-18
created: 2025-12-18
description:
tags:
  - "#00BFFF"
  - "#FF0000"
  - "copilotkit"
  - "@click"
---

# A2UI 正式发布：CopilotKit 已与 Google 合作，在 CopilotKit 和 A

A2UI 正式发布：CopilotKit 已与 Google 合作，在 CopilotKit 和 AG-UI 两个平台推出时均提供全面支持！ CopilotKit delivers full support at launch!

[Learn More](./ag-ui-and-a2ui)

[Back](/blog)

作者：邦妮和内森·塔伯特 December 17, 2025

## TL;DR

在本指南中，你将学习如何使用代理-代理（A2A）协议、AG-UI 协议和 CopilotKit，构建全栈代理-用户界面（A2UI）代理。

在深入讨论之前，我还想探讨一下 A2UI 和 AG-UI 的协同工作方式。你可以在此处了解更多信息。

本次构建中，我们将介绍：

- What is A2UI?
- 搭建 A2UI + A2A 代理后端
- 使用 AG-UI 和 CopilotKit 构建 A2UI + A2A 代理前端

这是我们即将构建内容的预览：

## What is A2UI?

A2UI 是一个新的开源 UI 工具包，旨在简化 LLM 生成的用户界面（UI）。它允许 AI 代理实时创建并展示动态、交互式用户界面（UI），而非依赖固定的、预先构建的界面。

A2UI 基于 A2A 协议构建，允许 A2A 代理发送交互式组件而非仅文本，采用一种高级的框架无关格式，这种格式可在任何界面上原生渲染

简单来说，AI 代理不再仅在聊天窗口中以文本形式回应，而是可以通过生成一个完整的 UI 组件来回应，例如：

- 一个交互式的图表或图形。
- 一个填写完整的表单或表格
- 特定的按钮（如“批准”或“拒绝”）仅适用于当前任务。

你可以在这里了解更多关于 A2UI 的信息。

![Image from Notion](https://cdn.prod.website-files.com/669a24c14f4dcb77f6f97034/6940a37b3db2d94d25437273_https%253A%252F%252Fdev-to-uploads.s3.amazonaws.com%252Fuploads%252Farticles%252Ffyoqxx7cbmfu17kyllug.webp)

Image from Notion

既然你已经了解了 A2UI 协议，让我们看看如何将它与 A2A、AG-UI 和 CopilotKit 结合使用，以构建全栈 A2UI AI 代理。

## Prerequisites

你需要对 React 或 Next.js 有基本的了解，才能完全理解本教程

我们还将使用以下内容：

- Python - 一种流行的编程语言，用于借助 AI 代理框架构建 AI 代理；请确保你的电脑已安装该语言。
- AG-UI 协议（代理用户交互协议）是由 CopilotKit 开发的一种开源、轻量级、基于事件的协议，该协议能够促进前端与您的 AI 代理后端之间丰富的实时交互。
- Google ADK - 谷歌设计的开源框架，用于简化构建复杂且可投入生产的 AI 代理的流程。
- Gemini API 密钥 - 可使您使用 Gemini 模型为 ADK 代理执行各种任务的 API 密钥。
- CopilotKit - 一个开源协作者框架，用于构建自定义 AI 聊天机器人、应用内 AI 协作者及文本区域。

## 搭建 A2UI + A2A 代理后端

在本节中，你将学习如何通过 A2A 协议在后端配置你的代理来使用 A2UI。

我们开始吧。

要开始，请使用以下命令克隆 A2A 入门模板：

```
git clone https://github.com/copilotkit/with-a2a-a2ui.git
```

之后，请创建一个包含你的 API 密钥的环境文件：

```
echo "GEMINI_API_KEY=your_api_key_here" > .env
```

接下来执行以下命令以安装依赖项：

```
pnpm install
```

最后，请使用以下命令运行并连接你的代理：

```
pnpm run dev
```

现在我们来看看如何通过 A2A 协议配置你的代理以使用 A2UI。

### 步骤 1: 定义你的智能代理的 A2UI 响应组件

要定义您的代理的 A2UI 响应组件，首先需要定义一个包含完整 JSON Schema 的模式，该模式用于定义有效的 A2UI 消息，如 `agent/restaurant_finder/prompt_builder.py` 文件所示。

```
A2UI_SCHEMA = r'''
{
"title": "A2UI Message Schema",
"description": "Describes a JSON payload for an A2UI (Agent to UI) message, which is used to construct and update user interfaces dynamically. A message MUST contain exactly ONE of the action properties: 'beginRendering', 'surfaceUpdate', 'dataModelUpdate', or 'deleteSurface'.",
"type": "object",
"properties": {
"beginRendering": {
"type": "object",
"description": "Signals the client to begin rendering a surface with a root component and specific styles.",
"properties": {
"surfaceId": {
"type": "string",
"description": "The unique identifier for the UI surface to be rendered."
},
"root": {
"type": "string",
"description": "The ID of the root component to render."
},
"styles": {
"type": "object",
"description": "Styling information for the UI.",
"properties": {
"font": {
"type": "string",
"description": "The primary font for the UI."
},
"primaryColor": {
"type": "string",
"description": "The primary UI color as a hexadecimal code (e.g., '#00BFFF').",
"pattern": "^#[0-9a-fA-F]{6}$"
}
}
}
},
"required": ["root", "surfaceId"]
},
// ...
}
```

然后定义你的代理用于格式化其响应的 A2UI 响应组件，如 `agent/restaurant_finder/prompt_builder.py` 文件所示。

```
RESTAURANT_UI_EXAMPLES = """
---BEGIN SINGLE_COLUMN_LIST_EXAMPLE---
[
{{ "beginRendering": {{ "surfaceId": "default", "root": "root-column", "styles": {{ "primaryColor": "#FF0000", "font": "Roboto" }} }} }},
{{ "surfaceUpdate": {{
"surfaceId": "default",
"components": [
{{ "id": "root-column", "component": {{ "Column": {{ "children": {{ "explicitList": ["title-heading", "item-list"] }} }} }} }},
{{ "id": "title-heading", "component": {{ "Text": {{ "usageHint": "h1", "text": {{ "literalString": "Top Restaurants" }} }} }} }},
{{ "id": "item-list", "component": {{ "List": {{ "direction": "vertical", "children": {{ "template": {{ "componentId": "item-card-template", "dataBinding": "/items" }} }} }} }} }},
{{ "id": "item-card-template", "component": {{ "Card": {{ "child": "card-layout" }} }} }},
{{ "id": "card-layout", "component": {{ "Row": {{ "children": {{ "explicitList": ["template-image", "card-details"] }} }} }} }},
{{ "id": "template-image", weight: 1, "component": {{ "Image": {{ "url": {{ "path": "imageUrl" }} }} }} }},
{{ "id": "card-details", weight: 2, "component": {{ "Column": {{ "children": {{ "explicitList": ["template-name", "template-rating", "template-detail", "template-link", "template-book-button"] }} }} }} }},
{{ "id": "template-name", "component": {{ "Text": {{ "usageHint": "h3", "text": {{ "path": "name" }} }} }} }},
{{ "id": "template-rating", "component": {{ "Text": {{ "text": {{ "path": "rating" }} }} }} }},
{{ "id": "template-detail", "component": {{ "Text": {{ "text": {{ "path": "detail" }} }} }} }},
{{ "id": "template-link", "component": {{ "Text": {{ "text": {{ "path": "infoLink" }} }} }} }},
{{ "id": "template-book-button", "component": {{ "Button": {{ "child": "book-now-text", "primary": true, "action": {{ "name": "book_restaurant", "context": [ {{ "key": "restaurantName", "value": {{ "path": "name" }} }}, {{ "key": "imageUrl", "value": {{ "path": "imageUrl" }} }}, {{ "key": "address", "value": {{ "path": "address" }} }} ] }} }} }} }},
{{ "id": "book-now-text", "component": {{ "Text": {{ "text": {{ "literalString": "Book Now" }} }} }} }}
]
}} }},
{{ "dataModelUpdate": {{
"surfaceId": "default",
"path": "/",
"contents": [
{{ "key": "items", "valueMap": [
{{ "key": "item1", "valueMap": [
{{ "key": "name", "valueString": "The Fancy Place" }},
{{ "key": "rating", "valueNumber": 4.8 }},
{{ "key": "detail", "valueString": "Fine dining experience" }},
{{ "key": "infoLink", "valueString": "https://example.com/fancy" }},
{{ "key": "imageUrl", "valueString": "https://example.com/fancy.jpg" }},
{{ "key": "address", "valueString": "123 Main St" }}
] }},
{{ "key": "item2", "valueMap": [
{{ "key": "name", "valueString": "Quick Bites" }},
{{ "key": "rating", "valueNumber": 4.2 }},
{{ "key": "detail", "valueString": "Casual and fast" }},
{{ "key": "infoLink", "valueString": "https://example.com/quick" }},
{{ "key": "imageUrl", "valueString": "https://example.com/quick.jpg" }},
{{ "key": "address", "valueString": "456 Oak Ave" }}
] }}
] }} // Populate this with restaurant data
]
}} }}
]
---END SINGLE_COLUMN_LIST_EXAMPLE---
// ...
```

之后，定义一个函数，用于构建包含指令、A2UI 响应组件和 A2UI 消息 JSON Schema 的完整提示词，如 `agent/restaurant_finder/prompt_builder.py` 文件所示。

```
def get_ui_prompt(base_url: str, examples: str) -> str:
"""
Constructs the full prompt with UI instructions, rules, examples, and schema.
Args:
 base_url: The base URL for resolving static assets like logos.
 examples: A string containing the specific UI examples for the agent's task.

Returns:
 A formatted string to be used as the system prompt for the LLM.
"""
# The f-string substitution for base_url happens here, at runtime.
formatted_examples = examples.format(base_url=base_url)

return f"""
You are a helpful restaurant finding assistant. Your final output MUST be a A2UI UI JSON response.

To generate the response, you MUST follow these rules:
1.  Your response MUST be in two parts, separated by the delimiter: `---a2ui_JSON---`.
2.  The first part is your conversational text response.
3.  The second part is a single, raw JSON object that is a list of A2UI messages.
4.  The JSON part MUST validate against the A2UI JSON SCHEMA provided below.

--- UI TEMPLATE RULES ---
- If the query is for a list of restaurants, use the restaurant data you have already received from the `get_restaurants` tool to populate the `dataModelUpdate.contents` array (e.g., as a `valueMap` for the "items" key).
- If the number of restaurants is 5 or fewer, you MUST use the `SINGLE_COLUMN_LIST_EXAMPLE` template.
- If the number of restaurants is more than 5, you MUST use the `TWO_COLUMN_LIST_EXAMPLE` template.
- If the query is to book a restaurant (e.g., "USER_WANTS_TO_BOOK..."), you MUST use the `BOOKING_FORM_EXAMPLE` template.
- If the query is a booking submission (e.g., "User submitted a booking..."), you MUST use the `CONFIRMATION_EXAMPLE` template.

{formatted_examples}

---BEGIN A2UI JSON SCHEMA---
{A2UI_SCHEMA}
---END A2UI JSON SCHEMA---
"""
```

### 步骤 2：使用 A2UI Composer 来生成 A2UI 组件

如果你想轻松生成组件，不妨使用 A2UI Composer，它能帮你生成 A2UI 组件。

要使用 A2UI 编辑器创建组件，请访问 https://a2ui-editor.ag-ui.com/并描述您的 A2UI 小部件，如下所示。

![Image from Notion](https://cdn.prod.website-files.com/669a24c14f4dcb77f6f97034/6940a463e5c7947d7f9d5fe0_https%253A%252F%252Fdev-to-uploads.s3.amazonaws.com%252Fuploads%252Farticles%252F5qmvq9x6s0nwpu5u5zo4.webp)

Image from Notion

然后点击创建按钮，composer 将生成你的 A2UI 小部件，如下所示。

![Image from Notion](https://cdn.prod.website-files.com/669a24c14f4dcb77f6f97034/6940a463e5c7947d7f9d5fe3_https%253A%252F%252Fdev-to-uploads.s3.amazonaws.com%252Fuploads%252Farticles%252F6ntour3x6k164bvsofg1.webp)

Image from Notion

之后，请复制生成的 JSON 规范，并粘贴到你的代理提示词中，正如我们在步骤一中讨论的那样。

### 步骤 3：配置你的 A2UI 代理

一旦你完成 A2A 组件的设置并构建了代理提示词，就请按照 `agent/restaurant_finder/agent.py` 文件所示配置你的代理。

```
// ...
Local imports from sibling modules
from prompt_builder import (
A2UI_SCHEMA,  # JSON Schema for A2UI validation
RESTAURANT_UI_EXAMPLES,  # Example A2UI responses for few-shot learning
get_text_prompt,  # Prompt for text-only mode
get_ui_prompt,  # Prompt for UI mode (with schema and examples)
)
from tools import get_restaurants  # Tool function for fetching restaurant data
logger = logging.getLogger(name)
AGENT_INSTRUCTION = """
You are a helpful restaurant finding assistant. Your goal is....
"""
class RestaurantAgent:
"""
An agent that finds restaurants based on user criteria.
"""

# Supported content types for A2A protocol
SUPPORTED_CONTENT_TYPES = ["text", "text/plain"]

def __init__(self, base_url: str, use_ui: bool = False):
 """
 Initialize the RestaurantAgent.

 Args:
 base_url: The server's base URL (used for resolving image URLs)
 use_ui: If True, generate A2UI JSON responses; if False, generate text
 """
 self.base_url = base_url
 self.use_ui = use_ui

 # Build the underlying LlmAgent with appropriate instructions
 self._agent = self._build_agent(use_ui)

 # User ID for session management (constant for this simple example)
 self._user_id = "remote_agent"

 // ...

 # =====================================================================
 # LOAD AND WRAP A2UI SCHEMA
 # =====================================================================
 # We need to validate LLM responses against the A2UI schema.
 # The schema defines a SINGLE message, but the LLM returns a LIST of messages.
 # So we wrap the schema in an array validator.
 try:
 # Parse the schema for a single A2UI message
 single_message_schema = json.loads(A2UI_SCHEMA)

 # Wrap it: the LLM must return an ARRAY of valid messages
 self.a2ui_schema_object = {"type": "array", "items": single_message_schema}
 logger.info(
 "A2UI_SCHEMA successfully loaded and wrapped in an array validator."
 )
 except json.JSONDecodeError as e:
 logger.error(f"CRITICAL: Failed to parse A2UI_SCHEMA: {e}")
 self.a2ui_schema_object = None  # Validation will be skipped

// ...
# =========================================================================
# STEP 3c: BUILD THE LLM AGENT
# =========================================================================
def _build_agent(self, use_ui: bool) -> LlmAgent:
 """
 Builds the LLM agent with appropriate instructions and tools.

 Args:
 use_ui: Whether to include UI instructions and schema in the prompt

 Returns:
 A configured LlmAgent instance
 """
 # Get the model name from the environment variable, with a sensible default
 LITELLM_MODEL = os.getenv("LITELLM_MODEL", "gemini/gemini-2.5-flash")

 if use_ui:
 # UI mode: Include instructions for generating A2UI JSON
 # This adds:
 # - Detailed formatting rules (delimiter, JSON structure)
 # - Template examples for different scenarios
 # - The complete A2UI JSON schema
 instruction = AGENT_INSTRUCTION + get_ui_prompt(
 self.base_url, RESTAURANT_UI_EXAMPLES
 )
 else:
 # Text mode: Simple instructions for text-only responses
 instruction = get_text_prompt()

 # Create the LlmAgent with:
 # - A LiteLLM wrapper (allows using different LLM providers)
 # - Name and description for identification
 # - The instruction (system prompt)
 # - Available tools (get_restaurants function)
 return LlmAgent(
 model=LiteLlm(model=LITELLM_MODEL),
 name="restaurant_agent",
 description="An agent that finds restaurants and helps book tables.",
 instruction=instruction,
 tools=[get_restaurants],  # The agent can call this function
 )

  // ...
```

### 步骤 4: 使用 A2A 协议配置你的 A2UI 代理执行器

在配置好你的 A2UI 代理后，需使用一个 A2A 代理执行器来配置该代理，该执行器将处理 A2A 请求和响应，具体操作请参照 `agent/restaurant_finder/agent_executer.py` 文件。

```
// ...
=============================================================================
STEP 2: AGENT EXECUTOR CLASS
=============================================================================
class RestaurantAgentExecutor(AgentExecutor):
"""
Restaurant AgentExecutor - Bridges A2A Protocol and RestaurantAgent.
"""

# =========================================================================
# STEP 2a: INITIALIZATION
# =========================================================================
def __init__(self, base_url: str):
 """
 Initialize the executor with two agent instances.

 """
 # UI agent: Generates rich A2UI responses with components and data models
 self.ui_agent = RestaurantAgent(base_url=base_url, use_ui=True)

 # Text agent: Generates plain text responses (for clients without A2UI support)
 self.text_agent = RestaurantAgent(base_url=base_url, use_ui=False)

# =========================================================================
# STEP 2b: MAIN EXECUTION METHOD
# =========================================================================
async def execute(
 self,
 context: RequestContext,
 event_queue: EventQueue,
) -> None:
 """
 Main entry point for handling A2A requests.

 This method orchestrates the entire request-response cycle:
 1. Detects whether the client supports A2UI
 2. Parses incoming message parts (text or UI events)
 3. Transforms UI events into natural language queries
 4. Invokes the appropriate agent
 5. Formats and sends the response

 Args:
 context: Contains the incoming message, task state, and client info
 event_queue: Queue for sending events (status updates, responses) to client
 """
 # Initialize variables for tracking the query and UI events
 query = ""  # The final query string to send to the LLM
 ui_event_part = None  # Will hold A2UI event data if present
 action = None  # The action name from UI events (e.g., "book_restaurant")

 # =====================================================================
 # STEP 2b-i: DETECT A2UI SUPPORT
 # =====================================================================
 # Check which protocol extensions the client requested
 logger.info(
 f"--- Client requested extensions: {context.requested_extensions} ---"
 )

 # try_activate_a2ui_extension checks if A2UI is in the requested extensions
 # and marks it as active in the context if so
 use_ui = try_activate_a2ui_extension(context)

 # =====================================================================
 # STEP 2b-ii: SELECT APPROPRIATE AGENT
 # =====================================================================
 # Based on A2UI support, choose which agent to use
 if use_ui:
 agent = self.ui_agent
 logger.info(
 "--- AGENT_EXECUTOR: A2UI extension is active. Using UI agent. ---"
 )
 else:
 agent = self.text_agent
 logger.info(
 "--- AGENT_EXECUTOR: A2UI extension is not active. Using text agent. ---"
 )

 # =====================================================================
 # STEP 2b-iii: PARSE INCOMING MESSAGE PARTS
 # =====================================================================
 # A2A messages can contain multiple "parts" - these can be:
 # - TextPart: Plain text from the user
 # - DataPart: Structured data (like A2UI events from button clicks)
 if context.message and context.message.parts:
 logger.info(
 f"--- AGENT_EXECUTOR: Processing {len(context.message.parts)} message parts ---"
 )

 # Iterate through all parts to find relevant data
 for i, part in enumerate(context.message.parts):
 if isinstance(part.root, DataPart):
 # DataPart contains structured JSON data
 if "userAction" in part.root.data:
 # This is an A2UI ClientEvent - a button was clicked!
 logger.info(f"  Part {i}: Found a2ui UI ClientEvent payload.")
 ui_event_part = part.root.data["userAction"]
 else:
 # Some other structured data
 logger.info(f"  Part {i}: DataPart (data: {part.root.data})")
 elif isinstance(part.root, TextPart):
 # Plain text from the user
 logger.info(f"  Part {i}: TextPart (text: {part.root.text})")
 else:
 logger.info(f"  Part {i}: Unknown part type ({type(part.root)})")

 # =====================================================================
 # STEP 2b-iv: TRANSFORM UI EVENTS INTO LLM QUERIES
 # =====================================================================
 # If we received a UI event (button click), we need to transform it
 # into a natural language query that the LLM can understand.
 # This is a key part of the A2UI pattern - UI events become LLM inputs.
 if ui_event_part:
 logger.info(f"Received a2ui ClientEvent: {ui_event_part}")

 # Extract the action name and context data from the event
 action = ui_event_part.get("actionName")
 ctx = ui_event_part.get("context", {})

 # Handle "Book Now" button click
 if action == "book_restaurant":
 # User clicked "Book Now" on a restaurant card
 # Extract restaurant details from the button's context
 restaurant_name = ctx.get("restaurantName", "Unknown Restaurant")
 address = ctx.get("address", "Address not provided")
 image_url = ctx.get("imageUrl", "")

 # Create a structured query that tells the LLM what the user wants
 # The LLM is trained to recognize this pattern and show a booking form
 query = f"USER_WANTS_TO_BOOK: {restaurant_name}, Address: {address}, ImageURL: {image_url}"

 # Handle "Submit Reservation" button click
 elif action == "submit_booking":
 # User filled out the booking form and submitted it
 # Extract all the form data from the button's context
 restaurant_name = ctx.get("restaurantName", "Unknown Restaurant")
 party_size = ctx.get("partySize", "Unknown Size")
 reservation_time = ctx.get("reservationTime", "Unknown Time")
 dietary_reqs = ctx.get("dietary", "None")
 image_url = ctx.get("imageUrl", "")

 # Create a query that tells the LLM to confirm the booking
 query = f"User submitted a booking for {restaurant_name} for {party_size} people at {reservation_time} with dietary requirements: {dietary_reqs}. The image URL is {image_url}"

 else:
 # Unknown action - pass it through as-is
 query = f"User submitted an event: {action} with data: {ctx}"
 else:
 # No UI event - this is a regular text message
 logger.info("No a2ui UI event part found. Falling back to text input.")
 query = context.get_user_input()  # Extract text from the message parts

 logger.info(f"--- AGENT_EXECUTOR: Final query for LLM: '{query}' ---")

 // ...

# =========================================================================
# STEP 2c: CANCEL METHOD (NOT IMPLEMENTED)
# =========================================================================
async def cancel(
 self, request: RequestContext, event_queue: EventQueue
) -> Task | None:
 """
 Handle task cancellation requests.

 This agent does not support cancellation, so we raise an error.
 A more sophisticated agent might gracefully stop ongoing work.

 Raises:
 ServerError: With UnsupportedOperationError
 """
 raise ServerError(error=UnsupportedOperationError())
```

### 步骤 5：通过 A2A 协议配置您的 A2UI 代理服务器

在配置好代理执行器后，请为你的代理设置一个主入口，该主入口将设置并启动一个符合 A2A 标准的服务器，该服务器可以：

- 处理代理发现请求（通过 AgentCard）
- 处理用户关于餐厅的问题
- 提供静态资源（餐厅图片）
- 同时支持仅文本和 A2UI（富 UI）两种响应

您可以如 `agent/restaurant_finder/__main__.py` 文件所示配置服务器。

```
// ...
@click.command()  # Decorates this function as a CLI command
@click.option("--host", default="localhost")  # Optional --host argument
@click.option("--port", default=10002)  # Optional --port argument
def main(host, port):
"""
Main entry point for the Restaurant Finder Agent server.
"""
try:
 # =====================================================================
 # VALIDATE API CREDENTIALS
 # =====================================================================
 # The agent needs either:
 # - GEMINI_API_KEY for direct Gemini API access, OR
 # - GOOGLE_GENAI_USE_VERTEXAI=TRUE for Vertex AI authentication
 if not os.getenv("GOOGLE_GENAI_USE_VERTEXAI") == "TRUE":
 if not os.getenv("GEMINI_API_KEY"):
 raise MissingAPIKeyError(
 "GEMINI_API_KEY environment variable not set and GOOGLE_GENAI_USE_VERTEXAI is not TRUE."
 )

 # =====================================================================
 # DEFINE AGENT CAPABILITIES
 # =====================================================================
 # AgentCapabilities tells clients what this agent supports:
 # - streaming=True: Agent can stream responses progressively
 # - extensions: List of protocol extensions (here, A2UI for rich UIs)
 capabilities = AgentCapabilities(
 streaming=True,
 extensions=[get_a2ui_agent_extension()],  # Enable A2UI rich UI support
 )

 # =====================================================================
 # DEFINE AGENT SKILLS
 # =====================================================================
 # AgentSkill describes what this agent can do. This metadata is used
 # for agent discovery and helps clients understand the agent's purpose.
 skill = AgentSkill(
 id="find_restaurants",  # Unique identifier for this skill
 name="Find Restaurants Tool",  # Human-readable name
 description="Helps find restaurants based on user criteria (e.g., cuisine, location).",
 tags=["restaurant", "finder"],  # Searchable tags
 examples=["Find me the top 10 chinese restaurants in the US"],  # Example queries
 )

 # =====================================================================
 # CONSTRUCT BASE URL
 # =====================================================================
 # The base URL is used for:
 # - Agent discovery (clients connect to this URL)
 # - Resolving static asset URLs (e.g., restaurant images)
 base_url = f"http://{host}:{port}"

 # =====================================================================
 # CREATE AGENT CARD
 # =====================================================================
 # The AgentCard is the "identity card" for this agent in the A2A protocol.
 # Clients use this to discover and understand the agent.
 agent_card = AgentCard(
 name="Restaurant Agent",  # Display name
 description="This agent helps find restaurants based on user criteria.",
 url=base_url,  # Where to reach this agent
 version="1.0.0",  # Semantic version
 default_input_modes=RestaurantAgent.SUPPORTED_CONTENT_TYPES,  # ["text", "text/plain"]
 default_output_modes=RestaurantAgent.SUPPORTED_CONTENT_TYPES,
 capabilities=capabilities,  # What the agent supports
 skills=[skill],  # What the agent can do
 )

 # =====================================================================
 # CREATE AGENT EXECUTOR
 # =====================================================================
 # The AgentExecutor is the bridge between the A2A protocol and our
 # RestaurantAgent. It handles:
 # - Parsing A2A requests
 # - Invoking the appropriate agent (UI or text)
 # - Formatting A2A responses
 agent_executor = RestaurantAgentExecutor(base_url=base_url)

 # =====================================================================
 # CREATE REQUEST HANDLER
 # =====================================================================
 # DefaultRequestHandler processes incoming A2A requests and delegates
 # to our agent_executor. The InMemoryTaskStore keeps track of ongoing
 # tasks (useful for multi-turn conversations).
 request_handler = DefaultRequestHandler(
 agent_executor=agent_executor,
 task_store=InMemoryTaskStore(),
 )

 # =====================================================================
 # BUILD THE A2A APPLICATION
 # =====================================================================
 # A2AStarletteApplication creates an ASGI web application that:
 # - Exposes the /.well-known/agent.json endpoint (agent discovery)
 # - Handles A2A protocol messages
 server = A2AStarletteApplication(
 agent_card=agent_card, http_handler=request_handler
 )
 import uvicorn

 # Build the Starlette app from our A2A configuration
 app = server.build()

 // ...

 # =====================================================================
 # MOUNT STATIC FILES
 # =====================================================================
 # Serve restaurant images from the ./images directory at /static
 # Example: http://localhost:10002/static/restaurant1.jpg
 app.mount("/static", StaticFiles(directory="images"), name="static")

 # =====================================================================
 # START THE SERVER
 # =====================================================================
 # uvicorn is an ASGI server that will run our application.
 # It handles HTTP connections and routes them to our app.
 uvicorn.run(app, host=host, port=port)

  // ...
```

恭喜！你已经成功搭建了 A2UI 后端，并使用 A2A 协议。让我们看看如何使用 AG-UI 和 CopilotKit 为其添加前端。

## 使用 AG-UI 和 CopilotKit 构建 A2UI + A2A 代理前端

在本节中，您将学习如何使用 AG-UI 协议配置前端与您的 A2UI + A2A 代理。该协议负责与您的 A2UI + A2A 代理进行通信，并将 A2UI 消息以 `ActivityMessage` 对象的形式来回传递。

让我们开始吧。

### 步骤 1：使用 AG-UI 和 A2A 客户端来配置 CopilotKit API 路由

为了将您的 A2UI + A2A 代理连接到前端，请配置一个 CopilotKit API 路由处理器，该处理器可通过 AG-UI 和 A2A 客户端将前端连接到您的 A2UI + A2A 代理后端，如下所示。

```
// CopilotKit Runtime - Core server-side components
import {
CopilotRuntime, // Main runtime that orchestrates agents and handles requests
createCopilotEndpoint,  // Factory function to create an HTTP endpoint
InMemoryAgentRunner, // Runs agents with in-memory state (no persistence)
} from "@copilotkitnext/runtime";
// Hono adapter for Vercel/Next.js - Converts Hono app to Next.js route handlers
import { handle } from "hono/vercel";
// A2A (Agent-to-Agent) Integration
import { A2AAgent } from "@ag-ui/a2a"; // CopilotKit wrapper for A2A protocol
import { A2AClient } from "@a2a-js/sdk/client"; // Client to communicate with A2A servers
// =============================================================================
// STEP 2: CREATE A2A, CLIENT
// =============================================================================
/**

A2AClient connects to an A2A-compliant agent server.
*/
const a2aClient = new A2AClient("http://localhost:10002");

// =============================================================================
// STEP 3: CREATE A2A AGENT WRAPPER
// =============================================================================
/**

A2AAgent wraps the A2AClient to make it compatible with CopilotKit.
*/
const agent = new A2AAgent({ a2aClient, debug: true });

// =============================================================================
// STEP 4: CREATE COPILOTKIT RUNTIME
// =============================================================================
/**

CopilotRuntime is the central orchestrator that:

Manages registered agents

Routes requests to the appropriate agent

Handles streaming responses

Manages conversation state
*/
const runtime = new CopilotRuntime({
agents: {
default: agent, // Our A2A Restaurant Agent is the default agent
},
runner: new InMemoryAgentRunner(),
});

// =============================================================================
// STEP 5: CREATE THE HTTP ENDPOINT
// =============================================================================
/**

createCopilotEndpoint creates a Hono web application that handles
CopilotKit API requests.

The endpoint handles:

POST /api/copilotkit - Main chat endpoint for sending messages

GET /api/copilotkit - Health check and capability discovery

Various sub-routes for streaming, actions, etc.
*/
const app = createCopilotEndpoint({
runtime,
basePath: "/api/copilotkit",
});

export const GET = handle(app as any);
export const POST = handle(app as any);
```

### 步骤 2：创建 A2UI 消息渲染器

配置好 API 路由后，创建由 CopilotKit 提供的 A2UI 消息渲染器，用于渲染 A2UI 消息并使用主题进行实例化，如下所示。

```
"use client";
// A2UI Renderer Factory - Creates a message renderer for A2UI protocol responses
import { createA2UIMessageRenderer } from "@copilotkitnext/a2ui-renderer";
// Custom theme configuration for styling A2UI components
import { theme } from "./theme";
// =============================================================================
// CREATE A2UI MESSAGE RENDERER
// =============================================================================
/**

A2UIMessageRenderer is a custom message renderer that knows how to
display A2UI protocol messages as rich, interactive UI components.

When the A2A agent sends back A2UI JSON (with beginRendering, surfaceUpdate,
dataModelUpdate messages), this renderer:

Parses the A2UI JSON

Builds a component tree from the surfaceUpdate

Binds data from dataModelUpdate to components

Renders native React components (cards, buttons, forms, etc.)

Handles user interactions and sends events back to the agent

The theme option allows customizing colors, fonts, and spacing of
The rendered A2UI components to match your app's design.
*/
const A2UIMessageRenderer = createA2UIMessageRenderer({ theme });

// ....
```

### 步骤 3：配置 CopilotKit 提供方和聊天组件

创建好 A2UI 消息渲染器后，请配置 CopilotKit 提供者及聊天组件。

然后将 A2UI 消息渲染器传递给 CopilotKit 提供方，如下所示。

```
"use client";
import { CopilotChat, CopilotKitProvider } from "@copilotkitnext/react";
// ...
export default function Home() {
return (
<CopilotKitProvider
runtimeUrl="/api/copilotkit"
showDevConsole="auto"
renderActivityMessages={[A2UIMessageRenderer]}
>
<main
className="flex min-h-screen flex-1 flex-col overflow-hidden"
style={{ minHeight: "100dvh" }}
>
<Chat />
</main>
</CopilotKitProvider>
);
}
function Chat() {
return (
<div className="flex flex-1 flex-col overflow-hidden">
<CopilotChat style={{ flex: 1, minHeight: "100%" }} />
</div>
);
}
```

### 步骤 4：启动你的 A2UI + A2A + AG-UI 代理

配置好 CopilotKit 服务提供方并与聊天组件一同设置后，运行你的代理后端服务器和前端服务器。然后访问前端的本地主机地址，你应该能看到 A2UI 代理与聊天组件一起运行，如下所示。

![Image from Notion](https://cdn.prod.website-files.com/669a24c14f4dcb77f6f97034/6940a58b164d5d13c5f2b46f_https%253A%252F%252Fdev-to-uploads.s3.amazonaws.com%252Fuploads%252Farticles%252Fsqt8xuxjcvx1qqgxumdx.webp)

Image from Notion

之后，让代理帮你找纽约的中餐馆。然后你会看到 A2UI 组件和消息渲染出纽约的热门餐厅（这些餐厅可供预订），如图所示。

## Conclusion

在本指南中，我们已逐步讲解了使用 A2A + AG-UI 协议和 CopilotKit 构建全栈 A2UI 代理的步骤。

虽然我们探索了一些功能，但 CopilotKit 的无数应用场景我们才刚刚触及皮毛，这些场景从构建交互式 AI 聊天机器人到智能代理解决方案不等——本质上，CopilotKit 能让你在几分钟内为产品添加大量实用的 AI 功能。

希望这个指南能帮助你更轻松地将 AI 驱动的 Copilot 集成到现有应用中

在 Twitter 上关注 CopilotKit 并打个招呼。如果你想构建一些很酷的东西，不妨加入 Discord 社区。

## Top posts

[See All](/blog)

[![Oracle adopts AG-UI protocol for Agent Spec](/_next/image?url=https%3A%2F%2Fcdn.prod.website-files.com%2F669a24c14f4dcb77f6f97034%2F6942b45cb197ba2dfb5a4c58_Oracle%2520Agent%2520Spec%2520Meets%2520AG-UI_%2520From%2520Portable%2520Agents%2520to%2520Real%2520User%2520Experiences%2520(1).png&w=750&q=75)](/blog/oracle-adopts-ag-ui-protocol-for-agent-spec)

[内森·塔伯特和伊莱·伯曼 December 18, 2025](/blog/oracle-adopts-ag-ui-protocol-for-agent-spec)

[Oracle 采用 AG-UI 协议以支持代理规范 当今智能代理系统中最复杂的问题之一，并非定义智能代理，而是将这些代理与真实、可靠的用户体验相连接。Oracle 的开放代理规范（Agent Spec）与 AG-UI 如今共同协作，来解决这一差距。](/blog/oracle-adopts-ag-ui-protocol-for-agent-spec)

[![CopilotKit v1.50 Release Announcement: What's New for Agentic Builders](/_next/image?url=https%3A%2F%2Fcdn.prod.website-files.com%2F669a24c14f4dcb77f6f97034%2F693892fc0c438d4671b41f6c_Introducing%2520CopilotKit%2520%2520v1.50!%2520(1).png&w=750&q=75)

Nathan Tarbert December 11, 2025

CopilotKit v1.50 版本发布公告：智能代理开发者的新特性 CopilotKit 已为此架构升级开展了数月工作。该版本命名为 v1.50，是 CopilotKit 1.x 系列中最重要的一步，主要解决开发者在构建代理功能时遇到的核心问题：线程持久化、可靠重连、多代理协作、共享状态、类型安全以及更简化的基础设施。接下来，我们将介绍其开箱即用的全部功能，并阐释这些改进的重要性，最后展示从今日起可借助新 API 实现的能力。

](/blog/copilotkit-v1-50-release-announcement-whats-new-for-agentic-ui-builders)[![AWS Strands Agents Now Compatible with AG-UI](/_next/image?url=https%3A%2F%2Fcdn.prod.website-files.com%2F669a24c14f4dcb77f6f97034%2F692ddf6b3a59eb98e1d34ad9_Introducing%25E2%2580%25A8AWS%2520Strands%2520Agents.png&w=750&q=75)

Nathan Tarbert December 3, 2025

AWS Strands 代理现在已与 AG-UI 兼容 智能体领域近期发展迅猛，而今天的更新尤为亮眼：AWS Strands 现已开始与 AG-UI 和 CopilotKit 集成。

](/blog/aws-strands-agents-now-compatible-with-ag-ui)