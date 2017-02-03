'use strict';
angular.module('leaderboard')
.controller('leaderboardController', function($scope, leaderboardService) {
    $scope.leaderboard = [];
    
	newsService.getNewsList().then(function(leaderboard){
		$scope.leaderboard = leaderboard;
	});
});