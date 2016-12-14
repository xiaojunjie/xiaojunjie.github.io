---
title: 早起的鸟儿
layout: default
---
<div class="col-md-9">
<div id="myChart" style="width:100%;height:400px"><ul></ul></div>
<div id="moji_morning_title" style="display: none;" class="text-overflow">
<div class="moji_morning_detail pull-left">
    <p>坐标：东经<span class="longitude"></span>   北纬<span class="latitude"></span></p>
    <p>地址：<span class="location"></span></p>
    <p>时间：<span class="time"></span></p>
</div>
<div class="face pull-right" style="width:10%"></div>
</div>
</div>
<div class="col-md-3">
<div id="moji_morning_image"  style="display: none;">
    <p>NO.<span class="NO"></span> <span class="province"></span> <span class="time"></span></p>
    <div class="picture"></div>
</div>
</div>

<script src="{{ site.storage }}/assets/lib/echarts/full.min.js"></script>
<script src="{{ site.storage }}/assets/lib/echarts/china.js"></script>

<script type="text/javascript">
var option = {
    title: {
        text: '早起的鸟儿',
        subtext: "数据来自墨迹天气",
        left: 'center'
    },
    tooltip: {
        trigger: 'item',
        formatter: '{b}'
    },
    series: [
        {
            name: '中国',
            type: 'map',
            mapType: 'china',
            selectedMode : 'multiple',
            label: {
                normal: {
                    show: true
                },
                emphasis: {
                    show: true
                }
            }
        }
    ]
};
myChart = echarts.init(document.getElementById("myChart"));
function setArrow(picture){
    switch (picture.province_name) {
        case "内蒙古自治区":
            return {coord: [picture.longitude-3, picture.latitude+3]};
            break;
        case "新疆维吾尔自治区":
        case "云南省":
        case "西藏自治区":
            return {coord: [picture.longitude-8, picture.latitude]};
            break;
        case "山东省":
        case "海南省":
        case "江苏省":
        case "上海市":
        case "浙江省":
        case "福建省":
            return {coord: [picture.longitude+5, picture.latitude]};
            break;
        default:
            return {coord: [picture.longitude+10, picture.latitude]};
    }
}
function isInside(picture){
    return -1 < ["贵州省","四川省","湖北省","湖南省","重庆市","陕西省","山西省","青海省","甘肃省"].indexOf(picture.province_name)
}
function setMarkPoint(picture){
    if(!isInside(picture))return null;
    return {
        symbol: 'pin',
        symbolSize: picture.city_name.length*20,
        label: {
            normal: {
                show: true,
                formatter: function(d) {
                    return picture.city_name
                }
            }
        },
        itemStyle: {
            emphasis: {
                borderColor: '#ddd',
                borderWidth: 5
            }
        },
        data: [{
                name:  picture.city_name,
                coord: [picture.longitude,picture.latitude]
            }
        ]
    };
}
function setMarkLine(picture) {
    if(isInside(picture))return null;
    return {
        symbol: ["circle","arrow"],
        data: [
            [{
                name:  picture.city_name,
                coord: [picture.longitude,picture.latitude]
            },setArrow(picture)]
        ]
    };
}
function setLocation(picture){
    myChart.setOption(option);
    myChart.setOption({
        series: [{
            center: [picture.longitude,picture.latitude],
            zoom: 4,
            data:[
                {name: picture.province_name.replace(/省|市|自治区/,''), selected: true}
            ],
            markLine:  setMarkLine(picture),
            markPoint: setMarkPoint(picture),
            animationDurationUpdate: 1000,
            animationEasingUpdate: 'cubicInOut',
        }]
    });
}
window.addEventListener('load', function(){
    function get_picture(id, index){
        $.ajax({
            async: true,
            url: "//api.xjjfly.com/moji/get_picture.php",
            data:{id:id},
            dataType: "jsonp",
            success:function(data){
                console.log(data);
                var picture = data.picture;
                var cdn = {
                    webp: "//cdn.moji002.com/images/webp/simgs/",
                    jpg: "//cdn.moji002.com/images/sthumb/"
                };
                var src = picture["path"].slice(-3)=="jpg"?cdn["jpg"]:cdn["webp"];
                    src+= picture["path"];
                console.log(picture.province_name);
                setLocation(picture);
                $("#moji_morning_title .longitude").text(picture.longitude);
                $("#moji_morning_title .latitude").text(picture.latitude);
                $("#moji_morning_title .location").text(picture.location);
                $("#moji_morning_title .time").text((new Date(picture.create_time)).toLocaleString());
                $("#moji_morning_image .picture").html("<img src="+src+">");
                /* $("#moji_morning_title .face").html("<img src="+picture.face+" class='img-circle'>");*/
                $("#moji_morning_image .time").text((new Date(picture.create_time)).toLocaleTimeString().slice(2,-3));
                $("#moji_morning_image .NO").text(index);
                $("#moji_morning_image .province").text(picture.province_name);
                $("#moji_morning_title").show();
                $("#moji_morning_image").show();
            }
        })
    };
    $.ajax({
        async: true,
        url: "//api.xjjfly.com/moji/morning.php",
        dataType: "jsonp",
        success:function(data){
            data.sort(function(a,b){
                return a["create_time"] - b["create_time"]
            });
            for (var i = 1; i < 200; i++) {
                $("#moji_morning_title").hide();
                $("#moji_morning_image").hide();
                data[i]["id"]!=data[i+1]["id"] && setTimeout(get_picture,2000*i,data[i]["id"],i)
            }
        }
    })

});
</script>
