---
title: "信息分层设计在 Claude Skills 中的运用"
source: "https://x.com/yan5xu/status/1989171335818600488"
author:
  - "[[@yan5xu]]"
published: 2025-11-14
created: 2025-11-14
description:
tags:
  - "@yan5xu # 信息分层设计 # LOD # AI Agent # 渲染 # 级别详细度"
---
**yan5xu** @yan5xu [2025-11-14](https://x.com/yan5xu/status/1989171335818600488)

claude skills 有个没怎么被看到的点，就是信息分层设计。首先用元信息替代完整信息，离当前任务距离越远，展示的细节越少。其次是按需加载，skills 基于 markdown+grep，就搭建出一套简单但非常有用的按需加载层。真的是非常优雅。

![Pyramid diagram divided into three colored layers from bottom to top: orange LOD-2 at base labeled 检索 with folder icon and text 基于 Token (100%), blue LOD-1 middle labeled 检索 with gear icon and text 基于 Token (20-80%), green LOD-0 top labeled Agent with search icon and text 基于 Token (1%).](https://pbs.twimg.com/media/G5r0o9EacAA0zB3?format=jpg&name=large)

---

**yan5xu** @yan5xu [2025-11-14](https://x.com/yan5xu/status/1989172813748642300)

这些在 3D 游戏中非常常见。游戏渲染的时候，会根据对象和摄像机的距离，选择不同的 LOD （Level of Detail）模型，降低渲染面数；对一些场景，比如塞尔达中的神庙，也只有在进入的时候，才进行渲染。

详细内容，我写在文章「从《塞尔达传说》到AI Agent：Claude Skills背后的信息分层设计哲学」中了

![Image](https://pbs.twimg.com/media/G5r1-O6a4AA_n3E?format=jpg&name=large)

---

**Victor Renard** @valent44355

Huge updates ! Rumors Earnings will be better than expected for NASDAQ\_NXXT  
重大更新！传闻纳斯达克\_NXXT 的收益将超出预期

---

**AIFUNS（海外账号，Claude镜像，ChatGPT充值）** @yinim276484 [2025-11-14](https://x.com/yinim276484/status/1989184065040445460)

看起来不错