import datetime

import jwt
from flask import current_app

from model import db
from tenacity import flask_bcrypt
from model.base import Base
from model.blacklist_token import BlacklistToken


class Account(Base):
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password_hash = db.Column(db.String(192), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, admin=False):
        self.email = email
        self.username = email  # allow this to be changed later?
        self.password_hash = Account.generate_password(password)
        self.registered_on = datetime.datetime.now()
        self.admin = admin

    @staticmethod
    def generate_password(password):
        return flask_bcrypt.generate_password_hash(
            password,
            current_app.config.get('BCRYPT_LOG_ROUNDS')
        ).decode()

    def update_password(self, password):
        """Update the current password of the account."""

        self.password_hash = Account.generate_password(password)

    def encode_auth_token(self):
        """Generate the authentication token.

        :return: string
        """

        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': self.id
            }
            return jwt.encode(
                payload,
                current_app.config.get('SECRET_KEY'),
                algorithm=current_app.config.get('JWT_ALGORITHM')
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """Decodes the authentication token.

        :param auth_token
        :return: integer|string
        """

        try:
            payload = jwt.decode(
                auth_token,
                current_app.config.get("SECRET_KEY"),
                algorithms=[current_app.config.get('JWT_ALGORITHM')]
            )
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return 'Token blacklisted. Please log in again.'
            else:
                return payload['sub']
        except jwt.ExpiredSignatureError:
            return "Signature expired. Please log in again."
        except jwt.InvalidTokenError:
            return "Invalid token. Please log in again."
