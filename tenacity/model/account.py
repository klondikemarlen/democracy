import datetime

import jwt

from tenacity import app, db, bcrypt
from tenacity.model.base import Base


class Account(Base):
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password_hash = db.Column(db.String(192), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, admin=False):
        self.email = email
        self.username = email  # allow this to be changed later?
        pass_hash = bcrypt.generate_password_hash(password, app.config.get('BCRYPT_LOG_ROUNDS'))
        self.password_hash = pass_hash.decode()
        self.registered_on = datetime.datetime.now()
        self.admin = admin

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
                app.config.get('SECRET_KEY'),
                algorithm=app.config.get('JWT_ALGORITHM')
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
                app.config.get("SECRET_KEY"),
                algorithms=[app.config.get('JWT_ALGORITHM')]
            )
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return "Signature expired. Please log in again."
        except jwt.InvalidTokenError:
            return "Invalid token. Please log in again."
