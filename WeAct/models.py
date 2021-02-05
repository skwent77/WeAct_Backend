from . import db


class Student(db.Model):
    userId = db.Column(db.Integer, primary_key=True)
    pw = db.Column(db.String(20), nullable=False)
    classId = db.Column(db.Integer, db.ForeignKey(
        'classes.classId', ondelete='CASCADE'))


class Tutor(db.Model):
    tutorId = db.Column(db.Integer, primary_key=True)
    pw = db.Column(db.String(20), nullable=False)
    classId = db.Column(db.Integer, db.ForeignKey('classes.classId'))


class Classes(db.Model):
    classId = db.Column(db.Integer, primary_key=True)
    className = db.Column(db.String(20), nullable=True)
    subject = db.Column(db.String(20), nullable=True)
    tutorId = db.Column(db.Integer, db.ForeignKey('tutor.tutorId'))
    students = db.relationship('Student', backref='classes')
    tutors = db.relationship('Tutor', backref='classes')
    lectures = db.relationship('Lecture', backref='classes')


class Lecture(db.Model):
    lectureId = db.Column(db.Integer, primary_key=True)
    classId = db.Column(db.Integer, db.ForeignKey('classes.classId'))
    title = db.Column(db.String(20), nullable=True)
    content = db.Column(db.LargeBinary, nullable=True)
    quizs = db.relationship('Quiz', backref='lecture',
                            uselist=False)   # one-to-one relationship


class Quiz(db.Model):
    quizId = db.Column(db.Integer, primary_key=True)
    lectureId = db.Column(db.Integer, db.ForeignKey(
        'lecture.lectureId', ondelete='CASCADE'))
    question = db.Column(db.String(30), nullable=True)
    answer = db.Column(db.String(30), nullable=True)
    a1 = db.Column(db.String(30), nullable=True)
    a2 = db.Column(db.String(30), nullable=True)
    a3 = db.Column(db.String(30), nullable=True)
    a4 = db.Column(db.String(30), nullable=True)
