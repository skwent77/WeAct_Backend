from WeAct import db


class Student(db.Model):
    userId = db.Column(db.Integer, primary_key=True)
    pw = db.Column(db.String(20), nullable=False)
    classId = db.Column(db.Integer, db.ForeignKey(
        'classes.classId', ondelete='CASCADE'))