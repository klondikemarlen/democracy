from tenacity import db
from tenacity.model.issue import Issue


def create_issue(title, message):
    issue = Issue(title=title, description=message)
    issue.save()
