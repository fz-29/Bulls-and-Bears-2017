var app = angular.module('xcms', ['ngCookies'])
.controller('mainCtrl', [ '$scope', '$cookies', '$window', function($scope, $cookies, $window){
    
    $scope.createCust = function(){
        var info = "/customer/create/?fbid=" + $scope.response;
        console.log(info);
        $window.location.href = info;
	}
    $scope.setCookie = function(){
        var info = $scope.dataKey;
        $cookies.put("authToken", info, { path : "/" });
        console.log("cookie : " + $cookies.get("authToken"));
        $scope.createCust();      
	}
}])
;