'use strict';
angular.module('market')
.controller('marketController', function($scope, $cookies, $timeout, marketService) {
    $scope.companies = [];
	$scope.accountBalance = 0;
    var authToken = 'Token ' + $cookies.get('authToken');
	console.log("authToken : " + authToken);

	var refreshingPromise = null; 
	var isRefreshing = false;
	$scope.startRefreshing = function(){
		if(isRefreshing) return;
		isRefreshing = true;
		(function refreshEvery(){
			//Do refresh
			//If async in then in callback do...
			marketService.getCompanyList(authToken).then(function(companyList){
				$scope.accountBalance = companyList.account_balance;
				$scope.companies = companyList.companies;
				refreshingPromise = $timeout(refreshEvery,60000);
			});
		}());
	} 
	$scope.startRefreshing();
	$scope.$on('$destroy',function(){
    if(refreshingPromise)
        $timeout.cancel(refreshingPromise);   
	});
});