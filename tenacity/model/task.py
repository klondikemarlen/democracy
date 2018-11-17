from tenacity.model.base import GameState, db


class Task(GameState):
    issue_id = db.Column(db.Integer, db.ForeignKey('issue.id'), nullable=True)

    # various fields
