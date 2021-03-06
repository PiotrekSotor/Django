from django.conf.urls import url, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login, name='login'),

    url(r'^task_edit/(?P<task_id>[\S]+)/$', views.task_edit, name='task_edit'),
    url(r'^task_erase/(?P<task_id>[\S]+)/$', views.task_erase, name='task_erase'),
    url(r'^task_submit_form/$', views.task_submit_form, name='task_submit_form'),
    url(r'^tasks/', views.tasks, name='tasks'),

    url(r'^worker_edit/(?P<worker_id>[\S]+)/$', views.worker_edit, name='worker_edit'),
    url(r'^worker_erase/(?P<worker_id>[\S]+)/$', views.worker_erase, name='worker_erase'),
    url(r'^worker_submit_form/$', views.worker_submit_form, name='worker_submit_form'),
    url(r'^workers/', views.workers, name='workers'),

    url(r'^job_edit/(?P<job_id>[\S]+)/$', views.job_edit, name='job_edit'),
    url(r'^job_erase/(?P<job_id>[\S]+)/$', views.job_erase, name='job_erase'),
    url(r'^job_submit_form/$', views.job_submit_form, name='job_submit_form'),
    url(r'^jobs/', views.jobs, name='jobs'),

    url(r'^aggregator/', views.aggregator, name='aggregator'),
    url(r'^aggregator_form/', views.aggregator_form, name='aggregator_form'),


    url(r'^accounts/login/$', auth_views.login, name='login2'),

]
app_name = 'proj_2'



