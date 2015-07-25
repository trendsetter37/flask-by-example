/*app.factory('url_service', ['$http', function($http, userInput){
	return $http.post('/start', {"url": userInput})
		.success(function (results) {
			return results;
		})
		.error(function(err){
			return err;
		});
}]);*/

app.factory('url_service', ['$http', function($http){
	return {
		getUrlResults: function(userInput){
			return $http.post('/start', {'url': userInput})
				.success(function(data){
					return data;
				})
				.error(function(err){
					return err;
				});
		}
	};
}]);
