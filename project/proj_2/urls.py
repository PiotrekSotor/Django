from django.conf.urls import url, include
from django.conf import settings
import registration
from django.contrib.auth import views as auth_views
from . import views

app_name = 'proj_2'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^task_edit/(?P<task_code>[\S]+)/$', views.task_edit, name='task_edit'),
    url(r'^task_erase/(?P<task_code>[\S]+)/$', views.task_erase, name='task_erase'),
    url(r'^tasks/', views.tasks, name='tasks'),
    url(r'^workers/', views.workers, name='workers'),
    url(r'^jobs/', views.jobs, name='jobs'),
    url(r'^accounts/login/$', auth_views.login, name='login2'),

]
