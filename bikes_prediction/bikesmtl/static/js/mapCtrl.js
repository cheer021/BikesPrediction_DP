angular.module('myApp.mapCtrl', ['ngMap'])
    .controller('mapController', function($scope, BikesMtl) {
        $scope.stations = {};
        
        $scope.$on('mapInitialized', function(evt, map) {
            //var infoWindow = map.infoWindows[1];

            $scope.zoomChanged = function(e) {
                //infoWindow.setContent('Predition: ' + 12);
               // map.setCenter(infoWindow.getPosition());
            }

        });
     	var empDocksCounts= [];
     	var icon_prefix='http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=';
     	var icon_end = '|00FF00|000000';
     	$scope.getBikeCounts = function(){
     		console.log("0");
        	BikesMtl.allDataNow().then(
        		function(response) {
        			
        			for(var s of response.mtlData){
                    	//console.log(s);
                    	empDocksCounts.push(s.nbEmptyDocks);
                    }
                    //console.log("1");
                    //$scope.stations.locations=locations;
                    //$scope.stations.locations["count"] = empDocksCounts;
                    //console.log(empDocksCounts) ;
                    
        		}).then(function(){
        			$scope.getLocations();
        		});
       };
        $scope.getLocations = function() {
            BikesMtl.allInfo().then(
                function(response) {
 
        			var locations = [];
        			var index=0;
        			//$scope.getBikeCounts();
        			//console.log("2");
        			//console.log(empDocksCounts);
                    for(var s of response.mtlData){
                    	//console.log(s);
                    	locations.push({location:s.latitude.toString()+","+s.longitude.toString(),icon:icon_prefix+empDocksCounts[index]+icon_end});
                    	index++;
                    }
                    $scope.stations.locations=locations;
                   //console.log(empDocksCounts);
                });
        };
        
        
        $scope.getBikeCounts();
        
        
    });