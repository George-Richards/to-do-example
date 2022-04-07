from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class TaskForm(FlaskForm):
    task_title = StringField('Task Title', validators=[DataRequired(), Length(max=30)])
    description = StringField('Task Description', validators=[Length(max=100)])
    submit = SubmitField('Add to list')
