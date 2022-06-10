

function init(){
	console.log("Starting graph program.")

	// CANVAS CREATION

	var rightDiv = document.getElementById("right-div");
	// var canvas = document.createElement('canvas');

	console.log(rightDiv.offsetWidth)

	var canvas = document.createElement("canvas");

	canvas.id = "canvas";
	canvas.width = rightDiv.offsetWidth;
	canvas.height = rightDiv.offsetHeight;
	
	rightDiv.appendChild(canvas);

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
	gl.strokeText("A", 295, 207)


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