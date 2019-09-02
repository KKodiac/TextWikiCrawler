from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_input = models.CharField(max_length=200)
    pub_time = models.DateTimeField('time entered')
    

