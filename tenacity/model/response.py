from tenacity.model.base import GameState, db


account_to_response = db.Table(
    'account_to_response', GameState.metadata,
    db.Column('account_id', db.Integer, db.ForeignKey('account.id')),
    db.Column('response_id', db.Integer, db.ForeignKey('response.id'))
)


class Response(GameState):
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=True)
    # various fields?
