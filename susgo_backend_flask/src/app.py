import json
import users_dao
import datetime
from unicodedata import category
from urllib import request

from flask import Flask
from flask import request

from db import db, User

app = Flask(__name__)
db_filename = "profiles.db"


db.init_app(app)
with app.app_context():
    db.create_all()


# generalized response formats
def success_response(data, code=200):
    return json.dumps(data), code

def failure_response(message, code=404):
    return json.dumps({"error": message}), code

def extract_token(request):
    """
    Helper function that extracts the token from the header of a request
    """
    auth_header = request.headers.get("Authorization")
    
    if auth_header is None:
        return False, json.dumps({"Missing authorization header"})

    bearer_token = auth_header.replace("Bearer", "").strip()

    return True, bearer_token


@app.route("/")
def hello_world():
    return json.dumps("Welcome to the Circus, you clown 🤡")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)