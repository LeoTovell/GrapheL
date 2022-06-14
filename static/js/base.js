function refresh(){
	location.reload();
}

var socket = io()

socket.on("redirect", function(url) {
	console.log("rec:")
	window.location.href = url;
})

// window.setInterval(refresh, 2000);