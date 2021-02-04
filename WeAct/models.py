from . import db

class Student(db.Model):
    userId = db.Column(db.Integer, primary_key = True)
    pw = db.Column(db.String(20),nullable = False)
    classId = db.Column(db.Integer, db.ForeignKey('classes.classId',ondelete='CASCADE'))
    #classes = db.relationship('Classes',backref=db.backref('class_set'))

class Tutor(db.Model):
    tutorId = db.Column(db.Integer, primary_key = True)
    pw = db.Column(db.String(20),nullable = False)
    classId = db.Column(db.Integer, db.ForeignKey('classes.classId',ondelete='CASCADE'))

class Classes(db.Model):
    classId = db.Column(db.Integer, primary_key = True)
    className = db.Column(db.String(20), nullable = True)
    subject = db.Column(db.String(20), nullable = True)
    tutorId = db.Column(db.Integer, db.ForeignKey('tutor.tutorId'))
    students = db.relationship('Student',backref='classes', lazy=True)
    tutors = db.relationship('Lecture',backref='classes')
    lectures = db.relationship('Lecture',backref='classes')

class Lecture:
    lectureId = db.Column(db.Integer, nullable = False)
    classId = db.Column(db.Integer,db.ForeignKey('classes.classId'))
    title = db.Column(db.String(20),nullable = True)
    content = db.Column(db.String(500),nullable = True)
    quizs = db.relationship('Quiz',backref='lectures', uselist=False)

class Quiz:
    quizId = db.Column(db.Integer, nullable = False)
    lectureId = db.Column(db.Integer, db.ForeignKey('lectures.lectureId', ondelete='CASCADE'))
    question = db.Column(db.String(30),nullable = True)
    answer = db.Column(db.String(30),nullable = True)
    a1 = db.Column(db.String(30),nullable = True)
    a2 = db.Column(db.String(30),nullable = True)
    a3 = db.Column(db.String(30),nullable = True)
    a4 = db.Column(db.String(30),nullable = True)

