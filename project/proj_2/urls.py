from django.conf.urls import url
from django.conf import settings
from . import views

app_name = 'proj_2'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'login/$', views.login, name="login"),
]
