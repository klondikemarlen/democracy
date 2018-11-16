import flask
from tenacity import app


@app.route('/index.html', methods=['GET', 'POST'])
def index():
    return flask.render_template("index.html")


@app.route('/', methods=['GET', 'POST'])
def entry():
    return flask.redirect(flask.url_for('index'))
