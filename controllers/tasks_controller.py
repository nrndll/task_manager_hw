from flask import Flask, render_template, Blueprint, request, redirect
from repositories import task_repository, user_repository
from models.task import Task

tasks_blueprint = Blueprint("tasks", __name__)

# GET '/tasks'
@tasks_blueprint.route("/tasks")
def tasks():
    tasks = task_repository.select_all() # NEW
    return render_template("tasks/index.html", all_tasks=tasks)

# NEW
# GET '/tasks/new'
@tasks_blueprint.route("/tasks/new")
def new_task():
    users = user_repository.select_all()
    return render_template("tasks/new.html", all_users=users)

# CREATE 
# POST '/tasks'
@tasks_blueprint.route("/tasks", methods=["POST"])
def create_task(): 
    description = request.form["description"]
    duration = request.form["duration"]
    completed = request.form["completed"]
    user_id = request.form["user_id"]
    user = user_repository.select(user_id)
    new_task = Task(description, user, duration, completed)
    task_repository.save(new_task)
    return redirect("/tasks")

# SHOW
# GET '/tasks/<id>'

# EDIT
# GET "tasks/<id>/edit"

# UPDATE
# PUT "/tasks/<id>"

# DELETE
# DELETE "/tasks/<id>"
@tasks_blueprint.route("/tasks/<id>/delete", methods=["POST"])
def delete_task(id):
    task_repository.delete(id)
    return redirect("/tasks")