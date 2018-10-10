from django.urls import path
from django.conf.urls import url,include
from .views import CapitalQuestionJsonSerialize



urlpatterns = [

    url(r'^course/(?P<id>\d+)', CapitalQuestionJsonSerialize, name='courses'),
]
