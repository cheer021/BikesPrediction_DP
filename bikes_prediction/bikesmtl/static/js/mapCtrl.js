var app=angular.module('myApp.mapCtrl', ['ngMap']);
app.controller('driversController', function($scope) {
  $scope.$on('mapInitialized', function(evt, map) {
    var infoWindow = map.infoWindows[1];
    $scope.zoomChanged = function(e) {
      infoWindow.setContent('Predition: ' + 12);
      map.setCenter(infoWindow.getPosition());
    }
  });
});