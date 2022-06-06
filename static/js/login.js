var socket = io();


socket.on('connect', function() {
	console.log("Connected to server")
});

socket.on("message", function(msg){
	console.log(msg);
});

socket.on("custom_message", function(data){
	console.log(data);
})

let user=null;
let pw=null;

function get_send_data(){
	user=document.getElementById("username").value;
	pw=document.getElementById("password").value;
	socket.emit("login", {user, pw})
}