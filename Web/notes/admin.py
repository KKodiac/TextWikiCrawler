from django.contrib import admin

# Register your models here.
from .models import Topic,Data

admin.site.register(Topic)
admin.site.register(Data)
