import flask
from tenacity import app


@app.route('/index.html', methods=['GET', 'POST'])
def index():
    return flask.render_template("index.html")
