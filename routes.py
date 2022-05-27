from __main__ import app
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