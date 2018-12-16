from tenacity.model.base import Base, db


class Vote(Base):
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=True)
    issue_id = db.Column(db.Integer, db.ForeignKey('issue.id'), nullable=True)

    cast = db.Column(db.Boolean)
    # weight
