angular.module('myApp.ListCtrl', []).
controller('driversController', function($scope, BikesMtl, $interval) {
   	var count = 0;
    var timer=$interval(function(){
    	
        BikesMtl.all().then(
        function putIntoData(response) {

            // body...
            count++;
            $scope.names = response.mtlData;
            var d  = new Date();
            $scope.lastSvcTime = d.toTimeString(); 
            $scope.svcCounter = count
            //alert("Just refreshed!");
            //console.log($scope.names);
        });
      },5000);
    
});
//   $.ajax({
//                     url: "js/Service/bike_server.py",
//                     type: "get",
//                     datatype:"json",
//                     success: function(response){
//                         alert(response.message);
//                         console.log(response.data);
//                     }
//                 });
// });