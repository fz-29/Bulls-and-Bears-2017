'use strict';
angular.module('market')
.controller('marketController', function($scope, $cookies, $interval, marketService) {
    $scope.companies = [];
	$scope.accountBalance = 0;
    var authToken = 'Token ' + $cookies.get('authToken');
	console.log("authToken : " + authToken);
	$scope.callAtInterval = function(){
		marketService.getCompanyList(authToken).then(function(companyList){
		$scope.accountBalance = companyList.account_balance;
		$scope.companies = companyList.companies;
	});}
	$scope.callAtInterval();
	$interval( function(){ $scope.callAtInterval(); }, 60000);
});