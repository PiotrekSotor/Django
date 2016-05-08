from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, request, request
from .forms import TaskForm, WorkerForm, JobForm, AggregatorForm
from django.db import IntegrityError
import datetime
from datetime import date
from django.db.models import Sum, Count
import collections
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
    tasks_to_render = Task.objects.order_by("task_code")
    context['tasks'] = tasks_to_render
    if message:
        context['message'] = message
    if not 'form' in context:
        context['form'] = TaskForm()
    print(context)
    return render(request, 'proj_2/tasks.html', context)


def task_submit_form(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            if 'id' in form.cleaned_data and not form.cleaned_data['id'] == '':
                task = get_object_or_404(Task, pk=form.cleaned_data['id'])
            else:
                task = Task()
                task.task_code = form.cleaned_data['task_code'].upper()
            task.wage = form.cleaned_data['wage']
            try:
                task.save()
            except IntegrityError as e:
                return tasks(request, message='Błąd!   Powielenie kodu czynności')
            print(task.__str__())

            return tasks(request, 'Success')
        else:
            print('INVALID')
            print(form.errors)
    return tasks(request, 'Failed')


def task_edit(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    initials = {'task_code': task.task_code, 'wage': task.wage, 'id': task.id}
    form = TaskForm(initial=initials)
    form.fields['task_code'].widget.attrs['readonly'] = True
    context = {'form': form, 'edit': 1}
    return tasks(request, context=context)


def task_erase(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return tasks(request, 'deleted task')


def worker_submit_form(request):
    if request.method == 'POST':
        form = WorkerForm(request.POST)
        if form.is_valid():
            if 'id' in form.cleaned_data and not form.cleaned_data['id'] == '':
                worker = get_object_or_404(Worker, pk=form.cleaned_data['id'])
            else:
                worker = Worker()
            worker.name = form.cleaned_data['name'].upper()
            worker.save()
            return workers(request, 'Success')
    return workers(request, 'Failed')


def worker_edit(request, worker_id):
    worker = get_object_or_404(Worker, pk=worker_id)
    print(worker)
    initials = {'name': worker.name, 'id': worker.id}
    form = WorkerForm(initial=initials)
    context = {'form': form, 'edit': 1}
    return workers(request, context=context)


def worker_erase(request, worker_id):
    worker = get_object_or_404(Worker, pk=worker_id)
    worker.delete()
    return workers(request, 'deleted worker')


def workers(request, message='', context={}):
    workers_to_render = Worker.objects.all()
    context['workers'] = workers_to_render
    if message:
        context['message'] = message
    if not 'form' in context:
        context['form'] = WorkerForm(initial={'date': datetime.date.today()})

    return render(request, 'proj_2/workers.html', context)


def job_submit_form(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        print(form.data)
        if form.data['task_code_combobox']:
            task_code_id = form.data['task_code_combobox']
        elif form.data['task_code_field']:
            task_code_id = 1
        else:
            return jobs(request, 'Brak kodu czynności')

        if form.data['worker_combobox']:
            worker_id = form.data['worker_combobox']
        elif form.data['worker_field']:
            worker_id = 1
        else:
            return jobs(request, 'Brak pracownika')

        if form.data['count']:
            count = form.data['count']
        else:
            return jobs(request, 'Brak ilości')

        if form.data['date']:
            date = form.data['date']
        else:
            date = datetime.date.today()

        if 'id' in form.data and not form.data['id'] == '':
            job = get_object_or_404(Job, pk=form.data['id'])
            job.count = count
            job.date = date
            job.person_id = worker_id
            job.task_code_id = task_code_id
        else:
            job = Job(task_code_id=task_code_id, person_id=worker_id, count=count, date=date)
        job.save()

        return jobs(request, 'Success')
    return jobs(request, 'Failed')


def job_edit(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    print(job)
    initials = {'worker_combobox': job.person_id,
                'task_code_combobox': job.task_code_id,
                'count': job.count,
                'date': job.date,
                'id': job.id}
    form = JobForm(initial=initials)
    context = {'form': form, 'edit': 1}
    return jobs(request, context=context)


def job_erase(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    job.delete()
    return jobs(request, 'deleted job')


def jobs(request, message='', context={}):
    jobs_to_render = Job.objects.all()
    context['jobs'] = jobs_to_render
    if message:
        context['message'] = message
    if not 'form' in context:
        context['form'] = JobForm()
    return render(request, "proj_2/jobs.html", context)


def aggregator(request, message='', context={}):
    if message:
        context['message'] = message
    if 'forn' not in context:
        context['form'] = AggregatorForm(
            initial={'startdate': date(date.today().year, date.today().month, 1), 'enddate': date.today()})
    return render(request, "proj_2/aggregator.html", context)


def aggregator_form(request):
    if request.method == 'GET':

        form = AggregatorForm(request.GET)
        if form.is_valid():
            print('valided', form.cleaned_data)
            context = {}
            workers = []
            task_summary = collections.defaultdict(dict)
            if form.cleaned_data['all_workers']:
                workers_to_search = Worker.objects.order_by("name")
            else:
                workers_to_search = form.cleaned_data['workers']
            if form.cleaned_data['all_tasks']:
                all = Task.objects.order_by("task_code")
                tasks_to_search = []
                for a in all:
                    tasks_to_search += [a.id]
            else:
                all = form.cleaned_data['tasks']
                tasks_to_search = []
                for a in all:
                    task = Task.objects.get(task_code=a)
                    tasks_to_search += [task.id]
            print('Workers to search: ', workers_to_search)
            print('Tasks to search:   ', tasks_to_search)
            for w in workers_to_search:
                sum_overall = 0
                worker = {'name': w}
                tasks_ = []
                res = Job.objects.filter(person__name=w) \
                    .filter(date__lte=form.cleaned_data['enddate']) \
                    .filter(date__gte=form.cleaned_data['startdate']) \
                    .values('task_code') \
                    .annotate(Count('count'), Sum('count'))
                print('Results: ', res)
                for r in res:
                    if not r['task_code'] in tasks_to_search:
                        continue
                    count = r['count__count']
                    task_code_id = r['task_code']
                    sum_of_count = r['count__sum']
                    task = get_object_or_404(Task, pk=task_code_id)
                    sum = sum_of_count * task.wage

                    if 'task_code' not in task_summary[task.task_code]:
                        task_summary[task.task_code]['task_code'] = task.task_code

                    if 'count' in task_summary[task.task_code]:
                        task_summary[task.task_code]['count'] += count
                    else:
                        task_summary[task.task_code]['count'] = count

                    if 'sum_of_count' in task_summary[task.task_code]:
                        task_summary[task.task_code]['sum_of_count'] += sum_of_count
                    else:
                        task_summary[task.task_code]['sum_of_count'] = sum_of_count

                    if 'sum' in task_summary[task.task_code]:
                        task_summary[task.task_code]['sum'] += sum
                    else:
                        task_summary[task.task_code]['sum'] = sum

                    # task = Task.objects.get(task_code=task_code_id)
                    sum_overall += sum
                    tasks_ += [{'task_code': task.task_code, 'count': count, 'sum': sum, 'sum_of_count': sum_of_count}]
                worker['tasks'] = tasks_
                worker['sum_overall'] = sum_overall
                workers += [worker]
            final_task_summary = []
            for t in task_summary:
                final_task_summary += [{'task_code': task_summary[t]['task_code'],
                                        'count': task_summary[t]['count'],
                                        'sum_of_count':task_summary[t]['sum_of_count'],
                                        'sum':task_summary[t]['sum']}]
            context['workers'] = workers
            print(task_summary)
            context['tasks_summary'] = final_task_summary
            return aggregator(request, message='Alles Gut', context=context)
        else:
            print(form.errors)
            return aggregator(request, message='Not valid')
    return aggregator(request, message='Not GET')

#
# class TaskInSummary
#     task_code = ''
#     count = 0
#     sum = 0
#     sum_of_count = 0
