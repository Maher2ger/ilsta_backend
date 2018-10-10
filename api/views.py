import json
from ilstaApp.models import Choice, Question, Course, Capital
from django.http import HttpResponse
from django.views.generic import View


def ChoicesListSerialize(qs):    #qs : QuerySet
    '''
    Serializert eine QuerySet von Choice-Objects
    :param qs: QuerySet von Choice-Objects
    :return: Liste von serialized Choice-Objects
    '''
    id = 0
    final_list = []
    for choice in qs:
        serializedChoice = choice.serialize(1)   #serialize(1): return Dictionary,
        serializedChoice['id'] = id              #serialize(2): return Json,
        id += 1
        final_list.append(serializedChoice)

    return final_list


def QuestionChoiceDictSerialize(id):
    '''
    Diese Funktion serializiert ein Question-Objects und die
    dazugehörigen Choices
    :param id: Id von Question
    :return: ein serialized-Dictiorary
    '''
    question = Question.objects.get(id=id)
    data = {
        "question": question.text,
        "answers": ChoicesListSerialize(Choice.objects.filter(question=question.id)),
        "tipps": question.tipps,
    }
    return data

def CapitalQuestionJsonSerialize(request,id):
    '''
    Serializiert die zu einem Kapital gehörigen Questions und Choices
    :param request: für Http request
    :param id: von Kapital
    :return: Json Datei : eine List von Questions mit deren Choices
    '''
    questions = list(Question.objects.filter(capital=id))
    final_list = []
    for question in questions:
        serializedQuestion = QuestionChoiceDictSerialize(question.id)
        final_list.append(serializedQuestion)

    json_data = json.dumps(final_list)

    return HttpResponse(json_data, content_type='application/json')


