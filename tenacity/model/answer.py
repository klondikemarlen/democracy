from tenacity.model.base import GameState, db


class Answer(GameState):
    text = db.Column(db.String(128), nullable=False)

    # currently one-to-one with question, possibly should be many-to-many with question?
    issue_id = db.Column(db.Integer, db.ForeignKey('issue.id'), nullable=True)
