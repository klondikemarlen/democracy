# tenacity/route/auth/views.py

from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from tenacity import bcrypt, db
from tenacity.model.account import Account

auth_blueprint = Blueprint('auth', __name__)


class RegisterAPI(MethodView):
    """User Registration Resource."""

    def post(self):
        # get the post data
        post_data = request.get_json()
        # check if account already exists
        account = Account.query.filter_by(
            email=post_data.get('email')).one_or_none()
        if not account:
            try:
                account = Account(
                    email=post_data.get('email'),
                    password=post_data.get('password')
                )
                account.save()
                # generate auth token
                aut_token = account.encode_auth_token()
                response = {
                    'status': 'success',
                    'message': 'Successfully registered.',
                    'auth_token': aut_token.decode()
                }
                return make_response(jsonify(response)), 201
            except Exception as e:
                response = {
                    'status': 'fail',
                    'message': 'Some error occurred. Please try again.'
                }
                return make_response(jsonify(response)), 401
        else:
            response = {
                'status': 'fail',
                'message': 'User already exists. Please log in.'
            }
            return make_response(jsonify(response)), 202


# define the API resources
registration_view = RegisterAPI.as_view('register_api')

# add rule for API endpoints
auth_blueprint.add_url_rule(
    '/auth/register',
    view_func=registration_view,
    methods=['POST']
)
