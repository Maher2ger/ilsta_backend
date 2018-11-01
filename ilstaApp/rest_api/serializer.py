import json
from rest_framework import serializers
from ilstaApp.models import (Question,
                     Choice,
                     Course,
                     Chapter,
                     TaskSolving,
                     Step,
                     Brick,
                     Explainer)

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields= [
            'user',
            'name',
        ]



class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields= [
            'id',
            'content',
            'is_true',
            'response_text'
        ]

class QuestionSerializer(serializers.ModelSerializer):
    answers = ChoiceSerializer(many=True, read_only=True)
    question = serializers.ReadOnlyField(source='__str__')
    class Meta:
        model = Question
        fields = [
                'question',
                'answers',
            ]


    def validate(self, data):
            content =data.get("content", None)
            if content == "":
                content = None
            image = data.get('image', None)
            if content is None:
                raise forms.ValidationError('Content  is required.')
            return data


class BrickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brick
        fields= [
            'id',
            'text',
             ]

class StepSerializer(serializers.ModelSerializer):
    answerBricks =BrickSerializer(many=True, read_only=True)
    stepText = serializers.ReadOnlyField(source='__str__')
    class Meta:
        model = Step
        fields= [
            'id',
            'stepText',
            'answerBricks',
        ]



class TaskSolvingSerializer(serializers.ModelSerializer):
    questionText = serializers.ReadOnlyField(source='get_text')
    steps = StepSerializer(many=True, read_only=True)
    class Meta:
        model = TaskSolving
        fields= [
            'id',
            'questionText',
            'steps'
        ]




class McqSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = Chapter
        fields= [
            'name',
            'course',
            'questions',
        ]


class TSSerializer(serializers.ModelSerializer):
    tasks = TaskSolvingSerializer(many=True, read_only=True)
    chapter = serializers.ReadOnlyField(source='__str__')
    class Meta:
        model = Chapter
        fields= [
            'chapter',
            'course',
            'tasks',
        ]




class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields= [
            'name',
            'course',
            'id'
        ]


class ExplainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Explainer
        fields= [
            'id',
            'title',
            'html',
        ]


class ExSerializer(serializers.ModelSerializer):
    explainer = ExplainerSerializer(many=True, read_only=True)
    class Meta:
        model = Chapter
        fields = [
            'name',
            'course',
            'explainer'
        ]