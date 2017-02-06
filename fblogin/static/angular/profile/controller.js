'use strict';
angular.module('profile')
.controller('profileController', function($scope, $cookies, $http, $interval, profileService) {
    $scope.customerDetail = {};
    var authToken = 'Token ' + $cookies.get('authToken');
	console.log("authToken : " + authToken);
	
	var refreshingPromise = null; 
	var isRefreshing = false;
	$scope.startRefreshing = function(){
		if(isRefreshing) return;
		isRefreshing = true;
		(function refreshEvery(){
			//Do refresh
			//If async in then in callback do...
			profileService.getProfile(authToken).then(function(customerDetail){
				$scope.customerDetail = customerDetail;
				refreshingPromise = $timeout(refreshEvery,60000);
			});
		}());
	} 
	$scope.startRefreshing();
	$scope.$on('$destroy',function(){
    if(refreshingPromise)
        $timeout.cancel(refreshingPromise);   
	});
	
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