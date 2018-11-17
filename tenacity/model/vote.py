from tenacity.model.base import GameState, db


class Vote(GameState):
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=True)
    issue_id = db.Column(db.Integer, db.ForeignKey('issue.id'), nullable=True)

    # various fields
