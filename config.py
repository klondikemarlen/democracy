import private_config

DATABASE_NAME = "tenacity"

MYSQL_BASE = "mysql+mysqldb://{user}:{passwd}@{host}/{dbname}?{options}"
USER = "tenacity"
DB_PASSWORD = private_config.DB_PASSWORD
HOST = "localhost"
OPTIONS = "charset=utf8"


class BaseConfig:
    """Base configuration."""
    ENV = 'base'
    SECRET_KEY = private_config.SECRET_KEY
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = private_config.CSRF_SESSION_KEY


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    ENV = 'development'
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = MYSQL_BASE.format(
        user=USER, passwd=DB_PASSWORD, host=HOST, dbname=DATABASE_NAME, options=OPTIONS)


class TestingConfig(BaseConfig):
    ENV = 'testing'
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = MYSQL_BASE.format(
        user=USER, passwd=DB_PASSWORD, host=HOST, dbname=DATABASE_NAME + '_test', options=OPTIONS)
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(BaseConfig):
    """Production configuration."""
    ENV = 'production'
    DEBUG = False
    SQLALCHEMY_POOL_RECYCLE = 299  # 1s less than PythonAnywhere's 300s (5 min).
    SQLALCHEMY_DATABASE_URI = MYSQL_BASE.format(
        user=USER, passwd=DB_PASSWORD, host=USER + '.mysql.pythonanywhere-services.com', dbname=DATABASE_NAME + '$default', options=OPTIONS)


