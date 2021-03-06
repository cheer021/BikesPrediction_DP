angular.module('myApp.services', [])
.factory('BikesMtl', BikesMtl);

BikesMtl.$inject = ['$http'];

function BikesMtl($http) {
    var BikesMtl = {
      allInfo: getAllStationInfo,
      allActual: getAllActual,
      allPredictions: getAllPredictions,
    };

    return BikesMtl;

    function getAllStationInfo() {
      return $http({
        method: 'GET',
        url: '/bikesmtl/stations/all/info'
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

    // function getStationInfo(stationId) {
    //   return $http({
    //     method: 'GET',
    //     url: '/bikesmtl/stations/' + stationId + '/info'
    //   }).then(function successCallback(response) {
    //     // this callback will be called asynchronously
    //     // when the response is available
    //     return response.data;
    //   }, function errorCallback(response) {
    //     // called asynchronously if an error occurs
    //     // or server returns response with an error status.
    //       return response.status;
    //   });
    // }

    // function getAllDataNow() {
    //   return $http({
    //     method: 'GET',
    //     url: '/bikesmtl/stations/all/now'
    //   }).then(function successCallback(response) {
    //     // this callback will be called asynchronously
    //     // when the response is available
    //     return response.data;
    //   }, function errorCallback(response) {
    //     // called asynchronously if an error occurs
    //     // or server returns response with an error status.
    //       return response.status;
    //   });
    // }

    // function getStationDataNow(stationId) {
    //   return $http({
    //     method: 'GET',
    //     url: '/bikesmtl/stations/' + stationId + '/now'
    //   }).then(function successCallback(response) {
    //     // this callback will be called asynchronously
    //     // when the response is available
    //     return response.data;
    //   }, function errorCallback(response) {
    //     // called asynchronously if an error occurs
    //     // or server returns response with an error status.
    //       return response.status;
    //   });
    // }

    function getAllActual(month, day, hour) {
      return $http({
        method: 'GET',
        url: '/bikesmtl/stations/all/actual/' + month + '/' + day + '/' + hour
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

    function getAllPredictions(month, day, hour) {
      return $http({
        method: 'GET',
        url: '/bikesmtl/stations/all/predictions/' + month + '/' + day + '/' + hour
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

    // function getStationPredictions(stationId) {
    //   return $http({
    //     method: 'GET',
    //     url: '/bikesmtl/stations/' + stationId + '/predictions'
    //   }).then(function successCallback(response) {
    //     // this callback will be called asynchronously
    //     // when the response is available
    //     return response.data;
    //   }, function errorCallback(response) {
    //     // called asynchronously if an error occurs
    //     // or server returns response with an error status.
    //       return response.status;
    //   });
    // }

}