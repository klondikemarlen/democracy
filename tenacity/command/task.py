from model import task as model_task


def issue_id(value):
    tasks = model_task.Task.query.filter_by(issue_id=value).all()
    # if not tasks:
    #     raise Exception("Database is probably empty, import sql.")

    data = []
    for task in tasks:
        data.append(dict(
            id=task.id,
            issue_id=task.issue_id,
            account_id=task.account_id,
            text=task.text,
            date_created=task.date_created,
            due_date=task.due_date
        ))

    return data
