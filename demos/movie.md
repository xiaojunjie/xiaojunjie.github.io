---
title: 电影
layout: post
---
复制链接后用迅雷下载  

## www.dy2018.com  

## www.loldytt.com  

<script type="text/javascript">
window.onload = function() {
    var sites = ["www.dy2018.com", "www.loldytt.com"];
    var api = "//api.xjjfly.com";
    sites.forEach(function(site){
        var data = {
            cat: "movie",
            site: site
        };
        $.ajax({
            type: "get",
            async: true,
            url: api,
            data: data,
            dataType: "jsonp",
            success:function(data){
                var html = '<ul>';
            	$.each(data,function(i,item){
            		html += '<li><a href="'
            			+ item.src + '" target="_blank">'+item.title+'</a></li>';
            	});
                html += '</ul>';
                $("#"+site.replace(/\./g,"")).after($(html));
            }
        })
    });
};
</script>
