from django.conf.urls import url
from .views import (ChoiceListAPIView,
                    QuetionListAPIView,
                    ChapterListAPIView,
                    TSListAPIView,
                    McqDetailAPIView,
                    TSDetailAPIView,
                    ExplainerDetailAPIView,
                    ExDetailAPIView)



urlpatterns = [
    #url(r'^$',ChoiceListAPIView.as_view()),
    #url(r'^$',QuetionListAPIView.as_view()),
    #url(r'^$',ChapterListAPIView.as_view()),
    #url(r'^$',TSListAPIView.as_view()),
    url(r'^mcq/(?P<pk>.*)/$',McqDetailAPIView.as_view()),
    url(r'^tasks/(?P<pk>.*)/$',TSDetailAPIView.as_view()),
    url(r'^ex/(?P<pk>.*)/$',ExDetailAPIView.as_view()),
]