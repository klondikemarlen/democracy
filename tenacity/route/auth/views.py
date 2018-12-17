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

