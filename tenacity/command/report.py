import tenacity.model.issue as model_issue
import tenacity.model.question as model_question
import tenacity.model.option as model_option


def issue_id(value):
    issue = model_issue.Issue.query.get(value)
    if issue is None:
        return None

    question_data = []
    for question in issue.questions:
        options_data = []
        for option in question.options:
            options_data.append(dict(
            id=option.id,
            text=option.text,
            ))

        response_data = []
        for response in question.responses:
            pass

        question_data.append(dict(
            id=question.id,
            text=question.text,
            issue_id=question.issue_id,
            answer_id=question.answer_id,
            options=options_data,
            responses=response_data,
        ))

    # yes_votes = sum([1 if vote.cast is not None else 0 for vote in issue.votes])
    # no_votes = sum([0 if vote.cast is not None else 1 for vote in issue.votes])
    # example data
    yes_votes = 57
    no_votes = 23
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
