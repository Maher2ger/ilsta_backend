from django.contrib import admin

from .models import (Question,
                     Choice,
                     Course,
                     Chapter,
                     TaskSolving,
                     Step,
                     Brick,
                     Explainer)

from .forms import (QuestionForm,
                     ChoiceForm,
                     CourseForm,
                     ChapterForm,
                     TaskSolvingForm,
                     StepForm,
                     BrickForm,
                     ExplainerForm)


class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'created', 'updated']
    form = CourseForm


class ChapterAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'course', 'created', 'updated']
    form = ChapterForm



class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'text', 'chapter', 'created', 'updated']
    form = QuestionForm



class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'content', 'is_true','question', 'created', 'updated']
    form = ChoiceForm



class TaskSolvingAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'text', 'created', 'updated']
    form = TaskSolvingForm



class StepAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'text', 'task', 'created', 'updated']
    form = StepForm


class ExplainerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'question', 'created', 'updated']
    form = ExplainerForm


class BrickAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'text', 'step', 'created', 'updated']
    form = BrickForm








admin.site.register(Chapter,ChapterAdmin)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice,ChoiceAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(TaskSolving,TaskSolvingAdmin)
admin.site.register(Step,StepAdmin)
admin.site.register(Explainer,ExplainerAdmin)
admin.site.register(Brick,BrickAdmin)





