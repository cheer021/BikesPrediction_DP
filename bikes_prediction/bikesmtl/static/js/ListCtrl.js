angular.module('myApp.ListCtrl', []).
controller('driversController', function($scope, $interval, BikesMtl) {
	var count = 0;
    $scope.bikes = {};

    $scope.updateAllDataNow = function(){
        
        BikesMtl.allDataNow().then(
        function putIntoData(response) {
            // body...
            count++;
            $scope.bikes.predictions = response.mtlData;
            // console.log($scope.bikes.predictions);
            var d  = new Date();
            $scope.lastSvcTime = d.toTimeString(); 
            $scope.svcCounter = count;
        });
    };

    $scope.updateAllDataNow();
    var timer = $interval($scope.updateAllDataNow, 5000);


});
