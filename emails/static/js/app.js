angular.module('testApp', ['ngRoute'])
    .config(function($routeProvider) {
        $routeProvider
            .when('/base', {
                controller: 'BaseCtrl',
                templateUrl: 'static/tpl/detail.html'
            })
            .when('/logout', {
                controller: 'LogoutCtrl',
                templateUrl: 'static/tpl/logout.html'
            })
            .otherwise({redirectTo:'/'});
    })

.controller('BaseCtrl', ['$scope', '$http', '$rootScope',
  function($scope, $http, $rootScope) {

      $http.get('http://localhost:8000/emails-data/').success(function(data) {
          $scope.emails = data;

      });

  }])

.controller('LogoutCtrl', ['$scope', '$http', '$rootScope',
  function($scope, $http, $rootScope) {

      window.location = "https://mail.google.com/mail/u/0/?logout&hl=en";

  }]);
