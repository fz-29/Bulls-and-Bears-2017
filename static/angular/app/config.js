'use strict';
angular.module('bnb').
    config(function ($locationProvider, $resourceProvider, $routeProvider) {
        $locationProvider.html5Mode(true);
        $resourceProvider.defaults.stripTrailingSlashes = true;
        $routeProvider.
            when("/", {
                redirectTo:'/market'
            }).
            when("/market", {
                controller:'marketController as market',
                templateUrl:'/static/templates/market.html'
            }).
            when("/profile", {
                controller:'profileController as profile',
                templateUrl:'/static/templates/profile.html'
            }).
            when("/news", {
                controller:'newsController as news',
                templateUrl:'/static/templates/news.html'
            }).
            when("/portfolio/:id", {
                controller:'portfolioController as portfolio',
                templateUrl:'/static/templates/companyportfolio.html'
            }).
            when("/leaderboard", {
                controller:'leaderboardController as leaderboard',
                templateUrl:'/static/templates/leaderboard.html'
            }).
            otherwise({
                template: "Not Found"
            });
    });