import model.issue as model_issue
import model.response as model_response


def issue_id(value):
    issue = model_issue.Issue.query.get(value)
    if issue is None:
        return None

    question_data = []
    for question in issue.questions:
        options_data = []
        for option in question.options:

            response_count = model_response.Response.query.filter_by(option_id=option.id).count()

            options_data.append(dict(
            id=option.id,
            text=option.text,
            response_count=response_count
            ))

        question_data.append(dict(
            id=question.id,
            text=question.text,
            issue_id=question.issue_id,
            answer_id=question.answer_id,
            options=options_data,
        ))

    yes_votes = sum([1 if vote.cast == 1 else 0 for vote in issue.votes])
    no_votes = sum([1 if vote.cast == 0 else 0 for vote in issue.votes])
    # example data
    # yes_votes = 57
    # no_votes = 23
    data = dict(
        id=issue.id,
        title=issue.title,
        description=issue.description,
        creator_id=issue.account_id,
        yes=yes_votes,
        no=no_votes,
        questions=question_data
    )

    return data
