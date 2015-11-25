angular.module('myApp.btnCtrl', []).
controller('btnController', function($scope) {
    $scope.getPrediction = function(){alert(document.getElementById("timeInput").value);};

});
