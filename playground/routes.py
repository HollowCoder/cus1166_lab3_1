from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from playground.models import Course, RegisteredStudent
from playground.app import app
from config import Config
from flask_migrate import Migrate

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    physics_course = Course(id=1001, course_number='1001', course_title='Physics')
    biology_course = Course(id=1002, course_number='1002', course_title='Biology')
    chemistry_course = Course(id=1003, course_number='1003', course_title='Chemistry')
    courses = Course.query.all()
    return render_template('index.html', courses=courses)

@app.route("/add_course/")
def add_course():

    return render_template("index.html")

@app.route("/register_student/", methods=['GET','POST'])
def register_student():

    return render_template()