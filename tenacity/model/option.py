from tenacity.model.base import GameState, db


class Option(GameState):
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=True)

    text = db.Column(db.String(500), nullable=False)

    # various fields
