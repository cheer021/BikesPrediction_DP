// define(["jquery","angular"], function(){


//  $.ajax({
//                         url: "../bike_server.py",
//                         type: "get",
//                         datatype:"json",
//                         success: function(response){
//                             alert(response.message);
//                             console.log(response);
//                         }
//                     });

// });
/**
 *  Module
 *
 * Description
 */
/**
 *  Module
 *
 * Description
 */
angular.module('myApp.services', [])
.factory('StationDataServiceMtl', StationDataServiceMtl);

StationDataServiceMtl.$inject = ['$http'];

function StationDataServiceMtl($http) {
    var BikesMtl = {
      all: all,
      get: get
    };

    return BikesMtl;

    function all() {
      return $http.get('/api/v1/bikedatanow/');
    }

    function get(station_id) {
      return $http.get('/api/v1/bikedatanow/' + station_id);
    }
  }