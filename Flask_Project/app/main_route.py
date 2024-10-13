# app/routes.py
from flask import Blueprint, render_template, request, session
from flask_login import login_required
from werkzeug.security import generate_password_hash
from .models import User  # Ensure correct import
from . import db  # Import db to use the SQLAlchemy instance

main = Blueprint('main', __name__)


@main.route('/', methods=[ 'GET'])
@login_required
def home():
    error_messages = session.pop('error_messages', None)  # Retrieve and remove error messages from session
    success_messages = session.pop('success_messages', None)  # Retrieve and remove success messages from session

    return render_template('home.html')

