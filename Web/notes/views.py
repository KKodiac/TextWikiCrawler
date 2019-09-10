from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

import sqlite3

from .models import Topic, Data

JSONPATH = '../../Crawler/DataFile/'

# Create your views here.
def results(request, topic):
    show_data = Data.objects.all()
    template = loader.get_template('notes/results.html')
    context = {
        'show_data': show_data,
        'url_context': request.GET.get('results')
    }   
    
    return HttpResponse(template.render(context, request))

def index(request, topic):
    show_topic = Topic.objects.all()
    print(show_topic)
    print(id)
    template = loader.get_template('notes/index.html')
    context = {
        'show_topic': show_topic,
    }
    
    return HttpResponse(template.render(context, request))

