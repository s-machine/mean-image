var margin = {top: 20, right: 20, bottom: 70, left: 40},
    width = 600 - margin.left - margin.right,
    height = 300 - margin.top - margin.bottom;

var svg = d3.select("body")
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)

var beginYear = 1923;
var year = 1967;
var index = year - beginYear;

d3.json("js/time.json",function(error, data){
  
  svg.selectAll("rect")
    .data(data[index].colorList)
    .enter()
    .append("rect")
    .attr("height","2")
    .attr("width","10")
    .attr("x","20")
    .attr("y",function(d,i){ return i*2})
    .attr("fill", function(d,i){return d});
  
  });