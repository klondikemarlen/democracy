from tenacity.model.base import GameState, db


class Response(GameState):
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=True)
    response_id = db.Column(db.Integer, db.ForeignKey('response.id'), nullable=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=True)
    # various fields?
