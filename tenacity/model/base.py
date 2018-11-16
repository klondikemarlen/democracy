from tenacity import db


class GameState(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
