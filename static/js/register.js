var socket = io();

socket.on('connect', function() {
	console.log("Connected to server")
});

socket.on("message", function(msg){
	console.log(msg);
});

function register_user(){
	user = document.getElementById("username").value;
	pw = document.getElementById("password").value;
	role = document.querySelector("input[type='radio'][name=role]:checked").value;
	socket.emit("register", {user, pw, role});
};