---
layout: default
title: "我的笔记列表"
---

<style>
  .container { display: flex; gap: 30px; }
  .sidebar { width: 200px; flex-shrink: 0; font-size: 0.9em; }
  .main-content { flex-grow: 1; }
  .sidebar h3 { font-size: 1.2em; border-bottom: 1px solid #ddd; padding-bottom: 5px; margin-top: 0; }
  .sidebar ul { list-style: none; padding: 0; margin: 0 0 20px 0; }
  .sidebar ul li a { text-decoration: none; color: #007bff; }
  .sidebar .tag-cloud a { 
    display: inline-block; background-color: #f0f0f0; color: #555;
    padding: 3px 8px; border-radius: 12px; font-size: 0.9em;
    margin-right: 5px; margin-bottom: 5px; text-decoration: none;
  }
  /* 右侧内容样式 */
  .post-list { list-style: none; padding-left: 0; }
  .month-group { margin-top: 0; padding-top: 10px; } /* padding-top 用于锚点定位偏移 */
  .day-group { margin-top: 30px; border-bottom: 1px solid #eee; padding-bottom: 15px; }
  .note-item { list-style-type: '▸'; margin-left: 20px; padding-left: 10px; margin-bottom: 15px; }
  .note-title a { text-decoration: none; font-weight: bold; color: #333; }
  .note-details { font-size: 0.9em; color: #777; padding-left: 20px; }
  .note-tags { margin-top: 5px; padding-left: 20px; }
</style>

{% assign sorted_notes = site.clippings | reverse %}

<div class="container">
  <aside class="sidebar">
    <h3>归档</h3>
    <ul>
      {% assign months = sorted_notes | map: 'created' | map: '%Y-%m' | uniq %}
      {% for month_code in months %}
        {% assign month_display = site.time | date: "1970-01-01" | date: "%Y-%m" | replace: month_code, "" | date: "%B %Y" %}
         <li><a href="#month-{{ month_code }}">{{ month_code | date: "%B %Y" }}</a></li>
      {% endfor %}
    </ul>

    <h3>标签</h3>
    <div class="tag-cloud">
      {% assign all_tags = "" %}
      {% for note in sorted_notes %}
        {% if note.tags %}
          {% assign tag_string = note.tags | first | append: " " %}
          {% assign all_tags = all_tags | append: tag_string %}
        {% endif %}
      {% endfor %}
      {% assign unique_tags = all_tags | split: " " | uniq %}
      {% for tag in unique_tags %}
        {% if tag != "" and tag != "#" %}
          <a>{{ tag }}</a>
        {% endif %}
      {% endfor %}
    </div>
  </aside>

  <main class="main-content">
    <h1>笔记列表</h1>
    {% assign current_month = "" %}
    {% assign current_day = "" %}
    <div class="post-list">
      {% for note in sorted_notes %}
        {% assign note_month_code = note.created | date: "%Y-%m" %}
        {% if note_month_code != current_month %}
          <h2 class="month-group" id="month-{{ note_month_code }}">{{ note.created | date: "%B %Y" }}</h2>
          {% assign current_month = note_month_code %}
          {% assign current_day = "" %}
        {% endif %}
        {% assign note_day = note.created | date: "%d" %}
        {% if note_day != current_day %}
          <h3 class="day-group">{{ note.created | date: "%B %-d" }}</h3>
          {% assign current_day = note_day %}
        {% endif %}
        <li class="note-item">
          <div class="note-title"><a href="{{ note.url | relative_url }}">{{ note.title | default: "无标题笔记" }}</a></div>
          <div class="note-details">
            {% if note.author %}<span>✍️ {{ note.author | join: ', ' | remove: '[[' | remove: ']]' }}</span>{% endif %}
            {% if note.source %}<span>🔗 <a href="{{ note.source }}" target="_blank">来源链接</a></span>{% endif %}
          </div>
          {% if note.tags %}<div class="note-tags">{% assign tag_list = note.tags | first | split: ' ' %}{% for tag in tag_list %}{% if tag != "" and tag != "#" %}<a class="tag">{{ tag }}</a>{% endif %}{% endfor %}</div>{% endif %}
        </li>
      {% endfor %}
    </div>
  </main>
</div>