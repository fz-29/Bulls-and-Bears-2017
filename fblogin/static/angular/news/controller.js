// 'use strict';
// angular.module('news')
// .controller('newsController', function($scope, $cookies, newsService) {
//     $scope.newsList = [];
//     var authToken = 'Token ' + $cookies.get('authToken');
// 	console.log("authToken : " + authToken);
// 	newsService.getNewsList(authToken).then(function(newsList){
// 		$scope.newsList = newsList;
// 	});
// });
'use strict';
angular.module('news')
.controller('newsController', function($scope, $cookies, newsService) {
    $scope.newsList = [];
    var authToken = 'Token ' + $cookies.get('authToken');
	console.log("authToken : " + authToken);
	newsService.getNewsList(authToken).then(function(newsList){
		$scope.newsList = newsList;
	});

});