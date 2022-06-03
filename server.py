from flask import Flask 
import sqlite3
from graph import Graph
from databaseManager import DatabaseManager
from dotenv import load_dotenv
from logonManager import LogonManager
from flask_socketio import SocketIO

# This file should mainly only include the core functionality to run the server.
 
app = Flask(__name__)
app.config["SECRET_KEY"] = "key"
socketio = SocketIO(app)

# databases = ["users.db", "graphs.db"]
userDBManager = DatabaseManager("users.db", "users")
graphDBManager = DatabaseManager("graphs.db", "graphs")
logonManager = LogonManager(userDBManager)
flashed_messages = []

# userDBManager.create_user("testUssser", "password123")

@app.context_processor
def inject_stage_and_region():
    return dict(logon_manager = logonManager, flashed_messages = flashed_messages)

# Import routes managed in external file (for ease) !! MUST BE AFTER APP DEFINITION AND BEFORE SCRIPT RUN !!
import routes
import sockets

if __name__ == "__main__":
	socketio.run(app, debug=True)
	# app.run(debug=True)
