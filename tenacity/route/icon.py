import os
from flask import send_from_directory

from tenacity import app


@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')
