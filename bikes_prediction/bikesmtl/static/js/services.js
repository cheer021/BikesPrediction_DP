// angular.module('myApp.services', ['ngResource'])
// .factory('BikesMtl', ['$resource', function($resource) {
//     return $resource('/crud/bikesmtl/', {'id': '@id'}, {
//     });
// }]);

angular.module('myApp.services', [])
.factory('BikesMtl', BikesMtl);

BikesMtl.$inject = ['$http'];

function BikesMtl($http) {
    var BikesMtl = {
      all: all
    };

    return BikesMtl;

    function all() {
      return $http({
        method: 'GET',
        url: '/bikesmtl'
      }).then(function successCallback(response) {
        // this callback will be called asynchronously
        // when the response is available
        return response.data;
      }, function errorCallback(response) {
        // called asynchronously if an error occurs
        // or server returns response with an error status.
          return response.status;
      });
    }


  }