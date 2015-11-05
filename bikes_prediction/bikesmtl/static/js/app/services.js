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
      all: all,
      get: get
    };

    return BikesMtl;

    function all() {
      // return $http.get('/bikesmtl/');
      return $http.get('/bikesmtl.json');
    }

    function get(station_id) {
      return $http.get('/bikesmtl/' + station_id);
    }
  }