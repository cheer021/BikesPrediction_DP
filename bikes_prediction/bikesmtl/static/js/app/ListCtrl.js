// angular.module('myApp.ListCtrl', []).
// controller('driversController', ['$scope', 'BikesMtl', function ($scope, BikesMtl) {
//     // Query returns an array of objects, BikesMtl.objects.all() by default
//     $scope.names = BikesMtl.query();

//     // Getting a single object
//     // var model = BikesMtl.get({pk: 1});

// }]);

angular.module('myApp.ListCtrl', []).
controller('driversController', function($scope, BikesMtl) {
    $scope.names = [];
    BikesMtl.all().success(
        function (response) {
            // body...
            $scope.names = response.mtlData;
            console.log($scope.names);
        });
    $scope.$apply();
});
