'use strict';
angular.module('market')
.controller('marketController', function($scope, $cookies, marketService) {
    $scope.companies = [];
	$scope.accountBalance = 0;
    var authToken = 'Token ' + $cookies.get('authToken');
	console.log("authToken : " + authToken);
	marketService.getCompanyList(authToken).then(function(companyList){
		$scope.companies = companyList;
	});
	marketService.getAccountBalance(authToken).then(function(customerDetail){
		$scope.accountBalance = customerDetail.fields.account_balance;
	});
});