from __main__ import app, logonManager
from flask import render_template, url_for

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/login")
def login():
	return render_template("login.html")

@app.route("/register")
def register():
	return render_template("register.html")

@app.route("/manage-db")
def manage_database():
	return render_template("manage-db.html", database = "users")

@app.route("/profile")
def profile():
	return render_template("profile.html", user=logonManager.get_user())

@app.route("/graph/<name>")
def graph_all(name):
        return "graph/" + name + " is not yet devloped, contact ask@leotovell.com for more details"
