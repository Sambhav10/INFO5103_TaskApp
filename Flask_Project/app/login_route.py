# app/login_routes.py
from flask import Blueprint, render_template, request
from werkzeug.security import check_password_hash
from .models import User  # Ensure correct import
from . import db

login_blueprint = Blueprint('login', __name__)

@login_blueprint.route('/login', methods=['POST', 'GET'])

def login():
    error_messages = []
    success_messages = []

    if request.method =="POST":
        #Fetch values from the fields
        email = request.form.get('email')
        password = request.form.get('password')

        #Field validation
        if not all([email, password]):
            error_messages.append("All fields are required.", "error")
            return render_template("login.html", error_messages=error_messages, success_messages=success_messages)

        #Check if the account exists
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            # Successfully logged in
            success_messages.append("Login successful!")
            # Redirect to a protected route or dashboard
            return render_template("main.html", error_messages=error_messages, success_messages=success_messages)
        else:
            error_messages.append("Invalid email or password.")
            return render_template("login.html",error_messages=error_messages)

    elif request.method == "GET":
        return render_template("login.html")