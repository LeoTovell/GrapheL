function refresh(){
	location.reload();
}

var socket = io()

socket.on("redirect", function(url) {
	window.location.href = url;
})

// window.setInterval(refresh, 2000);