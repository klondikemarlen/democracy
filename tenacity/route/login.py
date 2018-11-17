import flask
from tenacity import app

from tenacity.service import login as login_service


@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'POST':
        try:
            form_data = flask.json.loads(next(flask.request.form.keys()))
        except StopIteration:
            return flask.jsonify(login=False)
        if login_service.login_account(form_data['username'], form_data['password']):
            return flask.jsonify(login=True)
        return flask.jsonify(login=False)
    return flask.render_template("login.html")
