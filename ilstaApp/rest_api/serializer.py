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

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields= [
            'user',
            'name',
            'course',
        ]

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields= [
            'user',
            'text',
            'chapter',
                    ]

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields= [
            'user',
            'content',
            'is_true',
            'question'
        ]

    def validate(self, data):
            content =data.get("content", None)
            if content == "":
                content = None
            image = data.get('image', None)
            if content is None:
                raise forms.ValidationError('Content  is required.')
            return data

class TaskSolvingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskSolving
        fields= [
            'user',
            'text',
        ]

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields= [
            'user',
            'task',
            'text',
        ]

class ExplainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Explainer
        fields= [
            'user',
            'question',
            'title',
        ]

class BrickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brick
        fields= [
            'user',
            'text',
            'step'
        ]