var Flight = function(domID, date, airline) {
    this.chart = echarts.init(document.getElementById(domID));
    this.date = date;
    this.searchDay = date.getFullYear() + '-' + (date.getMonth() > 9 ? date.getMonth() + 1 : '0' + (date.getMonth() + 1)) + '-' + (date.getDate() > 9 ? date.getDate() : '0' + date.getDate());
    this.airline = airline;
    this.options = [];
};
Flight.City = [{
    name: "西安",
    id: "SIA"
}, {
    name: "福州",
    id: "FOC"
}, {
    name: "昆明",
    id: "KMG"
}];
Flight.airline = [{
    from: 0,
    to: 1
}, {
    from: 1,
    to: 0
}, {
    from: 0,
    to: 2
}, {
    from: 2,
    to: 0
}, {
    from: 1,
    to: 2
}, {
    from: 2,
    to: 1
}];
Flight.api = [{
    name: "阿里",
    src: "//sjipiao.alitrip.com/search/common_cheapest_calendar.htm",
    key: {
        from: "depCity",
        to: "arrCity",
        airport: "id",
        date: "searchDay"
    },
    data: {
        calType: "MonthCalendar"
    },
    callback: function(data) {
        var priceMAX = 0;
        var result = [];
        /* if(!data || !data.data)return [];*/
        data.data.forEach(function(day) {
            priceMAX = day.price > priceMAX ? day.price : priceMAX;
            result.push(day.price)
        });
        for (var past = this.date.getDate() - 2; past >= 0; past--) {
            result[past] = priceMAX;
        }
        return result;
    }
}, {
    name: "去哪儿",
    src: "//lp.flight.qunar.com/api/lp_calendar",
    key: {
        from: "dep",
        to: "arr",
        airport: "name",
        date: "dep_date"
    },
    data: {
        month_lp: 1
    },
    callback: function(data) {
        var priceMAX = 0;
        var result = [];
        /* if(!data || !data.data || !data.data.banner)return [];*/
        data.data.banner.forEach(function(day) {
            day.price = day.price > 9999 ? 0 : day.price;
            priceMAX = day.price > priceMAX ? day.price : priceMAX;
            result.push(day.price)
        });
        for (var past = this.date.getDate() - 2; past >= 0; past--) {
            result[past] = priceMAX;
        }
        return result;
    }
}/*,{
    name: "携程",
    src : "//api.xjjfly.com/public/jsonp.php",
    data: {
        url: "http://flights.ctrip.com/domesticsearch/search/SearchFirstRouteFlights"
    },
    key: {
        from: "DCity1",
        to : "ACity1",
        airport: "id",
        date: "DDate1"
    },
    callback: function(data){
        console.log(data.lps);
        var day = new Date(this.date.getFullYear(), this.date.getMonth() + 1, 0).getDate();
        var past = this.date.getDate()-1;
        var first = Object.keys(data.lps).indexOf(this.searchDay);
        var last  = first+day-past;
        console.log(first,last);
        data = Object.values(data.lps).slice(first,last);
        var priceMAX = Math.max.apply(Math,data);
        return (new Array(past)).fill(priceMAX).concat(data);
    }
}*/];
Flight.prototype.init = function() {
    this.LoadApiProfile();
    this.LoadChartView();
    return this;
};
Flight.prototype.render = function() {
    this.chart.setOption({
        timeline: this.timeline,
        options: this.options
    });
};
Flight.prototype.LoadChartView = function() {
    for (var i = 0; i < this.airline.length; i++) {
        this.options[i] = {
            title: {
                text: this.date.getMonth() + 1 + "月份"
            },
            tooltip: {
                trigger: 'axis'
            },
            legend: {
                padding: 5,
                itemGap: 10,
                data: []
            },
            toolbox: {
                show: true,
                feature: {
                    dataZoom: {
                        yAxisIndex: 'none'
                    },
                    dataView: {
                        readOnly: false
                    },
                    magicType: {
                        type: ['line', 'bar']
                    },
                    restore: {},
                    saveAsImage: {}
                }
            },
            xAxis: {
                data: (function() {
                    var result = [];
                    var day = new Date(this.date.getFullYear(), this.date.getMonth() + 1, 0).getDate();
                    for (var i = 1; i <= day; i++) {
                        result.push(i.toString())
                    };
                    return result;

                }).bind(this)()
            },
            yAxis: {},
            series: []
        };
    }
    this.timeline = {
        axisType: 'category',
        show: true,
        autoPlay: false,
        playInterval: 1500,
        data: (function() {
            var result = [];
            this.airline.forEach(function(flight) {
                result.push(Flight.City[flight.from].name + "->" + Flight.City[flight.to].name);
            });
            return result;
        }).bind(this)()
    };
    // console.log(this);
};
Flight.prototype.LoadApiView = function(site, i, j) {
    this.options[i].legend.data.push(site.name);
    this.options[i].series[j] = {
        data: [],
        name: site.name,
        type: 'line',
        markPoint: {
            data: [{
                type: 'min',
                name: '最小值'
            }]
        },
        itemStyle: {
            normal: {
                label: {
                    show: true,
                    position: 'top',
                    textStyle: {
                        color: 'blue'
                    },
                    formatter: "{c}"
                }
            }
        }
    };
};
Flight.prototype.LoadApiData = function(callback, data, i, j) {
    this.options[i].series[j].data = callback.call(this,data);
};
Flight.prototype.LoadApiProfile = function() {
    this.api = Flight.api;
    for (var i = 0; i < this.api.length; i++) {
        this.api[i].data[this.api[i]["key"]["date"]] = this.searchDay;
    }
};
Flight.prototype.fetch = function() {
    var self = this;
    this.airline.forEach(function(flight, i) {
        self.api.forEach(function(site, j) {
            site.data[site.key.from] = Flight.City[flight.from][site.key.airport];
            site.data[site.key.to] = Flight.City[flight.to][site.key.airport];
            $.ajax({
                type: "get",
                async: true,
                url: site.src,
                data: site.data,
                dataType: "jsonp",
                success: function(data) {
                    self.LoadApiView(site, i, j);
                    self.LoadApiData(site.callback, data, i, j);
                    self.render();
                }
            })
        });
    });
};
