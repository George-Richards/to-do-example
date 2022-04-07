from application import app, db
from application.forms import TaskForm
from application.models import Tasks
from flask import render_template, request, redirect, url_for

@app.route('/')
def index():
    all_tasks = Tasks.query.all()
    return render_template('index.html', all_tasks=all_tasks)

@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    form = TaskForm()
    if request.method == "POST":
        task = Tasks(task_title=form.task_title.data,
        description=form.description.data)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('add_task.html', form=form)
