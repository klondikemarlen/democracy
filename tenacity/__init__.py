# tenacity/__int__.py

import socket

from flask import Flask
from flask_sslify import SSLify  # Note: does not support factory pattern


from model import db, flask_bcrypt, flask_json
import model.account
import model.answer
import model.blacklist_token
import model.issue
import model.option
import model.question
import model.response
import model.task
import model.vote
from tenacity.auth.views import auth_blueprint
from tenacity.cache_buster.views import cache_buster_blueprint

app = Flask(__name__)

if 'live' in socket.gethostname():  # The server name will change.
    app.config.from_object('config.ProductionConfig')
    print("Running ProductionConfig")
else:
    app.config.from_object('config.DevelopmentConfig')

# attach various extentions to app
db.init_app(app)
flask_bcrypt.init_app(app)
flask_json.init_app(app)
flask_sslify = SSLify(app)  # Note: does not support factory pattern


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
    # import tenacity.cache_buster.views


import_routes()
app.register_blueprint(auth_blueprint)
app.register_blueprint(cache_buster_blueprint)
