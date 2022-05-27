from flask import Flask 
import sqlite3
from graph import Graph
from databaseManager import DatabaseManager

# This file should mainly only include the core functionality to run the server.

app = Flask(__name__)
if(app != None):
	print(f"App Created Successfully: {app}")

# databases = ["users.db", "graphs.db"]
userManager = DatabaseManager("users.db")
graphManager = DatabaseManager("graphs.db")

graph = Graph("leo")
graph.create_default_values()

# Import routes managed in external file (for ease) !! MUST BE AFTER APP DEFINITION AND BEFORE SCRIPT RUN !!
import routes

if __name__ == "__main__":
	app.run(debug=True)