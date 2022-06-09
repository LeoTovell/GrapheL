

var init = function(){
	console.log("Starting graph program.")

	// CANVAS CREATION

	var leftDiv = document.getElementById("right-div");
	// var canvas = document.createElement('canvas');

	console.log(leftDiv.offsetWidth)

	var canvas = document.createElement("canvas");

	canvas.id = "canvas";
	canvas.width = leftDiv.offsetWidth;
	canvas.height = leftDiv.offsetHeight;
	
	leftDiv.appendChild(canvas);

	var canvas = document.getElementById("canvas");
	var gl = canvas.getContext("2d");

if (!gl){
	console.log("Your browser does not support webGL without falling back on experimental.")
	// gl = canvas.getContext('experimental-webgl');
	}

if(!gl){
	alert("Your browser does not support webGL")
	}

	// gl.clearColor(0.75, 0.85, 0.8, 1.0);
	// gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);

	// Begin Loop
	// Each iteration get new positions, or if the list is unchanged, skip over.

	gl.beginPath();
	gl.arc(300, 250, 200, 0, 2 * Math.PI);
	gl.stroke();
};


var hideButton = function(){
	document.getElementById("initButton").hidden = true;
}