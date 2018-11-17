from tenacity.model.base import GameState, db


class Question(GameState):
    text = db.Column(db.String(128), nullable=False)

    issue_id = db.Column(db.Integer, db.ForeignKey('issue.id'), nullable=True)
    answer_id = db.Column(db.Integer, db.ForeignKey('answer.id'), nullable=True)

    options = db.relationship("Option")
    responses = db.relationship("Response")
