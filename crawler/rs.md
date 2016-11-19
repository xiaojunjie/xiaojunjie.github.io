---
title: 睿思
layout: default
---

<div class="module cl ml">
<ul>
{% for img in site.data.rs limit:15 offset:3 %}
  <li style="float: left">
    <a href="http://rs.xidian.edu.cn/{{ img.link }}" target="_blank">
      <img src="{{ img.src }}" width="215" height="225">
    </a>
    <p>{{ img.title }} </p>
  </li>
{% endfor %}
</ul>
</div>
