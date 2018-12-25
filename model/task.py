from model import db
from model.base import Base


class Task(Base):
    issue_id = db.Column(db.Integer, db.ForeignKey('issue.id'), nullable=True)

    # account which has taken responsibility for the task.
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=True)

    # Front end should
    text = db.Column(db.String(1000), nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    due_date = db.Column(db.DateTime, nullable=False)



