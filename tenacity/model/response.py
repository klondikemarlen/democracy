from tenacity.model.base import Base, db


class Response(Base):
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=True)
    option_id = db.Column(db.Integer, db.ForeignKey('option.id'), nullable=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=True)
    # various fields?
