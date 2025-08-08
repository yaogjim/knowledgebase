---
title: "智能体安全 - LLM 安全扫描器！"
source: "https://x.com/kieranklaassen/status/1930032748951154966"
author:
  - "[[@kieranklaassen]]"
created: 2025-06-04
description:
tags:
  - "@kieranklaassen #LLM安全 #智能体安全 #安全扫描器"
---
**Kieran Klaassen** @kieranklaassen [2025-06-03](https://x.com/kieranklaassen/status/1930032748951154966)

  
我如何使用 git 工作树并行运行多个 Claude 代码代理。如果有更好的方法请评论 :)\`\`\`

函数 wt() {

git 工作树添加 ../工作树/$1 主分支

进入上级目录下的 worktrees/$1 目录并在后台执行 git checkout -b $1 命令

}

在幕后发生了什么：

• \`git worktree add\` 创建一个链接的工作目录

• 同一个.git 仓库，完全独立的工作文件

• 切换任务时无需贮藏或提交

• 每个工作树可以运行不同的代码状态

示例：\`wt feature-auth\` 创建：

\`\`\`我的应用/

\`\`\`

├──.git/ （共享仓库）

├── 源文件/ （主工作树）

└── ../../工作树/

└── 功能认证/ （独立工作树）

└── src/ （独立的工作文件）\`\`\`清理函数以精准无误的方式移除所有工作树：\`\`\`bash

函数 wtc() {

git 工作树列表 --瓷质格式 |

grep -B2 "分支引用/头部/" |

grep "工作树" |

使用制表符分隔，取第二列 |

xargs -I {} git worktree remove {}

}

管道故障：

• \`list --porcelain\` → 机器可读格式

• \`grep -B2\` → 捕获分支信息上方的工作树路径

• \`cut -d' ' -f2\` → 仅提取路径

• \`xargs\` → 干净利落地移除每个工作树

为何这会带来彻底改变：

1\. 在处理问题#123 时运行 Claude，同时另一个进程处理拉取请求#456

2\. 无需上下文切换——每个代理都有自己的文件系统

3\. 在不影响主工作区的情况下测试重大变更

4\. 同时编译不同版本

为此专门构建了 Git 工作树。一个仓库，多个工作目录。非常适合并行 AI 开发。