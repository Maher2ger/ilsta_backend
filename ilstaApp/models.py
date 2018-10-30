import json
from django.utils import timezone
from django.conf import settings
from django.db import models
from .mixin import TimeStamped




class Course(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default="")
    name = models.CharField(default="chapter", max_length=264, unique=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name


    def serialize(self):
        data = {
            "user":self.user,
            "course_name": self.name,
            "create_date": self.create_date,
        }

        json_data = json.dumps(data)
        return json_data

class Chapter(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default="")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    name = models.CharField(default="chapter", max_length=264, unique=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name

    def serialize(self):
        data = {
            "course": self.course,
            "name": self.name,
            "create_date": self.create_date,
        }

        json_data = json.dumps(data)
        return json_data


class Question(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default="")
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, null=True)
    text = models.CharField(default="", max_length=264)
    tipps = models.TextField(blank=True, default="No Tipps!!")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

    def serialize(self):
        data = {
            "chapter": self.chapter,
            "question": self.text,
            "create_date": self.created,
            "tipps":self.tipps,
        }

        json_data = json.dumps(data)
        return json_data


class Choice(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default="")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    content = models.CharField(default="", max_length=264, blank=True, null=True)
    is_true = models.BooleanField(default=False)
    response_text = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(default=timezone.now)

    readonly_fields = ['created','updated']

    def __str__(self):
        return self.content

    def serialize(self,type):
        if type == 1:    #Die Ausgabe ist ein Dict
            data = {
                "id": self.id,
                "content": self.content,
                "is_true": self.is_true,
                "response_text": self.response_text,
                }
            return data

        if type == 2:    # #Die Ausgabe ist ein Json
            data = {
                "id": self.id,
                "content": self.content,
                "is_true": self.is_true,
                "response_text": self.response_text,
            }
            json_data = json.dumps(data)
            return json_data


class TaskSolving(models.Model):
    text = models.TextField(blank=True, default="No text!!")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Task_ID: " + self.id


class Explainer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="")
    question = models.ForeignKey(Chapter, on_delete=models.CASCADE, null=True)
    title = models.CharField(default="", max_length=264, blank=True, null=True)
    html = models.TextField(blank=True, default="No text!!")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Explainer_ID: " + self.id
    
    
    
class Steps(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="")
    task = models.ForeignKey(TaskSolving, on_delete=models.CASCADE, null=True)
    text = models.TextField(blank=True, default="No text!!")
    solution = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return  self.text



class Step(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="")
    task = models.ForeignKey(TaskSolving, on_delete=models.CASCADE, null=True)
    text = models.TextField(blank=True, default="No text!!")
    solution = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return  self.text

    
    
class Brick(models.Model,TimeStamped):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="")
    step = models.ForeignKey(Steps, on_delete=models.CASCADE, null=True)
    text = models.TextField(blank=True, default="No text!!")


    def __str__(self):
        return  self.text