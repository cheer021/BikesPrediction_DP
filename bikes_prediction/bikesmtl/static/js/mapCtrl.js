angular.module('myApp.mapCtrl', ['ngMap'])
    .controller('mapController', function($scope, BikesMtl) {

        $scope.stations = {};
        $scope.timeToPass = {month: 4, day: 23, hour: 1}; //use it as default value to predict
        $scope.$on('mapInitialized', function(evt, map) {});
        $scope.predictions = [];
        $scope.actual = [];
        var empDocksCounts = [];
        var icon_prefix = 'http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=';
        var icon_green_end = '|00FF00|000000';
        var icon_yellow_end = '|FFFF00|000000';
        var icon_red_end = '|FF0000|000000';
        $scope.getPredictionCounts = function() {
            BikesMtl.allActual(4,23,0).then(
                function(response) {
                    //console.log(response.mtlData);
                    for (var s of response.mtlData) {
                        // // //console.log(s);
                        // var iconlink = "";
                        // if ($scope.predictionNum[index] >= 5) {
                        //     iconlink = icon_prefix + $scope.predictionNum[index] + icon_green_end
                        // } else if ($scope.predictionNum[index] >= 3) {
                        //     iconlink = icon_prefix + $scope.predictionNum[index] + icon_yellow_end
                        // } else {
                        //     iconlink = icon_prefix + $scope.predictionNum[index] + icon_red_end
                        // }
                        $scope.actual.push({
                            // location: s.latitude.toString() + "," + s.longitude.toString(),
                            // icon: iconlink,
                            index: s.id,
                            nbBikesActual: s.nbBikes,
                            nbEmptyDocksActual: s.nbEmptyDocks

                        });
                        // index++;
                    }
                    BikesMtl.allPredictions(4,23,0).then(
                    function(response) {
                       // console.log(response.mtlData);
                        // $scope.predictionNum = response.mtlData;
                        var i = 0;
                        for (var s of response.mtlData) {
                            // // //console.log(s);
                            // var iconlink = "";
                            // if ($scope.predictionNum[index] >= 5) {
                            //     iconlink = icon_prefix + $scope.predictionNum[index] + icon_green_end
                            // } else if ($scope.predictionNum[index] >= 3) {
                            //     iconlink = icon_prefix + $scope.predictionNum[index] + icon_yellow_end
                            // } else {
                            //     iconlink = icon_prefix + $scope.predictionNum[index] + icon_red_end
                            // }
                            $scope.predictions.push({
                                // location: s.latitude.toString() + "," + s.longitude.toString(),
                                // icon: iconlink,
                                index: s.id,
                                nbBikesPredicted: s.nbBikes,
                                nbEmptyDocksPredicted: s.nbEmptyDocks

                            });
                            // i++;
                            //actual[i].nbBikesPredicted = s.nbBikes;
                            //actual[i].nbEmptyDocksPredicted = s.nbEmptyDocks;
                        }
                        // console.log($scope.actual);
                        // console.log($scope.predictions);

                        $scope.getLocations();
                        // $scope.x = mtlData;
                    });
                });
            

        };
        $scope.getLocations = function() {
            BikesMtl.allInfo().then(
                function(response) {

                     var locations = [];
                    var index = 0;
                    //$scope.getBikeCounts();
                   //console.log(response.mtlData);
                    // //console.log(empDocksCounts);
                    for (var s of response.mtlData) {
                        // //console.log(s);
                        // var iconlink = "";\
                        var station = s.id;
                        //console.log(station);
                        var bikesActual;
                        var emptyActual;
                        var bikesPred;
                        var emptyPred;

                        for (var a in $scope.actual){
                            // console.log();
                            if ($scope.actual[a].index == station) {
                                bikesActual = $scope.actual[a].nbBikesActual;
                                emptyActual = $scope.actual[a].nbEmptyDocksActual;
                                // console.log(a);
                            }
                        }
                        for (var a in $scope.predictions){
                            if ($scope.predictions[a].index == station) {
                                bikesPred = $scope.predictions[a].nbBikesPredicted;
                                emptyPred = $scope.predictions[a].nbEmptyDocksPredicted;
                            }
                        }
                        // console.log($scope.actual);
                        var diffBikes =(bikesPred - bikesActual)>=0? (bikesPred - bikesActual):-(bikesPred - bikesActual);
                        var diffDocks =(emptyPred - emptyActual)>=0? (emptyPred - emptyActual):-(emptyPred - emptyActual);
                        var diff = (diffBikes + diffDocks)/2;
                        if (diff >= 5) {
                            iconlink = icon_prefix + bikesPred + icon_red_end
                        } else if (diff>= 3) {
                            iconlink = icon_prefix + bikesPred + icon_yellow_end
                        } else {
                            iconlink = icon_prefix + bikesPred + icon_green_end
                        }
                        locations.push({
                            location: s.latitude.toString() + "," + s.longitude.toString(),
                            icon: iconlink,
                            index: s.id

                        });
                        index++;
                    }
                    // console.log(response.mtlData)
                    $scope.stations.locations = locations;

                    //console.log($scope.stations.locations);
                });
        };
        $scope.getPrediction = function() {
            //redraw the map 
            
            $scope.postProcess();
            $scope.getPredictionCounts();
            
        };
        $scope.postProcess = function(){
            var preProcess = $('#timeInput').val();
            if(preProcess==""){
                alert("the date is empty");
                return;
            }

            var monthProcessed = parseInt(preProcess.split("/",2)[0]);
            var dayProcessed = parseInt(preProcess.split("/",2)[1]);
            var hourToProcess = parseInt(preProcess.split(" ")[1].substring(0, 2));
            var hourProcessed = (preProcess.indexOf("PM")>-1)? (hourToProcess+12):hourToProcess;
            $scope.timeToPass = {month:monthProcessed, day: dayProcessed, hour: hourProcessed};
            //console.log($scope.timeToPass);


        };
        $scope.actualCount = function(){
            console.log($scope);
            var actualCount =$scope.markerId; 
            return actualCount;
        };
        // $scope.getLocations();
        $scope.getPredictionCounts();

    });
