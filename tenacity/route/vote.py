import flask
from tenacity import app


@app.route('/vote.html', methods=['GET', 'POST'])
def vote():
    return app.send_static_file("vote.html")
