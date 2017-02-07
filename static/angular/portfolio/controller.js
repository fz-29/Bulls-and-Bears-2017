'use strict';
angular.module('portfolio')
.controller('portfolioController', function($routeParams, $scope, $http, $cookies, $timeout, portfolioService) {
    $scope.company = {};
    var authToken = 'Token ' + $cookies.get('authToken');
	var chartData = {};
	console.log("authToken : " + authToken);

	var refreshingPromise = null; 
	var isRefreshing = false;
	$scope.startRefreshing = function(){
		if(isRefreshing) return;
		isRefreshing = true;
		(function refreshEvery(){
			//Do refresh
			//If async in then in callback do...
			portfolioService.getCompanyPortfolio(authToken, $routeParams.id).then(function(companyPortfolio){
				$scope.company = companyPortfolio;
				console.log(companyPortfolio);
				var price_history = []
				// var stock_history = []
				for (var price in companyPortfolio.price_history) {
					price_history.push(parseFloat(companyPortfolio.price_history[price]));
				}
				// for (var price in companyPortfolio.stock_history) {
				// 	stock_history.push(parseFloat(companyPortfolio.stock_history[price]));
				// }
				chartData = {
					type: "area",  // Specify your chart type here.
					title: {},
					legend: {}, // Creates an interactive legend
					series: [  // Insert your series data here.
						{ 
							values: price_history,
							text: "Price History"
						},
						// {
						// 	values: stock_history,
						// 	text: "Stock History"
						// }
					]
					};
					zingchart.render({ // Render Method[3]
					id: "chartDiv",
					data: chartData,
					width: '100%'
				});
				refreshingPromise = $timeout(refreshEvery,60000);
			});
		}());
	} 
	$scope.startRefreshing();
	$scope.$on('$destroy',function(){
    if(refreshingPromise)
        $timeout.cancel(refreshingPromise);   
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