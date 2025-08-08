---
layout: default
title: "我的笔记列表"
---

# 笔记列表

这里是我的所有笔记，按照最新发布的顺序排列。

<ul class="post-list">
  {% for post in site.Clippings %}
    <li>
      <span class="post-meta">{{ post.date | date: "%Y-%m-%d" }}</span>
      <h3>
        <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
      </h3>
    </li>
  {% endfor %}
</ul>