'use strict';
angular.module('market')
.controller('marketController', function($scope, marketService) {
    $scope.companies = [];
    
	marketService.getCompanyList().then(function(companyList){
		$scope.companies = companyList;
	});
});