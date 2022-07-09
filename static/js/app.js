var ctx;
var running = true;
var x = y = 200;
var graph;
// Graph = ["node", [x, y], [neighbour, weight], [neighbour, weight], [neighbour, weight]]

function request_graph(){
	// Get canvas dimensions and send to socket
	socket.emit("request_graph");
	console.log("Graph Reqeusted")
}

socket.on("receive_graph", function(data){
	graph = data;
	console.log(JSON.parse(graph))
});

function mousemove(canvas, event){
	var rect = canvas.getBoundingClientRect();

	// console.log("x = " + event.clientX - rect.left);
	// console.log("y = " + event.clientY - rect.top);

	if(event.buttons == 1){
	// console.log("X: " + Math.round(event.clientX - rect.left));
	// console.log("Y: " + Math.round(event.clientY - rect.top));
}
	return {
		x: event.clientX - rect.left,
		y: event.clientY - rect.top
	};
}

function init(){
	console.log("Starting graph program.")
	document.getElementById("initButton").remove()

	// CREATE Canvas


	var app_container = document.getElementById("app-container")
	var canvas = document.createElement("canvas");
	var canvas_div = document.getElementById("canvas-div");

	canvas.id = "canvas";
	canvas.setAttribute("onmousemove", "mousemove(this, event)")
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
	for(var i = 0; i < graph.graph.length; i++){ // Each node
		// Draw the vertex from its coordinate.
		ctx.beginPath();
		ctx.arc(graph.graph[i][1][0], graph.graph[i][1][1], 25, 0, 2 * Math.PI);
		ctx.fillStyle = "white";
		ctx.fill();
		ctx.stroke();
		ctx.closePath();

		for(var j = 2; j < graph.graph[i].length; j++){ // Each edge tuple
			console.log(graph.graph[i][0] + " --" + (graph.graph[i][j][1]).toString() + "--> "+ graph.graph[i][j][0])
			ctx.beginPath();
			ctx.moveTo()

		}
	}
	// console.log(graph.graph.length)
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
}

function hideButton(){
	document.getElementById("initButtonDiv").style.display = "None"
}

function incrementPos(x1, y1){
	x += x1;
	y += y1;
}