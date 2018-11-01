from django import forms

from .models import (Question,
                     Choice,
                     Course,
                     Chapter,
                     TaskSolving,
                     Step,
                     Brick,
                     Explainer)

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields= [
            'user',
            'name',
        ]

class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields= [
            'user',
            'name',
            'course',
        ]

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields= [
            'user',
            'text',
            'chapter',
                    ]

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields= [
            'user',
            'content',
            'is_true',
            'question'
        ]

class TaskSolvingForm(forms.ModelForm):
    class Meta:
        model = TaskSolving
        fields= [
            'user',
            'text',
            'chapter',
        ]

class StepForm(forms.ModelForm):
    class Meta:
        model = Step
        fields= [
            'user',
            'task',
            'text',
        ]

class ExplainerForm(forms.ModelForm):
    class Meta:
        model = Explainer
        fields= [
            'user',
            'question',
            'title',
            'html'
        ]

class BrickForm(forms.ModelForm):
    class Meta:
        model = Brick
        fields= [
            'user',
            'text',
            'step'
        ]