from tenacity.model.base import GameState, db
from werkzeug.security import generate_password_hash, check_password_hash


class Account(GameState):
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password_hash = db.Column(db.String(192), nullable=False)
