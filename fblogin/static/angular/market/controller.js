'use strict';
angular.module('market')
.controller('marketController', function($scope, $cookies, marketService) {
    $scope.companies = [];
    var authToken = 'Token ' + $cookies.get('authToken');
	console.log("authToken : " + authToken);
	marketService.getCompanyList(authToken).then(function(companyList){
		$scope.companies = companyList;
	});
	// $scope.data = "";
	// $http({
	// 			method: 'POST',
	// 			url: '/stockmarket/companylist/',
	// 			data: $scope.data,
	// 			headers: { 
	// 				'Authorization': authToken
	// 		 }
	// 		}).then(function(response){
	// 			console.log(response);
	// 		});
});