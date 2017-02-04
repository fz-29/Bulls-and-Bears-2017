'use strict';
angular.module('portfolio')
.factory('portfolioService', function($http) {
	return {
		getCompanyPortfolio : function(authToken) {
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