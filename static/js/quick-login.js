
var t_url = window.location.href;
var qq_link = 'http://vip.cssmoban.com/openlogin/qqlogin?url=' + encodeURIComponent(t_url); // qqå¿«æ·ç™»å½•
var wx_link = 'http://vip.cssmoban.com/openlogin/weixinlogin?url=' + encodeURIComponent(t_url); // å¾®ä¿¡å¿«æ·ç™»å½•

var login_html = '<div class="login-box">\n' +
    '    <div class="login">\n' +
    '\n' +
    '        <div class="close-loginbox"></div>\n' +
    '\n' +
    '        <div class="title">\n' +
    '            <p class="title-major">æ¨¡æ¿ä¹‹å®¶</p>\n' +
    '            <p class="title-minor"><em></em><span>ä¸‰ç§’ç™»å½•å³å¯ä¸‹è½½</span><em></em></p>\n' +
    '        </div>\n' +
    '\n' +
    '        <div class="quick-login">\n' +
    '            <div class="quick-l-wx wxlogin ajaxopen" data-action="' + wx_link + '" data-title="å¾®ä¿¡ç™»é™†" data-w="35%" data-y="50%" id="wxurl">\n' +
    '                <div class="l-wx-icon">\n' +
    '                    <div class="wx-icon"></div>\n' +
    '                </div>\n' +
    '                <p>å¾®ä¿¡ç™»å½•</p>\n' +
    '            </div>\n' +
    '            <a class="quick-l-qq qqlogin ajaxopen" href="'+ qq_link +'" data-title="QQç™»é™†" data-w="35%" data-y="50%">\n' +
    // '            <div class="quick-l-qq qqlogin" data-action="'+ qq_link +'" data-title="QQç™»é™†" data-w="50%" data-y="50%">\n' +
    '                <div class="l-qq-icon">\n' +
    '                    <div class="qq-icon"></div>\n' +
    '                </div>\n' +
    '                <p>QQç™»å½•</p>\n' +
    '            </div>\n' +
    '        </a>\n' +
    '    </div>\n' +
    '</div>' +
    '<div class="quick-login-ifr-box">' +
        '<div class="quick-login-ifr-title">' +
            '<span class="ifr-title">QQç™»å½•</span>' +
            '<div class="ifr-close"></div>' +
        '</div>' +
        '<iframe src="" frameborder="0" class="quick-login-ifr" id="quick-login-ifr"></iframe>' +
    '</div>';

$("body").append(login_html);

$(".close-loginbox").click(function () {
    $(".login-box").hide();
});

// $(".login > *").click(function (e) {
//     e.stopPropagation();
// });
//
// $(".login-box").click(function () {
//
//     $(this).hide();
// });