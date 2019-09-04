from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Topic

# Create your views here.
def index(request, id):
    return HttpResponse("You're looking at the main page for TOPIC %s" % id)

def results(request, id):
    show_topic = Topic.objects.all()
    template = loader.get_template('notes/results.html')
    context = {
        'show_topic': show_topic,
    }
    
    return HttpResponse(template.render(context, request))

