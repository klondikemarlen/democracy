import flask
from tenacity import app

from tenacity.command import question as command_question


@app.route('/question', methods=['GET', 'POST'])
def question():
    data = {}
    for key in flask.request.args.keys():
        # import pdb;pdb.set_trace()
        try:
            data[key] = getattr(command_question, key)(flask.request.args[key])
        except AttributeError:
            data = {"error": "'{}' does not exist.".format(key)}
            break

    return flask.jsonify(data)
