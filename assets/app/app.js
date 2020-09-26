var myApp=angular.module('myApp',[])

myApp.controller('appController',['$scope',function($scope){
  $scope.eleves=[
    { name:"fateh",
      age:15
    },
    { name:"houssam",
      age:18
    },
    { name:"nouno",
      age:19
    },
    { name:"moha",
      age:20
    }
  ];
}]);
