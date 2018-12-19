# tenacity/__int__.py

import socket

from flask import Flask, render_template
from flask_json import FlaskJSON
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_sslify import SSLify


app = Flask(__name__)

if 'live' in socket.gethostname():  # The server name will change.
    app.config.from_object('config.ProductionConfig')
    print("Running ProductionConfig")
else:
    app.config.from_object('config.DevelopmentConfig')

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
sslify = SSLify(app)
json = FlaskJSON(app)


@app.errorhandler(404)
def not_found(error):
    print("Error:", error)
    return render_template('404.html'), 404


def import_models():
    from tenacity.model.account import Account
    from tenacity.model.issue import Issue
    from tenacity.model.vote import Vote
    from tenacity.model.response import Response
    from tenacity.model.question import Question
    from tenacity.model.answer import Answer
    from tenacity.model.option import Option
    from tenacity.model.task import Task


def import_routes():
    import tenacity.route.hooks
    import tenacity.route.question
    import tenacity.route.reset_schema
    import tenacity.route.index
    import tenacity.route.login
    import tenacity.route.vote
    import tenacity.route.issue
    import tenacity.route.icon
    import tenacity.route.task
    import tenacity.route.report
    import tenacity.route.record

    from tenacity.route.auth.views import auth_blueprint
    app.register_blueprint(auth_blueprint)


import_models()
import_routes()
