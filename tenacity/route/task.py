import flask
from tenacity import app

from tenacity.service import login as login_service
from tenacity.command import task as command_task


@app.route('/task.html', methods=['GET', 'POST'])
def task():
    return app.send_static_file("task.html")


@app.route('/task', methods=['GET', 'POST'])
def get_tasks():
    data = {}
    for key in flask.request.args.keys():
        try:
            data[key] = getattr(command_task, key)(flask.request.args[key])
        except AttributeError as ex:
            data = {"error": "'{}' does not exist.".format(key)}
            break

    return flask.jsonify(data)
