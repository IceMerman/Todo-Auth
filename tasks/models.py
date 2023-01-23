from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=50)
    descrption = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True)
    important = models.BooleanField(default=False)
    # user = models.ForeignKey('django.contrib.auth.models.User', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)