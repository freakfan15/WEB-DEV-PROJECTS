from django.shortcuts import render
from django.conf import settings

# Create your views here.
def index(request):
    context ={
        'name': settings.DATA['NAME'],
        'about_me' :settings.DATA['ABOUT_ME']
    }
    response = render(request, 'main/index.html', context)
    return response

def projects(request):
    context ={
        'projects': settings.DATA['PROJECTS']
    }
    response = render(request, 'main/projects.html', context)
    return response

def blogs(request):
    context ={}
    response = render(request, 'main/blogs.html', context)
    return response

