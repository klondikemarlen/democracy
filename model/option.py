from model import db
from model.base import Base


class Option(Base):
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=True)

    text = db.Column(db.String(500), nullable=False)

    # various fields
