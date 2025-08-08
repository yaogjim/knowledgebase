---
layout: default
title: "我的笔记列表"
---

<style>
  /* 确保我们的布局在简洁的画布上正常工作 */
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji"; }
  .wrapper { max-width: 960px; margin: 0 auto; padding: 20px; }
  
  .top-nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-bottom: 15px;
    border-bottom: 1px solid #ddd;
    margin-bottom: 30px;
  }
  .top-nav h1 {
      margin: 0;
      font-size: 1.8em;
  }
  .dropdown { position: relative; display: inline-block; }
  .dropdown-button {
    background-color: #333;
    color: white;
    padding: 10px 15px;
    border: none;
    cursor: pointer;
    border-radius: 5px;
    font-size: 0.9em;
  }
  .dropdown-content {
    display: none;
    position: absolute;
    right: 0;
    background-color: #f9f9f9;
    min-width: 180px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1;
    border-radius: 5px;
    overflow: hidden;
  }
  .dropdown-content a { color: black; padding: 12px 16px; text-decoration: none; display: block; }
  .dropdown-content a:hover { background-color: #f1f1f1; }
  
  /* 内容样式 */
  .post-list { list-style: none; padding-left: 0; }
  .month-group { margin-top: 20px; padding-top: 10px; font-size: 1.5em; }
  .day-group { margin-top: 30px; border-bottom: 1px solid #eee; padding-bottom: 10px; font-size: 1.2em; color: #444; }
  .note-item { list-style-type: '▸'; margin-left: 20px; padding-left: 10px; margin-bottom: 20px; }
  .note-title a { text-decoration: none; font-weight: bold; color: #333; font-size: 1.1em; }
  .note-details { font-size: 0.9em; color: #777; padding-left: 20px; margin-top: 5px; }
  .note-details span { margin-right: 15px; }
  .note-tags { margin-top: 8px; padding-left: 20px; }
  .tag {
    display: inline-block; background-color: #f0f0f0; color: #555;
    padding: 4px 10px; border-radius: 15px; font-size: 0.9em;
    margin-right: 6px; margin-bottom: 8px; text-decoration: none;
    border: 1px solid #e0e0e0;
  }
</style>

{% assign sorted_notes = site.clippings | reverse %}

<header class="top-nav">
  <h1>我的知识库</h1>
  <div class="dropdown" id="archive-dropdown">
    <button class="dropdown-button">按月份归档 ▼</button>
    <div class="dropdown-content">
      {% assign months = sorted_notes | map: 'created' | map: '%Y-%m' | uniq %}
      {% for month_code in months %}
        <a href="#month-{{ month_code }}">{{ month_code | date: "%Y 年 %B" }}</a>
      {% endfor %}
    </div>
  </div>
</header>

{% assign current_month = "" %}
{% assign current_day = "" %}
<div class="post-list">
  {% for note in sorted_notes %}
    {% assign note_month_code = note.created | date: "%Y-%m" %}
    {% if note_month_code != current_month %}
      <h2 class="month-group" id="month-{{ note_month_code }}">{{ note.created | date: "%Y 年 %B" }}</h2>
      {% assign current_month = note_month_code %}
      {% assign current_day = "" %}
    {% endif %}
    {% assign note_day = note.created | date: "%d" %}
    {% if note_day != current_day %}
      <h3 class="day-group">{{ note.created | date: "%-d 日" }}</h3>
      {% assign current_day = note_day %}
    {% endif %}
    <li class="note-item">
      <div class="note-title"><a href="{{ note.url | relative_url }}">{{ note.title | default: "无标题笔记" }}</a></div>
      <div class="note-details">
        {% if note.author %}<span>✍️ {{ note.author | join: ', ' | remove: '[[' | remove: ']]' }}</span>{% endif %}
        {% if note.source %}<span>🔗 <a href="{{ note.source }}" target="_blank" rel="noopener noreferrer">来源链接</a></span>{% endif %}
      </div>
      {% if note.tags %}<div class="note-tags">{% assign tag_list = note.tags | first | split: ' ' %}{% for tag in tag_list %}{% if tag != "" and tag != "#" %}<span class="tag">{{ tag }}</span>{% endif %}{% endfor %}</div>{% endif %}
    </li>
  {% endfor %}
</div>

<script>
  document.addEventListener('DOMContentLoaded', function() {
    const dropdown = document.getElementById('archive-dropdown');
    if (!dropdown) return;
    const button = dropdown.querySelector('.dropdown-button');
    const content = dropdown.querySelector('.dropdown-content');
    
    button.addEventListener('click', function(event) {
      content.style.display = content.style.display === 'block' ? 'none' : 'block';
      event.stopPropagation();
    });

    document.addEventListener('click', function(event) {
      if (content.style.display === 'block' && !dropdown.contains(event.target)) {
        content.style.display = 'none';
      }
    });

    content.addEventListener('click', function() {
        content.style.display = 'none';
    });
  });
</script>