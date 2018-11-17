import flask
from tenacity import app


@app.route('/records.html', methods=['GET', 'POST'])
def record():
    return app.send_static_file("records.html")
