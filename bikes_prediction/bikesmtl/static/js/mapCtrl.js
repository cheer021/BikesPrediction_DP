angular.module('myApp.mapCtrl', ['ngMap'])
    .controller('mapController', function($scope, BikesMtl) {

        $scope.stations = {};
        $scope.$on('mapInitialized', function(evt, map) {

        });
        var empDocksCounts = [];
        var icon_prefix= 'http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=';
        var icon_green_end = '|00FF00|000000';
        var icon_yellow_end = '|FFFF00|000000';
        var icon_red_end = '|FF0000|000000';
        $scope.getBikeCounts = function() {
            //console.log("0");
            BikesMtl.allDataNow().then(
                function(response) {

                    for (var s of response.mtlData) {
                        //console.log(s);
                        empDocksCounts.push(s.nbEmptyDocks);
                    }
                    //console.log("1");
                    //$scope.stations.locations=locations;
                    //$scope.stations.locations["count"] = empDocksCounts;
                    //console.log(empDocksCounts) ;

                }).then(function() {
                $scope.getLocations();
            });
        };
        $scope.getLocations = function() {
            BikesMtl.allInfo().then(
                function(response) {

                    var locations = [];
                    var index = 0;
                    //$scope.getBikeCounts();
                    //console.log(response.mtlData);
                    //console.log(empDocksCounts);
                    for (var s of response.mtlData) {
                        //console.log(s);
                        var iconlink = "";
                        if(empDocksCounts[index]>=5){
                                iconlink=icon_prefix + empDocksCounts[index] + icon_green_end
                            }
                            else if(empDocksCounts[index]>=3){
                                iconlink=icon_prefix + empDocksCounts[index] + icon_yellow_end
                            }
                            else{
                                iconlink= icon_prefix + empDocksCounts[index] + icon_red_end
                            }
                        locations.push({
                            location: s.latitude.toString() + "," + s.longitude.toString(),icon:iconlink
                            
                            
                        });
                        index++;
                    }
                    $scope.stations.locations = locations;
                    // console.log($scope.stations.locations);
                });
        };

        $scope.getBikeCounts();

    });
