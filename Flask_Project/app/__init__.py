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
    from .main_route import main as main_blueprint
    from .register_route import register_blueprint
    from .login_route import login_blueprint

   # main is the home page 
    app.register_blueprint(main_blueprint)
    # register is the registration page 
    app.register_blueprint(register_blueprint)
    #login page
    app.register_blueprint(login_blueprint)


    return app
