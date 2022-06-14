from __main__ import app, logonManager, userDBManager, graphDBManager, flashed_messages
from flask import render_template, url_for, redirect
# from sockets import redirect_to_url

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    # returns a 200 (not a 404) with the following contents:
    return f"Page not found, www.leotovell.co.uk/{path}"

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/login")
def login():
	if logonManager.is_user_logged_on():
		flashed_messages.append("You're already logged on!")
		return redirect(url_for("profile"))
	return render_template("login.html")

@app.route("/register")
def register():
	if logonManager.is_user_logged_on():
		flashed_messages.append("You're already logged on!")
		return redirect(url_for("profile"))
	return render_template("register.html")

@app.route("/manage-db")
def manage_database():
	return render_template("manage-db.html", manager = userDBManager)

@app.route("/profile")
def profile():
	if not logonManager.is_user_logged_on():
		flashed_messages.append("You must be logged in to access your profile.")
		return redirect(url_for("login"))
	return render_template("profile.html")

# Updates - Provides link to github and project updates/progress | NO Validation needed
@app.route("/updates")
def updates():
	return render_template("updates.html")

# Tutorial - Provides examples and describes each feature | NO Validation needed
@app.route("/tutorial")
def tutorial():
	return render_template("tutorial.html")

# Admin - Provides access to admin functions, eg: global user + graph management | Is logged in? Is admin?
@app.route("/admin")
def admin():
	if logonManager.is_user_logged_on():
		if not logonManager.is_admin():
			flashed_messages.append("You don't have the required privileges to access /admin")
			return redirect(url_for("index"))
		else:
			return render_template("admin.html")
	else:
		flashed_messages.append("You need to log in before accessing /admin")
		return redirect(url_for("login"))

@app.route("/logout")
def logout():
	if logonManager.get_user() != None:
		logonManager.log_out_user()
		flashed_messages.append("Logged out!")
	else:
		flashed_messages.append("You must be logged in to log out!")
	return redirect(url_for("index"))

@app.route("/graph/<name>")
def graph_all(name):
	flashed_messages.append(f"www.leotovell.com/graph/{name} was not found on the server")
	return redirect(url_for("index"))

@app.route("/graph/app")
def graph_app():
	return render_template("app.html")