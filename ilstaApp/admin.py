from django.contrib import admin

from .models import Question, Choice, Course, Capital


admin.site.register(Capital)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Course)

