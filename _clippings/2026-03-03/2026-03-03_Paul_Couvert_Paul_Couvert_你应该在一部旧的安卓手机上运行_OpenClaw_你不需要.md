---
title: "2026-03-03_Paul_Couvert_Paul_Couvert_你应该在一部旧的安卓手机上运行_OpenClaw_你不需要"
source: "https://x.com/itsPaulAi/status/2028213201519640823"
author:
  - "[[@Paul Couvert]]"
published: 2026-03-03
created: 2026-03-03
description:
tags:
  - "x"
  - "@Paul Couvert"
  - "bash"
  - "picoclaw"
---

# Paul Couvert # 你应该在一部旧的安卓手机上运行 OpenClaw。 你不需要

**Paul Couvert**

# 你应该在一部旧的安卓手机上运行 OpenClaw。

你不需要 Mac Mini 来运行你的 AI 代理。

我在一部旧的安卓手机上，通过 Termux 运行了 PicoClaw（OpenClaw 的轻量级替代品），过程出奇地简单：

并非像 YouTube 演示视频里那样“简单”。更像是：先让人烦躁一个小时，然后就变得扎实了。

- 比 Mac Mini 便宜多了
- 随时可通过 Telegram 联系
- 出乎意料地比 OpenClaw 快

> 不，你不需要 Mac Mini 就能运行 OpenClaw。 实际上，你可以在一部旧安卓手机上托管你需要的一切。 你将拥有如下设置： 速度快得多 便宜得多 - 具有相同的功能 即使是25美元的手机也能胜任这项工作。
> 
> — Paul Couvert
> 
> [https://x.com/itsPaulAi/status/2025681978973094104](https://x.com/itsPaulAi/status/2025681978973094104)

以下是实际奏效的设置。

## 先从 Termux 开始，不要用快捷键。

请务必从 F-Droid 或使用 apk 文件安装 Termux 应用。 官方 GitHub 仓库。

首先，授予 Termux 存储访问权限并安装一些繁琐的组件：

```bash
termux-setup-storage
pkg update && pkg upgrade -y
pkg install -y wget proot ca-certificates openssl nano jq
```

\`ca-certificates\` 这行代码比人们想象的更重要。如果省略它，就会导致典型的 TLS 错误：代理无法验证 API 证书，即使你的密钥没问题，整个过程看起来也会出错。

然后检查您的手机架构：

```bash
uname -m
```

如果显示的是 \`aarch64\`，那么你需要的是 ARM64 架构的 PicoClaw 二进制文件。这适用于大多数安卓手机。

将二进制文件放在一个合理的位置。

请将真正的二进制文件保存在您的用户主目录中，不要放在共享存储上。

Android 喜欢让 \`/sdcard\` 用起来很方便，直到它阻塞程序执行为止。

我使用了类似这样的简单布局：

```bash
mkdir -p ~/bin && cd ~/bin
wget -O picoclaw https://github.com/sipeed/picoclaw/releases/download/v0.2.0/picoclaw-linux-arm64
chmod +x picoclaw
```

然后初始化 PicoClaw：

```bash
termux-chroot ~/picoclaw-linux-arm64 onboard
```

这样就能创建配置和工作区，避免你编辑尚不存在的随机文件。

## 真正重要的改变只有一个：通过 OpenRouter 使用 MiniMax M2.5

很多人都住在克劳德奥普斯岛，那里的住宿费用要贵得多。

比较干净的做法是将 PicoClaw 指向 OpenRouter，然后在 OpenRouter 中选择 MiniMax M2.5。

打开 \`~/.picoclaw/config.json\` 文件，并使用以下内容作为核心模型设置：

```bash
nano ~/.picoclaw/config.json
```

```json
{
  "agents": {
 "defaults": {
 "model": "minimax/minimax-m2.5"
 }
  },
  "providers": {
 "openrouter": {
 "api_key": "sk-or-v1-..."
 }
  }
}
```

这是大多数人忽略的关键一点。

并非因为它很复杂。

因为流传的旧示例仍然会引导人们使用旧版提供商配置，然后他们就会疑惑为什么代理总是调用错误的后端。

如果您特别想要 MiniMax M2.5 开关，那么就是这款。

## 一次性修复 TLS 问题，无需每次都修复。

如果你曾经遇到过证书错误，不要一直粘贴一次性的环境变量。

妥善包装。

创建一个小型启动脚本：

```bash
mkdir -p ~/bin
cat > ~/bin/picoclaw <<'EOF'
#!/data/data/com.termux/files/usr/bin/sh
export SSL_CERT_FILE=/etc/tls/cert.pem
export REQUESTS_CA_BUNDLE=/etc/tls/cert.pem
exec termux-chroot "$HOME/picoclaw-linux-arm64" "$@"
EOF
chmod +x ~/bin/picoclaw
```

然后确保 \`~/bin\` 已添加到您的 PATH 环境变量中：

```bash
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

这是另一个让我犯错的小错误。脚本确实存在，只是 shell 看不到它。

完成上述步骤后，您就可以像使用普通命令一样使用 PicoClaw 了：

```bash
picoclaw agent -m "Hello there!"
```

是的，如果问题能够永久解决，感觉会好得多。

## 在进行更复杂的操作之前，先测试一下代理。

在尝试将其设置为“始终开启”之前，请确保核心循环正常工作：

```bash
picoclaw agent -m "Write a tiny hello-world in Python and explain it."
```

## 如果您希望始终访问聊天功能，请运行网关。

代理程序运行正常后，下一步就是网关：

```bash
picoclaw gateway
```

我肯定会先手动测试一下。一直都是这样。

试图将一个损坏的系统守护进程化是没有意义的。先建立一个干净的会话，确认它能稳定运行，然后再进行自动化。

这样的顺序可以避免很多麻烦。

## 最令我惊讶的是

整件事最奇怪的地方在于，一旦运行起来，感觉就非常正常。

一部老旧的安卓手机。一个终端应用。一个轻量级的代理程序。一个合适的模型选择。

就是这样。

没有华丽的布景，没有昂贵的机器在桌面上嗡嗡作响，也没有为了证明自己“认真”而过度配置的设备。

一部真正能干活的手机。

说实话，我认为人们仍然低估了这一点。

“人工智能演示”和“实用个人代理”之间的差距正在迅速缩小。

有时候它小到可以放进口袋！

* * *

### 热门回复

**@Feb 23** ♥ 840 · 💬 87

不，你不需要 Mac Mini 就能运行 OpenClaw。 实际上，你可以在一部旧安卓手机上托管你需要的一切。 你将拥有如下设置： 速度快得多 便宜得多 - 具有相同的功能 即使是25美元的手机也能胜任这项工作。