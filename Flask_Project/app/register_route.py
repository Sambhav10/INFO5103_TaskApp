# app/register_routes.py
from flask import Blueprint, render_template, request
from werkzeug.security import generate_password_hash
from .models import User  # Ensure correct import
from . import db

register_blueprint = Blueprint('register', __name__)

@register_blueprint.route('/register', methods=['POST', 'GET'])

def register():
    error_messages = []
    success_messages = []

    if request.method == "POST":
        # Collect data
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        phone = request.form.get('phone')
        email = request.form.get('email')
        password = request.form.get('password')
        gender = request.form.get('gender')
        date_of_birth = request.form.get('dateOfBirth')

        # Simple validation
        if not all([first_name, last_name, phone, email, password, gender
                    ]):
            error_messages.append("All fields are required.")
            return render_template("register.html", error_messages=error_messages, success_messages=success_messages)

        # Check if email already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            error_messages.append("Email already exists.")
            return render_template("register.html", error_messages=error_messages, success_messages=success_messages)

        # Insert new user
        try:
            hashed_password = generate_password_hash(password)
            new_user = User(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                password=hashed_password,
                gender=gender,
       
            )
            db.session.add(new_user)
            db.session.commit()
            success_messages.append("User registered successfully.")
            return render_template("register.html", error_messages=error_messages, success_messages=success_messages)
        except Exception as e:
            print(f"Exception while trying to register user: {e}")
            error_messages.append(f"Could not register user. {e}")
            return render_template("register.html", error_messages=error_messages, success_messages=success_messages)

    elif request.method == "GET":
        return render_template("register.html", error_messages=error_messages, success_messages=success_messages)
