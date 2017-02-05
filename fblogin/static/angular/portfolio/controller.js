'use strict';
angular.module('portfolio')
.controller('portfolioController', function($routeParams, $scope, $http, $cookies, portfolioService) {
    $scope.company = {};
    var authToken = 'Token ' + $cookies.get('authToken');
	console.log("authToken : " + authToken);
	portfolioService.getCompanyPortfolio(authToken, $routeParams.id).then(function(companyPortfolio){
		$scope.company = companyPortfolio;
	});

	$scope.buy = function(){
		console.log("buyQty: " + $scope.buyQty);
		$scope.data = 'id=' + $routeParams.id +
			'&quantity=' + $scope.buyQty;
		$http({
			method: 'POST',
			url: '/customer/buy/',
			data: $scope.data,
			headers: { 
				'Authorization': authToken,
				'Content-Type': 'application/x-www-form-urlencoded' }
		}).then(function(response){
			if(response.data.success){
				portfolioService.getCompanyPortfolio(authToken, $routeParams.id).then(function(companyPortfolio){
					$scope.company = companyPortfolio;
					$scope.buyQty = 0;
					$scope.sellQty = 0;
				});
			}
		});
	}

	$scope.sell = function(){
		$scope.data = 'id=' + $routeParams.id +
			'&quantity=' + $scope.sellQty;
		$http({
			method: 'POST',
			url: '/customer/sell/',
			data: $scope.data,
			headers: { 
				'Authorization': authToken,
				'Content-Type': 'application/x-www-form-urlencoded' }
		}).then(function(response){
			if(response.data.success){
				portfolioService.getCompanyPortfolio(authToken, $routeParams.id).then(function(companyPortfolio){
					$scope.company = companyPortfolio;
					$scope.buyQty = 0;
					$scope.sellQty = 0;
				});
			}
		});
	}

	$scope.short = function(){
		$scope.data = 'id=' + $routeParams.id +
			'&quantity=' + $scope.shortQty;
		$http({
			method: 'POST',
			url: '/customer/short/',
			data: $scope.data,
			headers: { 
				'Authorization': authToken,
				'Content-Type': 'application/x-www-form-urlencoded' }
		}).then(function(response){
			if(response.data.success){
				portfolioService.getCompanyPortfolio(authToken, $routeParams.id).then(function(companyPortfolio){
					$scope.company = companyPortfolio;
					$scope.shortQty = 0;
					$scope.coverQty = 0;
				});
			}
		});
	}

	$scope.cover = function(){
		$scope.data = 'id=' + $routeParams.id +
			'&quantity=' + $scope.coverQty;
		$http({
			method: 'POST',
			url: '/customer/cover/',
			data: $scope.data,
			headers: { 
				'Authorization': authToken,
				'Content-Type': 'application/x-www-form-urlencoded' }
		}).then(function(response){
			if(response.data.success){
				portfolioService.getCompanyPortfolio(authToken, $routeParams.id).then(function(companyPortfolio){
					$scope.company = companyPortfolio;
					$scope.shortQty = 0;
					$scope.coverQty = 0;
				});
			}
		});
	}
});