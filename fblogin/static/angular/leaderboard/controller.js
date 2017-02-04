'use strict';
angular.module('leaderboard')
.controller('leaderboardController', function($scope, $cookies, leaderboardService) {
    $scope.customerList = [];
    var authToken = 'Token ' + $cookies.get('authToken');
	console.log("authToken : " + authToken);
	leaderboardService.getCustomerList(authToken).then(function(customerList){
		$scope.customerList = customerList;
	});
});