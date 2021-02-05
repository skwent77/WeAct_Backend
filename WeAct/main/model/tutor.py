from WeAct import db
class Tutor(db.Model):
    tutorId = db.Column(db.Integer, primary_key=True)
    pw = db.Column(db.String(20), nullable=False)
    classId = db.Column(db.Integer, db.ForeignKey('classes.classId'))