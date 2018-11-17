import tenacity.model.issue as model_issue
import tenacity.model.question as model_question
import tenacity.model.option as model_option


def id(value):
    issue = model_issue.Issue.query.get(value)
    if issue is None:
        raise Exception("Data base is empty, import sql.")
    data = dict(
        id=issue.id,
        title=issue.title,
        description=issue.description,
        account_id=issue.account_id,
        questions=[]
    )

    questions = model_question.Question.query.filter_by(issue_id=issue.id).all()
    for question in questions:
        options = model_option.Option.query.filter_by(question_id=question.id)

        options_data = []
        for option in options:
            options_data.append(dict(
            id=option.id,
            text=option.text,
            ))

        data['questions'].append(dict(
            id=question.id,
            text=question.text,
            issue_id=question.issue_id,
            answer_id=question.answer_id,
            options=options_data
        ))


    return data
