angular.module('myApp.ListCtrl', []).
controller('driversController', function($scope, StationDataServiceMtl) {
    $scope.names = [];
    StationDataServiceMtl.all().success(
        function putIntoData(response) {

            // body...
            $scope.names = response.mtlData;
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