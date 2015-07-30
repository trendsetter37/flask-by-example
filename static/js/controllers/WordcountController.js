app.controller('WordcountController', ['$scope', '$log', 'url_service',
 function($scope, $log, url_service){
  
	$scope.getResults = function(){
		$log.log('Input url: '+ $scope.input_url);
		var userInput = $scope.input_url;

		// fire api request
		url_service.getUrlResults(userInput)
      .success(function(data){
        $scope.results = data;
        $scope.chartData = data;
        initChart($scope.chartData);
        // test loop through received json 
        for (var key in data){
        	if (data.hasOwnProperty(key)) {
        		console.log(key + ": " + data[key]);
        	}
        }
      })
      .error(function(data){
        $log.log("There was an error");
      });
	};
}]);
