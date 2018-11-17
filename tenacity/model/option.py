from tenacity.model.base import GameState, db


class Option(GameState):
    response_id = db.Column(db.Integer, db.ForeignKey('response.id'), nullable=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=True)
    answer_id = db.Column(db.Integer, db.ForeignKey('answer.id'), nullable=True)

    text = db.Column(db.String(128), nullable=False)

    # various fields
