import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Topic(models.Model):
    topic_input = models.CharField(max_length=200)
    pub_time = models.DateTimeField('time entered')
    def __str__(self):
        return self.topic_input

    def was_published_recently(self):
        return self.pub_time >= timezone.now() - datetime.timedelta(days=1)

    
class Data(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField()
    def __str__(self):
        return self.title, self.link