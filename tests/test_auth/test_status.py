# tests/test_auth/test_status.py

import json
import pytest

from model.blacklist_token import BlacklistToken
from tests.test_auth.helpers import register_account, account_status
from tests.base import BaseTestCase


class TestAuthStatus(BaseTestCase):
    def test_account_status(self):
        with self.client:
            resp_register = register_account(self, "test@gmail.com", "password")
            response = account_status(self, resp_register)
            assert response.status_code == 200

            data = json.loads(response.data.decode())
            assert data['status'] == 'success'
            assert data['data'] is not None
            assert data['data']['email'] == 'test@gmail.com'
            # must be True or False by identity
            assert any(data['data']['admin'] is x for x in [True, False])

    def test_valid_blacklisted_token(self):
        """Test for user status with a blacklisted token."""

        with self.client:
            resp_register = register_account(self, 'test@gmail.com', '123456')
            blacklist_token = BlacklistToken(
                token=json.loads(resp_register.data.decode())['auth_token'])
            blacklist_token.save()
            response = account_status(self, resp_register)
            data = json.loads(response.data.decode())
            assert response.status_code == 401
            assert data['status'] == 'fail'
            assert data['message'] == 'Token blacklisted. Please log in again.'

    def test_account_status_malformed_bearer_token(self):
        """Test for user status with malformed bearer token."""

        with self.client:
            resp_register = register_account(self, 'test@gmail.com', '123456')
            response = self.client.get(
                '/auth/status',
                headers=dict(  # note lack of space after "Bearer"
                    Authorization='Bearer' + json.loads(
                        resp_register.data.decode()
                    )['auth_token']
                )
            )
            data = json.loads(response.data.decode())
            assert response.status_code == 401
            assert data['status'] == 'fail'
            assert data['message'] == 'Bearer token malformed.'


if __name__ == "__main__":
    import sys
    pytest.main(sys.argv)
