'use strict';
angular.module('news')
.controller('newsController', function($scope, $cookies, $interval, newsService) {
    $scope.newsList = [];
    var authToken = 'Token ' + $cookies.get('authToken');
	console.log("authToken : " + authToken);
	$scope.callAtInterval = function(){
		newsService.getNewsList(authToken).then(function(newsList){
		$scope.newsList = newsList;
	});}
	$scope.callAtInterval();
	// $interval( function(){ $scope.callAtInterval(); }, 60000);
});