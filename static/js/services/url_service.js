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
					console.log('data received from service: ' + data);
					for (prop in data){

						console.log(prop + ': ' + data[prop]);
					}
					return data;
				})
				.error(function(err){
					console.log('errors received from service: ' + err);
					return err;
				});
		}
	};
}]);
