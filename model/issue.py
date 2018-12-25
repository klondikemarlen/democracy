from model import db
from model.base import Base


class Issue(Base):
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(500), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=True)

    questions = db.relationship("Question")
    votes = db.relationship("Vote")
