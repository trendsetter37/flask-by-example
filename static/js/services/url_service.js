
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
