app.controller('WordcountController', ['$scope', '$log', 'url_service',
 function($scope, $log, url_service){
  
	$scope.getResults = function(){
		$log.log('Input url: '+ $scope.input_url);
		var userInput = $scope.input_url;

		// fire api request
		url_service.getUrlResults(userInput)
      .success(function(data){
        $scope.results = data;
      })
      .error(function(data){
        $log.log("There was an error");
      });
	};
}]);
