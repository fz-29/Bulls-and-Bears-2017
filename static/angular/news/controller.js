'use strict';
angular.module('news')
.controller('newsController', function($scope, $sce, $cookies, $interval, newsService) {
    $scope.newsList = [];
    var authToken = 'Token ' + $cookies.get('authToken');
	console.log("authToken : " + authToken);
	$scope.callAtInterval = function(){
		newsService.getNewsList(authToken).then(function(newsList){
		$scope.newsList = newsList;
		for (var news in $scope.newsList) {
			$scope.newsList[news].fields.news_text = $sce.trustAsHtml($scope.newsList[news].fields.news_text);
			$scope.newsList[news].fields.youtube_src = $sce.trustAsResourceUrl($scope.newsList[news].fields.youtube_src);
 		}
	});}
	$scope.callAtInterval();
	$interval( function(){ $scope.callAtInterval(); }, 60000);
});