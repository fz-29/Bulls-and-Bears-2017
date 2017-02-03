'use strict';
angular.module('market')
.factory('marketService', function($http) {
	return {
		getCompanyList : function() {
			return $http.get("/stockmarket/companylist/").then(function(response) {
                console.log(response);
				return response.data;
			});
		}
	}
});