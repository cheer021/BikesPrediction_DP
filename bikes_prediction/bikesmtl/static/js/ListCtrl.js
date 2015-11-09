angular.module('myApp.ListCtrl', []).
controller('driversController', function($scope, $interval, BikesMtl) {
	var count = 0;
    var timer=$interval(function(){
    	
        BikesMtl.all().then(
        function putIntoData(response) {
            // body...
            count++;
            $scope.bikes = {};
            $scope.bikes.predictions = response.mtlData;
            console.log($scope.bikes.predictions);
            var d  = new Date();
            $scope.lastSvcTime = d.toTimeString(); 
            $scope.svcCounter = count
            //alert("Just refreshed!");
            //console.log($scope.names);
        });

      },5000);


});
