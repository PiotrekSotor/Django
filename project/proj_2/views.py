from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world, this is index")

# Create your views here.
