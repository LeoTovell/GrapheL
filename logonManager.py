import hashlib
from dotenv import load_dotenv
from pathlib import Path
import os
import sqlite3
# .env for priv/publ key
# load_dotenv(dotenv_path=Path("sec.env"))

# class LogonManager:
# 	def __init__(self, manager):
# 		self.user_db_manager = manager
# 		self.logged_in_user = None

# 	def validate_user(self, username, unhashed_password):
# 		if self.user_db_manager.get_user_record(username) == None:
# 			return False
# 		else:
# 			hashed_stored_password = self.user_db_manager.get_user_record(username)[2] # id, uname, hpw, email
# 			hashed_password_to_validate = hashlib.sha256(unhashed_password.encode()).hexdigest() #Hash the password + convert to hex to get ready for comparison
# 			if hashed_password_to_validate == hashed_stored_password:
# 				return True
# 		return False

# 	def log_in_user(self, username):
# 		self.logged_in_user = username
# 		# logged_in_user_id = self.user_db_manager.get_id(username)

# 	def register_user(self, username, unhashed_password, role):
# 		hashed_password = hashlib.sha256(unhashed_password.encode()).hexdigest()
# 		id = self.user_db_manager.create_user(username, hashed_password, role)
# 		if id == None:
# 			return False
# 		return True

# 	def log_out_user(self):
# 		self.logged_in_user = None

# 	def get_user(self):
# 		return self.logged_in_user

# 	def is_user_logged_on(self):
# 		if self.logged_in_user == None:
# 			return False
# 		return True

# 	def is_admin(self):
# 		user_role = self.user_db_manager.get_user_record(self.logged_in_user)[4] # id, uname, hpw, email, role
# 		if user_role == "admin":
# 			return True
# 		return False

# from __main__ import set_session

class LogonManager:
	def __init__(self, path):
		self.db_path = path

	def login_user(self, username, password):
		error = "Username not recognised."
		conn = sqlite3.connect(self.db_path)
		cur = conn.cursor()
		cur.execute(f"SELECT * FROM USERS WHERE username='{username}'")
		record = cur.fetchall()
		if record:
			stored_hashed_password = record[0][2] #id, uname, pw, em, role
			hashed_password = hashlib.sha256(password.encode()).hexdigest()
			if hashed_password == stored_hashed_password:
				# set_session("user", username)
				error = None
				return error
			else:
				error = "Password incorrect."
		return error

	def get_user(self):
		return ["leo"]

	def is_logged_in(self):
		return True

	def is_admin(self):
		return True
		user = get_user()
		if user[4] == "admin":
			return True
		else:
			return False