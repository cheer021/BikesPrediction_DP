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
      return $http({
        method: 'GET',
        url: '../js/service/data.json'
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

    function get(station_id) {
      return $http.get('/bikesmtl/' + station_id);
    }
  }