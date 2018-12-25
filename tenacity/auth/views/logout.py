from flask import request, make_response, jsonify
from flask.views import MethodView

from model.account import Account
from model.blacklist_token import BlacklistToken


class LogoutAPI(MethodView):
    """Logout Resource"""

    def post(self):
        # get auth token
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_token = auth_header.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = Account.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                # mark the token as blacklisted
                blacklist_token = BlacklistToken(token=auth_token)
                try:
                    blacklist_token.save()
                    response = {
                        'status': 'success',
                        'message': 'Successfully logged out.'
                    }
                    return make_response(jsonify(response)), 200
                except Exception as e:
                    response = {
                        'status': 'fail',
                        'message': e
                    }
                    return make_response(jsonify(response)), 200
            else:
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
            return make_response(jsonify(response)), 403
