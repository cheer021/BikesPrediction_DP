angular.module('myApp.ListCtrl', []).
controller('driversController', function($scope, $interval, BikesMtl) {
    var count = 0;
    $scope.bikes = {};
    var name = [];
    $scope.updateAllDataNow = function() {

        BikesMtl.allDataNow().then(
            function(response) {
                // body...
                count++;
                //$scope.bikes.predictions = response.mtlData;
                // for (var s of response) {
                //     //console.log(s);
                //     console.log(response.nbBikes);
                // }
                //var index=0;;
                console.log(response.mtlData);
        
                $scope.bikes.predictions = response.mtlData;
                var d = new Date();
                $scope.lastSvcTime = d.toTimeString();
                $scope.svcCounter = count;
            });
    };
    $scope.getStationsNames = function(argument) {
        // body...
        BikesMtl.allInfo().then(
            function(response) {

                names = [];
                var index = 0;
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
