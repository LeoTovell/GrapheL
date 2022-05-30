from flask import Flask 
import sqlite3
from graph import Graph
from databaseManager import DatabaseManager
from dotenv import load_dotenv
from logonManager import LogonManager

# This file should mainly only include the core functionality to run the server.

app = Flask(__name__)
if(app != None):
	print(f"App Created Successfully: {app}")

# databases = ["users.db", "graphs.db"]
userDBManager = DatabaseManager("users.db")
graphDBManager = DatabaseManager("graphs.db")
logonManager = LogonManager(userDBManager)

# Import routes managed in external file (for ease) !! MUST BE AFTER APP DEFINITION AND BEFORE SCRIPT RUN !!
import routes

if __name__ == "__main__":
	app.run(debug=True)