'use strict';
angular.module('profile')
.factory('profileService', function($http) {
	return {
		getProfile : function(authToken) {
			return $http({
				method: 'GET',
				url: '/customer/customerdetail/',
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