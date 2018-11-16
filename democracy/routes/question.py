import flask
from democracy import app


@app.route('/question/<id>', methods=['GET', 'POST'])
def command(id=None):
    testing = True  # True/False
    if testing:
        print('request is:', repr(flask.request))
        # print('request data:', repr(request.data))
        # print("request form:", repr(request.form))
        print('request view_args:', repr(flask.request.view_args))
        print('request args:', repr(flask.request.args))
        print('cmd is:', repr(id))


    return flask.jsonify(account="example_account_name")
