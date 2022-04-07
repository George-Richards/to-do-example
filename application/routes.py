from application import app
from application.forms import TaskForm
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    form = TaskForm()
    return render_template('add_task.html', form=form)
