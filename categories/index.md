---
title: 分类
layout: default
---

<div class="categories">
  {% for cat in site.categories %}
    <h2>{{ cat[0] }} ( {{ cat[1].size }} )</h2>
    {% for post in cat[1] %}
      <div class="list">
        <time datetime="{{ post.date | date:"%Y-%m-%d" }}">{{ post.date | date:"%Y-%m-%d" }}</time>&nbsp;&nbsp;
        <a href="{{ post.url }}" title="{{ post.title }}">{{ post.title }}</a>
      </div>
    {% endfor %}
  {% endfor %}
</div>
