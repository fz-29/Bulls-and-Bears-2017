window.fbAsyncInit = function () {
    FB.init({
        appId: '218641865251508',
        xfbml: true,
        version: 'v2.8'
    });
    
    checkLoginState();

    FB.AppEvents.logPageView();
};

(function (d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) {
        return;
    }
    js = d.createElement(s);
    js.id = id;
    js.src = "https://connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));

function checkLoginState() {
    FB.getLoginStatus(function (response) {
        if (response.status === 'connected') {
            $.post("/rest-auth/facebook/", {
                    "access_token": response.authResponse.accessToken
                }, function (data, status) {       
                    console.log("Data: " + data.key + "\nStatus: " + status);
                    $('#uID').val(response.authResponse.userID).change();
                    $('#dk').val(data.key).change();
                }
            );
        } else {
            console.log('Not logged in.');
        }
    });
}