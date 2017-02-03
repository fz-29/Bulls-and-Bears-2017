'use strict';
angular.module('news')
.factory('newsService', function($http) {
	return {
		getNewsList : function() {
			return $http.get("/stockmarket/newslist/").then(function(response) {
                console.log(response);
				return response.data;
			});
		}
	}
});