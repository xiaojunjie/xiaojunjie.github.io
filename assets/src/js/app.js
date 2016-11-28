;(function() {
    "use strict";

    /* 0.config */
    var config = {
        backtopId: '#back-top',
        heading: 'h2,h3,h4,h5',
        tocid: '#toc',
        postNavClass: '.post-nav',
        hiddenTitle: '(●—●) 咦',
        visibTitle: document.title
    }

    /* 1.up to top */
    addLoadEvent(function(){
        backToTop(config.backtopId)
    });

    /* 2.title anchor */
    anchors.options = {
        placement: 'right',
        icon: '#'
    };
    anchors.add(config.heading);

    /* 3.table of content */
    tableOfContent(config.tocid);

    /* 4.display when page hidden */
    listenerPageHiddenDisplay(config.visibTitle, config.hiddenTitle)

    /* navScroll
    ** 悬停
    */
    function navScroll(objID,headerHeight) {
        $(window).bind('scroll', function () {
            if ($(window).scrollTop() > headerHeight) {
                $(objID).addClass('fixed');
            }
            else {
                $(objID).removeClass('fixed');
            }
        });
    }

    function tableOfContent(tocId){
        if ($(tocId)){
            var tocObj = $("#toc").tocify({'selectors': config.heading, 'extendPage': false, 'hideEffect': 'slidUp'});
            navScroll(config.postNavClass,150);
            // no toc
            if (!tocObj.find('li').length){
                $(config.postNavClass).hide();
            }
        }
    }

    function listenerPageHiddenDisplay(visibTitle, hiddenTitle){
        if (typeof document.addEventListener !== "undefined" || typeof document.hidden !== "undefined") {
          document.addEventListener("visibilitychange", pageHiddenDisplay, false);
        }
        function pageHiddenDisplay() {
          if (document.hidden) {
            document.title = hiddenTitle;
          } else {
            document.title = visibTitle;
          }
        }
    }

    function addLoadEvent(func) {
        var oldOnLoad = window.onload;
        if (typeof window.onload != 'function') {
            window.onload = func;
        } else {
            window.onload = function() {
                oldOnLoad();
                func();
            }
        }
    }

})();
