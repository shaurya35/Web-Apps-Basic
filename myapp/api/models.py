from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='events/')
    # is_liked = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)