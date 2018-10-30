from django.conf.urls import url

)



urlpatterns = [
    url(r'^$',StatusAPIView.as_view()),
]