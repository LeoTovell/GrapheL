import hashlib
from dotenv import load_dotenv
from pathlib import Path
import os

# .env for priv/publ key
load_dotenv(dotenv_path=Path("sec.env"))

class LogonManager:
	def __init__(self, manager):
		self.user_db_manager = manager
		self.logged_in_user = None

	def validate_user(self, username, unhashed_password):
		if self.user_db_manager.get_user_record(username) == None:
			return False
		else:
			hashed_stored_password = self.user_db_manager.get_user_record(username)[2] # id, uname, hpw, email
			hashed_password_to_validate = hashlib.sha256(unhashed_password.encode()).hexdigest() #Hash the password + convert to hex to get ready for comparison
			if hashed_password_to_validate == hashed_stored_password:
				return True
		return False

	def log_in_user(self, username):
		self.logged_in_user = username
		# logged_in_user_id = self.user_db_manager.get_id(username)

	def register_user(self, username, unhashed_password, role):
		hashed_password = hashlib.sha256(unhashed_password.encode()).hexdigest()
		id = self.user_db_manager.create_user(username, hashed_password, role)
		if id == None:
			return False
		return True

	def log_out_user(self):
		self.logged_in_user = None

	def get_user(self):
		return self.logged_in_user

	def is_user_logged_on(self):
		if self.logged_in_user == None:
			return False
		return True

	def is_admin(self):
		user_role = self.user_db_manager.get_user_record(self.logged_in_user)[4] # id, uname, hpw, email, role
		if user_role == "admin":
			return True
		return False