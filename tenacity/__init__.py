import os
import socket

from flask import Flask, render_template
from flask_json import FlaskJSON
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

import private_config

UPLOAD_FOLDER = 'tenacity/static/uploads/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config.from_object('private_config')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

if 'liveweb' in socket.gethostname():
    app.config['SQLALCHEMY_DATABASE_URI'] = private_config.SERVER_DATABASE_URI

# db = SQLAlchemy(app)

csrf = CSRFProtect(app)
csrf.init_app(app)

json = FlaskJSON(app)



@app.errorhandler(404)
def not_found(error):
    print("Error:", error)
    return render_template('404.html'), 404


from tenacity import model


# noinspection PyUnresolvedReferences
def import_routes():
    import tenacity.route.question


import_routes()
