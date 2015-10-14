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
.factory('BikesMtl', BikesMtl);

BikesMtl.$inject = ['$http'];

function BikesMtl($http) {
    var BikesMtl = {
      all: all,
      get: get
    };

    return BikesMtl;

    function all() {
      return $http.get('/bikesmtl/');
    }

    function get(station_id) {
      return $http.get('/bikesmtl/' + station_id);
    }
  }