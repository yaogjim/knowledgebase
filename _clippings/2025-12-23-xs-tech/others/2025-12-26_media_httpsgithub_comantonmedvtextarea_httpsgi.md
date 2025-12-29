---
title: "2025-12-26_news_ycombinator_com_httpsgithub_comantonmedvtextarea_httpsgi"
source: "https://news.ycombinator.com/item?id=46378554"
author:
  - "[[@media]]"
published: 2025-12-26
created: 2025-12-26
description:
tags:
  - "#l"
  - "#部分"
  - "news"
  - "@media"
---

# [httpsgithub.comantonmedvtextarea](httpsgi

[https://github.com/antonmedv/textarea](https://github.com/antonmedv/textarea)

我想看看仅用现代浏览器已提供的功能能构建出多深入的笔记应用——不使用任何框架，不使用任何存储 API，不需要构建步骤。

What it does:

单个 HTML 文件，无依赖，111 行代码

笔记存在于 URL 哈希中（可分享链接！）

使用 CompressionStream 自动压缩

纯文本编辑器（contenteditable）

History support

在 Hacker News 上展示：驻留在浏览器中的极简编辑器，所有内容均存储在 URL 中 | 黑客新闻

  支持浅色/深色模式

不存储、无 Cookie、不跟踪

整个应用就是页面源代码。

[https://textarea.my/](https://textarea.my/)

* * *

## Comments

> **gnyman** • [2025-12-24](https://news.ycombinator.com/item?id=46379719)
> 
> 真有意思，我做了几乎一模一样的东西，只是是针对地图的。
> 
> 我需要一种分享地图链接的方式，该链接带有绘图，并且能让接收者看到自己在地图上的位置。
> 
> 带注释的截图解决了第一个问题，但没有解决第二个问题。
> 
> Vibe 设计了这个，并且有很多和原帖作者相同的想法。
> 
> 花了一晚上。针对特定使用场景的即时应用是一种趋势。
> 
> 而且由于制作成本极低，且无需后端即可低成本托管，因此可以免费提供。
> 
> [https://nyman.re/mapdraw/#l=60.172108%2C24.941458&z=16&d=LU8...](https://nyman.re/mapdraw/#l=60.172108%2C24.941458&z=16&d=LU8xSyNhFJz57hLD3e13gctmi900d9uYFY5UXtJcdWSb5RqTJmW2sdxtRBsXQRRBCahVQhARQd0iNhb5A64iViKpBHHxB4iFFoJfVGbeq2bmvRHZjtjbPK5Gd6lx93kwkZ9dOzquxgepcUDLw3-0MIsVosvxniu3fc_13ErTbGrh91DrM5NwIiV2BCKBeyIhYiKEC0vDNDwEH_Ztyi5r2_wz15yvBeVgqmU15D84chK_FCZhQoNdK4flmHZCe0lYfSETURwJ2RHFaxZ85FF6k5XUvMOUTq4uG8WgEBQbsiGnc07WVOf7RI_qPcUfoe6bru5qli7fTToq5t9Tts5Y7_J3u-RktBnoX6PnQfX-KDWeqPXGLaw91rYoF9DET-RQ0fRvVy-D6v5uathDgSHxSCwJJALnAg_EiIg4bq6EKuvkJjVWeZHJxpw6pD3kuJlih9YGC2Heh9S_XKrEw9vUqI8-BTGXGXOdPS522I7o-Y6bsV4B)
> 
> > **mathgeek** • [2025-12-24](https://news.ycombinator.com/item?id=46380112)
> > 
> > \> Vibe engineered
> > 
> > 虽然我完全支持在适当的时候进行直觉式编码，但把这种编码称为工程学确实有很多幽默之处。:D
> > 
> > > **gnyman** • [2025-12-25](https://news.ycombinator.com/item?id=46383697)
> > > 
> > > 这不是我想出来的，是 Simon 写的，我喜欢“vibe coding”这种编码方式的区别——它需要更少的精力投入
> > > 
> > > 对于这个案例项目，我觉得实际上应该说这是“vibe 编码”的，但我不想只称之为“vibe 编码”，因为我确实花了时间反复调整并指导那个代理
> > > 
> > > [https://simonwillison.net/2025/Oct/7/vibe-engineering/](https://simonwillison.net/2025/Oct/7/vibe-engineering/)
> > > 
> > > > **mathgeek** • [2025-12-25](https://news.ycombinator.com/item?id=46384858)
> > > > 
> > > > 有趣的区别。我之前听说过有人将 vibe coding 描述为“vibe prompting，但你实际上要做一些工作”。不过话说回来，我就把你描述的这种情况称为用 AI 编程。
> > > > 
> > > > > **bdangubic** • [2025-12-25](https://news.ycombinator.com/item?id=46386369)
> > > > > 
> > > > > 用 AI 编码和用 VSCode 编码一样，都是编码。你决定从某个工具中获得哪些部分的帮助，哪些部分不需要。归根结底，本质上都是编码，而“用 AI 编码”听起来和“用键盘/麦克风编码”一样荒谬。
> > > > > 
> > > > > > **mathgeek** • [2025-12-26](https://news.ycombinator.com/item?id=46387991)
> > > > > > 
> > > > > > 第一部分正是我的观点，但在我看来，后者是无稽之谈。你不能让 AI 之前的 VSCode 帮你写程序。这就好比用 AI 做数学和用 Nspire CAS 做数学。没有理由去回应那些贬低凭感觉编码的人，他们声称我们不应该区分工具，但我们也不应该说所有工具都一样。我们不会认为用激光动力除草机耕作和用马拉犁耕作是一样的。
> > > 
> > > **stogot** • [2025-12-25](https://news.ycombinator.com/item?id=46385221)
> > > 
> > > 我怀疑需要一个规范来指导，才能称之为 vibe engineered
> > 
> > **block\_dagger** • [2025-12-24](https://news.ycombinator.com/item?id=46380139)
> > 
> > 好吧。不过，工程的一半似乎只是给任何实际有效的东西起个体面的名字。
> > 
> > > **mathgeek** • [2025-12-24](https://news.ycombinator.com/item?id=46380185)
> > > 
> > > 对于软件来说，不过这一点现在已经是一条被走熟的路了。我在 3D 建模领域见过一些实际上属于“氛围工程”的项目（这些项目并非软件相关），所以术语变得很混乱。
> > 
> > **jimmygrapes** • [2025-12-26](https://news.ycombinator.com/item?id=46388308)
> > 
> > 我一直是设计辅助开发者（DAD）的粉丝
> > 
> > **InsideOutSanta** • [2025-12-25](https://news.ycombinator.com/item?id=46383537)
> > 
> > 我只希望真正的工程师不会开始凭感觉设计桥梁和建筑。
> > 
> > **NuclearPM** • [2025-12-25](https://news.ycombinator.com/item?id=46386328)
> > 
> > 这有什么好笑的？
> 
> **zenmac** • [2025-12-25](https://news.ycombinator.com/item?id=46383256)
> 
> 很棒的工具！有个小问题：+/- 缩放按钮无法工作，可能是被其他 div 块覆盖了。在 Mac 上的 Firefox 浏览器中。
> 
> 这个代码是否在线上某处开源？
> 
> > **gnyman** • [2025-12-25](https://news.ycombinator.com/item?id=46383705)
> > 
> > 谢谢你的信息，我会看看是否能找一个代理来修复它
> > 
> > 这是一个静态网页，右键查看源代码即可获取。我在上面添加了 BSD2 许可证头，明确表示可以自由获取并进行几乎任何操作
> > 
> > > **zenmac** • [2025-12-25](https://news.ycombinator.com/item?id=46386611)
> > > 
> > > 嗯，放在 Codeberg、GitLab 或者甚至 GitHub 的仓库上会更好。这样我们就可以提交 PR 了。
> > > 
> > > Here is the fix:
> > > 
> > > .leaflet-top, .leaflet-left{ z-index: 100000; /\* 一些较高的数值 \*/ }
> > > 
> > > > **gnyman** • [2025-12-25](https://news.ycombinator.com/item?id=46386831)
> > > > 
> > > > 嗯，我在 Firefox 上试过了，它对我来说能用，而且对我而言，.leaflet-top 已经有一个较高的 z-index 值：1000；
> > > > 
> > > > 尽管我使用的是 140.6.0esr 版本，所以可能更新的版本需要更高的版本？
> > > > 
> > > > 代码现在在 GH 上了 [https://github.com/gnyman/mapdraw](https://github.com/gnyman/mapdraw)，codeberg 在我的待办事项里
> > > > 
> > > > > **Kailhus** • [2025-12-25](https://news.ycombinator.com/item?id=46387282)
> > > > > 
> > > > > 可以试试这个 hack 式的 2147483647 最大 z-index。在安卓版火狐浏览器上没有问题。
> 
> **ninalanyon** • [2025-12-25](https://news.ycombinator.com/item?id=46386911)
> 
> 看起来很有用，但对我来说并不完全如预期那样工作。
> 
> 在 Vivaldi 中，位置追踪功能无法使用。版本 7.7.3851.66（官方版本）（64 位）Chromium 版本 142.0.7444.245 扩展稳定频道（可能还包含其他安全补丁） 频道：官方版本 平台/操作系统：Linux - linuxmint 21.3
> 
> 并且在同一台机器上的 Firefox 146.0.1 中，URL 不会更新。
> 
> **gnyman** • [2025-12-25](https://news.ycombinator.com/item?id=46383734)
> 
> 我把源代码的一个副本放在了 GitHub 上，以防有人想改进这个项目 [https://github.com/gnyman/mapdraw](https://github.com/gnyman/mapdraw)
> 
> **nolito** • [2025-12-25](https://news.ycombinator.com/item?id=46386503)
> 
> 但还未经过充分测试。尝试创建一个地图并将 URL 复制到另一个地图。现在对第一个地图添加更多注释或移动地图中心，然后复制生成的 URL 并粘贴到另一个浏览器中的另一个地图。这不起作用（至少对我来说，在不同浏览器上是这样）。
> 
> > **gnyman** • [2025-12-25](https://news.ycombinator.com/item?id=46386813)
> > 
> > 我想我明白你的意思，感谢你的反馈。如果在网页上修改#部分，这和重新加载网页是不一样的，而且我不确定我会留意那部分的变化
> 
> **antman** • [2025-12-25](https://news.ycombinator.com/item?id=46382757)
> 
> 太棒了！现在用它来计划旅行。
> 
> 我们还能添加文本注释吗？另外，删除按钮可以只删除最后一个图形或者一个选中的图形，以免重新开始？
> 
> **piffey** • [2025-12-25](https://news.ycombinator.com/item?id=46386267)
> 
> 喜欢这个。真不知道有多少次我截图过地图，然后在上面给家人/朋友画路线指引。好主意。
> 
> **blntechie** • [2025-12-25](https://news.ycombinator.com/item?id=46382393)
> 
> 这太酷了！！页面的响应速度比我用过的任何地图应用都要好得多。
> 
> > **gnyman** • [2025-12-25](https://news.ycombinator.com/item?id=46383714)
> > 
> > 是的，如果你稍微花点功夫，现代计算机的速度有多快是不是很令人印象深刻？在这个例子中，我觉得我让它只用纯 JavaScript，并确保它运行得快（笑）
> 
> **nextaccountic** • [2025-12-25](https://news.ycombinator.com/item?id=46381985)
> 
>   这真的很酷！
> 
> 并且如果你愿意接受 bug 报告的话…当我移动（地图）时，图形会随地图平滑移动，但当我缩放（地图）时，图形只会在地图缩放动画结束后才移动，而不是平滑地跟随缩放过程。
> 
> **getupyang** • [2025-12-25](https://news.ycombinator.com/item?id=46385515)
> 
> 真的很酷——这是我用过的加载速度最快的地图。
> 
> **RandomDistort** • [2025-12-24](https://news.ycombinator.com/item?id=46380120)
> 
>   这是开源的吗？
> 
> > **gnyman** • [2025-12-25](https://news.ycombinator.com/item?id=46383706)
> > 
> > 它是一个静态网页，源代码可通过右键查看源代码获取。我在其中添加了一个 BSD2 许可证头文件，以明确表示可以获取并对其做大部分想做的事情
> 
> **Gehinnn** • [2025-12-24](https://news.ycombinator.com/item?id=46380427)
> 
> This is very cool!

> **maxloh** • [2025-12-24](https://news.ycombinator.com/item?id=46378863)
> 
> 根据规范\[0\]，一个 URL 可以容纳至少 8000 个字符。
> 
> 建议所有发送方和接收方至少支持协议元素中长度为 8000 字节的统一资源标识符（URI）。需要注意的是，这意味着某些结构和传输时的表示形式（例如 HTTP/1.1 中的请求行）在某些情况下必然会更大。
> 
> 主流浏览器支持至少 64,000 个字符\[1\]，而 Chrome 支持最多 2MB\[2\]。
> 
> \[0\]: [https://www.rfc-editor.org/rfc/rfc9110#section-4.1-5](https://www.rfc-editor.org/rfc/rfc9110#section-4.1-5)
> 
> \[1\]: [https://stackoverflow.com/a/417184/](https://stackoverflow.com/a/417184/)
> 
> \[2\]: [https://chromium.googlesource.com/chromium/src/+/HEAD/docs/s...](https://chromium.googlesource.com/chromium/src/+/HEAD/docs/security/url_display_guidelines/url_display_guidelines.md#url-length)
> 
> > **medv** • [2025-12-24](https://news.ycombinator.com/item?id=46378900)
> > 
> > Chrome 限制为 2MB，Firefox 为 1MB，WebKit 无限制。
> > 
> > 以下是费奥多尔·陀思妥耶夫斯基的《罪与罚》：
> > 
> > [https://medv.io/goto/crime-and-punishment-by-fyodor-dostoevs...](https://medv.io/goto/crime-and-punishment-by-fyodor-dostoevsky.html)
> > 
> > > **maxloh** • [2025-12-24](https://news.ycombinator.com/item?id=46379250)
> > > 
> > > 不管怎么说，iOS 端可能有一个 2GB 的限制。
> > > 
> > > [https://github.com/swiftlang/swift-corelibs-foundation/blob/...](https://github.com/swiftlang/swift-corelibs-foundation/blob/swift-DEVELOPMENT-SNAPSHOT-2025-12-19-a/Sources/CoreFoundation/CFURLComponents_URIParser.c#L719)
> > > 
> > > **spicyusername** • [2025-12-25](https://news.ycombinator.com/item?id=46381560)
> > > 
> > > Incredible.
> > > 
> > > 我最喜欢现代性的一点，是我们被赋予了能够对一个 riff 的 riff 再进行 riff 的能力。
> > > 
> > > 1346年，如果一个铁匠想出了什么很酷的东西，那么它很可能会随着他一起失传。
> > > 
> > > > **Kye** • [2025-12-25](https://news.ycombinator.com/item?id=46384838)
> > > > 
> > > > 在核实我对历史的既有假设的过程中，我学到一件事：就是很容易低估过去的人们。他们可能比你想象的更擅长交流这类事情。
> > 
> > **idle\_zealot** • [2025-12-25](https://news.ycombinator.com/item?id=46387251)
> > 
> > 我可以在移动版 Safari 中打开包含书籍文本的页面，但在尝试复制/分享页面 URL 时，iOS 似乎会截断内容。我无法让它在往返到备忘录（Notes）时保持完整。对于移动用户来说，或许应该提醒他们，如果写得太多，保存链接时可能会导致链接损坏。
> > 
> > **buddhistdude** • [2025-12-25](https://news.ycombinator.com/item?id=46387247)
> > 
> > 我觉得这很有趣，当你阅读这条评论时，整本书已经在你的电脑上了。当你点击链接时，它就会被渲染。
> > 
> > 编辑：实际上不是这样的，因为你使用了 URL 缩短服务
> > 
> > **caminanteblanco** • [2025-12-25](https://news.ycombinator.com/item?id=46382910)
> > 
> > 不幸的是，这立即导致我的 Android Firefox 夜间版浏览器崩溃了。有趣的是，页面加载了，但点击地址栏一次就直接把我带到了主屏幕。
> > 
> > > **Departed7405** • [2025-12-25](https://news.ycombinator.com/item?id=46386873)
> > > 
> > > 对我来说，在 IronFox 浏览器上，它显示了一个空白的地址栏，但在感觉像是 5 秒之后才加载完成。
> > 
> > **gchamonlive** • [2025-12-24](https://news.ycombinator.com/item?id=46380184)
> > 
> > 有趣的是，在 Firefox 移动版（实际上是 Fennec）中，如果我点击地址栏，会出现一个空的文本框。
> > 
> > 编辑：实际上我可以编辑 URL，但是加载需要一些时间。
> > 
> > **ron-ulitsky** • [2025-12-26](https://news.ycombinator.com/item?id=46388372)
> > 
> > 第一次我在我的 Pixel 上尝试打开那个链接时，它导致 Chrome 崩溃了，哈哈。不过第二次就正常工作了。
> > 
> > **oneseven** • [2025-12-25](https://news.ycombinator.com/item?id=46381136)
> > 
> > 嗯...让我好奇你是否可以用 gzipped 文本训练 LLMs，这样会节省大量的词元。
> > 
> > **hallole** • [2025-12-24](https://news.ycombinator.com/item?id=46379051)
> > 
> > 哈哈，轻触地址栏导致我的 Chrome 在移动设备上崩溃了。
> > 
> > > **lurking\_swe** • [2025-12-24](https://news.ycombinator.com/item?id=46379703)
> > > 
> > > 在移动 Safari 上对我来说加载成功了。
> > > 
> > > > **kylecazar** • [2025-12-24](https://news.ycombinator.com/item?id=46379940)
> > > > 
> > > > 我这边加载也正常——但和父帖一样，在安卓设备上点击地址栏进行分享后，应用崩溃了 :)
> > > > 
> > > > > **nosrepa** • [2025-12-24](https://news.ycombinator.com/item?id=46380397)
> > > > > 
> > > > > 我的 Firefox 在手机上似乎处理得很好。
> > 
> > **scotty79** • [2025-12-24](https://news.ycombinator.com/item?id=46379341)
> > 
> > 在 Win11 Edge 上运行良好
> 
> **berkes** • [2025-12-24](https://news.ycombinator.com/item?id=46379505)
> 
> 我猜监控行业有足够的动机让这个变得越来越大，以便他们能够在 URL 中塞进更多的 UTM 跟踪器、活动 ID、推荐跟踪器等等。
> 
> Instagram、YouTube 或其他大型平台上的典型内容分享链接竟然如此冗长，这真的很离谱。本可以是像 example.com/t/some-large-enough-id?time=13337 这样简洁的 URL，现在却塞满了数百个字符，只是为了收集更多关于使用这些链接的人的数据。
> 
> **dspillett** • [2025-12-24](https://news.ycombinator.com/item?id=46379141)
> 
> *
> 
> 根据规范\[0\]，一个 URL 可以容纳至少 8000 个字符。*
> 
> *
> 
> 建议所有发送方和接收方至少支持协议元素中长度为 8000 字节的统一资源标识符（URI）。*
> 
> 始终值得记住的是，除非你已经确保内容已被转换为 URI 安全的 ASCII 子集，否则字符和字节不是一回事。
> 
> > **ghurtado** • [2025-12-24](https://news.ycombinator.com/item?id=46379236)
> > 
> > 说得很有道理。在最坏的情况下，你只会有那个容量的五分之一。
> 
> **mrweasel** • [2025-12-25](https://news.ycombinator.com/item?id=46386889)
> 
> 允许超过 64000 个字符的背后可能的原因是什么？即使 64k 似乎也显得不必要地大。

> **roxolotl** • [2025-12-24](https://news.ycombinator.com/item?id=46379412)
> 
> 今天早上我也刚在做类似的事情。顺便说一下，你可以通过使用 \`.toBase64({ alphabet: "base64url" })\` 和 \`fromBase64({ alphabet: "base64url"})\` 来避免在 base64 字符串中进行字符串替换。
> 
> [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Refe...](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/fromBase64#alphabet)

> **gabrielsroka** • [2025-12-25](https://news.ycombinator.com/item?id=46381321)
> 
> 几年前我用电子表格做过类似的事情。它很简陋，但能用。我记得你得按 Tab 键离开输入框，然后刷新页面。
> 
> [https://gabrielsroka.github.io/webpages/calc.htm#a1:=Rate=3....](https://gabrielsroka.github.io/webpages/calc.htm#a1:=Rate=3.875;a2:=Years=30;a3:=NPer=Years*12;a4:=PV=644000;a5:=Pmt=Math.round(Math.pmt(Rate/12/100,NPer,PV)*100+1)/100;rows:5;cols:1)
> 
> ```
> https://gabrielsroka.github.io/webpages/calc.htm#a1:=Rate=3.875;a2:=Years=30;a3:=NPer=Years*12;a4:=PV=644000;a5:=Pmt=Math.round(Math.pmt(Rate/12/100,NPer,PV)*100+1)/100;rows:5;cols:1
> ```
> 
> 更多示例 https://gabrielsroka.github.io/webpages/
> 
> 大约 130 行 JavaScript 代码

> **101008** • [2025-12-25](https://news.ycombinator.com/item?id=46384376)
> 
> 我从盗版的角度来思考。如果我分享一个包含书籍的链接，DCMA 或法律监管机构会采取什么措施？他们无法要求服务器（textarea.my）删除该链接，因为它并不存在。
> 
> 他们也不能通过链接追踪每一个网站并要求被移除。
> 
> 他们能否要求 textarea.my 不解析链接，从而不显示内容？textarea.my 能否拒绝？
> 
> > **singiamtel** • [2025-12-25](https://news.ycombinator.com/item?id=46384735)
> > 
> > 我希望不是这样。受版权保护的内容似乎是那个链接，而不是应用中的任何内容。
> > 
> > 你的例子听起来像阻止记事本渲染受版权保护的内容
> > 
> > > **wavemode** • [2025-12-25](https://news.ycombinator.com/item?id=46384916)
> > > 
> > > 从技术角度来看，你完全正确。
> > > 
> > > 从监管角度来看，大多数法院可能不会认识到这种区别。在他们看来——你运营一个网站，而该网站包含受版权保护的内容。把它下架。
> > > 
> > > 你可能不得不将相关链接列入黑名单，以避免法律上的麻烦。
> 
> **tnecio** • [2025-12-25](https://news.ycombinator.com/item?id=46386970)
> 
> 在这种情况下，我会说链接 *就是* 内容本身。所以它应该是你分享链接的地方，而不是“渲染页面”，这一点更值得担忧。
> 
> **fsmv** • [2025-12-25](https://news.ycombinator.com/item?id=46384786)
> 
> 反正，即使经过压缩，一本书也无法放入 URL 中
> 
> > **badsectoracula** • [2025-12-25](https://news.ycombinator.com/item?id=46384882)
> > 
> > 另一条评论里有人提到了陀思妥耶夫斯基的《罪与罚》，所以一本书可以放进 URL 里。只是这个 URL 大约有 500000 个字符 :-P（这本书本身大约有 120 万个字符）

> **growt** • [2025-12-24](https://news.ycombinator.com/item?id=46379055)
> 
> 我最近构建了一个小框架，用于创建使用这种 URL 共享方式的 JavaScript 应用，因此不需要后端：[https://github.com/grothkopp/lost.js](https://github.com/grothkopp/lost.js)

> **rfl890** • [2025-12-25](https://news.ycombinator.com/item?id=46381430)
> 
> 你声称不进行跟踪，但页面底部却放置了一个 Cloudflare Web Analytics 信标（幸运的是被 uBlock Origin 过滤掉了）
> 
> > **gettingoverit** • [2025-12-25](https://news.ycombinator.com/item?id=46385974)
> > 
> > 从那里的问题来看，帖子的其余部分似乎也不那么真实
> > 
> > 编辑：叫我喷子吧，但... 我认识这个人！就是谷歌的那个家伙，他写的代码总是以最搞笑的方式出问题！看看他其他置顶仓库里的问题。

> **levmiseri** • [2025-12-24](https://news.ycombinator.com/item?id=46379647)
> 
> 从隐私角度来看，我真的很喜欢这一点。以至于我正在考虑在我的 [https://kraa.io](https://kraa.io) 编辑器中添加一个纯 URL 存储的解决方案作为选项。
> 
> > **omoikane** • [2025-12-24](https://news.ycombinator.com/item?id=46380172)
> > 
> > 从隐私角度来看，你可能不想使用 textarea.my，因为它在末尾包含一些跟踪位：
> > 
> > ```
> > <script defer src="https://static.cloudflareinsights.com/beacon.min.js/vcd15cbe7772f49c399c6a5babf22c1241717689176015" integrity="sha512-ZpsOmlRQV6y907TI0dKBHq9Md29nnaEIPlkf84rnaERnq6zvWvPUqr2ft8M1aS28oN72PdrCzSjY4U6VaAw1EQ==" data-cf-beacon='{"version":"2024.11.0","token":"6a22b097a2b44fa4af0a95817ce96ab5","r":1,"server_timing":{"name":{"cfCacheStatus":true,"cfEdge":true,"cfExtPri":true,"cfL4":true,"cfOrigin":true,"cfSpeedBrain":true},"location_startswith":null}}' crossorigin="anonymous"></script>
> > ```
> > 
> > > **brightbeige** • [2025-12-25](https://news.ycombinator.com/item?id=46383590)
> > > 
> > > 追踪功能不在 HTML 中，而且由于它是静态的，你可以用任何你喜欢的其他方式来托管它
> > > 
> > > [https://htmlpreview.github.io/?https://raw.githubusercontent...](https://htmlpreview.github.io/?https://raw.githubusercontent.com/antonmedv/textarea/refs/heads/master/index.html#88tXcM7JL01Jy0ksSgUA)
> 
> **wingtw** • [2025-12-26](https://news.ycombinator.com/item?id=46388533)
> 
> 开始输入 / Leaf list 设置 点击“添加标签以筛选” 输入任意字符
> 
> 然后我回到了空编辑器，只显示那一个字符
> 
> (Firefox 146.0.1 (构建 #2016132551), 86bb7f6af6312ba3c0161085f854bcdff68f1a91 GV: 146.0.1-20251217121356 AS: 146.0.2 OS: Android 14)
> 
> **WD-42** • [2025-12-24](https://news.ycombinator.com/item?id=46379888)
> 
> 从隐私角度来看，它比仅仅使用本地原生文本编辑器好在哪里？
> 
> > **levmiseri** • [2025-12-24](https://news.ycombinator.com/item?id=46380284)
> > 
> > 从纯粹的隐私角度来看，这并不理想。但是如果你还想要 Markdown 特性、自定义排版和便捷分享，这就开始变得更合理了。

> **surrTurr** • [2025-12-24](https://news.ycombinator.com/item?id=46379721)
> 
> 厚脸皮推荐：我开发了一个非常类似的东西，但没人在意：[https://github.com/AlexW00/Buffertab](https://github.com/AlexW00/Buffertab)
> 
> > **zahlman** • [2025-12-25](https://news.ycombinator.com/item?id=46384460)
> > 
> > 我很确定，今年在 Hacker News 上我见过几个类似的。
> > 
> > **antman** • [2025-12-25](https://news.ycombinator.com/item?id=46382787)
> > 
> > 语音输入是一个很酷的功能，你有没有考虑过使用 Whisper Wasm 而不是 OpenAI API？

> **qingcharles** • [2025-12-25](https://news.ycombinator.com/item?id=46386209)
> 
> 这是一个我从某处找到并优化过的书签小程序，因此没有任何远程内容：
> 
> data:text/html,<title>Notepad</title><textarea autofocus spellcheck=0 style="position:fixed;inset:0;padding:1em;border:0;font:monospace">
> 
> 你的文本实际上在 Chrome 重启后仍然存在。
> 
> 有人能想到一种将 textarea 的值存储到 URL 中的方法吗？我尝试使用 JS 设置一个 #，但在这个场景下这没什么意义。
> 
> 编辑：这是我能做到的最好的
> 
> data:text/html,<title>Notepad</title><textarea id=t autofocus spellcheck=0 style=position:fixed;inset:0;padding:2em;border:0;font:monospace></textarea><a id=s style=position:fixed;top:10px;right:10px>Right-click Open to save...</a><script>\[,P,S\]=location.href.slice(15).match(/(.*<textarea\[^>\]*\>)\[^\]*?(<\\/textarea>.*)/),t.oninput=U=\_=>s.href='data:text/html,'+P+encodeURIComponent(t.value.replace(/&/g,'&amp;').replace(/<\\/textarea/g,'&lt;/textarea'))+S,U()</script> 

> **nickweb** • [2025-12-24](https://news.ycombinator.com/item?id=46379234)
> 
> 你可能无意中发现了一种为移动设备提供额外测试的方法。
> 
> 那个叫《罪与罚》的（编辑器）持续导致我的 Brave 移动端崩溃。我猜测是 URL 长度的问题——而且我看到另一位评论员也说 Chrome 移动端有同样的问题（当然，两者使用相同的代码库，所以很可能是上游问题）。

> **ctenb** • [2025-12-24](https://news.ycombinator.com/item?id=46378889)
> 
> 我曾经做过类似的东西，专门针对吉他六线谱 [https://tabviewer.app/](https://tabviewer.app/) 为了让链接更短以便与他人分享，我使用短链接服务。粘贴长达数千字符的网址会很麻烦。
> 
> > **planb** • [2025-12-24](https://news.ycombinator.com/item?id=46379466)
> > 
> > 哇，太巧了！我刚在另一条评论里发了我的标签编辑器，现在才看到这个。我和你有相同的使用场景。
> > 
> > [https://github.com/planbnet/guitartabs](https://github.com/planbnet/guitartabs)

> **ooxoo** • [2025-12-25](https://news.ycombinator.com/item?id=46385239)
> 
> 性能问题可能是由于使用了\`text-wrap-style: pretty\`。尝试将该值切换为\`stable\`。[https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/P...](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-style#description)

> **samcollins** • [2025-12-24](https://news.ycombinator.com/item?id=46378707)
> 
> 不错！我做了一个类似的东西，但这个文本编辑器的 HTML 代码可以放在一个数据 URI 中，所以它可以作为书签或新标签页来快速记笔记
> 
> [https://gist.github.com/smcllns/8b727361ce4cf55cbc017faaefbb...](https://gist.github.com/smcllns/8b727361ce4cf55cbc017faaefbbf951)

> **nake13** • [2025-12-25](https://news.ycombinator.com/item?id=46386076)
> 
> 大约 10 天前，我开发了一个非常类似的实验并在这里分享了它（这篇帖子是中文的）：https://x.com/nake13/status/2000401664923324439
> 
> 我的重点是找到一种良好的文本→URL 别名压缩策略。我主要使用 ChatGPT-5.2-Pro 来探索和比较不同的压缩方法及权衡。

> **meander\_water** • [2025-12-25](https://news.ycombinator.com/item?id=46382307)
> 
> 很酷的项目，但是加载《罪与罚》时导致我的移动浏览器崩溃了。
> 
> 我觉得 URL 不是为那种惩罚而设计的。
> 
> > **ooxoo** • [2025-12-25](https://news.ycombinator.com/item?id=46385342)
> > 
> > 我认为这是 text-wrap-style 值。[https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/P...](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-style#pretty)

> **medv** • [2025-12-24](https://news.ycombinator.com/item?id=46378940)
> 
> 如果你错过了的话：可以通过 CSS 设置 textarea 的样式并分享它。
> 
> [https://textarea.my/#TYuxDcIwEEWpmeKUCiSIJQoKU0KFRBUWOGwnWDi...](https://textarea.my/#TYuxDcIwEEWpmeKUCiSIJQoKU0KFRBUWOGwnWDi-yHcJhClYhKWYBAua_O49_XfsWYA6F-HghjNRYMBoAa0FljE4QJEEQoBJvMkMn_drNoe8C5pbk6iPVkOfwkKp1tmh9KSQ2QkrFkxcNr5e7n5BTVHWNbY-jBqKPbXeQIWR4VQVq6nIZPrEfnCTkP3Tadhsu8dfGgqUNNyvXvLtCw==)

> **danhite** • [2025-12-25](https://news.ycombinator.com/item?id=46386688)
> 
> 买家自慎 关于长标签技术 在 iPad Safari 上...
> 
> 你可能认为 Safari 没有有效的 URL 限制（即限制非常高），但如果你曾经将地址栏中的 URL 视为可编辑的，你就有可能被悄无声息地截断到 4096 字节（例如，在地址栏中选择一个字符并替换它）
> 
> 刚才在 iPadOS 26.2 的 Safari 浏览器中，我以各种方式重新测试了潜在的缓冲区限制，结果导致我的 Safari 界面变得极其卡顿，几乎无法操作。
> 
> 例如，在将 example.com（附带约 20k 个哈希标签）保存到阅读列表后——这条回复里的每一次按键都要花几秒钟，所以我不得不强制退出 Safari 并重新输入才能发布这条警告

> **greggman65** • [2025-12-24](https://news.ycombinator.com/item?id=46380344)
> 
> 我这里有个与之略有相似的东西：[https://jsgist.org](https://jsgist.org)
> 
> 如果你点击保存，你会得到使用 URL 的选项。
> 
> 每次编辑都生成一个新的 URL 是个问题。所以你把 URL 发给朋友，然后修正一个拼写错误，他们就需要一个新的 URL。
> 
> 另一个问题当然是空间限制。

> **AltruisticGapHN** • [2025-12-25](https://news.ycombinator.com/item?id=46383662)
> 
> 我喜欢这个。这是个很棒的小 HTML 页面，用来复习 JavaScript 的。
> 
> 出于好玩，我把它输入到 ChatGPT 里，并询问是否存在 bug。
> 
> 它警告说 fromBase64()和 toBase64()在主流浏览器中不存在。虽然它得到了支持，但它确实是一个新的“2025 基准”特性。它建议使用两个小函数手动转换字符的更兼容代码。
> 
> "deflate-raw 不被一致支持。它建议改用 'deflate'。"

> **wwarren** • [2025-12-24](https://news.ycombinator.com/item?id=46378759)
> 
> 太神奇了！罪与罚的例子在我点击网址时导致我 iPhone 上的 Google Chrome 崩溃了，哈哈

> **codazoda** • [2025-12-24](https://news.ycombinator.com/item?id=46379272)
> 
> Nice! I love this.
> 
> 我以同样的思路构建了 Ponder。不过它只有 10 个文件。我没有使用 URL，没有双倍的乐趣，现在我很沮丧。
> 
> [https://github.com/codazoda/ponder](https://github.com/codazoda/ponder)

> **okaleniuk** • [2025-12-25](https://news.ycombinator.com/item?id=46384077)
> 
> 我将类似的想法用于教学：https://lnkd.in/gsySKda4
> 
> 学生有点懒，但这种“懒”是好事，所以如果整个课程内容就只是一个链接的话，他们更可能自己动手操作并与交互元素互动。

> **ciccionamente** • [2025-12-25](https://news.ycombinator.com/item?id=46385604)
> 
> 我使用了相同的原理，让人们能够以安全的方式撰写自己的紧急便条：[https://weexpire.org](https://weexpire.org)

> **zX41ZdbW** • [2025-12-25](https://news.ycombinator.com/item?id=46380956)
> 
> 几年前我就实现了同样的想法：[https://pastila.nl/](https://pastila.nl/)
> 
> > **medv** • [2025-12-25](https://news.ycombinator.com/item?id=46382766)
> > 
> > 它在后端使用数据库（DB）。

> **marcuskaz** • [2025-12-24](https://news.ycombinator.com/item?id=46378888)
> 
> 我有一个类似的使用 localStorage 的（工具） [https://github.com/mkaz/browser-pad](https://github.com/mkaz/browser-pad)

> **planb** • [2025-12-24](https://news.ycombinator.com/item?id=46379336)
> 
> 几周前，我一时兴起编写了一个吉他谱编辑器，只是想在乐队的聊天群里快速分享一个谱子。当第一个原型已经运行得很好时，我就忍不住继续添加功能，以至于现在它甚至有了鼠标悬停时显示和弦图和复制粘贴功能。
> 
> 分享的运作方式就像这里一样，通过在 URL 中编码标签页本身。
> 
> [https://github.com/planbnet/guitartabs](https://github.com/planbnet/guitartabs)

> **valgaze** • [2025-12-25](https://news.ycombinator.com/item?id=46381095)
> 
> 这让我想到: [https://hashify.me/IyBUaXRsZQ==](https://hashify.me/IyBUaXRsZQ==)

> **coder543** • [2025-12-25](https://news.ycombinator.com/item?id=46384340)
> 
> 我记得几年前很受欢迎的另一个：[https://news.ycombinator.com/item?id=17459204](https://news.ycombinator.com/item?id=17459204)

> **frizlab** • [2025-12-25](https://news.ycombinator.com/item?id=46381391)
> 
> 支持浅色/深色模式
> 
> Not really… 使用 js 动态修改 CSS 不是一个好的做法。为什么这很重要？因为“深色模式”浏览器扩展。它们通常使用@media 查询（或其他设置深色模式颜色的标准 CSS 方法），而如果是用 JS 来改变颜色，我们常常会得到不完整的深色模式，这根本不起作用。
> 
> > **medv** • [2025-12-25](https://news.ycombinator.com/item?id=46382752)
> > 
> > 不使用 JS 来处理颜色。
> > 
> > > **frizlab** • [2025-12-25](https://news.ycombinator.com/item?id=46385672)
> > > 
> > > 哦。我收回我的评论，我刚刚看了代码。我的深色模式扩展简直太烂了。

> **urbandw311er** • [2025-12-25](https://news.ycombinator.com/item?id=46380968)
> 
> 不错。但为什么要从 Markdown 标题语法自动设置标题，而它本身并不支持 Markdown？（实际上也不支持任何富文本）
> 
> > **medv** • [2025-12-25](https://news.ycombinator.com/item?id=46382771)
> > 
> > 你仍然可以写 Markdown。没有人阻止你。

> **zkmon** • [2025-12-25](https://news.ycombinator.com/item?id=46382759)
> 
> 为什么要存储在 URL 中并让它变得臃肿？本地存储难道不够吗？
> 
> > **Departed7405** • [2025-12-25](https://news.ycombinator.com/item?id=46386882)
> > 
> > 关键是你可以非常轻松地在任何地方分享它。

> **spacedoutman** • [2025-12-25](https://news.ycombinator.com/item?id=46380976)
> 
> 看起来我们都做过类似的东西。
> 
> 希望我的编辑器能凭借我设法塞进的所有额外功能脱颖而出

> **ljlolel** • [2025-12-24](https://news.ycombinator.com/item?id=46379228)
> 
> I love this.
> 
> 现在如果你也把应用代码自举到 URL 中，那么你就可以拥有一个最小内核来在 URL 中运行任何机器。
> 
> 然后你也可以以某种方式编写一个 Quine。

> **billforsternz** • [2025-12-24](https://news.ycombinator.com/item?id=46379140)
> 
> 这非常有趣，很提神，简单又巧妙，做得非常棒，一切都很好。太棒了，谢谢。

> **chuckadams** • [2025-12-25](https://news.ycombinator.com/item?id=46384509)
> 
> TypeScript 游乐场实际上也能为共享链接实现相同的功能，不过它不会在你输入时实时更新。

> **mixedmath** • [2025-12-24](https://news.ycombinator.com/item?id=46379845)
> 
> 我在 mathbin 关闭时写了一个类似的应用。它允许大约 1500 个字符的用 MathJax 显示的笔记。\[1\]
> 
> \[1\]: [https://davidlowryduda.com/mathshare/](https://davidlowryduda.com/mathshare/)

> **jerrygoyal** • [2025-12-25](https://news.ycombinator.com/item?id=46382406)
> 
> 我也做了一个（文本存储在 localStorage 中）
> 
> [https://gourav.io/devtools/notepad](https://gourav.io/devtools/notepad)

> **pglevy** • [2025-12-24](https://news.ycombinator.com/item?id=46379317)
> 
> 感谢分享！我尝试了类似的将内容嵌入 URL 的方法来开发一个家庭购物清单应用，但没能把 URL 弄得那么短。（虽然可行，但通过 WhatsApp 分享有点麻烦。）会看看能从中学到什么！
> 
> > **gisho** • [2025-12-24](https://news.ycombinator.com/item?id=46379802)
> > 
> > I created a similar app just 2 days ago targeting Whatsapp ([https://linqshare.com](https://linqshare.com)) . Context: In my locality, EA, we normally have Whatsapp groups raising funds for whatever reason; for every content edit, the admin has to copy-edit-paste updated content(which contains name and amount) to the group. This small app intends to provide a table that's easy to convey this info. App stores content in the url but a preview image (needed for Whatsapp share) is stored at R2. Let me know if you want the source code running at Cloudflare. 
> > 
> > \--edit-- 测试链接: [https://linqshare.com/#eJxtkM9KxDAQxl-lzLmHrv8Ova3IHlz04BY8F...](https://linqshare.com/#eJxtkM9KxDAQxl-lzLmHrv8Ova3IHlz04BY8FA9jO9hoki7J1GVd9ujNgwoiguDFJ_MJfITNtHXZghBC8vu-mW-SFVSEJTkPaQ7naAhiGJu6sRwOM0ZuPFzF4OqFOHKYOLSF8lFQR0kS9p_Px2DIYdxocgoD2RvwSyzICT4S-vv19tzZtSok6zAZ4FO0QkdxkiRxL72-t9KU9L2y2_7bkjO8I9vndsLLU9_LkG_nbOn3R0uPw5DSZX93yInih5swpi7lYQeDB2TK1Fwto7ZmkHyCVpHuKnb5lBRX__gvlmgFy2pTMfj-7uGTDTFCugJWrAlSyMhzlOG1li8pyRdOzVnVNkgzNHNNEYuDxREtJJNMfas8rNcbV4CUAg)

> **huhtenberg** • [2025-12-24](https://news.ycombinator.com/item?id=46379638)
> 
> 在 Firefox 中，[https://textarea.my](https://textarea.my) 显示为一个完全静态、不可操作的白色页面。只有白色，光标是默认样式。控制台中没有错误。

> **thelastgallon** • [2025-12-25](https://news.ycombinator.com/item?id=46381878)
> 
> 我想知道这个编辑器是否可以与本地 URL 缩短工具配对使用？将其与本地 URL 缩短工具结合后，可以实现通过单个字母（或非常少的字母）访问任何文档。

> **bdcravens** • [2025-12-25](https://news.ycombinator.com/item?id=46382266)
> 
> 我把它放在书签栏里，以便在需要粘贴一段快速文本时使用（但它不会持久保存）
> 
> data:text/html, <html contenteditable>
> 
> > **lifthrasiir** • [2025-12-25](https://news.ycombinator.com/item?id=46383052)
> > 
> > 如果需要持久性，请使用 xem 的版本 \[1\]:
> > 
> > ```
> > <body id=b contentEditable onload=b[i="innerHTML"]=[(l=localStorage).c] oninput=l.c=b[i]>
> > ```
> > 
> > \[1\] [https://xem.github.io/postit/](https://xem.github.io/postit/)

> **Sayyidalijufri** • [2025-12-25](https://news.ycombinator.com/item?id=46383451)
> 
> 首先我觉得它还在加载，因为只有一片白色
> 
> 但当我敲击键盘时，我可以看到它已经加载完成
> 
> Good job!

> **qbane** • [2025-12-24](https://news.ycombinator.com/item?id=46378734)
> 
> 假期期间刚开始用 CodeMirror 6 自己做一个。目前没有保存功能：[https://qbane.github.io/cgm](https://qbane.github.io/cgm)

> **sltkr** • [2025-12-24](https://news.ycombinator.com/item?id=46380141)
> 
> 由以“圣诞夜编程挑战”闻名的埃里克·沃斯特尔开发的类似工具：[https://topaz.github.io/paste/](https://topaz.github.io/paste/)

> **khalby786** • [2025-12-25](https://news.ycombinator.com/item?id=46386231)
> 
> 我们不要忘记原始的 itty.bitty.site \[0\]
> 
> \[0\]: [http://about.bitty.site/](http://about.bitty.site/)
> 
> > **blakewatson** • [2025-12-26](https://news.ycombinator.com/item?id=46390184)
> > 
> > 是的，这就是我刚才想到的那个！

> **WhyIsItAlwaysHN** • [2025-12-24](https://news.ycombinator.com/item?id=46379724)
> 
> 我自己的插件，在 SQL 方言之间进行翻译，状态存储在 URL 中，以便你可以分享它：
> 
> [https://sqlscope.netlify.app/](https://sqlscope.netlify.app/)

> **nchmy** • [2025-12-25](https://news.ycombinator.com/item?id=46384140)
> 
> 当我尝试打开《罪与罚》时，我的移动版 Chromium 浏览器会崩溃。
> 
>   Firefox 似乎可以正常工作。

> **nvahalik** • [2025-12-24](https://news.ycombinator.com/item?id=46378628)
> 
> 喜欢你的其他工具，顺便说一句！
> 
> > **medv** • [2025-12-24](https://news.ycombinator.com/item?id=46378903)
> > 
> > Thanks!

> **reconnecting** • [2025-12-24](https://news.ycombinator.com/item?id=46379735)
> 
> 这些标签 *<head>、<body> 和 </html>* 是否是故意缺失的？
> 
> Safari 15.6.1: *未处理的 Promise 拒绝: 引用错误: 找不到变量: CompressionStream*
> 
> > **wdporter** • [2025-12-24](https://news.ycombinator.com/item?id=46379823)
> > 
> > 我可能不应该擅自代表原发帖人发言，但既然它们是可选的，我觉得应该是这样，是的。

> **Yash16** • [2025-12-25](https://news.ycombinator.com/item?id=46382569)
> 
> 我喜欢这个，因为大多数时候我需要随机的东西——数字、快速搜索或者想法——而这能立即帮上忙。

> **cantalopes** • [2025-12-25](https://news.ycombinator.com/item?id=46381511)
> 
> 我觉得这更像是一个有趣的玩具项目，因为如果我每天都用它，我的浏览器历史缓存和浏览器性能就会被彻底摧毁

> **nemtsv** • [2025-12-24](https://news.ycombinator.com/item?id=46380235)
> 
> 我想几天前我在谷歌公司内网偶然发现了你的编辑器，当时我正在找一个用于格式化输出 JSON 的内部工具，世界真小 :)
> 
> > **medv** • [2025-12-25](https://news.ycombinator.com/item?id=46382780)
> > 
> > 这个 http://go/fmt-err? =) 是的，这是我的。

> **mishrapravin441** • [2025-12-25](https://news.ycombinator.com/item?id=46384622)
> 
> 对 URL 作为状态的非常好的探索。这种方法很优雅，但移动端崩溃凸显了一旦链接离开浏览器，现实世界中 URL 处理仍然是多么不友好。

> **ngc6677** • [2025-12-25](https://news.ycombinator.com/item?id=46383293)
> 
> 也在这里 [https://space-element.pages.dev/#data=eyJ2YWx1ZSI6IvCTgoAg8J...](https://space-element.pages.dev/#data=eyJ2YWx1ZSI6IvCTgoAg8JOHmiDwk4%2BfIPCTj54ifQ%3D%3D)

> **jaysonelliot** • [2025-12-24](https://news.ycombinator.com/item?id=46379223)
> 
> 用于《罪与罚》示例的 546,229 字符长度的 URL
> 
> 半兆字节的 URL。这确实是个事儿。

> **theoa** • [2025-12-24](https://news.ycombinator.com/item?id=46380678)
> 
> 这个小技巧已经完全打乱了我的下午！也许甚至永远如此。

> **xeonmc** • [2025-12-24](https://news.ycombinator.com/item?id=46378926)
> 
> 你能默认设为等宽字体吗，这样这个就能用作代码片段存储了？
> 
> > **medv** • [2025-12-24](https://news.ycombinator.com/item?id=46379037)
> > 
> > 当然！textarea.my 支持自定义样式属性：[https://textarea.my/#Ky4tSlVUyCotLlEoLUhJLElVKC6pzElVSCwpKWJ...](https://textarea.my/#Ky4tSlVUyCotLlEoLUhJLElVKC6pzElVSCwpKWJIy88r0U1LzM3MqbRSyM3Pyy8uSExOtQYA)
> > 
> > > **throwaway150** • [2025-12-24](https://news.ycombinator.com/item?id=46379499)
> > > 
> > > 之后你如何分享？我可以打开开发者工具并修改属性，但之后 URL 没有更新。
> > > 
> > > > **medv** • [2025-12-25](https://news.ycombinator.com/item?id=46382791)
> > > > 
> > > > 稍微修改一下文本以触发保存事件。
> 
> **koolala** • [2025-12-25](https://news.ycombinator.com/item?id=46384196)
> 
> 这是一个具有相同 URL 概念的代码编辑器：
> 
> [https://flems.io/](https://flems.io/)
> 
> **adamschwartz** • [2025-12-24](https://news.ycombinator.com/item?id=46378964)
> 
> 试试 [https://a10z.co/note](https://a10z.co/note)

> **edgars\_xx** • [2025-12-24](https://news.ycombinator.com/item?id=46378931)
> 
> 喜欢它，说来也巧，几周前我突然有个类似的想法，就是能够在浏览器里存储简短笔记并收藏它们，供日后查看

> **dachris** • [2025-12-25](https://news.ycombinator.com/item?id=46383613)
> 
> 压缩效果很好，你可以在里面放入很长的（低熵 ;-) 消息——这个有9000个字符：
> 
> [https://textarea.my/#7cGBAAAAAMMgzfmTHORVAQAAAAAAAADAuwE=](https://textarea.my/#7cGBAAAAAMMgzfmTHORVAQAAAAAAAADAuwE=)

> **srexrg** • [2025-12-25](https://news.ycombinator.com/item?id=46382710)
> 
> 这确实非常极简 :)

> **LordDragonfang** • [2025-12-24](https://news.ycombinator.com/item?id=46379404)
> 
> 如果 Ctrl+S 能提供将文本框内容下载到 .txt 文件的功能，那就太好了。

> **desireco42** • [2025-12-24](https://news.ycombinator.com/item?id=46379168)
> 
> 唯一缺少的是 Markdown 和几个主题。我觉得这是个很棒的分享想法。喜欢你做的这个东西。

> **sublinear** • [2025-12-24](https://news.ycombinator.com/item?id=46379097)
> 
> 我喜欢这类项目，但添加文件导出/导入功能是不可避免的。这与其说是 URL 的限制，不如说是实用性的问题。
> 
> 我也无法确认 URL 是否会在服务器端被记录，所以我绝不会相信“不跟踪”的说法。这就是为什么这些项目最终也会选择自托管。
> 
> > **denisinvader** • [2025-12-24](https://news.ycombinator.com/item?id=46379161)
> > 
> > URL 的哈希部分仅在浏览器中可用，据我所知，服务器无法获取#的值
> > 
> > > **jamesdwilson** • [2025-12-24](https://news.ycombinator.com/item?id=46379652)
> > > 
> > > 服务器很容易故意（或因被入侵）添加一行代码来发送哈希文本。
> > > 
> > > **sublinear** • [2025-12-24](https://news.ycombinator.com/item?id=46379232)
> > > 
> > > 不过拼写错误和 URL 变形很常见，而且在那种情况下，我仍然无法确认是否被记录。这不在 GitHub 源代码的任何部分的范围内，而是取决于托管该页面的服务器。我知道这并不意味着它会非常安全，但仍然值得一提。
> > > 
> > > > **throwaway150** • [2025-12-24](https://news.ycombinator.com/item?id=46379544)
> > > > 
> > > > Typos aren't making the hash part turn into something else. Like your parent comment explained to you, the hash part is not sent to the server. If you go out of your way to mangle the URL then of course a mangled URL without hash will likely get logged to the server. But I'm not sure how one would manage to go so much out of the way that they mangle the URL in a way that removes the hash. 
> > > > 
> > > > > **sublinear** • [2025-12-24](https://news.ycombinator.com/item?id=46380315)
> > > > > 
> > > > > 在某些应用中粘贴链接时，你没有选择的余地。它们可能会剥离查询参数和哈希部分、进行百分号编码、强制使用 URL 缩短服务等。
> > > > > 
> > > > > 百分号编码尤其糟糕，因为它还可能增加 URL 长度，导致截断和解压失败。URL 中存在没完没了的坑。

> **ThrowawayTestr** • [2025-12-24](https://news.ycombinator.com/item?id=46379069)
> 
> [https://textarea.my/#Cy4tsAcA](https://textarea.my/#Cy4tsAcA)
> 
> > **teach** • [2025-12-24](https://news.ycombinator.com/item?id=46379115)
> > 
> > [https://textarea.my/#Cy4tsOfi8ssvUcgtTc7QU\_DIz0stLsmpVPBUSK0...](https://textarea.my/#Cy4tsOfi8ssvUcgtTc7QU_DIz0stLsmpVPBUSK0oSE0uSU1RSFQoykzOLsrPydHj4gIA)
> > 
> > > **medv** • [2025-12-24](https://news.ycombinator.com/item?id=46379160)
> > > 
> > > [https://textarea.my/#ZY\_NTgMhFIVd9ylYNZpMuQwDmZ9m4qM0SG9ncCg...](https://textarea.my/#ZY_NTgMhFIVd9ylYNZpMuQwDmZ9m4qM0SG9ncCggXNro0xujcaG7c76z-c7DjjHGXozdlhxrOE-sZv-4EqUyASRv6BLzldOKN8wLchuvcE8HGwNhIKjJR3MuUBxhAQl2jbmWX_xdT6YUJLg4jyBl18pej5Cd3XL0_qQ2_pqW57dqvKP3eRT7Qtml2Xi_tzmmWTSt4L0alRqUFr3smlaIph-4Fm0rOjEOWqun458jh-I-cGJfosaFf2vGhIYmFuJPPO4-AQ==)
> > > 
> > > > **RonanSoleste** • [2025-12-24](https://news.ycombinator.com/item?id=46380394)
> > > > 
> > > > [https://textarea.my/#ZY87b8MgFIU7-1fQJWqlBDDG8iOyOnfvHlF8Y6g...](https://textarea.my/#ZY87b8MgFIU7-1fQJWqlBDDG8iOyOnfvHlF8Y6gJELikan9904c6tN90Hss5VfXFk1F-zbfkkXiAGWaCRuFNRa48K70uKRQ_j6Qkd2cQYx4Zi07hMaQTRQMXSAtQHU7sNe508AgeWYkuqDmzbBEyE0ybkEr-jb_tQeUMyI7WAROiqUXXDixZvabg3EGu9CUuD-einMW3aeCbjMnGSTm30SnEiW9rTjs5SNnLlneiuXq-7Xra8rrmDR_6tpX3-z9Hdtm-w0g-hyrr_7UJIigciQ8_cl99AA==)

> **mzelling** • [2025-12-24](https://news.ycombinator.com/item?id=46378855)
> 
> Love it!

> **deafpolygon** • [2025-12-24](https://news.ycombinator.com/item?id=46378632)
> 
>   你能保存任何东西吗？
> 
> > **rorylawless** • [2025-12-24](https://news.ycombinator.com/item?id=46378702)
> > 
> > [https://textarea.my/#i0wtBgA=](https://textarea.my/#i0wtBgA=)
> > 
> > > **sltkr** • [2025-12-24](https://news.ycombinator.com/item?id=46379639)
> > > 
> > > 不，应该是这个：[https://textarea.my/#c8yrLMnIzEsHAA==](https://textarea.my/#c8yrLMnIzEsHAA==)
> > > 
> > > > **RonanSoleste** • [2025-12-24](https://news.ycombinator.com/item?id=46380407)
> > > > 
> > > > 更像是：[https://textarea.my/#c8yrLMnIzEu3BwA=](https://textarea.my/#c8yrLMnIzEu3BwA=)
> 
> **thomascgalvin** • [2025-12-24](https://news.ycombinator.com/item?id=46378701)
> 
> 不是楼主：好的，直接加书签就行
> 
> > **tony\_cannistra** • [2025-12-24](https://news.ycombinator.com/item?id=46378712)
> > 
> > 有点——不过每次更新的时候你就得重新收藏它...
> > 
> > > **medv** • [2025-12-24](https://news.ycombinator.com/item?id=46378908)
> > > 
> > > 它也会保存到 localStorage

> **rane** • [2025-12-24](https://news.ycombinator.com/item?id=46379791)
> 
> 现在要是它不会污染浏览器历史记录会怎么样？