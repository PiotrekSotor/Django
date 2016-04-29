from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import  login_required


@login_required(login_url='login')
def index(request):
    return HttpResponse("Hello world, this is index %s" % (settings.LOGIN_URL))

def login(request):
    if request.user.is_authenticated():
        redirect('index.html')
    return HttpResponse("Hello world, this is index")
# Create your views here.
