# app/login_routes.py
from flask import Blueprint, redirect,session, render_template, request, url_for
from flask_login import login_required, login_user, logout_user
from werkzeug.security import check_password_hash
from .models import User  # Ensure correct import
from . import db

login_logout_blueprint = Blueprint('login_logout', __name__)

@login_logout_blueprint.route('/login', methods=['POST', 'GET'])
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

            # Login user
            login_user(user) # This logs the user in and stores their ID in the session
           
            # Redirect to home page
            session['success_messages'] = ['Login successful!']  # Store success message in session
            return redirect(url_for('main.home'))  # Redirect to home after login
      
        else:
            error_messages.append("Invalid email or password.")
            return render_template("login.html",error_messages=error_messages)

    elif request.method == "GET":
        return render_template("login.html")
    
@login_logout_blueprint.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return render_template("logout.html")