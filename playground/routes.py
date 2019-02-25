from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from playground.models import Course, RegisteredStudent
from playground.app import app, db
from config import Config
from flask_migrate import Migrate
from playground.forms import NewCourseForm, RegisteredStudent

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    #physics_course = Course(id=1001, course_number='1001', course_title='Physics')
    #biology_course = Course(id=1002, course_number='1002', course_title='Biology')
    #chemistry_course = Course(id=1003, course_number='1003', course_title='Chemistry')

    course_form = NewCourseForm()
    if course_form.validate_on_submit():
        return redirect(url_for('add_course', course_form))
    courses = Course.query.all()
    return render_template('index.html', courses=courses, course_form=course_form)

@app.route("/add_course/", methods=['POST'])
def add_course(course_form):
    db.session.add(course_form)
    return render_template("index.html")

@app.route("/register_student/<int:course_id>/", methods=['GET','POST'])
def register_student():

    return render_template()