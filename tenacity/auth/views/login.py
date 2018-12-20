from flask import request, make_response, jsonify
from flask.views import MethodView

from tenacity import bcrypt, db
from tenacity.model.account import Account


class LoginAPI(MethodView):
    """Account login resource."""

    def post(self):
        post_data = request.get_json()
        try:
            # fetch the account data
            account = Account.query.filter_by(
                email=post_data.get('email')
            ).first()
            if account and bcrypt.check_password_hash(account.password_hash, post_data.get('password')):
                auth_token = account.encode_auth_token()
                if auth_token:
                    response = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'auth_token': auth_token.decode()
                    }
                    return make_response(jsonify(response)), 200
            elif account:
                response = {
                    'status': 'fail',
                    'message': 'Password is incorrect.'
                }
                return make_response(jsonify(response)), 401
            else:
                response = {
                    'status': 'fail',
                    'message': 'Account does not exist.'
                }
                return make_response(jsonify(response)), 404
        except Exception as e:
            print(e)
            response = {
                'status': 'fail',
                'message': 'Try again'
            }
            return make_response(jsonify(response)), 500


# define API resource
login_view = LoginAPI.as_view('login_api')
