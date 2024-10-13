from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.secret_key = 'info5103'

    # To manage login/logout
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'  # Flask-Login will redirect to this view if not logged in

    # Load configuration
    app.config.from_object('app.config.Config')  # Use the correct path to Config

    # Initialize extensions
    db.init_app(app)

    # Import and register blueprints here to avoid circular import
    from .main_route import main as main_blueprint
    from .register_route import register_blueprint
    from .login_logout_route import login_logout_blueprint
    from .new_task import task_blueprint

    # main is the home page
    app.register_blueprint(main_blueprint)

    # register is the registration page
    app.register_blueprint(register_blueprint)

    # login/logout
    app.register_blueprint(login_logout_blueprint)

    # new task page
    app.register_blueprint(task_blueprint)

    # User loader: This tells Flask-Login how to load a user from an ID (from session)
    from app.models import User  # Avoid circular imports by importing here

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))  # Fetch user from the database by ID

    return app
