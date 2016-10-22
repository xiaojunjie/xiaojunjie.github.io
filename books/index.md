---
title: 阅读
layout: default
---

<div id="douban">
	<!--
		<div id="bookreading" class="douban-list"></div>
		<div id="bookread" class="douban-list"></div>
		<div id="bookwish" class="douban-list"></div>
	-->
</div>

<script type="text/javascript" src="/assets/dist/js/douban.api.min.js"></script>
<script type="text/javascript">
  var dbapi = new DoubanApi();
  window.onload = book;
  function book(){
    dbapi.show();
  }
</script>
