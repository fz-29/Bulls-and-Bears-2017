'use strict';
angular.module('leaderboard')
.factory('leaderboardService', function($http) {
	return {
		getLeaderboard : function() {
			return $http.get("http://127.0.0.1:8080/stockmarket//").then(function(response) {
                console.log(response);
				return response.data;
			});
		}
	}
});