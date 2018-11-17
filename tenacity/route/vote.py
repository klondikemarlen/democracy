import flask
from tenacity import app


@app.route('/vote.html', methods=['GET', 'POST'])
def index():
    return flask.render_template("vote.html")
