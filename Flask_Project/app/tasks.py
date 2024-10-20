from flask import Blueprint
from .models import Task, User
from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import login_required, current_user


tasks_blueprint = Blueprint('tasks', __name__)

@tasks_blueprint.route('/my-tasks', methods=['GET'])
@login_required
def view_tasks():
    tasks = Task.query.filter_by(user_id=current_user.id).all()  # Fetch tasks for the logged-in user
    return render_template('tasks.html', tasks=tasks)  # Render a template with the list of tasks