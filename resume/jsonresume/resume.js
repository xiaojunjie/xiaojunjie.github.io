(function(){
    config = {
        resumeid: "resume",
        jsonfilename: "resume.json"
    };
    createresume(handle, config.jsonfilename);

    function createresume(handle, jsonfilename){
        var xmlhttp, resumehtml;
        if (window.XMLHttpRequest){// code for IE7+, Firefox, Chrome, Opera, Safari
            xmlhttp=new XMLHttpRequest();
        }else{// code for IE6, IE5
            xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
        }

        xmlhttp.onreadystatechange=function() {
            if (xmlhttp.readyState==4 && xmlhttp.status==200){
                handle(JSON.parse(xmlhttp.responseText)); 
            }
        }
        xmlhttp.open("GET", jsonfilename, true);
        xmlhttp.send();
    }

    function handle(resumejson){
        append( handlejson(resumejson) );
    }

    // 通过 json 构建 HTML 结构
    function handlejson(jsonobj){
        var key, re, html, tmp;
        re = jsonobj;
        html = "<h1>JSON RESUME</h1>";
        for (key in re){
            if ( re.hasOwnProperty(key) ){
                html = html + "<h2>" + key + "</h2>";
                html = html + "<p>" + re[key].toString() + "</p>";
                // debugger;
            }
        }
        return html;
    }

    function append( htmlstr ){
        document.getElementById(config.resumeid).innerHTML = htmlstr;
    }
}());