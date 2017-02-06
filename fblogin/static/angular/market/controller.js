'use strict';
angular.module('market')
.controller('marketController', function($scope, $cookies, marketService) {
    $scope.companies = [];
	$scope.accountBalance = 0;
    var authToken = 'Token ' + $cookies.get('authToken');
	console.log("authToken : " + authToken);

	marketService.getCompanyList(authToken).then(function(companyList){
		$scope.accountBalance = companyList.account_balance;
		$scope.companies = companyList.companies;
	});
	
});