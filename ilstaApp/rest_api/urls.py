from django.conf.urls import url
from .views import ChoiceAPIView



urlpatterns = [
    url(r'^$',ChoiceAPIView.as_view()),
]