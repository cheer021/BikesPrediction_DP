angular.module('myApp.ListCtrl', []).
controller('driversController', function($scope, bixiAPIservice) {
    $scope.names = [];
    bixiAPIservice.getDrivers().success(
        function putIntoData(response) {

            // body...
            $scope.names = response.mtlStations;
            console.log($scope.names);
        });
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