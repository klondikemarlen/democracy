# tests/test_auth/test_status.py

import json
import time

import pytest

from tenacity.model.blacklist_token import BlacklistToken
from tests.test_auth.helpers import register_account, login_account, logout_account
from tests.base import BaseTestCase


class TestAuthLogout(BaseTestCase):
    def test_valid_logout(self):
        """Test for logout before token expires."""
        with self.client:
            # user registration
            resp_register = register_account(self, 'test@gmail.com', '123456')
            assert resp_register.content_type == 'application/json'
            assert resp_register.status_code == 201

            data_register = json.loads(resp_register.data.decode())
            assert data_register['status'] == 'success'
            assert data_register['message'] == 'Successfully registered.'
            assert data_register['auth_token']

            # user login
            resp_login = login_account(self, 'test@gmail.com', '123456')
            assert resp_login.content_type == 'application/json'
            assert resp_login.status_code == 200

            data_login = json.loads(resp_login.data.decode())
            assert data_login['status'] == 'success'
            assert data_login['message'] == 'Successfully logged in.'
            assert data_login['auth_token']

            # valid logout
            response = logout_account(self, resp_login)
            assert response.status_code == 200

            data = json.loads(response.data.decode())
            assert data['status'] == 'success'
            assert data['message'] == 'Successfully logged out.'

    def test_invalid_logout(self):
        with self.client:
            # user registration
            resp_register = register_account(self, 'test@gmail.com', '123456')
            assert resp_register.content_type == 'application/json'
            assert resp_register.status_code == 201

            data_register = json.loads(resp_register.data.decode())
            assert data_register['status'] == 'success'
            assert data_register['message'] == 'Successfully registered.'
            assert data_register['auth_token']

            # user login
            resp_login = login_account(self, 'test@gmail.com', '123456')
            assert resp_login.content_type == 'application/json'
            assert resp_login.status_code == 200

            data_login = json.loads(resp_login.data.decode())
            assert data_login['status'] == 'success'
            assert data_login['message'] == 'Successfully logged in.'
            assert data_login['auth_token']

            # invalid token logout
            time.sleep(6)
            response = logout_account(self, resp_login)
            assert response.status_code == 401

            data = json.loads(response.data.decode())
            assert data['status'] == 'fail'
            assert data['message'] == 'Signature expired. Please log in again.'

    def test_valid_blacklisted_token_logout(self):
        """Test for logout after a valid token gets blacklisted."""

        with self.client:
            # user registration
            resp_register = register_account(self, 'test@gmail.com', '123456')
            assert resp_register.content_type == 'application/json'
            assert resp_register.status_code == 201

            data_register = json.loads(resp_register.data.decode())
            assert data_register['status'] == 'success'
            assert data_register['message'] == 'Successfully registered.'
            assert data_register['auth_token']

            # user login
            resp_login = login_account(self, 'test@gmail.com', '123456')
            assert resp_login.content_type == 'application/json'
            assert resp_login.status_code == 200

            data_login = json.loads(resp_login.data.decode())
            assert data_login['status'] == 'success'
            assert data_login['message'] == 'Successfully logged in.'
            assert data_login['auth_token']

            # blacklist a valid token
            blacklist_token = BlacklistToken(
                token=json.loads(resp_login.data.decode())['auth_token'])
            blacklist_token.save()
            response = logout_account(self, resp_login)
            data = json.loads(response.data.decode())
            assert response.status_code == 401
            assert data['status'] == 'fail'
            assert data['message'] == 'Token blacklisted. Please log in again.'


if __name__ == "__main__":
    import sys
    pytest.main(sys.argv)
