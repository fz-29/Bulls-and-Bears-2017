'use strict';
angular.module('market')
.factory('marketService', function($http) {
	return {
		getCompanyList : function(authToken) {
			return $http({
				method: 'GET',
				url: '/stockmarket/companylist/',
				headers: { 
					'Authorization': authToken
			 }
			}).then(function(response){
				console.log(response);
				return response.data;
			});
			// return $http.get("/stockmarket/companylist/").then(function(response) {
            //     console.log(response);
			// 	return response.data;
			// });
		}
	}
});