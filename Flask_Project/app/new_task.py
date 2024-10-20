from datetime import date
from typing import Optional
from wsgiref.validate import validator
from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import login_required, current_user

from .models import Task
from . import db

# Flask-WTF for data validations
from flask_wtf import FlaskForm
from wtforms import DateTimeField, StringField, TextAreaField, DateField
from wtforms.validators import DataRequired, Length, Optional


task_blueprint = Blueprint('task', __name__)


class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=5, max=100)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=10, max=250)])
    due_date = DateTimeField('Due Date', format='%Y-%m-%dT%H:%M', validators=[Optional()])  # Use Optional as a list



# Route to display the form for creating a new task
@task_blueprint.route('/newTask', methods=['GET', 'POST'])
@login_required
def new_task():
    form = TaskForm()

    if request.method == "POST":
        if form.validate_on_submit():
            # Process the valid form data
            task = Task(
                title=form.title.data,
                description=form.description.data,
                due_date=form.due_date.data if form.due_date.data else None,  # Set to None if empty
                user_id=current_user.id
            )
            db.session.add(task)
            db.session.commit()
            return redirect(url_for('main.home'))

    # For GET or invalid POST, render the form with errors if any
    return render_template("newTask.html", form=form)

