'use strict';
angular.module('leaderboard')
.factory('leaderboardService', function($http) {
	return {
		getCustomerList : function(authToken) {
			return $http({
				method: 'GET',
				url: '/customer/customerlist/',
				headers: { 
					'Authorization': authToken ,
					'Accept': 'application/json',
        			"X-Login-Ajax-call": 'true'
			 }
			}).then(function(response){
				console.log(response);
				return response.data;
			});
		}
	}
});