# tests/test_auth/test_status.py

import json
import pytest

from tests.test_auth.helpers import register_user
from tests.base import BaseTestCase


class TestAuthStatus(BaseTestCase):
    def test_account_status(self):
        with self.client:
            resp_register = register_user(self, "test@gmail.com", "password")
            response = self.client.get(
                '/auth/status',
                headers=dict(
                    Authorization='Bearer ' + json.loads(
                        resp_register.data.decode()
                    )['auth_token']
                )
            )
            assert response.status_code == 200

            data = json.loads(response.data.decode())
            assert data['status'] == 'success'
            assert data['data'] is not None
            assert data['data']['email'] == 'test@gmail.com'
            # must be True or False by identity
            assert any(data['data']['admin'] is x for x in [True, False])


if __name__ == "__main__":
    import sys
    pytest.main(sys.argv)
