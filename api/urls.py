from django.urls import path
from django.conf.urls import url,include
from .views import ChapterQuestionJsonSerialize



urlpatterns = [

    url(r'^course/(?P<id>\d+)', ChapterQuestionJsonSerialize, name='courses'),
]
