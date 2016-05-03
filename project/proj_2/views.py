from django.shortcuts import render, redirect
from django.http import HttpResponse, request, request
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.template import Context
from .models import Task

# @login_required
def index(request):
    return render(request, 'proj_2/index.html')


def login(request):
    if request.user.is_authenticated():
        redirect('index.html')
    return HttpResponse("Hello world, this is login")

# Create your views here.

def tasks(request):
    tasks_to_render = Task.objects.all()

    context = {'tasks': tasks_to_render}
    print (context)
    return render(request, 'proj_2/tasks.html', context)

def task_edit(request, task_code):
    return HttpResponse("task edit %s" % (task_code))

def task_erase(request, task_code):
    return HttpResponse("task erase %s" % (task_code))

def workers(request):
    # workers_to_render = {'task_code': 'PIEL', 'wage': '1.25'}
    # context['tasks'] = tasks_to_render
    return HttpResponse("workers")

def jobs(request):
    # workers_to_render = {'task_code': 'PIEL', 'wage': '1.25'}
    # context['tasks'] = tasks_to_render
    return HttpResponse("jobs")