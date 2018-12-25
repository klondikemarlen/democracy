from model import db
from model.base import Base


class Response(Base):
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=True)
    option_id = db.Column(db.Integer, db.ForeignKey('option.id'), nullable=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=True)
    # various fields?
