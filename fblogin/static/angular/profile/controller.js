'use strict';
angular.module('news')
.controller('newsController', function($scope, newsService) {
    $scope.newsList = [];
    
	newsService.getNewsList().then(function(newsList){
		$scope.newsList = newsList;
	});
});