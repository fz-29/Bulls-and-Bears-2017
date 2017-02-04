'use strict';
angular.module('news')
.factory('newsService', function($http) {
	return {
		getNewsList : function(authToken) {
			return $http({
				method: 'GET',
				url: '/stockmarket/newslist/',
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