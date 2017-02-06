'use strict';
angular.module('portfolio')
.factory('portfolioService', function($http) {
	return {
		getCompanyPortfolio : function(authToken, id) {
			return $http({
				method: 'GET',
				url: '/stockmarket/companydetail/?id='+id,
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