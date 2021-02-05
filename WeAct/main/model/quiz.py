from WeAct import db
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