---
title: 肖俊杰
layout: default
---

<div class="row">
    <div class="col-md-9">
        {% for post in site.posts limit:7 %}
        <div class="article">
            <h1><a href="{{ post.url }}">{{ post.title }}</a></h1>
            <div class="date">{{ post.date | date_to_string }}</div>
            <p class="abstract">
              {{ post.content | strip_html | truncatewords:20 }}
            </p>
            <p class="full-article"><a href="{{ post.url }}">Read more...</a></p>
        </div>
        {% endfor %}
        <div class="article" >
          <h1 style="border:none;"><a href="/archives/">查看所有文档 →</a></h1>
        </div>
    </div>
    <div class="col-md-3">
        {% include sidebar.html %}
    </div>
</div>