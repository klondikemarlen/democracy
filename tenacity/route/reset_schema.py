import flask
from tenacity import app, db

# from tenacity.command import question as command_question


@app.route('/reset_schema', methods=['GET', 'POST'])
def reset_schema():
    db.drop_all()
    db.create_all()
    return "Database schema reset."
