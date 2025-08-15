---
layout: main
title: "我的笔记列表"
---

{%- comment -%}
步骤 1: 【分组】我们不再直接排序，而是先按一个标准化的日期字符串进行分组。
`date: '%Y-%m-%d %H:%M:%S'` 会将所有日期格式（无论带不带时间）都统一转换成一个
可以按字典序正确排序的字符串。无效的日期会返回空字符串，自动被忽略。
{%- endcomment -%}
{%- assign notes_grouped_by_time = site.clippings | group_by_exp: "item", "item.created | date: '%Y-%m-%d %H:%M:%S'" -%}

{%- comment -%}
步骤 2: 【排序】我们对这些“组”进行排序。因为组的 `name` 属性现在是标准化的日期字符串，
所以 `sort: 'name'` 是绝对安全的，并且能得到正确的时序。
{%- endcomment -%}
{%- assign sorted_groups = notes_grouped_by_time | sort: 'name' | reverse -%}

{%- comment -%}
步骤 3: 【重组】我们将排好序的组重新展开，得到一个最终的、正确排序的笔记列表。
{%- endcomment -%}
{%- assign sorted_notes = "" | split: "" -%}
{%- for group in sorted_groups -%}
  {%- for note in group.items -%}
    {%- assign sorted_notes = sorted_notes | push: note -%}
  {%- endfor -%}
{%- endfor -%}

<!-- 步骤 4: 【安全分组】现在，对这个绝对干净且排好序的列表进行按月份分组 -->
{%- assign notes_by_month = sorted_notes | group_by_exp: "note", "note.created | date: '%Y-%m'" -%}

<!-- 内容容器 -->
<div class="content-container">
  {% for month in notes_by_month %}
    <div id="content-{{ month.name }}" class="month-content-panel">
      <ul class="post-list">
        {% assign current_day = "" %}
        {% for note in month.items %}
          {% assign note_day = note.created | date: "%d" %}
          {% if note_day != current_day %}
            <h3 class="day-group">{{ note.created | date: "%-d 日" }}</h3>
            {% assign current_day = note_day %}
          {% endif %}
          <li class="note-item">
            <div class="note-title"><a href="{{ note.url | relative_url }}">{{ note.title | default: "无标题笔记" }}</a></div>
            <div class="note-details">
              {% if note.author and note.author != "" %}
                <span>✍️ 
                {%- if note.author contains '[' -%}
                  {{ note.author | join: ', ' | remove: '[[' | remove: ']]' }}
                {%- else -%}
                  {{ note.author }}
                {%- endif -%}
                </span>
              {% endif %}
              {% if note.source %}<span>🔗 <a href="{{ note.source }}" target="_blank" rel="noopener noreferrer">来源链接</a></span>{% endif %}
            </div>
            {% if note.tags and note.tags != "" %}
              <div class="note-tags">
                {%- assign tag_string = note.tags | join: ' ' -%}
                {%- assign tag_list = tag_string | split: ' ' -%}
                {%- for tag in tag_list -%}
                  {%- if tag != "" and tag != "#" -%}
                    <a href="#" class="tag">{{ tag }}</a>
                  {%- endif -%}
                {%- endfor -%}
              </div>
            {% endif %}
          </li>
        {% endfor %}
      </ul>
    </div>
  {% endfor %}
</div>