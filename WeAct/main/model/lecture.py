from WeAct import db
class Lecture(db.Model):
    lectureId = db.Column(db.Integer, primary_key=True)
    classId = db.Column(db.Integer, db.ForeignKey('classes.classId'))
    title = db.Column(db.String(20), nullable=True)
    content = db.Column(db.LargeBinary, nullable=True)
    quizs = db.relationship('Quiz', backref='lecture',
                            uselist=False)   # one-to-one relationship