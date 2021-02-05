from WeAct import db
class Classes(db.Model):
    classId = db.Column(db.Integer, primary_key=True)
    className = db.Column(db.String(20), nullable=True)
    subject = db.Column(db.String(20), nullable=True)
    tutorId = db.Column(db.Integer, db.ForeignKey('tutor.tutorId'))
    students = db.relationship('Student', backref='classes')
    tutors = db.relationship('Tutor', backref='classes')
    lectures = db.relationship('Lecture', backref='classes')