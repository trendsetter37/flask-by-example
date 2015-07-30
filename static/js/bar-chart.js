function type(d) {
	d.frequency = +d.frequency;
	return d;
}
// fix this below to work with flask app 
function initChart(data) {

	// clear previous data
	d3.select("svg").selectAll("*").remove();

	// Rebuild
	var margin = {top:20,right:30,bottom:30,left:40},
		width = d3.select("svg").parent().width() - margin.left - margin.right,//use to be 960
		height = d3.select("svg").parent().height() - margin.top - margin.bottom; // use to be 500

	var formatPercent = d3.format(".03%");
	// scale functions
	var x = d3.scale.ordinal()
		.rangeRoundBands([0, width], .1);

	var y = d3.scale.linear()
		.range([height, 0]);

	// Axis functions
	var xAxis = d3.svg.axis()
		.scale(x)
		.orient("bottom");

	var yAxis = d3.svg.axis()
		.scale(y)
		.orient("left")
		.ticks(10, "%");

	// setting up tooltip for bars
	var tip = d3.tip()
		.attr("class", "d3-tip")
		.offset([-10, 0])
		.html(function(d) {
			return "<strong>(" + d.word + ") Frequency: </strong> <span style='color:red'>" + d.frequency + "</span>";
		});

	// setting up svg element
	var svg = d3.select("svg")
			.attr("width", width + margin.left + margin.right)
			.attr("height", height + margin.top + margin.bottom)
		.append("g") // group element 
			.attr("transform", "translate(" + margin.left + "," + margin.top + ")"); // positioning g element
	
	// initiate tool-tippage
	svg.call(tip);

	// labels for x axis
	
	 x.domain(data.map(function(d){
	 	return d.word;
	 }));
	 y.domain([0, d3.max(data, function(d){
	 	return d.frequency;
	 })]);

	 // Build x axis g element
	 // Move to bottom of graph where
	 // The x axis should reside
	 svg.append("g")
	 	.attr("class", "x axis")
	 	.attr("transform", "translate(0," + height + ")")
	 	.call(xAxis);

	 // Now for the Y axis
	 svg.append("g")
	 		.attr("class", "y axis")
	 		.call(yAxis)
	 	.append("text")
	 		.attr("transform", "rotate(-90)") // Frequency label
	 		.attr("y", 6)
	 		.attr("dy", ".71em")
	 		.style("text-anchor", "end")
	 		.text("Frequency")

	// Adding bars
	 svg.selectAll(".bar")
	 		.data(data)
	 	.enter().append("rect")
	 		.attr("class", "bar")
	 		.attr("x", function(d){
	 			return x(d.word);
	 		})
	 		.attr("width", x.rangeBand())
	 		.attr("y", function(d){
	 			return y(d.frequency);
	 		})
	 		.attr("height", function(d){
	 			return height - y(d.frequency);
	 		})
	 		.on("mouseover", tip.show)
	 		.on("mouseout", tip.hide);

}