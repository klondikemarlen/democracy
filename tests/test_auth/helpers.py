import json


def register_account(self, email, password):
    return self.client.post(
        '/auth/register',
        data=json.dumps(dict(
            email=email,
            password=password
        )),
        content_type='application/json',
    )


def login_account(self, email, password):
    return self.client.post(
        '/auth/login',
        data=json.dumps(dict(
            email=email,
            password=password
        )),
        content_type='application/json'
    )


def account_status(self, response):
    return self.client.get(
        '/auth/status',
        headers=dict(
            Authorization='Bearer ' + json.loads(
                response.data.decode()
            )['auth_token']
        )
    )


def logout_account(self, response):
    return self.client.post(
        '/auth/logout',
        headers=dict(
            Authorization='Bearer ' + json.loads(
                response.data.decode()
            )['auth_token']
        )
    )
