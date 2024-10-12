from flask import Blueprint, render_template, request


task_blueprint = Blueprint('task', __name__)


# In-memory task list for demonstration
tasks = []

# Route to display the form for creating a new task
@task_blueprint.route('/newTask', methods=['GET'])
def new_task():
    return render_template('newTask.html')