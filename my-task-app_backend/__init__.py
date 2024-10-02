# __init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from routes import main as main_blueprint

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)  # Allow cross-origin requests

    # Load configuration
    app.config.from_object('config.Config')

    # Initialize extensions
    db.init_app(app)

    # Register blueprints
   
    app.register_blueprint(main_blueprint)

    return app
