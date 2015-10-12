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
angular.module('myApp.services', []).
factory('bixiAPIservice', function($http) {
    var bixiAPI = {};
    bixiAPI.getDrivers = function() {
        return $http({
            method: 'GET',
            url: 'js/service/data.json'
        });
    }

    return bixiAPI;
});