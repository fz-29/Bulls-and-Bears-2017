'use strict';
angular.module('market')
.controller('marketController', function($scope, $cookies, $interval, marketService) {
    $scope.companies = [];
	$scope.accountBalance = 0;
    var authToken = 'Token ' + $cookies.get('authToken');
	console.log("authToken : " + authToken);

	$scope.refreshMarket = function() {
       marketService.getCompanyList(authToken).then(function(companyList){
			$scope.accountBalance = companyList.account_balance;
			$scope.companies = companyList.companies;
		});
    }
	refreshMarket();
    var promise = $interval($scope.refreshMarket, 10000);
    $scope.$on('$destroy',function(){
        if(promise)
            $interval.cancel(promise);   
    });

	// var refreshingPromise; 
	// var isRefreshing = false;
	// $scope.startRefreshing = function(){
	// 	if(isRefreshing) return;
	// 	isRefreshing = true;
	// 	(function refreshEvery(){
	// 		//Do refresh
	// 		//If async in then in callback do...
	// 		marketService.getCompanyList(authToken).then(function(companyList){
	// 			$scope.accountBalance = companyList.account_balance;
	// 			$scope.companies = companyList.companies;
	// 			refreshingPromise = $timeout(refreshEvery,60000)
	// 		});
	// 	}());
	// } 
	// $scope.$on('$destroy',function(){
    // if(refreshingPromise)
    //     $timeout.cancel(refreshingPromise);   
	// });

	// var intervalPromise;
	// $scope.refreshMe = function(){
	// 	marketService.getCompanyList(authToken).then(function(companyList){
	// 		$scope.accountBalance = companyList.account_balance;
	// 		$scope.companies = companyList.companies;
	// 		intervalPromise = $interval($scope.refreshMe, 60000);
	// 	});
	// }
	// $scope.$on('$destroy',function(){
	// 	if(intervalPromise)
	// 		$interval.cancel(intervalPromise);   
	// });
});