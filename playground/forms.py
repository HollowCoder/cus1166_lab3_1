from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired

class NewCourseForm(FlaskForm):
    class_id = IntegerField('Class ID:', validators=[DataRequired()])
    course_number = IntegerField('Course Number:', validators=[DataRequired()])
    course_title = StringField('Course Title:', validators=[DataRequired()])
    submit = SubmitField('Submit')

class RegisteredStudent(FlaskForm):
    id = IntegerField('Student ID:', validators=[DataRequired()])
    name = StringField('Student Name:', validators=[DataRequired()])
    grade = StringField('Student Grade:', validators=[DataRequired()])
    submit = SubmitField('Submit')