# tests/test_auth/test_register.py

import pytest
import json

from model import Account
from tests.base import BaseTestCase
from tests.test_auth.helpers import register_account


class TestAuthRegister(BaseTestCase):
    def test_registration(self):
        """Test for account registration."""

        with self.client:
            response = register_account(self, 'test@gmail.com', '123456')
            assert response.content_type == 'application/json'
            assert response.status_code == 201

            data = json.loads(response.data.decode())
            assert data['status'] == 'success'
            assert data['message'] == 'Successfully registered.'
            assert data['auth_token']

    def test_register_with_already_registered_account(self):
        """Test registration with already registered email."""

        account = Account(
            email='test@gmail.com',
            password='test'
        )
        account.save()

        with self.client:
            response = register_account(self, 'test@gmail.com', '123456')
            assert response.content_type == 'application/json'
            assert response.status_code == 202

            data = json.loads(response.data.decode())
            assert data['status'] == 'fail'
            assert data['message'] == 'User already exists. Please log in.'


if __name__ == "__main__":
    import sys
    pytest.main(sys.argv)
