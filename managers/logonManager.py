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
		hashed_password_to_validate = hashlib.sha256(unhashed_password.encode()).hexdigest() #Hash the password + convert to hex to get ready for comparison
		hashed_stored_password = self.manager.get_hashed_password(username)
		if hashed_password_to_validate == hashed_stored_password:
			return True
		return False

	def log_in_user(self, username):
		logged_in_user = username
		logged_in_user_id = self.user_db_manager.get_id(username)

	def register_user(self, username, hashed_password):
		id = manager.create_user(username, hashed_password)
		if id == none:
			return False
		return True

	def get_user(self):
		return self.logged_in_user