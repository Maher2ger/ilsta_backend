from django.db import models
from django.utils import timezone
from django.conf import settings



class TimeStamped():
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(default=timezone.now)
