from __main__ import socketio, logonManager, flashed_messages
from flask import redirect, flash, url_for

@socketio.on("login")
def form_submit(data):
	username = data["user"]
	password = data["pw"]
	socketio.send("data recieved")
	returned = logonManager.validate_user(username, password)
	if returned == True:
		logonManager.log_in_user(username)
		flashed_messages.append(f"Login Successful, {logonManager.get_user()}!")
		redirect_to_url("/")
	else:
		flashed_messages.append("Login Unsuccessful, username/password incorrect.")
		redirect_to_url("/login")

@socketio.on("register")
def register_user(data):
	username = data["user"]
	password = data["pw"]
	role = data["role"]
	# email = data["email"]
	socketio.send("recieved registration")
	returned = logonManager.register_user(username, password, role)
	if returned == True:
		flashed_messages.append("Registration Successful, welcome to the club!")
		redirect_to_url("/")
	else:
		flashed_messages.append("Registration Failed, username is already taken...")
		redirect_to_url("/register")



def redirect_to_url(url):
	# socketio.emit("redirect", "/graph/asuhdasd")
	socketio.emit("redirect", url)