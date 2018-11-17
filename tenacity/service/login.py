from tenacity.model.account import Account


def login_account(username, password):
    account = Account.query.filter_by(username=username).one()
    if account.password == password:
        return True
    return False
