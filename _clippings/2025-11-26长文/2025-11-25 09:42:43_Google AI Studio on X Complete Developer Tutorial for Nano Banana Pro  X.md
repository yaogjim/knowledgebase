---
title: "Google AI Studio on X: "Complete Developer Tutorial for Nano Banana Pro" / X"
source: "https://x.com/GoogleAIStudio/status/1992267030050083091"
author: ""
created: 2025-11-25 09:42:43
published: 2025-11-25 09:42:43
description: ""
tags: ""
status: "inbox"
importance: 2
effort: 2
review_level: 0
review_next: "2025-12-10"
review_interval: null
review_count: 0
decision: null
topics: []
links_out: []
summary: ""
pov: ""
actions: []
---
探索这款下一代 AI 模型的先进功能——包括思考、搜索基础和惊艳的 4K 输出——将如何赋能您构建复杂而富有创意的应用程序。

虽然 Flash 模型（Nano Banana）带来了速度和成本优势，但 Pro 版本引入了"思考"能力、搜索基础和高保真 4K 输出。现在是时候用复杂创意任务大展身手了！

本指南将引导您通过 使用 Nano Banana Pro 的高级功能。

本指南将涵盖： 1\. 在 Google AI Studio 中使用 Nano Banana Pro 2. 项目设置 3. 初始化客户端 4. 基础生成（经典篇） 5. 思考过程 6. 搜索基础 7. 高分辨率 4K 生成 8. 多语言支持能力 9. 高级图像混合 10. 独家演示版 11. 最佳实践与提示技巧

> 注 ：如需交互式版本，请查阅 或 AI Studio 的 。

虽然最终用户可以通过 访问 Nano Banana Pro，但开发者进行提示词原型设计和测试的最佳环境是 。AI Studio 是一个无需编写代码即可体验所有可用 AI 模型的实验场，同时也是使用 Gemini API 进行开发的入口。

您可以在 AI Studio 中使用 Nano Banana Pro。开始使用时，请前往 ，使用您的 Google 账户登录，并在模型选择器中选取 Nano Banana Pro（Gemini 3 Pro 图像版）。

与 Nano-Banana 相反，专业版不提供免费层级 ，这意味着您需要选择已启用计费的 API 密钥（参见下文"项目设置"部分）。

[

![Image](https://pbs.twimg.com/media/G6XvNuTa0AAdoTn?format=jpg&name=medium)



](https://x.com/GoogleAIStudio/article/1992267030050083091/media/1992261429228130304)

> 提示 ：您也可以在 AI Studio 中直接体验 Nano Banana 网页应用，访问地址：，或浏览代码并重构。

-   项目账单设置已完成。
    
-   适用于 或 的 Google 生成式 AI SDK
    

如果你已经是资深的 Gemini API 用户，并且已具备上述所有条件，那太好了！直接跳过本节进入下一部分即可。否则，以下是入门指南：

首次登录 AI Studio 时，系统会自动创建一个 Google Cloud 项目及相应的 API 密钥。

打开 并点击“复制”图标以复制您的 API 密钥。

[

![Image](https://pbs.twimg.com/media/G6XvZ89asAAnQ0S?format=jpg&name=medium)



](https://x.com/GoogleAIStudio/article/1992267030050083091/media/1992261639320809472)

由于 Nano Banana Pro 不提供免费套餐，您必须在 Google Cloud 项目中启用计费功能。

[

![Image](https://pbs.twimg.com/media/G6XvWHWacAAEDAi?format=jpg&name=medium)



](https://x.com/GoogleAIStudio/article/1992267030050083091/media/1992261573390528512)

使用 Nano Banana Pro 生成图像比 Flash 版本更昂贵，尤其是 4K 图像。截至本文发布时，1K 或 2K 图像的成本为 0.134 美元，而 4K 图像则需 0.24 美元（还需加上输入内容和文本输出的 token 费用）。

> 专业提示 ：若想节省 50%的生成成本，可使用。但作为交换，您可能需要等待最多 24 小时才能获取生成图像。

```
pip install -U google-genai
# Install the Pillow library for image manipulation
pip install Pillow
```

```
npm install @google/genai
```

> 注意 ：以下示例使用 Python SDK 进行演示。本文档的 中提供了使用 JavaScript 实现 Nano Banana 的等效代码片段。

如需使用专业版模型，您需要使用 gemini-3-pro-image-preview 模型标识符。

```
from google import genai
from google.genai import types

# Initialize the client
client = genai.Client(api_key="YOUR_API_KEY")

# Set the model ID
PRO_MODEL_ID = "gemini-3-pro-image-preview"
```

在深入探讨高级功能之前，我们先来看一个标准生成示例。您可以通过 response\_modalities（用于获取文本和图像或仅图像）和 aspect\_ratio 参数来控制输出效果。

```
prompt = "Create a photorealistic image of a siamese cat with a green left eye and a blue right one"
aspect_ratio = "16:9" # "1:1","2:3","3:2","3:4","4:3","4:5","5:4","9:16","16:9" or "21:9"

response = client.models.generate_content(
    model=PRO_MODEL_ID,
    contents=prompt,
    config=types.GenerateContentConfig(
        response_modalities=['Text', 'Image'], # Or just ['Image']
        image_config=types.ImageConfig(
            aspect_ratio=aspect_ratio,
        )
    )
)

# Display the image
for part in response.parts:
    if image:= part.as_image():
        image.save("cat.png")
```

[

![Image](https://pbs.twimg.com/media/G6XwpVpbgAAORXI?format=jpg&name=medium)



](https://x.com/GoogleAIStudio/article/1992267030050083091/media/1992263003157528576)

聊天模式也是一个选择（实际上，在多轮编辑中我会推荐使用此模式）。请查看第8个示例"多语言香蕉"作为参考。

Nano Banana Pro 不止是绘画；它是在思考 。这意味着在生成图像前，它能先对你最复杂曲折的指令进行逻辑推演。最妙的是？你还能窥探它的大脑运作！

要启用此功能，请在 thinking\_config 中设置 include\_thoughts=True。

```
prompt = "Create an unusual but realistic image that might go viral"
aspect_ratio = "16:9"

response = client.models.generate_content(
    model=PRO_MODEL_ID,
    contents=prompt,
    config=types.GenerateContentConfig(
        response_modalities=['Text', 'Image'],
        image_config=types.ImageConfig(
            aspect_ratio=aspect_ratio,
        ),
        thinking_config=types.ThinkingConfig(
            include_thoughts=True # Enable thoughts
        )
    )
)

# Display the image and thoughts
for part in response.parts:
  if part.thought:
    print(f"Thought: {part.text}")
  elif image:= part.as_image():
    image.save("viral.png")
```

```
## Imagining Llama Commuters

I'm focusing on the llamas now. The goal is to capture them as
daily commuters on a bustling bus in La Paz, Bolivia. My plan
involves a vintage bus crammed with amused passengers. The image
will highlight details like one llama looking out the window,
another interacting with a passenger, all while people take
photos.

[IMAGE]

## Visualizing the Concept

I'm now fully immersed in the requested scenario. My primary
focus is on the "unusual yet realistic" aspects. The scene is
starting to take shape with the key elements established.
```

[

![Image](https://pbs.twimg.com/media/G6XxIxGaEAA-_4r?format=jpg&name=medium)



](https://x.com/GoogleAIStudio/article/1992267030050083091/media/1992263543102771200)

这种透明度让你能清楚了解模型是如何解读你的请求，就像与艺术家直接对话一样！

最具颠覆性的功能之一是搜索锚定 。Nano Banana Pro 不拘泥于过去，它能通过谷歌搜索获取实时数据，生成精准且最新的图像。想要天气信息？轻松搞定。

```
prompt = "Visualize the current weather forecast for the next 5 days in Tokyo as a clean, modern weather chart. add a visual on what i should wear each day"

response = client.models.generate_content(
    model=PRO_MODEL_ID,
    contents=prompt,
    config=types.GenerateContentConfig(
        response_modalities=['Text', 'Image'],
        image_config=types.ImageConfig(
            aspect_ratio="16:9",
        ),
        tools=[{"google_search": {}}] # Enable Google Search
    )
)

# Save the image
for part in response.parts:
    if image:= part.as_image():
        image.save("weather.png")

# Display sources (you must always do that)
print(response.candidates[0].grounding_metadata.search_entry_point.rendered_content)
```

[

![Image](https://pbs.twimg.com/media/G6XxUgraAAEqo94?format=jpg&name=medium)



](https://x.com/GoogleAIStudio/article/1992267030050083091/media/1992263744852983809)

需要印刷级画质？Nano Banana Pro 支持 4K 分辨率。毕竟有时候，大即是美。

```
prompt = "A photo of an oak tree experiencing every season"
resolution = "4K" # Options: "1K", "2K", "4K", be careful lower case do not work.

response = client.models.generate_content(
    model=PRO_MODEL_ID,
    contents=prompt,
    config=types.GenerateContentConfig(
        response_modalities=['Text', 'Image'],
        image_config=types.ImageConfig(
            aspect_ratio="1:1",
            image_size=resolution
        )
    )
)
```

[

![Image](https://pbs.twimg.com/media/G6Xxf5zbwAA272v?format=jpg&name=medium)



](https://x.com/GoogleAIStudio/article/1992267030050083091/media/1992263940576100352)

> 注意 ：4K 生成成本较高，请谨慎使用！

该模型能生成并翻译图像中的文字，支持十余种语言，堪称您视觉上的万能翻译器。

```
# Generate an infographic in Spanish
message = "Make an infographic explaining Einstein's theory of General Relativity suitable for a 6th grader in Spanish"

response = chat.send_message(message,
    config=types.GenerateContentConfig(
        image_config=types.ImageConfig(aspect_ratio="16:9")
    )
)

# Save the image
for part in response.parts:
    if image:= part.as_image():
        image.save("relativity.png")
```

[

![Image](https://pbs.twimg.com/media/G6Xxvc_bQAAMjIz?format=jpg&name=medium)



](https://x.com/GoogleAIStudio/article/1992267030050083091/media/1992264207719677952)

```
# Translate it to Japanese
message = "Translate this infographic in Japanese, keeping everything else the same"
response = chat.send_message(message)

# Save the image
for part in response.parts:
    if image:= part.as_image():
        image.save("relativity_JP.png")
```

[

![Image](https://pbs.twimg.com/media/G6XxxpZbYAEJ5xQ?format=jpg&name=medium)



](https://x.com/GoogleAIStudio/article/1992267030050083091/media/1992264245409701889)

虽然 Flash 模型最多只能混合 3 张图片，但 Pro 模型却能处理多达 14 张图片 ！这简直是一场提示词里的狂欢派对。无论是制作复杂拼贴画，还是展示全系列产品线，都再合适不过。

```
# Mix multiple images
response = client.models.generate_content(
    model=PRO_MODEL_ID,
    contents=[
        "An office group photo of these people, they are making funny faces.",
        PIL.Image.open('John.png'),
        PIL.Image.open('Jane.png'),
        # ... add up to 14 images
    ],
)

# Save the image
for part in response.parts:
    if image:= part.as_image():
        image.save("group_picture.png")
```

[

![Image](https://pbs.twimg.com/media/G6XyAQTbMAAB0oK?format=jpg&name=medium)



](https://x.com/GoogleAIStudio/article/1992267030050083091/media/1992264496371675136)

> 注意 ：若想确保角色形象高度还原，建议将数量控制在 5 个以内——这已足够让派对之夜精彩纷呈！

以下是仅凭 Nano Banana Pro 才能实现的惊艳功能，准备好大开眼界吧：

> 提示词 ："搜索网络后生成等轴测视角的详细像素艺术图，展现纪尧姆·韦尔纳德的职业生涯"

这利用搜索基础来查找关于某个人的具体信息，并以特定风格进行可视化呈现。

[

![Image](https://pbs.twimg.com/media/G6XyJNeaQAACFpl?format=jpg&name=medium)



](https://x.com/GoogleAIStudio/article/1992267030050083091/media/1992264650231267328)

> 提示词 ："展示一张关于十四行诗运作机制的信息图，需包含一首以香蕉为主题的十四行诗范例，并附上对这首诗的详尽文学分析。整体呈现复古美学风格"

该模型能够生成连贯、长篇的文本，并将其完美融入复杂的布局中。

[

![Image](https://pbs.twimg.com/media/G6XyLLBbAAA8IfB?format=jpg&name=medium)



](https://x.com/GoogleAIStudio/article/1992267030050083091/media/1992264683932549120)

> 提示词 ："一张关于 TCG 玩家的百老汇演出节目单照片，节目单置于精美的剧院座椅上，专业制作且质感光鲜，可见封面及展示舞台剧照的内页。"

[

![Image](https://pbs.twimg.com/media/G6XyNKPaMAA4Y8q?format=jpg&name=medium)



](https://x.com/GoogleAIStudio/article/1992267030050083091/media/1992264718082519040)

为充分发挥 Nano Banana 模型性能，请遵循以下提示词使用指南：

追求极致细节 ：对主体、色彩、光线和构图描述得越具体，对生成结果的控制力就越强。

提供背景与意图 ：说明图像的创作目的或期望氛围。模型对背景的理解将影响其创作选择。

迭代优化 ：无需追求一次成型。借助模型的对话能力逐步调整，持续完善你的图像作品。

采用分步指导 ：针对复杂场景，将提示词拆解为一系列清晰有序的指令序列。

采用积极表述 ：避免使用“禁止车辆”这类否定式提示词，转而用积极方式描绘理想场景：“空无一人的街道，毫无交通痕迹”。

控制镜头语言 ：运用摄影与电影术语指导构图，例如"广角镜头"、"微距特写"或"低角度视角"。

善用搜索基础功能 ：当你希望模型使用实时或现实世界数据时，务必表述精确。例如，“搜索网络上关于里昂奥林匹克队最近一场奥运比赛的信息并制作信息图”会比单纯说“制作 OL 最近比赛的信息图”（虽然后者也可能有效，但不要冒险）效果更好。

使用 来降低成本并获取更高配额 ：批量 API 支持将小型或超大批量请求打包发送。虽然处理时间可能长达 24 小时，但能为您节省 50%的生成成本，同时配额上限也更高！

若想深入了解最佳实践，请查阅文档以及官方博客发布的 。

Nano Banana Pro（Gemini 3 Pro 图像版）为 AI 图像生成开辟了新前沿。凭借其思考、搜索和 4K 渲染能力，它既是专业创作者的利器，也是深度娱乐的玩伴。

准备好尝试了吗？前往 ，试用或定制我们的 ，或查看 。