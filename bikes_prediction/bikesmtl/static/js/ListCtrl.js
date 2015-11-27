angular.module('myApp.ListCtrl', []).
controller('driversController', function($scope, $interval, BikesMtl) {
    var count = 0;
    $scope.bikes = {};
    var name = [];
    $scope.updateAllDataNow = function() {

        BikesMtl.allActual(4,23,0).then(
            function(response) {
                console.log(response.mtlData);
            });
        BikesMtl.allPredictions(4,23,0).then(
            function(response) {
                console.log(response.mtlData);
            });
    };
    $scope.getStationsNames = function(argument) {
        // body...
        BikesMtl.allInfo().then(
            function(response) {
                console.log(response.mtlData);
                // names = [];
                // var index = 0;
                //$scope.getBikeCounts();
                //console.log("2");
                //console.log(empDocksCounts);
                for (var s of response.mtlData) {
                    //console.log(s);
                    name.push(s.name.toString());
                }
                // $scope.stations.locations=locations;
                //console.log(name);
            }).then($scope.updateAllDataNow());
    }

    // $scope.updateAllDataNow();
    $scope.getStationsNames();
    // var timer = $interval($scope.updateAllDataNow, 60000);


});
