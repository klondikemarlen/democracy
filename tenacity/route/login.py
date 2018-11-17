import flask
from tenacity import app

from tenacity.service import login as login_service


@app.route('/question', methods=['POST'])
def login():
    username = flask.request.form.get('username', '', type=str)
    password = flask.request.form.get('password', '', type=str)

    if flask.request.method == 'POST':
        if login_service.login_account(username, password):
            return flask.jsonify(login=True)
    return flask.jsonify(login=False)
