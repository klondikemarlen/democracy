import pytest
from flask import current_app
from flask_testing import TestCase

from tenacity import app


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('config.DevelopmentConfig')
        return app

    def test_app_is_testing(self):
        assert app.config['DEBUG']
        assert current_app is not None
        # TODO hide password and change it.
        assert "mysql+mysqldb://tenacity:7ArQMuTUSoxXqEfzYfUR@localhost/tenacity?charset=utf8"


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('config.TestingConfig')
        return app

    def test_app_is_testing(self):
        assert app.config['DEBUG']
        assert app.config['TESTING']
        # TODO hide password and change it.
        assert "mysql+mysqldb://tenacity:7ArQMuTUSoxXqEfzYfUR@localhost/tenacity_test?charset=utf8"


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('config.ProductionConfig')
        return app

    def test_app_is_production(self):
        assert app.config['DEBUG'] is False
        assert app.config['SQLALCHEMY_POOL_RECYCLE'] == 299


if __name__ == "__main__":
    import sys
    pytest.main(sys.argv)
