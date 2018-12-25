from flask import request, make_response, jsonify
from flask.views import MethodView

from model.account import Account


class AccountAPI(MethodView):
    """Account resource"""
    def get(self):
        # get the auth token
        auth_header = request.headers.get('Authorization')
        if auth_header:
            try:
                auth_token = auth_header.split(" ")[1]
            except IndexError:
                response = {
                    'status': 'fail',
                    'message': 'Bearer token malformed.'
                }
                return make_response(jsonify(response)), 401
        else:
            auth_token = ''
        if auth_token:
            resp = Account.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                account = Account.query.filter_by(id=resp).first()
                response = {
                    'status': 'success',
                    'data': {
                        'user_id': account.id,
                        'email': account.email,
                        'admin': account.admin,
                        'registered_on': account.registered_on
                    }
                }
                return make_response(jsonify(response)), 200
            response = {
                'status': 'fail',
                'message': resp
            }
            return make_response(jsonify(response)), 401
        else:
            response = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return make_response(jsonify(response)), 401


account_view = AccountAPI.as_view('account_api')
