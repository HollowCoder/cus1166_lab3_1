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
        flash('Sucess 1')
        return redirect(url_for('add_course', course_form=course_form))
    courses = Course.query.all()
    return render_template('index.html', course_form=course_form)

@app.route("/add_course/", methods=['GET','POST'])
def add_course(course_form):
    flash('Sucess 2')
    course_form = Course(course_form.class_id.data, course_form.course_number.data, course_form.course_title.data)
    db.session.add(course)
    db.session.commit()
    flash('Course Added!')
    return render_template("index.html")

@app.route("/register_student/<int:course_id>/", methods=['GET','POST'])
def register_student():

    return render_template()