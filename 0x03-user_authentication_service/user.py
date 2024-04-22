from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()


class User(db.Model):
    """user database table"""
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), nullable=False)
    hashed_password = db.Column(db.String(250), nullable=False)
    session_id = db.Column(db.String(250), nullable=True)
    reset_token = db.Column(db.String(250), nullable=True)
