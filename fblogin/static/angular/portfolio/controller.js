'use strict';
angular.module('portfolio')
.controller('portfolioController', function($routeParams, $scope, $cookies, portfolioService) {
    $scope.company = {};
    var authToken = 'Token ' + $cookies.get('authToken');
	console.log("authToken : " + authToken);
	portfolioService.getCompanyPortfolio(authToken, $routeParams.id).then(function(companyPortfolio){
		$scope.company = companyPortfolio;
	});
});