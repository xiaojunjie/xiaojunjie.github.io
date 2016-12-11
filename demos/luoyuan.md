---
title: 罗源县
layout: post
---
[百度百科](//baike.baidu.com/view/190654.htm){:target="1"} --
[维基百科](//zh.wikipedia.org/zh-hans/罗源){:target="1"} --
[县志](//vdisk.weibo.com/s/uaZyCAQu-lwfJ){:target="2"} --
[优酷](//www.soku.com/v?keyword=罗源&f=1&kb=010200000000000__罗源&_rp=14811861002844AY){:target="3"} --
[YouTube](//www.youtube.com/results?sp=CAI%253D&q=罗源){:target="3"}


## 墨迹时景  

### 今天  
<div id="moji_today"><ul></ul></div>  

### 昨天  
<div id="moji_yesterday"><ul></ul></div>  

### 前天  
<div id="moji_before_yesterday"><ul></ul></div>  

### 以前  
<div id="moji_past"><ul></ul></div>  

## 百度贴吧  
<div id="luoyuan_baidu"></div>  

## 新浪微博  
<div id="luoyuan_sina"></div>  

<script type="text/javascript">
window.addEventListener('load', function(){
    $("div[id^='moji_']").bind("cat",function(index,picture){
        var cdn = "//cdn.moji002.com/images/webp/simgs/";
        var title = picture.location +"----"+ new Date(picture.create_time).toLocaleString();
        var style = picture.width > picture.height ? "width:100%" :"width:400px";
        $(this).children("ul").append($("<li><span>"+title+"</span><br /><img src="+cdn+picture.path+" style="+style+"><br /><br /></li>"));
    });
    $.ajax({
        async: true,
        url: "http://api.xjjfly.com/luoyuan/moji.php",
        dataType: "jsonp",
        success: function(data) {
            var now = new Date();
            var year = now.getFullYear();
            var month= now.getMonth();
            var day  = now.getDate();
            var yesterday = new Date(year, month, day);
            var before_yesterday = new Date(year, month, day-1);
            var past = new Date(year, month, day-2);
            var cat = [
                function( picture ){
                    return picture.create_time < now && picture.create_time>yesterday ;
                },function( picture ){
                    return picture.create_time < yesterday && picture.create_time>before_yesterday;
                },function( picture ){
                    return picture.create_time < before_yesterday && picture.create_time>past;
                }
            ];
            data["picture_list"].forEach(function(picture){
                cat.some(function(handler,index){
                    return handler(picture) && $("div[id^='moji_']").eq(index).trigger("cat",picture);
                }) || $("div[id^='moji_']").eq(-1).trigger("cat",picture);
            })

        }
    })
});

window.addEventListener('load', function(){
    var api = "//api.xjjfly.com/luoyuan/baidu.php";
    $.ajax({
        type: "get",
        async: true,
        url: api,
        data: null,
        dataType: "jsonp",
        success:function(data){
            data.forEach(function(src,index){
                $("#luoyuan_baidu").append($("<img src=//crawler.xjjfly.com/"+src+"><br /><br />"))
            })
        }
    })
});

window.addEventListener('load', function(){
    var api = "//api.xjjfly.com/luoyuan/sina.php";
    $.ajax({
        type: "get",
        async: true,
        url: api,
        data: null,
        dataType: "jsonp",
        success:function(data){
            data.forEach(function(src){
                $("#luoyuan_sina").append($("<img src="+src+"><br /><br />"))
            })
        }
    })
});
</script>
