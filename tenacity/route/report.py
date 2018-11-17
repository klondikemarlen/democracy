import flask
from tenacity import app

from tenacity.command import report as command_report


@app.route('/report', methods=['GET', 'POST'])
def report():
    data = {}
    for key in flask.request.args.keys():
        try:
            data[key] = getattr(command_report, key)(flask.request.args[key])
        except AttributeError as ex:
            data = {"error": "query end-point '{}' does not exist.".format(key)}
            break

    return flask.jsonify(data)
