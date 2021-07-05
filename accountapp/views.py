from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(requests):
    return render(requests, 'accountapp/hello_world.html')