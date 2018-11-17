from tenacity.model.account import Account


def login_account(username, password):
    account = Account.query.filter_by(username=username).one_or_none()
    if account and account.password_hash == password:
        return True
    return False
