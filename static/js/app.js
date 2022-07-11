var ctx;
var running = true;
var x = y = 200;
var graph;
var edge_color = "#000000";
var vertex_color = "#ffffff";
var bg_colour = "#ffffff";
var edge_width = 1;
var customisation_form;

function request_graph(){
	width = ctx.canvas.width;
	height = ctx.canvas.height;
	socket.emit("request_graph", {width, height});
	console.log("Graph Reqeusted")
}

socket.on("receive_graph", function(data){
	graph = JSON.parse(data.graph);
	// console.log(graph)
	draw_graph()
});

function mousemove(event){
	var rect = canvas.getBoundingClientRect();
	create_vertex(event.clientX - rect.left, event.clientY - rect.top);
}
	// return {
	// 	x: event.clientX - rect.left,
	// 	y: event.clientY - rect.top
	// };

function init(){
	console.log("Starting graph program.")
	document.getElementById("initButton").remove()

	// CREATE Canvas


	var app_container = document.getElementById("app-container")
	var canvas = document.createElement("canvas");
	var canvas_div = document.getElementById("canvas-div");

	canvas.id = "canvas";
	// canvas.setAttribute("onmousemove", "mousemove(this, event)")
	canvas.addEventListener("click", function(event) {mousemove(event)}, false)
	canvas.width = canvas_div.offsetWidth;
	canvas.height = canvas_div.offsetHeight;
	canvas_div.appendChild(canvas)

	ctx = canvas.getContext("2d");

if (!ctx){
	console.log("Your browser does not support webctx without falling back on experimental.")
	ctx = canvas.getContext('experimental-webctx');
	}

if(!ctx){
	alert("Your browser does not support webctx")
	}

	// ctx.clearColor(0.75, 0.85, 0.8, 1.0);
	// ctx.clear(ctx.COLOR_BUFFER_BIT | ctx.DEPTH_BUFFER_BIT);

	// Begin Loop
	// Each iteration get new positions, or if the list is unchanged, skip over.

	canvas_clear()

	ctx.beginPath();
	ctx.moveTo(300, 200);
	ctx.lineTo(500, 400);
	ctx.stroke();
	ctx.closePath();

	ctx.beginPath();
	ctx.arc(300, 200, 25, 0, 2 * Math.PI); // X, Y, radius
	ctx.fillStyle = "white"
	ctx.fill()
	ctx.stroke();
	ctx.closePath();

	ctx.font = "20px serif";
	ctx.strokeText("A", 293, 207)


	ctx.beginPath();
	ctx.arc(500, 400, 25, 0, 2 * Math.PI); // X, Y, radius
	ctx.fillStyle = "white"
	ctx.fill()
	ctx.stroke();
	ctx.closePath();

	ctx.strokeText("B", 495, 408)


}

function draw_graph(){
	for (const node in graph){
		for(var element in graph[node]){
			if(!Boolean(element === "x" | element === "y")){
				ctx.beginPath()
				ctx.moveTo(graph[node]["x"], graph[node]["y"]);
				ctx.lineTo(graph[element]["x"], graph[element]["y"]);
				ctx.lineWidth = edge_width;
				ctx.fillStyle = edge_color;
				ctx.strokeStyle = edge_color
				ctx.stroke();
				ctx.closePath();
			}
		}
	}
	for (const node in graph){
		ctx.beginPath();
		ctx.arc(graph[node]["x"], graph[node]["y"], 20, 0, 2 * Math.PI);
		ctx.fillStyle = vertex_color;
		ctx.lineWidth = 1;
		ctx.strokeStyle = "black"
		ctx.fill();
		ctx.stroke();
		ctx.closePath();

		ctx.strokeText(node, graph[node]["x"] - 5, graph[node]["y"] + 8);
	}
}

function canvas_draw_square(){
	ctx.beginPath();
	ctx.rect(x, y, 200, 200);
	ctx.fillStyle = "black";
	ctx.fill()
	ctx.stroke();
	ctx.closePath();
}

function canvas_clear(){
	ctx.clearRect(0, 0, canvas.width, canvas.height);
	ctx.fillStyle = bg_colour;
	ctx.fillRect(0, 0, canvas.width, canvas.height);
}

function hideButton(){
	document.getElementById("initButtonDiv").style.display = "None"
}

function incrementPos(x1, y1){
	x += x1;
	y += y1;
}

function update_customisation(){
	customisation_form = document.getElementById("customisation_form");
	vertex_color = customisation_form.elements.vertexcolorpicker.value;
	edge_color = customisation_form.elements.edgecolorpicker.value;
	bg_colour = customisation_form.elements.bgcolorpicker.value;
	edge_width = customisation_form.elements.edgewidth.value;
	canvas_clear();
	draw_graph();
	// return false;
}

function create_vertex(x, y){
	console.log(x)
	socket.emit("create_vertex", {x, y});
}