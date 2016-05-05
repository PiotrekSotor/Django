from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, request, request
from .forms import TaskForm
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.template import Context

from .models import Task, Worker, Job


# @login_required
def index(request):
    return render(request, 'proj_2/index.html')


def login(request):
    if request.user.is_authenticated():
        redirect('index.html')
    return HttpResponse("Hello world, this is login")


# Create your views here.

def tasks(request, message='', context={}):
    tasks_to_render = Task.objects.all()
    context['tasks'] = tasks_to_render
    if message:
        context['message'] = message
    if not 'form' in context:
        context['form'] = TaskForm
    print (context)
    return render(request, 'proj_2/tasks.html', context)


def task_submit_form(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            if 'id' in form.cleaned_data and not form.cleaned_data['id'] == '':
                task = get_object_or_404(Task, pk=form.cleaned_data['id'])
                task.wage = form.cleaned_data['wage']
                task.save()
            else:
                task = Task()
                task.task_code = form.cleaned_data['task_code']
                task.wage = form.cleaned_data['wage']
                task.save()
            print(task.__str__())


            return tasks(request, 'Success')
        else:
            print ('INVALID')
            print (form.errors)
    return tasks(request, 'Failed')


def task_edit(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    initials = {'task_code': task.task_code, 'wage': task.wage, 'id': task.id}
    print(initials)
    form = TaskForm(initial=initials)
    form.fields['task_code'].widget.attrs['readonly']=True
    # form.task_code = task.task_code
    # form.id = task.id
    # form.wage = task.wage
    context = {'form': form, 'edit': 1}
    return tasks(request, context=context)


def task_erase(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return tasks(request, 'deleted task')


def worker_edit(request, worker_id):
    worker = get_object_or_404(Worker, pk=worker_id)
    return HttpResponse("worker edit %s" % (worker))


def worker_erase(request, worker_id):
    worker = get_object_or_404(Worker, pk=worker_id)
    worker.delete()
    return workers(request, 'deleted worker')


# def worker_submit_form(request):
#

def workers(request, message=''):
    workers_to_render = Worker.objects.all()
    context = {'workers': workers_to_render}
    if message:
        context['message'] = message
    return render(request, 'proj_2/workers.html', context)


def job_edit(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return HttpResponse("job edit %s" % (job))


def job_erase(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    job.delete()
    return jobs(request, 'deleted job')


def jobs(request, message=''):
    jobs_to_render = Job.objects.all()
    context = {'jobs': jobs_to_render}
    if message:
        context['message'] = message
    return render(request, "proj_2/jobs.html", context)
