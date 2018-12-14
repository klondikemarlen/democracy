import pytest

from flask import current_app
from flask_testing import TestCase

from tenacity import app


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('private_config.DevelopmentConfig')
        return app

    def test_app_is_testing(self):
        assert app.config['DEBUG']
        assert current_app is not None
        assert "mysql+mysqldb://tenacity:7ArQMuTUSoxXqEfzYfUR@localhost/tenacity?charset=utf8"


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('private_config.TestingConfig')
        return app

    def test_app_is_testing(self):
        assert app.config['DEBUG']
        assert app.config['TESTING']
        assert "mysql+mysqldb://tenacity:7ArQMuTUSoxXqEfzYfUR@localhost/tenacity_test?charset=utf8"


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('private_config.ProductionConfig')
        return app

    def test_app_is_production(self):
        assert app.config['DEBUG'] is False
