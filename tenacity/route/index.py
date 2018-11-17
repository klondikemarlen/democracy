import flask
from tenacity import app

from tenacity.service import issue


@app.route('/index.html', methods=['GET', 'POST'])
def index():
    if flask.request.method == 'POST':
        try:
            form_data = flask.json.loads(next(flask.request.form.keys()))
        except StopIteration:
            return flask.jsonify(submit=False)
        if issue.create_issue(form_data['title'], form_data['message']):
            return flask.jsonify(submit=True)
        return flask.jsonify(submit=False)
    return app.send_static_file("index.html")


@app.route('/', methods=['GET', 'POST'])
def entry():
    return flask.redirect(flask.url_for('index'))
