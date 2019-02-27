from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from playground.models import Course, RegisteredStudent
from playground.app import app, db
from config import Config
from flask_migrate import Migrate
from playground.forms import NewCourseForm, RegisteredStudent

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    course_form = NewCourseForm()
    if course_form.validate_on_submit():
        course_class_id = course_form.class_id.data
        course_number = course_form.course_number.data
        course_title = course_form.course_title.data
        return redirect(url_for('add_course', course_class_id=course_class_id, course_number=course_number,course_title=course_title))
    courses = Course.query.all()
    return render_template('index.html', course_form=course_form, courses=courses)

@app.route('/add_course/<course_class_id>/<course_number>/<course_title>', methods=['GET', 'POST']) #Need to pass values in URL parameters. Otherwise error.
def add_course(course_class_id, course_number, course_title):
    course = Course(course_class_id, course_number, course_title)
    db.session.add(course)
    db.session.commit()
    flash('Course Added!')
    courses=Course.query.all()
    return render_template("index.html", course_form=NewCourseForm(), courses=courses)

@app.route("/register_student/<int:course_id>/", methods=['GET'])
def get_register_student():
    course_id = Course.course_id.query.all()
    if id==course_id:
        
    
    return render_template("course_details.html")

@app.route("/register_student/<int:course_id>/", methods=['POST'])
def post_register_student():

    return render_template("course_details.html")