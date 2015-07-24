app.controller('WordcountController', ['$scope', '$log', 'url_service',
 function($scope, $log, url_service){
	$scope.getResults = function(){
		$log.log('test: '+ $scope.input_url);
		//console.log('get result performed');

		//gettin input from the user
		var userInput = $scope.input_url;

		// fire api request

		$scope.results = url_service.getUrlResults(userInput);
		$log.log('results: ' + $scope.results);
    $lot.log('listing the results:');
    for (key in $scope.results) {
      $log.log(key + ': ' + $scope.results[key]);
    }
	};
}]);
