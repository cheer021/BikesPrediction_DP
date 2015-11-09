angular.module('myApp', [
    'myApp.ListCtrl',
    'myApp.services',
    'myApp.mapCtrl'
]).config(function($httpProvider,$interpolateProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
    $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
});
