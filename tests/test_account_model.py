# tests/test_account_model.py

import pytest

from model import Account
from tests.base import BaseTestCase


class TestAccountModel(BaseTestCase):
    def test_encode_auth_token(self):
        account = Account(
            email="test@gmail.com",
            password="test"
        )

        account.save()
        auth_token = account.encode_auth_token()

        assert isinstance(auth_token, bytes)

    def test_decode_auth_token(self):
        account = Account(
            email="test@gmail.com",
            password="test"
        )
        account.save()
        auth_token = account.encode_auth_token()
        assert isinstance(auth_token, bytes)
        assert Account.decode_auth_token(auth_token.decode('utf-8')) == 1


if __name__ == "__main__":
    import sys
    pytest.main(sys.argv)
