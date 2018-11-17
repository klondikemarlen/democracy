from tenacity import db
from tenacity.model.issue import Issue


def create_issue(title, message):
    issue = Issue(title=title, description=message)
    db.session.add(issue)
    try:
        db.session.commit()
        return True
    except:
        db.session.rollback()
    finally:
        db.session.close()
    return False
