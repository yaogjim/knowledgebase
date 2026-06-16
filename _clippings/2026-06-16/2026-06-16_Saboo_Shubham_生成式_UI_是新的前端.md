---
title: "2026-06-16_Saboo_Shubham_生成式_UI_是新的前端"
source: "https://x.com/Saboo_Shubham_/status/2062220865643982875"
author:
  - "[[@Saboo_Shubham_]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "x"
  - "@Saboo_Shubham_"
  - "agent"
  - "https"
---

# 生成式 UI 是新的前端

**Shubham Saboo**

# 生成式 UI 是新的前端

前端曾经是固定不变的。设计师绘制它，工程师构建它，用户得到最终交付的产品。

就这样结束了。

2026年推出的界面部分由代理自身实时生成，依据用户实际的请求内容。请求一个表格，就得到一个表格。不是一段描述它的文字。

生成式 UI 是让代理停止描述并开始展示的那一层。构建它的三种模式已经出现，而它们之间的差异比大多数团队意识到的更为重要。

但构建这个没有唯一的方法。有三种。而大多数团队会选择其中一种，却没意识到自己选了哪一种。

## 协议栈

三个协议。每个完成一项工作。

MCP 将客服人员与工具连接起来。A2A 将客服人员彼此连接起来。AG \-UI 将客服人员与用户连接起来。

AG-UI is the streaming layer that carries everything you'll see below: tool calls, A2UI schemas, MCP App events, state deltas. Runs over SSE. State flows both ways on the same stream. User edits, agent sees. Agent mutates, user sees.

A2UI is Google's spec for agents emitting UI as schema. It rides on AG-UI. CopilotKit ships it in production.

你不需要为这些内容编写解析器。CopilotKit 是一个 AG-UI 客户端，会为你解码流。

## 大多数团队最容易混淆的三种模式

询问十位开发者什么是生成式 UI，你会得到十个答案。其中大多数人描述的是他们当前使用的框架所提供的任何一种模式。

只有三个。这个范围从更多控制到更大灵活性。

- Controlled: You pre-build the components. The agent picks which to render.
- Declarative: The agent emits a schema. Your app maps it to components.
- Open-ended: The agent writes raw HTML. Your app renders it in a sandbox.

![Image](https://pbs.twimg.com/media/HI0u2OsbMAAPV5V?format=jpg&name=large)

2026 年的每一代 UI 框架都处于这条线的某个位置。差异在于架构层面，而非外观层面。每种模式在大规模应用时都会以不同方式破坏你的应用。

我尝试了不同的技术栈。大多数都能很好地处理一种模式。最终选择了 CopilotKit，因为它支持三种模式在同一运行时下运行，基于 AG-UI。那就是下面所有内容运行的技术栈。

## 模式 1：受控的，前端拥有 UI

![Image](https://pbs.twimg.com/media/HI24iaKagAAn_d8?format=jpg&name=large)

This is where most teams start. It's also where most teams get stuck.

You pre-build a React component. You bind it to a tool name. The agent picks that tool and the component renders inline in chat with the agent's args as props.

One frontend hook. Zero agent code. That's it.

```typescript
"use client";
import { z } from "zod";
import { useComponent } from "@copilotkit/react-core/v2";

const expenseChartSchema = z.object({
  title: z.string(),
  data: z.array(z.object({ label: z.string(), value: z.number() })),
});

function ExpenseChart({ title, data }: z.infer<typeof expenseChartSchema>) {
  return (
 <section className="rounded-xl border p-4">
 <h3 className="text-sm font-medium">{title}</h3>
 <ul className="mt-2 grid gap-1">
 {data.map((d) => (
 <li key={d.label} className="flex justify-between text-sm">
 <span>{d.label}</span>
 <span>${d.value}</span>
 </li>
 ))}
 </ul>
 </section>
  );
}

export function ExpensesCopilot() {
  useComponent({
 name: "showExpenseChart",
 description: "Render a breakdown of expenses by category.",
 parameters: expenseChartSchema,
 render: ExpenseChart,
  });

  return null;
}
```

The hook registers the tool with CopilotKit's runtime. The runtime advertises it to the agent over AG-UI. When the agent calls it, the args stream in and your component renders inline. No Python tool to write, no schema to wire, no API route to add.

Your design system stays in charge.

That expense chart isn't a mockup. The

[AI Financial Coach Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/generative_ui_agents/ai-financial-coach-agent) renders cards just like it for real budgets, savings plans, and debt payoff.

[![视频](https://pbs.twimg.com/amplify_video_thumb/2062047076545167360/img/Tp6C3uPe6M7deRKf.jpg)](https://x.com/Saboo_Shubham_/status/2062220865643982875)[![视频](https://pbs.twimg.com/amplify_video_thumb/2062047076545167360/img/Tp6C3uPe6M7deRKf.jpg)](https://x.com/Saboo_Shubham_/status/2062220865643982875)

Want the bare hook first? It's 'use-generative-ui-examples.tsx' in the

[Generative UI Starter Project](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/generative_ui_agents/generative-ui-starter-project).

The token tax

Every component you register sits in the agent's context window before the user has said anything. A typical tool description with its JSON schema runs around 400 tokens. 25 components are 10,000 tokens on every turn. You pay that tax per request.

The agent picks the wrong component too. Too many look similar. Pie chart and donut chart both "show proportions." It guesses.

When to add agent-side state

Shared state is the one case where writing a Python tool is worth it. The agent writes to session state. Other parts of the UI subscribe and re-render with no second LLM call. Pin a metric, the dashboard updates. Add a row, the table redraws.

```python
from google.adk.agents import LlmAgent
from google.adk.tools import ToolContext

def pin_metric(tool_context: ToolContext, label: str, value: float) -> dict:
 """Pin a metric to the user's dashboard."""
 pinned = tool_context.state.get("pinnedMetrics", [])
 tool_context.state["pinnedMetrics"] = pinned + [{"label": label, "value": value}]
 return {"status": "pinned"}

agent = LlmAgent(name="dashboard_agent", model="gemini-3.5-flash", tools=[pin_metric])
```

The frontend reads pinned metrics through CopilotKit's shared-state hook. The chat component still renders inline because the same tool name is wired with the frontend hook.

[AI Dashboard Canvas Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/generative_ui_agents/ai-dashboard-canvas-agent)

[![视频](https://pbs.twimg.com/amplify_video_thumb/2062048953902981120/img/CrZNRJf0XdKNJ8Hl.jpg)](https://x.com/Saboo_Shubham_/status/2062220865643982875)[![视频](https://pbs.twimg.com/amplify_video_thumb/2062048953902981120/img/CrZNRJf0XdKNJ8Hl.jpg)](https://x.com/Saboo_Shubham_/status/2062220865643982875)

[AI Deep Research Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/generative_ui_agents/ai-deep-research-agent)

[![视频](https://pbs.twimg.com/amplify_video_thumb/2062048571344715776/img/pMgtHFeZJ4495QB2.jpg)](https://x.com/Saboo_Shubham_/status/2062220865643982875)[![视频](https://pbs.twimg.com/amplify_video_thumb/2062048571344715776/img/pMgtHFeZJ4495QB2.jpg)](https://x.com/Saboo_Shubham_/status/2062220865643982875)

When to ship Controlled: Ten or fewer high-value flows. Design precision matters. You know the exact UIs you need.

When not to: Your codebase grows linearly with use cases. 25 components means 25 tool definitions sitting in every agent turn.

What breaks: Agent picks the wrong component. Two tool descriptions overlap semantically. Past 15 tools, two of them probably read like "displays data." Fix: rewrite descriptions to name the user intent, not the visual. "Use when the user asks to compare proportions of a whole" beats "renders a pie chart."

## Pattern 2: Declarative (A2UI), agent emits schema

![Image](https://pbs.twimg.com/media/HI24mX9agAEAzha?format=jpg&name=large)

This is the pattern most production agent apps end up needing.

The agent emits a JSON schema describing the UI. Your app has a catalog of components that maps schema nodes to React (or Svelte, Flutter, anything). One tool. Many UIs.

A2UI is the standard spec. CopilotKit ships the runtime. ADK runs the agent. AG-UI is the wire.

The agent tool returns three operations in order: create a surface, push the component tree, push the data.

```python
def search_flights(flights: list[Flight]) -> dict[str, Any]:
 """Search flights and display them as rich cards."""
 return {
 "a2ui_operations": [
 {"type": "create_surface", "surfaceId": SURFACE_ID, "catalogId": CATALOG_ID},
 {"type": "update_components", "surfaceId": SURFACE_ID, "components": FLIGHT_SCHEMA},
 {"type": "update_data_model", "surfaceId": SURFACE_ID, "data": {"flights": flights}},
 ]
 }
```

这是实际功能，不是伪代码。运行时中间件在工具结果中看到 a2ui\_operations 容器，并将界面转发到前端。添加酒店？新的模式文件。另一个具有不同界面 ID 的函数。前端无需额外工作。

Fixed schema vs dynamic schema

The component tree above lives in flights.json. You wrote it. The agent only fills in the data. That's a fixed schema.

Dynamic schema flips it: a secondary LLM writes the component tree per turn from conversation context. Same a2ui\_operations container at the end. The Google ADK showcase ships both.

The catalog is the contract

Definitions list the components the agent is allowed to emit, with Zod schemas for the props. Renderers fill in React. Typos become build errors instead of blank screens.

```typescript
const renderers: CatalogRenderers<TravelDefinitions> = {
  FlightCard: ({ props }) => (
 <article className="rounded-xl border p-4">
 <header className="flex justify-between">
 <span>{(props as any).airline}</span>
 <span>{(props as any).price}</span>
 </header>
 <div className="text-sm text-muted-foreground">
 {(props as any).origin} → {(props as any).destination} · {(props as any).departureTime}
 </div>
 </article>
  ),
};

export const travelCatalog = createCatalog(travelDefinitions, renderers, {
  catalogId: "copilotkit://travel-catalog",
  includeBasicCatalog: true,
});
```

[Generative UI Starter Project](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/generative_ui_agents/generative-ui-starter-project)

[![视频](https://pbs.twimg.com/amplify_video_thumb/2062050354922233856/img/HUgLymIIUEQNLrYy.jpg)](https://x.com/Saboo_Shubham_/status/2062220865643982875)[![视频](https://pbs.twimg.com/amplify_video_thumb/2062050354922233856/img/HUgLymIIUEQNLrYy.jpg)](https://x.com/Saboo_Shubham_/status/2062220865643982875)

Buttons and other interactive components carry an action in the schema. The basic catalog wires it to onClick. Click fires an event back to the agent over AG-UI. The agent decides what to render next. Zero click handlers.

The token math

50 card types or 500, the agent sees one function. Tokens per turn stay flat as your component library grows.

Extensible to any rendering framework because it's just JSON. Any agent that already speaks AG-UI can drive A2UI on day zero. You don't touch agent code to wire this up.

Trade-off: The LLM owns the layout. Output varies run to run within your catalog. If you're shipping legal disclosures, marketing surfaces, or anything where exact pixel placement matters, this is not your bucket.

Declarative is the pattern built for the long tail. Dashboards, results, forms, cards, widgets.

When to ship Declarative: You have more use cases than time to pre-build. You care about token economics past the prototype stage.

What breaks: Built a custom FlightCard. Every flight renders as the basic catalog's generic card. No error in the console. The CATALOG\_ID on the agent and catalogId in createCatalog on the frontend don't match. Frontend doesn't recognize the catalog the agent is targeting, falls back to basic. Match the strings exactly on both sides.

## Pattern 3: Open-ended, no catalog, no rules

![Image](https://pbs.twimg.com/media/HI25lZ8bUAAiX0A?format=jpg&name=large)

The third pattern is the opposite extreme. No catalog. No schema. Just a blank canvas.

Two sub-patterns live in this bucket.

MCP Apps

An MCP server exposes UI surfaces that the agent drives. Excalidraw is the example that stuck with me. The agent gets full control of the canvas. Draws diagrams from your context. Owns every pixel on the board.

![Image](https://pbs.twimg.com/media/HI0yNVwbYAACK88?format=jpg&name=large)

Implementing the client protocol from scratch is painful, so CopilotKit ships an MCPAppsMiddleware. Attach it to your agent and point it at any MCP Apps server.

```typescript
const agent = new BuiltInAgent({
  model: "openai/gpt-5.5",
  prompt: "You are a helpful assistant.",
}).use(
  new MCPAppsMiddleware({
 mcpServers: [{ type: "http", url: "https://mcp.excalidraw.com/mcp", serverId: "my-server" }],
  }),
);
```

Spin up the

[MCP Apps Showcase](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/generative_ui_agents/mcp-apps-generative-ui-showcase) and you're booking flights and reserving hotels inside the chat window. Same middleware, real MCP servers. Or go further.

The

[AI MCP App Builder](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/generative_ui_agents/ai-mcp-app-builder) lets the agent write a brand-new app into an E2B sandbox, then renders it live.

[![视频](https://pbs.twimg.com/amplify_video_thumb/2062049679664398336/img/WEGGWcRPy3RhPaAV.jpg)](https://x.com/Saboo_Shubham_/status/2062220865643982875)[![视频](https://pbs.twimg.com/amplify_video_thumb/2062049679664398336/img/WEGGWcRPy3RhPaAV.jpg)](https://x.com/Saboo_Shubham_/status/2062220865643982875)

Sandboxed HTML

The agent writes raw HTML. Your app renders it inside a sandboxed iframe so it can't hijack the session.

The runtime registers an HTML rendering tool and ships it to the agent over AG-UI. The agent calls it with whatever markup it wants. There is no HTML tool to define on the agent side. The runtime injects it.

Agent-side instruction is doing real work:

```python
canvas_agent = LlmAgent(
 name="canvas_agent",
 model="gemini-3.5-flash",
 instruction=(
 "You are a visualization assistant. When the user asks to see, "
 "draw, or visualize anything, generate an interactive HTML UI. "
 "Use Tailwind classes only. No external fonts. Stick to neutral "
 "colors unless the user names one."
 ),
)
```

Without those style rules, the model defaults to whatever aesthetic was loudest in its training data that week. With them, you get something close to your brand most of the time. Not always.

The brand inconsistency problem

I tried shipping Open-ended as the primary UI for an agent. Pulled it in a week.

"Neo-brutalist" on Tuesday. "iOS 4 clone" on Wednesday. Style rules in the prompt nudge the agent toward your brand. They don't guarantee it. The brand kept changing. The product felt unserious.

![Image](https://pbs.twimg.com/media/HI0y7Y7agAAzYK9?format=jpg&name=large)

Open-ended isn't useless. It's misapplied.

Right call for one thing: throwaway interactions where the user doesn't care what the interface looks like and will never see it again. "Show me how electrons work." "Give me a weird bar chart of my last 10 queries." "Visualize this API response." The kind of thing you see in Google AI overviews.

When to ship Open-ended: One-shot queries. Disposable visualizations. Sandboxed experiments. Never as the primary surface.

What breaks: The iframe renders. Buttons don't click. Forms don't submit. Sandbox flags are too tight, or too loose in a way the browser refuses. Set the iframe sandbox to allow scripts and allow forms. Nothing else. Never allow-same-origin.

## How to pick

Run the decision tree before you write code.

Designer has pixel-perfect mockups for this flow? Controlled.

Dozens of card types or widgets to ship? Declarative.

One-shot, throwaway visualization the user will never see twice? Open-ended.

Can't decide? Default to Declarative. Upgrade to Controlled for the top 3 flows. Never Open-ended as the default.

If you're already shipping and not sure where you landed, count the render tools. Past 15, you're in Controlled and the wall is close. Start wiring A2UI this week.

## Three patterns. Three bets.

Controlled bets on you. Pre-built components, pixel-perfect. Expensive past 25 of them.

Declarative bets on the schema. The schema is the contract. The agent fills it in. Scales flat.

Open-ended bets on the model. No catalog, no schema, raw HTML. Good for throwaway. Brittle for anything that ships twice.

The mistake isn't picking the wrong pattern. It's not knowing you picked one.

Most teams default to Controlled because the framework defaults to Controlled. They hit the wall at 25 components and reach for Open-ended because it looks compelling in demos. Neither was a decision. Both were drift.

Pick on purpose. Match the pattern to the problem. Controlled for the flows that need to be exact. Declarative for the long tail. Open-ended for the disposable.

Open Source Generative UI Agent Templates

The reference for all three lives in the new

[Generative UI Agents](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/generative_ui_agents) section of awesome-llm-apps. Clone what you need. Rip out what you don't.

* * *

I'll be publishing more about shipping agents in production, AG-UI, and the patterns that scale. Follow me

[@Saboo\_Shubham\_](https://twitter.com/Saboo_Shubham_) to stay tuned.