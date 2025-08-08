---
layout: default
title: "我的笔记列表"
---
# 笔记列表

<ul class="post-list">
  {% comment %} 
    site.clippings 默认按日期升序, 我们需要降序 (最新的在前面), 所以使用 reverse 过滤器 
  {% endcomment %}
  {% assign sorted_notes = site.clippings | reverse %}
  {% for note in sorted_notes %}
    <li>
      <span class="post-meta">{{ note.date | date: "%Y-%m-%d" }}</span>
      <h3>
        <a class="post-link" href="{{ note.url | relative_url }}">{{ note.title }}</a>
      </h3>
    </li>
  {% endfor %}
</ul>