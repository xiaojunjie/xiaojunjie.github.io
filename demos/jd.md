---
title: 京东
layout: default
categories: 爬虫
---

<div id="jd"></div>
<script type="text/javascript">
window.onload = function() {
    var api = "//api.xjjfly.com/jd/nice.php";
    var data = {
        area: "xian"
    };
    $.ajax({
        async: true,
        url: api,
        data: data,
        dataType: "jsonp",
        success:function(data){
            var html = '<ul>';
        	$.each(data,function(i,item){
        		html += '<li><a href="'
        			+ item.link + '" target="_blank">'+item.name+'</a></li>';
        	});
            html += '</ul>';
            $("#jd").html(html);
        }
    })
};
</script>
