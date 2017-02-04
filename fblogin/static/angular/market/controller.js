'use strict';
angular.module('market')
.controller('marketController', function($scope, $cookies, marketService) {
    $scope.companies = [];
    var authToken = $cookies.get('authToken');
	console.log("authToken : " + authToken);
	marketService.getCompanyList().then(function(companyList){
		$scope.companies = companyList;
	});
});