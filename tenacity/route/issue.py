import flask
from tenacity import app

from tenacity.command import issue as command_issue


@app.route('/issue', methods=['GET', 'POST'])
def issue():
    data = {}
    for key in flask.request.args.keys():
        try:
            data[key] = getattr(command_issue, key)(flask.request.args[key])
        except AttributeError as ex:
            data = {"error": "'{}' does not exist.".format(key)}
            break

    return flask.jsonify(data)
