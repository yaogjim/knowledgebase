---
title: "Automating Link Uploads to NotebookLM Using Python and Playwright"
source: "https://oboe-violin-w3kd.squarespace.com/blogs/automating-link-uploads-to-notebooklm-using-python-and-playwright?utm_source=chatgpt.com"
author:
  - "[[Written By Team Databasyx]]"
  - "[[Team Databasyx]]"
published: 2025-11-20
created: 2025-11-20
description: "Tired of manually adding links to Google’s NotebookLM one at a time? In this post, I walk through how I built a Python-based automation tool using Playwright that lets you upload up to 300 sources in just a few clicks — and how you can start using it yourself."
tags:
  - "Written By Team Databasyx"
  - "Team Databasyx"
---
## 使用 Python 与 Playwright 实现 NotebookLM 链接上传自动化

by Nathan Purvis

**Background**

Google 的 [NotebookLM](https://notebooklm.google.com/) 是一款卓越工具，它借助 Gemini 的强大能力消化多源信息，为你提供包括播客、思维导图、学习指南等各类资源。但如果你曾尝试手动添加大量链接，就会切身感受到现有流程的繁琐——既无法批量添加，又缺乏官方 API，除了反复复制粘贴外别无选择。

这就是本项目的用武之地！我最近利用 [Playwright](https://playwright.dev/python/) 构建了一个轻量级 Python 解决方案，实现了整个资源上传流程的自动化。目标是什么？让用户只需提供网页/YouTube 链接列表，点击运行，就能自动生成填充了这些资源的新笔记本——最高可达平台 300 个资源的上限。

**Why Playwright?**

此前我常用 Selenium 进行网页抓取这类浏览器自动化操作，但想探索是否有更高效的替代方案。最终选择 Playwright 主要基于以下几点考量：

- 支持无头与有头两种模式——便于在发布前轻松测试和故障排除，确保最终执行的顺畅无误
- 轻松安装并支持 Chromium
- 简单、无缝地处理持久登录状态
- 与 Python 集成并提供简洁 API，适用于 NotebookLM 等现代化动态网站

**管理与持久化 Google 登录**

由于 NotebookLM 是 Google 旗下的产品，我们需要使用 Google 账户进行认证。显然，我们既不愿在代码库中硬编码凭证，也无法绕过登录流程——更何况我们还需要在创建笔记本后访问它们！这时set\_login\_state.py便闪亮登场解决了难题。运行以下脚本：

1. 启动一个新的浏览器会话
2. 打开 NotebookLM 并等待手动登录
3. 将 Cookie 及本地/会话存储内容保存至您目录下的 state.json 文件（无需担心，该文件已默认加入.gitignore 忽略列表！）

![](https://images.squarespace-cdn.com/content/v1/6426fb4e849c041c6979c776/e7f0e712-7452-43eb-9a2a-b4c1d6f60f7b/1.png?format=100w)

![](https://images.squarespace-cdn.com/content/v1/6426fb4e849c041c6979c776/c62c523f-1c41-40f9-8f05-529ed59f5805/2.png?format=100w)

进入实际操作流程，Playwright 内置了所有必要功能来确保这一过程顺畅运行。例如，以下代码块所示：

```js
link_button = page.locator(
    "span.mdc-evolution-chip__text-label", has_text=re.compile(f"{source_type}",re.I)
)
link_button.wait_for(state="attached")
link_button.click()
```

在这段代码中，定位器方法会搜索包含指定文本标签（例如“网站”或“YouTube”，具体取决于来源类型）的按钮元素。wait\_for 函数确保该按钮存在于 DOM 中且处于“已附加”状态，这意味着它已准备好进行交互。最后，click 方法模拟用户点击按钮的操作。这一系列步骤确保脚本仅在按钮完全加载且可交互时才与之互动，从而避免因尝试点击未就绪元素而可能出现的错误。

遍历源文件由 links.py 处理。你会注意到两个 if 语句，根据提供的 URL 数量检查是否处于首次或末次循环。这是因为，若为首次循环，我们需要先创建一个新笔记本：

![](https://images.squarespace-cdn.com/content/v1/6426fb4e849c041c6979c776/2846612d-13da-482d-bd98-bf92688a1871/3.png?format=100w)

而如果当前已是最后一个信息来源，我们便无需继续点击“添加来源”按钮延续流程：

![](https://images.squarespace-cdn.com/content/v1/6426fb4e849c041c6979c776/50b29ee2-cc3c-465e-9c9e-45572a301ada/4.png?format=100w)

一旦我们跳出这个循环并完成向笔记本添加所有来源后，最后一步是设置用户提供的标题，并记录执行时间作为额外信息：

![](https://images.squarespace-cdn.com/content/v1/6426fb4e849c041c6979c776/b9aec7c3-d77d-4db4-9746-aedd0ac30b66/5.png?format=100w)

注意：如果你想观看实际操作过程，只需在 main.py 文件中修改以下内容：

```js
headless=True
```

To:

```js
headless=False
```

**Future ideas**

截至目前，该项目在处理网站和 YouTube 链接方面表现优异。但若需求足够旺盛，我还在构思一些拓展方向，例如：

- 为在本地.txt 文件中保存笔记的用户添加“复制文本”支持
- 将此转化为命令行工具以提升用户体验

欢迎提出更多想法和建议，也欢迎提交拉取请求！

**Final thoughts**

这真是一次令人无比愉悦的构建过程——表面看似简单，但深入探究用户界面流程和处理账户登录等细节时，却能发现一些关键的精妙之处。如果你花在上传链接上的时间比实际使用 NotebookLM 还多，不妨试试这个方法：这个脚本虽小但功能强大，能为你节省大量时间！

你可以在 [这里](https://github.com/DataNath/notebooklm_source_automation) 找到 GitHub 仓库，其中附有易于理解的 README 文件，包含更多信息和入门步骤。如果觉得有用，别忘了给它点个星标！

一如既往，如果您有任何补充建议、反馈或对未来内容的请求，请随时联系我！