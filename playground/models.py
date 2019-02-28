from flask_sqlalchemy import SQLAlchemy
from playground.app import db

class Course(db.Model):
    course_id = db.Column(db.Integer, primary_key = True)
    course_number = db.Column(db.Integer, nullable = False)
    course_title = db.Column(db.String, nullable = False)
    students = db.relationship('RegisteredStudent')

    def __init__(self, course_id, course_number, course_title):
        self.course_id = course_id
        self.course_number = course_number
        self.course_title = course_title
        
class RegisteredStudent(db.Model):
    student_id = db.Column(db.Integer, primary_key = True)
    student_name = db.Column(db.Integer, nullable = False)
    student_grade = db.Column(db.Integer, nullable = False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), nullable=False)