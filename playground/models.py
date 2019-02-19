from flask_sqlalchemy import SQLAlchemy
from playground import routes, models

db = SQLAlchemy()

class Course(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    course_number = db.Column(db.String, nullable = False)
    course_title = db/Column(db.String, nullable = False)

class RegisteredStudent(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Integer, nullable = False)
    grade = db.Column(db.Integer, nullable = False)
