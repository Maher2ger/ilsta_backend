import json
import requests
from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from ilstaApp.models import (Question,
                     Choice,
                     Course,
                     Chapter,
                     TaskSolving,
                     Step,
                     Brick,
                     Explainer)

from ilstaApp.forms import (QuestionForm,
                     ChoiceForm,
                     CourseForm,
                     ChapterForm,
                     TaskSolvingForm,
                     StepForm,
                     BrickForm,
                     ExplainerForm)

from .serializer import (QuestionSerializer,
                     ChoiceSerializer,
                     CourseSerializer,
                     ChapterSerializer,
                     TaskSolvingSerializer,
                     StepSerializer,
                     BrickSerializer,
                     ExplainerSerializer,
                     TSSerializer,
                     McqSerializer,
                     ExSerializer)

def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False

    return is_valid


class ChoiceListAPIView(generics.ListAPIView):
    permission_classes = []
    authentication_classes = []

    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class QuetionListAPIView(generics.ListAPIView):
    permission_classes = []
    authentication_classes = []

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ChapterListAPIView(generics.ListAPIView):
    permission_classes = []
    authentication_classes = []

    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer


class TSListAPIView(generics.ListAPIView):
    permission_classes = []
    authentication_classes = []

    queryset = TaskSolving.objects.all()
    serializer_class = TSSerializer


class McqDetailAPIView(generics.RetrieveAPIView):

    permission_classes = []
    authentication_classes = []
    queryset = Chapter.objects.all()
    serializer_class = McqSerializer


    # def post(self,request, *args,**kwargs):
    #     return self.create(request,*args,**kwargs)


    # def get_object(self,*args,**kwargs):
    #     kwargs= self.kwargs
    #     kw_id = kwargs.get('id')
    #     return Chapter.objects.get(id=kw_id)

class TSDetailAPIView(generics.RetrieveAPIView):

    permission_classes = []
    authentication_classes = []
    queryset = Chapter.objects.all()
    serializer_class = TSSerializer


class ExplainerDetailAPIView(generics.RetrieveAPIView):

    permission_classes = []
    authentication_classes = []
    queryset = Explainer.objects.all()
    serializer_class = ExplainerSerializer


class ExDetailAPIView(generics.RetrieveAPIView):

    permission_classes = []
    authentication_classes = []
    queryset = Chapter.objects.all()
    serializer_class = ExSerializer