# routes.py
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from .models import User
from . import db

main = Blueprint('main', __name__)

@main.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    phone = data.get('phone')
    email = data.get('email')
    password = data.get('password')
    gender = data.get('gender')
    date_of_birth = data.get('dateOfBirth')

    # Simple validation
    if not all([first_name, last_name, phone, email, password, gender, date_of_birth]):
        return jsonify({"error": "All fields are required."}), 400

    # Check if email already exists
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"error": "Email already exists."}), 400

    # Insert new user
    hashed_password = generate_password_hash(password)
    new_user = User(first_name=first_name, last_name=last_name, phone=phone,
                    email=email, password=hashed_password, gender=gender,
                    date_of_birth=date_of_birth)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Registration successful!"}), 201
