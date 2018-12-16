from tenacity.model.base import Base, db


class Option(Base):
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=True)

    text = db.Column(db.String(500), nullable=False)

    # various fields
