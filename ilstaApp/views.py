from django.shortcuts import render
from .models import Choice,Question,Course
from django.http import HttpResponse, JsonResponse

def index(request):
    return HttpResponse("<h1>The server works fine!!</h1>")

