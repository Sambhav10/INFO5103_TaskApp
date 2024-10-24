# app/models.py
from flask_login import UserMixin
from . import db

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.String(10), nullable=False)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    
    # Nullable due date field
    due_date = db.Column(db.DateTime, nullable=True) 

    # Foreign key to link the task to a user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


