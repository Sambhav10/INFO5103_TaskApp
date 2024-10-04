# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object('app.config.Config')  # Use the correct path to Config

    # Initialize extensions
    db.init_app(app)

    # Import and register blueprints here to avoid circular import
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
