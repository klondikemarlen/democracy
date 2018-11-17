import os
import socket

from flask import Flask, render_template
from flask_json import FlaskJSON
from flask_sqlalchemy import SQLAlchemy
import flask_sslify
# from flask_wtf.csrf import CSRFProtect

import private_config

UPLOAD_FOLDER = 'tenacity/static/uploads/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config.from_object('private_config')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

if 'liveweb' in socket.gethostname():
    app.config['SQLALCHEMY_DATABASE_URI'] = private_config.SERVER_DATABASE_URI

db = SQLAlchemy(app)
sslify = flask_sslify.SSLify(app)

# csrf = CSRFProtect(app)
# csrf.init_app(app)

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


import_models()
import_routes()

if os.environ.get("FLASK_CLEAN") == "true" and os.environ.get("WERKZEUG_RUN_MAIN") == "true":
    db.drop_all()
    db.create_all()
    print("Rebuilding database")
