function XjjflyApi(type) {
	this.type = type;
	this[type+"_callback_show"] = function (data) {
		var mainplace = $("#" + this.type);
		var list_item = this.make_list_item(data)
		$(list_item).appendTo(mainplace);
		console.log(data)
	}
}

XjjflyApi.prototype.make_api_url = function(type,user,key,status,begin,end) {
	url = "http://api.xjjfly.com/?cat=movie&&callback="+this.type+"."+this.type+"_callback_show"
	return url;
}

XjjflyApi.prototype.make_list_item = function(items) {
	var html = '';
	$.each(items,function(i,item){
		html += '<li><a href="'
			+ item.src + '" target="_blank">'+item.title+'</a></li>';
	});
	return html;
};

XjjflyApi.prototype.parse_json = function(json) {
	return;
};

XjjflyApi.prototype.fix_num = function(num) {
	var index = 1;
	var fixnums = [];
	if (50 > num && num  > 0) {
		fixnums.push({begin:index,end:num});
	}
	else {
		while (num > 0) {
			fixnums.push({begin:index,end:index + 49});
			num -= 50;
			index += 50;
		}
	}
	return fixnums;
};

XjjflyApi.prototype.show = function() {
	this.appendScript(this.make_api_url());
};

XjjflyApi.prototype.appendScript = function(url) {
	if (url && url.length > 0) {
		$("<script/>").attr("src",url).attr("charset","utf-8").appendTo($("head")[0]);
	}
};

XjjflyApi.prototype.all_url = function(type,status,begin,end) {
	if (end === 0 ) return;
	if (!this[type + status + "_show"]) {
		this[type + status + "_show"] = function(json) {
			var mainplace = $("#" + this.defaults.place);
			if (mainplace.length === 0) {
				mainplace = $('<div id="' + this.defaults.place + '"></div>').prependTo($("body"));
			}
			if ($("#" + type + status).length === 0) {
				var title = this.defaults[type + status + "title"];
				$('<h2 class="douban-title">' + title + '</h2>').appendTo(mainplace);
				$('<div id="' + type + status + '" class="douban-list clearfix"><ul></ul></div>').appendTo(mainplace);
			}
			$("#" + type + status + " > ul").append(this.make_list_item(this.parse_json(json)));
		};
	}
	return this.make_api_url(type,this.defaults.user,this.defaults.api,status,begin,end);
};
