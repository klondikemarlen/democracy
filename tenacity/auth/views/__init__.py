# tenacity/auth/views/__int__.py

from flask import Blueprint

from .register import RegisterAPI
from .login import LoginAPI
from .account import AccountAPI
from .logout import LogoutAPI

auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')

# add rule for API endpoints
auth_blueprint.add_url_rule('/register', view_func=RegisterAPI.as_view('register_api'))
auth_blueprint.add_url_rule('/login', view_func=LoginAPI.as_view('login_api'))
auth_blueprint.add_url_rule('/status', view_func=AccountAPI.as_view('account_api'))
auth_blueprint.add_url_rule('/logout', view_func=LogoutAPI.as_view('logout_api'))
