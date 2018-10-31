import json
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
                     ExplainerSerializer)

def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False

    return is_valid





class ChoiceAPIView(generics.ListAPIView):


    permission_classes = []
    authentication_classes = []

    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
