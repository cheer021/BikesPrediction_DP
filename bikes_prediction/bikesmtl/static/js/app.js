angular.module('myApp', [
    'myApp.ListCtrl',
    'myApp.services'
]).config(function($httpProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});
