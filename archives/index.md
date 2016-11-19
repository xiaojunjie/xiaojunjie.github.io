---
title: 归档
layout: default
---

<div class="archives">
{% assign loopindex = 0 %}
{% assign yeartime = 0 %}

{% for post in site.posts %}
{% capture y %}{{post.date | date:"%Y"}}{% endcapture %}
{% if year != y %}
  {% assign loopindex = 0 %}
  {% if yeartime != 0 %}
    {% if rowfinder == 1 %}
      </div>
    {% endif %}
  {% endif %}
  {% assign year = y %}
  <h2>{{ y }}</h2>
{% endif %}
{% assign yeartime = yeartime | plus: 1 %}

{% assign loopindex = loopindex | plus: 1 %}
{% assign rowfinder = loopindex | modulo: 2 %}
{% if rowfinder == 1 %}
  <div class="row">
    <div class="col-md-6">
      <time datetime="{{ post.date | date:"%m-%d" }}">{{ post.date | date:"%m-%d" }}</time>&nbsp;&nbsp;
      <a href="{{ post.url }}" title="{{ post.title }}">{{ post.title }}</a>
    </div>
  {% else %}
    <div class="col-md-6">
      <time datetime="{{ post.date | date:"%m-%d" }}">{{ post.date | date:"%m-%d" }}</time>&nbsp;&nbsp;
      <a href="{{ post.url }}" title="{{ post.title }}">{{ post.title }}</a>
    </div>
  </div>
{% endif %}
{% endfor %}
{% if rowfinder != 0 %}
      </div>
{% endif %}
</div>
