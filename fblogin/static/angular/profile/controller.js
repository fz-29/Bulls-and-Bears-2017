'use strict';
angular.module('profile')
.controller('profileController', function($scope, $cookies, profileService) {
    $scope.customerDetail = {};
    var authToken = 'Token ' + $cookies.get('authToken');
	console.log("authToken : " + authToken);
	profileService.getProfile(authToken).then(function(customerDetail){
		$scope.customerDetail = customerDetail;
	});

});