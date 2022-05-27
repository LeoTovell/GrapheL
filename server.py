from flask import Flask 

app = Flask(__name__)

# Import routes managed in external file (for ease)
import routes

if __name__ == "__main__":
	app.run(debug=True)