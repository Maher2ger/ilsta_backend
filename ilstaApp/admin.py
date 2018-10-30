from django.contrib import admin

from .models import Question, Choice, Course, Chapter, TaskSolving


admin.site.register(Chapter)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Course)
admin.site.register(TaskSolving)



