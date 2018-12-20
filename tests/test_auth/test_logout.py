# tests/test_auth/test_status.py

import json
import pytest

from tests.test_auth.helpers import register_user, login_user
from tests.base import BaseTestCase


class TestAuthLogout(BaseTestCase):
    def test_valid_logout(self):
        """Test for logout before token expires."""
        with self.client:
            # user registration
            resp_register = register_user(self, 'test@gmail.com', '123456')
            assert resp_register.content_type == 'application/json'
            assert resp_register.status_code == 201

            data_register = json.loads(resp_register.data.decode())
            assert data_register['status'] == 'success'
            assert data_register['message'] == 'Successfully registered.'
            assert data_register['auth_token']

            # user login
            resp_login = login_user(self, 'test@gmail.com', '123456')
            assert resp_login.content_type == 'application/json'
            assert resp_login.status_code == 200

            data_login = json.loads(resp_login.data.decode())
            assert data_login['status'] == 'success'
            assert data_login['message'] == 'Successfully logged in.'
            assert data_login['auth_token']

            # valid logout
            response = self.client.post(
                '/auth/logout',
                headers=dict(
                    Authorization='Bearer ' + json.loads(
                        resp_login.data.decode()
                    )['auth_token']
                )
            )
            assert response.status_code == 200

            data = json.loads(response.data.decode())
            assert data['status'] == 'success'
            assert data['message'] == 'Successfully logged out.'


if __name__ == "__main__":
    import sys
    pytest.main(sys.argv)
