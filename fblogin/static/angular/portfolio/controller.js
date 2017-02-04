'use strict';
angular.module('portfolio')
.controller('portfolioController', function($scope, $cookies, portfolioService) {
    $scope.companyPortfolio = {};
    var authToken = 'Token ' + $cookies.get('authToken');
	console.log("authToken : " + authToken);
	portfolioService.getCompanyPortfolio(authToken).then(function(companyPortfolio){
		$scope.companyPortfolio = companyPortfolio;
	});
});