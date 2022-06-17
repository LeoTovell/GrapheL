from __main__ import socketio, logonManager, flashed_messages, get_graph
from flask import redirect, flash, url_for, request

@socketio.on("login")
def form_submit(data):
	sid = request.sid
	username = data["user"]
	password = data["pw"]
	socketio.emit("data recieved", room=sid)
	returned = logonManager.validate_user(username, password)
	if returned == True:
		logonManager.log_in_user(username)
		flashed_messages.append(f"Login Successful, {logonManager.get_user()}!")
		# redirect_to_url("/", sid)
		socketio.emit("redirect", "/", room=sid)
	else:
		flashed_messages.append("Login Unsuccessful, username/password incorrect.")
		# redirect_to_url("/login", sid)
		socketio.emit("redirect", "/login", room=sid)

@socketio.on("register")
def register_user(data):
	sid = request.sid
	username = data["user"]
	password = data["pw"]
	role = data["role"]
	# email = data["email"]
	socketio.emit("recieved registration", request.sid)
	returned = logonManager.register_user(username, password, role)
	if returned == True:
		flashed_messages.append("Registration Successful, welcome to the club!")
		redirect_to_url("/", sid)
	else:
		flashed_messages.append("Registration Failed, username is already taken...")
		redirect_to_url("/register", sid)

@socketio.on("test_sid")
def test_sid(data):
	# print(data, flush=True)
	print(request.sid, flush=True)
	socketio.send("test_message", data, room=request.sid)

@socketio.on("request_graph")
def request_graph():
	print("Graph Requested", flush=True)
	graph = get_graph()
	print(graph.compile_adjacency_list_debug(), flush=True)
	socketio.emit("receive_graph", {"graph": graph.compile_adjacency_list_debug()})

def redirect_to_url(url, sid):
	print(url, flush=True)
	socketio.emit("redirect", url) #room=sid)