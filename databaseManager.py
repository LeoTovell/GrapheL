import sqlite3

class DatabaseManager:
	def __init__(self, database):
		#Params: database name
		self.database = database
		conn = sqlite3.connect(database)
		conn.close()

	def connect(self):
		self.connection = sqlite3.connect(self.database)
		

	def disconnect(self):
		self.connection.close()

	def add_record(self):
		pass

	def find_record(self):
		pass

	def delete_record(self):
		pass

	def to_string(self):
		print("database: " + this.database)

