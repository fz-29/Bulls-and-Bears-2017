'use strict';
angular.module('market')
.factory('marketService', function($http) {
	var companyList = function(authToken) {
			return $http({
				method: 'GET',
				url: '/stockmarket/companylist/',
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
	return {
		getCompanyList: companyList
	}
});