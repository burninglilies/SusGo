from enum import auto
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import datetime
import hashlib
import os

import bcrypt

db = SQLAlchemy()


class User(db.Model):
    """
    User model
    Sellers have a one-to-many relationship with Listings
    Buyers have a many-to-many relationship with Listings
    contact, username, password_digest, session_token, session_expiration, update_token
    """
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False, unique=False)
    points = db.Column(db.Integer, nullable=True, unique=False)
    email = db.Column(db.String, nullable=False)

    # User information
    username = db.Column(db.String, nullable=False, unique=True)
    password_digest = db.Column(db.String, nullable=False)

    # Session information
    session_token = db.Column(db.String, nullable=False, unique=True)
    session_expiration = db.Column(db.DateTime, nullable=False)
    update_token = db.Column(db.String, nullable=False, unique=True)

    def __init__(self, **kwargs):
        """
        initializes User object
        """
        self.name = kwargs.get("name")
        self.email = kwargs.get("email")
        self.points = 0
        self.username = kwargs.get("username", "")
        self.password_digest = bcrypt.hashpw(kwargs.get("password").encode("utf8"), bcrypt.gensalt(rounds=13))
        self.renew_session()
    
    def serialize(self):        
        """
        serialize a User object
        """
        return {      
            "id": self.id,      
            "username": self.username,
            "name": self.name,
            "points": self.points,
            "email": self.email,
        }

    def simple_serialize(self):
        """
        Simple serializes a User object
        """
        return {
            "id": self.id,      
            "username": self.username,
            "points": self.points
        }

    #authentication methods
    def _urlsafe_base_64(self):
        """
        Randomly generates hashed tokens (used for session/update tokens)
        """
        return hashlib.sha1(os.urandom(64)).hexdigest()

    def renew_session(self):
        """
        Renews the sessions, i.e.
        1. Creates a new session token
        2. Sets the expiration time of the session to be a day from now
        3. Creates a new update token
        """
        self.session_token = self._urlsafe_base_64()
        self.session_expiration = datetime.datetime.now() + datetime.timedelta(days=1)
        self.update_token = self._urlsafe_base_64()

    def verify_password(self, password):
        """
        Verifies the password of a user
        """
        return bcrypt.checkpw(password.encode("utf8"), self.password_digest)

    def verify_session_token(self, session_token):
        """
        Verifies the session token of a user
        """
        return session_token == self.session_token and datetime.datetime.now() < self.session_expiration

    def verify_update_token(self, update_token):
        """
        Verifies the update token of a user
        """
        return update_token == self.update_token
