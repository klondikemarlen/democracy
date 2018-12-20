# tenacity/auth/views/__int__.py

from flask import Blueprint

from .register import registration_view
from .login import login_view
from .account import account_view

auth_blueprint = Blueprint('auth', __name__)

# add rule for API endpoints
auth_blueprint.add_url_rule(
    '/auth/register',
    view_func=registration_view,
    methods=['POST']
)

auth_blueprint.add_url_rule(
    '/auth/login',
    view_func=login_view,
    methods=['POST']
)

auth_blueprint.add_url_rule(
    '/auth/status',
    view_func=account_view,
    methods=['GET']
)
