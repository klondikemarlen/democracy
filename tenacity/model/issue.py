from tenacity.model.base import GameState, db


class Issue(GameState):
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(500), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=True)
