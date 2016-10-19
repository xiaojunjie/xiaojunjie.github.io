function backToTop(toTopId) {

    // fade in #back-top
    $(window).scroll(function() {
        if ($(this).scrollTop() > 300) {
            $(toTopId).addClass('scrolled');
        } else {
            $(toTopId).removeClass('scrolled');
        }
    });

    // scroll body to 0px on click
    $(toTopId).click(function() {
        $('body,html').animate({
            scrollTop: 0
        }, 200);
        return false;
    });
}