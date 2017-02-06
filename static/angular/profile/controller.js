'use strict';
angular.module('profile')
.controller('profileController', function($scope, $cookies, $http, $interval, profileService) {
    $scope.customerDetail = {};
    var authToken = 'Token ' + $cookies.get('authToken');
	console.log("authToken : " + authToken);
	$scope.callAtInterval = function(){
	profileService.getProfile(authToken).then(function(customerDetail){
		$scope.customerDetail = customerDetail;
	});}
	$scope.callAtInterval();
	$interval( function(){ $scope.callAtInterval(); }, 60000);
	
	$scope.takeLoan = function(){
		$http({
			method: 'POST',
			url: '/customer/takeloan/',
			// data: $scope.data,
			headers: { 'Authorization': authToken }
		}).then(function(response){
			if(response.data.success){
				profileService.getProfile(authToken).then(function(customerDetail){
					$scope.customerDetail = customerDetail;
				});
			}
		});
	}

	$scope.repayLoan = function(){
		$http({
			method: 'POST',
			url: '/customer/repayloan/',
			// data: $scope.data,
			headers: { 'Authorization': authToken }
		}).then(function(response){
			if(response.data.success){
				profileService.getProfile(authToken).then(function(customerDetail){
					$scope.customerDetail = customerDetail;
				});
			}
		});
	}
});