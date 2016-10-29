---
title: 睿思
layout: default
---

<ul>
{% for img in site.data.rs limit:15 %}
  <li>
    <a href="http://rs.xidian.edu.cn/forum.php?mod=forumdisplay&fid=106/{{ img.link }}">
      <img src="http://rs.xidian.edu.cn/forum.php?mod=forumdisplay&fid=106/{{ img.src }}">
    </a>
    <span>{{ img.title }} </span>
  </li>
{% endfor %}
</ul>
