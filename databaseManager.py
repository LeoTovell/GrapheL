import sqlite3

class DatabaseManager:

	connection = None

	def __init__(self, database, table_name):
		#Params: database name
		self.database = database
		conn = sqlite3.connect(self.database)
		# Create USER TABLE
		command = f"CREATE TABLE IF NOT EXISTS {table_name.upper()} (id INTEGER PRIMARY KEY, username TEXT NOT NULL UNIQUE, password TEXT NOT NULL, email TEXT UNIQUE, role TEXT NOT NULL)"
		conn.execute(command)
		conn.commit()
		conn.close()

	def get_cursor(self):
		pass

	def get_table(self, table_name, data):
		table_content = []
		rows = self.get_cursor().execute(f"select * from {table_name}")
		for row in rows:
			table_content.append(row)
		return table_content

	def add_record(self):
		pass

	def find_record(self, table_name):
		command = f"select * from {table_name}"

	def get_user_record(self, username):
		record = None
		connection = sqlite3.connect(self.database)
		cursor = connection.cursor()
		try:
			cursor.execute(f"SELECT * FROM USERS WHERE username='{username}'")
			record = cursor.fetchall()[0] # get user record
		except Exception as e:
			print(e, flush=True)
		connection.close()
		return record

	def delete_record(self):
		pass

	def to_string(self):
		print("database: " + self.database)

	def create_user(self, username, hashed_password, role):
		registered = True
		connection = sqlite3.connect(self.database)
		cursor = connection.cursor()
		try:
			cursor.execute(f"INSERT INTO USERS VALUES(null, '{username}', '{hashed_password}', null, '{role}')")
			connection.commit()
			connection.close()
		except Exception as e:
			print(e, flush=True)
			connection.close()
			registered = False
		return registered
		
