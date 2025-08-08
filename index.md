---
layout: default
title: "我的笔记列表"
---

<style>
  /* 为了让列表更好看，这里直接内嵌了一些简单的 CSS 样式 */
  .post-list { list-style: none; padding-left: 0; }
  .note-item { border-bottom: 1px solid #eee; padding: 20px 0; }
  .note-item:last-child { border-bottom: none; }
  .note-title { margin-top: 0; margin-bottom: 5px; }
  .note-title a { text-decoration: none; color: #333; }
  .note-title a:hover { text-decoration: underline; }
  .note-meta { font-size: 0.9em; color: #777; margin-bottom: 10px; }
  .note-meta span { margin-right: 15px; }
  .note-description { color: #555; margin-top: 10px; }
  .note-tags { margin-top: 15px; }
  .tag {
    display: inline-block;
    background-color: #f0f0f0;
    color: #555;
    padding: 3px 8px;
    border-radius: 12px;
    font-size: 0.8em;
    margin-right: 5px;
    margin-bottom: 5px;
    text-decoration: none;
  }
</style>

# 笔记列表

<ul class="post-list">
  {% assign sorted_notes = site.clippings | reverse %}
  {% for note in sorted_notes %}
    <li class="note-item">
      <h3 class="note-title">
        <a href="{{ note.url | relative_url }}">{{ note.title | default: "无标题笔记" }}</a>
      </h3>

      <div class="note-meta">
        <span>🗓️ {{ note.created | date: "%Y-%m-%d" }}</span>
        
        {% if note.author %}
          <span>✍️ 
            {% assign author_string = note.author | join: ', ' | remove: '[[' | remove: ']]' %}
            {{ author_string }}
          </span>
        {% endif %}

        {% if note.source %}
          <span>🔗 <a href="{{ note.source }}" target="_blank" rel="noopener noreferrer">来源链接</a></span>
        {% endif %}
      </div>

      {% if note.description and note.description != "" %}
        <p class="note-description">{{ note.description }}</p>
      {% endif %}

      {% if note.tags %}
        <div class="note-tags">
          {% assign tag_string = note.tags | first %}
          {% assign tag_list = tag_string | split: ' ' %}
          {% for tag in tag_list %}
            {% if tag != "" %}
              <span class="tag">{{ tag }}</span>
            {% endif %}
          {% endfor %}
        </div>
      {% endif %}
    </li>
  {% endfor %}
</ul>