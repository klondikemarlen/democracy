# tests/test_auth.py

import pytest
import json

from tenacity import db
from tenacity.model.account import Account
from tests.base import BaseTestCase


class TestAuthBlueprint(BaseTestCase):
    def test_registration(self):
        """Test for account registration."""

        with self.client:
            response = self.client.post(
                '/auth/register',
                data=json.dumps(dict(
                    email='test@gmail.com',
                    password='123456'
                )),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            assert data['status'] == 'success'
            assert data['message'] == 'Successfully registered.'
            assert data['auth_token']
            assert response.content_type == 'application/json'
            assert response.status_code == 201


if __name__ == "__main__":
    pytest.main([__file__])
