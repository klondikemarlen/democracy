import flask
from tenacity import app

from tenacity.command import question as command_question


@app.route('/question', methods=['GET', 'POST'])
def question():
    testing = True  # True/False
    if testing:
        print('request is:', repr(flask.request))
        print('request data:', repr(flask.request.data))
        print("request form:", repr(flask.request.form))
        print('request view_args:', repr(flask.request.view_args))
        print('request args:', repr(flask.request.args))
        print('cmd is:', repr(id))

    print(dir(command_question))

    data = {}
    for key in flask.request.args.keys():
        try:
            data[key] = getattr(command_question, key)(flask.request.args[key])
        except AttributeError:
            data = {"error": "'{}' does not exist.".format(key)}
            break

    return flask.jsonify(data)
