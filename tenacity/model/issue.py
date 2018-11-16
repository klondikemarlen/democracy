from tenacity.model.base import GameState, db


class Issue(GameState):
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(500), nullable=False)
