---
title: 机票
layout: default
---
<div id="thisMonth" style="width: 100%;height:400px;margin-bottom:100px;"></div>
<div id="nextMonth" style="width: 100%;height:400px;"></div>
<script src="{{ site.storage }}/assets/lib/echarts.min.js"></script>
<script src="{{ site.storage }}/assets/lib/xjjfly.api.flight.js"></script>
<script type="text/javascript">
window.addEventListener('load',function(){
    var thisMonth = new Date;
    var nextMonth = new Date;
    nextMonth.setDate(1);
    nextMonth.setMonth(thisMonth.getMonth()+1);

    var thisMonthChart = new Flight("thisMonth", thisMonth, Flight.airline);
    var nextMonthChart = new Flight("nextMonth", nextMonth, Flight.airline);
    thisMonthChart.init().fetch();
    nextMonthChart.init().fetch();
})
</script>
