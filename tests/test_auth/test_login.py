# tests/test_auth/test_login.py

import json
import pytest

# kept full path to allow running only this file.
from tests.test_auth.helpers import register_user, login_user
from tests.base import BaseTestCase


class TestAuthLogin(BaseTestCase):
    def test_registered_account_login(self):
        """Test for login of registered-account login."""

        with self.client:
            # user registration
            resp_register = register_user(self, 'test@gmail.com', '123456')
            assert resp_register.content_type == 'application/json'
            assert resp_register.status_code == 201

            data_register = json.loads(resp_register.data.decode())
            assert data_register['status'] == 'success'
            assert data_register['message'] == 'Successfully registered.'
            assert data_register['auth_token']

            # registered user login
            response = login_user(self, 'test@gmail.com', '123456')
            assert response.content_type == 'application/json'
            assert response.status_code == 200

            data = json.loads(response.data.decode())
            assert data['status'] == 'success'
            assert data['message'] == 'Successfully logged in.'
            assert data['auth_token']

    def test_non_registered_account_login(self):
        """Test for login of non-registered account."""

        with self.client:
            response = login_user(self, 'test@gmail.com', '123456')
            assert response.content_type == 'application/json'
            assert response.status_code == 404

            data = json.loads(response.data.decode())
            assert data['status'] == 'fail'
            assert data['message'] == 'Account does not exist.'

    def test_correct_email_incorrect_password(self):
        with self.client:
            resp_register = register_user(self, 'test@gmail.com', '123456')
            assert resp_register.content_type == 'application/json'
            assert resp_register.status_code == 201

            data_register = json.loads(resp_register.data.decode())
            assert data_register['status'] == 'success'
            assert data_register['message'] == 'Successfully registered.'
            assert data_register['auth_token']

            response = login_user(self, 'test@gmail.com', 'wrong_password')
            assert response.content_type == 'application/json'
            assert response.status_code == 401

            data = json.loads(response.data.decode())
            assert data['status'] == 'fail'
            assert data['message'] == 'Password is incorrect.'


if __name__ == "__main__":
    import sys
    pytest.main(sys.argv)
