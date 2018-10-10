import json
from ilstaApp.models import Choice, Question, Course, Capital
from django.http import HttpResponse
from django.views.generic import View


def ChoicesListSerialize(qs):
    id = 0
    final_list = []
    for choice in qs:
        serializedChoice = choice.serialize(1)
        serializedChoice['id'] = id
        id += 1
        final_list.append(serializedChoice)

    return final_list


def QuestionChoiceDictSerialize(id):
    question = Question.objects.get(id=id)
    data = {
        "question": question.text,
        "answers": ChoicesListSerialize(Choice.objects.filter(question=question.id)),
        "tipps": question.tipps,
    }
    return data

def CapitalQuestionJsonSerialize(request,id):
    questions = list(Question.objects.filter(capital=id))
    final_list = []
    for question in questions:
        serializedQuestion = QuestionChoiceDictSerialize(question.id)
        final_list.append(serializedQuestion)

    json_data = json.dumps(final_list)

    return HttpResponse(json_data, content_type='application/json')


