

function mousemove(canvas, event){
	var rect = canvas.getBoundingClientRect();

	// console.log("x = " + event.clientX - rect.left);
	// console.log("y = " + event.clientY - rect.top);

	if(event.buttons == 1){
	console.log("X: " + Math.round(event.clientX - rect.left));
	console.log("Y: " + Math.round(event.clientY - rect.top));
}
	return {
		x: event.clientX - rect.left,
		y: event.clientY - rect.top
	};
}

function init(){
	console.log("Starting graph program.")
	document.getElementById("initButton").remove()

	// CANVAS CREATION

	// var rightDiv = document.getElementById("canvas-container");
	// // var canvas = document.createElement('canvas');

	// console.log(rightDiv.offsetWidth)
	// console.log(rightDiv.offsetHeight)

	
	
	// rightDiv.appendChild(canvas);


	// CREATE UI

	// var app_container = document.createElement("div");
	var app_container = document.getElementById("app_container")
	var control_div = document.createElement("div");
	var canvas_div = document.createElement("div");
	var canvas = document.createElement("canvas");

	canvas.id = "canvas";
	canvas.setAttribute("onmousemove", "mousemove(this, event)")

	control_div.id = "controls-container";
	canvas_div.id = "canvas-container";
	// app_container.id = "page-container";

	// app_container.style = "padding: 20px; display: flex; align-items: stretch; height: 100%; position: relative"
	control_div.style = "float:left; border: 2px solid red; position: relative; height: 100%; width: 18%";
	canvas_div.style = "float:right; border: 2px solid green; margin-left: 10px; position: relative; height: 100%; width: 78%";


	app_container.appendChild(control_div);
	app_container.appendChild(canvas_div);
	document.body.appendChild(app_container);

	canvas.width = canvas_div.offsetWidth;
	canvas.height = canvas_div.offsetHeight;
	canvas_div.appendChild(canvas)

	var gl = canvas.getContext("2d");

if (!gl){
	console.log("Your browser does not support webGL without falling back on experimental.")
	gl = canvas.getContext('experimental-webgl');
	}

if(!gl){
	alert("Your browser does not support webGL")
	}

	// gl.clearColor(0.75, 0.85, 0.8, 1.0);
	// gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);

	// Begin Loop
	// Each iteration get new positions, or if the list is unchanged, skip over.

	gl.beginPath();
	gl.moveTo(300, 200);
	gl.lineTo(500, 400);
	gl.stroke();
	gl.closePath();

	gl.beginPath();
	gl.arc(300, 200, 25, 0, 2 * Math.PI); // X, Y, radius
	gl.fillStyle = "white"
	gl.fill()
	gl.stroke();
	gl.closePath();

	gl.font = "20px serif";
	gl.strokeText("A", 293, 207)


	gl.beginPath();
	gl.arc(500, 400, 25, 0, 2 * Math.PI); // X, Y, radius
	gl.fillStyle = "white"
	gl.fill()
	gl.stroke();
	gl.closePath();

	gl.strokeText("B", 495, 408)


}


function hideButton(){
	document.getElementById("initButtonDiv").style.display = "None"
}